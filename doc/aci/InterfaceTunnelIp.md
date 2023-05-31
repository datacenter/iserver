# Node Interface - Tunnel

## Filter by IP address

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc --ip 10.3.192.67

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+-------+-------------+----------+------+----------------+-----------------------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Tunnel Type | Type     | Req  | Source         | Destination                 | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+-------------+----------+------+----------------+-----------------------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical | isis | 10.3.192.64/32 | 10.3.192.67 (cl201-eu-spdc) | overlay-1 | 9000 | 
+---------------------+-----------+-------+------+-------+-------------+----------+------+----------------+-----------------------------+-----------+------+
```

Developer

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc --ip 10.3.192.67

{
    "duration": 1129,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 621,
        "total_time": 1024
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

True	403	-	connect apic11o.emea-sp.cisco.com
True	307	11	apic11o.emea-sp.cisco.com class fabricNode
True	314	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/tunnelIf
```

[[Back]](./InterfaceTunnel.md)