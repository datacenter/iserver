# Attachable Access Entity Profile (AAEP)

## Intf view

```
# iserver get aci aaep --apic apic11 --view intf

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - Interfaces [#30]
----------------------------------------------------------

+---------+-----------------------------+---------------+-----------+-----------+
| Faults  | Name                        | Node          | Intf Type | Intf Name |
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | cvim-brAPI_AAEP             | cl201-eu-spdc | l1PhysIf  | eth1/24   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/68   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/24   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/68   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | cvim1-SRIOV_AAEP            | cl201-eu-spdc | l1PhysIf  | eth1/12   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/15   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/3    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/6    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/9    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/12   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/15   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/3    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/6    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/9    | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | cvim4-SRIOV_AAEP            | cl201-eu-spdc | l1PhysIf  | eth1/51   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/54   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/57   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/60   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/63   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/66   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/51   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/54   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/57   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/60   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/63   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/66   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | DC-CFP                      | bl205-eu-spdc | l1PhysIf  | eth1/28   | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/28   | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/29   | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/29   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 1 | DC-CFP-AEP                  |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | default                     |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 1 | ESX-CDC_AAEP                | cl201-eu-spdc | l1PhysIf  | eth1/31   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/32   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/33   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/34   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/35   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/36   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/37   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/38   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/39   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/40   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/41   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/42   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/43   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/44   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/45   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/46   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/47   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/31   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/32   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/33   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/34   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/35   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/36   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/37   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/38   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/39   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/40   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/41   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/42   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/43   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/44   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/45   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/46   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/47   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | ESX-R3DC_AAEP               | rl301-eu-spdc | l1PhysIf  | eth1/24/1 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/24/2 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/25/1 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/25/2 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/25/3 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/25/4 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/26/1 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/26/2 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/26/3 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/26/4 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/27/1 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/27/2 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/27/3 | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/27/4 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/24/1 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/24/2 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/25/1 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/25/2 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/25/3 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/25/4 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/26/1 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/26/2 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/26/3 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/26/4 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/27/1 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/27/2 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/27/3 | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/27/4 | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 1 | ESX_AAEP                    |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | F5-ADC_AAEP                 |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | HX1_AAEP                    | bl205-eu-spdc | l1PhysIf  | eth1/11   | 
|         |                             | bl205-eu-spdc | l1PhysIf  | eth1/12   | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/11   | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/12   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | IKS1-mgmt_AAEP              | cl201-eu-spdc | l1PhysIf  | eth1/71   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/71   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | IKS2-mgmt_AAEP              | cl201-eu-spdc | l1PhysIf  | eth1/72   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/72   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | Infra-2_AAEP                |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | Infra_AAEP                  | cl201-eu-spdc | l1PhysIf  | eth1/96   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/96   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | Infra_L3_AAEP               | bl205-eu-spdc | l1PhysIf  | eth1/24   | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/24   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | multipodL3Out_AAEP          |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | multipodL3Out_EntityProfile |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | nidemo-dummy                | rl301-eu-spdc | l1PhysIf  | eth1/28   | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/28   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | pod1a_AAEP                  | cl201-eu-spdc | l1PhysIf  | eth1/1    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/10   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/11   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/13   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/14   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/2    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/23   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/27   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/4    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/5    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/7    | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/8    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/1    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/10   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/11   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/13   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/14   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/2    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/23   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/27   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/4    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/5    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/7    | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/8    | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | pod4a_AAEP                  | cl201-eu-spdc | l1PhysIf  | eth1/49   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/50   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/52   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/53   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/55   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/56   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/58   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/59   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/61   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/62   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/64   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/65   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/67   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/49   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/50   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/52   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/53   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/55   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/56   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/58   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/59   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/61   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/62   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/64   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/65   | 
|         |                             | cl202-eu-spdc | l1PhysIf  | eth1/67   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | Private5G_AAEP              | bl205-eu-spdc | l1PhysIf  | eth1/15   | 
|         |                             | bl205-eu-spdc | l1PhysIf  | eth1/16   | 
|         |                             | bl205-eu-spdc | l1PhysIf  | eth1/17   | 
|         |                             | bl205-eu-spdc | l1PhysIf  | eth1/18   | 
|         |                             | bl205-eu-spdc | l1PhysIf  | eth1/19   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/81   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/82   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/83   | 
|         |                             | cl201-eu-spdc | l1PhysIf  | eth1/84   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | RL-L3Out_EntityProfile      |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | SPN_AAEP                    | bl205-eu-spdc | l1PhysIf  | eth1/27   | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/27   | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | SR-Infra-CDC-2_AAEP         |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | SR-Infra-RDC-3_AAEP         |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | SR-Infra-RDC-4_AAEP         |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 1 | SR-Infra_AAEP               |               |           |           | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | UCSB1-R3DC_AAEP             | rl301-eu-spdc | l1PhysIf  | eth1/3    | 
|         |                             | rl301-eu-spdc | l1PhysIf  | eth1/4    | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/3    | 
|         |                             | rl302-eu-spdc | l1PhysIf  | eth1/4    | 
+---------+-----------------------------+---------------+-----------+-----------+
| 0 0 0 0 | UCSB1_AAEP                  | bl205-eu-spdc | l1PhysIf  | eth1/1    | 
|         |                             | bl205-eu-spdc | l1PhysIf  | eth1/2    | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/1    | 
|         |                             | bl206-eu-spdc | l1PhysIf  | eth1/2    | 
+---------+-----------------------------+---------------+-----------+-----------+
```

Developer

```
# iserver get aci aaep --apic apic11 --view intf

{
    "duration": 19002,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 370,
        "disconnect_time": 0,
        "mo_time": 17881,
        "total_time": 18251
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

True	370	-	connect apic11o.emea-sp.cisco.com:443
True	392	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	298	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	469	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra-CDC-2_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	501	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-multipodL3Out_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	501	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra-RDC-4_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	596	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Infra_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	311	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	502	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-IKS2-mgmt_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	593	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-RL-L3Out_EntityProfile query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	610	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-cvim-brAPI_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	599	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Infra_L3_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	601	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-HX1_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	521	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-UCSB1-R3DC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	626	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-cvim4-SRIOV_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	475	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra-RDC-3_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	579	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-ESX_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	594	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-ESX-CDC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	579	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-UCSB1_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	530	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-DC-CFP-AEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	495	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SPN_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	596	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-DC-CFP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	503	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Infra-2_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	602	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-pod4a_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	701	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-ESX-R3DC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	698	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-pod1a_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	605	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-IKS1-mgmt_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	606	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-cvim1-SRIOV_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	458	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-SR-Infra_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	537	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-Private5G_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	697	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-default query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	497	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-nidemo-dummy query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	492	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-F5-ADC_AAEP query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
True	517	1	apic11o.emea-sp.cisco.com:443 mo uni/infra/attentp-multipodL3Out_EntityProfile query rsp-subtree-include=full-deployment&target-node=all&target-path=AttEntityPToPthIf
```

[[Back]](./Aaep.md)