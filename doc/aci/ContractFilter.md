# Contract

## Contract Filter

Use '--type filter' to get contract filters details
- filter name and tenant
- properties
    - Ethernet Type
    - IP Protocol
    - match only fragments
    - stateful
    - source range
    - destination range
    - TCP rules
- filter usage (standard and taboo contracts)

```
# iserver get aci contract --apic apic21 --type filter --tenant k8s/*

Apic: apic21 (mode:online, cache:off)
```

Developer

```
# iserver get aci contract --apic apic21 --type filter --tenant k8s/*

{
    "duration": 944,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 368,
        "total_time": 790
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

True	422	-	connect apic21o.emea-sp.cisco.com:443
True	368	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./Contract.md)