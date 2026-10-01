# Configuration cheat sheet

[[Back]](../README.md)

Type | Details
--- | ---
[minimum](#minimum) | [Link](./configuration-hubble-minimum.md)
[hubble relay without tls](#hubble-relay-without-tls) | [Link](./configuration-hubble-relay-no-tls.md)
[hubble with tls](#hubble-relay-with-tls) | [Link](./configuration-hubble-relay-tls.md)
[timescape without tls](#timescape-without-tls) | [Link](./configuration-hubble-timescape-no-tls.md)
[timescape with tls](#timescape-with-tls) | [Link](./configuration-hubble-timescape-tls.md)

## Minimum

```yaml
spec:
  hubble:
    enabled: true
```

[Details](./configuration-hubble-minimum.md)

## Hubble relay without tls

```yaml
spec:
  hubble:
    enabled: true
    relay:
      enabled: true
    tls:
      enabled: false
```

[Details](./configuration-hubble-relay-no-tls.md)

## Hubble relay with tls

```yaml
spec:
  hubble:
    enabled: true
    relay:
      enabled: true
    tls:
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: ClusterIssuer
          name: cilium-root-ca
        certValidityDuration: 1
        enabled: true
        method: certmanager
      enabled: true
```

[Details](./configuration-hubble-relay-tls.md)

## Timescape without tls

```yaml
spec:
  enterprise:
    featureGate:
      approved:
      - HubbleTimescape
  hubble:
    enabled: true
    timescape:
      enabled: true
    tls:
      enabled: false
```

[Details](./configuration-hubble-timescape-no-tls.md)

## Timescape with tls

```yaml
spec:
  hubble:
    enabled: true
    timescape:
      enabled: true
    tls:
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: ClusterIssuer
          name: cilium-root-ca
        certValidityDuration: 1
        enabled: true
        method: certmanager
      enabled: true
```

[Details](./configuration-hubble-timescape-tls.md)

[[Back]](../README.md)