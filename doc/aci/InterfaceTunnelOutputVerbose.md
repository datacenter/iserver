# Node Interface - Virtual Port Channel (VPC)

## Verbose output

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --id tunnel16
    --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Interface Tunnel
----------------
- Interface          : tunnel16
- Admin State        : up
- Oper State         : up
- Reason             : 
- Tunnel Layer       : l3
- Tunnel Type        : ivxlan
- Type               : dci-ucast,fabric-ext,physical
- Source IP          : 10.3.192.64
- Destination IP     : 172.16.30.161
- Destiation Node    :
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
    "duration": 1101,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 618,
        "total_time": 1028
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

True	410	-	connect apic11o.emea-sp.cisco.com
True	298	13	apic11o.emea-sp.cisco.com class fabricNode
True	320	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/tunnelIf
```

[[Back]](./InterfaceTunnel.md)