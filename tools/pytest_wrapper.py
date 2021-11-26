import sys

import pytest

if __name__ == "__main__":
    args = sys.argv[1:]
    print("Got args {}".format(args))
    sys.exit(pytest.main(args))
