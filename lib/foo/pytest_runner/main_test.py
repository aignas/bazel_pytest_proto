if __name__ == "__main__":
    import sys
    import pytest
    pytest.main(sys.argv[1:] + ["--import-mode=importlib"])
