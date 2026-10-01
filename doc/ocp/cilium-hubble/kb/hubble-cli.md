# Hubble CLI

[[Back]](../README.md)

## Table of contents

- [hubble relay](#hubble-relay)
- [hubble timescape without tls](#hubble-timescape-without-tls)
- [hubble timescape with tls](#hubble-timescape-with-tls)

## hubble relay

Requirements
- [hubble client](../../cli/create_hubble.md)
- hubble relay [with](./configuration-hubble-relay-tls.md) or [without](./configuration-hubble-relay-no-tls.md) TLS

Port forwarding must be enabled

```
$ oc -n cilium port-forward service/hubble-relay 4245:80
Forwarding from 127.0.0.1:4245 -> 4245
Forwarding from [::1]:4245 -> 4245
```

```
$ hubble status
Healthcheck (via localhost:4245): Ok
Current/Max Flows: 12,285/12,285 (100.00%)
Flows/s: 393.54
Connected Nodes: 3/3
```

```
$ hubble observe
Jun 23 12:01:41.446: openshift-controller-manager/controller-manager-5dfdff7874-9h7cq:54514 (ID:51318) -> 10.10.10.65:6443 (host) to-stack FORWARDED (TCP Flags: ACK)
```

## hubble timescape without tls

Requirements
- [hubble client](../../cli/create_hubble.md)
- [hubble timescape](./configuration-hubble-timescape-no-tls.md)

Port forwarding must be enabled

```
$ kubectl port-forward -n cilium svc/hubble-timescape 4245:80
Forwarding from 127.0.0.1:4245 -> 4244
Forwarding from [::1]:4245 -> 4244
Handling connection for 4245
```

```
$ hubble status
Healthcheck (via localhost:4245): Ok
Current/Max Flows: 596,411/596,411 (100.00%)
Flows/s: 53.42
```

```
$ hubble observe 
Jul  1 07:10:56.671: openshift-apiserver/apiserver-77b7fc74cb-htkw7:45726 (ID:818) -> 10.10.10.66:2379 (kube-apiserver) to-stack FORWARDED (TCP Flags: RST)
```

## hubble timescape with tls

Requirements
- [hubble client](../../cli/create_hubble.md)
- [hubble timescape](./configuration-hubble-timescape-tls.md)

Port forwarding must be enabled

```
$ kubectl port-forward -n cilium svc/hubble-timescape 4245:443
Forwarding from 127.0.0.1:4245 -> 4244
Forwarding from [::1]:4245 -> 4244
```

```
$ hubble status --tls-allow-insecure --server tls://localhost:4245
Healthcheck (via localhost:4245): Ok
Current/Max Flows: 115,969/115,969 (100.00%)
Flows/s: 52.37
```

```
$ hubble observe --tls-allow-insecure --server tls://localhost:4245
Jul  1 08:06:33.140: 10.128.1.92:44772 (remote-node) -> openshift-cnv/virt-api-776df55bf6-lv9gr:8443 (ID:6625) to-endpoint FORWARDED (TCP Flags: ACK, RST)
```

[[Back]](../README.md)