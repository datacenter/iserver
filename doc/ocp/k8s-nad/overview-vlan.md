# Network Attachment Definition - VLAN

[[Back]](./README.md) [[Prev]](./pod-vlan.md) [[Next]](./crd-schema-vlan.md)

The vlan plugin creates a vlan subinterface off an master interface in the host network namespace and place the vlan subinterface inside the container namespace. Each container must use different master and vlanId pair.

The host-local IPAM plugin can be used to allocate an IP address to the container. The traffic of the container interface will be vland through the master interface.

POD’s virtual interface mac-address is the same as parent interface. This rules out DHCP IP address assignment option.

[[Back]](./README.md) [[Prev]](./pod-vlan.md) [[Next]](./crd-schema-vlan.md)