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

+--------------------------+-------------+--------+----------------+---------------+-------------+
| VRF                      | DP Learning | Mcast  | PCE Preference | PCE Direction | BD Enforced |
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/copy              | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/default           | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/Infra_privIP_VRF  | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/Infra_VRF         | enabled     | permit | unenforced     | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/Test_VRF1         | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| Ericsson_PACO/PDN        | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| Ericsson_PACO/RAN        | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| hefernan_ni-demo/ni-demo | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| infra/ave-ctrl           | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| infra/overlay-1          | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| k8s/k8s_SRIoV_VRF        | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| k8s/k8s_VRF              | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/EU-SPDC-ERSPAN-VRF  | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/EU-SPDC-MGMT-VRF1   | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/inb                 | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/oob                 | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| nidemo/streamz-vrf       | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| SPN_IntraLab/SPN_VRF1    | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC/Leaking_VRF         | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC/VSFO                | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC_demo/ACC_VRF        | enabled     | permit | unenforced     | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC_demo/INT_VRF        | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC_demo/MGMT_VRF       | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --view prop

{
    "duration": 3908,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 2995,
        "total_time": 3412
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

True	417	-	connect apic21o.emea-sp.cisco.com:443
True	338	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	420	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	431	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	377	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	367	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	330	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	397	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	335	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./Vrf.md)