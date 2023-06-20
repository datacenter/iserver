# Application Endpoint Group (EPG)

## Verbose output

Get selected EPG details
- EPG properties
- Consumed and provided contracts with filters
- Bridge Domain properties and subnets
- VRF properties
- Associated L3 Outs properties
- Deployed nodes
- Endpoints

Note: All selected EPGs will be shown in verbose mode

```
# iserver get aci epg --apic apic21 --name sriov_a* --view verbose

Apic: apic21 (mode:online, cache:off)

+----+---------------------+----------------+-----------------+-----------+-----------+
| Up | EPG                 | Bridge Domain  | BD Subnets      | Endpoints | Contracts |
+----+---------------------+----------------+-----------------+-----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_A | k8s/SRIoV_A_BD | 15.20.16.254/24 | 1         | 3         | 
+----+---------------------+----------------+-----------------+-----------+-----------+

Application EPG Properties
--------------------------
- Up                     : V
- Configuration State    : applied
- EPG Name               : SRIoV_A
- Application Profile    : k8s_ANP
- Tenant                 : k8s
- Bridge Domain          : k8s/SRIoV_A_BD
- Alias                  : 
- Description            : 
- Annotations            : orchestrator:terraform
- Class ID               : 32772
- Contract Exception Tag : 
- QoS Class              : unspecified
- Intra EPG Isolation    : unenforced
- Preferred Group Member : exclude
- Flood in Encapsulation : disabled
- ESG Matched            : 

Contract Consumed
-----------------
- k8s/BT-Demo

Standard Contracts
------------------

+-------------+---------+---------+-------------+---------+----------------+
| Contract    | Scope   | Intent  | Target DSCP | Subject | Filter         |
+-------------+---------+---------+-------------+---------+----------------+
| k8s/BT-Demo | context | install | unspecified | k8s/Any | k8s/alltraffic | 
+-------------+---------+---------+-------------+---------+----------------+

Contract Filters
----------------

+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Contract Provided
-----------------
- k8s/BT-Demo

Standard Contracts
------------------

+-------------+---------+---------+-------------+---------+----------------+
| Contract    | Scope   | Intent  | Target DSCP | Subject | Filter         |
+-------------+---------+---------+-------------+---------+----------------+
| k8s/BT-Demo | context | install | unspecified | k8s/Any | k8s/alltraffic | 
+-------------+---------+---------+-------------+---------+----------------+

Contract Filters
----------------

+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Contract Taboo
--------------
- k8s/MyTabooContract

Taboo Contracts
---------------

+---------------------+--------------------+----------+
| Taboo               | Subject            | Filter   |
+---------------------+--------------------+----------+
| k8s/MyTabooContract | k8s/MyTabooSubject | k8s/icmp | 
+---------------------+--------------------+----------+

Contract Filters
----------------

+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter   | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/icmp | icmp  | ipv4  |          | icmp  | no        | no       |        |             |       | 
+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Bridge Domain Properties
------------------------
- Name                  : SRIoV_A_BD
- Tenant                : k8s
- Dn                    : uni/tn-k8s/BD-SRIoV_A_BD
- Description           : SRIoV_A_BD (Managed by Terraform)
- Health Score          : 100
- Type                  : regular
- Subnet Count          : 1
- VRF                   : k8s/k8s_SRIoV_VRF
- Associated L3 Outs    : 0
- Endpoints Count       : 
- Endpoint Groups Count : 


+---------------+--------------+-----------+---------+---------+------------------------+----------+--------------+
| Network       | Gateway      | Preferred | Virtual | Scope   | IP Data Plane Learning | IP Usage | IP Available |
+---------------+--------------+-----------+---------+---------+------------------------+----------+--------------+
| 15.20.16.0/24 | 15.20.16.254 | no        | no      | private | enabled                | 2/254    | 252          | 
+---------------+--------------+-----------+---------+---------+------------------------+----------+--------------+

VRF Properties
--------------
- Name                                  : k8s_SRIoV_VRF
- Tenant                                : k8s
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : enforced
- Bridge Domain Enforcement Status      : no


Deployed Nodes
--------------

+--------+----------------------+---------+--------+-------------+-------------+--------------+------+----------------+-------------+----------------+
| Apic   | Node Name            | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role | Model          | Serial      | Version        |
+--------+----------------------+---------+--------+-------------+-------------+--------------+------+----------------+-------------+----------------+
| apic21 | pod-1/cl2207-eu-spdc | 2207    | 1      | 10.5.240.34 | on          | active       | leaf | N9K-C9336C-FX2 | FDO23490E4G | n9000-15.2(7g) | 
| apic21 | pod-1/cl2208-eu-spdc | 2208    | 1      | 10.5.240.35 | on          | active       | leaf | N9K-C9336C-FX2 | FDO234807ED | n9000-15.2(7g) | 
+--------+----------------------+---------+--------+-------------+-------------+--------------+------+----------------+-------------+----------------+

EPG Endpoints
-------------

+----+-------------------+-------------+--------+---------+---------+-------+-------------------+
| SF | MAC Address       | IP Address  | Tenant | AP      | EPG     | Encap | VRF               |
+----+-------------------+-------------+--------+---------+---------+-------+-------------------+
| L  | 02:CC:0F:00:00:5A | 15.20.16.15 | k8s    | k8s_ANP | SRIoV_A | 808   | k8s/k8s_SRIoV_VRF | 
+----+-------------------+-------------+--------+---------+---------+-------+-------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --name sriov_a* --view verbose

{
    "duration": 5095,
    "apic": {
        "read": true,
        "success": 13,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 12,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 4354,
        "total_time": 4760
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

True	406	-	connect apic21o.emea-sp.cisco.com:443
True	368	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg
True	360	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	331	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	410	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	412	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	422	710	apic21o.emea-sp.cisco.com:443 class fabricPathEp
True	348	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	350	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	364	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	339	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	313	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	337	23	apic21o.emea-sp.cisco.com:443 class fvCtx
```

[[Back]](./ApplicationEpg.md)