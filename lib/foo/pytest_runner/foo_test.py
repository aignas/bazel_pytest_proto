from idl.foo.foo_pb2 import Foo

def test_simple_foo():
    assert Foo() is not None
