import os
import random

import pytest


@pytest.fixture(autouse=True)
def _seed():
    """Deterministic by default; export ALGO_SEED=<n> to explore other seeds."""
    random.seed(int(os.environ.get("ALGO_SEED", "12345")))
