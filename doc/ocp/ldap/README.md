## LDAP Identity Provider

[[Back]](../Operations.md)

LDAP Identity Provider enables users to log in to OpenShift Container Platform with credentials stored in LDAP server.

Refer to official [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/authentication_and_authorization/configuring-identity-providers#configuring-ldap-identity-provider) for details.

Command | Intent | Details
--- | --- | ---
iserver get ocp ldap | check ldap identity providers | [Link](./get.md)
iserver set ocp ldap | configure ldap identity provider | [Link](./set.md)
iserver set ocp task | in task way | [provider](./create_task.md), [sync](./create_task_sync.md)
iserver delete ocp ldap | delete ldap identity provider | [Link](./delete.md)
iserver delete ocp task | in task way | [provider](./delete_task.md), [sync](./delete_task_sync.md)

## Extras

- [LDAP identity provider example](./example_idp.md)
- [LDAP group sync example](./example_sync.md)
- [LDAP group sync job example](./example_job.md)

[[Back]](../Operations.md)