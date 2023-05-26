# Node Protocol - IPv4

## Filter IPv4 route table based on IP subnet

Example: Equal IP subnet

```
# iserver get aci proto ipv4 --apic apic11 --node rl --subnet 172.16.21.0/24

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| Node                | VRF       | Prefix         | Next Hop         | Type       | Source          | Interface  | NH VRF    | MPLS Label | Active | Preference |
+---------------------+-----------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.31.2/32  | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.32.2/32  | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
+---------------------+-----------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
```

Example: Contain IP subnet

```
# iserver get aci proto ipv4
    --apic apic11
    --node rl
    --subnet 172.16.21.16/28
    --longer

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| Node                | VRF       | Prefix         | Next Hop         | Type       | Source          | Interface  | NH VRF    | MPLS Label | Active | Preference |
+---------------------+-----------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.31.2/32  | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.32.2/32  | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
+---------------------+-----------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
```

[[Back]](./ProtocolIpv4.md)