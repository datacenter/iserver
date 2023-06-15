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

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_1_BD | 10.58.24.174/28 | 1/14  | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+

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
| 10.58.24.160/28 | 10.58.24.174 | no        | no      | public | enabled                | 1/14     | 13           | 
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+

Endpoint Groups
---------------

+----+----------+--------+-------------+-----------+----------+
| Up | EPG Name | Tenant | App Profile | Endpoints | Contract |
+----+----------+--------+-------------+-----------+----------+
| V  | vk8s_1   | k8s    | k8s_ANP     | 8         |          | 
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

Bridge Domain Endpoints
-----------------------

+----+-------------------+--------+---------------+--------+---------+------------------+
| SF | MAC Address       | Tenant | BD            | EPG    | Ap      | VRF              |
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:11:50 | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:3D:19 | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:67:1F | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:85:73 | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:9C:81 | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:9E:D0 | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:D2:45 | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+
| V  | 00:50:56:B4:EB:6A | k8s    | k8s/vk8s_1_BD | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+---------------+--------+---------+------------------+

Bridge Domain Endpoints with VMM information
--------------------------------------------

+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| Apic | SF | MAC Address       | IP Address | VMM           | Hypervisor              | VM Name                  | VM State   | vNIC Name         | vNIC State |
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:11:50 |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | ocp-devel-installer      | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:3D:19 |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-worker-ggl7q | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:67:1F |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-master-2     | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:85:73 |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-master-0     | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:9C:81 |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-worker-d6c8p | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:9E:D0 |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-worker-wfvql | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:D2:45 |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-rhcos        | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
|      | V  | 00:50:56:B4:EB:6A |            | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-5tt4q-master-1     | poweredOff | Network adapter 1 | down       | 
+------+----+-------------------+------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci bd --apic apic21 --name vk8s_1* --view verbose

{
    "duration": 11196,
    "apic": {
        "read": true,
        "success": 15,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 14,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 9166,
        "total_time": 9593
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

True	427	-	connect apic21o.emea-sp.cisco.com
True	400	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	324	23	apic21o.emea-sp.cisco.com class fvCtx
True	353	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	425	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	1150	1019	apic21o.emea-sp.cisco.com class compVm
True	911	2855	apic21o.emea-sp.cisco.com class compVNic
True	821	104	apic21o.emea-sp.cisco.com class compHv
True	487	710	apic21o.emea-sp.cisco.com class fabricPathEp
True	2228	19	apic21o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	351	15	apic21o.emea-sp.cisco.com class fabricNode
True	470	1	apic21o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2207&target-path=AccBaseGrpToEthIf
True	550	1	apic21o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2208&target-path=AccBaseGrpToEthIf
True	366	1	apic21o.emea-sp.cisco.com mo uni/tn-common/snPol-default
True	330	1	apic21o.emea-sp.cisco.com mo uni/tn-common/mldsnoopPol-default
```

[[Back]](./BridgeDomain.md)