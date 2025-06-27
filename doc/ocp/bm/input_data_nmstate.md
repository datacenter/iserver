# Nmstate

Server's networking configuration may be customized using file with nmstate syntax. The filename is referred per server in [server](./input_data_server.md) section. The file may have variables.

## Bonding Example

Note: server section may be either in cluster.json or in server.json

```
"server": [
    {
        "hostname": "bm1-1",
        "nmstate": "bonding.yaml",
        "variables": {
            "BOND": "bond0",
            "BOND_MEMBER_1": "eno5",
            "BOND_MEMBER_2": "eno6",
            "VLAN": "666",
            "IP": "10.4.4.1",
            "PREFIX": "28",
            "GW": "10.4.4.15",
            "DNS_SEARCH": "domain.com",
            "DNS_IP": "20.20.20.20"
        }
    }
]
```

bonding.yaml content

```
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
    mode: 802.3ad
    options:
      lacp_rate: slow
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

## Single interface example

Note: server section may be either in cluster.json or in server.json

```
"server": [
    {
        "hostname": "bm1-1",
        "nmstate": "single.yaml",
        "variables": {
            "IFNAME": "eno5",
            "VLAN": "666",
            "IP": "10.4.4.1",
            "PREFIX": "28",
            "GW": "10.4.4.15",
            "DNS_SEARCH": "domain.com",
            "DNS_IP": "20.20.20.20"
        }
    }
]
```

single.yaml content

```
interfaces:
- name: ${IFNAME}.${VLAN}
  type: vlan
  state: up
  vlan:
    base-iface: ${IFNAME}
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
    next-hop-interface: ${IFNAME}.${VLAN}
dns-resolver:
  config:
    search:
    - ${DNS_SEARCH}
    server:
    - ${DNS_IP}
```

[Back](../BareMetalCluster.md)
