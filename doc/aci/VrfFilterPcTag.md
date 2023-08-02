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

VRF [#7]
--------

+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| Health | Faults  | VRF                    | Class ID | VNID    | PCE Preference | PCE Direction | Associated EPG                     | Associated BD        | BD Subnets       | Associated L3Out  |
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | common/default         | 16386    | 3014656 | enforced       | ingress       |                                    |                      |                  | common/default    | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | Ericsson_PACO/RAN      | 16386    | 2293761 | enforced       | ingress       |                                    |                      |                  | Ericsson_PACO/RAN | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | mgmt/EU-SPDC-MGMT-VRF1 | 16386    | 2916352 | enforced       | ingress       |                                    |                      |                  |                   | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | mgmt/inb               | 16386    | 3080192 | enforced       | ingress       |                                    | mgmt/inb             | 10.58.50.190/27  | mgmt/INB_L3out    | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | nidemo/streamz-vrf     | 16386    | 2424834 | enforced       | ingress       | nidemo/streamz/appserver           | nidemo/appserver     | 10.0.2.1/24      |                   | 
|        |         |                        |          |         |                |               | nidemo/streamz/database            | nidemo/database      | 10.0.3.1/24      |                   | 
|        |         |                        |          |         |                |               | nidemo/streamz/frontend            | nidemo/frontend      | 10.0.1.1/24      |                   | 
|        |         |                        |          |         |                |               | nidemo/streamz/management          | nidemo/management    | 10.0.4.1/24      |                   | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | SPN_IntraLab/SPN_VRF1  | 16386    | 3080193 | enforced       | ingress       | SPN_IntraLab/SPN_Connect_ANP/TEST2 | SPN_IntraLab/SPN_BD1 | 192.168.1.254/24 |                   | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
| 100    | 0 0 0 0 | vEPC_demo/MGMT_VRF     | 16386    | 2588672 | enforced       | ingress       |                                    |                      |                  |                   | 
+--------+---------+------------------------+----------+---------+----------------+---------------+------------------------------------+----------------------+------------------+-------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --pctag lt16390

{
    "duration": 4113,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 423,
        "disconnect_time": 0,
        "mo_time": 3176,
        "total_time": 3599
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

True	423	-	connect apic21o.emea-sp.cisco.com:443
True	436	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	467	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	354	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	336	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	443	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	454	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	320	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	366	154	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)