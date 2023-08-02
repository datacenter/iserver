# Virtual Routing and Forwarding (VRF)

## Route output

Get selected vrf route table

```
# iserver get aci vrf --apic apic21 --name k8s_SRIoV_VRF --view route

Apic: apic21 (mode:online, cache:off)

VRF k8s/k8s_SRIoV_VRF - IPv4 Routes [#8]
----------------------------------------

+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| Pod   | Node      | Prefix          | Next Hop        | Next Hop VRF      | Type   | Details   | Preference | Source |
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2207 | 15.20.16.0/24   | 10.5.80.66/32   | overlay-1         | static | attached  | 1          | static | 
|       |           |                 |                 |                   |        | direct    |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
|       |           |                 |                 |                   |        | recursive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2208 | 15.20.16.0/24   | 10.5.80.66/32   | overlay-1         | static | attached  | 1          | static | 
|       |           |                 |                 |                   |        | direct    |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
|       |           |                 |                 |                   |        | recursive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2207 | 15.20.16.254/32 | 15.20.16.254/32 | k8s:k8s_SRIoV_VRF | local  | attached  | 0          | local  | 
|       |           |                 |                 |                   |        | local     |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2208 | 15.20.16.254/32 | 15.20.16.254/32 | k8s:k8s_SRIoV_VRF | local  | attached  | 0          | local  | 
|       |           |                 |                 |                   |        | local     |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2207 | 15.20.17.0/24   | 10.5.80.66/32   | overlay-1         | static | attached  | 1          | static | 
|       |           |                 |                 |                   |        | direct    |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
|       |           |                 |                 |                   |        | recursive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2208 | 15.20.17.0/24   | 10.5.80.66/32   | overlay-1         | static | attached  | 1          | static | 
|       |           |                 |                 |                   |        | direct    |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
|       |           |                 |                 |                   |        | recursive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2207 | 15.20.17.254/32 | 15.20.17.254/32 | k8s:k8s_SRIoV_VRF | local  | attached  | 0          | local  | 
|       |           |                 |                 |                   |        | local     |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
| pod-1 | node-2208 | 15.20.17.254/32 | 15.20.17.254/32 | k8s:k8s_SRIoV_VRF | local  | attached  | 0          | local  | 
|       |           |                 |                 |                   |        | local     |            |        | 
|       |           |                 |                 |                   |        | pervasive |            |        | 
+-------+-----------+-----------------+-----------------+-------------------+--------+-----------+------------+--------+
```

Developer

```
# iserver get aci vrf --apic apic21 --name k8s_SRIoV_VRF --view route

{
    "duration": 4578,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 471,
        "disconnect_time": 0,
        "mo_time": 3730,
        "total_time": 4201
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

True	471	-	connect apic21o.emea-sp.cisco.com:443
True	439	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	459	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	386	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	397	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	428	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	465	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	340	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	380	154	apic21o.emea-sp.cisco.com:443 class fvLocale
True	436	8	apic21o.emea-sp.cisco.com:443 class uribv4Nexthop query query-target-filter=wcard(uribv4Nexthop.dn,"sys/uribv4/dom-k8s:k8s_SRIoV_VRF/db-rt")
```

[[Back]](./Vrf.md)