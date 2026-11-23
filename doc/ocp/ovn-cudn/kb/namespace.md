# CUDN - Namespace selection

[[Back]](../README.md)

Cluster User Defined Network (CUDN) is cluster-scope object and at the same time it selects the namespaces by name or label where the cudn is operational.

Namespace selection considerations
- `default` and `openshift-*` namespaces should not be selected
- if `spec:namespaceSelector` is not configured, all namespaces are selected
- if the CUDN is configured with `role: Primary`, then selected namespaces **must** be defined with `k8s.ovn.org/primary-user-defined-network` label

## Primary cudn with namespace selected by name

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: a
  name: a1p
```

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: a1
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - a1p
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.66.0/24
    topology: Layer2
```

If namespace does not exist when cudn is created

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-07-05T16:50:53Z"
    message: 'NetworkAttachmentDefinition has been created in following namespaces:
      []'
    reason: NetworkAttachmentDefinitionCreated
    status: "True"
    type: NetworkCreated
```

As soon as namespace is created

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-07-05T16:50:53Z"
    message: 'NetworkAttachmentDefinition has been created in following namespaces:
      [a1p]'
    reason: NetworkAttachmentDefinitionCreated
    status: "True"
    type: NetworkCreated
  - lastTransitionTime: "2026-07-05T16:53:01Z"
    message: Network allocation succeeded for all synced nodes.
    reason: NetworkAllocationSucceeded
    status: "True"
    type: NetworkAllocationSucceeded
```

In case namepace is missing required annotation

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-07-05T16:54:35Z"
    message: 'invalid primary network state for namespace "a1p": a valid primary user
      defined network or network attachment definition custom resource, and required
      namespace label "k8s.ovn.org/primary-user-defined-network" must both be present'
    reason: NetworkAttachmentDefinitionSyncError
    status: "False"
    type: NetworkCreated
  - lastTransitionTime: "2026-07-05T16:53:01Z"
    message: Network allocation succeeded for all synced nodes.
    reason: NetworkAllocationSucceeded
    status: "True"
    type: NetworkAllocationSucceeded
```

## Secondary cudn with namespace selected by label

> [!CAUTION]
> matchLabels terms are evaluated with an **AND** relationship

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    tenant: a
  name: a1s
```

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: a1
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "a"
  network:
    layer2:
      role: Secondary
      subnets:
      - 66.66.66.0/24
    topology: Layer2
```

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-07-05T19:26:07Z"
    message: 'NetworkAttachmentDefinition has been created in following namespaces:
      [a1s]'
    reason: NetworkAttachmentDefinitionCreated
    status: "True"
    type: NetworkCreated
  - lastTransitionTime: "2026-07-05T19:26:07Z"
    message: Network allocation succeeded for all synced nodes.
    reason: NetworkAllocationSucceeded
    status: "True"
    type: NetworkAllocationSucceeded
```

if another namespace is added with label

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-07-05T19:26:07Z"
    message: 'NetworkAttachmentDefinition has been created in following namespaces:
      [a1s, a2s]'
    reason: NetworkAttachmentDefinitionCreated
    status: "True"
    type: NetworkCreated
  - lastTransitionTime: "2026-07-05T19:26:07Z"
    message: Network allocation succeeded for all synced nodes.
    reason: NetworkAllocationSucceeded
    status: "True"
    type: NetworkAllocationSucceeded
```

[[Back]](../README.md) 