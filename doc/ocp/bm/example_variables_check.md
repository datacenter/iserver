# RunIt - Server Variables Check and NMState Generation

[[Back]](../BareMetalCluster.md) [[Next]](./example_console_body_generation.md) [[Prev]](./example_openshift_api_check.md)

Variables Generation
- global variables baed on [cluster.json](./input_data_cluster_base.md)
- per-server variables based on server input in [server.json](./input_data_server.md)
- user-defined per-server variables in [server.json](./input_data_server.md)

```json
[
  {
      "hostname": "bm1-1",
      "variables": {
        ...
      }
  }
]
```

Variables check
- all variables defined in `${VAR}` format in [nmstate.yaml](./input_data_nmstate.md) **must resolve**

```
Variables
---------
Server [bm1-1]

~~~
{
    "VLAN": 666,
    "IP": "10.10.10.10",
    "PREFIX": "28",
    "GW": "10.10.10.14",
    "DNS_SEARCH_1": "domain.com",
    "DNS_SEARCH": "domain.com",
    "DNS_IP_1": "20.20.20.20",
    "DNS_IP": "20.20.20.20",
    "IFNAME": "eno5"
}
~~~

NMState [bm1-1]
---------------
- [eno5] aa:aa:aa:aa:aa:aa

~~~
interfaces:
- name: eno5.666
  type: vlan
  state: up
  vlan:
    base-iface: eno5
    id: 666
  ipv4:
    address:
    - ip: 10.10.10.10
      prefix-length: 28
    dhcp: false
    enabled: true
routes:
  config:
  - destination: 0.0.0.0/0
    next-hop-address: 10.10.10.14
    next-hop-interface: eno5.666
dns-resolver:
  config:
    search:
    - domain.com
    server:
    - 20.20.20.20
~~~
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_console_body_generation.md) [[Prev]](./example_openshift_api_check.md)