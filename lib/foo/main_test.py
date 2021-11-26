import os
import sys

import pytest


def run(args = None):
    if args is None:
        args = list(sys.argv[1:])

    __file__ = "py.test"
    sys.argv[0] = sys.argv[0].replace("pytest_wrapper.py", "py.test")

    filter = os.environ.get("TESTBRIDGE_TEST_ONLY")
    if filter:
        if args is None:
            args = []
        parts = filter.split("$", 1)
        args.append(parts[0])  # path
        if len(parts) > 1:
            args.extend(["-k", parts[1]])  # function name

    print(args)
    return pytest.main(args)

if __name__ == "__main__":
    raise SystemExit(run())
