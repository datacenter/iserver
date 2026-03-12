# OpenShitf Authentication (OAuth) - Get

[[Back]](./README.md) [[Prev]](./log.md) [[Next]](./restart.md)

## Workflow

- get crd: `ClusterOperator`, `Authentication`, `OAuth`, `Group`, `User`
- get pods state in `openshift-authentication` and `openshift-authentication-operator` namespaces

## Requirements

None

## Configurable options

```
# iserver get ocp oauth
  --cluster TEXT   Cluster Name
  -v, --view TEXT  [state|verbose]  [default: state]
```

## Example (view:state)

```
# iserver get ocp oauth --cluster bm1

OpenShift Workflow - OAuth - Get Information
============================================

OpenShift Cluster: bm1


Cluster operator
----------------
- Cluster Operator : authentication
- Version          : 4.21.0
- Available        : V
- Progressing      : X
- Degraded         : X
- Upgradeable      : V



Authentication Operator
-----------------------
- Name             : cluster
- Log Level        : Normal
- Error Conditions : ---


Pod
---
- operator: 1/1
- authentication: 3/3

Authentication and Authorization
--------------------------------
- identity provider htpasswd [local-admins] with [2/3] active users
- identity provider ldap [ldap] with [0] active users
- users: 2
- group: 3 with 2 from ldap

Command hints
-------------
iserver get k8s pod --namespace openshift-authentication-operator -v logs
iserver get k8s pod --namespace openshift-authentication -v logs
iserver get ocp htpasswd
iserver get ocp ldap
iserver get k8s user
iserver get k8s group

View: state (def), verbose
```

## Example (view:verbose)

```
# iserver get ocp oauth --cluster bm1 -v verbose

OpenShift Workflow - OAuth - Get Information
============================================

OpenShift Cluster: bm1

+----+------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| ID | Cluster Operator | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since | Age |
+----+------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| 1  | authentication   | 4.21.0  | ClusterVersion | V         | X           | X        | V           | 1d    | 13d | 
|    |                  |         | version        |           |             |          |             |       |     | 
+----+------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+

+----+-------------------------+-----------+------------------+
| ID | Authentication Operator | Log Level | Error Conditions |
+----+-------------------------+-----------+------------------+
| 1  | cluster                 | Normal    | ---              | 
+----+-------------------------+-----------+------------------+

+----+-----------------------------------------+-------+---------+--------------------+---------+--------------+-----+------------+-----+
| ID | Pod                                     | Ready | Label   | Annotation         | Node    | IP           | Net | Restart    | Age |
+----+-----------------------------------------+-------+---------+--------------------+---------+--------------+-----+------------+-----+
| 1  | openshift-authentication-operator       | 1/1   | Running | Initialized: V     | bm1-3   | 10.128.1.20  | 1   | 4 (2d ago) | 13d | 
|    | authentication-operator-b95c6db64-k7cqq |       |         | PodScheduled: V    |         |              |     |            |     | 
|    |                                         |       |         | ContainersReady: V |         |              |     |            |     | 
|    |                                         |       |         | Ready: V           |         |              |     |            |     | 
+----+-----------------------------------------+-------+---------+--------------------+---------+--------------+-----+------------+-----+
| 2  | openshift-authentication                | 1/1   | Running | Initialized: V     | bm1-1   | 10.128.4.219 | 1   | 0          | 1d  | 
|    | oauth-openshift-55f74b6ccd-kqvrz        |       |         | PodScheduled: V    |         |              |     |            |     | 
|    |                                         |       |         | ContainersReady: V |         |              |     |            |     | 
|    |                                         |       |         | Ready: V           |         |              |     |            |     | 
+----+-----------------------------------------+-------+---------+--------------------+---------+--------------+-----+------------+-----+
| 3  | openshift-authentication                | 1/1   | Running | Initialized: V     | bm1-2   | 10.128.0.138 | 1   | 0          | 1d  | 
|    | oauth-openshift-55f74b6ccd-p8bdm        |       |         | PodScheduled: V    |         |              |     |            |     | 
|    |                                         |       |         | ContainersReady: V |         |              |     |            |     | 
|    |                                         |       |         | Ready: V           |         |              |     |            |     | 
+----+-----------------------------------------+-------+---------+--------------------+---------+--------------+-----+------------+-----+
| 4  | openshift-authentication                | 1/1   | Running | Initialized: V     | bm1-3   | 10.128.2.136 | 1   | 0          | 1d  | 
|    | oauth-openshift-55f74b6ccd-qp4fd        |       |         | PodScheduled: V    |         |              |     |            |     | 
|    |                                         |       |         | ContainersReady: V |         |              |     |            |     | 
|    |                                         |       |         | Ready: V           |         |              |     |            |     | 
+----+-----------------------------------------+-------+---------+--------------------+---------+--------------+-----+------------+-----+

+----+---------+-------------------+---------------+----------------+
| ID | OAuth   | Identity Provider | Identity Type | Identity Users |
+----+---------+-------------------+---------------+----------------+
| 1  | cluster | local-admins      | HTPasswd      | 2              | 
|    |         | ldap              | LDAP          | 0              | 
+----+---------+-------------------+---------------+----------------+

+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+
| ID | OAuth   | Provider | LDAP                                                                               | Attribute                            |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+
| 1  | cluster | ldap     | ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName | id: sAMAccountName                   |
|    |         |          | bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com                               | name: cn                             |
|    |         |          | secret: ldap [exists:True]                                                         | email: mail                          |
|    |         |          | mapping: claim                                                                     | preferredUsername: userPrincipalName |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+

+----+---------+-------------------+--------------+-----------+-------------+
| ID | OAuth   | Htpasswd Provider | Secret       | Is Secret | User        |
+----+---------+-------------------+--------------+-----------+-------------+
| 1  | cluster | local-admins      | local-admins | True      | xxx (admin) | 
|    |         |                   |              |           | yyy (admin) | 
|    |         |                   |              |           | zzz (admin) | 
+----+---------+-------------------+--------------+-----------+-------------+

+----+----------+-----------+-------+-----------------------+---------------+---------------+
| ID | User     | Full Name | Group | Identity              | Provider Name | Provider User |
+----+----------+-----------+-------+-----------------------+---------------+---------------+
| 1  | xxx      | ---       | ---   | local-admins:xxx      | local-admins  | xxx           | 
| 2  | yyy      | ---       | ---   | local-admins:yyy      | local-admins  | yyy           | 
+----+----------+-----------+-------+-----------------------+---------------+---------------+

+----+----------+---------------+-----------------------------------------------------------------------+
| ID | Group    | User          | LDAP Sync                                                             |
+----+----------+---------------+-----------------------------------------------------------------------+
| 1  | NORTH    | n1@domain.com | ldap-server.domain.com                                                | 
|    |          | n2@domain.com | CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com                       | 
|    |          | n3@domain.com | 2026-03-10T21:25:59Z                                                  | 
+----+----------+---------------+-----------------------------------------------------------------------+
| 2  | SOUTH    | s1@domain.com | ldap-server.domain.com                                                | 
|    |          | s2@domain.com | CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com                       | 
|    |          | s3@domain.com | 2026-03-10T21:25:59Z                                                  | 
+----+----------+---------------+-----------------------------------------------------------------------+
| 3  | rhods    | ---           | ---                                                                   | 
+----+----------+---------------+-----------------------------------------------------------------------+

View: state (def), verbose
```

[[Back]](./README.md) [[Prev]](./log.md) [[Next]](./restart.md)