# Private Network - eBPF Maps

[[Back]](../README.md) [[iserver-way]](../get_map.md) [[Next]](./crd.md)

```shell
kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell
```

| Command | Description |
|---------|-------------|
| `db/show privnet-endpoints` | Show all PrivNet endpoints (local + remote) with network IP and PIP mappings |
| `db/show privnet-routes` | Show routing table including auto-generated peering routes |
| `db/show privnet-subnets` | Show subnets with DHCP mode and interface bindings (local-access) |
| `db/show privnet-dhcp-leases` | Show DHCP leases with renewal/expiry times |
| `db/show privnet-local-workloads` | Show local workloads with PrivNet/PIP mappings |
| `db/show privnet-inbs` | Show connected INB instances and their health/role |
| `privnet/status` | Show overall PrivNet status including INB HA state |

[[Back]](../README.md) [[iserver-way]](../get_map.md) [[Next]](./crd.md)