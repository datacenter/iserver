# Policy - CDP

## Usage specific output

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view usage

Apic: apic11

+-------------+---------------------+-----------------+-------------------------------+----------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type               | Ref Policy Name      |
+-------------+---------------------+-----------------+-------------------------------+----------------------+
| cdp-enabled | pod-1/bl205-eu-spdc | 1               | Leaf Access Port Policy Group | BERLIN-35-RDC-3-vlan | 
|             | pod-1/bl206-eu-spdc | 1               | Leaf Access Port Policy Group | SR-Demo-CDC-2-vlan   | 
|             | pod-1/rl301-eu-spdc | 1               | Leaf Access Port Policy Group | SR-Demo-RDC-3-vlan   | 
|             | pod-1/rl302-eu-spdc | 1               |                               |                      | 
+-------------+---------------------+-----------------+-------------------------------+----------------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view usage

{
    "duration": 1616,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 1092,
        "total_time": 1477
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
    }
}

Log: apic
----------

True	385	-	connect apic11o.emea-sp.cisco.com
True	324	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	442	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	326	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)