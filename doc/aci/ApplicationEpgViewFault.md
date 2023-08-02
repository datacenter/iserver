# Application Endpoint Group (EPG)

## Fault view

```
# iserver get aci epg --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)

EPG - Faults [#12]
------------------

+------------------------------------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| EPG                                | Sev | Code  | Cause                | Created Time                  | Lifecycle | Description                                                                      |
+------------------------------------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| k8s/k8s_ANP/MGMT                   | Min | F0467 | configuration-failed | 2023-06-18T09:15:09.613+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|                                    |     |       |                      |                               |           | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|                                    |     |       |                      |                               |           | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|                                    |     |       |                      |                               |           | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|                                    |     |       |                      |                               |           | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|                                    |     |       |                      |                               |           | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s/k8s_ANP/MGMT                   | Min | F0467 | configuration-failed | 2023-06-18T09:43:05.674+02:00 | raised    | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|                                    |     |       |                      |                               |           | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|                                    |     |       |                      |                               |           | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|                                    |     |       |                      |                               |           | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|                                    |     |       |                      |                               |           | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|                                    |     |       |                      |                               |           | domain, associated with both EPG and Port, that has required VLAN;               | 
| SPN_IntraLab/SPN_Connect_ANP/TEST2 | Min | F0467 | configuration-failed | 2023-06-18T09:18:24.895+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|                                    |     |       |                      |                               |           | uni/tn-SPN_IntraLab/ap-SPN_Connect_ANP/epg-TEST2 node 2206 SPN_PolGrp due to     | 
|                                    |     |       |                      |                               |           | Invalid VLAN Configuration, debug message: invalid-vlan: vlan-2200 :Either the   | 
|                                    |     |       |                      |                               |           | EpG is not associated with a domain or the domain does not have this vlan        | 
|                                    |     |       |                      |                               |           | assigned to it;                                                                  | 
| SPN_IntraLab/SPN_Connect_ANP/TEST2 | Min | F0467 | configuration-failed | 2023-06-18T09:45:22.256+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|                                    |     |       |                      |                               |           | uni/tn-SPN_IntraLab/ap-SPN_Connect_ANP/epg-TEST2 node 2205 SPN_PolGrp due to     | 
|                                    |     |       |                      |                               |           | Invalid VLAN Configuration, debug message: invalid-vlan: vlan-2200 :Either the   | 
|                                    |     |       |                      |                               |           | EpG is not associated with a domain or the domain does not have this vlan        | 
|                                    |     |       |                      |                               |           | assigned to it;                                                                  | 
| vEPC_demo/vEPG_ANP/vEPG_ACC        | Min | F0467 | configuration-failed | 2023-06-18T09:43:27.504+02:00 | raised    | Fault delegate: Configuration failed for node 2201 sys/lsnode-10.58.234.138 due  | 
|                                    |     |       |                      |                               |           | to Invalid Path Configuration, debug message: invalid-path: Interface does not   | 
|                                    |     |       |                      |                               |           | exist;                                                                           | 
| vEPC_demo/vEPG_ANP/vEPG_CTRL       | Min | F0467 | configuration-failed | 2023-06-18T09:43:27.502+02:00 | raised    | Fault delegate: Configuration failed for node 2201 sys/lsnode-10.58.234.138 due  | 
|                                    |     |       |                      |                               |           | to Invalid Path Configuration, debug message: invalid-path: Interface does not   | 
|                                    |     |       |                      |                               |           | exist;                                                                           | 
| vEPC_demo/vEPG_ANP/vEPG_INT        | Min | F0467 | configuration-failed | 2023-06-18T09:43:36.031+02:00 | raised    | Fault delegate: Configuration failed for node 2201 sys/lsnode-10.58.234.138 due  | 
|                                    |     |       |                      |                               |           | to Invalid Path Configuration, debug message: invalid-path: Interface does not   | 
|                                    |     |       |                      |                               |           | exist;                                                                           | 
| vEPC_demo/vEPG_ANP/vEPG_MGMT       | Min | F0467 | configuration-failed | 2023-06-18T09:43:07.632+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|                                    |     |       |                      |                               |           | uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT node 2207 eth1/10/4 due to Invalid    | 
|                                    |     |       |                      |                               |           | Path Configuration, debug message: invalid-path: Interface does not exist;       | 
| vEPC_demo/vEPG_ANP/vEPG_MGMT       | Min | F0467 | configuration-failed | 2023-06-18T09:43:07.622+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|                                    |     |       |                      |                               |           | uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT node 2207 eth1/10/3 due to Invalid    | 
|                                    |     |       |                      |                               |           | Path Configuration, debug message: invalid-path: Interface does not exist;       | 
| vEPC_demo/vEPG_ANP/vEPG_MGMT       | Min | F0467 | configuration-failed | 2023-06-18T09:43:07.616+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|                                    |     |       |                      |                               |           | uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT node 2207 eth1/10/1 due to Invalid    | 
|                                    |     |       |                      |                               |           | Path Configuration, debug message: invalid-path: Interface does not exist;       | 
| vEPC_demo/vEPG_ANP/vEPG_MGMT       | Min | F0467 | configuration-failed | 2023-06-18T09:43:07.627+02:00 | raised    | Fault delegate: Configuration failed for                                         | 
|                                    |     |       |                      |                               |           | uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT node 2207 eth1/10/2 due to Invalid    | 
|                                    |     |       |                      |                               |           | Path Configuration, debug message: invalid-path: Interface does not exist;       | 
| vEPC_demo/vEPG_ANP/vEPG_MGMT       | Min | F0467 | configuration-failed | 2023-06-18T09:43:36.029+02:00 | raised    | Fault delegate: Configuration failed for node 2201 sys/lsnode-10.58.234.138 due  | 
|                                    |     |       |                      |                               |           | to Invalid Path Configuration, debug message: invalid-path: Interface does not   | 
|                                    |     |       |                      |                               |           | exist;                                                                           | 
+------------------------------------+-----+-------+----------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --view fault

{
    "duration": 2146,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 522,
        "disconnect_time": 0,
        "mo_time": 1257,
        "total_time": 1779
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

True	522	-	connect apic21o.emea-sp.cisco.com:443
True	507	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	382	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	368	12	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ApplicationEpg.md)