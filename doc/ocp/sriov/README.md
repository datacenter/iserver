# SR-IOV Network Operator

The SR-IOV Network Operator  is generally responsible for configuring the sriov components in a openshift cluster as explained in  [RedHat OpenShift documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking_operators/sr-iov-operator) and [overview](./overview.md)

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp sriov | check the sriov operator and instance state | [Link](./get.md)
iserver set ocp sriov --mode operator | install sriov operator | [Link](./create_operator.md)
iserver set ocp sriov --mode instance | create sriov instance | [Link](./create_instance.md)
iserver set ocp sriov --mode all | install sriov operator and create instance | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp sriov --mode operator | delete sriov operator | [Link](./delete_operator.md)
iserver delete ocp sriov --mode instance | delete sriov instance | [Link](./delete_instance.md)
iserver delete ocp sriov --mode all | delete sriov instance and operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)