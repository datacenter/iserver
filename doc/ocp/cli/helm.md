# Helm

Add helm cli on the cluster [management node](../Access.md)

## Workflow

- if --version value is not defined check helm version using https://get.helm.sh/helm-latest-version
- if --url value is not defined then url defaults to https://get.helm.sh/helm-VERSION-linux-amd64.tar.gz
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Expected Outcome

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

OpenShift Workflow - Install helm cli
=====================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "url": "https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz",
    "version": null,
    "confirmation": true,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- cli helm: not found

Downloading helm binary from https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz
Uploading helm binary to cluster management node
Unpack
Copy helm to /usr/local/bin
Remove local files
Change file flags
Helm binary ready to be used
version.BuildInfo{Version:"v3.19.0", GitCommit:"3d8990f0836691f0229297773f3524598f46bda6", GitTreeState:"clean", GoVersion:"go1.24.7"}
```

[[Back]](./README.md)