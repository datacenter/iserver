# OpenShift Operations

## HTPasswd Identity Provider

HTPasswd Identity Provider Configure allow users to log in to OpenShift Container Platform with credentials from an htpasswd file.

Refer to officlal [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/authentication_and_authorization/configuring-identity-providers#identity-provider-htpasswd-CR_configuring-htpasswd-identity-provider) for details.

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

## Get HTPasswd Identity Providers

```
# iserver get ocp htpasswd --cluster my-cluster

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user3         |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
```

## Add user to admin group

Notes:
- option --admin can be used several times

```
# iserver set ocp htpasswd --cluster my-cluster --provider my_test_provider --admin user3

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user3         |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+

Add username user3 to cluster admins group

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user3 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
```

## Remove user from admin group

Notes:
- option --admin can be used several times

```
# iserver set ocp htpasswd --cluster my-cluster --provider my_test_provider --admin user3 --mode delete

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user3 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+

Removing user [user3] from cluster-admin group

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user3         |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
```

## Add user to existing provider

Notes:
- multiple users can be defined
- use --htpasswd [filename] parameter if users are already defined in htpasswd file
- options --htpasswd and --user can be combined
- use --admin option to elevate selected customers to admin role in single workflow run

```
# iserver set ocp htpasswd --cluster my-cluster --provider my_test_provider --user user2:pass123 --admin user2

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user3         |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+

Secret openshift-config/my-test-provider updated
Add username user2 to cluster admins group

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user2 (admin) |
|         |                   |                   |           | user3         |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
```

## Remove identity provider

Note:
- including associated users and admin roles

```
# iserver set ocp htpasswd --cluster my-cluster --provider my_test_provider --mode delete

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test_provider  | my-test-provider  | True      | user2 (admin) |
|         |                   |                   |           | user3         |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+

Deleting user [user2] and identity [my_test_provider:user2]
User already deleted, checking for identity leftover
Deleting user [user2] from cluster-admin group
Deleting user [user3] and identity [my_test_provider:user3]
Deleting user [user3] from cluster-admin group
Deleting secret [openshift-config/my-test-provider]
Deleting htpasswd identity provider [my_test_provider]

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+
```

## Replace identity provider with new users

```
# cat /tmp/htpasswd
user66:$2y$05$...
user67:$2y$36$...

# iserver set ocp htpasswd --cluster my-cluster --provider my_test2_provider --htpasswd /tmp/htpasswd.txt --mode post --admin user66

+---------+-------------------+-------------------+-----------+---------------+
| OAuth   | Name              | Secret            | Is Secret | User          |
+---------+-------------------+-------------------+-----------+---------------+
| cluster | my_test2_provider | my-test2-provider | True      | user1 (admin) |
+---------+-------------------+-------------------+-----------+---------------+

Secret openshift-config/my-test2-provider updated
Deleting user [user1] and identity [my_test2_provider:user1]
User already deleted, checking for identity leftover
Add username user66 to cluster admins group

OAuth HTPasswd [#1]
-------------------

+---------+-------------------+-------------------+-----------+----------------+
| OAuth   | Name              | Secret            | Is Secret | User           |
+---------+-------------------+-------------------+-----------+----------------+
| cluster | my_test2_provider | my-test2-provider | True      | user66 (admin) |
|         |                   |                   |           | user67         |
+---------+-------------------+-------------------+-----------+----------------+
```