load("@rules_python//python:defs.bzl", "py_test")
load("@pip//:requirements.bzl", "requirement")

[
     py_test(
         name = name,
         srcs = [name + ".py"],
         deps = [
             "//idl/foo:foo_py",
         ],
         visibility = ["//visibility:public"],
     )
     for name in ["foo_test", "bar_test"]
]
