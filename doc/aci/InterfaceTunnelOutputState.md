# Node Interface - Virtual Port Channel (VPC)

## Default state focused output

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+----------------+-----------------------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Tunnel Type | Type                          | Req            | Source         | Destination                 | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+----------------+-----------------------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                      | isis           | 10.3.192.64/32 | 10.3.32.64 (bl206-eu-spdc)  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                      | isis           | 10.3.192.64/32 | 10.3.32.65 (s102-eu-spdc)   | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                      | isis           | 10.3.192.64/32 | 10.3.192.65 (s101-eu-spdc)  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                      | isis           | 10.3.192.64/32 | 10.3.40.67                  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                      | isis           | 10.3.192.64/32 | 10.3.192.67 (cl201-eu-spdc) | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                      | isis           | 10.3.192.64/32 | 10.3.192.68 (cl202-eu-spdc) | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4       | isis           | 10.3.192.64/32 | 10.3.40.64                  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac      | isis           | 10.3.192.64/32 | 10.3.40.65                  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6       | isis           | 10.3.192.64/32 | 10.3.40.66                  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                      |                | 10.3.192.64/32 | 10.3.0.1 (apic1)            | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical                      |                | 10.3.192.64/32 | 10.3.0.2 (apic2)            | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical                      |                | 10.3.192.64/32 | 10.3.0.3 (apic3)            | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                      |                | 10.3.192.64/32 | 172.16.11.1/32              | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical            |                | 10.3.192.64/32 | 172.16.21.1/32              | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | inst-overlay-1 | 10.3.192.64/32 | 172.16.30.88                | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | inst-overlay-1 | 10.3.192.64/32 | 172.16.30.121               | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | inst-overlay-1 | 10.3.192.64/32 | 172.16.30.161               | overlay-1 | 9000 | 
+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+----------------+-----------------------------+-----------+------+
```

Developer

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc

{
    "duration": 1265,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 688,
        "total_time": 1080
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

True	392	-	connect apic11o.emea-sp.cisco.com
True	348	11	apic11o.emea-sp.cisco.com class fabricNode
True	340	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/tunnelIf
```

[[Back]](./InterfaceTunnel.md)