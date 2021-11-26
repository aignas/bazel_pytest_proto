load("@rules_python//python:defs.bzl", _py_test = "py_test")
load("@pip//:requirements.bzl", "requirement")

def py_test(name, srcs, **kwargs):
    _py_test(
        name = name,
        srcs = [
            "//rules/pytest:__main__.py",
        ] + srcs,
        deps = [
            requirement("pytest"),
        ] + kwargs.pop("deps", []),
        args = [
            "--capture=no",
            "--import-mode=importlib",
        ] + kwargs.pop("args", []) + ["$(location :%s)" % s for s in srcs],
        main = "//rules/pytest:__main__.py",
        **kwargs,
    )
