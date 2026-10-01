# Tridentctl

Add tridentctl cli on the cluster [management node](../ManagementServer.md)

## Workflow

- --url or --version is required (refer to releases: https://github.com/NetApp/trident/releases)
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Expected outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which tridentctl
/usr/local/bin/tridentctl
```

## Configurable options

```
# iserver set ocp cli-tridentctl 
  --cluster TEXT  OCP cluster name
  --url TEXT      Tridentctl download url
  --version TEXT  Tridentctl version
```

## Example

```
# iserver set ocp cli-tridentctl --cluster bm1 --version 26.02.0

OpenShift Workflow - CLI - Add tridentctl
=========================================

OpenShift Cluster: bm1
Download: https://github.com/NetApp/trident/releases/download/v26.02.0/trident-installer-26.02.0.tar.gz
Uploading file to cluster management node: /tmp/56f2d99c-be4a-4132-8a37-5ec0b2070150
Unpack: sudo tar xzvfC /tmp/56f2d99c-be4a-4132-8a37-5ec0b2070150 /tmp/
Copy file: sudo sudo mv /tmp/trident-installer/tridentctl /usr/local/bin/tridentctl
Change file flags: sudo chmod a+x /usr/local/bin/tridentctl
Test: tridentctl --help

~~~
A CLI tool for managing the NetApp Trident external storage provisioner for Kubernetes

Usage:
  tridentctl [command]

Available Commands:
  completion  Generate completion script 
  create      Add a resource to Trident
  delete      Remove one or more resources from Trident
  get         Get one or more resources from Trident
  help        Help about any command
  images      Print a table of the container images Trident needs
  import      Import an existing resource to Trident
  install     Install Trident
  logs        Print the logs from Trident
  send        Send a resource from Trident
  uninstall   Uninstall Trident
  update      Modify a resource in Trident
  version     Print the version of Trident

Flags:
  -d, --debug               Set the log level to debug
  -h, --help                help for tridentctl
  -k, --kubeconfig string   Kubernetes config path
      --log-level string    Log level (trace, debug, warn, info, error, fatal (default "info")
  -n, --namespace string    Namespace of Trident deployment
  -o, --output string       Output format. One of json|yaml|name|wide|ps (default)
  -s, --server string       Address/port of Trident REST interface (127.0.0.1 or [::1] only)

Use "tridentctl [command] --help" for more information about a command.
~~~

Completed tasks
- tridentctl installed

+----+---------+-------+-------------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow          | Changes | Success | Duration [s] |
+----+---------+-------+-------------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create tridentctl | 0       | V       | 148          | 
+----+---------+-------+-------------------+---------+---------+--------------+
```

[[Back]](./README.md)