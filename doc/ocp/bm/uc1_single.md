# OpenShift Cluster on UCSX with NVIDIA GPU

single.yaml in nmstate format defines the single interface setup. The variables are defined per-server in [cluster](./uc1_cluster.md) definition file

```
interfaces:
- name: ${INTF}
  type: ethernet
  state: up
- name: ${INTF}.${VLAN}
  type: vlan
  state: up
  vlan:
    base-iface: ${INTF}
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
    next-hop-interface: ${INTF}.${VLAN}
dns-resolver:
  config:
    search:
    - ${DNS_SEARCH}
    server:
    - ${DNS_IP}
```

[Back](./uc1.md)