# Metal Kubed - Power on

[[Back]](../README.md) [[iserver-way]](../power_on.md)

`BareMetalHost` resource exposes `spec.online` boolean property to control the power on/off desired state of the node. This property can be used with BareMetalHosts in Provisioned, ExternallyProvisioned or Available states that require proper [registration](./register.md).

## Example

```
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: example
spec:
  online: true
```

```
# oc patch bmh -n openshift-machine-api bm1-1 --type merge -p '{"spec": {"online": true}}'
baremetalhost.metal3.io/bm1-1 patched
```


[[Back]](../README.md) [[iserver-way]](../power_on.md)