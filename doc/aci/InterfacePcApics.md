# Node Interface - Port Channel (PC)

## Multi-APIC

```
# iserver get aci intf pc --apic dom:milan --node any

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Apic   | Node                 | Id   | Name                     | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+--------+----------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| apic11 | pod-1/bl205-eu-spdc  | po1  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po2  | SPN_PolGrp               | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po3  | UCSB1-FI-B_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po4  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po5  | UCSB1-FI-A_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po1  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po2  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po3  | UCSB1-FI-B_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po4  | UCSB1-FI-A_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po5  | SPN_PolGrp               | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po1  | pod-4a-br-API            | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po2  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po3  | pod4a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po4  | pod1a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po5  | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po6  | pod4a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po7  | pod4a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po8  | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po9  | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po10 | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po11 | pod4a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po12 | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl201-eu-spdc  | po13 | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po14 | pod4a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po15 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po16 | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po17 | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po18 | pod4a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po19 | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po20 | pod4a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po21 | pod4a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po22 | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po23 | pod4a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po24 | pod4a-COMP-3-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po25 | pod4a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po26 | pod4a-COMP-3-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po27 | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po28 | pod4a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po1  | pod4a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po2  | pod4a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po3  | pod4a-COMP-3-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po4  | pod4a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po5  | pod4a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po6  | pod4a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po7  | pod4a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po8  | pod4a-COMP-3-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po9  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po10 | pod4a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po11 | pod4a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po12 | pod4a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po13 | pod4a-MX_PolGrp          | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl202-eu-spdc  | po14 | pod-4a-br-API            | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po15 | pod4a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po16 | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po17 | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po18 | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po19 | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po20 | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po21 | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po22 | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po23 | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po24 | pod1a-MX_PolGrp          | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl202-eu-spdc  | po25 | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl202-eu-spdc  | po26 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po27 | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po28 | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/rl301-eu-spdc  | po1  | UCSB1-R3DC-FI-A_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic11 | pod-1/rl301-eu-spdc  | po2  | UCSB1-R3DC-FI-B_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic11 | pod-1/rl302-eu-spdc  | po1  | UCSB1-R3DC-FI-B_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic11 | pod-1/rl302-eu-spdc  | po2  | UCSB1-R3DC-FI-A_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po1  | UCSB1-FI-A_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po2  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po3  | SPN_PolGrp               | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po4  | ESX22-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 256        | 0            | 
| apic21 | pod-1/bl2205-eu-spdc | po5  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po6  | UCSB1-FI-B_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po1  | ESX22-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 256        | 0            | 
| apic21 | pod-1/bl2206-eu-spdc | po2  | UCSB1-FI-B_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po3  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po4  | UCSB1-FI-A_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po5  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po6  | SPN_PolGrp               | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/cl2201-eu-spdc | po1  | ESX20-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 212        | 0            | 
| apic21 | pod-1/cl2201-eu-spdc | po2  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 212        | 1            | 
| apic21 | pod-1/cl2202-eu-spdc | po1  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 212        | 1            | 
| apic21 | pod-1/cl2202-eu-spdc | po2  | ESX20-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 212        | 0            | 
| apic21 | pod-1/cl2207-eu-spdc | po1  | ESX21-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2207-eu-spdc | po2  | k8s_ocp_bm_3_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2207-eu-spdc | po3  | k8s_ocp_bm_4_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po4  | k8s_ocp_bm_5_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po5  | k8s_esx71_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po6  | k8s_esx72_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po7  | k8s_ocp_bm_1_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po8  | k8s_ocp_bm_2_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po1  | ESX21-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2208-eu-spdc | po2  | k8s_esx71_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po3  | k8s_esx72_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po4  | k8s_ocp_bm_1_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po5  | k8s_ocp_bm_2_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po6  | k8s_ocp_bm_3_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2208-eu-spdc | po7  | k8s_ocp_bm_4_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po8  | k8s_ocp_bm_5_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/rl2701-eu-spdc | po1  | UCSB1-R7DC-FI-A_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
| apic21 | pod-1/rl2701-eu-spdc | po2  | UCSB1-R7DC-FI-B_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
| apic21 | pod-1/rl2702-eu-spdc | po1  | UCSB1-R7DC-FI-B_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
| apic21 | pod-1/rl2702-eu-spdc | po2  | UCSB1-R7DC-FI-A_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
+--------+----------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

[[Back]](./InterfacePc.md)