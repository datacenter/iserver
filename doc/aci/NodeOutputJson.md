# Node

## JSON

```
# iserver get aci node --apic apic11 -o json

[
    {
        "__Output": {
            "adSt": "Green"
        },
        "address": "10.3.0.1",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-1",
        "id": "1",
        "fabricSt": "",
        "model": "APIC-SERVER-M3",
        "name": "apic1",
        "nodeType": "unspecified",
        "role": "controller",
        "serial": "WZP234408RN",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "5.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/apic1",
        "roleUi": "controller"
    },
    {
        "__Output": {
            "adSt": "Green"
        },
        "address": "10.3.0.2",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-2",
        "id": "2",
        "fabricSt": "",
        "model": "APIC-SERVER-M3",
        "name": "apic2",
        "nodeType": "unspecified",
        "role": "controller",
        "serial": "WZP234310FJ",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "5.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/apic2",
        "roleUi": "controller"
    },
    {
        "__Output": {
            "adSt": "Green"
        },
        "address": "10.3.0.3",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-3",
        "id": "3",
        "fabricSt": "",
        "model": "APIC-SERVER-M3",
        "name": "apic3",
        "nodeType": "unspecified",
        "role": "controller",
        "serial": "WZP234408PR",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "5.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/apic3",
        "roleUi": "controller"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "10.3.192.64",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-205",
        "id": "205",
        "fabricSt": "active",
        "model": "N9K-C93600CD-GX",
        "name": "bl205-eu-spdc",
        "nodeType": "unspecified",
        "role": "leaf",
        "serial": "FDO233804F9",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl205-eu-spdc",
        "roleUi": "leaf"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "10.3.32.64",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-206",
        "id": "206",
        "fabricSt": "active",
        "model": "N9K-C93600CD-GX",
        "name": "bl206-eu-spdc",
        "nodeType": "unspecified",
        "role": "leaf",
        "serial": "FDO24300ZJH",
        "userdom": "all",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl206-eu-spdc",
        "roleUi": "leaf"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "10.3.192.67",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-201",
        "id": "201",
        "fabricSt": "active",
        "model": "N9K-C93360YC-FX2",
        "name": "cl201-eu-spdc",
        "nodeType": "unspecified",
        "role": "leaf",
        "serial": "FDO23350LNB",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/cl201-eu-spdc",
        "roleUi": "leaf"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "10.3.192.68",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-202",
        "id": "202",
        "fabricSt": "active",
        "model": "N9K-C93360YC-FX2",
        "name": "cl202-eu-spdc",
        "nodeType": "unspecified",
        "role": "leaf",
        "serial": "FDO23350LJY",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/cl202-eu-spdc",
        "roleUi": "leaf"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "172.16.30.160",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-301",
        "id": "301",
        "fabricSt": "active",
        "model": "N9K-C9336C-FX2",
        "name": "rl301-eu-spdc",
        "nodeType": "remote-leaf-wan",
        "role": "leaf",
        "serial": "FDO2346137N",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/rl301-eu-spdc",
        "roleUi": "remote leaf"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "172.16.30.120",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-302",
        "id": "302",
        "fabricSt": "active",
        "model": "N9K-C9336C-FX2",
        "name": "rl302-eu-spdc",
        "nodeType": "remote-leaf-wan",
        "role": "leaf",
        "serial": "FDO234613DB",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/rl302-eu-spdc",
        "roleUi": "remote leaf"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "10.3.192.65",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-101",
        "id": "101",
        "fabricSt": "active",
        "model": "N9K-C9316D-GX",
        "name": "s101-eu-spdc",
        "nodeType": "unspecified",
        "role": "spine",
        "serial": "FDO233806C2",
        "userdom": "",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/s101-eu-spdc",
        "roleUi": "spine"
    },
    {
        "__Output": {
            "adSt": "Green",
            "fabricSt": "Green"
        },
        "address": "10.3.32.65",
        "adSt": "on",
        "apicType": "apic",
        "dn": "topology/pod-1/node-102",
        "id": "102",
        "fabricSt": "active",
        "model": "N9K-C9316D-GX",
        "name": "s102-eu-spdc",
        "nodeType": "unspecified",
        "role": "spine",
        "serial": "FDO24350JND",
        "userdom": "all",
        "vendor": "Cisco Systems, Inc",
        "version": "n9000-15.2(7f)",
        "podId": "1",
        "apic": "apic11",
        "pod_node_name": "pod-1/s102-eu-spdc",
        "roleUi": "spine"
    }
]
```

[[Back]](./Node.md)