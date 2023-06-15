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
# iserver get aci epg --apic apic21 --name vk8s_1 --view verbose

Apic: apic21 (mode:online, cache:off)

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | BD Subnets      | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+

Application EPG Properties
--------------------------
- Up                     : V
- Configuration State    : applied
- EPG Name               : vk8s_1
- Application Profile    : k8s_ANP
- Tenant                 : k8s
- Bridge Domain          : k8s/vk8s_1_BD
- Alias                  : 
- Description            : 
- Annotations            : orchestrator:terraform
- Class ID               : 49162
- Contract Exception Tag : 
- QoS Class              : unspecified
- Intra EPG Isolation    : unenforced
- Preferred Group Member : exclude
- Flood in Encapsulation : disabled
- ESG Matched            : 

Contract Consumed
-----------------
- common/k8s_vm

Standard Contracts
------------------

+---------------+--------+---------+-------------+-----------------+------------+
| Contract      | Scope  | Intent  | Target DSCP | Subject         | Filter     |
+---------------+--------+---------+-------------+-----------------+------------+
| common/k8s_vm | global | install | unspecified | common/k8s_prov | common/any | 
+---------------+--------+---------+-------------+-----------------+------------+

Contract Filters
----------------

+------------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter     | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+------------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/any | any   | ipv4  |          |       | no        | no       |        |             |       | 
+------------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

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
- Endpoints Count       : 
- Endpoint Groups Count : 


+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| Network         | Gateway      | Preferred | Virtual | Scope  | IP Data Plane Learning | IP Usage | IP Available |
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| 10.58.24.160/28 | 10.58.24.174 | no        | no      | public | enabled                | 1/14     | 13           | 
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : no


Associated L3 Out
-----------------

+--------------------+------+-----+-----+------+-------+------------------+-------------+
| L3Out              | MPLS | PIM | BGP | OSPF | EIGRP | VRF              | L3 Domain   |
+--------------------+------+-----+-----+------+-------+------------------+-------------+
| common/Infra_L3out | X    | X   | V   | X    | X     | common/Infra_VRF | Infra_L3Dom | 
|                    |      |     |     |      |       |                  |             | 
+--------------------+------+-----+-----+------+-------+------------------+-------------+

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

+----+-------------------+--------+--------+---------+------------------+
| SF | MAC Address       | Tenant | EPG    | Ap      | VRF              |
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:11:50 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:3D:19 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:67:1F | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:85:73 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:9C:81 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:9E:D0 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:D2:45 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:EB:6A | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------+--------+---------+------------------+
```

Developer

```
# iserver get aci epg --apic apic21 --name vk8s_1 --view verbose

{
    "duration": 8736,
    "apic": {
        "read": true,
        "success": 16,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 15,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 7825,
        "total_time": 8237
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

True	412	-	connect apic21o.emea-sp.cisco.com:443
True	388	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	341	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	345	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	384	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	471	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	440	710	apic21o.emea-sp.cisco.com:443 class fabricPathEp
True	2073	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	530	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2207&target-path=AccBaseGrpToEthIf
True	445	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=2208&target-path=AccBaseGrpToEthIf
True	700	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	356	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	353	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	306	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	348	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	345	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./ApplicationEpg.md)