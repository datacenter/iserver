# Virtctl

Add virtctl cli on the cluster [management node](../ManagementServer.md)

## Workflow

- if --url value is not defined then url defaults to https://hyperconverged-cluster-cli-download-openshift-cnv.CLUSTER-DOMAIN/amd64/linux/virtctl.tar.gz
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Virtualization [operator](../cnv/create_operator.md) and [instance](../cnv/create_instance.md) ready

## Expected outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which virtctl
/usr/local/bin/virtctl
[core@bm1 ~]$ virtctl --help
virtctl controls virtual machine related operations on your kubernetes cluster.

Available Commands:
  addvolume         add a volume to a running VM
  adm               Administrate KubeVirt configuration.
  completion        Generate the autocompletion script for the specified shell
  console           Connect to a console of a virtual machine instance.
  create            Create a manifest for the specified Kind.
  credentials       Manipulate credentials on a virtual machine.
  expand            Return the VirtualMachine object with expanded instancetype and preference.
  expose            Expose a virtual machine instance, virtual machine, or virtual machine instance replica set as a new service.
  fslist            Return full list of filesystems available on the guest machine.
  guestfs           Start a shell into the libguestfs pod
  guestosinfo       Return guest agent info about operating system.
  help              Help about any command
  image-upload      Upload a VM image to a DataVolume/PersistentVolumeClaim.
  memory-dump       Dump the memory of a running VM to a pvc
  migrate           Migrate a virtual machine.
  migrate-cancel    Cancel migration of a virtual machine.
  pause             Pause a virtual machine
  permitted-devices List the permitted devices for vmis.
  port-forward      Forward local ports to a virtualmachine or virtualmachineinstance.
  removevolume      remove a volume from a running VM
  restart           Restart a virtual machine.
  scp               SCP files from/to a virtual machine instance.
  soft-reboot       Soft reboot a virtual machine instance
  ssh               Open a SSH connection to a virtual machine instance.
  start             Start a virtual machine.
  stop              Stop a virtual machine.
  unpause           Unpause a virtual machine
  usbredir          Redirect an USB device to a virtual machine instance.
  userlist          Return full list of logged in users on the guest machine.
  version           Print the client and server version information.
  vmexport          Export a VM volume.
  vnc               Open a vnc connection to a virtual machine instance.
```

## Configurable options

```
# iserver set ocp cli-virtctl 
  --cluster TEXT  OCP cluster name
  --url TEXT      Virtctl package url
```

## Example

```
# iserver set ocp cli-virtctl --cluster bm1

OpenShift Workflow - CLI - Add virtctl
======================================

OpenShift Cluster: bm1
Check for cluster endpoint to download virtctl binary from [timeout:30]...
Wait for endpoint openshift-cnv/hyperconverged-cluster-cli-download...
Download: https://hyperconverged-cluster-cli-download-openshift-cnv.apps.bm1.ocp.domain.com.com/amd64/linux/virtctl.tar.gz
Uploading file to cluster management node: /tmp/da338736-5117-4d5e-98ff-9e8079d85226
Unpack: sudo tar xzvfC /tmp/da338736-5117-4d5e-98ff-9e8079d85226 /tmp/
Copy file: sudo sudo mv /tmp/virtctl /usr/local/bin/virtctl
Change file flags: sudo chmod a+x /usr/local/bin/virtctl
Test: virtctl version

~~~
Client Version: version.Info{GitVersion:"v1.7.2-43-g4ba49e3e1e", GitCommit:"4ba49e3e1e704f0140d502652ce306095e21c217", GitTreeState:"clean", BuildDate:"2026-03-25T18:46:25Z", GoVersion:"go1.24.13 (Red Hat 1.24.13-1.el9_6) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{GitVersion:"v1.7.2-43-g4ba49e3e1e", GitCommit:"4ba49e3e1e704f0140d502652ce306095e21c217", GitTreeState:"clean", BuildDate:"2026-03-25T18:46:02Z", GoVersion:"go1.24.13 (Red Hat 1.24.13-1.el9_6) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
~~~

Completed tasks
- virtctl installed

+----+---------+-------+----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create virtctl | 0       | V       | 45           | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md)