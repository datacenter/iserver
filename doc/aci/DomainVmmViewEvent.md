# VMM Domain

## Event view

```
# iserver get aci domain vmm --apic apic21 --name *cdc* --when any --view event

Apic: apic21 (mode:online, cache:off)

VMM Domain - Event Logs last 10y [#1]
-------------------------------------

+----------------+------+----------+-------------------------+-------------------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Domain         | Sev  | Code     | Cause                   | Created Time                  | Description                                                                  | Change Set                                                                    |
+----------------+------+----------+-------------------------+-------------------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4205018 | user-association-formed | 2021-01-05T20:41:53.340+02:00 | Association from VMM Controller:                                             | forceResolve:yes, rType:mo, state:formed, stateQual:none, tCl:vmmUsrAccP,     | 
|                |      |          |                         |                               | uni/vmmp-VMware/dom-EU-SPDC-CDC-22/ctrlr-EU-SPDC-CDC-22 to User Account:     | tDn:uni/vmmp-VMware/dom-EU-SPDC-CDC-22/usracc-EU-SPDC-CDC-22_Cred, tType:mo,  | 
|                |      |          |                         |                               | uni/vmmp-VMware/dom-EU-SPDC-CDC-22/usracc-EU-SPDC-CDC-22_Cred is Established | userdom::all:common:                                                          | 
+----------------+------+----------+-------------------------+-------------------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --name *cdc* --when any --view event

{
    "duration": 2808,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 486,
        "disconnect_time": 0,
        "mo_time": 1781,
        "total_time": 2267
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

True	486	-	connect apic21o.emea-sp.cisco.com:443
True	503	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	787	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	491	8	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./DomainVmm.md)