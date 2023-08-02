# Attachable Access Entity Profile (AAEP)

## Node view

```
# iserver get aci aaep --apic apic11 --view node

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - Nodes [#30]
-----------------------------------------------------

+---------+-----------------------------+---------------+------------+
| Faults  | Name                        | Node          | Interfaces |
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | cvim-brAPI_AAEP             | cl201-eu-spdc | 2          | 
|         |                             | cl202-eu-spdc | 2          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | cvim1-SRIOV_AAEP            | cl201-eu-spdc | 5          | 
|         |                             | cl202-eu-spdc | 5          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | cvim4-SRIOV_AAEP            | cl201-eu-spdc | 6          | 
|         |                             | cl202-eu-spdc | 6          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | DC-CFP                      | bl205-eu-spdc | 1          | 
|         |                             | bl206-eu-spdc | 1          | 
|         |                             | rl301-eu-spdc | 1          | 
|         |                             | rl302-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 1 | DC-CFP-AEP                  |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | default                     |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 1 | ESX-CDC_AAEP                | cl201-eu-spdc | 17         | 
|         |                             | cl202-eu-spdc | 17         | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | ESX-R3DC_AAEP               | rl301-eu-spdc | 14         | 
|         |                             | rl302-eu-spdc | 14         | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 1 | ESX_AAEP                    |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | F5-ADC_AAEP                 |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | HX1_AAEP                    | bl205-eu-spdc | 2          | 
|         |                             | bl206-eu-spdc | 2          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | IKS1-mgmt_AAEP              | cl201-eu-spdc | 1          | 
|         |                             | cl202-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | IKS2-mgmt_AAEP              | cl201-eu-spdc | 1          | 
|         |                             | cl202-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | Infra-2_AAEP                |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | Infra_AAEP                  | cl201-eu-spdc | 1          | 
|         |                             | cl202-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | Infra_L3_AAEP               | bl205-eu-spdc | 1          | 
|         |                             | bl206-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | multipodL3Out_AAEP          |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | multipodL3Out_EntityProfile |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | nidemo-dummy                | rl301-eu-spdc | 1          | 
|         |                             | rl302-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | pod1a_AAEP                  | cl201-eu-spdc | 12         | 
|         |                             | cl202-eu-spdc | 12         | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | pod4a_AAEP                  | cl201-eu-spdc | 13         | 
|         |                             | cl202-eu-spdc | 13         | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | Private5G_AAEP              | bl205-eu-spdc | 5          | 
|         |                             | cl201-eu-spdc | 4          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | RL-L3Out_EntityProfile      |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | SPN_AAEP                    | bl205-eu-spdc | 1          | 
|         |                             | bl206-eu-spdc | 1          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | SR-Infra-CDC-2_AAEP         |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | SR-Infra-RDC-3_AAEP         |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | SR-Infra-RDC-4_AAEP         |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 1 | SR-Infra_AAEP               |               |            | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | UCSB1-R3DC_AAEP             | rl301-eu-spdc | 2          | 
|         |                             | rl302-eu-spdc | 2          | 
+---------+-----------------------------+---------------+------------+
| 0 0 0 0 | UCSB1_AAEP                  | bl205-eu-spdc | 2          | 
|         |                             | bl206-eu-spdc | 2          | 
+---------+-----------------------------+---------------+------------+
```

Developer

```
# iserver get aci aaep --apic apic11 --view node

{
    "duration": 18780,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 17669,
        "total_time": 18115
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

True	446	-	connect apic11o.emea-sp.cisco.com:443
True	415	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	325	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	536	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra-CDC-2_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	609	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-multipodL3Out_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	597	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra-RDC-4_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	504	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Infra_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	291	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	529	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-IKS2-mgmt_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	483	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-RL-L3Out_EntityProfile query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	506	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-cvim-brAPI_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	605	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Infra_L3_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	610	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-HX1_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	604	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-UCSB1-R3DC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	605	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-cvim4-SRIOV_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	603	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra-RDC-3_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	608	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-ESX_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	511	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-ESX-CDC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	589	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-UCSB1_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	591	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-DC-CFP-AEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	484	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SPN_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	508	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-DC-CFP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	466	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Infra-2_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	623	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-pod4a_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	598	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-ESX-R3DC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	558	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-pod1a_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	497	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-IKS1-mgmt_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	530	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-cvim1-SRIOV_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	609	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	505	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Private5G_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	482	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-default query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	697	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-nidemo-dummy query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	499	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-F5-ADC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	492	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-multipodL3Out_EntityProfile query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
```

[[Back]](./Aaep.md)