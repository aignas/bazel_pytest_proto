from idl.foo.foo_pb2 import Foo

def test_simple():
    assert Foo() is not None
