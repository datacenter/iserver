# Tenant

Get the list of tenants with related policies count.

Use specific policy commands with '--tenant' filtering rule to get the per-tenant policy details.

## Default output

```
# iserver get aci tenant --apic apic21

Apic: apic21 (mode:online, cache:off)

+------------------+-------------+-----+---------------+-----+-------+-------+---------------+----------+----------+
| Name             | App Profile | EPG | Bridge Domain | VRF | L2Out | L3Out | MPLS-SR L3Out | Contract | Endpoint |
+------------------+-------------+-----+---------------+-----+-------+-------+---------------+----------+----------+
| common           | 3           | 2   | 4             | 5   | 1     | 0     | 0             | 7        | 2        | 
| Ericsson_PACO    | 0           | 0   | 0             | 2   | 0     | 0     | 0             | 1        | 24       | 
| hefernan_ni-demo | 1           | 2   | 2             | 1   | 0     | 0     | 0             | 2        | 0        | 
| infra            | 2           | 2   | 2             | 2   | 0     | 0     | 0             | 0        | 0        | 
| k8s              | 1           | 19  | 14            | 2   | 1     | 0     | 0             | 3        | 48       | 
| mgmt             | 1           | 2   | 3             | 4   | 0     | 0     | 0             | 1        | 1        | 
| nidemo           | 1           | 4   | 4             | 1   | 0     | 0     | 0             | 4        | 7        | 
| SPN_IntraLab     | 1           | 1   | 1             | 1   | 0     | 0     | 0             | 0        | 0        | 
| Testing_MSO      | 0           | 0   | 0             | 0   | 0     | 0     | 0             | 0        | 0        | 
| ttrabatt-test    | 0           | 0   | 0             | 0   | 0     | 0     | 0             | 0        | 0        | 
| vEPC             | 1           | 1   | 2             | 2   | 0     | 0     | 0             | 1        | 2        | 
| vEPC_demo        | 1           | 4   | 4             | 3   | 0     | 0     | 0             | 3        | 9        | 
+------------------+-------------+-----+---------------+-----+-------+-------+---------------+----------+----------+
```

## JSON output

```
# iserver get aci tenant --apic apic21 --name k8s -o json

[
    {
        "descr": "Kubernetes Environment - Modified with Terraform (ttrabatt)",
        "dn": "uni/tn-k8s",
        "lcOwn": "local",
        "name": "k8s",
        "userdom": ":all:common:",
        "bdCount": 14,
        "vrfCount": 2,
        "apCount": 1,
        "aEpgCount": 19,
        "l2OutCount": 1,
        "l3OutCount": 0,
        "mplsL3OutCount": 0,
        "contractCount": 3,
        "endpointCount": 48
    }
]
```

## Developer

```
# iserver get aci tenant --apic apic21

{
    "duration": 5875,
    "apic": {
        "read": true,
        "success": 13,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 12,
        "connect_time": 450,
        "disconnect_time": 0,
        "mo_time": 4638,
        "total_time": 5088
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

True	450	-	connect apic21o.emea-sp.cisco.com
True	331	12	apic21o.emea-sp.cisco.com class fvTenant
True	426	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	375	23	apic21o.emea-sp.cisco.com class fvCtx
True	343	12	apic21o.emea-sp.cisco.com class fvAp
True	417	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	365	2	apic21o.emea-sp.cisco.com class l2extOut query rsp-subtree=children&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	382	15	apic21o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	357	18	apic21o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	363	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	361	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	382	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	536	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./README.md)