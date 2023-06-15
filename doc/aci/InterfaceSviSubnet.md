# Node Interface - SVI

## Filter by IP subnet

```
# iserver get aci intf svi
    --apic apic11
    --node bl205-eu-spdc
    --subnet 15.0.0.0/8
    --view addr

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| Node                | Interface | Admin State | Oper State | Vlan ID | MAC               | IPv4              |
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 1       | 00:22:BD:3D:C2:CC | 15.3.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan18    | up          | up         | 18      | 00:22:BD:3D:C2:BB | 15.3.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 19      | 00:22:BD:3D:C1:CC | 15.3.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan20    | up          | up         | 20      | 00:22:BD:3D:C1:BB | 15.3.61.254/24    | 
| pod-1/bl205-eu-spdc | vlan23    | up          | up         | 23      | 00:22:BD:F8:19:FF | 15.2.203.254/24   | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | 30      | 00:22:BD:F5:AA:FF | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 32      | 00:22:BD:F8:19:FF | 15.101.3.254/24   | 
| pod-1/bl205-eu-spdc | vlan33    | up          | up         | 33      | 00:22:BD:F8:00:FF | 15.2.10.254/24    | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 39      | 00:22:BD:CD:C2:CC | 15.2.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | 43      | 00:22:BD:CD:C2:BB | 15.2.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan44    | up          | up         | 44      | 00:22:BD:CD:C3:CC | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan45    | up          | up         | 45      | 00:22:BD:CD:C1:CC | 15.2.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | 5       | 00:22:BD:3D:C3:CC | 15.3.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan56    | up          | up         | 56      | 00:22:BD:F5:BB:FF | 15.2.7.254/24     | 
|                     |           |             |            |         |                   | 15.2.7.253/24     | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | 57      | 00:22:BD:F8:19:FF | 15.100.169.1/24   | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 59      | 00:22:BD:F8:19:FF | 15.100.161.126/25 | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 61      | 00:22:BD:EE:EE:FF | 15.254.254.254/24 | 
|                     |           |             |            |         |                   | 192.168.0.14/28   | 
| pod-1/bl205-eu-spdc | vlan67    | up          | up         | 67      | 00:22:BD:CD:C2:BB | 15.2.7.254/24     | 
|                     |           |             |            |         |                   | 15.2.7.253/24     | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | 70      | 00:22:BD:F8:19:FF | 15.100.161.254/25 | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | 72      | 00:22:BD:CD:C1:BB | 15.2.61.254/24    | 
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic11
    --node bl205-eu-spdc
    --subnet 15.0.0.0/8
    --view addr

{
    "duration": 1524,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 383,
        "disconnect_time": 0,
        "mo_time": 972,
        "total_time": 1355
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

True	383	-	connect apic11o.emea-sp.cisco.com
True	291	13	apic11o.emea-sp.cisco.com class fabricNode
True	386	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	295	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)