# This import must be here or otherwise pytest changes our env and this import
# path stops working due to some reason.
import idl.foo.foo_pb2

if __name__ == "__main__":
    import sys
    import pytest
    pytest.main(sys.argv[1:])
