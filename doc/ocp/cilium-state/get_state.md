# Cilium - Get state

## Workflow

- check openshift network settings
- run 'cilium status' command on the [management node](../Access.md)

## Requirements

None

## Configurable options

```
# iserver get ocp cilium state
  --cluster TEXT   Cluster Name
```

## Example

```
# iserver get ocp cilium state --cluster bm1

OpenShift Workflow - Cilium - Get state
=======================================

OpenShift Cluster: bm1
Cilium cni found

OpenShift Network
-----------------
- Name            : cluster
- Network Type    : Cilium
- Cluster Network : 10.128.0.0/14
- Host Prefix     : 23
- Service Network : 172.30.0.0/16


    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet              cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment             cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 1
                       cilium-envoy             Running: 1
                       cilium-operator          Running: 1
                       clustermesh-apiserver
                       hubble-relay
Cluster Pods:          66/66 managed by Cilium
Image versions         cilium             ...
                       cilium-envoy       ...
                       cilium-operator    ...
```

[[Back]](./README.md)