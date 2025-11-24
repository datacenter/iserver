# Service Mesh Operator

The OpenShift Service Mesh Operator enables you to install, configure, and manage an instance of Red Hat OpenShift Service Mesh as explained in official [documentation](https://www.redhat.com/en/blog/introducing-red-hat-openshift-service-mesh-3).

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp service-mesh | check the server mesh operator state | [Link](./get.md)
iserver set ocp service-mesh | install server mesh operator | [Link](./create_operator.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp service-mesh | uninstall server mesh operator | [Link](./delete_operator.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)