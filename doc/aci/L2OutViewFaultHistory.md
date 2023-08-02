# L2Out

## Fault history view

```
# iserver get aci l2out --apic apic21 --when any --view hfault

Apic: apic21 (mode:online, cache:off)

L2Out - Fault Records last 10y [#27]
------------------------------------

+----------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| L2Out    | Sev | Code  | Cause                | Created Time                  | Lifecycle | Description                                                                      |
+----------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.624+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.622+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.621+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.619+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:17:30.936+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T09:15:16.851+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T01:03:43.975+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T01:03:43.974+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-18T01:03:42.947+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.710+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.693+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.965+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.963+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.961+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.957+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-31T22:23:05.520+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-31T22:20:50.355+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T21:08:58.038+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T21:08:58.036+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T21:06:35.540+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T21:06:35.538+02:00 | soaking   | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T19:59:58.360+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T19:59:58.270+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T19:59:58.240+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T18:38:12.111+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T18:38:12.038+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|          |     |       |                      |                               |           | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|          |     |       |                      |                               |           | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|          |     |       |                      |                               |           | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|          |     |       |                      |                               |           | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|          |     |       |                      |                               |           | interface assigned to it;                                                        | 
| k8s/Test | Min | F0467 | configuration-failed | 2023-05-30T18:38:12.036+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|          |     |       |                      |                               |           | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|          |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|          |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have      | 
|          |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|          |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;         | 
+----------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --when any --view hfault

{
    "duration": 2017,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1048,
        "total_time": 1484
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

True	436	-	connect apic21o.emea-sp.cisco.com:443
True	329	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	325	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	394	27	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./L2Out.md)