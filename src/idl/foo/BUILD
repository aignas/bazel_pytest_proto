load("@rules_proto_grpc//python:defs.bzl", "python_proto_library")
load("@rules_proto//proto:defs.bzl", "proto_library")

python_proto_library(
    name = "foo_py",
    protos = [":foo_proto"],
    visibility = ["//visibility:public"],
)

proto_library(
    name = "foo_proto",
    srcs = [
        "bar.proto",
        "foo.proto",
    ],
    visibility = ["//visibility:public"],
)
