# Node Interface - SVI

## Filter by IP address

```
# iserver get aci intf svi
    --apic apic11
    --node bl205-eu-spdc
    --ip 15.3.64.128
    --view addr

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+-------------------+----------------+
| Node                | Interface | Admin State | Oper State | Vlan ID | MAC               | IPv4           |
+---------------------+-----------+-------------+------------+---------+-------------------+----------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 1       | 00:22:BD:3D:C3:CC | 15.3.64.254/24 | 
+---------------------+-----------+-------------+------------+---------+-------------------+----------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic11
    --node bl205-eu-spdc
    --ip 15.3.64.128
    --view addr

{
    "duration": 1760,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 1170,
        "total_time": 1592
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	305	11	apic11o.emea-sp.cisco.com class fabricNode
True	493	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	372	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)