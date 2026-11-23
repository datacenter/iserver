# RunIt - Create cluster

[[Back]](../BareMetalCluster.md) [[Next]](./example_iso.md) [[Prev]](./example_console_body_generation.md)

Workflow
- send data to RedHat Console via API
- cluster definition
- infra (networking) definition
- in case of Cilium CNI, upload all Cilium manifests

## Cilium manifests fixup

- ipam section defines cluster pool cidr and mask and that must be aligned with the same settings defined on OpenShift level
- operator replicas is by default two and if you are installing single node openshift, it should be changed to one
- fixups can be disabled with `cilium:managed:false` in cluster.json

```
Cluster created: bm1 [AAAA]
Cluster install config cni patched: Cilium
Infra created: BBB
Manifest created: rbac.authorization.k8s.io_v1_clusterrolebinding_clife-metrics-auth-rolebinding.yaml
Manifest created: apiextensions.k8s.io_v1_customresourcedefinition_ciliumconfigs.cilium.io.yaml
Manifest created: apps_v1_deployment_clife-controller-manager.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-metrics-reader.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-ciliumconfig-admin-role.yaml
Manifest created: subscription.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-manager-role.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrolebinding_clife-manager-rolebinding.yaml
Manifest created: v1_namespace_cilium.yaml
Manifest created: rbac.authorization.k8s.io_v1_rolebinding_clife-leader-election-rolebinding.yaml
Manifest created: v1_serviceaccount_clife-controller-manager.yaml
Manifest created: v1_service_clife-metrics.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-metrics-auth-role.yaml
Manifest created: rbac.authorization.k8s.io_v1_role_clife-leader-election-role.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-ciliumconfig-viewer-role.yaml
Manifest created: ciliumconfig.yaml
Manifest created: operatorgroup.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-ciliumconfig-editor-role.yaml
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_iso.md) [[Prev]](./example_console_body_generation.md)