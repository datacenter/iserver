# eBPF Maps

[[Back]](./README.md)

The applications connected to private network deployed in the test setup

```
$ oc get pod -o wide
NAME    READY   STATUS    RESTARTS   AGE     IP             NODE  
b1      1/1     Running   1          22d     10.128.3.75    bm1-1
b2      1/1     Running   1          22d     10.128.4.29    bm1-2
b3      1/1     Running   1          22d     10.128.1.51    bm1-3
r1      1/1     Running   0          7d19h   10.128.3.160   bm1-1
r2      1/1     Running   0          7d19h   10.128.4.124   bm1-2
r3      1/1     Running   0          7d19h   10.128.1.199   bm1-3
```

Corresponding state of (selected) eBPF maps

```shell
kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell
```

| Command | Description |
|---------|-------------|
| `db/show privnet-endpoints` | Show all PrivNet endpoints (local + remote) with network IP and PIP mappings |
| `db/show privnet-routes` | Show routing table including auto-generated peering routes |
| `db/show privnet-subnets` | Show subnets with DHCP mode and interface bindings (local-access) |
| `db/show privnet-dhcp-leases` | Show DHCP leases with renewal/expiry times |
| `db/show privnet-local-workloads` | Show local workloads with PrivNet/PIP mappings |
| `db/show privnet-inbs` | Show connected INB instances and their health/role |
| `db/show vni-mappings` | VNI to network id mapping |
| `privnet/status` | Show overall PrivNet status including INB HA state |

## Endpoints

```
$ kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell -- db/show privnet-endpoints
Source                  Name   Network   Subnet    NetworkIP     NetworkMAC          PodIP          ActivatedAt
default/default/bm1-1   b1     blue      subnet0   10.0.200.11   9e:5e:3c:f1:19:c0   10.128.3.75    2026-06-08T16:16:45Z
default/default/bm1-1   r1     red       subnet0   10.0.100.11   92:84:6c:da:7f:0f   10.128.3.160   2026-06-17T12:24:00Z
default/default/bm1-2   b2     blue      subnet0   10.0.200.12   1a:4b:dc:30:db:4a   10.128.4.29    2026-06-08T16:17:21Z
default/default/bm1-2   r2     red       subnet0   10.0.100.12   4e:c4:bf:41:a5:34   10.128.4.124   2026-06-17T12:24:00Z
default/default/bm1-3   b3     blue      subnet0   10.0.200.13   3e:11:cf:64:a6:07   10.128.1.51    2026-06-08T16:18:35Z
default/default/bm1-3   r3     red       subnet0   10.0.100.13   8e:ce:4e:9c:cd:5c   10.128.1.199   2026-06-17T12:24:00Z
```

## Subnets

```
$ kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell -- db/show privnet-subnets
Network   Name      ID       CIDRv4          CIDRv6   Routes   DHCP   Interface
blue      subnet0   0xc8fd   10.0.200.0/24   -        1        none   N/A
red       subnet0   0x86eb   10.0.100.0/24   -        1        none   N/A
```

## Routes

```
$ kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell -- db/show privnet-routes
Network   Subnet    Destination     Gateway
blue      subnet0   0.0.0.0/0       evpn
blue      subnet0   10.0.200.0/24   N/A
red       subnet0   0.0.0.0/0       evpn
red       subnet0   10.0.100.0/24   N/A
```

## VNI Mappings

```
$ kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell -- db/show vni-mappings
VNI     NetworkID
50002   35644
60000   35811
```

## Status

```
$ kubectl exec -ti ds/cilium -n cilium -c cilium-agent -- cilium-dbg shell 
    /¯¯\
 /¯¯\__/¯¯\
 \__/¯¯\__/  Cilium 1.19.0 96c34b91 2026-04-13T11:45:17+02:00 go version go1.25.8 linux/amd64
 /¯¯\__/¯¯\  Welcome to the Cilium Shell! Type 'help' for list of commands.
 \__/¯¯\__/
    \__/

bm1-2> privnet/status
Node                                            bm1-2                                     Status  OK

  Network blue                                                                                    OK
    Subnets   10.0.200.0/24
    Routes    0.0.0.0/0 via invalid IP
    Local Endpoints 1                                                              Total Endpoints 3

    Endpoints           default (local)     3 Endpoints

    Connected INBs    
      No connected INBs
    
  Network red                                                                                     OK
    Subnets   10.0.100.0/24
    Routes    0.0.0.0/0 via invalid IP
    Local Endpoints 1                                                              Total Endpoints 3

    Endpoints           default (local)     3 Endpoints

    Connected INBs    
      No connected INBs
```

[[Back]](./README.md)