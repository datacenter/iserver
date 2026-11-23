# Overview

SR-IOV enables you to segment a compliant network device, recognized on the host node as a physical function (PF), into multiple virtual functions (VFs). The VF is used like any other network device. The SR-IOV device driver for the device determines how the VF is exposed in the container:
- netdevice driver: A regular kernel network device in the netns of the container
- vfio-pci driver: A character device mounted in the container

SR-IOV Network Operator is responsible for configuring the SR-IOV components in OpenShift cluster.
- initialize the SR-IOV NICs on nodes.
- provision SR-IOV device plugin on selected node.
- provision SR-IOV CNI plugin on selected nodes.
- manage configuration of SR-IOV device plugin.
- generate net-att-def CRs for SR-IOV CNI plugin.
- create node specific SriovNetworkNodeState custom resources

SR-IOV Network Operator installation in few steps:
- Goto Administrator - Operators - OperatorHub page on OCP Console UI
- Select 'SR-IOV Network Operator' provided by RedHat Inc
- Install operator
- Create SriovOperatorConfig CR

SR-IOV Network Operator adds the SriovNetworkNodePolicy CR. It is used to configure an SR-IOV network device on cluster worker node.

[[Back]](./README.md)