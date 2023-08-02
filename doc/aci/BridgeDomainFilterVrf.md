# Bridge Domain

## Filter by bridge domain's vrf name

```
# iserver get aci bd --apic apic21 --vrf vEPC_demo/*

Apic: apic21 (mode:online, cache:off)

Bridge Domain [#3]
------------------

+--------+---------+---------------------------+----------+----------+----------------+-------+---------------------+-------------------+---------------------+
| Health | Faults  | Bridge Domain             | Class ID | VNID     | Subnet         | Usage | EPG                 | VRF               | L3Out               |
+--------+---------+---------------------------+----------+----------+----------------+-------+---------------------+-------------------+---------------------+
| 100    | 0 0 0 0 | vEPC_demo/ACC_BD          | 49153    | 15794150 | 15.20.0.254/24 | 1/254 | vEPC_demo/vEPG_ACC  | vEPC_demo/ACC_VRF | vEPC_demo/ACC_L3out | 
|        |         |                           |          |          |                |       |                     |                   | vEPC_demo/SX_L3out  | 
+--------+---------+---------------------------+----------+----------+----------------+-------+---------------------+-------------------+---------------------+
| 100    | 0 0 0 0 | vEPC_demo/INT_BD          | 32770    | 15892442 | 15.20.3.254/24 | 1/254 | vEPC_demo/vEPG_INT  | vEPC_demo/INT_VRF | vEPC_demo/INT_L3out | 
+--------+---------+---------------------------+----------+----------+----------------+-------+---------------------+-------------------+---------------------+
| 100    | 0 0 0 0 | vEPC_demo/vEPC-CTRL-SX_BD | 16387    | 15728623 |                |       | vEPC_demo/vEPG_CTRL | vEPC_demo/ACC_VRF | vEPC_demo/SX_L3out  | 
+--------+---------+---------------------------+----------+----------+----------------+-------+---------------------+-------------------+---------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --vrf vEPC_demo/*

{
    "duration": 2995,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 483,
        "disconnect_time": 0,
        "mo_time": 1882,
        "total_time": 2365
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

True	483	-	connect apic21o.emea-sp.cisco.com:443
True	476	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	522	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	386	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	498	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)