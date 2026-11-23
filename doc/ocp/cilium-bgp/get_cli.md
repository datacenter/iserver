# Cilium BGP Control Plane - Get cilium cli output

## Workflow

- run `cilium bgp` commands on the cluster [management node](../ManagementServer.md)

## Requirements

[Management node](../ManagementServer.md) configured

## Configurable options

```
# iserver get ocp cilium bgp -v cli
  --cluster TEXT     Cluster Name
```

## Example

```
# iserver get ocp cilium bgp --cluster bm1 -v cli

OpenShift Workflow - Cilium BGP Control Plane - Get
===================================================

OpenShift Cluster: bm1

~~~
# cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address   Session State   Uptime   Family         Received   Advertised
bm1-1   64661      64001     10.10.10.20    established     37s      ipv4/unicast   0          2
        64661      64001     10.10.10.21    established     37s      ipv4/unicast   0          2
bm1-2   64661      64001     10.10.10.20    established     37s      ipv4/unicast   0          2
        64661      64001     10.10.10.21    established     37s      ipv4/unicast   0          2
bm1-3   64661      64001     10.10.10.20    established     37s      ipv4/unicast   0          2
        64661      64001     10.10.10.21    established     37s      ipv4/unicast   0          2

~~~

~~~
# cilium bgp routes advertised ipv4 unicast -n cilium
Node    VRouter   Peer          Prefix          NextHop       Age   Attrs
bm1-1   64661     10.10.10.20   10.128.2.0/23   10.10.10.10   39s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.10} {Communities: 64661:100, blackhole}]
        64661     10.10.10.21   10.128.2.0/23   10.10.10.10   39s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.10} {Communities: 64661:100, blackhole}]
bm1-2   64661     10.10.10.20   10.128.4.0/23   10.10.10.11   39s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.11} {Communities: 64661:100, blackhole}]
        64661     10.10.10.21   10.128.4.0/23   10.10.10.11   39s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.11} {Communities: 64661:100, blackhole}]
bm1-3   64661     10.10.10.20   10.128.0.0/23   10.10.10.12   39s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.12} {Communities: 64661:100, blackhole}]
        64661     10.10.10.21   10.128.0.0/23   10.10.10.12   39s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.12} {Communities: 64661:100, blackhole}]

~~~

~~~
# cilium bgp routes advertised ipv4 mpls_vpn -n cilium
Node   VRouter   Peer   Prefix   NextHop   Age   Attrs

~~~

~~~
# cilium bgp routes advertised ipv6 unicast -n cilium
Node   VRouter   Peer   Prefix   NextHop   Age   Attrs

~~~
```

[[Back]](./README.md)