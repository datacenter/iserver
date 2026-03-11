# HTPasswd Identity Provider - Set

[[Back]](./README.md) [[Prev]](./get.md) [[Next]](./create_task.md)

## Workflow

- add htpasswd identity provider in `OAuth` 'cluster' if not already defined
- get all users defined in input parameters i.e. htpasswd file and user:pass entries
- (patch mode) add-or-replace users in `Secret` object
- (post mode) overwrite `Secret` object with user credentials
- add selected users to cluster-admin group using `ClusterRoleBinding`

## Configurable options

```
# iserver delete ocp htpasswd
  --cluster TEXT       Cluster Name
  --provider TEXT      HTPasswd Provider Name
  --filename TEXT      htpasswd filename
  --user TEXT          User:pass entries
  --admin TEXT         Admin users
  --mode [post|patch]  Mode of operation  [default: patch]
```

Notes:
- option --user and --filename can be defined multiple times and be combined
- --admin option elevate selected customers to admin role in single workflow run

## Use cases

Intent | Example
--- | --- 
Add new provider | [Link](./add_new_provider.md)
Add user to existing provider | [Link](./add_new_user.md)
Grant admin role to user | [Link](./add_admin.md)
Update user | [Link](./update_user.md)

[[Back]](./README.md) [[Prev]](./get.md) [[Next]](./create_task.md)