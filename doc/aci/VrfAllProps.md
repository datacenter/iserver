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

+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| VRF                      | DP Learning | Mcast  | PCE Preference | PCE Direction | BD Enforced | Class ID | VNID     |
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/copy              | enabled     | permit | enforced       | ingress       | no          | 49153    | 2555904  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/default           | enabled     | permit | enforced       | ingress       | no          | 16386    | 3014656  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/Infra_privIP_VRF  | enabled     | permit | enforced       | ingress       | no          | 49153    | 2326529  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/Infra_VRF         | enabled     | permit | unenforced     | ingress       | no          | 49153    | 2818048  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| common/Test_VRF1         | enabled     | permit | enforced       | ingress       | no          | 32770    | 2490368  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| Ericsson_PACO/PDN        | enabled     | permit | enforced       | ingress       | no          | 49153    | 3112962  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| Ericsson_PACO/RAN        | enabled     | permit | enforced       | ingress       | no          | 16386    | 2293761  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| hefernan_ni-demo/ni-demo | enabled     | permit | enforced       | ingress       | no          | 32770    | 2916353  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| infra/ave-ctrl           | enabled     | permit | enforced       | ingress       | no          | 32770    | 2686976  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| infra/overlay-1          | enabled     | permit | enforced       | ingress       | no          | 32770    | 16777199 | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| k8s/k8s_SRIoV_VRF        | enabled     | permit | enforced       | ingress       | no          | 32770    | 2228224  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| k8s/k8s_VRF              | enabled     | permit | enforced       | ingress       | no          | 32770    | 2916354  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/EU-SPDC-ERSPAN-VRF  | enabled     | permit | enforced       | ingress       | no          | 32770    | 2883584  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/EU-SPDC-MGMT-VRF1   | enabled     | permit | enforced       | ingress       | no          | 16386    | 2916352  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/inb                 | enabled     | permit | enforced       | ingress       | no          | 16386    | 3080192  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| mgmt/oob                 | enabled     | permit | enforced       | ingress       | no          | 49153    | 2195456  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| nidemo/streamz-vrf       | enabled     | permit | enforced       | ingress       | no          | 16386    | 2424834  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| SPN_IntraLab/SPN_VRF1    | enabled     | permit | enforced       | ingress       | no          | 16386    | 3080193  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC/Leaking_VRF         | enabled     | permit | enforced       | ingress       | no          | 32770    | 2457600  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC/VSFO                | enabled     | permit | enforced       | ingress       | no          | 49153    | 3112960  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC_demo/ACC_VRF        | enabled     | permit | unenforced     | ingress       | no          | 32770    | 2785280  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC_demo/INT_VRF        | enabled     | permit | enforced       | ingress       | no          | 49153    | 2424833  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
| vEPC_demo/MGMT_VRF       | enabled     | permit | enforced       | ingress       | no          | 16386    | 2588672  | 
+--------------------------+-------------+--------+----------------+---------------+-------------+----------+----------+
```

Developer

```
# iserver get aci vrf --apic apic21 --view prop

{
    "duration": 4396,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 3012,
        "total_time": 3420
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

True	408	-	connect apic21o.emea-sp.cisco.com:443
True	302	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	435	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	362	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	355	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	386	92	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	511	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	316	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	345	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)