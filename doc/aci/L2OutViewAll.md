# L2Out

## All view

```
# iserver get aci l2out --apic apic21 --when any --view all

Apic: apic21 (mode:online, cache:off)

L2Out [#2]
----------

+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| Faults  | L2 Out         | Target DSCP | Bridge Domain  | Encapsulation | Ext Phy Domain | Path                                                            |
+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| 0 0 0 0 | common/default | unspecified | common/default | unknown       |                |                                                                 | 
+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| 0 0 3 0 | k8s/Test       | unspecified | k8s/Test       | vlan-666      | Infra_L2dom    | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
|         |                |             |                |               |                | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+

L2Out - Nodes [#2]
------------------

+---------+----------------+----------------+------------+
| Faults  | L2Out          | Node           | Interfaces |
+---------+----------------+----------------+------------+
| 0 0 0 0 | common/default |                |            | 
+---------+----------------+----------------+------------+
| 0 0 3 0 | k8s/Test       | cl2207-eu-spdc | 3          | 
|         |                | cl2208-eu-spdc | 2          | 
+---------+----------------+----------------+------------+

L2Out - Interfaces [#2]
-----------------------

+---------+----------------+----------------+-----------+
| Faults  | L2Out          | Node           | Interface |
+---------+----------------+----------------+-----------+
| 0 0 0 0 | common/default |                |           | 
+---------+----------------+----------------+-----------+
| 0 0 3 0 | k8s/Test       | cl2207-eu-spdc | eth1/2/3  | 
|         |                | cl2207-eu-spdc | eth1/30   | 
|         |                | cl2207-eu-spdc | po4       | 
|         |                | cl2208-eu-spdc | eth1/2/3  | 
|         |                | cl2208-eu-spdc | po8       | 
+---------+----------------+----------------+-----------+

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

L2Out - Event Logs last 10y [#2]
--------------------------------

+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
| L2Out          | Sev  | Code     | Cause      | Created Time                  | Description   | Change Set                                                         |
+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
| common/default | Info | E4212437 | transition | 2020-12-15T12:33:29.587+02:00 | RsEBd created | encap:unknown, forceResolve:yes, rType:mo, state:formed,           | 
|                |      |          |            |                               |               | stateQual:default-target, tCl:fvBD, tDn:uni/tn-common/BD-default,  | 
|                |      |          |            |                               |               | tRn:BD-default, tType:name                                         | 
+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+
| common/default | Info | E4212437 | transition | 2020-12-09T20:07:28.270+02:00 | RsEBd created | encap:unknown, forceResolve:yes, rType:mo, state:formed,           | 
|                |      |          |            |                               |               | stateQual:default-target, tCl:fvBD, tDn:uni/tn-common/BD-default,  | 
|                |      |          |            |                               |               | tRn:BD-default, tType:name                                         | 
+----------------+------+----------+------------+-------------------------------+---------------+--------------------------------------------------------------------+

L2Out - Audit Logs last 10y [#9]
--------------------------------

+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| L2Out    | Sev  | Code     | Cause      | Created Time                  | Description                                                                     | Change Set                                                               |
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212443 | transition | 2023-05-05T14:08:52.099+02:00 | RsPathL2OutAtt topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp]  | tDn:topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp],     | 
|          |      |          |            |                               | created                                                                         | targetDscp:unspecified, userdom::all:common:                             | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212440 | transition | 2023-05-05T13:07:47.171+02:00 | RsL2DomAtt created                                                              | tDn:uni/l2dom-Infra_L2dom, userdom::all:common:                          | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212443 | transition | 2023-05-05T13:07:47.171+02:00 | RsPathL2OutAtt topology/pod-1/paths-2207/pathep-[eth1/30] created               | tDn:topology/pod-1/paths-2207/pathep-[eth1/30], targetDscp:unspecified,  | 
|          |      |          |            |                               |                                                                                 | userdom::all:common:                                                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212428 | transition | 2023-05-05T13:07:47.170+02:00 | LIfP default created                                                            | name:default, tag:yellow-green, userdom::all:common:                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4214168 | transition | 2023-05-05T13:07:47.170+02:00 | RsCustQosPol created                                                            | userdom:all                                                              | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212431 | transition | 2023-05-05T13:07:47.170+02:00 | LNodeP default created                                                          | name:default, tag:yellow-green, userdom::all:common:                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212425 | transition | 2023-05-05T13:07:47.169+02:00 | InstP L2Out-ext-epg created                                                     | floodOnEncap:disabled, matchT:AtleastOne, name:L2Out-ext-epg,            | 
|          |      |          |            |                               |                                                                                 | prefGrMemb:exclude, prio:unspecified, targetDscp:unspecified,            | 
|          |      |          |            |                               |                                                                                 | userdom::all:common:                                                     | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212437 | transition | 2023-05-05T13:07:47.169+02:00 | RsEBd created                                                                   | encap:vlan-666, tnFvBDName:Test, userdom:all                             | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| k8s/Test | Info | E4212434 | transition | 2023-05-05T13:07:47.168+02:00 | Out Test created                                                                | name:Test, targetDscp:unspecified, userdom::all:common:                  | 
+----------+------+----------+------------+-------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --when any --view all

{
    "duration": 4223,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 428,
        "disconnect_time": 0,
        "mo_time": 3130,
        "total_time": 3558
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
True	327	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	328	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	348	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/l2out-default query rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf
True	338	3	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=faults,no-scoped,subtree
True	383	27	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	383	4	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	379	9	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
True	329	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/l2out-Test query rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf
True	315	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./L2Out.md)