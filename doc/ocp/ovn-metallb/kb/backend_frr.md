# MetalLB - Instance bgpBackend frr

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)

> [!NOTE]
> OCP4.21.4 with OVNKubernetes CNI

```
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  bgpBackend: frr
```

Observations
- [ovn-bgp](../../ovn-bgp/README.md) **not enabled automatically**
- metallb speaker pods **with** frr
- [BGPPeer](./bgp_peer.md) configures generates per-host `FRRConfiguration` objects
- standalone `FRRConfiguration` objects effectively **unsupported** since do not change speaker's frr instance configuration
- not the right mode if you want ovn-bgp

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
  namespace: metallb-system
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
NAMESPACE        NAME               AGE
metallb-system   another-session2   12s
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
+----+------------------+---------------+---------------------------+----------------------+---------------------------------+

Feature
- frr-k8s: disabled
- route advertisement: disabled
```

```
# iserver get ocp metallb --cluster bm1 -v exec --cmd "show run" --node bm1-1

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1
Operator metallb-operator found
Metallb instance in l3 mode with bgpBackend [frr]

FRR speaker-jvs9f [bm1-1]
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
 no bgp hard-administrative-reset
 no bgp default ipv4-unicast
 no bgp graceful-restart notification
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 ebgp-multihop
 !
 address-family ipv4 unicast
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-in in
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 deny any
!
ipv6 prefix-list 6.6.6.6-allowed-ipv6 seq 1 deny any
!
route-map 6.6.6.6-in deny 20
exit
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-allowed-ipv4
exit
!
route-map 6.6.6.6-out permit 2
 match ipv6 address prefix-list 6.6.6.6-allowed-ipv6
exit
!
ip nht resolve-via-default
!
ipv6 nht resolve-via-default
!
end
```

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)