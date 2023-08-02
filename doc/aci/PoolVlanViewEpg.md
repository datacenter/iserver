# VLAN Pool

## Default output

```
# iserver get aci pool vlan --apic apic21 --view epg

Apic: apic21 (mode:online, cache:off)

Pool VLAN - Associated EPG [#32]
--------------------------------

+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| Pool Name              | EPG                                | VLAN Pool              | Alloc Mode | VLAN | Deployment | Resolution    | Switching |
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | SPN_IntraLab/SPN_Connect_ANP/TEST2 | ESX-CDC-22_VlanPool    | dynamic    | 2703 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | common/privIP_TEST/privIP_TEST     | ESX-CDC-22_VlanPool    | dynamic    | 2804 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | hefernan_ni-demo/APP/EPG1          | ESX-CDC-22_VlanPool    | dynamic    | 2701 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | hefernan_ni-demo/APP/EPG2          | ESX-CDC-22_VlanPool    | dynamic    | 2702 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | ESX-CDC-22_VlanPool    | dynamic    | 2704 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | nidemo/streamz/appserver           | ESX-CDC-22_VlanPool    | dynamic    | 2901 | lazy       | lazy          | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | nidemo/streamz/database            | ESX-CDC-22_VlanPool    | dynamic    | 2801 | lazy       | lazy          | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | nidemo/streamz/frontend            | ESX-CDC-22_VlanPool    | dynamic    | 2900 | lazy       | lazy          | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | nidemo/streamz/management          | ESX-CDC-22_VlanPool    | dynamic    | 2800 | lazy       | lazy          | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | vEPC/vSFO_ANP/WWW                  | ESX-CDC-22_VlanPool    | dynamic    | 2902 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-CDC-22_VlanPool    | vEPC_demo/vEPG_ANP/vEPG_MGMT       | ESX-CDC-22_VlanPool    | dynamic    | 2708 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-R7DC_VlanPool      | nidemo/streamz/management          | ESX-R7DC_VlanPool      | dynamic    | 3736 | lazy       | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| ESX-R7DC_VlanPool      | vEPC/vSFO_ANP/WWW                  | ESX-R7DC_VlanPool      | dynamic    | 3735 | lazy       | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/MGMT                   | k8s_esx_VlanPool       | dynamic    | 1370 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/backbone1              | k8s_esx_VlanPool       | dynamic    | 1301 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/bmk8s_prov             | k8s_esx_VlanPool       | dynamic    | 1434 | immediate  | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/csr1_lan               | k8s_esx_VlanPool       | dynamic    | 1303 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/csr2_lan               | k8s_esx_VlanPool       | dynamic    | 1435 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/csr_b2b                | k8s_esx_VlanPool       | dynamic    | 1305 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/site1_lan              | k8s_esx_VlanPool       | dynamic    | 1306 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/site1_pe               | k8s_esx_VlanPool       | dynamic    | 1304 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/site2_lan              | k8s_esx_VlanPool       | dynamic    | 1437 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/site2_pe               | k8s_esx_VlanPool       | dynamic    | 1302 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/vk8s_1                 | k8s_esx_VlanPool       | dynamic    | 1367 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/vk8s_2                 | k8s_esx_VlanPool       | dynamic    | 1300 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/vk8s_3                 | k8s_esx_VlanPool       | dynamic    | 1369 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | k8s/k8s_ANP/vk8s_4                 | k8s_esx_VlanPool       | dynamic    | 1368 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| k8s_esx_VlanPool       | nidemo/streamz/management          | k8s_esx_VlanPool       | dynamic    | 1372 | lazy       | pre-provision | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-ESX21-22_VlanPool | vEPC_demo/vEPG_ANP/vEPG_ACC        | vEPC-ESX21-22_VlanPool | dynamic    | 2700 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-ESX21-22_VlanPool | vEPC_demo/vEPG_ANP/vEPG_CTRL       | vEPC-ESX21-22_VlanPool | dynamic    | 2701 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-ESX21-22_VlanPool | vEPC_demo/vEPG_ANP/vEPG_INT        | vEPC-ESX21-22_VlanPool | dynamic    | 2800 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
| vEPC-ESX21-22_VlanPool | vEPC_demo/vEPG_ANP/vEPG_MGMT       | vEPC-ESX21-22_VlanPool | dynamic    | 2900 | immediate  | immediate     | native    | 
+------------------------+------------------------------------+------------------------+------------+------+------------+---------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --view epg

{
    "duration": 1140,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 365,
        "disconnect_time": 0,
        "mo_time": 617,
        "total_time": 982
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

True	365	-	connect apic21o.emea-sp.cisco.com:443
True	305	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	312	32	apic21o.emea-sp.cisco.com:443 class vmmEpPD
```

[[Back]](./PoolVlan.md)