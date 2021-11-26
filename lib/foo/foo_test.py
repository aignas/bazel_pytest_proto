try:
    from idl.foo.foo_pb2 import Foo
except ImportError:
    import importlib
    import pkgutil
    import sys
    import idl
    def find_abs_modules(module):
        path_list = []
        spec_list = []
        for importer, modname, ispkg in pkgutil.walk_packages(module.__path__):
            import_path = f"{module.__name__}.{modname}"
            if ispkg:
                spec = pkgutil._get_spec(importer, modname)
                importlib._bootstrap._load(spec)
                spec_list.append(spec)
            else:
                path_list.append(import_path)
        for spec in spec_list:
            del sys.modules[spec.name]
        return path_list

    print("Available modules:")
    print(find_abs_modules(idl))

def simple_test():
    assert Foo() is not None

if __name__ == "__main__":
    simple_test()
