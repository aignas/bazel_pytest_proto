load("@rules_python//python:defs.bzl", "py_test")
load("@pip//:requirements.bzl", "requirement")

py_test(
    name = "foo_test",
    srcs = [
        "//tools:pytest_wrapper.py",
        "foo_test.py",
    ],
    deps = [
        "//idl/foo:foo_py",
        requirement("pytest"),
    ],
    args = [
        "--capture=no",
        "$(location :foo_test.py)"
    ],
    main = "//tools:pytest_wrapper.py",
    python_version = "PY3",
    srcs_version = "PY3",
    visibility = ["//visibility:public"],
)
