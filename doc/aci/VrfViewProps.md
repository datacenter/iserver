# Virtual Routing and Forwarding (VRF)

## Get VRF properties

Use '--view props' to get properties of selected vrfs
- vrf name and tenant
- data plane learning
- policy control enforcement preference and direction
- multicast
- bridge domain enforcement

```
# iserver get aci vrf --apic apic21 --view prop

Apic: apic21 (mode:online, cache:off)

VRF - Properties [#23]
----------------------

+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| VRF                      | DP Learning | Mcast  | PCE Preference | PCE Direction | BD Enforced | Class ID | VNID     |
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/copy              | V           | permit | enforced       | ingress       | X           | 49153    | 2555904  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/default           | V           | permit | enforced       | ingress       | X           | 16386    | 3014656  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/Infra_privIP_VRF  | V           | permit | enforced       | ingress       | X           | 49153    | 2326529  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/Infra_VRF         | V           | permit | unenforced     | ingress       | X           | 49153    | 2818048  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/Test_VRF1         | V           | permit | enforced       | ingress       | X           | 32770    | 2490368  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| Ericsson_PACO/PDN        | V           | permit | enforced       | ingress       | X           | 49153    | 3112962  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| Ericsson_PACO/RAN        | V           | permit | enforced       | ingress       | X           | 16386    | 2293761  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| hefernan_ni-demo/ni-demo | V           | permit | enforced       | ingress       | X           | 32770    | 2916353  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| infra/ave-ctrl           | V           | permit | enforced       | ingress       | X           | 32770    | 2686976  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| infra/overlay-1          | V           | permit | enforced       | ingress       | X           | 32770    | 16777199 | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| k8s/k8s_SRIoV_VRF        | V           | permit | enforced       | ingress       | X           | 32770    | 2228224  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| k8s/k8s_VRF              | V           | permit | enforced       | ingress       | X           | 32770    | 2916354  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/EU-SPDC-ERSPAN-VRF  | V           | permit | enforced       | ingress       | X           | 32770    | 2883584  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/EU-SPDC-MGMT-VRF1   | V           | permit | enforced       | ingress       | X           | 16386    | 2916352  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/inb                 | V           | permit | enforced       | ingress       | X           | 16386    | 3080192  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/oob                 | V           | permit | enforced       | ingress       | X           | 49153    | 2195456  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| nidemo/streamz-vrf       | V           | permit | enforced       | ingress       | X           | 16386    | 2424834  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| SPN_IntraLab/SPN_VRF1    | V           | permit | enforced       | ingress       | X           | 16386    | 3080193  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC/Leaking_VRF         | V           | permit | enforced       | ingress       | X           | 32770    | 2457600  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC/VSFO                | V           | permit | enforced       | ingress       | X           | 49153    | 3112960  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC_demo/ACC_VRF        | V           | permit | unenforced     | ingress       | X           | 32770    | 2785280  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC_demo/INT_VRF        | V           | permit | enforced       | ingress       | X           | 49153    | 2424833  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC_demo/MGMT_VRF       | V           | permit | enforced       | ingress       | X           | 16386    | 2588672  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
```

Developer

```
# iserver get aci vrf --apic apic21 --view prop

{
    "duration": 4335,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 3253,
        "total_time": 3687
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

True	434	-	connect apic21o.emea-sp.cisco.com:443
True	464	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	463	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	372	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	364	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	442	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	457	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	349	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	342	154	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)