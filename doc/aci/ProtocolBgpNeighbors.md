# Node Protocol - BGP

## Get BGP neighbors from all nodes

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

```
# iserver get aci proto bgp --apic apic11 --node any

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

+---------------------+-------------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                           | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+-------------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.1    | established | 64701 | ebgp | 1   | 31              | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.66   | established | 64701 | ebgp | 5   | 68              | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.98   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.102  | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.90   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.94   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl205-eu-spdc | mgmt:inb                      | 192.168.254.17   | established | 64701 | ebgp | 1   | 31              | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1       | idle        | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.1       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.2       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.3       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.4       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.5       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.6       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl205-eu-spdc | overlay-1                     | 10.3.192.65      | established | 50000 | ibgp | 1   |                 | 
| pod-1/bl205-eu-spdc | overlay-1                     | 10.3.32.65       | established | 50000 | ibgp | 1   |                 | 
| pod-1/bl205-eu-spdc | overlay-1                     | 15.16.2.1        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/bl205-eu-spdc | overlay-1                     | 172.31.2.54      | established | 64001 | ebgp | 2   |                 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.41   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.101     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.103     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.105     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.106     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.104     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.102     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 192.168.254.105  | established | 64701 | ebgp | 1   | 31              | 
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.5    | established | 64701 | ebgp | 1   | 31              | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.70   | established | 64701 | ebgp | 5   | 68              | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.96   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.100  | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.88   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.92   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl206-eu-spdc | mgmt:inb                      | 192.168.254.21   | established | 64701 | ebgp | 1   | 1               | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1       | idle        | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.1       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.2       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.3       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.4       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.5       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.6       | established | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | overlay-1                     | 10.3.192.65      | established | 50000 | ibgp | 1   |                 | 
| pod-1/bl206-eu-spdc | overlay-1                     | 10.3.32.65       | established | 50000 | ibgp | 1   |                 | 
| pod-1/bl206-eu-spdc | overlay-1                     | 15.16.2.5        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/bl206-eu-spdc | overlay-1                     | 172.31.2.54      | established | 64001 | ebgp | 2   |                 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.45   | established | 64701 | ebgp | 1   | 27              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.101     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.103     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.105     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.106     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.104     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 10.58.24.102     | established | 65321 | ebgp | 2   | 10              | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 192.168.254.107  | established | 64701 | ebgp | 1   | 1               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.101     | established | 65100 | ebgp | 5   | 16              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.41      | established | 65101 | ebgp | 5   | 5               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.191   | established | 65066 | ebgp | 1   | 7               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.192   | established | 65066 | ebgp | 1   | 7               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.193   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.194   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.195   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.196   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.191   | established | 65066 | ebgp | 1   | 5               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.192   | established | 65066 | ebgp | 1   | 5               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.193   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.194   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.195   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.196   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120     | idle        | 65101 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220     | idle        | 65101 | ebgp | 8   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221     | idle        | 65101 | ebgp | 10  | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.101   | established | 65100 | ebgp | 5   | 16              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.41    | idle        | 65101 | ebgp | 5   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.191   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.192   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.193   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.194   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.195   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.196   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.191   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.192   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.193   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.194   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.195   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.196   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.65      | established | 50000 | ibgp | 1   |                 | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.32.65       | established | 50000 | ibgp | 1   |                 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.101     | established | 65100 | ebgp | 5   | 16              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.41      | idle        | 65101 | ebgp | 5   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.191   | established | 65066 | ebgp | 1   | 7               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.192   | established | 65066 | ebgp | 1   | 7               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.193   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.194   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.195   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.196   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.191   | established | 65066 | ebgp | 1   | 5               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.192   | established | 65066 | ebgp | 1   | 5               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.193   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.194   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.195   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.196   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120     | idle        | 65101 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220     | idle        | 65101 | ebgp | 8   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221     | idle        | 65101 | ebgp | 10  | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.101   | established | 65100 | ebgp | 5   | 16              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.41    | idle        | 65101 | ebgp | 5   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.191   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.192   | shut        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.193   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.194   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.195   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.196   | shut        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.191   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.192   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.193   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.194   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.195   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.196   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | overlay-1                     | 10.3.192.65      | established | 50000 | ibgp | 1   |                 | 
| pod-1/cl202-eu-spdc | overlay-1                     | 10.3.32.65       | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.1       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.2       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | overlay-1                     | 15.16.3.1        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl301-eu-spdc | overlay-1                     | 172.16.11.1      | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 172.16.11.228    | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 172.31.3.35      | established | 64001 | ebgp | 2   |                 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.1       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.2       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | overlay-1                     | 15.16.3.5        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl302-eu-spdc | overlay-1                     | 172.16.11.1      | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 172.16.11.228    | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 172.31.3.35      | established | 64001 | ebgp | 2   |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 10.3.192.64      | established | 50000 | ibgp | 1   |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 10.3.192.67      | established | 50000 | ibgp | 1   |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 10.3.32.64       | established | 50000 | ibgp | 1   |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 10.3.192.68      | established | 50000 | ibgp | 1   |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 111.111.111.111  | established | 52000 | ebgp | 16  |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 112.112.112.112  | established | 52000 | ebgp | 16  |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 172.16.30.160    | established | 50000 | ibgp | 1   |                 | 
| pod-1/s101-eu-spdc  | overlay-1                     | 172.16.30.120    | established | 50000 | ibgp | 1   |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 10.3.192.68      | established | 50000 | ibgp | 1   |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 10.3.192.67      | established | 50000 | ibgp | 1   |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 10.3.32.64       | established | 50000 | ibgp | 1   |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 10.3.192.64      | established | 50000 | ibgp | 1   |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 111.111.111.111  | established | 52000 | ebgp | 16  |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 112.112.112.112  | established | 52000 | ebgp | 16  |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 172.16.30.160    | established | 50000 | ibgp | 1   |                 | 
| pod-1/s102-eu-spdc  | overlay-1                     | 172.16.30.120    | established | 50000 | ibgp | 1   |                 | 
+---------------------+-------------------------------+------------------+-------------+-------+------+-----+-----------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any

{
    "duration": 8753,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 7835,
        "total_time": 8225
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

True	390	-	connect apic11o.emea-sp.cisco.com
True	304	11	apic11o.emea-sp.cisco.com class fabricNode
True	587	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	290	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	319	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	301	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	305	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	289	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	315	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	271	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	321	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	327	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	312	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	325	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	284	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	293	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	294	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	296	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	294	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	292	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)