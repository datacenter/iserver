# Node Protocol - IS-IS

## Tun view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tun

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tun

{
    "duration": 834,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 301,
        "total_time": 701
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

True	400	-	connect apic11o.emea-sp.cisco.com:443
True	301	13	apic11o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./ProtocolIsis.md)