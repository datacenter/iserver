# Host provisioning

[[Back]](../README.md)

The most fundamental feature of Metal3 Bare Metal Operator is provisioning of bare-metal machines with a user-provided image a.k.a. **OS installation**

Provisioning workflow requires the host to be in [available](./available.md) state which means that
- host is already [registered](./register.md) with `soec:bmc` defining redfish details incl. address, credentials stored in `Secret` object and ssl verification flag
- [hardware inspection](./inspect.md) completes following `spec:preprovisioningNetworkDataName` reference to `Secret` object with networking configuration ([details](./provisiong_preprovisioning_network_data.md))

The minimum trigger for provisioning is `spec:image` definition with url, checksum and format. However, in practice you also need to define
- `spec:rootDeviceHints` that defines (hints) target storage device e.g., using disk serial number ([details](./provisioning_device_hints.md))
- `spec:networkData` reference to `Secret` object that defines the desired networking layout ([details](./provisioning_network_data.md))
- `spec:userData` reference to `Secret` object that defines `cloud-config` type of information with e.g., user credentials ([details](./provisioning_user_data.md))
- `spec:bootMode` to control UEFI or non-UEFI boot mode
- `spec:bootMACAddress` that defines your main interface mac address from installed OS point of view i.e. it is **not** imc/management mac address

In case of problems, refer to [troubleshooting hints](./provisioning_troubleshooting.md).

>[!CAUTION]
>When host reaches `provisioned` state, it may still not be ip reachable. Consider boot and OS initialization extra time that is **not** exposed in bare metal host state.

[[Back]](../README.md)