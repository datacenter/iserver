# User Defined Network (UDN)

[[Back]](../Operations.md)

User-defined networks (UDNs) extend OVN-Kubernetes to enable custom layer 2 and layer 3 network segments with default isolation, providing enhanced network flexibility, security, and segmentation capabilities for multi-tenant deployments and custom network architectures as explained in the official [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/pdf/multiple_networks/OpenShift_Container_Platform-4.21-Multiple_networks-en-US.pdf)

![Overview](../images/ovn-udn/overview.png)

## Features

- [namespace](./overview/namespace.md) scope
- [L2 topology](./overview/l2.md) - flat L2 subnet across the nodes
- [L3 topology](./overview/l3.md) - similar to POD CIDR with per node subnets
- single primary and mutliple secondary networks per namespace
- topology type [mix-and-match](./example/mix_and_match.md)
- mandatory IPAM (DHCP) unless no subnet defined in L2 topology
- bridging (L2 topology) or routing (L3 topology) with [overlay-on-the-wire](./example/overlay.md)
- [multicast friendly](./example/multicast.md)
- masquerade with cluster node ip on [egress](./example/egress.md)
- isolation
    - udn subnets can [overlap](./example/overlap.md) between namespaces
    - intra-udn traffic [allowed](./policy/intra_udn_allowed.md) unless [network policy](./policy/intra_udn_network_policy.md) applied
    - cross-udn traffic [not allowed](./policy/inter_udn_not_allowed.md)
    - udn cannot communicate with default network unless [open ports](./policy/open_ports.md) defined

## HowTo

Intent | Create w/CRD | Create w/Task | Get State
--- | --- | --- | ---
[Namespace](./overview/namespace.md) | [Link](./create/namespace_crd.md) | [Link](./create/namespace_task.md) | [Link](./get/namespace.md)
[UDN L2](./overview/l2.md) | [Link](./create/l2_crd.md) | [Link](./create/l2_task.md) | [Link](./get/l2.md)
[UDN L3](./overview/l3.md) | [Link](./create/l3_crd.md) | [Link](./create/l3_task.md) | [Link](./get/l3.md)
[POD](./overview/pod.md) | [Link](./create/pod_crd.md) | [Link](./create/pod_task.md) | [Link](./get/pod.md)
[VM](./overview/vm.md) | [Link](./create/vm_crd.md) | [Link](./create/vm_task.md) | [Link](./get/vm.md)

[[Back]](../Operations.md)