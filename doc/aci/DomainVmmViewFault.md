# VMM Domain

## Fault view

```
# iserver get aci domain vmm --apic apic21 --name *cdc* --view fault

Apic: apic21 (mode:online, cache:off)

VMM Domain - Faults [#6]
------------------------

+----------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Domain         | Sev | Code  | Cause              | Created Time                  | Lifecycle | Description                                                                      |
+----------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-06-19T14:01:51.640+02:00 | raised    | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-06-19T14:21:51.755+02:00 | raised    | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj | F1313 | operational-issues | 2023-06-20T17:26:09.864+02:00 | raised    | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |     |       |                    |                               |           | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:30, error: [Could not find        | 
|                |     |       |                    |                               |           | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj | F1313 | operational-issues | 2023-06-20T17:26:09.869+02:00 | raised    | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |     |       |                    |                               |           | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:31, error: [Could not find        | 
|                |     |       |                    |                               |           | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-07-26T17:14:15.281+02:00 | raised    | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-07-26T17:32:49.442+02:00 | raised    | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
+----------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --name *cdc* --view fault

{
    "duration": 2365,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 1542,
        "total_time": 2005
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

True	463	-	connect apic21o.emea-sp.cisco.com:443
True	385	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	773	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	384	16	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./DomainVmm.md)