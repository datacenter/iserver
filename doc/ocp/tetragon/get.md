# Tetragon Operator - Get 

[[Back]](./README.md)

## Workflow

- get tetragon operator subscription
- get tetragon crds

## Requirements

None

## Configurable options

```
# iserver get ocp tetragon
  --cluster TEXT   Cluster Name
  --verbose        Verbose output
  -v, --view TEXT  [state|res|all]  [default: state]
```

## Example (view:state)

```
# iserver get ocp tetragon --cluster bm1

OpenShift Workflow - Tetragon - Get Information
===============================================

OpenShift Cluster: bm1

Collecting state...

Operator
- subscription          : tetragon/tetragon-operator
- package               : tetragon/tetragon-catalog/tetragon-operator
- channel               : v1.18
- install plan          : tetragon/install-bkpn6
- install plan approved : V
- installed csv         : tetragon-operator.v1.18.2
- latest_csv            : V


Tetragon resources
- AlertRule: 0
- SandboxPolicy: 0
- SandboxPolicyNamespaced: 0
- TracingPolicy: 0
- TracingPolicyNamespaced: 0

View: state (def), res, all
```

[[Back]](./README.md)