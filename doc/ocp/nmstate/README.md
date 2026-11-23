# NMState Operator

[[Back]](../Operations.md)

![Overview](../images/nmstate/logo.png)

The Kubernetes NMState Operator provides a Kubernetes API for performing state-driven network configuration as explained in [RedHat OpenShift documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking_operators/k8s-nmstate-about-the-k8s-nmstate-operator).

## Features

- [get](./nns.md) networking state of the cluster nodes via `NodeNetworkState` CRD
    - interface
        - addresses: ipv4, ipv6, mac
        - settings: mtu, type
        - state
        - ethtool flags: coalescence, feature, fec, pause, ring
        - sriov vf
        - driver
    - route table
    - DNS configuration
    - LLDP neighbor information
- [configure](../nncp/README.md) networking stack via `NodeNetworkConfigurationPolicy` CRD and verify configuration intent with `NodeNetworkConfigurationEnactment` CRD

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp nmstate | check the nmstate operator state | [Link](./get.md)
iserver set ocp nmstate --mode operator | install and configure nmstate operator | [Link](./create_operator.md)
iserver set ocp nmstate --mode instance | create nmstate instance | [Link](./create_instance.md)
iserver set ocp nmstate --mode lldp | enable LLDP in nmstate operator and optionally disable on interfaces | [Link](./enable_lldp.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp nmstate --mode operator | remove nmstate operator | [Link](./delete_operator.md)
iserver delete ocp nmstate --mode instance | remove nmstate instance | [Link](./delete_instance.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Related Commands

Command | Intent | Details
--- | --- | ---
iserver get k8s nns | get network node states | [Link](./nns.md)
iserver create k8s nncp | create network node configuration policies | [Link](../nncp/README.md)

[[Back]](../Operations.md)