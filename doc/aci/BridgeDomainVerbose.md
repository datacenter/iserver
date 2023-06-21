# Bridge Domain

## Verbose output

Get selected bridge domain details
- L2/L3 forwarding properties
- Multicast properties
- IGMP Snoop policy
- MLD Snoop policy
- VRF properties
- List of associated EPGs
- Endpoints with fabric and vmm information

```
# iserver get aci bd --apic apic21 --name vk8s_1* --view verbose

Apic: apic21 (mode:online, cache:off)

+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Class ID | VNID     | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_1_BD | 16399    | 15007706 | 10.58.24.174/28 | 2/14  | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+

Bridge Domain Properties
------------------------
- Name                  : vk8s_1_BD
- Tenant                : k8s
- Dn                    : uni/tn-k8s/BD-vk8s_1_BD
- Description           : Cloud_1_BD (Managed by Terraform)
- Health Score          : 100
- Type                  : regular
- Subnet Count          : 1
- VRF                   : common/Infra_VRF
- Associated L3 Outs    : 1
- Endpoints Count       : 8
- Endpoint Groups Count : 1


L2 Forwarding Properties
------------------------
- L2 Unknown Unicast         : flood
- Multi Destination Flooding : bd-flood
- Clear Remote MAC Entries   : no


Multicast Properties
--------------------
- IGMP Snooping Policy               : default
- MLD Snooping Policy                : default
- IPv4 Multicast                     : no
- IPv4 L3 Unknown Multicast Flooding : flood
- IPv6 Multicast                     : no
- IPv6 L3 Unknown Multicast          : flood


IGMP Snoop Policy
-----------------
- Name                       : default
- Tenant                     : common
- Admin state                : enabled
- Last Member Query Interval : 1
- Query Interval             : 125
- Query Response interval    : 10
- Start Query Count          : 2
- Start Query interval       : 31


MLD Snoop Policy
----------------
- Name                       : default
- Tenant                     : common
- Admin state                : disabled
- Version                    : v2
- Last Member Query Interval : 1
- Query Interval             : 125
- Query Response interval    : 10
- Start Query Count          : 2
- Start Query interval       : 31


L3 Forwarding Properties
------------------------
- Unicast Routing                           : yes
- BD MAC Address                            : 00:22:BD:C8:11:FF
- Virtual MAC Address                       : 
- IP Learning                               : yes
- Advertise Host Routes                     : no
- Limit Local IP Learning to BD/EPG Subnets : yes
- ARP Flooding                              : yes
- EP Move Detection Mode                    : 


+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| Network         | Gateway      | Preferred | Virtual | Scope  | IP Data Plane Learning | IP Usage | IP Available |
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| 10.58.24.160/28 | 10.58.24.174 | no        | no      | public | enabled                | 2/14     | 12           | 
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+

Endpoint Groups
---------------

+----+----------+--------+-------------+-----------+----------+
| Up | EPG Name | Tenant | App Profile | Endpoints | Contract |
+----+----------+--------+-------------+-----------+----------+
| V  | vk8s_1   | k8s    | k8s_ANP     |           |          | 
+----+----------+--------+-------------+-----------+----------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : no
- Class ID                              : 49153
- VNID                                  : 2818048

Bridge Domain Endpoints
-----------------------

+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| SF | MAC Address       | IP Address   | EPG                | Encap | BD            | VRF              |
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:11:50 | 10.58.24.161 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:3D:19 |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:67:1F |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:85:73 |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:9C:81 |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:9E:D0 |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| V  | 00:50:56:B4:D2:45 |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:EB:6A |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+

Bridge Domain Endpoints with VMM information
--------------------------------------------

+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| Apic | SF | MAC Address       | IP Address   | VMM           | Hypervisor              | VM Name                  | VM State   | vNIC Name         | vNIC State |
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:11:50 | 10.58.24.161 | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | ocp-devel-installer      | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:3D:19 |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-worker-ggl7q | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:67:1F |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-master-2     | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:85:73 |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-master-0     | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:9C:81 |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-worker-d6c8p | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:9E:D0 |              | EU-SPDC-POD2B | esx72.emea-sp.cisco.com | devel-5tt4q-worker-wfvql | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:D2:45 |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-rhcos        | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | LV | 00:50:56:B4:EB:6A |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-master-1     | poweredOn  | Network adapter 1 | up         | 
+------+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci bd --apic apic21 --name vk8s_1* --view verbose

{
    "duration": 11792,
    "apic": {
        "read": true,
        "success": 17,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 16,
        "connect_time": 380,
        "disconnect_time": 0,
        "mo_time": 9316,
        "total_time": 9696
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

True	380	-	connect apic21o.emea-sp.cisco.com:443
True	381	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	291	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	362	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	289	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	360	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	701	1016	apic21o.emea-sp.cisco.com:443 class compVm
True	783	2852	apic21o.emea-sp.cisco.com:443 class compVNic
True	323	104	apic21o.emea-sp.cisco.com:443 class compHv
True	404	710	apic21o.emea-sp.cisco.com:443 class fabricPathEp
True	2908	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	503	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx72_PolGrp query rsp-subtree-include=full-deployment&target-node=2207&target-path=AccBaseGrpToEthIf
True	492	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx72_PolGrp query rsp-subtree-include=full-deployment&target-node=2208&target-path=AccBaseGrpToEthIf
True	458	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2207&target-path=AccBaseGrpToEthIf
True	486	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2208&target-path=AccBaseGrpToEthIf
True	291	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/snPol-default
True	284	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/mldsnoopPol-default
```

[[Back]](./BridgeDomain.md)