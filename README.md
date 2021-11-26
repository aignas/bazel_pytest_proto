# When bazel meets pytest and rules_proto_grpc

Bazel is amazing in providing reproducible builds, but the [rules_python] is still under heavy development.
Pytest usage from within bazel can be a bit tricky, as can be seen from:

1. [A stack overflow answer](https://stackoverflow.com/a/58345932) where we make each test file a script and need to remember to add an `if __name__ == "__main__"` block.
2. [Answer within the same thread](https://stackoverflow.com/a/67389568) where we create a wrapper macro, which allows us not need the solution from above.

All was well until I started to use [rules_proto_grpc]. I could not get the example code to work if I was using `pytest` as my testing framework.

Some important things to note:

1. `rules_proto_grpc` is defining a python library with usage of `imports`
   [flag]. This is needed because the path to the python files in the
   `bazel-bin` directory are
   `bazel-bin/idl/path/to/build/file/name_pb/idl/for/import` where
   `idl/path/to/build/file` segment mirrors the path of the BUILD file relative
   to your `WORKSPACE` and `idl/for/import` segment mirrors the import path
   found in the `.proto` file. Benefits of such approach as far as I can see are manyfold:
   1. The import path and the bazel path are decoupled.
   1. No two rules are going to overwrite the same files.
   1. Probably something else which I am not yet aware.
1. This `imports` usage in turn [modifies the PYTHONPATH][imports] such that we
   could import the generated python package via `from idl.for.import import foo_pb2 as foo_pb`.
1. Everything works until `pytest` comes along, which is doing some test
   discovery and is also modifying the paths which python checks when importing
   `idl.for.import`. The way it is doing this is:
   1. We are running inside `bazel-bin/lib/foo/foo_test.runfiles/<my-workspace-name>` directory
      (assuming the test rule we are running from is called `foo_test`).
   1. Pytest crawls the directories it can see and notices that we have python
      files within `idl/path/to/build/file/name_pb/idl/for/import` and happily
      _prepends_ the list of paths to search python modules from so our
      previously working `idl/for/import` stops working because both of the
      paths have `idl` in the prefix and Python checks the `idl` directory and
      does not go into `idl/path/to/build/file/name_pb/idl` directory because
      it is failing fast in this case.
   1. Everything works if pytest is doing the crawl after we load the
      `idl.for.import` module because of how python module caching works as
      alluded [here][pytest_docs].

So this repo shows a solution:

> pass an extra `--import-mode=importlib`, which will become later the default.

If you know a better solution, let me know via an issue or a PR to this example!

[rules_python]: https://github.com/bazelbuild/rules_python
[rules_proto_grpc]: https://github.com/rules-proto-grpc/rules_proto_grpc
[flag]: https://github.com/rules-proto-grpc/rules_proto_grpc/blob/d143d46d4297cc33ef0908967c52cb369b11b319/python/python_proto_library.bzl#L24
[imports]: https://docs.bazel.build/versions/main/be/python.html#py_test.imports
[pytest_docs]: https://docs.pytest.org/en/6.2.x/pythonpath.html
