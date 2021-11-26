load("@rules_python//python:defs.bzl", "py_test")
load("@pip//:requirements.bzl", "requirement")

py_test(
    name = "foo_test",
    srcs = [
        "main_test.py",
        "foo_test.py",
        "bar_test.py",
    ],
    deps = [
        "//idl/foo:foo_py",
        requirement("pytest"),
    ],
    main = "main_test.py",
    visibility = ["//visibility:public"],
)
