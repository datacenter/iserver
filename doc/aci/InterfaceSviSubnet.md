# Node Interface - SVI

## Filter by IP subnet

```
# iserver get aci intf svi
    --apic apic11
    --node bl205-eu-spdc
    --subnet 15.0.0.0/8
    --view addr

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| Node                | Interface | Admin State | Oper State | Vlan ID | MAC               | IPv4              |
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 1       | 00:22:BD:3D:C3:CC | 15.3.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | 13      | 00:22:BD:3D:C1:CC | 15.3.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan16    | up          | up         | 16      | 00:22:BD:3D:C2:BB | 15.3.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | 17      | 00:22:BD:F8:00:FF | 15.2.10.254/24    | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 19      | 00:22:BD:F8:19:FF | 15.100.161.126/25 | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | 21      | 00:22:BD:3D:C2:CC | 15.3.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan24    | up          | up         | 24      | 00:22:BD:CD:C1:CC | 15.2.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | 25      | 00:22:BD:CD:C2:BB | 15.2.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan28    | up          | up         | 28      | 00:22:BD:CD:C1:BB | 15.2.61.254/24    | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | 29      | 00:22:BD:CD:C3:CC | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 32      | 00:22:BD:F8:19:FF | 15.100.161.254/25 | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | 37      | 00:22:BD:F5:AA:FF | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 39      | 00:22:BD:F8:19:FF | 15.101.3.254/24   | 
| pod-1/bl205-eu-spdc | vlan4     | up          | up         | 4       | 00:22:BD:3D:C1:BB | 15.3.61.254/24    | 
| pod-1/bl205-eu-spdc | vlan41    | up          | up         | 41      | 00:22:BD:F8:19:FF | 15.100.169.1/24   | 
| pod-1/bl205-eu-spdc | vlan53    | up          | up         | 53      | 00:22:BD:F8:19:FF | 15.2.203.254/24   | 
| pod-1/bl205-eu-spdc | vlan55    | up          | up         | 55      | 00:22:BD:EE:EE:FF | 15.254.254.254/24 | 
|                     |           |             |            |         |                   | 192.168.0.14/28   | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 59      | 00:22:BD:CD:C2:CC | 15.2.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 61      | 00:22:BD:CD:C2:BB | 15.2.7.254/24     | 
|                     |           |             |            |         |                   | 15.2.7.253/24     | 
| pod-1/bl205-eu-spdc | vlan63    | up          | up         | 63      | 00:22:BD:F5:BB:FF | 15.2.7.253/24     | 
|                     |           |             |            |         |                   | 15.2.7.254/24     | 
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
    "duration": 1681,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 1085,
        "total_time": 1496
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
    }
}

Log: apic
----------

True	411	-	connect apic11o.emea-sp.cisco.com
True	314	11	apic11o.emea-sp.cisco.com class fabricNode
True	472	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	299	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)