# HTPasswd Identity Provider - Delete

[[Back]](./README.md) [[Prev]](./create_task.md) [[Next]](./delete_task.md)

## Workflow

- check api access to openshift cluster
- check if provider name exists (OAuth CRD)
- if users or admin users are not defined, then delete entire provider
- if admin users defined, then remove selected users from admin group (ClusterRoleBinding CRD)
- if users defined (htpasswd file or user), then delete selected users (Secret CRD)

## Requirements

None

## Configurable options

```
# iserver delete ocp htpasswd
  --cluster TEXT   Cluster Name
  --provider TEXT  HTPasswd Provider Name
  --filename TEXT  htpasswd filename
  --user TEXT      Usernames
  --admin TEXT     Admin users
  --help           Show this message
```

## Use cases

Intent | Example
--- | --- 
Delete admin role | [Link](./delete_admin.md)
Delete user | [Link](./delete_user.md)
Delete provider | [Link](./delete_provider.md)

[[Back]](./README.md) [[Prev]](./create_task.md) [[Next]](./delete_task.md)

## Example: Remove user from admin group

```
# iserver delete ocp htpasswd --cluster bm1 --provider new123 --admin ggg

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | ggg (admin)  |
+---------+----------+--------+-----------+--------------+

Removing user [ggg] from cluster-admin group

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================



+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | ggg          |
+---------+----------+--------+-----------+--------------+
```

## Example: Delete user

```
# iserver delete ocp htpasswd --cluster bm1 --provider new123 --user ggg    

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | ggg          |
+---------+----------+--------+-----------+--------------+

Deleting user [ggg] and identity [new123:ggg]
User already deleted, checking for identity leftover
Deleting user [ggg] from cluster-admin group
Deleting secret [openshift-config/new123]
Deleting htpasswd identity provider [new123]

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================



+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
```

## Example: Delete provider

```
# iserver delete ocp htpasswd --cluster bm1 --provider custom                 

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+

Deleting user [kali] and identity [custom:kali]
User already deleted, checking for identity leftover
Deleting user [kali] from cluster-admin group
Deleting secret [openshift-config/custom]
Deleting htpasswd identity provider [custom]

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================


Identity htpasswd not defined
```

[[Back]](./README.md) [[Prev]](./create_task.md) [[Next]](./delete_task.md)