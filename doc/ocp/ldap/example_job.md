# LDAP group sync job example

[[Back]](./README.md) [[Prev]](./example_sync.md) [[Next]](./example_idp.md)

LDAP group synchronization using `oc adm groups sync` command as explained [here](./example_sync.md) can run as cron job.

Refer to CRD example below and [RedHat's documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/authentication_and_authorization/ldap-syncing#ldap-auto-syncing_ldap-syncing-groups).

## Namespace

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: ldap-sync
~~~

## ServiceAccount

~~~
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
~~~

## ClusterRole

~~~
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ldap-group-syncer
rules:
- apiGroups:
  - ''
  - user.openshift.io
  resources:
  - groups
  verbs:
  - get
  - list
  - create
  - update
~~~

# ClusterRoleBinding

~~~
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: ldap-group-syncer
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ldap-group-syncer
subjects:
- kind: ServiceAccount
  name: ldap-group-syncer
  namespace: ldap-sync
~~~

# ConfigMap

~~~
apiVersion: v1
data:
  sync.yaml: |-
    apiVersion: v1
    bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com
    bindPassword: secret
    insecure: true
    kind: LDAPSyncConfig
    rfc2307:
      groupMembershipAttributes:
      - member
      groupNameAttributes:
      - cn
      groupUIDAttribute: dn
      groupsQuery:
        baseDN: ou=Groups,ou=se,dc=se,dc=domain,dc=com
        derefAliases: never
        filter: (objectClass=group)
        pageSize: 0
        scope: sub
      tolerateMemberNotFoundErrors: false
      tolerateMemberOutOfScopeErrors: false
      userNameAttributes:
      - userPrincipalName
      userUIDAttribute: dn
      usersQuery:
        baseDN: ou=se,dc=se,dc=domain,dc=com
        derefAliases: never
        pageSize: 0
        scope: sub
    url: ldap://ldap-server.domain.com
kind: ConfigMap
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
~~~

~~~
apiVersion: v1
data:
  whitelist.txt: |-
    CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
    CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
kind: ConfigMap
metadata:
  name: ldap-whitelist-group-syncer
  namespace: ldap-sync
~~~

# CronJob

~~~
apiVersion: batch/v1
kind: CronJob
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
spec:
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 0
      template:
        spec:
          activeDeadlineSeconds: 500
          containers:
          - command:
            - /bin/bash
            - -c
            - oc adm groups sync --sync-config=/etc/config/sync.yaml --whitelist=/etc/whitelist/whitelist.txt
              --confirm
            image: registry.redhat.io/openshift4/ose-cli:latest
            name: ldap-group-syncer
            volumeMounts:
            - mountPath: /etc/config
              name: ldap-sync-volume
            - mountPath: /etc/whitelist
              name: ldap-sync-whitelist
          dnsPolicy: ClusterFirst
          restartPolicy: Never
          serviceAccountName: ldap-group-syncer
          terminationGracePeriodSeconds: 30
          volumes:
          - configMap:
              name: ldap-group-syncer
            name: ldap-sync-volume
          - configMap:
              name: ldap-whitelist-group-syncer
            name: ldap-sync-whitelist
      ttlSecondsAfterFinished: 1800
  schedule: '*/30 * * * *'
~~~

[[Back]](./README.md) [[Prev]](./example_sync.md) [[Next]](./example_idp.md)