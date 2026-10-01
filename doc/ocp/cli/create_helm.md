# Helm

Add helm cli on the cluster [management node](../ManagementServer.md)

## Workflow

- if --version value is not defined check helm version using https://get.helm.sh/helm-latest-version
- if --url value is not defined then url defaults to https://get.helm.sh/helm-VERSION-linux-amd64.tar.gz
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Expected outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which helm
/usr/local/bin/helm
[core@bm1 ~]$ helm version
version.BuildInfo{Version:"v3.19.0", GitCommit:"3d8990f0836691f0229297773f3524598f46bda6", GitTreeState:"clean", GoVersion:"go1.24.7"}
```

## Configurable options

```
# iserver set ocp cli-helm 
  --cluster TEXT  OCP cluster name
  --url TEXT      Helm download url
  --version TEXT  Helm version
```

## Example

```
# iserver set ocp cli-helm --cluster bm1

OpenShift Workflow - CLI - Add helm
===================================

OpenShift Cluster: bm1
Download: https://get.helm.sh/helm-v4.1.4-linux-amd64.tar.gz
Uploading file to cluster management node: /tmp/cf592b95-3ed5-45ea-bacb-74dea6962191
Unpack: sudo tar xzvfC /tmp/cf592b95-3ed5-45ea-bacb-74dea6962191 /tmp/
Copy file: sudo sudo mv /tmp/linux-amd64/helm /usr/local/bin/helm
Change file flags: sudo chmod a+x /usr/local/bin/helm
Test: helm version

~~~
version.BuildInfo{Version:"v4.1.4", GitCommit:"05fa37973dc9e42b76e1d2883494c87174b6074f", GitTreeState:"clean", GoVersion:"go1.25.9", KubeClientVersion:"v1.35"}
~~~

Completed tasks
- helm installed

+----+---------+-------+-------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow    | Changes | Success | Duration [s] |
+----+---------+-------+-------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create helm | 0       | V       | 36           | 
+----+---------+-------+-------------+---------+---------+--------------+
```

[[Back]](./README.md)