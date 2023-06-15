# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view addr

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| Node                | Interface | Admin State | Oper State | Vlan ID | MAC               | IPv4              |
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 1       | 00:22:BD:3D:C2:CC | 15.3.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | 11      | 00:22:BD:F8:BB:EE |                   | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | 13      | 00:22:BD:F8:19:FF |                   | 
| pod-1/bl205-eu-spdc | vlan15    | up          | up         | 15      | 00:22:BD:F8:19:FF |                   | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | 17      | 00:22:BD:F8:19:FF | 192.168.20.1/24   | 
| pod-1/bl205-eu-spdc | vlan18    | up          | up         | 18      | 00:22:BD:3D:C2:BB | 15.3.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 19      | 00:22:BD:3D:C1:CC | 15.3.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan2     | up          | up         | 2       | 00:22:BD:F8:19:FF | 10.58.28.175/27   | 
|                     |           |             |            |         |                   | 10.58.28.190/27   | 
| pod-1/bl205-eu-spdc | vlan20    | up          | up         | 20      | 00:22:BD:3D:C1:BB | 15.3.61.254/24    | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | 21      | 00:22:BD:DD:EE:FF | 10.58.27.142/28   | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | 22      | 00:22:BD:DD:EE:FF | 10.58.27.110/28   | 
| pod-1/bl205-eu-spdc | vlan23    | up          | up         | 23      | 00:22:BD:F8:19:FF | 15.2.203.254/24   | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | 25      | 00:22:BD:F8:33:33 | 10.58.239.254/24  | 
| pod-1/bl205-eu-spdc | vlan27    | up          | up         | 27      | 00:22:BD:BD:99:FF |                   | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | 29      | 00:22:BD:DD:AA:FF | 10.58.27.126/28   | 
| pod-1/bl205-eu-spdc | vlan3     | up          | up         | 3       | 00:22:BD:F8:19:FF |                   | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | 30      | 00:22:BD:F5:AA:FF | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 32      | 00:22:BD:F8:19:FF | 15.101.3.254/24   | 
| pod-1/bl205-eu-spdc | vlan33    | up          | up         | 33      | 00:22:BD:F8:00:FF | 15.2.10.254/24    | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | 35      | 00:22:BD:FE:FF:FF | 99.99.99.254/24   | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | 37      | 00:22:BD:CC:19:CC | 10.58.24.254/27   | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 39      | 00:22:BD:CD:C2:CC | 15.2.62.254/24    | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | 40      | 00:22:BD:AA:CC:FF | 10.58.24.158/27   | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | 43      | 00:22:BD:CD:C2:BB | 15.2.63.254/24    | 
| pod-1/bl205-eu-spdc | vlan44    | up          | up         | 44      | 00:22:BD:CD:C3:CC | 15.2.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan45    | up          | up         | 45      | 00:22:BD:CD:C1:CC | 15.2.6.254/24     | 
| pod-1/bl205-eu-spdc | vlan49    | up          | up         | 49      | 00:22:BD:F8:19:FF | 10.58.24.110/28   | 
|                     |           |             |            |         |                   | 10.58.24.109/28   | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | 5       | 00:22:BD:3D:C3:CC | 15.3.64.254/24    | 
| pod-1/bl205-eu-spdc | vlan56    | up          | up         | 56      | 00:22:BD:F5:BB:FF | 15.2.7.254/24     | 
|                     |           |             |            |         |                   | 15.2.7.253/24     | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | 57      | 00:22:BD:F8:19:FF | 15.100.169.1/24   | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 59      | 00:22:BD:F8:19:FF | 15.100.161.126/25 | 
| pod-1/bl205-eu-spdc | vlan6     | up          | up         | 6       | 00:22:BD:F9:99:FF | 192.168.0.254/24  | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 61      | 00:22:BD:EE:EE:FF | 15.254.254.254/24 | 
|                     |           |             |            |         |                   | 192.168.0.14/28   | 
| pod-1/bl205-eu-spdc | vlan65    | up          | up         | 65      | 00:22:BD:F8:19:FF | 192.168.1.1/24    | 
| pod-1/bl205-eu-spdc | vlan67    | up          | up         | 67      | 00:22:BD:CD:C2:BB | 15.2.7.254/24     | 
|                     |           |             |            |         |                   | 15.2.7.253/24     | 
| pod-1/bl205-eu-spdc | vlan68    | up          | up         | 68      | 00:22:BD:F8:19:FF | 192.168.1.1/24    | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | 70      | 00:22:BD:F8:19:FF | 15.100.161.254/25 | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | 72      | 00:22:BD:CD:C1:BB | 15.2.61.254/24    | 
+---------------------+-----------+-------------+------------+---------+-------------------+-------------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view addr

{
    "duration": 1681,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 990,
        "total_time": 1392
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

True	402	-	connect apic11o.emea-sp.cisco.com
True	300	13	apic11o.emea-sp.cisco.com class fabricNode
True	391	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	299	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)