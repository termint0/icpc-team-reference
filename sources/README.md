# algolib – competitive-programming reference algorithms (Python)

Every algorithm lives in its own folder, e.g. `graphs/tree/euler-tour/`:

    euler_tour.py        the code (self-contained: copy-paste it anywhere)
    euler_tour.yaml      name, description, time, memory
    test_euler_tour.py   pytest tests (brute-force / independent references)

Top level: `algebra/ datastructures/ graphs/ strings/ geometry/ dp/`. `INDEX.md` lists all 97 entries.

Run all tests:   `pip install pytest pyyaml && python3 -m pytest -q`
Other seeds:     `ALGO_SEED=7 python3 -m pytest -q`   (default seed is fixed, 12345)

* Code files never import each other. Where an algorithm needs a helper that is also its own entry
  (e.g. `lucas` needs `Binomial`, `half_plane_intersection` needs `cross2`), the helper is copied in.
* Each test file also runs on its own: copy one folder anywhere and run `pytest` inside it.
* Conventions: ranges are half-open [l, r); vertices/indices are 0-based; weighted adjacency is
  adj[u] = [(v, w)], edge lists are [(u, v, w)].
