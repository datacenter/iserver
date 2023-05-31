# Policy - CDP

## Verbose output

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view verbose

Apic: apic11

CDP Policy Properties
---------------------
- Policy Name : cdp-enabled
- TF          : False
- Admin State : enabled


+---------------------+-----------+
| Node                | Interface |
+---------------------+-----------+
| pod-1/bl205-eu-spdc | eth1/28   | 
| pod-1/bl206-eu-spdc | eth1/28   | 
| pod-1/rl301-eu-spdc | eth1/29   | 
| pod-1/rl302-eu-spdc | eth1/29   | 
+---------------------+-----------+

+----------------------+-------------------------------+-----------------+
| Policy Name          | Policy Type                   | Policy Class    |
+----------------------+-------------------------------+-----------------+
| BERLIN-35-RDC-3-vlan | Leaf Access Port Policy Group | infraAccPortGrp | 
| SR-Demo-CDC-2-vlan   | Leaf Access Port Policy Group | infraAccPortGrp | 
| SR-Demo-RDC-3-vlan   | Leaf Access Port Policy Group | infraAccPortGrp | 
+----------------------+-------------------------------+-----------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view verbose

{
    "duration": 1616,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 1095,
        "total_time": 1492
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	325	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	437	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	333	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)