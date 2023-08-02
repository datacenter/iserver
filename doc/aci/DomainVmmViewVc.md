# VMM Domain

## Vc view

```
# iserver get aci domain vmm --apic apic21 --view vc

Apic: apic21 (mode:online, cache:off)

VMM Domain - vCenter [#4]
-------------------------

+---------+----------------+-------------------+-----------------+----------------------+-----------------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| Faults  | Domain Name    | Controller Faults | Controller Name | IP                   | Username                    | Online | Model                                      | Serial   | Rev   | Datacenter | HV | VM  |
+---------+----------------+-------------------+-----------------+----------------------+-----------------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| 0 6 0 0 | EU-SPDC-CDC-22 | 0 7 0 0           | EU-SPDC-CDC-22  | 10.58.28.18          | admin@admin.local           | V      | VMware vCenter Server 7.0.3 build-21958406 | 53aba35e | 7.0.3 | eu-spdc-dc | 34 | 332 | 
+---------+----------------+-------------------+-----------------+----------------------+-----------------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| 0 1 0 0 | EU-SPDC-POD2B  | 0 1 0 0           | EU-SPDC-POD2B   | 10.58.29.66          | administrator@vsphere.local | V      | VMware vCenter Server 7.0.3 build-21477706 | 1175d77b | 7.0.3 | k8s-DC     | 2  | 32  | 
+---------+----------------+-------------------+-----------------+----------------------+-----------------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| 0 4 0 0 | EU-SPDC-R7DC   | 0 5 0 0           | EU-SPDC-R7DC    | 10.58.28.18          | administrator@admin.local   | V      | VMware vCenter Server 7.0.3 build-21958406 | 53aba35e | 7.0.3 | eu-spdc-dc | 34 | 332 | 
+---------+----------------+-------------------+-----------------+----------------------+-----------------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| 0 5 0 0 | vEPC-Dataplane | 0 6 0 0           | vc-eu-spdc      | vc-eu-spdc.cisco.com | admin@admin.local           | V      | VMware vCenter Server 7.0.3 build-21958406 | 53aba35e | 7.0.3 | eu-spdc-dc | 34 | 332 | 
+---------+----------------+-------------------+-----------------+----------------------+-----------------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view vc

{
    "duration": 2493,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 445,
        "disconnect_time": 0,
        "mo_time": 1257,
        "total_time": 1702
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

True	445	-	connect apic21o.emea-sp.cisco.com:443
True	428	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	829	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
```

[[Back]](./DomainVmm.md)