# Metal Kubed - Reboot

[[Back]](../README.md) [[iserver-way]](../reboot.md)

The reboot annotation can be used for rebooting BareMetalHosts in the provisioned state. Refere to [official documentation](https://book.metal3.io/bmo/reboot_annotation.html) for details.

## Example

> [!NOTE]
> The controller will remove the annotation as soon as it has restored power to the host.

```
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: example
  annotations:
    reboot.metal3.io: ""
```

```
$ oc annotate bmh -n openshift-machine-api bm1-1 reboot.metal3.io=''
baremetalhost.metal3.io/bm1-1 annotated
```

[[Back]](../README.md) [[iserver-way]](../reboot.md)