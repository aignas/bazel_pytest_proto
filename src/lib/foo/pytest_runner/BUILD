load("//rules/pytest:rules.bzl", "py_test")

py_test(
    name = "foo_test",
    srcs = [
        "foo_test.py",
        "bar_test.py",
    ],
    deps = [
        "//idl/foo:foo_py",
    ],
    visibility = ["//visibility:public"],
)
