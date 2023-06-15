# Node Interface - Port Channel (PC)

## Multi-APIC

```
# iserver get aci intf pc --apic dom:milan --node any

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc
Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Apic   | Node                 | Id   | Name                     | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+--------+----------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| apic11 | pod-1/bl205-eu-spdc  | po1  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po2  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po3  | SPN_PolGrp               | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po4  | UCSB1-FI-B_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl205-eu-spdc  | po5  | UCSB1-FI-A_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po1  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po2  | UCSB1-FI-B_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po3  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po4  | UCSB1-FI-A_PolGrp        | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/bl206-eu-spdc  | po5  | SPN_PolGrp               | up    | enabled   | up    |                           | active    | 105        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po1  | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po2  | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po3  | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl201-eu-spdc  | po4  | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po5  | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po6  | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po7  | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po8  | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po9  | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po10 | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po11 | pod1a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po12 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po13 | pod-4a-br-API            | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po14 | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po15 | pod4a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po16 | pod4a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po17 | pod4a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po18 | pod4a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po19 | pod4a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po20 | pod4a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po21 | pod4a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po22 | pod4a-MX_PolGrp          | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po23 | pod4a-COMP-3-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po24 | pod4a-COMP-3-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po25 | pod4a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po26 | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po27 | pod4a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl201-eu-spdc  | po28 | pod4a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po1  | pod1a-NVBench_PolGrp     | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl202-eu-spdc  | po2  | pod1a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po3  | pod1a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po4  | pod1a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po5  | pod1a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po6  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po7  | pod1a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po8  | pod1a-MX_PolGrp          | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl202-eu-spdc  | po9  | pod1a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po10 | pod1a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po11 | pod1a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po12 | pod1a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po13 | pod1a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po14 | pod4a-AIO-3-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po15 | pod4a-COMP-1-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po16 | pod4a-MX_PolGrp          | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| apic11 | pod-1/cl202-eu-spdc  | po17 | pod4a-COMP-3-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po18 | pod4a-COMP-1-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po19 | pod4a-COMP-2-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po20 | pod4a-AIO-1-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po21 | pod4a-AIO-2-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po22 | pod4a-COMP-2-PET_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po23 | pod4a-AIO-3-SAMX_PolGrp  | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po24 | pod4a-AIO-1-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po25 | pod1a-API_PolGrp         | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po26 | pod4a-AIO-2-PET_PolGrp   | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po27 | pod4a-COMP-3-SAMX_PolGrp | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/cl202-eu-spdc  | po28 | pod-4a-br-API            | up    | enabled   | up    |                           | active    | 100        | 1            | 
| apic11 | pod-1/rl301-eu-spdc  | po1  | UCSB1-R3DC-FI-A_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic11 | pod-1/rl301-eu-spdc  | po2  | UCSB1-R3DC-FI-B_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic11 | pod-1/rl302-eu-spdc  | po1  | UCSB1-R3DC-FI-B_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic11 | pod-1/rl302-eu-spdc  | po2  | UCSB1-R3DC-FI-A_PolGrp   | up    | enabled   | up    |                           | active    | 300        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po1  | SPN_PolGrp               | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po2  | ESX22-CDC-22_PolGrp      | up    | enabled   | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po3  | UCSB1-FI-B_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po4  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po5  | UCSB1-FI-A_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2205-eu-spdc | po6  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po1  | UCSB1-FI-B_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po2  | ESX22-CDC-22_PolGrp      | up    | enabled   | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po3  | HX1-FI-A_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po4  | HX1-FI-B_PolGrp          | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po5  | UCSB1-FI-A_PolGrp        | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/bl2206-eu-spdc | po6  | SPN_PolGrp               | up    | disabled  | up    |                           | active    | 256        | 1            | 
| apic21 | pod-1/cl2201-eu-spdc | po1  | ESX20-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 212        | 0            | 
| apic21 | pod-1/cl2201-eu-spdc | po2  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 212        | 1            | 
| apic21 | pod-1/cl2202-eu-spdc | po1  | ESX20-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 212        | 0            | 
| apic21 | pod-1/cl2202-eu-spdc | po2  | Infra_PolGrp             | up    | enabled   | up    |                           | active    | 212        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po1  | ESX21-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2207-eu-spdc | po2  | k8s_ocp_bm_3_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2207-eu-spdc | po3  | k8s_ocp_bm_4_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po4  | k8s_ocp_bm_5_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po5  | k8s_esx71_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po6  | k8s_esx72_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po7  | k8s_ocp_bm_1_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2207-eu-spdc | po8  | k8s_ocp_bm_2_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po1  | ESX21-CDC-22_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2208-eu-spdc | po2  | k8s_ocp_bm_3_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 278        | 0            | 
| apic21 | pod-1/cl2208-eu-spdc | po3  | k8s_ocp_bm_4_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po4  | k8s_ocp_bm_5_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po5  | k8s_esx71_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po6  | k8s_esx72_PolGrp         | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po7  | k8s_ocp_bm_1_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/cl2208-eu-spdc | po8  | k8s_ocp_bm_2_PolGrp      | up    | enabled   | up    |                           | active    | 278        | 1            | 
| apic21 | pod-1/rl2701-eu-spdc | po1  | UCSB1-R7DC-FI-A_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
| apic21 | pod-1/rl2701-eu-spdc | po2  | UCSB1-R7DC-FI-B_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
| apic21 | pod-1/rl2702-eu-spdc | po1  | UCSB1-R7DC-FI-A_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
| apic21 | pod-1/rl2702-eu-spdc | po2  | UCSB1-R7DC-FI-B_PolGrp   | up    | disabled  | up    |                           | active    | 227        | 1            | 
+--------+----------------------+------+--------------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic dom:milan --node any

{
    "duration": 17869,
    "apic": {
        "read": true,
        "success": 54,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 52,
        "connect_time": 955,
        "disconnect_time": 0,
        "mo_time": 15983,
        "total_time": 16938
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

True	416	-	connect apic11o.emea-sp.cisco.com
True	303	13	apic11o.emea-sp.cisco.com class fabricNode
True	539	-	connect apic21o.emea-sp.cisco.com
True	310	15	apic21o.emea-sp.cisco.com class fabricNode
True	304	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	294	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	306	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	337	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	279	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	288	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	354	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	307	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	373	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	289	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	325	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	287	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	285	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	318	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	315	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	301	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	334	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	296	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	285	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	320	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	327	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	345	6	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	282	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/vpcDom
True	297	6	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205/sys/vpc/inst/dom-256 query query-target=children&target-subtree-class=vpcIf
True	308	6	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	295	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/vpcDom
True	291	6	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206/sys/vpc/inst/dom-256 query query-target=children&target-subtree-class=vpcIf
True	316	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	290	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/vpcDom
True	301	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201/sys/vpc/inst/dom-212 query query-target=children&target-subtree-class=vpcIf
True	320	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	278	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/vpcDom
True	287	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202/sys/vpc/inst/dom-212 query query-target=children&target-subtree-class=vpcIf
True	319	8	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	288	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/vpcDom
True	301	8	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207/sys/vpc/inst/dom-278 query query-target=children&target-subtree-class=vpcIf
True	302	8	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	360	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/vpcDom
True	327	8	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208/sys/vpc/inst/dom-278 query query-target=children&target-subtree-class=vpcIf
True	309	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	296	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	286	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	278	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/vpcDom
True	297	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701/sys/vpc/inst/dom-227 query query-target=children&target-subtree-class=vpcIf
True	282	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	290	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/vpcDom
True	298	2	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702/sys/vpc/inst/dom-227 query query-target=children&target-subtree-class=vpcIf
True	435	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	287	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)