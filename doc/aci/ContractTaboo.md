# Contract

## Taboo Contract

Use '--type taboo' to get taboo contracts details
- contract name and tenant
- subject and filters
- details of all filters used by selected taboo contracts
- taboo contracts usage (protected EPG)

```
# iserver get aci contract --apic apic21 --type taboo --tenant k8s

Apic: apic21 (mode:online, cache:off)

Taboo Contracts
---------------

+---------------------+--------------------+----------+
| Taboo               | Subject            | Filter   |
+---------------------+--------------------+----------+
| k8s/MyTabooContract | k8s/MyTabooSubject | k8s/icmp | 
+---------------------+--------------------+----------+

Contract Filters
----------------

+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter   | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/icmp | icmp  | ipv4  |          | icmp  | no        | no       |        |             |       | 
+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Taboo Contracts Usage
---------------------

+---------------------+---------------------+
| Taboo               | Protected EPG       |
+---------------------+---------------------+
| k8s/MyTabooContract | k8s/k8s_ANP/SRIoV_A | 
+---------------------+---------------------+
```

Developer

```
# iserver get aci contract --apic apic21 --type taboo --tenant k8s

{
    "duration": 1834,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 491,
        "disconnect_time": 0,
        "mo_time": 1084,
        "total_time": 1575
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

True	491	-	connect apic21o.emea-sp.cisco.com:443
True	354	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	350	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	380	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./Contract.md)