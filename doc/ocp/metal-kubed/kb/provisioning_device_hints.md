## Provisioning - specifying root device

[[Back]](./provisioned.md)

Bare-metal machines often have more than one block device, and in many cases a user will want to specify, which of them to use as the root device. Root device hints allow selecting one device or a group of devices to choose from. You can provide the hints via the `spec.rootDeviceHints` field on your `BareMetalHost` object definition. Check further details on official [documentation](https://book.metal3.io/bmo/root_device_hints.html)

>[!NOTE]
>Using by-path identifiers (which depend on PCI/ATA bus ordering) are more fragile in general and may even change across reloads. One recommendation is using the disk's **serial number** instead, which isn't affected by this.

Example

```yaml
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: test
  namespace: openshift-machine-api
spec:
  online: true
  preprovisioningNetworkDataName: test-network
  bootMACAddress: aa:aa:aa:aa:aa:aa
  bootMode: UEFI
  networkData:
    name: test-networkdata
  userData:
    name: test-userdata
  bmc:
    address: redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAA
    credentialsName: test-bmc-secret
    disableCertificateVerification: true
  image:
    url: http://20.20.20.20/rhel-9.8-x86_64-kvm.qcow2
    checksum: b99091f1b4489111004d449398d9cc6aa024cb48b02c72fa99e6ca1fc48a7e4e
    checksumType: sha256
  rootDeviceHints:
    serialNumber: 123456
```

[[Back]](./provisioned.md)