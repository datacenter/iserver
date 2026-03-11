# LDAP Identity Provider - Set provider

[[Back]](./README.md) [[Prev]](./get.md) [[Next]](./create_task.md)

## Workflow

- check ldap server access using `curl` if cluster has [management server](../Access.md)
- replace `OAuth` cluster with ldap identity provider entry
- create `Secret`
- wait for auth pods restart

## Requirements

None

## Configurable options

```
# iserver set ocp ldap
  --cluster TEXT                Cluster Name
  --filename TEXT               oauth provider filename
  --provider TEXT               LDAP Provider Name
  --url TEXT                    LDAP URL with baseDN
  --bind TEXT                   Binding dn
  --secret TEXT                 LDAP secret
  --id TEXT                     Attribute id
  --name TEXT                   Attribute name
  --username TEXT               Attribute preferredUsername
  --email TEXT                  Attribute email
  --insecure                    LDAP secure mode
  --mapping [claim|lookup|add]  Mapping method  [default: claim]
  --no-confirm                  Confirmation mode
```

## Before

![Login](../images/ldap/no_ldap.png)

```
# iserver get ocp ldap --cluster bm1
    
OpenShift Workflow - LDAP Identity Provider - Get
=================================================

OpenShift Cluster: bm1
Identity ldap not defined

View: list (def), verbose
```

## Action

```
# iserver set ocp ldap \
    --cluster bm1 \
    --provider ldap \
    --url ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName \
    --bind CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com \
    --secret secret \
    --id sAMAccountName \
    --name cn \
    --email mail \
    --username userPrincipalName \
    --insecure \
    --no-confirm

OpenShift Workflow - LDAP Identity Provider - Add
=================================================

OpenShift Cluster: bm1

Check LDAP access from clusters management host...
~~~
# curl -sS --insecure ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName -u CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com:secret
DN: ou=users,ou=se,dc=se,dc=domain,dc=com


~~~

Set LDAP identity provider
--------------------------
- oauth: cluster
- provider: ldap

Replace OAuth
-------------
- name: cluster

~~~
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: 'true'
    include.release.openshift.io/self-managed-high-availability: 'true'
    release.openshift.io/create-only: 'true'
  name: cluster
spec:
  identityProviders:
  - htpasswd:
      fileData:
        name: local-admins
    mappingMethod: claim
    name: local-admins
    type: HTPasswd
  - ldap:
      attributes:
        email:
        - mail
        id:
        - sAMAccountName
        name:
        - cn
        preferredUsername:
        - userPrincipalName
      bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com
      bindPassword:
        name: ldap
      insecure: true
      url: ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName
    mappingMethod: claim
    name: ldap
    type: LDAP

~~~
OAuth [cluster] replaced

Create Secret
-------------
- namespace: openshift-config
- name: ldap

~~~
apiVersion: v1
data:
  bindPassword: ...
kind: Secret
metadata:
  name: ldap
  namespace: openshift-config
type: Opaque

~~~
Secret [openshift-config/ldap] created
- wait for Secret openshift-config/ldap [timeout:60s]

OAuth restart
- wait for no Pod openshift-authentication/oauth-openshift-668df78d4f-gs495 [timeout:180s]
- wait for no Pod openshift-authentication/oauth-openshift-668df78d4f-qjcvq [timeout:180s]
- wait for no Pod openshift-authentication/oauth-openshift-668df78d4f-thm25 [timeout:180s]
- wait for deployment openshift-authentication/oauth-openshift ready state [timeout:180s]

Completed tasks
- LDAP Identity Provider configured
```

## After

![Login](../images/ldap/ldap_login.png)

```
# iserver get ocp ldap --cluster bm1 -v verbose

+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| ID | OAuth   | Provider | LDAP                                                                               | Attribute                            | Usage    |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| 1  | cluster | ldap     | ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName | id: sAMAccountName                   | User:  0 | 
|    |         |          | bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com                               | name: cn                             | Group: 0 | 
|    |         |          | secret: ldap [exists:True]                                                         | email: mail                          |          | 
|    |         |          | mapping: claim                                                                     | preferredUsername: userPrincipalName |          |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
```

[[Back]](./README.md) [[Prev]](./get.md) [[Next]](./create_task.md)