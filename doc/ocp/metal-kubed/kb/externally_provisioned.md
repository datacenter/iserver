# Externally provisioned host

[[Back]](../README.md)

BareMetal Operator allows enrolling hosts that have been not been provisioned by Metal Kubed e.g., 
- OpenShift cluster nodes installed using Assisted Installer method
- External hosts defined with `spec.externallyProvisioned` field to `true`

Once the bmc details are defined and the server is successfully registered, its status changes from initial `unmanaged` to `externally provisioned` that enables cluster's Metal3/Ironic components for identity and power management **only**.

Limited set of actions is possible on externally provisioned hosts:
- Powering [on](./power_on.md) and [off](./power_off.md) using the online field
- Rebooting using the [reboot annotation](./reboot.md)
- Live updates (servicing)
- Deletion without cleaning i.e. the host is only powered off

Inventory information is **not collected**. 

Refer to details in [official documentation](https://book.metal3.io/bmo/externally_provisioned.html).

> [!NOTE]
> `spec.externallyProvisioned` defaults to `false` and cannot be changed

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-bmc-secret
  namespace: openshift-machine-api
  labels:
    environment.metal3.io: baremetal
type: Opaque
data:
  username: YWRtaW4=
  password: cGFzc3dvcmQ=
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: test
  namespace: openshift-machine-api
spec:
  online: true
  externallyProvisioned: true
  bmc:
    address: redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAA
    credentialsName: test-bmc-secret
    disableCertificateVerification: true
```

![ExternallyProvisioned](../../images/metal-kubed/externally-provisioned.png)

When `BareMetalHost` is created, the host is powered on. When object is deleted, the host is powered off via Redfish and object deletion wait until host is down.

```
$ oc -n openshift-machine-api get events 
Registered           baremetalhost/test   Registered new host
ProfileSet           baremetalhost/test   Hardware profile set: unknown
BMCAccessValidated   baremetalhost/test   Verified access to BMC
PowerOn              baremetalhost/test   Host powered on
...
BMCAccessValidated   baremetalhost/test   Verified access to BMC
PowerOff             baremetalhost/test   Host powered off
```
[[Back]](../README.md)