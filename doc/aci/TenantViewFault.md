# Tenant

## Fault view

```
# iserver get aci tenant --apic apic21 --name k8s --view fault

Apic: apic21 (mode:online, cache:off)

Tenant - Faults [#9]
--------------------

+--------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Tenant | Sev | Code  | Cause                | Created Time                  | Lifecycle | Description                                                                      |
+--------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:15:09.613+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |           | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |           | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |           | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |           | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |           | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:17:11.715+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |           | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |           | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:12.252+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:28.444+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |           | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |           | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:12.254+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|        |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|        |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:17:11.712+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |           | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |           | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:28.440+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |           | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |           | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:05.674+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |           | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |           | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |           | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |           | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |           | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:15:15.541+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |           | interface assigned to it;                                                        | 
+--------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci tenant --apic apic21 --name k8s --view fault

{
    "duration": 1546,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 839,
        "total_time": 1227
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

True	388	-	connect apic21o.emea-sp.cisco.com:443
True	514	12	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	325	21	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./Tenant.md)