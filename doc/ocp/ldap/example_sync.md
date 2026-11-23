# LDAP group sync example

[[Back]](./README.md) [[Prev]](./example_idp.md) [[Next]](./example_job.md)

The goal is to sync LDAP groups and users with OpenShift using `oc adm groups sync` cli with mandatory `--sync-config` yaml file that defines
- ldap server url, bind dn (username) and bind password
- groupsQuery section with baseDN for groups
- usersQuery section with baseDN for users
- extra parameters controlling how group and user ldap information is parsed and how it gets translated to Group CRD in Kubernetes
 
Optional cli parameters
- blacklist: file with the group dn that will not be synced
- whitelist: file with the group dn that will be synced
- confirm: OpenShift groups will be modified

[Reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/ldap-syncing#ldap-syncing-config-rfc2307_ldap-syncing-groups)

## LDAP 

- Server: ldap://ldapserver.domain.com
- BindDN (username): cn=bm1,ou=Users,ou=se,dc=se,dc=domain,dc=com
- Password: secret

<ins>Group</ins>

```
objectClass: group
cn: ADMINS-EMEA
name: ADMINS-EMEA
sAMAccountName: ADMINS-EMEA
distinguishedName: CN=ADMINS-EMEA,OU=Groups,OU=se,DC=se,DC=domain,DC=com
member: CN=Arkadiusz Kaliwoda,OU=Users,OU=se,DC=se,DC=domain,DC=com
```

All details with: 'curl ldap://ldapserver.domain.com/CN=ADMINS-EMEA,OU=Groups,OU=se,DC=se,DC=domain,DC=com -u cn=bm1,ou=Users,ou=se,dc=se,dc=domain,dc=com:secret'

<ins>User</ins>

```
objectClass: person
objectClass: user
cn: Arkadiusz Kaliwoda
distinguishedName: CN=Arkadiusz Kaliwoda,OU=Users,OU=se,DC=se,DC=domain,DC=com
displayName: Arkadiusz Kaliwoda
name: Arkadiusz Kaliwoda
sAMAccountName: akaliwod
userPrincipalName: akaliwod@domain.com
memberOf: CN=ADMINS-EMEA,OU=Groups,OU=se,DC=se,DC=domain,DC=com
```

All details with: 'curl ldap://ldapserver.domain.com/CN="Arkadiusz%20Kaliwoda",OU=Users,OU=se,DC=se,DC=domain,DC=com -u cn=bm1,ou=Users,ou=se,dc=se,dc=domain,dc=com:secret'

## Sync config

```
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://ldapserver.domain.com
insecure: true
bindDN: cn=bm1,ou=Users,ou=se,dc=se,dc=domain,dc=com
bindPassword: "secret"
rfc2307:
    groupsQuery:
        baseDN: ou=Groups,ou=se,dc=se,dc=domain,dc=com
        scope: sub
        filter: (objectClass=group)
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: ou=se,dc=se,dc=domain,dc=com
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn
    userNameAttributes: [ userPrincipalName ]
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
```

Attribute | Description
--- | ---
groupUIDAttribute | The attribute that uniquely identifies a group on the LDAP server
groupNameAttributes | The attribute to use as the name of the group
groupMembershipAttributes | The attribute on the group that stores the membership information
userUIDAttribute | The attribute that uniquely identifies a user on the LDAP server
userNameAttributes | The attribute to use as the name of the user in the OpenShift Container Platform group record.
tolerateMemberNotFoundErrors | If group contains member attributes that are known to be missing, setting this property to `true` value will keep sync running
tolerateMemberOutOfScopeErrors | If user entry does not belong to usersQuery.baseDN, sync breaks unless this property is `true`

> [!NOTE]
> if the groups being synced contain members whose entries are outside of the scope defined in the member query, the group sync fails with an error 'Error determining LDAP group membership'

The example from above that works

```
    groupsQuery:
        baseDN: ou=Groups,ou=se,dc=se,dc=domain,dc=com
    usersQuery:
        baseDN: ou=se,dc=se,dc=domain,dc=com
```

While distinguished name of the user is e.g., cn=Arkadiusz Kaliwoda,ou=Users,ou=se,dc=se,dc=domain,dc=com so one can try with the following query definitions

```
    groupsQuery:
        baseDN: ou=Groups,ou=se,dc=se,dc=domain,dc=com
    usersQuery:
        baseDN: ou=Users,ou=se,dc=se,dc=domain,dc=com
```

However, this one will fail with 'Error determining LDAP group membership'.

## Sync check

`oc adm groups sync --sync-config=./sync-config.yaml`

Collect LDAP information
- get all groups selected with groupsQuery.baseDN
- get group members as defined with groupMembershipAttributes using usersQuery
- tolerateMemberNotFoundErrors controls what-if the user is not found
- tolerateMemberOutOfScopeErrors controls what-if the group member user is outside of usersQuery.baseDN

Prepare Kubernetes Group CRD
- Group metadata.name based on groupNameAttributes of LDAP Group
- Group users with userNameAttributes of LDAP User
- annotations and labels auto-generated and cannot be controlled

Note: while groupNameAttributes and userNameAttributes allow defining list of attributes, only the first list item is used

Example

```
apiVersion: v1
items:
- apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: "2026-03-06T14:34:26Z"
      openshift.io/ldap.uid: CN=ADMINS-EMEA,OU=Groups,OU=se,DC=se,DC=domain,DC=com
      openshift.io/ldap.url: ldapserver.domain.com:389
    labels:
      openshift.io/ldap.host: ldapserver.domain.com
    name: ADMINS-EMEA
  users:
  - akaliwod@domain.com
```

## Sync run

`oc adm groups sync --sync-config=./sync-config.yaml --confirm`

```
# oc adm groups sync --sync-config=./sync-config.yaml --confirm
group/ADMINS-EMEA
```

```
# oc get group
NAME               USERS
ADMINS-EMEA        akaliwod@domain.com
```

Notes:
- the generated Kubernetes `Group` objects are applied (add-or-replace)
- if command ru-runs with different generated `Group` objects (as the result of change in LDAP or whitelisting/blacklisting), the `Group` that has been created previously and has ldap annotations and lables will *not* be deleted

## Whitelisting and blacklisting

`oc adm groups sync` selects all LDAP groups from groupsQuery.baseDN. For fine-grained filtering, pass --whitelist or --blacklist parameter with text file reference with group distinguished names to be synced or to be not-synced
- unlike bindDN and baseDN in sync config yaml; make sure to keep the attribute names case sensitive in whitelist following whatever is done in LDAP
- every group defined in whitelist must exist in LDAP or error is raised
- non-existing group defined in blacklist is silently ignored
- if both whitelist and blacklist is defined then whitelist LDAP groups are selected first followed with removing groups that are in blacklist

```
# cat whitelist.txt
CN=ADMINS-EMEA,OU=Groups,OU=se,DC=se,DC=domain,DC=com

# cat blacklist.txt
CN=AAA,OU=Groups,OU=se,DC=se,DC=domain,DC=com
CN=BBB,OU=Groups,OU=se,DC=se,DC=domain,DC=com

# oc adm groups sync --sync-config=./sync-config.yaml --blacklist=./blacklist.txt  --whitelist=./whitelist.txt
apiVersion: v1
items:
- apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: "2026-03-06T15:14:03Z"
      openshift.io/ldap.uid: CN=ADMINS-EMEA,OU=Groups,OU=se,DC=se,DC=domain,DC=com
      openshift.io/ldap.url: ldapserver.domain.com:389
    labels:
      openshift.io/ldap.host: ldapserver.domain.com
    name: ADMINS-EMEA
  users:
  - akaliwod@domain.com
```

[[Back]](./README.md) [[Prev]](./example_idp.md) [[Next]](./example_job.md)