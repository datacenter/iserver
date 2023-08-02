# Node Protocol - ARP

## Default output

```
# iserver get aci proto arp --apic apic21 --node bl2205-eu-spdc --view adj

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Adjacency [#13]
------------------------------

+----------------------+-------------------------+-------------------+----------------+------------+------------+---------------+-------------------------------+
| Node                 | VRF                     | MAC               | IP             | State      | Interface  | Phy Interface | Timestamp                     |
+----------------------+-------------------------+-------------------+----------------+------------+------------+---------------+-------------------------------+
| pod-1/bl2205-eu-spdc | common:Infra_privIP_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.74 | normal     | eth1/25.17 | eth1/25       | 2023-08-02T14:28:36.062+02:00 | 
| pod-1/bl2205-eu-spdc | common:Infra_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.9  | normal     | eth1/25.18 | eth1/25       | 2023-08-02T14:28:37.342+02:00 | 
| pod-1/bl2205-eu-spdc | mgmt:inb                | 00:A3:8E:EB:B3:3F | 192.168.254.25 | normal     | eth1/25.19 | eth1/25       | 2023-08-02T14:28:36.112+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.1   | incomplete | vlan1      |               | 2023-08-02T14:33:13.898+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.2   | incomplete | vlan1      |               | 2023-08-02T14:33:13.900+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.3   | incomplete | vlan1      |               | 2023-08-02T14:33:13.901+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.4   | incomplete | vlan1      |               | 2023-08-02T14:33:13.902+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.5   | incomplete | vlan1      |               | 2023-08-02T14:33:13.903+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.1   | incomplete | vlan20     |               | 2023-08-02T14:33:13.892+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.2   | incomplete | vlan20     |               | 2023-08-02T14:33:13.893+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.3   | incomplete | vlan20     |               | 2023-08-02T14:33:13.894+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.4   | incomplete | vlan20     |               | 2023-08-02T14:33:13.896+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.5   | incomplete | vlan20     |               | 2023-08-02T14:33:13.897+02:00 | 
+----------------------+-------------------------+-------------------+----------------+------------+------------+---------------+-------------------------------+

Protocol ARP - Interface Adjacency Summary [#5]
-----------------------------------------------

+----------------------+------------+-----------+
| Node                 | Interface  | Adjacency |
+----------------------+------------+-----------+
| pod-1/bl2205-eu-spdc | eth1/25.17 | 1         | 
| pod-1/bl2205-eu-spdc | eth1/25.18 | 1         | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | 1         | 
| pod-1/bl2205-eu-spdc | vlan1      | 5         | 
| pod-1/bl2205-eu-spdc | vlan20     | 5         | 
+----------------------+------------+-----------+
```

Developer

```
# iserver get aci proto arp --apic apic21 --node bl2205-eu-spdc --view adj

{
    "duration": 1404,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 379,
        "disconnect_time": 0,
        "mo_time": 833,
        "total_time": 1212
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	379	-	connect apic21o.emea-sp.cisco.com:443
True	278	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	271	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	284	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)