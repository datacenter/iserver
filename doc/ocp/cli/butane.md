# Butane

Add butane cli on the cluster [management node](../Access.md)

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
  --cluster TEXT  OCP cluster name
  --url TEXT      Helm download url
  --version TEXT  Helm version
```

## Example

```
# iserver set ocp cli-butane --cluster bm1

OpenShift Workflow - Install butane cli
=======================================

OpenShift Cluster: bm1
Downloading butane binary from https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-amd64
Uploading butane binary to cluster management node
Copy butane to /usr/local/bin
Change file flags

~~~
Butane 0.25.1

~~~

Completed tasks
- butane installed
```

[[Back]](./README.md)