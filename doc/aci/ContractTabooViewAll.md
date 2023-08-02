# Taboo Contract

## All view

```
# iserver get aci contract taboo
    --apic apic21
    --name k8s/my*
    --when any
    --view all

Apic: apic21 (mode:online, cache:off)

Taboo Contract [#1]
-------------------

+---------+---------------------+--------------------+----------+
| Faults  | Taboo               | Subject            | Filter   |
+---------+---------------------+--------------------+----------+
| 0 0 0 0 | k8s/MyTabooContract | k8s/MyTabooSubject | k8s/icmp | 
+---------+---------------------+--------------------+----------+

Contract Filter [#1]
--------------------

+---------+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Faults  | Filter   | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+---------+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| 0 0 0 0 | k8s/icmp | icmp  | ipv4  |          | icmp  | no        | no       |        |             |       | 
+---------+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Taboo Contract - Usage [#1]
---------------------------

+---------+---------------------+---------------------+
| Faults  | Taboo               | Protected EPG       |
+---------+---------------------+---------------------+
| 0 0 0 0 | k8s/MyTabooContract | k8s/k8s_ANP/SRIoV_A | 
+---------+---------------------+---------------------+

Taboo Contract - Faults [#0]
----------------------------
None

Taboo Contract - Fault Records last 10y [#0]
--------------------------------------------
None

Taboo Contract - Event Logs last 10y [#0]
-----------------------------------------
None

Taboo Contract - Audit Logs last 10y [#3]
-----------------------------------------

+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| Taboo Contract      | Sev  | Code     | Cause      | Created Time                  | Description                   | Change Set                                 |
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| k8s/MyTabooContract | Info | E4213703 | transition | 2023-05-02T16:12:41.616+02:00 | TSubj MyTabooSubject created  | name:MyTabooSubject, userdom::all:common:  | 
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| k8s/MyTabooContract | Info | E4213679 | transition | 2023-05-02T16:12:41.616+02:00 | RsDenyRule icmp created       | tnVzFilterName:icmp, userdom::all:common:  | 
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| k8s/MyTabooContract | Info | E4213706 | transition | 2023-05-02T16:12:41.616+02:00 | Taboo MyTabooContract created | name:MyTabooContract, userdom::all:common: | 
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
```

Developer

```
# iserver get aci contract taboo
    --apic apic21
    --name k8s/my*
    --when any
    --view all

{
    "duration": 3179,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 431,
        "disconnect_time": 0,
        "mo_time": 2542,
        "total_time": 2973
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

True	431	-	connect apic21o.emea-sp.cisco.com:443
True	335	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	329	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	360	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	336	0	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=faults,no-scoped,subtree
True	409	0	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	381	6	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	392	3	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ContractTaboo.md)