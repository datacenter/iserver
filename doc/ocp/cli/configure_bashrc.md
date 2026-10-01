# .bashrc

Configure .bashrc http proxy settings on the cluster [management node](../ManagementServer.md)

## Workflow

- get .bashrc file
- modify .bashrc http proxy content based on user input
- upload .bashrc file

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver set ocp cli-bashrc
  --cluster TEXT      Cluster name
  --http_proxy TEXT   http proxy
  --https_proxy TEXT  https proxy
  --no_proxy TEXT     no proxy
  --inherit           Inherit from cluster proxy
```

## Example

```
# iserver set ocp cli-bashrc --cluster bm1 --inherit

OpenShift Workflow - CLI - .bashrc proxy settings
=================================================

OpenShift Cluster: bm1
Proxy settings inherited from cluster proxy
http_proxy: http://proxy.domain.com:80
https_proxy: http://proxy.domain.com:80
no_proxy: .bm1.domain.com,.cluster.local,.svc,10.244.0.0/14,api-int.bm1.domain.com,domain.com,localhost
Download /var/home/core/.bashrc
http proxy settings will be added/replaced
added line [export HTTP_PROXY=http://proxy.domain.com:80]
added line [export HTTPS_PROXY=http://proxy.domain.com:80]
added line [export NO_PROXY=.bm1.domain.com,.cluster.local,.svc,10.244.0.0/14,api-int.bm1.domain.com,domain.com,localhost]
Upload /var/home/core/.bashrc
.bashrc uploaded with proxy settings

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create bashrc | 0       | V       | 5            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)