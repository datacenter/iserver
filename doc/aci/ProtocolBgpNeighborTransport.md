# Node Protocol - BGP

## Show IP transport related attributes of selected BGP neighbors

```
# iserver get aci proto bgp --apic apic11 --node rl -o trans

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-----------------+-------------+-------------+-------+------+-----+-------------+---------------+
| Node                | VRF                      | Neighbor Address | Router Id       | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP      |
+---------------------+--------------------------+------------------+-----------------+-------------+-------------+-------+------+-----+-------------+---------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 172.24.3.1      | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.15   | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 172.24.3.2      | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.15   | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3      | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.15   | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1        | 35.35.35.35     | enabled     | established | 64001 | ebgp | 1   | eth1/29     | 15.16.3.2     | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1      | 102.102.102.102 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.160 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228    | 101.101.101.101 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.160 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35      | 35.35.35.35     | enabled     | established | 64001 | ebgp | 2   | lo4         | 172.31.3.31   | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 172.24.3.1      | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14   | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 172.24.3.2      | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14   | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3      | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14   | 
| pod-1/rl302-eu-spdc | overlay-1                | 15.16.3.5        | 35.35.35.35     | enabled     | established | 64001 | ebgp | 1   | eth1/29     | 15.16.3.6     | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.1      | 102.102.102.102 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.120 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.228    | 101.101.101.101 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.120 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35      | 35.35.35.35     | enabled     | established | 64001 | ebgp | 2   | lo4         | 172.31.3.32   | 
+---------------------+--------------------------+------------------+-----------------+-------------+-------------+-------+------+-----+-------------+---------------+
```

[[Back]](./ProtocolBgp.md)