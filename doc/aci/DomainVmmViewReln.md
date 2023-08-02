# VMM Domain

## Reln view

```
# iserver get aci domain vmm --apic apic21 --view reln

Apic: apic21 (mode:online, cache:off)

VMM Domain - Policy Relationships [#4]
--------------------------------------

+---------+----------------+-----------------+------------------------------------+
| Faults  | Domain         | Policy Type     | Policy Name                        |
+---------+----------------+-----------------+------------------------------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | Application EPG | SPN_IntraLab/SPN_Connect_ANP/TEST2 | 
|         |                | Application EPG | common/privIP_TEST/privIP_TEST     | 
|         |                | Application EPG | hefernan_ni-demo/APP/EPG1          | 
|         |                | Application EPG | hefernan_ni-demo/APP/EPG2          | 
|         |                | Application EPG | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | 
|         |                | Application EPG | nidemo/streamz/appserver           | 
|         |                | Application EPG | nidemo/streamz/database            | 
|         |                | Application EPG | nidemo/streamz/frontend            | 
|         |                | Application EPG | nidemo/streamz/management          | 
|         |                | Application EPG | vEPC/vSFO_ANP/WWW                  | 
|         |                | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
|         |                | AAEP            | ESX-CDC-22_AAEP                    | 
+---------+----------------+-----------------+------------------------------------+
| 0 1 0 0 | EU-SPDC-POD2B  | Application EPG | k8s/k8s_ANP/MGMT                   | 
|         |                | Application EPG | k8s/k8s_ANP/backbone1              | 
|         |                | Application EPG | k8s/k8s_ANP/bmk8s_prov             | 
|         |                | Application EPG | k8s/k8s_ANP/csr1_lan               | 
|         |                | Application EPG | k8s/k8s_ANP/csr2_lan               | 
|         |                | Application EPG | k8s/k8s_ANP/csr_b2b                | 
|         |                | Application EPG | k8s/k8s_ANP/site1_lan              | 
|         |                | Application EPG | k8s/k8s_ANP/site1_pe               | 
|         |                | Application EPG | k8s/k8s_ANP/site2_lan              | 
|         |                | Application EPG | k8s/k8s_ANP/site2_pe               | 
|         |                | Application EPG | k8s/k8s_ANP/vk8s_1                 | 
|         |                | Application EPG | k8s/k8s_ANP/vk8s_2                 | 
|         |                | Application EPG | k8s/k8s_ANP/vk8s_3                 | 
|         |                | Application EPG | k8s/k8s_ANP/vk8s_4                 | 
|         |                | Application EPG | nidemo/streamz/management          | 
+---------+----------------+-----------------+------------------------------------+
| 0 4 0 0 | EU-SPDC-R7DC   | Application EPG | nidemo/streamz/management          | 
|         |                | Application EPG | vEPC/vSFO_ANP/WWW                  | 
|         |                | AAEP            | ESX-R7DC_AAEP                      | 
+---------+----------------+-----------------+------------------------------------+
| 0 5 0 0 | vEPC-Dataplane | Application EPG | vEPC_demo/vEPG_ANP/vEPG_ACC        | 
|         |                | Application EPG | vEPC_demo/vEPG_ANP/vEPG_CTRL       | 
|         |                | Application EPG | vEPC_demo/vEPG_ANP/vEPG_INT        | 
|         |                | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
|         |                | AAEP            | vEPC-ESX21-22_AAEP                 | 
+---------+----------------+-----------------+------------------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view reln

{
    "duration": 2137,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 1174,
        "total_time": 1618
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

True	444	-	connect apic21o.emea-sp.cisco.com:443
True	370	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	804	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
```

[[Back]](./DomainVmm.md)