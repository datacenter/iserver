# Reprovisioning

[[Back]](../README.md)

Use case: host is already [provisioned](./provisioned.md) and you want to install new operating system or reinstall the host with changed [network](./provisioning_network_data.md) or [user](./provisioning_user_data.md) data
- If the URL of the image changes, the re-provisioning process will start automatically. Make sure to update the user and network data in the same or earlier edit operation.
- If the URL of the image is the same, you need to remove the image field, then add it back once the state of the BareMetalHost changes to deprovisioning.

>[!CAUTION]
>updating the userData and networkData fields alone does not trigger a new provisioning.

[[Back]](../README.md)