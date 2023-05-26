# Node Protocol - BGP

## Show BGP selected VRF domains for selected nodes

```
# iserver get aci proto bgp --apic apic11 --node any --vrf overlay-1 -o vrf

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
| Node                | VRF       | BGP State | Mode   | Router ID       | RD                  | Neighbors | Established |
+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
| pod-1/bl205-eu-spdc | overlay-1 | up        | fabric | 125.125.125.125 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/bl206-eu-spdc | overlay-1 | up        | fabric | 126.126.126.126 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/cl201-eu-spdc | overlay-1 | up        | fabric | 10.3.192.67     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/cl202-eu-spdc | overlay-1 | up        | fabric | 10.3.192.68     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/rl301-eu-spdc | overlay-1 | up        | fabric | 131.131.131.131 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/rl302-eu-spdc | overlay-1 | up        | fabric | 132.132.132.132 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/s101-eu-spdc  | overlay-1 | up        | fabric | 101.101.101.101 | unknown:unknown:0:0 | 8         | 8           | 
| pod-1/s102-eu-spdc  | overlay-1 | up        | fabric | 102.102.102.102 | unknown:unknown:0:0 | 8         | 8           | 
+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
```

[[Back]](./ProtocolBgp.md)