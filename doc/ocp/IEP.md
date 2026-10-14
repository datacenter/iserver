# Isovalent Registry Access

[[Back]](./Operations.md) [[Next]](./BareMetalCluster.md)

In case of Isovalent Enterprise Platform CNI installation in OpenShift, identity token and registry hostname name **must** be configured to properly authenticate with registry. Identity token must be acquired from [Isovalent Container Registry](https://docs.isovalent.com/iep/latest/platform/registry.html).

Configuration needs to be repeated once token expires.

## Configure

Make sure that registry name is just hostname, nothing more

```
# iserver set ocp cilium registry --registry registry.isovalent.com --token aaa

OpenShift Workflow - Isovalent registry access settings
=======================================================

Registry: registry.isovalent.com
Identity token: aaa
Access token created
~~~
{
    "token_id": "bbb",
    "access_token": "ccc",
    "expires_in": 7776000,
    "scope": "applied-permissions/user",
    "token_type": "Bearer",
    "description": "iserver-test-token",
    "username": "userid"
}
~~~
Access token deleted: bbb
Registry authentication and access token manipulation successfully verified
Cilium settings directory: C:\Users\akaliwod\.itool\cilium
Isovalent registry settings saved
```

## Check

```
# iserver get ocp cilium registry                                                                                                                               

OpenShift Workflow - Isovalent registry access settings
=======================================================

Registry: registry.isovalent.com
Identity token: aaa
Access token created
~~~
{
    "token_id": "bbb",
    "access_token": "ccc",
    "expires_in": 7776000,
    "scope": "applied-permissions/user",
    "token_type": "Bearer",
    "description": "iserver-test-token",
    "username": "userid"
}
~~~
Access token deleted: bbb
Registry authentication and access token manipulation successfully verified
```

## Get access token

```
# iserver get ocp cilium token

OpenShift Workflow - Isovalent registry access settings
=======================================================

Registry: registry.isovalent.com
Identity token: aaa
Access token created
~~~
{
    "token_id": "bbb",
    "access_token": "ccc",
    "expires_in": 7776000,
    "scope": "applied-permissions/user",
    "token_type": "Bearer",
    "description": "iserver-test-token",
    "username": "userid"
}
~~~
```

## Revoke access token

```
# iserver delete ocp cilium token --token-id bbb

OpenShift Workflow - Isovalent registry access settings
=======================================================

Registry: registry.isovalent.com
Identity token: aaa
Access token deleted: bbb
```

[[Back]](./Operations.md) [[Next]](./BareMetalCluster.md)