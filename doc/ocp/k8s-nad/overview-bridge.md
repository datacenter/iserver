# Network Attachment Definition - Bridge

Bridge CNI plugin acts as a network switch between multiple pods on the same node host.

By default, a bridge interface is created that does not link any physical host interface. As a result, connections are not made to any external networks including other pods on the other host nodes. However, it is possible to configure external bridge connectivity.

![Overview](../images/nad/bridge_overview.png)

## JSON Configuration 

![JSON](../images/nad/bridge_json.png)

## Links

- [CRD example](./crd-bridge.md)
- [Functional test](./test-bridge.md)
- [bridge plugin](https://www.cni.dev/plugins/current/main/bridge/)

[[Back]](./README.md)