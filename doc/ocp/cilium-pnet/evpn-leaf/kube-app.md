## Application

[[Back]](./README.md) [[Next]](./kube-baseline.md)

>[!NOTE]
>Application can be POD or Kubevirt VM. In this case study, only PODs are used.

POD | PrivNet | IP address | Node
--- | --- | --- | ---
r1 | red | 10.0.100.11 | bm1-1
r2 | red | 10.0.100.12 | bm1-2
r3 | red | 10.0.100.13 | bm1-3
b1 | blue | 10.0.200.11 | bm1-1
b2 | blue | 10.0.200.12 | bm1-2
b3 | blue | 10.0.200.13 | bm1-3

## POD

Showing single pod for brevity, refer to [complete configuration reference](./kube-baseline.md) for details.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: r1
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "red",
        "ipv4": "10.0.100.11"
      }
spec:
  nodeName: bm1-1
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
```
## Expected outcome

>[!NOTE]
>It is expected to see POD IP from POD CIDR in the output below

```
$ oc get pod -o wide
NAME    READY   STATUS    RESTARTS   AGE     IP             NODE  
b1      1/1     Running   0          7s      10.128.2.92    bm1-1
b2      1/1     Running   0          7s      10.128.4.230   bm1-2
b3      1/1     Running   0          7s      10.128.0.181   bm1-3
r1      1/1     Running   0          12s     10.128.2.246   bm1-1
r2      1/1     Running   0          12s     10.128.4.222   bm1-2
r3      1/1     Running   0          12s     10.128.1.167   bm1-3
```

The actual pod's ip address can be checked in two ways

```
$ oc get pod r1 -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    privnet.isovalent.com/network-attachment: |-
      {
        "network": "red",
        "ipv4": "10.0.100.11"
      }
```

```
$ oc exec -it r1 -- ip a
7637: eth0@if7638: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default 
    inet 10.0.100.11/32 scope global eth0
```

BGP advertisement of pod's /32 addresses in private network, every server advertises one ip address of pod in each private network

```
$ cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address                     Session State   Uptime     Family         Received   Advertised
bm1-1   666        64000     100.64.10.201                    established     12m34s     l2vpn/evpn     15         2    
        666        64000     100.64.10.202                    established     12m34s     l2vpn/evpn     15         2    
bm1-2   666        64000     100.64.10.201                    established     6h18m48s   l2vpn/evpn     15         2    
        666        64000     100.64.10.202                    established     6h18m53s   l2vpn/evpn     15         2    
bm1-3   666        64000     100.64.10.201                    established     6h18m47s   l2vpn/evpn     15         2    
        666        64000     100.64.10.202                    established     6h18m52s   l2vpn/evpn     15         2    
```

[[Back]](./README.md) [[Next]](./kube-baseline.md)