# Contract

## Filter by name

Example: name

```
# iserver get aci contract --apic apic21 --type filter --name alltraffic

Apic: apic21 (mode:online, cache:off)

Contract Filters
----------------

+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter               | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| vEPC_demo/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/alltraffic    | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/alltraffic       | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Contract Filters Usage
----------------------

+----------------------+-----------------------------+-------+
| Filter               | Contract                    | Taboo |
+----------------------+-----------------------------+-------+
| vEPC_demo/alltraffic | vEPC_demo/vEPG_ACC          |       | 
|                      | vEPC_demo/vEPG_INT          |       | 
|                      | vEPC_demo/vEPG_SX           |       | 
+----------------------+-----------------------------+-------+
| common/alltraffic    | common/IKSHS-alltraffic     |       | 
|                      | common/vEPG-MGMT_alltraffic |       | 
+----------------------+-----------------------------+-------+
| k8s/alltraffic       | k8s/BT-Demo                 |       | 
+----------------------+-----------------------------+-------+
```

Example: tenant and name

```
# iserver get aci contract --apic apic21 --type filter --name k8s/*

Apic: apic21 (mode:online, cache:off)

Contract Filters
----------------

+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination   | Rules |
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |               |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/http       | http       | ipv4  |          | tcp   | no        | no       |        | http - http   |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/https      | https      | ipv4  |          | tcp   | no        | no       |        | https - https |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/icmp       | icmp       | ipv4  |          | icmp  | no        | no       |        |               |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/ssh        | ssh        | ipv4  |          | tcp   | no        | no       |        | ssh - ssh     |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+

Contract Filters Usage
----------------------

+----------------+-------------+---------------------+
| Filter         | Contract    | Taboo               |
+----------------+-------------+---------------------+
| k8s/alltraffic | k8s/BT-Demo |                     | 
+----------------+-------------+---------------------+
| k8s/http       |             |                     | 
+----------------+-------------+---------------------+
| k8s/https      |             |                     | 
+----------------+-------------+---------------------+
| k8s/icmp       |             | k8s/MyTabooContract | 
+----------------+-------------+---------------------+
| k8s/ssh        |             |                     | 
+----------------+-------------+---------------------+
```

Developer

```
# iserver get aci contract --apic apic21 --type filter --name alltraffic

{
    "duration": 2659,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 452,
        "disconnect_time": 0,
        "mo_time": 1870,
        "total_time": 2322
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

True	452	-	connect apic21o.emea-sp.cisco.com:443
True	354	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	437	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	352	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	360	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	367	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./Contract.md)