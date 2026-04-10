# MetalLB - BFD profile

[[Back]](../README.md) [[iserver-way]](../create_bfd.md)

To enable rapid detection of communication failures between routing peers, configure the properties of the MetalLB `BFDProfile` custom resource (CR). 

## Spec

Refer to [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html-single/ingress_and_load_balancing/index#metallb-configure-bfd-profiles) for complete spec.

> [!CAUTION]
> BFDProfile spec parameters are case-sensitive and unknown silently ignored

Parameter | Type | Description
--- | --- | ---
detectMultiplier | int | def. 3
echoMode | bool | def. false
echoInterval | int | def. 50
minimumTtl | int | def. 254
passiveMode | bool | def. false
receiveInterval | int | def. 300
transmitInterval | int | def. 300

## CRD Example

```
apiVersion: metallb.io/v1beta1
kind: BFDProfile
metadata:
  name: profile1
  namespace: metallb-system
spec:
  detectMultiplier: 5
  echoInterval: 100
  echoMode: true
  minimumTtl: 100
  passiveMode: true
  receiveInterval: 500
  transmitInterval: 500
```

## Triggered configration

```
bfd
 profile profile1
  detect-multiplier 5
  transmit-interval 500
  receive-interval 500
  passive-mode
  echo-mode
  echo transmit-interval 100
  echo receive-interval 100
  minimum-ttl 100
 exit
```

[[Back]](../README.md) [[iserver-way]](../create_bfd.md)