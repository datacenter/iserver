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

VRF Summary
-----------

+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| VRF                    | Class ID | VNID    | PCE Preference | PCE Direction | Associated EPG                     | Associated BD        | BD Subnets       | Associated L3Out  |
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| common/default         | 16386    | 3014656 | enforced       | ingress       |                                    |                      |                  | common/default    | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| Ericsson_PACO/RAN      | 16386    | 2293761 | enforced       | ingress       |                                    |                      |                  | Ericsson_PACO/RAN | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| mgmt/EU-SPDC-MGMT-VRF1 | 16386    | 2916352 | enforced       | ingress       | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      | mgmt/EU-SPDC-BD1     |                  |                   | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| mgmt/inb               | 16386    | 3080192 | enforced       | ingress       |                                    | mgmt/inb             | 10.58.50.190/27  | mgmt/INB_L3out    | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| nidemo/streamz-vrf     | 16386    | 2424834 | enforced       | ingress       | nidemo/streamz/appserver           | nidemo/appserver     | 10.0.2.1/24      |                   | 
|                        |          |         |                |               | nidemo/streamz/database            | nidemo/database      | 10.0.3.1/24      |                   | 
|                        |          |         |                |               | nidemo/streamz/frontend            | nidemo/frontend      | 10.0.1.1/24      |                   | 
|                        |          |         |                |               | nidemo/streamz/management          | nidemo/management    | 10.0.4.1/24      |                   | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| SPN_IntraLab/SPN_VRF1  | 16386    | 3080193 | enforced       | ingress       | SPN_IntraLab/SPN_Connect_ANP/TEST2 | SPN_IntraLab/SPN_BD1 | 192.168.1.254/24 |                   | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| vEPC_demo/MGMT_VRF     | 16386    | 2588672 | enforced       | ingress       |                                    |                      |                  |                   | 
+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --pctag lt16390

{
    "duration": 4681,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 3075,
        "total_time": 3481
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
True	291	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	407	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	438	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	459	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	381	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	383	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	307	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	409	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)