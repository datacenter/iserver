# Metal Kubed - Unmanaged host

[[Back]](../README.md)

An unmanaged host is missing both the BMC address and credentials secret name, and does not have any information to access the BMC for registration. The corresponding operational status is discovered.

> [!NOTE]
> OpenShift cluster installed using Assisted Installer method, all nodes have corresponding `BareMetalHost` object instance in unmanaged state.

![Example](../../images/metal-kubed/bmh.png)

## CRD

```
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: bm1-1
  namespace: openshift-machine-api
spec:
  externallyProvisioned: true
  bmc:
    address: ""
    credentialsName: ""
status:
  operationalStatus: discovered
  poweredOn: true
  provisioning:
    state: unmanaged
```

[[Back]](../README.md)