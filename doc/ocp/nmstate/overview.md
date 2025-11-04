# NMState Operator Overview

NMState Operator exposes network state and network configuration abstraction of the cluster nodes via Kubernetes API
- network interface state
    - addresses: ipv4, ipv6, mac
    - settings: mtu, type
    - state
    - ethtool flags: coalescence, feature, fec, pause, ring
    - sriov vf
    - driver
- route table state
- DNS configuration
- LLDP neighbor information
- network configuration
    - Bond
    - VLAN subinterface
    - Linux bridge
    - OVS

NMState Operator installation in few steps:
- Goto Administrator - Operators - OperatorHub page on OCP Console UI
- Select 'Kubernetes NMState Operator' provided by RedHat Inc
- Install operator
- Create NMState instance

Once NMState Operator is installed, new CRD objects are exposed:
- NMState to control instance
- NodeNetworkConfigurationEnactment to control network configuration
- NodeNetworkConfigurationPolicy to control network configuration
- NodeNetworkState to get the network state in yaml/json format

LLDP neighbor information improves operational experience however,
- LLDP is disabled by default on nmstate level and can be enabled by applying specific nncp resource
- LLDP may be enabled on the NIC firmware level
    - depends on the NIC HW type and firmware defaults
    - ethtool priv flags show lldp-on-nic settings
    - ethtool priv flags not shown in nns output
    - priv flags controlling lldp-on-nic not standard and differ per NIC type e.g. Intel 700 vs 800 series

Refer to [RedHat OpenShift documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking_operators/k8s-nmstate-about-the-k8s-nmstate-operator) for details.

[[Back]](./README.md)