# Attachable Access Entity Profile (AAEP)

## Diag view

```
# iserver get aci aaep --apic apic11 --when 60d --view diag

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - Faults [#4]
-----------------------------------------------------

+---------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| Name          | Sev  | Code  | Cause             | Created Time                  | Lifecycle | Description                                                                     |
+---------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| DC-CFP-AEP    | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.292+02:00 | raised    | Failed to form relation to MO uni/l3dom-DC-CFP-EXT-DOMAIN of class l3extDomP    | 
| ESX-CDC_AAEP  | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.308+02:00 | raised    | Failed to form relation to MO uni/l3dom-smi5Gc-ExtR_L3Dom of class l3extDomP    | 
| ESX_AAEP      | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.312+02:00 | raised    | Failed to form relation to MO uni/phys-ESX_PhysDom of class physDomP            | 
| SR-Infra_AAEP | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.324+02:00 | raised    | Failed to form relation to MO uni/l3dom-SR-Infra-CDC-3_L3Dom of class l3extDomP | 
+---------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+

Attachable Access Entity Profile (AAEP) - Fault Records last 60d [#16]
----------------------------------------------------------------------

+-----------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| Name            | Sev  | Code  | Cause             | Created Time                  | Lifecycle | Description                                                                     |
+-----------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| DC-CFP-AEP      | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.293+02:00 | raised    | Failed to form relation to MO uni/l3dom-DC-CFP-EXT-DOMAIN of class l3extDomP    | 
| DC-CFP-AEP      | Warn | F1003 | resolution-failed | 2023-06-12T10:35:04.973+02:00 |           | Failed to form relation to MO uni/l3dom-DC-CFP-EXT-DOMAIN of class l3extDomP    | 
| ESX-CDC_AAEP    | Warn | F0982 | resolution-failed | 2023-07-17T10:22:26.386+02:00 |           | Failed to form relation to MO uni/tn-TESTING_BRUNO/ap-UntitledAP1/epg-SITE1 of  | 
|                 |      |       |                   |                               |           | class fvAEPg                                                                    | 
| ESX-CDC_AAEP    | Warn | F0982 | resolution-failed | 2023-07-17T10:22:26.249+02:00 | raised    | Failed to form relation to MO uni/tn-TESTING_BRUNO/ap-UntitledAP1/epg-SITE1 of  | 
|                 |      |       |                   |                               |           | class fvAEPg                                                                    | 
| ESX-CDC_AAEP    | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.309+02:00 | raised    | Failed to form relation to MO uni/l3dom-smi5Gc-ExtR_L3Dom of class l3extDomP    | 
| ESX-CDC_AAEP    | Warn | F1003 | resolution-failed | 2023-06-12T10:35:04.971+02:00 |           | Failed to form relation to MO uni/l3dom-smi5Gc-ExtR_L3Dom of class l3extDomP    | 
| ESX-R3DC_AAEP   | Warn | F0982 | resolution-failed | 2023-07-10T15:52:22.913+02:00 |           | Failed to form relation to MO                                                   | 
|                 |      |       |                   |                               |           | uni/tn-MPC-E/ap-Tunnel-Termination/epg-Tunnel-Termination of class fvAEPg       | 
| ESX-R3DC_AAEP   | Warn | F0982 | resolution-failed | 2023-07-10T15:52:22.821+02:00 | raised    | Failed to form relation to MO                                                   | 
|                 |      |       |                   |                               |           | uni/tn-MPC-E/ap-Tunnel-Termination/epg-Tunnel-Termination of class fvAEPg       | 
| ESX_AAEP        | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.313+02:00 | raised    | Failed to form relation to MO uni/phys-ESX_PhysDom of class physDomP            | 
| ESX_AAEP        | Warn | F1003 | resolution-failed | 2023-06-12T10:35:04.920+02:00 |           | Failed to form relation to MO uni/phys-ESX_PhysDom of class physDomP            | 
| SR-Infra_AAEP   | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.325+02:00 | raised    | Failed to form relation to MO uni/l3dom-SR-Infra-CDC-3_L3Dom of class l3extDomP | 
| SR-Infra_AAEP   | Warn | F1003 | resolution-failed | 2023-06-12T10:35:04.977+02:00 |           | Failed to form relation to MO uni/l3dom-SR-Infra-CDC-3_L3Dom of class l3extDomP | 
| UCSB1-R3DC_AAEP | Warn | F0982 | resolution-failed | 2023-07-10T15:52:22.937+02:00 |           | Failed to form relation to MO                                                   | 
|                 |      |       |                   |                               |           | uni/tn-MPC-E/ap-Tunnel-Termination/epg-Tunnel-Termination of class fvAEPg       | 
| UCSB1-R3DC_AAEP | Warn | F0982 | resolution-failed | 2023-07-10T15:52:22.845+02:00 | raised    | Failed to form relation to MO                                                   | 
|                 |      |       |                   |                               |           | uni/tn-MPC-E/ap-Tunnel-Termination/epg-Tunnel-Termination of class fvAEPg       | 
| UCSB1_AAEP      | Warn | F0982 | resolution-failed | 2023-07-17T10:22:26.410+02:00 |           | Failed to form relation to MO uni/tn-TESTING_BRUNO/ap-UntitledAP1/epg-SITE1 of  | 
|                 |      |       |                   |                               |           | class fvAEPg                                                                    | 
| UCSB1_AAEP      | Warn | F0982 | resolution-failed | 2023-07-17T10:22:26.233+02:00 | raised    | Failed to form relation to MO uni/tn-TESTING_BRUNO/ap-UntitledAP1/epg-SITE1 of  | 
|                 |      |       |                   |                               |           | class fvAEPg                                                                    | 
+-----------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+

Attachable Access Entity Profile (AAEP) - Event Logs last 60d [#0]
------------------------------------------------------------------
None

Attachable Access Entity Profile (AAEP) - Audit Logs last 60d [#0]
------------------------------------------------------------------
None
```

Developer

```
# iserver get aci aaep --apic apic11 --when 60d --view diag

{
    "duration": 7864,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 7115,
        "total_time": 7515
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

True	400	-	connect apic11o.emea-sp.cisco.com:443
True	383	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	320	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	320	4	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=faults,no-scoped,subtree
True	2508	783	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1750	4	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1834	70	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./Aaep.md)