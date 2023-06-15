# Node Protocol - IPv6

## JSON

```
# iserver get aci proto ipv6 --apic apic11 --node cl201-eu-spdc -o json

{
      "summary": [
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-black-hole",
                  "modTs": "2023-06-12T09:13:34.000+02:00",
                  "name": "black-hole",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:Infra_BGP_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "common:Infra_BGP_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:Infra_privIP_VRF",
                  "modTs": "2023-06-12T10:35:41.000+02:00",
                  "name": "common:Infra_privIP_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:Infra_VRF",
                  "modTs": "2023-06-12T10:35:53.000+02:00",
                  "name": "common:Infra_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1-N3-N4_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "common:smi5Gc-cvim1-N3-N4_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1-N6_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "common:smi5Gc-cvim1-N6_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "common:smi5Gc-cvim1_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim4-N3-N4_VRF",
                  "modTs": "2023-06-12T10:35:44.000+02:00",
                  "name": "common:smi5Gc-cvim4-N3-N4_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim4-N6_VRF",
                  "modTs": "2023-06-12T10:35:22.000+02:00",
                  "name": "common:smi5Gc-cvim4-N6_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim4_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "common:smi5Gc-cvim4_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-cvim1a:cvim1a-tenant_VRF",
                  "modTs": "2023-06-12T10:35:16.000+02:00",
                  "name": "cvim1a:cvim1a-tenant_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-cvim1a:cvim1a_VRF",
                  "modTs": "2023-06-12T10:35:22.000+02:00",
                  "name": "cvim1a:cvim1a_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-cvim4a:cvim4a-tenant_VRF",
                  "modTs": "2023-06-12T10:35:19.000+02:00",
                  "name": "cvim4a:cvim4a-tenant_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-cvim4a:cvim4a_VRF",
                  "modTs": "2023-06-12T10:35:22.000+02:00",
                  "name": "cvim4a:cvim4a_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-ECMP-demo:ACC-ext_VRF",
                  "modTs": "2023-06-12T10:35:48.000+02:00",
                  "name": "ECMP-demo:ACC-ext_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-ECMP-demo:MPC-CDC-2_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "ECMP-demo:MPC-CDC-2_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-iks-monitoring:iks-mon_VRF",
                  "modTs": "2023-06-12T10:35:24.000+02:00",
                  "name": "iks-monitoring:iks-mon_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-management",
                  "modTs": "2023-06-12T10:35:22.000+02:00",
                  "name": "management",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-mgmt:EU-SPDC-ERSPAN-VRF",
                  "modTs": "2023-06-12T10:35:18.000+02:00",
                  "name": "mgmt:EU-SPDC-ERSPAN-VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-mgmt:inb",
                  "modTs": "2023-06-12T10:35:47.000+02:00",
                  "name": "mgmt:inb",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-MPC-E:MPC-E-sPBR-OUT_VRF",
                  "modTs": "2023-06-12T10:35:23.000+02:00",
                  "name": "MPC-E:MPC-E-sPBR-OUT_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-MPC-F5T:F5-IN_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "MPC-F5T:F5-IN_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-MPC-F5T:F5-OUT_VRF",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "MPC-F5T:F5-OUT_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-MPC:MPC-sPBR-IN_VRF",
                  "modTs": "2023-06-12T10:35:46.000+02:00",
                  "name": "MPC:MPC-sPBR-IN_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-MPC:MPC-sPBR-OUT_VRF",
                  "modTs": "2023-06-12T10:35:29.000+02:00",
                  "name": "MPC:MPC-sPBR-OUT_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-NXOS-HandOff_Test:default",
                  "modTs": "2023-06-12T10:35:53.000+02:00",
                  "name": "NXOS-HandOff_Test:default",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-overlay-1",
                  "modTs": "2023-06-12T09:13:34.000+02:00",
                  "name": "overlay-1",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-P5G:P5G_VRF",
                  "modTs": "2023-06-12T10:35:53.000+02:00",
                  "name": "P5G:P5G_VRF",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-SPIN_InnoLab:SPIN_VRF1",
                  "modTs": "2023-06-12T10:35:10.000+02:00",
                  "name": "SPIN_InnoLab:SPIN_VRF1",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-SPN_IntraLab:SPN_VRF1",
                  "modTs": "2023-06-12T10:35:40.000+02:00",
                  "name": "SPN_IntraLab:SPN_VRF1",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            },
            {
                  "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                  },
                  "childAction": "",
                  "dn": "topology/pod-1/node-201/sys/uribv6/dom-TESTING_BRUNO:default",
                  "modTs": "2023-06-12T10:35:53.000+02:00",
                  "name": "TESTING_BRUNO:default",
                  "operSt": "up",
                  "status": "",
                  "pod_node_name": "pod-1/cl201-eu-spdc",
                  "routes": [],
                  "routes_summary": {
                        "count": 0,
                        "default": false,
                        "ebgp": 0,
                        "ibgp": 0,
                        "bgp": 0,
                        "local": 0,
                        "direct": 0
                  }
            }
      ],
      "route": []
}
```

[[Back]](./ProtocolIpv6.md)