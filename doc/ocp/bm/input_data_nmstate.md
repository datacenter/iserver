# nmstate.yaml

[[Back]](../BareMetalCluster.md) [[Next]](./input_data_ssh_pub.md) [[Prev]](./input_data_redfish.md)

Server's networking configuration may be customized using file with nmstate syntax. The filename is referred per server in [server](./input_data_server.md) section. The file may have variables. 

> [!NOTE]
> Check [here](https://wwwin-github.cisco.com/emear-telcocloud/ocp-bm-cluster) for more examples

## Bonding Example 

```yaml
interfaces:
- name: ${BOND_MEMBER_1}
  type: ethernet
  state: up
- name: ${BOND_MEMBER_2}
  type: ethernet
  state: up
- name: ${BOND}
  type: bond
  state: up
  link-aggregation:
    mode: ${BOND_MODE}
    options:
      lacp_rate: ${LACP_RATE}
    port:
    - ${BOND_MEMBER_1}
    - ${BOND_MEMBER_2}
- name: ${BOND}.${VLAN}
  type: vlan
  state: up
  vlan:
    base-iface: ${BOND}
    id: ${VLAN}
  ipv4:
    address:
    - ip: ${IP}
      prefix-length: ${PREFIX}
    dhcp: false
    enabled: true
routes:
  config:
  - destination: 0.0.0.0/0
    next-hop-address: ${GW}
    next-hop-interface: ${BOND}.${VLAN}
dns-resolver:
  config:
    search:
    - ${DNS_SEARCH}
    server:
    - ${DNS_IP}
```

[[Back]](../BareMetalCluster.md) [[Next]](./input_data_ssh_pub.md) [[Prev]](./input_data_redfish.md)