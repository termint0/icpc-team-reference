import glob
import os

import yaml

ROOT = os.path.dirname(os.path.abspath(__file__))


def test_every_algorithm_folder_is_complete():
    folders = sorted({os.path.dirname(f) for f in glob.glob(f"{ROOT}/**/*.yaml", recursive=True)})
    assert len(folders) == 97
    for d in folders:
        ys = glob.glob(f"{d}/*.yaml")
        code = [f for f in glob.glob(f"{d}/*.py") if not os.path.basename(f).startswith("test_")]
        tests = glob.glob(f"{d}/test_*.py")
        assert len(ys) == len(code) == len(tests) == 1, d
        stem = os.path.splitext(os.path.basename(ys[0]))[0]
        assert os.path.basename(code[0]) == stem + ".py" and os.path.basename(tests[0]) == f"test_{stem}.py"
        doc = yaml.safe_load(open(ys[0]))
        assert list(doc) == ["name", "description", "time", "memory"], d
        t = doc["time"]
        assert (isinstance(t, str) and t) or (isinstance(t, dict) and t and all(isinstance(v, str) for v in t.values())), d
        assert all(isinstance(doc[k], str) and doc[k].strip() for k in ("name", "description", "memory")), d
