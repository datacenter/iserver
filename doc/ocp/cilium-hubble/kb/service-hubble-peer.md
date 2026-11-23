## hubble peer

[[Back]](../README.md)

- Implements gRPC peer service used by Hubble relay to discover peer Hubble servers.
- Used by Hubble relay to discover avalible Hubble servers in the cluster
- enabled with `spec:hubble:enabled = True`

```
$ oc get service -n cilium
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
hubble-peer       ClusterIP   172.30.77.238    <none>        443/TCP    245d
```

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    meta.helm.sh/release-name: cilium-release
    meta.helm.sh/release-namespace: cilium
  creationTimestamp: "2025-10-20T17:45:37Z"
  labels:
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hubble-peer
    app.kubernetes.io/part-of: cilium
    app.kubernetes.io/version: 1.19.0
    isovalent.io/managed-by: clife
    k8s-app: cilium
  name: hubble-peer
  namespace: cilium
  ownerReferences:
  - apiVersion: cilium.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: CiliumConfig
    name: ciliumconfig
    uid: 23c5b57e-6fa3-429c-a86f-3e212122b307
  resourceVersion: "133679729"
  uid: 832ebb20-75e6-4c8e-9519-2e61b55fe9e7
spec:
  clusterIP: 172.30.77.238
  clusterIPs:
  - 172.30.77.238
  internalTrafficPolicy: Local
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - name: peer-service
    port: 443
    protocol: TCP
    targetPort: 4244
  selector:
    k8s-app: cilium
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

[[Back]](../README.md)