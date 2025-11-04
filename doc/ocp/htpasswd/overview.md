# HTPasswd Identity Provider

## Overview

HTPasswd Identity Provider enables users to log in to OpenShift Container Platform with credentials from an htpasswd file.

Refer to official [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/authentication_and_authorization/configuring-identity-providers#identity-provider-htpasswd-CR_configuring-htpasswd-identity-provider) for details.

Defining new an htpasswd identity provider and users, requires the following tasks:
- Create an htpasswd file to store the user and password information.
- Create a secret to represent the htpasswd file.
- Define an htpasswd identity provider resource that references the secret.
- Apply the resource to the default OAuth configuration to add the identity provider.

In case of password change for a single user:
- Extract the htpasswd file content from secret
- Replace user password with new value
- Encode the htpasswd file
- Update the secret

In case of user delete:
- Extract the htpasswd file content from secret
- Remove the line with user password
- Encode the htpasswd file
- Update the secret
- Remove existing resources for each deleted user i.e. User and Identity CRD

If htpasswd identity provider should be deleted:
- Extract the htpasswd file content from secret
- Get the list of users
- Remove existing resources for each deleted user i.e. User and Identity CRD
- Delete secret
- Update OAuth configuration to remove the identity provider

Adding or removing user from admin group, requires ClusterRoleBinding CRD update.

iserver supports all workflows above with easy to use commands with flexbible options.

[[Back]](./README.md)