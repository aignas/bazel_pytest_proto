load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "foo_test",
    srcs = [
        "foo_test.py",
    ],
    deps = [
        "//idl/foo:foo_py",
    ],
    visibility = ["//visibility:public"],
)
