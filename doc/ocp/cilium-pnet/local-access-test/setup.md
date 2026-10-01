# Private Network - local access connectivity test

[[Back]](./README.md) [[Next]](./namespace.md)

## Cilium configuration

```shell
iserver set ocp cilium pnet --mode feature --pnet local-access
iserver set ocp cilium pnet --mode multus
```

```yaml
enterprise:
  privateNetworks:
    enabled: true
    mode: local-access
    networkAttachmentDefinitions:
      enabled: true
```

Notes:
- **`local-access`** mode -- Uses dedicated local network devices (VLAN or physical interfaces) on Kubernetes nodes for private network traffic
- **`networkAttachmentDefinitions`** must be enabled for secondary interfaces into private network

## Check

```
# iserver get ocp cilium pnet              

OpenShift Workflow - Isovalent Private Network - Get Information
================================================================

OpenShift Cluster: bm1
Cilium cni found


Isovalent Private Network State
-------------------------------
- enabled : ✓
- multus  : ✓
- webhook : ✗
- crds    : ✓
- ready   : ✓



Private Network Custom Resources
--------------------------------
- clusterwide private network : 0
- endpoint slice              : 0
- external endpoint           : 0
- node attachment             : 0



Cilium Agent Database
---------------------
- network  : 0
- subnet   : 0
- route    : 0
- inb      : 0
- endpoint : 0
- map      : 0

View: state (def), res, webhook, db, ep, all
```

[[Back]](./README.md) [[Next]](./namespace.md)