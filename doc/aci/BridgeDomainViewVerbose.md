# Bridge Domain

## Verbose view

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

Bridge Domain [#1]
------------------

+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| Health | Faults  | Bridge Domain | Class ID | VNID     | Subnet          | Usage | EPG        | VRF              | L3Out              |
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+
| 100    | 0 0 0 0 | k8s/vk8s_1_BD | 16399    | 15007706 | 10.58.24.174/28 | 10/14 | k8s/vk8s_1 | common/Infra_VRF | common/Infra_L3out | 
+--------+---------+---------------+----------+----------+-----------------+-------+------------+------------------+--------------------+

Bridge Domain Properties
------------------------
- Health       : 100
- Faults       : 0 0 0 0
- Tenant       : k8s
- Name         : vk8s_1_BD
- Dn           : uni/tn-k8s/BD-vk8s_1_BD
- Description  : Cloud_1_BD (Managed by Terraform)
- Type         : regular
- Subnet Count : 1
- VRF          : common/Infra_VRF
- L3Out        : 1
- Endpoint     : 8
- EPG          : 1


L2 Forwarding Properties
------------------------
- L2 Unknown Unicast         : Flood
- Multicast Address (GIPo)   : 225.1.58.128
- Multi Destination Flooding : Flood in BD
- Clear Remote MAC Entries   : X
- Scaled L2 Only Mode        : X


Multicast Properties
--------------------
- IGMP Snooping Policy               : common/default
- MLD Snooping Policy                : common/default
- IPv4 Multicast                     : X
- IPv4 L3 Unknown Multicast Flooding : Flood
- IPv6 Multicast                     : X
- IPv6 L3 Unknown Multicast          : Flood


IGMP Snoop Policy
-----------------
- Tenant                     : common
- Name                       : default
- Admin state                : enabled
- Last Member Query Interval : 1
- Query Interval             : 125
- Query Response interval    : 10
- Start Query Count          : 2
- Start Query interval       : 31


MLD Snoop Policy
----------------
- Tenant                     : common
- Name                       : default
- Admin state                : disabled
- Version                    : v2
- Last Member Query Interval : 1
- Query Interval             : 125
- Query Response interval    : 10
- Start Query Count          : 2
- Start Query interval       : 31


L3 Forwarding Properties
------------------------
- Unicast Routing                           : V
- BD MAC Address                            : 00:22:BD:C8:11:FF
- Virtual MAC Address                       : --
- IP Learning                               : V
- Advertise Host Routes                     : X
- Limit Local IP Learning to BD/EPG Subnets : V
- ARP Flooding                              : V
- EP Move Detection Mode                    : --


+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| Network         | Gateway      | Preferred | Virtual | Scope  | IP Data Plane Learning | IP Usage | IP Available |
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| 10.58.24.160/28 | 10.58.24.174 | X         | X       | public | V                      | 10/14    | 4            | 
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+

Endpoint Groups
---------------

+----+--------------------+-----------+----------+
| Up | EPG                | Endpoints | Contract |
+----+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1 | 8         | 1        | 
+----+--------------------+-----------+----------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : V
- Multicast                             : V
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : X
- Class ID                              : 49153
- VNID                                  : 2818048

Bridge Domain Endpoints
-----------------------

+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| SF | MAC Address       | IP Address   | EPG                | Encap | BD            | VRF              |
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:04:A1 | 10.58.24.163 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
|    |                   | 10.58.24.170 |                    |       |               |                  | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:1F:B2 | 10.58.24.168 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:2B:BE | 10.58.24.169 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| V  | 00:50:56:B4:70:AD |              | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:CE:19 | 10.58.24.161 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:D3:91 | 10.58.24.165 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:DE:16 | 10.58.24.166 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+
| LV | 00:50:56:B4:E7:C4 | 10.58.24.162 | k8s/k8s_ANP/vk8s_1 | 1367  | k8s/vk8s_1_BD | common/Infra_VRF | 
|    |                   | 10.58.24.167 |                    |       |               |                  | 
+----+-------------------+--------------+--------------------+-------+---------------+------------------+

Bridge Domain Endpoints with VMM information
--------------------------------------------

+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| SF | MAC Address       | IP Address   | VMM           | Hypervisor              | VM Name                  | VM State   | vNIC Name         | vNIC State |
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:04:A1 | 10.58.24.163 | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-fnrrp-worker-fvwck | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.24.170 |               |                         |                          |            |                   |            | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:1F:B2 | 10.58.24.168 | EU-SPDC-POD2B | esx72.emea-sp.cisco.com | devel-fnrrp-worker-db2jd | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:2B:BE | 10.58.24.169 | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-fnrrp-worker-tprng | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| V  | 00:50:56:B4:70:AD |              | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-fnrrp-rhcos        | poweredOff | Network adapter 1 | down       | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:CE:19 | 10.58.24.161 | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | ocp-devel-installer      | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:D3:91 | 10.58.24.165 | EU-SPDC-POD2B | esx72.emea-sp.cisco.com | devel-fnrrp-master-0     | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:DE:16 | 10.58.24.166 | EU-SPDC-POD2B | esx71.emea-sp.cisco.com | devel-fnrrp-master-1     | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
| LV | 00:50:56:B4:E7:C4 | 10.58.24.162 | EU-SPDC-POD2B | esx72.emea-sp.cisco.com | devel-fnrrp-master-2     | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.24.167 |               |                         |                          |            |                   |            | 
+----+-------------------+--------------+---------------+-------------------------+--------------------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci bd --apic apic21 --name vk8s_1* --view verbose

{
    "duration": 13427,
    "apic": {
        "read": true,
        "success": 17,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 16,
        "connect_time": 465,
        "disconnect_time": 0,
        "mo_time": 10752,
        "total_time": 11217
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

True	465	-	connect apic21o.emea-sp.cisco.com:443
True	498	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	491	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	491	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	341	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	476	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	624	1028	apic21o.emea-sp.cisco.com:443 class compVm
True	823	2873	apic21o.emea-sp.cisco.com:443 class compVNic
True	416	104	apic21o.emea-sp.cisco.com:443 class compHv
True	381	710	apic21o.emea-sp.cisco.com:443 class fabricPathEp
True	3021	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	538	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2207&target-path=AccBaseGrpToEthIf
True	590	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2208&target-path=AccBaseGrpToEthIf
True	536	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx72_PolGrp query rsp-subtree-include=full-deployment&target-node=2207&target-path=AccBaseGrpToEthIf
True	545	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx72_PolGrp query rsp-subtree-include=full-deployment&target-node=2208&target-path=AccBaseGrpToEthIf
True	482	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/snPol-default
True	499	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/mldsnoopPol-default
```

[[Back]](./BridgeDomain.md)