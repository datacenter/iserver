# Contract

## Standard Contract

Use '--type standard' to get standard contracts details
- contract name and tenant
- properties (scope, intent and target DSCP)
- subject and filters
- details of all filters used by selected contracts
- standard contracts usage (consumer and provider EPG)

```
# iserver get aci contract --apic apic21 --type standard --tenant k8s

Apic: apic21

Standard Contracts
------------------

+---------------+---------+---------+-------------+---------------+----------------+
| Contract      | Scope   | Intent  | Target DSCP | Subject       | Filter         |
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/BT-Demo   | context | install | unspecified | k8s/Any       | k8s/alltraffic | 
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/k8s_tn_bm | global  | install | unspecified | k8s/k8s_tn_bm | common/any     | 
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/k8s_tn_vm | global  | install | unspecified | k8s/k8s_tn_bm | common/any     | 
+---------------+---------+---------+-------------+---------------+----------------+

Contract Filters
----------------

+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/any     | any        | ipv4  |          |       | no        | no       |        |             |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Standard Contracts Usage
------------------------

+---------------+---------------------+------------------------------+
| Contract      | Consumer EPG        | Provider EPG                 |
+---------------+---------------------+------------------------------+
| k8s/BT-Demo   | k8s/k8s_ANP/SRIoV_A | k8s/k8s_ANP/SRIoV_A          | 
+---------------+---------------------+------------------------------+
| k8s/k8s_tn_bm |                     | k8s/bml3_k8s/bml3_k8s_ExtEPG | 
+---------------+---------------------+------------------------------+
| k8s/k8s_tn_vm |                     | k8s/vl3_k8s/vl3_k8s_ExtEPG   | 
+---------------+---------------------+------------------------------+
```

Developer

```
# iserver get aci contract --apic apic21 --type standard --tenant k8s

{
    "duration": 1634,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 1001,
        "total_time": 1413
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

True	412	-	connect apic21o.emea-sp.cisco.com
True	349	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	341	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	311	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./Contract.md)