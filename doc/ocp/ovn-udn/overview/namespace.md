# Namespace - Overview

[[Back]](../README.md) [[Prev]](../get/namespace.md) [[Next]](../create/namespace_crd.md)

Developers and administrators can create a user-defined network that is namespace scoped using the
custom resource. 

An overview of the process is as follows:
1. An administrator creates a namespace for a user-defined network with the `k8s.ovn.org/primary-user-defined-network` label.
2. The UserDefinedNetwork CR is created by either the cluster administrator or the user.
3. The user creates pods in the namespace.

[[Back]](../README.md) [[Prev]](../get/namespace.md) [[Next]](../create/namespace_crd.md)