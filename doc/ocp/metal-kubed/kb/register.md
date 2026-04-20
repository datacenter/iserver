# Metal Kubed - Node registration

[[Back]](../README.md)

In case of OpenShift cluster installed with assisted installer, all hosts are discovered as `BareMetalHost` object in [unmanaged](./unmanaged.md) operational state.

```
  operationalStatus: discovered
  poweredOn: true
  provisioning:
    state: unmanaged
```

Node registration procedure allows power management and requires providing BMC access details with the **hardware dependent address format** as explained [here](https://book.metal3.io/bmo/supported_hardware.html).

> [!CAUTION]
> in case of http proxy, make sure bmc address is in noProxy, otherwise the node may hang in registering phase for quite a while and eventually fail.

## Example Console

![Register](../images/metal-kubed/register.png)

## Example CRD

```
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: bm1-1
  namespace: openshift-machine-api
spec:
  bmc:
    address: redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAA
    credentialsName: bm1-1-bmc-secret
    disableCertificateVerification: true
```

where the credentialsName refers to `Secret` crd carrying base64-encoded Redfish authentication credentials

```
apiVersion: v1
kind: Secret
metadata:
  name: bm1-1-bmc-secret
  namespace: openshift-machine-api
  labels:
    environment.metal3.io: baremetal
type: Opaque
data:
  password: cGFzc3dvcmQ=
  username: YWRtaW4=
```

## State transition

Once bmc details are defined, the node changes to `registering` state

```
  provisioning:
    state: registering
```

and after a while it should transition to [externally provisioned](./externally_provisioned.md)

```
  provisioning:
    state: externally provisioned
```

[[Back]](../README.md)