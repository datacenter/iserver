# Node Interface - Virtual Port Channel (VPC)

## Verbose output

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --id tunnel16
    --view verbose

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

Interface tunnel
----------------
- Interface          : tunnel16
- Admin State        : up
- Oper State         : up
- Reason             : 
- Tunnel Layer       : l3
- Tunnel Type        : ivxlan
- Type               : dci-ucast,fabric-ext,physical
- Source             : 10.3.192.64/32
- Destination        : 172.16.30.88
- VRF                : overlay-1
- MTU                : 9000
- Keepalive Interval : 10
- Keepalive Retries  : 3
```

Developer

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --id tunnel16
    --view verbose

{
    "duration": 1301,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 494,
        "disconnect_time": 0,
        "mo_time": 673,
        "total_time": 1167
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

True	494	-	connect apic11o.emea-sp.cisco.com
True	373	11	apic11o.emea-sp.cisco.com class fabricNode
True	300	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/tunnelIf
```

[[Back]](./InterfaceTunnel.md)