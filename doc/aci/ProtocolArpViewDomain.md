# Node Protocol - ARP

## Dom view

```
# iserver get aci proto arp --apic apic21 --node bl2205-eu-spdc --view dom

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Domain [#12]
---------------------------

+----------------------+-------------------------+--------+---------+-----------+
| Node                 | VRF                     | Health | Faults  | Adjacency |
+----------------------+-------------------------+--------+---------+-----------+
| pod-1/bl2205-eu-spdc | black-hole              | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | common:Infra_privIP_VRF | 100    | 0 0 0 0 | 1         | 
| pod-1/bl2205-eu-spdc | common:Infra_VRF        | 100    | 0 0 0 0 | 1         | 
| pod-1/bl2205-eu-spdc | Ericsson_PACO:PDN       | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | management              | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | mgmt:inb                | 100    | 0 0 0 0 | 1         | 
| pod-1/bl2205-eu-spdc | nidemo:streamz-vrf      | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | overlay-1               | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | SPN_IntraLab:SPN_VRF1   | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | 100    | 0 0 0 0 | 5         | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | 100    | 0 0 0 0 | 5         | 
+----------------------+-------------------------+--------+---------+-----------+
```

Developer

```
# iserver get aci proto arp --apic apic21 --node bl2205-eu-spdc --view dom

{
    "duration": 1336,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 819,
        "total_time": 1211
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

True	392	-	connect apic21o.emea-sp.cisco.com:443
True	277	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	291	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	251	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)