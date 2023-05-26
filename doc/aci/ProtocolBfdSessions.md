# Node Protocol - BFD

## Get BFD sessions from all nodes

```
# iserver get aci proto bfd --apic apic11 --node any

Apic: apic11
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

+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
| Node                | Local Address  | State | Session Id | Remote Address | State | Session Id | Type      | VRF                           | Interface |
+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
| pod-1/bl205-eu-spdc | 172.31.2.25    | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop  | overlay-1                     | lo3       | 
| pod-1/bl206-eu-spdc | 172.31.2.26    | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop  | overlay-1                     | lo3       | 
| pod-1/cl201-eu-spdc | 15.254.101.4   | down  | 1090519041 | 15.100.7.41    | down  | 0          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan468   | 
| pod-1/cl201-eu-spdc | 15.254.103.252 | up    | 1090519045 | 15.254.103.192 | up    | 3          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan469   | 
| pod-1/cl201-eu-spdc | 15.254.103.252 | up    | 1090519047 | 15.254.103.191 | up    | 3          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan469   | 
| pod-1/cl201-eu-spdc | 15.254.106.252 | up    | 1090519043 | 15.254.106.191 | up    | 1          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan473   | 
| pod-1/cl201-eu-spdc | 15.254.106.252 | up    | 1090519049 | 15.254.106.192 | up    | 1          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan473   | 
| pod-1/cl202-eu-spdc | 15.254.104.253 | up    | 1090519042 | 15.254.104.191 | up    | 4          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan491   | 
| pod-1/cl202-eu-spdc | 15.254.104.253 | up    | 1090519045 | 15.254.104.192 | up    | 4          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan491   | 
| pod-1/cl202-eu-spdc | 15.254.107.253 | up    | 1090519044 | 15.254.107.192 | up    | 2          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan494   | 
| pod-1/cl202-eu-spdc | 15.254.107.253 | up    | 1090519046 | 15.254.107.191 | up    | 2          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan494   | 
| pod-1/rl301-eu-spdc | 172.31.3.31    | down  | 1090519041 | 172.31.3.35    | down  | 0          | multihop  | overlay-1                     | lo4       | 
| pod-1/rl302-eu-spdc | 172.31.3.32    | down  | 1090519041 | 172.31.3.35    | down  | 0          | multihop  | overlay-1                     | lo4       | 
+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
```

[[Back]](./ProtocolBfd.md)