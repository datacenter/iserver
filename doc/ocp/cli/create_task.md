# CLI Tools - Create via Task

## Input

```
[
  {
    "cli": {
      "butane": {},
      "cilium": {},
      "helm": {},
      "hubble": {},
      "tridentctl": {
        "version": "26.02.0"
      },
      "virtctl": {},
      "file": {
        "namespace": "default",
        "filename": [
            "C:\\tmp\\to-apply"
        ]
      }
    }
  }
]
```

Notes:
- [butane](./create_butane.md), [cilium](./create_cilium.md), [helm](./create_helm.md), [hubble](./create_hubble.md), [tridentctl](./create_tridentctl.md) and [virtctl](./create_virtctl.md) trigger workflow execution with optional input parameters
- [file](./apply_file.md) applies crds from files

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

CLI tool installed

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - CLI - Add butane
=====================================

OpenShift Cluster: bm1
Download: https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-amd64
Uploading file to cluster management node: /tmp/97b27841-7fab-4f3d-9026-9bfe1ceb0fe2
Copy file: sudo sudo mv /tmp/97b27841-7fab-4f3d-9026-9bfe1ceb0fe2 /usr/local/bin/butane
Change file flags: sudo chmod a+x /usr/local/bin/butane
Test: butane --version

~~~
Butane 0.26.0
~~~

Completed tasks
- butane installed

OpenShift Workflow - CLI - Add cilium
=====================================

OpenShift Cluster: bm1
Download: https://github.com/cilium/cilium-cli/releases/download/v0.19.2/cilium-linux-amd64.tar.gz
Uploading file to cluster management node: /tmp/194e6078-1b82-4aec-b8e3-a98a0e5a5535
Unpack: sudo tar xzvfC /tmp/194e6078-1b82-4aec-b8e3-a98a0e5a5535 /tmp/
Copy file: sudo sudo mv /tmp/cilium /usr/local/bin/cilium
Change file flags: sudo chmod a+x /usr/local/bin/cilium
Test: cilium version

~~~
cilium-cli: v0.19.2 compiled with go1.25.5 on linux/amd64
cilium image (default): v1.19.1
cilium image (stable): unknown
cilium image (running): unknown. Unable to obtain cilium version. Reason: release: not found
~~~

Completed tasks
- cilium installed

OpenShift Workflow - CLI - Add helm
===================================

OpenShift Cluster: bm1
Download: https://get.helm.sh/helm-v4.1.4-linux-amd64.tar.gz
Uploading file to cluster management node: /tmp/38df87bc-66ab-43f4-a70c-8729c8f88574
Unpack: sudo tar xzvfC /tmp/38df87bc-66ab-43f4-a70c-8729c8f88574 /tmp/
Copy file: sudo sudo mv /tmp/linux-amd64/helm /usr/local/bin/helm
Change file flags: sudo chmod a+x /usr/local/bin/helm
Test: helm version

~~~
version.BuildInfo{Version:"v4.1.4", GitCommit:"05fa37973dc9e42b76e1d2883494c87174b6074f", GitTreeState:"clean", GoVersion:"go1.25.9", KubeClientVersion:"v1.35"}
~~~

Completed tasks
- helm installed

OpenShift Workflow - CLI - Add hubble
=====================================

OpenShift Cluster: bm1
Download: https://github.com/cilium/hubble/releases/download/v1.19.3/hubble-linux-amd64.tar.gz
Uploading file to cluster management node: /tmp/59de6056-74f2-4c0b-a842-fbaa226e80b0
Unpack: sudo tar xzvfC /tmp/59de6056-74f2-4c0b-a842-fbaa226e80b0 /tmp/
Copy file: sudo sudo mv /tmp/hubble /usr/local/bin/hubble
Change file flags: sudo chmod a+x /usr/local/bin/hubble
Test: hubble version

~~~
hubble v1.19.3@HEAD-400168b compiled with go1.26.2 on linux/amd64
~~~

Completed tasks
- hubble installed

OpenShift Workflow - CLI - Add tridentctl
=========================================

OpenShift Cluster: bm1
Download: https://github.com/NetApp/trident/releases/download/v26.02.0/trident-installer-26.02.0.tar.gz
Uploading file to cluster management node: /tmp/3de7dff3-f046-42b0-88b7-6c96fb2fa2ad
Unpack: sudo tar xzvfC /tmp/3de7dff3-f046-42b0-88b7-6c96fb2fa2ad /tmp/
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

OpenShift Workflow - CLI - Add virtctl
======================================

OpenShift Cluster: bm1
Check for cluster endpoint to download virtctl binary from [timeout:30]...
Wait for endpoint openshift-cnv/hyperconverged-cluster-cli-download...
Download: https://hyperconverged-cluster-cli-download-openshift-cnv.apps.bm1.ocp.domain.com.com/amd64/linux/virtctl.tar.gz
Uploading file to cluster management node: /tmp/ed9ea3f1-f09e-4bb6-989f-3200ed386a10
Unpack: sudo tar xzvfC /tmp/ed9ea3f1-f09e-4bb6-989f-3200ed386a10 /tmp/
Copy file: sudo sudo mv /tmp/virtctl /usr/local/bin/virtctl
Change file flags: sudo chmod a+x /usr/local/bin/virtctl
Test: virtctl version

~~~
Client Version: version.Info{GitVersion:"v1.7.2-43-g4ba49e3e1e", GitCommit:"4ba49e3e1e704f0140d502652ce306095e21c217", GitTreeState:"clean", BuildDate:"2026-03-25T18:46:25Z", GoVersion:"go1.24.13 (Red Hat 1.24.13-1.el9_6) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{GitVersion:"v1.7.2-43-g4ba49e3e1e", GitCommit:"4ba49e3e1e704f0140d502652ce306095e21c217", GitTreeState:"clean", BuildDate:"2026-03-25T18:46:02Z", GoVersion:"go1.24.13 (Red Hat 1.24.13-1.el9_6) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
~~~

Completed tasks
- virtctl installed

+----+---------+-------+-------------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow          | Changes | Success | Duration [s] |
+----+---------+-------+-------------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create butane     | 0       | V       | 27           | 
| 2  | ocp:bm1 | cli   | create cilium     | 0       | V       | 167          | 
| 3  | ocp:bm1 | cli   | create helm       | 0       | V       | 65           | 
| 4  | ocp:bm1 | cli   | create hubble     | 0       | V       | 49           | 
| 5  | ocp:bm1 | cli   | create tridentctl | 0       | V       | 190          | 
| 6  | ocp:bm1 | cli   | create virtctl    | 0       | V       | 80           | 
+----+---------+-------+-------------------+---------+---------+--------------+
```

[[Back]](./README.md)