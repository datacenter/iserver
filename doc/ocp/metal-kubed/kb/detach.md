# Metal Kubed - Detaching hosts from provisioner

[[Back]](../README.md) [[iserver-way]](../detach.md)

The detached annotation provides a way to prevent management of a `BareMetalHost`. It works by deleting the host information from Ironic without triggering deprovisioning. The BareMetal Operator will recreate the host in Ironic again once the annotation is removed. This annotation can be used with BareMetalHosts in Provisioned, ExternallyProvisioned or Available states. 

Refer to details in [official documentation](https://book.metal3.io/bmo/detached_annotation.html#detaching-hosts-from-provisioner).

## How to attach again

If you want to attach a previously detached host, remove the annotation and wait for the operationalStatus field to become OK.

## Example

> [!NOTE]
> The annotation key is `baremetalhost.metal3.io/detached` and the value can be anything (it is ignored). 

```
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: example
  annotations:
    baremetalhost.metal3.io/detached: ""
spec:
  online: true
  bootMACAddress: 00:8a:b6:8e:ac:b8
  bootMode: legacy
  bmc:
    address: ipmi://192.168.111.1:6230
    credentialsName: example-bmc-secret
```

[[Back]](../README.md) [[iserver-way]](../detach.md)