import sys

import pytest

sys.exit(pytest.main(sys.argv[1:] + ["--import-mode=importlib"]))
