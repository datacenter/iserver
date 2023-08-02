# L2Out

## Fault view

```
# iserver get aci l2out --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)

L2Out - Faults [#3]
-------------------

+----------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| L2Out    | Sev | Code  | Cause                | Created Time                  | Lifecycle | Description                                                                      |
+----------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:43:12.254+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:43:12.252+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:15:15.541+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
+----------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --view fault

{
    "duration": 1607,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 992,
        "total_time": 1434
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

True	442	-	connect apic21o.emea-sp.cisco.com:443
True	342	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	321	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	329	3	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./L2Out.md)