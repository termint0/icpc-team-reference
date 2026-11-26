# Index

| Folder | Name | Time | Memory |
|---|---|---|---|
| `algebra/linear-algebra/berlekamp-massey/` | Berlekamp-Massey | O(n^2) | O(n) |
| `algebra/linear-algebra/gauss-float/` | Gaussian elimination (floating point) | O(n*m*min(n,m)) | O(n*m) |
| `algebra/linear-algebra/gauss-mod/` | Gaussian elimination mod p | O(n*m*min(n,m)) | O(n*m) |
| `algebra/linear-algebra/matrix-exponentiation/` | Matrix exponentiation | mat_mul: O(n^3); mat_pow: O(n^3*log(e)) | O(n^2) |
| `algebra/linear-algebra/simplex/` | Simplex (linear programming) | per pivot: O(m*n); worst case: exponential | O(m*n) |
| `algebra/number-theory/binomial-mod-p/` | Binomial coefficients mod a prime | build: O(N); query: O(1) | O(N) |
| `algebra/number-theory/crt/` | Chinese remainder theorem | crt: O(log(m)); crt_list: O(k*log(M)) | O(1) |
| `algebra/number-theory/euler-phi/` | Euler's totient function | O(sqrt(n)) | O(1) |
| `algebra/number-theory/inclusion-exclusion/` | Inclusion-exclusion | O(2^k) | O(k) |
| `algebra/number-theory/linear-sieve/` | Linear sieve (smallest prime factor) | build: O(n); factorize: O(log(x)) | O(n) |
| `algebra/number-theory/lucas/` | Lucas' theorem | precompute: O(p); query: O(log_p(n)) | O(p) |
| `algebra/number-theory/miller-rabin/` | Miller-Rabin primality test | O(k*log(n)) | O(1) |
| `algebra/number-theory/mod-inverse/` | Modular inverse (extended Euclid) | O(log(m)) | O(1) |
| `algebra/number-theory/mod-pow/` | Modular exponentiation | O(log(e)) | O(1) |
| `algebra/number-theory/pollard-rho/` | Pollard's rho factorisation | expected: O(n^(1/4)) | O(log(n)) |
| `algebra/number-theory/sieve/` | Sieve of Eratosthenes | O(n*log(log(n))) | O(n) |
| `algebra/polynomial/fft/` | Fast Fourier transform | O(n*log(n)) | O(n) |
| `algebra/polynomial/fwht/` | Fast Walsh-Hadamard transform | O(n*log(n)) | O(n) |
| `algebra/polynomial/ntt/` | Number theoretic transform | O(n*log(n)) | O(n) |
| `datastructures/line-containers/convex-hull-trick/` | Convex hull trick (monotone slopes) | add: O(1) amortized; query: O(log(n)) | O(n) |
| `datastructures/line-containers/li-chao-tree/` | Li Chao tree | add_line: O(log(C)); query: O(log(C)) | O(n) |
| `datastructures/monotone/monotone-deque/` | Monotone deque (sliding window) | O(n) | O(k) |
| `datastructures/monotone/monotone-stack/` | Monotone stack | O(n) | O(n) |
| `datastructures/range-queries/lazy-segment-tree/` | Segment tree with lazy propagation | build: O(n); update: O(log(n)); query: O(log(n)) | O(n) |
| `datastructures/range-queries/merge-sort-tree/` | Merge sort tree | build: O(n*log(n)); query: O(log^2(n)) | O(n*log(n)) |
| `datastructures/range-queries/mo-algorithm/` | Mo's algorithm | O((n + q)*sqrt(n)*T) | O(n + q) |
| `datastructures/range-queries/persistent-segment-tree/` | Persistent segment tree | add: O(log(n)); query: O(log(n)); kth: O(log(n)) | O(n + q*log(n)) |
| `datastructures/range-queries/segment-tree-beats/` | Segment tree beats | build: O(n); chmin: O(log(n)) amortized; sum: O(log(n)); max: O(log(n)) | O(n) |
| `datastructures/range-queries/segment-tree/` | Segment tree (iterative) | build: O(n); update: O(log(n)); query: O(log(n)) | O(n) |
| `datastructures/range-queries/sqrt-decomposition/` | Sqrt decomposition | build: O(n); add: O(sqrt(n)); sum: O(sqrt(n)); get: O(1) | O(n) |
| `datastructures/sets-and-tries/ordered-set/` | Order statistic set (pb_ds replacement) | O(sqrt(n)) per operation | O(n) |
| `datastructures/sets-and-tries/trie/` | Trie | O(L) per operation | O(total length) |
| `datastructures/sets-and-tries/xor-trie/` | XOR trie | insert: O(bits); erase: O(bits); max_xor: O(bits) | O(n*bits) |
| `datastructures/trees/centroid-decomposition/` | Centroid decomposition | O(n*log(n)) | O(n) |
| `datastructures/trees/hld/` | Heavy-light decomposition | build: O(n); path: O(log(n)); lca: O(log(n)); path query with segment tree: O(log^2(n)) | O(n) |
| `datastructures/trees/implicit-treap/` | Implicit treap | insert: O(log(n)) expected; erase: O(log(n)) expected; reverse: O(log(n)) expected; sum: O(log(n)) expected | O(n) |
| `datastructures/trees/link-cut-tree/` | Link-cut tree | link: O(log(n)) amortized; cut: O(log(n)) amortized; connected: O(log(n)) amortized; path_sum: O(log(n)) amortized | O(n) |
| `dp/classic/bitmask-dp/` | Bitmask DP (assignment problem) | O(2^n * n) | O(2^n) |
| `dp/classic/digit-dp/` | Digit DP | O(len(N) * states * base) | O(states) |
| `dp/classic/edit-distance/` | Edit distance (Levenshtein) | O(n*m) | O(m) |
| `dp/classic/knapsack/` | Knapsack (0/1, unbounded, bounded) | knapsack_01: O(n*W); knapsack_unbounded: O(n*W); knapsack_bounded: O(n*W*log(c)) | O(W) |
| `dp/classic/lcs/` | Longest common subsequence | O(n*m) | O(n*m) |
| `dp/classic/lis/` | Longest increasing subsequence | O(n*log(n)) | O(n) |
| `dp/classic/sos-dp/` | Sum over subsets (SOS DP) | O(2^b * b) | O(2^b) |
| `dp/combinatorics/burnside/` | Burnside's lemma | O(|G|*n) | O(n) |
| `dp/combinatorics/gray-code/` | Gray codes | gray: O(1); gray_inverse: O(log(n)) | O(1) |
| `dp/combinatorics/permutations/` | Permutation utilities | next_permutation: O(n); kth_permutation: O(n^2); permutation_rank: O(n^2); permutation_inverse: O(n); permutation_cycles: O(n) | O(n) |
| `dp/combinatorics/special-numbers/` | Catalan, Stirling and Bell numbers | catalan: O(n); stirling tables: O(n^2); bell: O(n^2) | O(n^2) |
| `dp/combinatorics/sprague-grundy/` | Sprague-Grundy numbers | O(N * cost of options) | O(N) |
| `dp/optimization/dc-optimization/` | Divide and conquer optimisation | O(K*n*log(n)) | O(n) |
| `dp/optimization/knuth-optimization/` | Knuth optimisation | O(n^2) | O(n^2) |
| `dp/search/binary-search-answer/` | Binary search on the answer | O(log(range)) evaluations of pred | O(1) |
| `dp/search/meet-in-the-middle/` | Meet in the middle (subset sums) | count: O(2^(n/2)); closest: O(2^(n/2) * n) | O(2^(n/2)) |
| `dp/search/ternary-search/` | Ternary search | O(log(range)) evaluations of f | O(1) |
| `dp/utilities/coordinate-compression/` | Coordinate compression | O(n*log(n)) | O(n) |
| `dp/utilities/fast-io/` | Fast input | O(input size) | O(input size) |
| `dp/utilities/random-hash/` | Randomisation and hashing utilities | O(1) per call (shuffle: O(n)) | O(1) |
| `geometry/circle-intersection/` | Circle intersection | O(1) | O(1) |
| `geometry/closest-pair/` | Closest pair of points | O(n*log^2(n)) | O(n) |
| `geometry/convex-hull/` | Convex hull (monotone chain) | O(n*log(n)) | O(n) |
| `geometry/half-plane-intersection/` | Half-plane intersection | O(n*log(n)) | O(n) |
| `geometry/line-intersection/` | Line intersection | O(1) | O(1) |
| `geometry/min-enclosing-circle/` | Minimum enclosing circle | expected: O(n) | O(n) |
| `geometry/point-in-polygon/` | Point in polygon | O(n) | O(1) |
| `geometry/polygon-area/` | Polygon area | O(n) | O(1) |
| `geometry/primitives/` | Geometry primitives | O(1) | O(1) |
| `geometry/rotating-calipers/` | Rotating calipers (convex diameter) | O(n) | O(1) |
| `geometry/segment-intersection/` | Segment intersection | O(1) | O(1) |
| `graphs/connectivity/bridges-bcc/` | Bridges, articulation points, biconnected components | O(V + E) | O(V + E) |
| `graphs/connectivity/two-sat/` | 2-SAT | O(n + clauses) | O(n + clauses) |
| `graphs/flow/dinic/` | Dinic's max flow | general: O(V^2*E); unit capacities: O(E*sqrt(V)) | O(V + E) |
| `graphs/flow/min-cost-flow/` | Min-cost max-flow | O(F*V*E) | O(V + E) |
| `graphs/flow/stoer-wagner/` | Stoer-Wagner global min cut | O(V^3) | O(V^2) |
| `graphs/matching/blossom/` | Edmonds' blossom (general matching) | O(V^3) | O(V + E) |
| `graphs/matching/hopcroft-karp/` | Hopcroft-Karp bipartite matching | O(E*sqrt(V)) | O(V + E) |
| `graphs/paths-and-cycles/euler-path/` | Euler path / circuit (Hierholzer) | O(V + E) | O(V + E) |
| `graphs/paths-and-cycles/tsp-bitmask/` | Bitmask TSP | O(2^n * n^2) | O(2^n * n) |
| `graphs/shortest-paths/bellman-ford/` | Bellman-Ford | O(V*E) | O(V) |
| `graphs/shortest-paths/floyd-warshall/` | Floyd-Warshall | O(V^3) | O(V^2) |
| `graphs/shortest-paths/johnson/` | Johnson's algorithm | O(V*E*log(V)) | O(V^2) |
| `graphs/shortest-paths/spfa/` | SPFA (queue-based Bellman-Ford) | O(V*E) | O(V) |
| `graphs/spanning-trees/directed-mst/` | Directed MST (Chu-Liu/Edmonds) | O(V*E) | O(V + E) |
| `graphs/spanning-trees/prim/` | Prim's algorithm | O(E*log(V)) | O(V + E) |
| `graphs/traversal/bfs-01/` | 0-1 BFS | O(V + E) | O(V) |
| `graphs/traversal/bfs/` | Breadth-first search | O(V + E) | O(V) |
| `graphs/traversal/dfs/` | Depth-first search (iterative) | O(V + E) | O(V) |
| `graphs/tree/binary-lifting/` | Binary lifting (k-th ancestor, LCA) | build: O(n*log(n)); kth_ancestor: O(log(n)); lca: O(log(n)) | O(n*log(n)) |
| `graphs/tree/euler-tour/` | Euler tour of a tree | O(n) | O(n) |
| `graphs/tree/rerooting/` | Rerooting DP | O(n) | O(n) |
| `graphs/tree/tree-diameter/` | Tree diameter | O(n) | O(n) |
| `strings/aho-corasick/` | Aho-Corasick | build: O(m); find_all: O(n + z) | O(m) |
| `strings/duval/` | Lyndon factorisation (Duval) | O(n) | O(1) |
| `strings/kmp/` | KMP / prefix function | O(n + m) | O(m) |
| `strings/manacher/` | Manacher's algorithm | O(n) | O(n) |
| `strings/min-rotation/` | Minimal rotation | O(n) | O(n) |
| `strings/suffix-automaton/` | Suffix automaton | build: O(n); count_distinct: O(n); contains: O(|t|); longest_common_substring: O(|t|) | O(n) |
| `strings/z-function/` | Z-function | O(n) | O(n) |
