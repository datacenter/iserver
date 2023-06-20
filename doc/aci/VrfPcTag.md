# Virtual Routing and Forwarding (VRF)

## Filter by pcTag

Supported pcTag filtering options by example:
- --pctag system
- --pctag global
- --pctag 32770
- --pctag lt100
- --pctag 32000-32100

```
# iserver get aci vrf --apic apic21 --pctag lt16390

Apic: apic21 (mode:online, cache:off)

+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| VRF                    | PCE Preference | PCE Direction | Class ID | VNID    | Associated EPG            | Associated BD        | BD Subnets       | Associated L3Out  |
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| common/default         | enforced       | ingress       | 16386    | 3014656 |                           |                      |                  | common/default    | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| Ericsson_PACO/RAN      | enforced       | ingress       | 16386    | 2293761 |                           |                      |                  | Ericsson_PACO/RAN | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| mgmt/EU-SPDC-MGMT-VRF1 | enforced       | ingress       | 16386    | 2916352 |                           | mgmt/EU-SPDC-BD1     |                  |                   | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| mgmt/inb               | enforced       | ingress       | 16386    | 3080192 |                           | mgmt/inb             | 10.58.50.190/27  | mgmt/INB_L3out    | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| nidemo/streamz-vrf     | enforced       | ingress       | 16386    | 2424834 | nidemo/streamz/appserver  | nidemo/appserver     | 10.0.2.1/24      |                   | 
|                        |                |               |          |         | nidemo/streamz/database   | nidemo/database      | 10.0.3.1/24      |                   | 
|                        |                |               |          |         | nidemo/streamz/frontend   | nidemo/frontend      | 10.0.1.1/24      |                   | 
|                        |                |               |          |         | nidemo/streamz/management | nidemo/management    | 10.0.4.1/24      |                   | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| SPN_IntraLab/SPN_VRF1  | enforced       | ingress       | 16386    | 3080193 |                           | SPN_IntraLab/SPN_BD1 | 192.168.1.254/24 |                   | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
| vEPC_demo/MGMT_VRF     | enforced       | ingress       | 16386    | 2588672 |                           |                      |                  |                   | 
+------------------------+----------------+---------------+----------+---------+---------------------------+----------------------+------------------+-------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --pctag lt16390

{
    "duration": 4387,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 2954,
        "total_time": 3384
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

True	430	-	connect apic21o.emea-sp.cisco.com:443
True	311	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	414	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	334	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	351	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	423	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	428	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	342	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	351	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)