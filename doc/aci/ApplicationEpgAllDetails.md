# Application Endpoint Group (EPG)

## Get all details of selected properties

```
# iserver get aci epg --apic apic21 --name sriov* --view all

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
| Up | EPG                 | BD             | BD Subnet       | Endpoint | Node | Domain           | Contract | StPort | StMember | DynMember |
+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_A | k8s/SRIoV_A_BD | 15.20.16.254/24 | 1        |      | k8s_esx_PhysDom  | 3        | 14     | 0        | 0         | 
|    |                     |                |                 |          |      | k8s_phys_PhysDom |          |        |          |           | 
+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/SRIoV_B | k8s/SRIoV_B_BD | 15.20.17.254/24 | 1        |      | k8s_esx_PhysDom  | 0        | 14     | 0        | 0         | 
|    |                     |                |                 |          |      | k8s_phys_PhysDom |          |        |          |           | 
+----+---------------------+----------------+-----------------+----------+------+------------------+----------+--------+----------+-----------+

EPG Policy Properties
---------------------

+----+---------------------+------------------+----------+----------+-------------+------------+-------------+
| Up | EPG                 | Preferred Member | Flood    | Class ID | QoS Class   | Isolation  | Label Match |
+----+---------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/SRIoV_A | exclude          | disabled | 32772    | unspecified | unenforced | AtleastOne  | 
+----+---------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | k8s/k8s_ANP/SRIoV_B | exclude          | disabled | 32771    | unspecified | unenforced | AtleastOne  | 
+----+---------------------+------------------+----------+----------+-------------+------------+-------------+

EPG BD Properties
-----------------

+----+---------------------+----------------+-----------------+-------+-------------------+-------+
| Up | EPG                 | Bridge Domain  | BD Subnets      | Usage | VRF               | L3Out |
+----+---------------------+----------------+-----------------+-------+-------------------+-------+
| V  | k8s/k8s_ANP/SRIoV_A | k8s/SRIoV_A_BD | 15.20.16.254/24 | 2/254 | k8s/k8s_SRIoV_VRF |       | 
+----+---------------------+----------------+-----------------+-------+-------------------+-------+
| V  | k8s/k8s_ANP/SRIoV_B | k8s/SRIoV_B_BD | 15.20.17.254/24 | 2/254 | k8s/k8s_SRIoV_VRF |       | 
+----+---------------------+----------------+-----------------+-------+-------------------+-------+

EPG Endpoints
-------------

+----+-------------------+-------------+---------------------+-------+----------------+-------------------+
| SF | MAC Address       | IP Address  | EPG                 | Encap | BD             | VRF               |
+----+-------------------+-------------+---------------------+-------+----------------+-------------------+
| L  | 02:CC:0F:00:00:5A | 15.20.16.15 | k8s/k8s_ANP/SRIoV_A | 808   | k8s/SRIoV_A_BD | k8s/k8s_SRIoV_VRF | 
+----+-------------------+-------------+---------------------+-------+----------------+-------------------+
| L  | 02:CC:0F:00:00:56 | 15.20.17.15 | k8s/k8s_ANP/SRIoV_B | 807   | k8s/SRIoV_B_BD | k8s/k8s_SRIoV_VRF | 
+----+-------------------+-------------+---------------------+-------+----------------+-------------------+

EPG Contracts
-------------

+----+---------------------+----------+-------------------+-------------------+---------------------+
| Up | EPG                 | Class ID | Contract Consumed | Contract Provided | Contract Taboo      |
+----+---------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/SRIoV_A | 32772    | k8s/BT-Demo       | k8s/BT-Demo       | k8s/MyTabooContract | 
+----+---------------------+----------+-------------------+-------------------+---------------------+
| V  | k8s/k8s_ANP/SRIoV_B | 32771    |                   |                   |                     | 
+----+---------------------+----------+-------------------+-------------------+---------------------+

EPG Domain
----------

+---------------------+------------------+-------------+------------+------------+----------------+------------+------+
| EPG                 | Domain Name      | Domain Type | Deployment | Resolution | Switching Mode | Encap Mode | CoS  |
+---------------------+------------------+-------------+------------+------------+----------------+------------+------+
| k8s/k8s_ANP/SRIoV_A | k8s_esx_PhysDom  | Physical    | lazy       | lazy       | native         | auto       | Cos0 | 
|                     | k8s_phys_PhysDom | Physical    | lazy       | lazy       | native         | auto       | Cos0 | 
+---------------------+------------------+-------------+------------+------------+----------------+------------+------+
| k8s/k8s_ANP/SRIoV_B | k8s_esx_PhysDom  | Physical    | lazy       | lazy       | native         | auto       | Cos0 | 
|                     | k8s_phys_PhysDom | Physical    | lazy       | lazy       | native         | auto       | Cos0 | 
+---------------------+------------------+-------------+------------+------------+----------------+------------+------+

EPG Deployed Nodes
------------------

+---------------------+-----------+------------+-------+--------+-------+--------+---------+
| EPG                 | Node Name | IP Address | Admin | Fabric | Model | Serial | Version |
+---------------------+-----------+------------+-------+--------+-------+--------+---------+
| k8s/k8s_ANP/SRIoV_A |           |            |       |        |       |        |         | 
+---------------------+-----------+------------+-------+--------+-------+--------+---------+
| k8s/k8s_ANP/SRIoV_B |           |            |       |        |       |        |         | 
+---------------------+-----------+------------+-------+--------+-------+--------+---------+

EPG Members
-----------

+---------------------+-------------+------+------+----+------+
| EPG                 | Member Type | Node | Type | ID | VLAN |
+---------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/SRIoV_A |             |      |      |    |      | 
+---------------------+-------------+------+------+----+------+
| k8s/k8s_ANP/SRIoV_B |             |      |      |    |      | 
+---------------------+-------------+------+------+----+------+

EPG Static Ports
----------------

+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
| EPG                 | Path      | Type | Ep       | Encapsulation | Mode  | Deployment Immediacy | State    |
+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
| k8s/k8s_ANP/SRIoV_A | node-2207 | Intf | eth1/3/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/3/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/3/3 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/3/4 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/4/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/4/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/4/3 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/3 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/4 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/4/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/4/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/4/3 | vlan-808      | Trunk | immediate            | unformed | 
+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
| k8s/k8s_ANP/SRIoV_B | node-2207 | Intf | eth1/5/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/5/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/5/3 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/5/4 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/6/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/6/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/6/3 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/3 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/4 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/6/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/6/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/6/3 | vlan-807      | Trunk | immediate            | unformed | 
+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
```

Developer

```
# iserver get aci epg --apic apic21 --name sriov* --view all

{
    "duration": 6471,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 4760,
        "total_time": 5187
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

True	427	-	connect apic21o.emea-sp.cisco.com:443
True	383	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	315	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	363	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	351	152	apic21o.emea-sp.cisco.com:443 class fvLocale
True	417	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	368	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	417	710	apic21o.emea-sp.cisco.com:443 class fabricPathEp
True	316	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	357	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	351	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	343	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	448	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	331	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./ApplicationEpg.md)