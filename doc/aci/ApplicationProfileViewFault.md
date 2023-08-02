# Application Profile

## Fault view

```
# iserver get aci ap --apic apic21 --name *k8s* --view fault

Apic: apic21 (mode:online, cache:off)

Application Profile - Faults [#2]
---------------------------------

+---------------------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Application Profile | Sev | Code  | Cause                | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-06-18T09:15:09.613+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|                     |     |       |                      |                               |           | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|                     |     |       |                      |                               |           | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|                     |     |       |                      |                               |           | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|                     |     |       |                      |                               |           | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|                     |     |       |                      |                               |           | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-06-18T09:43:05.674+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|                     |     |       |                      |                               |           | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|                     |     |       |                      |                               |           | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|                     |     |       |                      |                               |           | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|                     |     |       |                      |                               |           | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|                     |     |       |                      |                               |           | domain, associated with both EPG and Port, that has required VLAN;               | 
+---------------------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s* --view fault

{
    "duration": 2653,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 509,
        "disconnect_time": 0,
        "mo_time": 1747,
        "total_time": 2256
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

True	509	-	connect apic21o.emea-sp.cisco.com:443
True	377	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	504	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	423	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	443	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ApplicationProfile.md)