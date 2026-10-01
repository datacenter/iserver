# Traffic forwarding - east-west

[[Back]](./README.md)

East-west traffic between the applications deployed on the same Kubernetes cluster goes via kube overlay ( pod routing ), **not via evpn/vxlan overlay**.

Rerf to [test setup](../ew-test/README.md) for east-west forwarding details.

[[Back]](./README.md)