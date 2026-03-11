## HTPasswd Identity Provider

[[Back]](../Operations.md)

HTPasswd Identity Provider enables users to log in to OpenShift Container Platform with credentials from an htpasswd file.

Refer to official [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/authentication_and_authorization/configuring-identity-providers#identity-provider-htpasswd-CR_configuring-htpasswd-identity-provider) for details.

Command | Intent | Details
--- | --- | ---
iserver get ocp htpasswd | check htpasswd identity providers | [Link](./get.md)
iserver set ocp htpasswd | configure htpasswd identity provider | [Link](./set.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp htpasswd | delete htpasswd identity provider, user or admin-role | [Link](./delete.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Extras

- [CRD Example](./example_crd.md)

[[Back]](../Operations.md)