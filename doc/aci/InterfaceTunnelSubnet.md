# Node Interface - Tunnel

## Filter by IP subnet

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --subnet 172.16.30.0/24

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+----------------+---------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Tunnel Type | Type                          | Req            | Source         | Destination   | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+----------------+---------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | inst-overlay-1 | 10.3.192.64/32 | 172.16.30.88  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | inst-overlay-1 | 10.3.192.64/32 | 172.16.30.121 | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | inst-overlay-1 | 10.3.192.64/32 | 172.16.30.161 | overlay-1 | 9000 | 
+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+----------------+---------------+-----------+------+
```

Developer

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --subnet 172.16.30.0/24

{
    "duration": 1137,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 633,
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

True	391	-	connect apic11o.emea-sp.cisco.com
True	314	11	apic11o.emea-sp.cisco.com class fabricNode
True	319	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/tunnelIf
```

[[Back]](./InterfaceTunnel.md)