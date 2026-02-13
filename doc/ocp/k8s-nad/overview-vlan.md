# Network Attachment Definition - VLAN

The vlan plugin creates a vlan subinterface off an master interface in the host network namespace and place the vlan subinterface inside the container namespace. Each container must use different master and vlanId pair.

The host-local IPAM plugin can be used to allocate an IP address to the container. The traffic of the container interface will be bridged through the master interface.

POD’s virtual interface mac-address is the same as parent interface. This rules out DHCP IP address assignment option.

## JSON Configuration 

![JSON](../images/nad/vlan_json.png)

## Links

- [CRD example](./crd-vlan.md)
- [Functional test](./pod-vlan.md)
- [vlan plugin](https://www.cni.dev/plugins/current/main/vlan/)

[[Back]](./README.md)