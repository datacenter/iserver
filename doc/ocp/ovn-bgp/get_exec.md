# OVNKubernetes BGP - Get FRR cli command output

[[Back]](./README.md)

```
# iserver get ocp ovn-bgp --cluster bm1 -v exec --cmd "show bgp nei"

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-9ckzb [bm1-2]
-------------------------
BGP neighbor is 6.6.6.6, remote AS 64600, local AS 64667, external link
  Local Role: undefined
  Remote Role: undefined
  BGP version 4, remote router ID 6.6.6.6, local router ID 66.66.66.11
  BGP state = Established, up for 4d12h27m
  ...

FRR frr-k8s-c4jk4 [bm1-1]
-------------------------
BGP neighbor is 6.6.6.6, remote AS 64600, local AS 64667, external link
  Local Role: undefined
  Remote Role: undefined
  BGP version 4, remote router ID 6.6.6.6, local router ID 66.66.66.10
  BGP state = Established, up for 4d12h16m
  ...

FRR frr-k8s-zpxj6 [bm1-3]
-------------------------
BGP neighbor is 6.6.6.6, remote AS 64600, local AS 64667, external link
  Local Role: undefined
  Remote Role: undefined
  BGP version 4, remote router ID 6.6.6.6, local router ID 66.66.66.12
  BGP state = Established, up for 4d12h27m
```

[[Back]](./README.md)