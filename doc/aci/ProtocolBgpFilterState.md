# Node Protocol - BGP

## Filter BGP neighbors by state (established|idle)

Example: established (up)

```
# iserver get aci proto bgp --apic apic11 --node rl301 --state up --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#7]
----------------------------

+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
| Node                | VRF                      | Nbr Address   | Router Id       | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP      | Conns (A/D/E) | Paths           |
+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1    | 172.24.3.1      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2    | 172.24.3.2      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3    | 172.24.3.3      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1     | 35.35.35.35     | enabled | established | 64001 | ebgp | 1   | eth1/29  | 15.16.3.2     | 1/0/1         |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1   | 102.102.102.102 | enabled | established | 50000 | ibgp | 1   | lo0      | 172.16.30.160 | 1/0/1         | VPNv4-ucast:393 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228 | 101.101.101.101 | enabled | established | 50000 | ibgp | 1   | lo0      | 172.16.30.160 | 1/0/1         | VPNv4-ucast:393 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35   | 35.35.35.35     | enabled | established | 64001 | ebgp | 2   | lo3      | 172.31.3.31   | 3/0/1         |                 | 
+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
```

Example: idle (down)

```
# iserver get aci proto bgp --apic apic11 --node any --state down --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

Protocol BGP - Neighbor [#37]
-----------------------------

+---------------------+-------------------------------+----------------+-----------+---------+------+-------+------+-----+----------+----------+---------------+--------------+
| Node                | VRF                           | Nbr Address    | Router Id | Admin   | BGP  | ASN   | Type | TTL | Src Intf | Local IP | Conns (A/D/E) | Paths        |
+---------------------+-------------------------------+----------------+-----------+---------+------+-------+------+-----+----------+----------+---------------+--------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1     | 0.0.0.0   | enabled | idle | 64271 | ebgp | 4   | lo9      | 0.0.0.0  | 2447/0/0      | IPv4-ucast:3 | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1     | 0.0.0.0   | enabled | idle | 64271 | ebgp | 4   | lo4      | 0.0.0.0  | 42098/0/0     | IPv4-ucast:3 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.193 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan496  | 0.0.0.0  | 42140/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.194 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan496  | 0.0.0.0  | 42111/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.195 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan496  | 0.0.0.0  | 42090/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.196 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan496  | 0.0.0.0  | 42092/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.193 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan492  | 0.0.0.0  | 42113/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.194 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan492  | 0.0.0.0  | 42076/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.195 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan492  | 0.0.0.0  | 42090/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.196 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan492  | 0.0.0.0  | 42096/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120   | 0.0.0.0   | enabled | idle | 65101 | ebgp | 1   | lo6      | 0.0.0.0  | 0/0/0         |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220   | 0.0.0.0   | enabled | idle | 65101 | ebgp | 8   | lo6      | 0.0.0.0  | 51017/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221   | 0.0.0.0   | enabled | idle | 65101 | ebgp | 10  | lo6      | 0.0.0.0  | 51059/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.194 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan473  | 0.0.0.0  | 42083/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.195 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan473  | 0.0.0.0  | 42073/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.196 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan473  | 0.0.0.0  | 42105/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.194 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan494  | 0.0.0.0  | 42103/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.195 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan494  | 0.0.0.0  | 42096/0/0     |              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.196 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan494  | 0.0.0.0  | 42066/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.41    | 0.0.0.0   | enabled | idle | 65101 | ebgp | 5   | lo5      | 0.0.0.0  | 51016/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.193 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan488  | 0.0.0.0  | 42112/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.194 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan488  | 0.0.0.0  | 42085/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.195 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan488  | 0.0.0.0  | 42113/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.196 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan488  | 0.0.0.0  | 42084/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.193 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan472  | 0.0.0.0  | 42105/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.194 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan472  | 0.0.0.0  | 42126/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.195 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan472  | 0.0.0.0  | 42140/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.196 | 0.0.0.0   | enabled | idle | 65066 | ebgp | 1   | vlan472  | 0.0.0.0  | 42091/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120   | 0.0.0.0   | enabled | idle | 65101 | ebgp | 1   | lo4      | 0.0.0.0  | 0/0/0         |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220   | 0.0.0.0   | enabled | idle | 65101 | ebgp | 8   | lo4      | 0.0.0.0  | 51065/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221   | 0.0.0.0   | enabled | idle | 65101 | ebgp | 10  | lo4      | 0.0.0.0  | 51019/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.41  | 0.0.0.0   | enabled | idle | 65101 | ebgp | 5   | lo7      | 0.0.0.0  | 50469/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.194 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan468  | 0.0.0.0  | 42120/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.195 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan468  | 0.0.0.0  | 42089/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.194 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan490  | 0.0.0.0  | 42078/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.195 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan490  | 0.0.0.0  | 42134/0/0     |              | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.196 | 0.0.0.0   | enabled | idle | 65069 | ebgp | 1   | vlan490  | 0.0.0.0  | 42077/0/0     |              | 
+---------------------+-------------------------------+----------------+-----------+---------+------+-------+------+-----+----------+----------+---------------+--------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --state up --view nei

{
    "duration": 3831,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 504,
        "disconnect_time": 0,
        "mo_time": 3150,
        "total_time": 3654
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

True	504	-	connect apic11o.emea-sp.cisco.com:443
True	295	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	287	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	319	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	280	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	282	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[15.16.3.1/32]/ent-[15.16.3.1]/peerstats
True	268	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.31.3.35/32]/ent-[172.31.3.35]/peerstats
True	279	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.228/32]/ent-[172.16.11.228]/peerstats
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.1/32]/ent-[172.16.11.1]/peerstats
True	280	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	304	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
```

[[Back]](./ProtocolBgp.md)