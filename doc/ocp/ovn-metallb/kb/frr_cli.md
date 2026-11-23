# MetalLB - FRR CLI access

[[Back]](../README.md) 

```
$ oc get pod -n metallb-system -l component=speaker -o wide
NAME            READY   STATUS    RESTARTS   AGE     IP             NODE    NOMINATED NODE   READINESS GATES
speaker-d4lr8   6/6     Running   0          7m13s   10.10.10.211   bm1-2   <none>           <none>
speaker-g8lz6   6/6     Running   0          7m13s   10.10.10.212   bm1-3   <none>           <none>
speaker-wlgdt   6/6     Running   0          7m13s   10.10.10.210   bm1-1   <none>           <none>
```

```
# iserver get ocp metallb --cluster bm1 -v cli

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1

+----+-------+------------------------------+-------+-------------------------------------------------------------+
| ID | Host  | Pod                          | Ready | FRR cli                                                     |
+----+-------+------------------------------+-------+-------------------------------------------------------------+
| 1  | bm1-1 | metallb-system/speaker-wlgdt | 6/6   | oc exec -it -n metallb-system speaker-wlgdt -c frr -- vtysh |
| 2  | bm1-2 | metallb-system/speaker-d4lr8 | 6/6   | oc exec -it -n metallb-system speaker-d4lr8 -c frr -- vtysh |
| 3  | bm1-3 | metallb-system/speaker-g8lz6 | 6/6   | oc exec -it -n metallb-system speaker-g8lz6 -c frr -- vtysh |
+----+-------+------------------------------+-------+-------------------------------------------------------------+
```

```
$ oc exec -it -n metallb-system speaker-wlgdt -c frr -- vtysh
[root@bm1-1 ~]# vtysh 

Hello, this is FRRouting (version 8.5.3).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

bm1-1# show
  bfd               Bidirection Forwarding Detection
  bgp               BGP information
  bmp               BGP Monitoring Protocol
  daemons           Show list of running daemons
  debugging         State of each debugging option
  dmvpn             DMVPN information
  error             Information on errors
  evpn              EVPN
  fpm               Forwarding Plane Manager configuration
  history           The list of commands stored in history
  interface         Interface status and configuration
  ip                IP information
  ipv6              IPv6 information
  isis              IS-IS routing protocol
  logging           Show current logging configuration
  mac               mac access lists
  memory            Memory statistics
  modules           Loaded modules
  motd              Show motd
  mpls              MPLS information
  nexthop-group     Show Nexthop Groups
  openfabric        OpenFabric routing protocol
  pathd             pathd daemon
  pbr               Policy-Based Routing
  route-map         route-map information
  route-map-unused  unused route-map information
  router-id         Show the configured router-id
  running-config    Current operating configuration
  segment-routing   Segment Routing
  sr-te             SR-TE info
  startup-config    Contents of startup configuration
  thread            Thread information
  version           Displays zebra version
  vnc               VNC information
  vrf               VRF
  vrrp              Virtual Router Redundancy Protocol
  watchfrr          watchfrr information
  work-queues       Work Queue information
  yang              YANG information
  zebra             Zebra information
```

[[Back]](../README.md) 