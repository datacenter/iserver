# Taboo Contract

## Usage view

```
# iserver get aci contract taboo --apic apic21 --name k8s/my* --view usage

Apic: apic21 (mode:online, cache:off)

Taboo Contract - Usage [#1]
---------------------------

+---------+---------------------+---------------------+
| Faults  | Taboo               | Protected EPG       |
+---------+---------------------+---------------------+
| 0 0 0 0 | k8s/MyTabooContract | k8s/k8s_ANP/SRIoV_A | 
+---------+---------------------+---------------------+
```

Developer

```
# iserver get aci contract taboo --apic apic21 --name k8s/my* --view usage

{
    "duration": 1575,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 428,
        "disconnect_time": 0,
        "mo_time": 1027,
        "total_time": 1455
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

True	428	-	connect apic21o.emea-sp.cisco.com:443
True	337	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	332	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	358	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractTaboo.md)