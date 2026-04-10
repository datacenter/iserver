# MetalLB - Instance bgpBackend undefined

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)

> [!NOTE]
> OCP4.21.4 with OVNKubernetes CNI

```
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
```

Observations
- [ovn-bgp](../../ovn-bgp/README.md) automatically enabled i.e., `openshift-frr-k8s` created, `frr-k8s` enabled, frr deployed
  - if ovn-bgp is pre-enabled, then things are still working fine
- metallb speaker pods **without** frr
- [BGPPeer](./bgp_peer.md) generates per-host `FRRConfiguration` objects
- standalone `FRRConfiguration` objects supported and configure frr instance
- proper metallb + ovn-bgp integrated mode

```
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  namespace: metallb-system
  name: leaf1
spec:
  peerAddress: 6.6.6.6
  peerASN: 64600
  myASN: 64667
  ebgpMultiHop: true
```

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: another-session2
  namespace: openshift-frr-k8s
  labels:
    fabric: nxos
spec:
  bgp:
    routers:
    - asn: 64667
      neighbors:
      - address: 8.8.8.8
        asn: 64669
```

```
$ oc get frrconfigurations.frrk8s.metallb.io -A
NAMESPACE           NAME               AGE
openshift-frr-k8s   another-session2   3m9s
openshift-frr-k8s   metallb-bm1-1      9m11s
openshift-frr-k8s   metallb-bm1-2      9m11s
openshift-frr-k8s   metallb-bm1-3      9m11s
```

```
# iserver get ocp ovn-bgp       

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+------------------+---------------+---------------------------+----------------------+---------------------------------+
| ID | Network Operator | CNI           | Condition                 | CIDR                 | Settings                        |
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+
| 1  | cluster 4.21.4   | OVNKubernetes | ✓ Available               | Pod 10.128.0.0/14/23 | deployKubeProxy:False           |
|    |                  |               | ✗ Degraded                | Svc 172.30.0.0/16    | disableMultiNetwork:False       |
|    |                  |               | ✗ ManagementStateDegraded |                      | disableNetworkDiagnostics:False |
|    |                  |               | ✗ Progressing             |                      | logLevel:Normal                 |
|    |                  |               | ✓ Upgradeable             |                      | managementState:Managed         |
|    |                  |               |                           |                      | operatorLogLevel:Normal         |
|    |                  |               |                           |                      | ---                             |
|    |                  |               |                           |                      | frr-k8s                         |
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+

Feature
- frr-k8s:  enabled
- route advertisement: disabled
Configuration
- frr: 4 incl. 0 ra-generated
- node bm1-1: converted, reloaded
- node bm1-2: converted, reloaded
- node bm1-3: converted, reloaded
BGP sessions
- configured nodes: 3/3
- bm1-1: 1/2
- bm1-2: 1/2
- bm1-3: 1/2
```

```
# iserver get ocp ovn-bgp --node bm1-1 --cmd "show run" -v exec

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-mqbb8 [bm1-1]
-------------------------
Building configuration...

Current configuration:
!
frr version 8.5.3
frr defaults traditional
hostname bm1-1
log file /etc/frr/frr.log informational
log timestamp precision 3
no ip forwarding
no ipv6 forwarding
service integrated-vtysh-config
!
router bgp 64667
 no bgp ebgp-requires-policy
 no bgp default ipv4-unicast
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 ebgp-multihop
 neighbor 8.8.8.8 remote-as 64669
 !
 address-family ipv4 unicast
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-in in
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
  neighbor 8.8.8.8 activate
  neighbor 8.8.8.8 route-map 8.8.8.8-in in
  neighbor 8.8.8.8 route-map 8.8.8.8-out out
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 deny any
ip prefix-list 6.6.6.6-inpl-ipv4 seq 1 deny any
ip prefix-list 8.8.8.8-allowed-ipv4 seq 1 deny any
ip prefix-list 8.8.8.8-inpl-ipv4 seq 1 deny any
!
ipv6 prefix-list 6.6.6.6-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 6.6.6.6-inpl-ipv4 seq 2 deny any
ipv6 prefix-list 8.8.8.8-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 8.8.8.8-inpl-ipv4 seq 2 deny any
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-allowed-ipv4
exit
!
route-map 6.6.6.6-out permit 2
 match ipv6 address prefix-list 6.6.6.6-allowed-ipv6
exit
!
route-map 6.6.6.6-in permit 3
 match ip address prefix-list 6.6.6.6-inpl-ipv4
exit
!
route-map 6.6.6.6-in permit 4
 match ipv6 address prefix-list 6.6.6.6-inpl-ipv4
exit
!
route-map 8.8.8.8-out permit 1
 match ip address prefix-list 8.8.8.8-allowed-ipv4
exit
!
route-map 8.8.8.8-out permit 2
 match ipv6 address prefix-list 8.8.8.8-allowed-ipv6
exit
!
route-map 8.8.8.8-in permit 3
 match ip address prefix-list 8.8.8.8-inpl-ipv4
exit
!
route-map 8.8.8.8-in permit 4
 match ipv6 address prefix-list 8.8.8.8-inpl-ipv4
exit
!
ip nht resolve-via-default
!
ipv6 nht resolve-via-default
!
end
```

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)