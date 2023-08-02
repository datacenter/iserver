# VMM Domain

## Epg view

```
# iserver get aci domain vmm --apic apic21 --view epg

Apic: apic21 (mode:online, cache:off)

VMM Domain - Associated EPG [#32]
---------------------------------

+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| Domain Name    | EPG                                | VLAN Pool              | Alloc Mode | VLAN | Deployment | Resolution    | Switching |
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | SPN_IntraLab/SPN_Connect_ANP/TEST2 | ESX-CDC-22_VlanPool    | dynamic    | 2703 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | common/privIP_TEST/privIP_TEST     | ESX-CDC-22_VlanPool    | dynamic    | 2804 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | hefernan_ni-demo/APP/EPG1          | ESX-CDC-22_VlanPool    | dynamic    | 2701 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | hefernan_ni-demo/APP/EPG2          | ESX-CDC-22_VlanPool    | dynamic    | 2702 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | ESX-CDC-22_VlanPool    | dynamic    | 2704 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/appserver           | ESX-CDC-22_VlanPool    | dynamic    | 2901 | lazy       | lazy          | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/database            | ESX-CDC-22_VlanPool    | dynamic    | 2801 | lazy       | lazy          | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/frontend            | ESX-CDC-22_VlanPool    | dynamic    | 2900 | lazy       | lazy          | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/management          | ESX-CDC-22_VlanPool    | dynamic    | 2800 | lazy       | lazy          | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | vEPC/vSFO_ANP/WWW                  | ESX-CDC-22_VlanPool    | dynamic    | 2902 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | vEPC_demo/vEPG_ANP/vEPG_MGMT       | ESX-CDC-22_VlanPool    | dynamic    | 2708 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/MGMT                   | k8s_esx_VlanPool       | dynamic    | 1370 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/backbone1              | k8s_esx_VlanPool       | dynamic    | 1301 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/bmk8s_prov             | k8s_esx_VlanPool       | dynamic    | 1434 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/csr1_lan               | k8s_esx_VlanPool       | dynamic    | 1303 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/csr2_lan               | k8s_esx_VlanPool       | dynamic    | 1435 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/csr_b2b                | k8s_esx_VlanPool       | dynamic    | 1305 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/site1_lan              | k8s_esx_VlanPool       | dynamic    | 1306 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/site1_pe               | k8s_esx_VlanPool       | dynamic    | 1304 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/site2_lan              | k8s_esx_VlanPool       | dynamic    | 1437 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/site2_pe               | k8s_esx_VlanPool       | dynamic    | 1302 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/vk8s_1                 | k8s_esx_VlanPool       | dynamic    | 1367 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/vk8s_2                 | k8s_esx_VlanPool       | dynamic    | 1300 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/vk8s_3                 | k8s_esx_VlanPool       | dynamic    | 1369 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | k8s/k8s_ANP/vk8s_4                 | k8s_esx_VlanPool       | dynamic    | 1368 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-POD2B  | nidemo/streamz/management          | k8s_esx_VlanPool       | dynamic    | 1372 | lazy       | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-R7DC   | nidemo/streamz/management          | ESX-R7DC_VlanPool      | dynamic    | 3736 | lazy       | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-R7DC   | vEPC/vSFO_ANP/WWW                  | ESX-R7DC_VlanPool      | dynamic    | 3735 | lazy       | pre-provision | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-Dataplane | vEPC_demo/vEPG_ANP/vEPG_ACC        | vEPC-ESX21-22_VlanPool | dynamic    | 2700 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-Dataplane | vEPC_demo/vEPG_ANP/vEPG_CTRL       | vEPC-ESX21-22_VlanPool | dynamic    | 2701 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-Dataplane | vEPC_demo/vEPG_ANP/vEPG_INT        | vEPC-ESX21-22_VlanPool | dynamic    | 2800 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-Dataplane | vEPC_demo/vEPG_ANP/vEPG_MGMT       | vEPC-ESX21-22_VlanPool | dynamic    | 2900 | immediate  | immediate     | native    | 
+----------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view epg

{
    "duration": 3005,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 520,
        "disconnect_time": 0,
        "mo_time": 1650,
        "total_time": 2170
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

True	520	-	connect apic21o.emea-sp.cisco.com:443
True	419	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	830	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	401	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainVmm.md)