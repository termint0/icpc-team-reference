#!/usr/bin/env python3
"""
Compile a directory of annotated Python sources into a compact, two-column
LaTeX document and PDF.

Layout expected:
    sources/
      graphs/                  -> \\section
        bfs/                   -> \\subsection
          dijkstra/            -> \\subsubsection (leaf: one .py + one .yaml/.yml/.json)
            dijkstra.py
            info.yaml          (name, description, time, memory)

Depth 1 = section, 2 = subsection, 3 = subsubsection, 4 = paragraph,
5+ = subparagraph.

Usage:
    python build_book.py [sources_dir] [-o out_name] [--cover cover.tex]
        [--preamble extra.tex] [--columns 2] [--engine pdflatex|xelatex|lualatex]
        [--title "My Algorithms"] [--institution "Name"] [--no-toc] [--tex-only]

--cover     A .tex *fragment* (no \\documentclass / \\begin{document}) that is
            \\input as the first page, replacing the default title. A page
            break follows it.
--preamble  A .tex file inserted into the preamble (extra packages, macros
            used by the cover, ...).

Requires PyYAML only for YAML metadata (pip install pyyaml).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

META_EXTS = {".yaml", ".yml", ".json"}
HEADINGS = ["section", "subsection", "subsubsection", "paragraph", "subparagraph"]
TABSIZE = 4

KEYS = {
    "name": ["name", "title"],
    "description": ["description", "desc", "summary"],
    "time": ["time", "time_complexity", "time_complexity_big_o", "runtime"],
    "memory": ["memory", "mem", "space", "space_complexity", "memory_complexity"],
}

_ESC = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def esc(text) -> str:
    return "".join(_ESC.get(c, c) for c in str(text))


def pretty(dirname: str) -> str:
    return dirname.replace("_", " ").replace("-", " ").strip().title()


def complexity(value) -> str:
    s = str(value).strip()
    if "$" in s:
        return s
    if re.match(r"^[OΘΩoθ]\s*\(", s) or re.match(r"^(Theta|Omega)\s*\(", s):
        m = s.replace("Θ", r"\Theta").replace("Ω", r"\Omega")
        m = re.sub(r"\blog\b", r"\\log", m)
        m = re.sub(r"\bsqrt\(([^)]*)\)", r"\\sqrt{\1}", m)
        m = m.replace("*", r" \cdot ")
        m = re.sub(r"\^\(([^)]*)\)", r"^{\1}", m)
        m = m.replace("%", r"\%").replace("#", r"\#").replace("&", r"\&")
        return f"${m}$"
    return esc(s)


def fmt_complexity(value) -> str:
    """A complexity is a string, a list of strings, or a dict {label: complexity}."""
    if isinstance(value, dict):
        return ", ".join(f"\\textit{{{esc(k)}}}: {fmt_complexity(v)}"
                         for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return ", ".join(fmt_complexity(v) for v in value)
    return complexity(value)


def load_meta(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        data = json.loads(raw)
    else:
        if yaml is None:
            sys.exit(f"PyYAML is needed to read {path} (pip install pyyaml)")
        data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        sys.exit(f"{path}: expected a mapping at top level")
    lowered = {str(k).lower(): v for k, v in data.items()}
    return {c: next((lowered[a] for a in al if a in lowered), None)
            for c, al in KEYS.items()}


def classify(directory: Path):
    py, meta, subs = [], [], []
    for p in sorted(directory.iterdir()):
        if p.name.startswith(".") or p.name == "__pycache__":
            continue
        if p.is_dir():
            subs.append(p)
        elif p.suffix == ".py":
            py.append(p)
        elif p.suffix in META_EXTS:
            meta.append(p)
    return py, meta, subs


def heading(depth: int, title: str) -> str:
    return f"\\Needspace{{5\\baselineskip}}\\{HEADINGS[min(depth, len(HEADINGS)) - 1]}{{{title}}}\n"


def max_line_chars(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    return max((len(l.expandtabs(TABSIZE).rstrip()) for l in text.splitlines()),
               default=1) or 1


def render_leaf(directory: Path, py: Path, meta_path: Path, depth: int,
                tex_dir: Path) -> str:
    meta = load_meta(meta_path)
    out = [heading(depth, esc(meta["name"] or pretty(directory.name)))]

    info = []
    if meta["time"] is not None:
        info.append(f"\\textbf{{Time:}} {fmt_complexity(meta['time'])}")
    if meta["memory"] is not None:
        info.append(f"\\textbf{{Memory:}} {fmt_complexity(meta['memory'])}")
    if info:
        out.append("{\\small " + r"\quad ".join(info) + "}\\par\n")
    if meta["description"]:
        out.append("{\\small " + esc(str(meta["description"]).strip()) + "}\\par\n")

    try:
        rel = py.resolve().relative_to(tex_dir.resolve())
    except ValueError:
        rel = py.resolve()
    out.append(f"\\codefile{{{max_line_chars(py)}}}{{{rel.as_posix()}}}\n\n")
    return "".join(out)


def walk(directory: Path, depth: int, tex_dir: Path, warnings: list) -> str:
    py, meta, subs = classify(directory)
    if not subs:
        if len(py) != 1 or len(meta) != 1:
            warnings.append(
                f"{directory}: leaf should have exactly 1 .py and 1 yaml/json "
                f"(found {len(py)} .py, {len(meta)} meta) - skipped")
            return ""
        return render_leaf(directory, py[0], meta[0], depth, tex_dir)

    if py or meta:
        warnings.append(f"{directory}: has subdirectories AND files; files ignored")
    body = "".join(walk(s, depth + 1, tex_dir, warnings) for s in subs)
    if not body:
        return ""
    return heading(depth, esc(pretty(directory.name))) + body


PREAMBLE = r"""\documentclass[8pt,a4paper]{extarticle}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{courier}
\usepackage[margin=1.3cm,top=1.9cm,headheight=10pt,headsep=7pt]{geometry}
\usepackage{fancyhdr}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{multicol}
\usepackage{needspace}
\usepackage[compact]{titlesec}
\usepackage[hidelinks]{hyperref}
\usepackage{listings}
\usepackage[listings,breakable,skins]{tcolorbox}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1pt}
\setlength{\columnsep}{0.6cm}
\setlength{\columnseprule}{0.2pt}
\titleformat{\section}{\normalfont\large\bfseries}{\thesection}{0.5em}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries}{\thesubsection}{0.5em}{}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries}{\thesubsubsection}{0.5em}{}
\titlespacing*{\section}{0pt}{6pt}{2pt}
\titlespacing*{\subsection}{0pt}{4pt}{2pt}
\titlespacing*{\subsubsection}{0pt}{3pt}{1pt}
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}

\lstdefinestyle{pycode}{
  language=Python,
  basicstyle=\ttfamily\fontsize{6.5}{7.5}\selectfont,
  keywordstyle=\color{blue!70!black}\bfseries,
  commentstyle=\color{green!40!black}\itshape,
  stringstyle=\color{red!60!black},
  breaklines=true, showstringspaces=false, tabsize=4,
  columns=fixed, keepspaces=true,
  literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1
           {→}{{$\rightarrow$}}1 {≤}{{$\leq$}}1 {≥}{{$\geq$}}1,
}

% Width of one monospaced character in the code font.
\newlength{\codecw}
\settowidth{\codecw}{\ttfamily\fontsize{6.5}{7.5}\selectfont 0}
\newlength{\codew}
% \codefile{<longest line in chars>}{<path>}: box hugs the code, capped at column width.
\newcommand{\codefile}[2]{%
  \setlength{\codew}{\dimexpr \numexpr#1+1\relax\codecw + 5pt\relax}%
  \ifdim\codew>\linewidth\setlength{\codew}{\linewidth}\fi
  \tcbinputlisting{listing engine=listings, listing file={#2}, listing only,
    listing options={style=pycode},
    enhanced jigsaw, breakable, width=\codew,
    boxrule=0.3pt, colframe=black!35, colback=black!3,
    left=2pt, right=2pt, top=1pt, bottom=1pt, boxsep=0pt, arc=0pt,
    before skip=2pt, after skip=3pt}%
}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sources", nargs="?", default="sources", type=Path)
    ap.add_argument("-o", "--output", default="algorithms")
    ap.add_argument("--title", default="Algorithm Reference")
    ap.add_argument("--institution", default="",
                    help="name shown in the top-left of every page")
    ap.add_argument("--cover", type=Path, help=".tex fragment used as first page")
    ap.add_argument("--preamble", type=Path, help=".tex file added to the preamble")
    ap.add_argument("--columns", type=int, default=2)
    ap.add_argument("--no-toc", action="store_true")
    ap.add_argument("--engine", default="pdflatex",
                    choices=["pdflatex", "xelatex", "lualatex"])
    ap.add_argument("--tex-only", action="store_true")
    args = ap.parse_args()

    root = args.sources
    if not root.is_dir():
        sys.exit(f"{root} is not a directory")
    for f in (args.cover, args.preamble):
        if f and not f.is_file():
            sys.exit(f"{f} not found")

    tex_path = Path(f"{args.output}.tex").resolve()
    tex_dir = tex_path.parent
    warnings: list = []

    body = "".join(walk(d, 1, tex_dir, warnings)
                   for d in sorted(p for p in root.iterdir()
                                   if p.is_dir() and not p.name.startswith(".")))

    def inc(p: Path) -> str:
        try:
            return p.resolve().relative_to(tex_dir).as_posix()
        except ValueError:
            return p.resolve().as_posix()

    doc = [PREAMBLE]
    if args.preamble:
        doc.append(f"\\input{{{inc(args.preamble)}}}\n")
    doc.append(f"\\title{{{esc(args.title)}}}\n\\author{{}}\n\\date{{\\today}}\n")
    doc.append(
        "\\pagestyle{fancy}\\fancyhf{}\n"
        f"\\fancyhead[L]{{\\small {esc(args.institution)}}}\n"
        "\\fancyhead[R]{\\small\\thepage}\n"
        "\\renewcommand{\\headrulewidth}{0.2pt}\n")
    doc.append("\\begin{document}\n")
    if args.cover:
        doc.append(f"\\thispagestyle{{empty}}\n\\input{{{inc(args.cover)}}}\n\\clearpage\n")
    else:
        doc.append("\\begingroup\\centering{\\Large\\bfseries "
                   f"{esc(args.title)}\\par}}\\vspace{{2pt}}"
                   "{\\small\\today\\par}\\endgroup\\vspace{4pt}\n")
    n = max(args.columns, 1)
    if n > 1:
        doc.append(f"\\begin{{multicols}}{{{n}}}\n")
    if not args.no_toc:
        doc.append("{\\small\\setlength{\\parskip}{0pt}\\tableofcontents}\n")
    doc.append(body)
    if n > 1:
        doc.append("\\end{multicols}\n")
    doc.append("\\end{document}\n")
    tex_path.write_text("".join(doc), encoding="utf-8")
    print(f"wrote {tex_path}")
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)

    if args.tex_only:
        return
    if shutil.which(args.engine) is None:
        sys.exit(f"{args.engine} not found. Install TeX Live/MiKTeX, "
                 f"or rerun with --tex-only.")
    cmd = [args.engine, "-interaction=nonstopmode", "-halt-on-error", tex_path.name]
    for _ in range(2):
        r = subprocess.run(cmd, cwd=tex_dir, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:], file=sys.stderr)
            sys.exit(f"{args.engine} failed; see {tex_path.with_suffix('.log')}")
    for ext in (".aux", ".toc", ".out"):
        tex_path.with_suffix(ext).unlink(missing_ok=True)
    print(f"wrote {tex_path.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
