# NMState Operator

The Kubernetes NMState Operator provides a Kubernetes API for performing state-driven network configuration as explained in [RedHat OpenShift documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking_operators/k8s-nmstate-about-the-k8s-nmstate-operator) and [overview](./overview.md)

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp nmstate | check the NMState operator state | [Link](./get.md)
iserver set ocp nmstate --mode operator | install and configure NMState operator | [Link](./create_operator.md)
iserver set ocp nmstate --mode lldp | enable LLDP in NMState operator and optionally disable on interfaces | [Link](./enable_lldp.md)
iserver set ocp lso --mode all | install operator and enable lldp | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp nmstate --mode operator | remove NMState operator | [Link](./delete_operator.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Related Commands

Command | Intent | Details
--- | --- | ---
iserver get k8s nns | get network node states | [Link](./nns.md)
iserver create k8s nncp | create network node configuration policies | [Link](../nncp/README.md)

[[Back]](../Operations.md)