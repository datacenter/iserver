# Application Profile

## All view

```
# iserver get aci ap --apic apic21 --name *k8s* --when 7d --view all

Apic: apic21 (mode:online, cache:off)

Application Profile [#1]
------------------------

+--------+---------+---------------------+------------------+-------------+
| Health | Faults  | Application Profile | Application EPGs | Priority    |
+--------+---------+---------------------+------------------+-------------+
| 95     | 0 0 2 0 | k8s/k8s_ANP         | k8s/backbone1    | unspecified | 
|        |         |                     | k8s/bmk8s_1      |             | 
|        |         |                     | k8s/bmk8s_2      |             | 
|        |         |                     | k8s/bmk8s_prov   |             | 
|        |         |                     | k8s/csr1_lan     |             | 
|        |         |                     | k8s/csr2_lan     |             | 
|        |         |                     | k8s/csr_b2b      |             | 
|        |         |                     | k8s/MGMT         |             | 
|        |         |                     | k8s/site1_lan    |             | 
|        |         |                     | k8s/site1_pe     |             | 
|        |         |                     | k8s/site2_lan    |             | 
|        |         |                     | k8s/site2_pe     |             | 
|        |         |                     | k8s/SRIoV_A      |             | 
|        |         |                     | k8s/SRIoV_B      |             | 
|        |         |                     | k8s/Test         |             | 
|        |         |                     | k8s/vk8s_1       |             | 
|        |         |                     | k8s/vk8s_2       |             | 
|        |         |                     | k8s/vk8s_3       |             | 
|        |         |                     | k8s/vk8s_4       |             | 
+--------+---------+---------------------+------------------+-------------+

Application Profile - Nodes [#1]
--------------------------------

+---------+---------------------+----------------+------------+
| Faults  | Application Profile | Node           | Interfaces |
+---------+---------------------+----------------+------------+
| 0 0 2 0 | k8s/k8s_ANP         | cl2207-eu-spdc | 26         | 
|         |                     | cl2208-eu-spdc | 26         | 
+---------+---------------------+----------------+------------+

Application Profile - Interfaces [#1]
-------------------------------------

+---------+---------------------+----------------+-----------+
| Faults  | Application Profile | Node           | Interface |
+---------+---------------------+----------------+-----------+
| 0 0 2 0 | k8s/k8s_ANP         | cl2207-eu-spdc | eth1/1/1  | 
|         |                     | cl2207-eu-spdc | eth1/1/2  | 
|         |                     | cl2207-eu-spdc | eth1/1/3  | 
|         |                     | cl2207-eu-spdc | eth1/1/4  | 
|         |                     | cl2207-eu-spdc | eth1/2/1  | 
|         |                     | cl2207-eu-spdc | eth1/2/2  | 
|         |                     | cl2207-eu-spdc | eth1/2/3  | 
|         |                     | cl2207-eu-spdc | eth1/3/1  | 
|         |                     | cl2207-eu-spdc | eth1/3/2  | 
|         |                     | cl2207-eu-spdc | eth1/3/3  | 
|         |                     | cl2207-eu-spdc | eth1/3/4  | 
|         |                     | cl2207-eu-spdc | eth1/4/1  | 
|         |                     | cl2207-eu-spdc | eth1/4/2  | 
|         |                     | cl2207-eu-spdc | eth1/4/3  | 
|         |                     | cl2207-eu-spdc | eth1/5/1  | 
|         |                     | cl2207-eu-spdc | eth1/5/2  | 
|         |                     | cl2207-eu-spdc | eth1/5/3  | 
|         |                     | cl2207-eu-spdc | eth1/5/4  | 
|         |                     | cl2207-eu-spdc | eth1/6/1  | 
|         |                     | cl2207-eu-spdc | eth1/6/2  | 
|         |                     | cl2207-eu-spdc | eth1/6/3  | 
|         |                     | cl2207-eu-spdc | po2       | 
|         |                     | cl2207-eu-spdc | po3       | 
|         |                     | cl2207-eu-spdc | po4       | 
|         |                     | cl2207-eu-spdc | po7       | 
|         |                     | cl2207-eu-spdc | po8       | 
|         |                     | cl2208-eu-spdc | eth1/1/1  | 
|         |                     | cl2208-eu-spdc | eth1/1/2  | 
|         |                     | cl2208-eu-spdc | eth1/1/3  | 
|         |                     | cl2208-eu-spdc | eth1/1/4  | 
|         |                     | cl2208-eu-spdc | eth1/2/1  | 
|         |                     | cl2208-eu-spdc | eth1/2/2  | 
|         |                     | cl2208-eu-spdc | eth1/2/3  | 
|         |                     | cl2208-eu-spdc | eth1/3/1  | 
|         |                     | cl2208-eu-spdc | eth1/3/2  | 
|         |                     | cl2208-eu-spdc | eth1/3/3  | 
|         |                     | cl2208-eu-spdc | eth1/3/4  | 
|         |                     | cl2208-eu-spdc | eth1/4/1  | 
|         |                     | cl2208-eu-spdc | eth1/4/2  | 
|         |                     | cl2208-eu-spdc | eth1/4/3  | 
|         |                     | cl2208-eu-spdc | eth1/5/1  | 
|         |                     | cl2208-eu-spdc | eth1/5/2  | 
|         |                     | cl2208-eu-spdc | eth1/5/3  | 
|         |                     | cl2208-eu-spdc | eth1/5/4  | 
|         |                     | cl2208-eu-spdc | eth1/6/1  | 
|         |                     | cl2208-eu-spdc | eth1/6/2  | 
|         |                     | cl2208-eu-spdc | eth1/6/3  | 
|         |                     | cl2208-eu-spdc | po4       | 
|         |                     | cl2208-eu-spdc | po5       | 
|         |                     | cl2208-eu-spdc | po6       | 
|         |                     | cl2208-eu-spdc | po7       | 
|         |                     | cl2208-eu-spdc | po8       | 
+---------+---------------------+----------------+-----------+

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

Application Profile - Fault Records last 7d [#116]
--------------------------------------------------

+---------------------+-----+-------+----------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| Application Profile | Sev | Code  | Cause                | Created Time                  | Lifecycle | Description                                                                     |
+---------------------+-----+-------+----------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| k8s/k8s_ANP         | Maj | F3083 | config-error         | 2023-07-26T08:03:42.002+02:00 |           | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                     |     |       |                      |                               |           | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1;         | 
|                     |     |       |                      |                               |           | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;). This can happen when  | 
|                     |     |       |                      |                               |           | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                     |     |       |                      |                               |           | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP         | Maj | F3083 | config-error         | 2023-07-26T08:03:40.663+02:00 | soaking   | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                     |     |       |                      |                               |           | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1;         | 
|                     |     |       |                      |                               |           | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;). This can happen when  | 
|                     |     |       |                      |                               |           | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                     |     |       |                      |                               |           | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.761+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.760+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.759+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.757+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.755+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.754+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.752+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.752+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.750+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.750+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.749+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.748+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.747+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.746+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.745+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.744+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.743+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.741+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.739+02:00 |           | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.728+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.727+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.727+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.726+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.725+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.724+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.723+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.722+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.721+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.720+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.720+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.718+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.717+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.716+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.715+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.714+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.712+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.710+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.708+02:00 |           | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.274+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.273+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.272+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.271+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.270+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.268+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.268+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.267+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.266+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.266+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.265+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.264+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.263+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.261+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.261+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.260+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.259+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.258+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.257+02:00 | raised    | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.910+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.909+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.908+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.908+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.907+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.905+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.904+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.903+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.903+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.902+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.901+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.901+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.900+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.899+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.898+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.897+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.896+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.895+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.894+02:00 | raised    | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.918+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.917+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.916+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.915+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.914+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.913+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.912+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.911+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.910+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.909+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.907+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.907+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.906+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.905+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.904+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.903+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.902+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.901+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.900+02:00 | soaking   | Fault delegate: Configuration failed for node 2208 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.893+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.891+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.891+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.890+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.888+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.887+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.886+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.885+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.884+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.882+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.881+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.880+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.879+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.878+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.877+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.876+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.875+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.873+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
| k8s/k8s_ANP         | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.871+02:00 | soaking   | Fault delegate: Configuration failed for node 2207 due to Invalid Path          | 
|                     |     |       |                      |                               |           | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10  | 
|                     |     |       |                      |                               |           | :Either the EpG is not associated with a domain or the domain does not have     | 
|                     |     |       |                      |                               |           | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated   | 
|                     |     |       |                      |                               |           | with a domain or the domain does not have this interface assigned to it;        | 
+---------------------+-----+-------+----------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+

Application Profile - Event Logs last 7d [#1]
---------------------------------------------

+---------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| Application Profile | Sev  | Code     | Cause      | Created Time                  | Description                                                          |
+---------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP         | Info | E4209236 | transition | 2023-07-26T08:03:41.872+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+---------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+

Application Profile - Audit Logs last 7d [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci ap --apic apic21 --name *k8s* --when 7d --view all

{
    "duration": 21834,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 455,
        "disconnect_time": 0,
        "mo_time": 14081,
        "total_time": 14536
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

True	455	-	connect apic21o.emea-sp.cisco.com:443
True	420	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	507	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	387	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	660	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/ap-k8s_ANP query rsp-subtree-include=full-deployment&target-node=all&target-path=ApToNwIf
True	365	12	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=faults,no-scoped,subtree
True	6303	3494	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	3986	4027	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1453	1943	apic21o.emea-sp.cisco.com:443 class fvAp query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ApplicationProfile.md)