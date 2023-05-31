# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view addr

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| Node                | Interface | Admin State | Oper State | Vlan ID | MAC               | IPv4              |
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 1       | 00:22:BD:3D:C3:CC | 15.3.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | 11      | 00:22:BD:F8:19:FF | 192.168.1.1/24    | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | 13      | 00:22:BD:3D:C1:CC | 15.3.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan14    | up          | up         | 14      | 00:22:BD:FE:FF:FF | 99.99.99.254/24   | 
| pod-1/bl205-eu-spdc | vlan16    | up          | up         | 16      | 00:22:BD:3D:C2:BB | 15.3.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | 17      | 00:22:BD:F8:00:FF | 15.2.10.254/24    | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 19      | 00:22:BD:F8:19:FF | 15.100.161.126/25 | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | 21      | 00:22:BD:3D:C2:CC | 15.3.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | 22      | 00:22:BD:F8:33:33 | 10.58.239.254/24  | 
| pod-1/bl205-eu-spdc | vlan24    | up          | up         | 24      | 00:22:BD:CD:C1:CC | 15.2.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | 25      | 00:22:BD:CD:C2:BB | 15.2.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan26    | up          | up         | 26      | 00:22:BD:CC:19:CC | 10.58.24.254/27   | 
| pod-1/bl205-eu-spdc | vlan28    | up          | up         | 28      | 00:22:BD:CD:C1:BB | 15.2.61.254/24    | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | 29      | 00:22:BD:CD:C3:CC | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | 30      | 00:22:BD:F8:19:FF |                   | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 32      | 00:22:BD:F8:19:FF | 15.100.161.254/25 | 
| pod-1/bl205-eu-spdc | vlan34    | up          | up         | 34      | 00:22:BD:F8:19:FF | 10.58.28.175/27   | 
|                     |           |             |            |         |                   | 10.58.28.190/27   | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | 35      | 00:22:BD:F8:19:FF | 10.58.24.110/28   | 
|                     |           |             |            |         |                   | 10.58.24.109/28   | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | 37      | 00:22:BD:F5:AA:FF | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 39      | 00:22:BD:F8:19:FF | 15.101.3.254/24   | 
| pod-1/bl205-eu-spdc | vlan4     | up          | up         | 4       | 00:22:BD:3D:C1:BB | 15.3.61.254/24    | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | 40      | 00:22:BD:F8:19:FF | 192.168.20.1/24   | 
| pod-1/bl205-eu-spdc | vlan41    | up          | up         | 41      | 00:22:BD:F8:19:FF | 15.100.169.1/24   | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | 43      | 00:22:BD:AA:CC:FF | 10.58.24.158/27   | 
| pod-1/bl205-eu-spdc | vlan46    | up          | up         | 46      | 00:22:BD:F8:BB:EE |                   | 
| pod-1/bl205-eu-spdc | vlan48    | up          | up         | 48      | 00:22:BD:F8:19:FF |                   | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | 5       | 00:22:BD:F8:19:FF |                   | 
| pod-1/bl205-eu-spdc | vlan50    | up          | up         | 50      | 00:22:BD:F9:99:FF | 192.168.0.254/24  | 
| pod-1/bl205-eu-spdc | vlan53    | up          | up         | 53      | 00:22:BD:F8:19:FF | 15.2.203.254/24   | 
| pod-1/bl205-eu-spdc | vlan55    | up          | up         | 55      | 00:22:BD:EE:EE:FF | 15.254.254.254/24 | 
|                     |           |             |            |         |                   | 192.168.0.14/28   | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | 57      | 00:22:BD:BD:99:FF |                   | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 59      | 00:22:BD:CD:C2:CC | 15.2.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 61      | 00:22:BD:CD:C2:BB | 15.2.7.254/24     | 
|                     |           |             |            |         |                   | 15.2.7.253/24     | 
| pod-1/bl205-eu-spdc | vlan63    | up          | up         | 63      | 00:22:BD:F5:BB:FF | 15.2.7.253/24     | 
|                     |           |             |            |         |                   | 15.2.7.254/24     | 
| pod-1/bl205-eu-spdc | vlan69    | up          | up         | 69      | 00:22:BD:DD:EE:FF | 10.58.27.142/28   | 
| pod-1/bl205-eu-spdc | vlan7     | up          | up         | 7       | 00:22:BD:F8:19:FF | 192.168.1.1/24    | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | 70      | 00:22:BD:DD:AA:FF | 10.58.27.126/28   | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | 72      | 00:22:BD:DD:EE:FF | 10.58.27.110/28   | 
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view addr

{
    "duration": 1800,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 534,
        "disconnect_time": 0,
        "mo_time": 1049,
        "total_time": 1583
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

True	534	-	connect apic11o.emea-sp.cisco.com
True	308	11	apic11o.emea-sp.cisco.com class fabricNode
True	437	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	304	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)