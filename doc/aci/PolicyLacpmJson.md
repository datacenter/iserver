# Policy - Port Channel Member

## JSON

```
# iserver get aci policy lacp-m --apic apic11 --name default -o json

[
    {
        "__Output": {},
        "annotation": "",
        "dn": "uni/infra/lacpifp-default",
        "name": "default",
        "prio": "32768",
        "txRate": "normal",
        "relnFrom": [
            {
                "class": "lacpIfPol",
                "rn": "rtresLacpIfPol",
                "tCl": "infraInfra",
                "tDn": "uni/infra",
                "policyType": "Access Infra",
                "policyName": "infra"
            }
        ],
        "tf": false,
        "tfTick": "",
        "references": 1,
        "l1RsLacpIfPolCons": [
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/1",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/10",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/11",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/13",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/14",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/2",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/23",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/24",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/27",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/4",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/49",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/5",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/50",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/52",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/53",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/55",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/56",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/58",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/59",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/61",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/62",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/64",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/65",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/67",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/68",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/7",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/8",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "201",
                "nodeName": "cl201-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaceId": "eth1/96",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/1",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/10",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/11",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/13",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/14",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/2",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/23",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/24",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/27",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/4",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/49",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/5",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/50",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/52",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/53",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/55",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/56",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/58",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/59",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/61",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/62",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/64",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/65",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/67",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/68",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/7",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/8",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "202",
                "nodeName": "cl202-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaceId": "eth1/96",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "205",
                "nodeName": "bl205-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interfaceId": "eth1/1",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "205",
                "nodeName": "bl205-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interfaceId": "eth1/11",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "205",
                "nodeName": "bl205-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interfaceId": "eth1/12",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "205",
                "nodeName": "bl205-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interfaceId": "eth1/2",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "205",
                "nodeName": "bl205-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interfaceId": "eth1/27",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "206",
                "nodeName": "bl206-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl206-eu-spdc",
                "interfaceId": "eth1/1",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "206",
                "nodeName": "bl206-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl206-eu-spdc",
                "interfaceId": "eth1/11",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "206",
                "nodeName": "bl206-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl206-eu-spdc",
                "interfaceId": "eth1/12",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "206",
                "nodeName": "bl206-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl206-eu-spdc",
                "interfaceId": "eth1/2",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "206",
                "nodeName": "bl206-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/bl206-eu-spdc",
                "interfaceId": "eth1/27",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "301",
                "nodeName": "rl301-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/rl301-eu-spdc",
                "interfaceId": "eth1/3",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "301",
                "nodeName": "rl301-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/rl301-eu-spdc",
                "interfaceId": "eth1/4",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "302",
                "nodeName": "rl302-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/rl302-eu-spdc",
                "interfaceId": "eth1/3",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            },
            {
                "podId": "1",
                "nodeId": "302",
                "nodeName": "rl302-eu-spdc",
                "apic": "apic11",
                "pod_node_name": "pod-1/rl302-eu-spdc",
                "interfaceId": "eth1/4",
                "policyType": "lacpIfPol",
                "policyDn": "uni/infra/lacpifp-default",
                "policyName": "-default"
            }
        ],
        "interfaces": 70,
        "nodeInterfaces": [
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interfaces": 5
            },
            {
                "pod_node_name": "pod-1/bl206-eu-spdc",
                "interfaces": 5
            },
            {
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfaces": 28
            },
            {
                "pod_node_name": "pod-1/cl202-eu-spdc",
                "interfaces": 28
            },
            {
                "pod_node_name": "pod-1/rl301-eu-spdc",
                "interfaces": 2
            },
            {
                "pod_node_name": "pod-1/rl302-eu-spdc",
                "interfaces": 2
            }
        ]
    }
]
```

[[Back]](./PolicyLacpm.md)