# Egress Gateway

```
enterprise:
  featureGate:
    approved:
    - EgressGatewayIPv4

bpf:
  masquerade: true

egressGateway:
  enabled: true

kubeProxyReplacement: true
```

Source: https://docs.cilium.io/en/stable/network/egress-gateway/egress-gateway/

Rollout restart of operator and agent required
- did not check only operator or only agent
- not sure if this is mandatory

## Egress Gateway HA

```
  enterprise:
    featureGate:
      approved:
      - EgressGatewayHA
    egressGatewayHA:
      enabled: true
```

Source: https://docs.isovalent.com/configuration-guide/networking/egress-gateway/introduction.html#


# Hubble 

1.17 (Clife)

```
    hubble:
      enabled: true
      metrics:
        enabled:
        - dns:labelsContext=source_namespace,destination_namespace
        - drop:labelsContext=source_namespace,destination_namespace
        - tcp:labelsContext=source_namespace,destination_namespace
        - port-distribution:labelsContext=source_namespace,destination_namespace
        - icmp:labelsContext=source_namespace,destination_namespace;sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity
        - flow:sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity;labelsContext=source_namespace,destination_namespace
        - httpV2:exemplars=true;labelsContext=source_ip,source_namespace,source_workload,destination_ip,destination_namespace,destination_workload,traffic_direction;sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity
        - policy:sourceContext=app|workload-name|pod|reserved-identity;destinationContext=app|workload-name|pod|dns|reserved-identity;labelsContext=source_namespace,destination_namespace
        - flow_export
```

```
$ helm repo add isovalent https://helm.isovalent.com
"isovalent" has been added to your repositories

$ helm upgrade hubble-ui isovalent/hubble-ui --install --version 1.3.7 --namespace cilium --set relay.address="hubble-relay.cilium.svc.cluster.local" --wait
Release "hubble-ui" does not exist. Installing it now.
NAME: hubble-ui
LAST DEPLOYED: Wed Sep 17 07:08:58 2025
NAMESPACE: cilium
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
You have successfully installed Hubble-Ui.
Your release version is 1.3.7.
```

```
$ cilium status -n cilium
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 3, Ready: 3/3, Available: 3/3
DaemonSet              cilium-envoy             Desired: 3, Ready: 3/3, Available: 3/3
Deployment             cilium-operator          Desired: 2, Ready: 2/2, Available: 2/2
Deployment             hubble-ui                Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 3
                       cilium-envoy             Running: 3
                       cilium-operator          Running: 2
                       clustermesh-apiserver
                       hubble-relay
                       hubble-ui                Running: 1
```

Then use

```
cilium --kubeconfig C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig -n cilium hubble ui
```