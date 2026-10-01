# CLI - Butane

Add butane cli on the cluster [management node](../ManagementServer.md)

## Workflow

- if --url value is not defined then url defaults to https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-amd64
- download binary
- upload binary to cluster's management node /usr/local/bin
- make binary executable

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Expected outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which butane
/usr/local/bin/butane
[core@bm1 ~]$ butane --version
Butane 0.25.1
```

## Configurable options

```
# iserver set ocp cli-butane 
  --cluster TEXT  Cluster name
  --url TEXT      Butane download url
  --no-confirm    Confirmation mode
```

## Example

```
# iserver set ocp cli-butane --cluster bm1

OpenShift Workflow - CLI - Add butane
=====================================

OpenShift Cluster: bm1
Uploading file to cluster management node: /tmp/cd3d5011-68ec-4b5c-bc79-3fb8e7d9636f
Copy file to /usr/local/bin
Change file flags

~~~
Butane 0.26.0
~~~

Completed tasks
- butane installed

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create butane | 0       | V       | 20           | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)