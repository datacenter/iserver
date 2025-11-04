# HTPasswd Identity Provider - Set

## Workflow

- check api access to openshift cluster
- check if provider name exists (OAuth CRD), if not then create one
- get all users defined in input parameters i.e. htpasswd file and user:pass entries
- in case of patch mode, add users and if user already exists, update the password (Secret CRD)
- in case of post mode, replace users (Secret CRD)
- add selected users to admin group (ClusterRoleBinding CRD)

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

## Example: Add new identity provider

Notes:
- multiple users can be defined
- use --filename [filename] parameter if users are already defined in htpasswd file
- options --filename and --user can be combined
- use --admin option to elevate selected customers to admin role in single workflow run

```
# iserver set ocp htpasswd --cluster bm1 --provider new123 --user hhh:passhhh --filename C:\tmp\new-htpasswd.txt            

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

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================


OAuth updated with htpasswd [new123]
Secret openshift-config/new123 created

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================



+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) | 
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | ggg          |
|         |          |        |           | hhh          |
+---------+----------+--------+-----------+--------------+
```

## Example: Add new user

Notes:
- multiple users can be defined
- use --filename [filename] parameter if users are already defined in htpasswd file
- options --filename and --user can be combined
- use --admin option to elevate selected customers to admin role in single workflow run

```
# iserver set ocp htpasswd --cluster bm1 --provider new123 --user aaa:bbb --user xxx:yyy --admin aaa
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
|         |          |        |           | hhh          |
+---------+----------+--------+-----------+--------------+

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================


Secret openshift-config/new123 updated
Add username aaa to cluster admins group

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================



+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | aaa (admin)  |
|         |          |        |           | ggg          |
|         |          |        |           | hhh          |
|         |          |        |           | xxx          |
+---------+----------+--------+-----------+--------------+
```

## Example: Add existing user to admin group

Notes:
- option --admin can be used several times

```
# iserver set ocp htpasswd --cluster bm1 --provider new123 --admin ggg   
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
| cluster | new123   | new123 | True      | aaa (admin)  |
|         |          |        |           | ggg          |
|         |          |        |           | hhh          |
|         |          |        |           | xxx          |
+---------+----------+--------+-----------+--------------+

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================


Add username ggg to cluster admins group

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================



+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | aaa (admin)  |
|         |          |        |           | ggg (admin)  |
|         |          |        |           | hhh          |
|         |          |        |           | xxx          |
+---------+----------+--------+-----------+--------------+
```

## Example: Replace users

```
# iserver set ocp htpasswd --cluster bm1 --provider new123 --mode post --filename C:\tmp\new-htpasswd.txt  

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
| cluster | new123   | new123 | True      | aaa (admin)  |
|         |          |        |           | ggg (admin)  |
|         |          |        |           | hhh          |
|         |          |        |           | xxx          |
+---------+----------+--------+-----------+--------------+

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================


Secret openshift-config/new123 updated
Deleting user [hhh] and identity [new123:hhh]
User already deleted, checking for identity leftover
Deleting user [aaa] and identity [new123:aaa]
User already deleted, checking for identity leftover
Deleting user [xxx] and identity [new123:xxx]
User already deleted, checking for identity leftover

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================



+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
| cluster | new123   | new123 | True      | ggg (admin)  |
+---------+----------+--------+-----------+--------------+
```

[[Back]](./README.md)