# Contract Filter

## Usage view

```
# iserver get aci contract filter --apic apic21 --name k8s/icmp --view usage

Apic: apic21 (mode:online, cache:off)

Contract Filter - Usage [#1]
----------------------------

+---------+----------+----------+-----------------------+
| Faults  | Filter   | Contract | Taboo                 |
+---------+----------+----------+-----------------------+
| 0 0 0 0 | k8s/icmp |          | vEPC_demo/alltraffic  | 
|         |          |          | common/alltraffic     | 
|         |          |          | k8s/alltraffic        | 
|         |          |          | common/any            | 
|         |          |          | nidemo/any            | 
|         |          |          | common/arp            | 
|         |          |          | common/default        | 
|         |          |          | common/est            | 
|         |          |          | common/http           | 
|         |          |          | hefernan_ni-demo/HTTP | 
|         |          |          | nidemo/http           | 
|         |          |          | k8s/http              | 
|         |          |          | mgmt/http-filter      | 
|         |          |          | common/https          | 
|         |          |          | nidemo/https          | 
|         |          |          | k8s/https             | 
|         |          |          | mgmt/https-filter     | 
|         |          |          | common/icmp           | 
|         |          |          | nidemo/icmp           | 
|         |          |          | k8s/icmp              | 
|         |          |          | mgmt/icmp-filter      | 
|         |          |          | mgmt/inband-default   | 
|         |          |          | mgmt/ntp-filter       | 
|         |          |          | mgmt/snmp-filter      | 
|         |          |          | nidemo/sql            | 
|         |          |          | common/ssh            | 
|         |          |          | nidemo/ssh            | 
|         |          |          | k8s/ssh               | 
|         |          |          | mgmt/ssh-filter       | 
|         |          |          | vEPC/vEPC_alltraffic  | 
+---------+----------+----------+-----------------------+
```

Developer

```
# iserver get aci contract filter --apic apic21 --name k8s/icmp --view usage

{
    "duration": 1701,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 1103,
        "total_time": 1525
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
True	363	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	377	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	363	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./ContractFilter.md)