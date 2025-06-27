# Tasks

General notes:
- tasks are optional
- tasks run only after successful installation of bare metal cluster
- use --tasks flag during command execution to run tasks only
- it should be safe to re-run the command with --tasks flag since task execution code checks if the work has been already done
- add 'break-on-error:flag' property per task if you want workflow to stop when task fails
- by default, the tasks will run to completion even if some tasks fail
- operators installation is supported only
- tasks can be defined in tasks.json file

### Task: cli

- executes arbitrary list of commands (cli.exec)
- installs cli tools selected with flags
- configures .bashrc of core user

```
    "tasks": [
        {
            "cli": {
                "exec": [
                    "oc get node"
                ],
                "virtctl": true,
                "helm": true,
                "bashrc": true,
                "cilium": true,
                "hubble": true
            }
        }
    ]
```

Expected outcome if all flags enabled

```
$ ls /usr/local/bin
cilium
helm
hubble
virtctl
```

```
$ id
uid=1000(core) gid=1000(core) groups=1000(core),4(adm),10(wheel),16(sudo),190(systemd-journal) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
$ tail -3 .bashrc
export HTTP_PROXY=http://proxy.domain:80
export HTTPS_PROXY=http://proxy.domain.com:80
export NO_PROXY=localhost,.ocp.lan,10.4.4.1
```

### Task: cni

- enable OVS CNI based on https://github.com/k8snetworkplumbingwg/ovs-cni

Example:

```
    "cni": {
        "ovs": "0.39.0"
    }
```

Make sure that cni.ovs contains version value available at [releases](https://github.com/k8snetworkplumbingwg/ovs-cni/releases)

Expected outcome

```
$ ls -lta /var/lib/cni/bin/ovs
-rwxr-xr-x. 1 core core 13521372 Jun 11 07:17 /var/lib/cni/bin/ovs

$ /var/lib/cni/bin/ovs -v
CNI OVS bridge plugin version unknown
CNI protocol versions supported: 0.1.0, 0.2.0, 0.3.0, 0.3.1, 0.4.0, 1.0.0, 1.1.0
```

### Task: identity

- adds identity provider of HTPasswd type with user credentials defined in input file located in root directory
- selected or all users defined in the htpasswd file are configured with cluster-admin role
- htpasswd file has to be created offline, check [here](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/authentication_and_authorization/index#identity-provider-creating-htpasswd-file-linux_configuring-htpasswd-identity-provider) for guidance
- kubeadmin user is by default created by assisted installer workflow, you may decide to delete it automatically

```
    "tasks": [
        {
            "identity": {
                "provider": "htpasswd",
                "filename": "htpasswd",
                "admin": [
                    "__ALL__"
                ]
            }
        },
        {
            "identity": {
                "provider": "kubeadmin",
                "delete": false
            }
        }
```

### Task: ssh

- single ssh public key is defined at the global level of cluster.json file or in ssh.pub file
- add extra keys if needed by definining ssh.keys list or putting ssh public keys in ssh subdirectory

```
    "tasks": [
        {
            "ssh": {
                "keys": [
                    "ssh-ed25519 AAAA..."
                ]
            }
        }
    ]
```

### Task: nmstate

nmstate operator installation with the following defaults

```
    "nmstate": {
        "namespace": "openshift-nmstate",
        "name": "kubernetes-nmstate-operator",
        "channel": "stable",
        "instance": "nmstate",
        "confirmation": false,
        "check-fqdn": false,
        "break-on-error": false,
        "lldp": {
            "nic-fw-disable": false,
            "enable": false,
            "include-down": true,
            "delete-nncp": true
        }
    }
```

The minimum task definition

```
    "nmstate": {}
```

Workflow details
- operator installed from package manifest nmstate.name and nmstate.channel into nmstate.namespace
- wait until operator installation completes
- nmstate.instance created with default empty spec
- wait until nns available per node
- if lldp.nic-fw-disable
    - for every physical ethernet interface
    - check priv flags with ethtools
    - if lldp enabled on fw level, then disable it
    - Intel NIC 700/800 series supported
- if lldp.enable
    - check nns for every physical ethernet interface
    - if lldp disabled then enable it with extra check on interface state vs nmstate.lldp.include-down flag
    - lldp is enabled on interface using nncp
    - nmstate.lldp.delete-nncp control if nncp policies are deleted

```
    deployments = [
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-cert-manager'},
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-console-plugin'},
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-operator'},
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-webhook'}
    ]
```

### Task: nfd

Node feature discovery (nfd) operator installation with the following defaults

```
    "nfd": {
        "namespace": "openshift-nfd",
        "name": "nfd",
        "channel": "stable",
        "instance": "nfd-instance",
        "confirmation": false,
        "check-fqdn": false,
        "break-on-error": false
    }
```

The minimum task definition

```
    "nfd": {}
```

Workflow details
- operator installed from package manifest nmstate.name and nmstate.channel into nmstate.namespace
- wait until operator installation completes
- wait until nodes annotated with nfd features

```
    deployments = [
        {'namespace': 'openshift-nfd', 'name': 'nfd-controller-manager'},
        {'namespace': 'openshift-nfd', 'name': 'nfd-master'}
    ]

    daemon_sets = [
        {'namespace': 'openshift-nfd', 'name': 'nfd-worker'}
    ]
```

### Task: sriov

SR-IOV operator installation with the following defaults

```
    "sriov": {
        "namespace": "openshift-sriov-network-operator,
        "name": "sriov-network-operator",
        "channel": "stable",
        "confirmation": false,
        "check-fqdn": false,
        "break-on-error": false,
        "wait_ready": 600,
        "wait_not_ready": 180
    }
```

The minimum task definition

```
    "sriov": {}
```

Workflow details
- operator installed from package manifest nmstate.name and nmstate.channel into nmstate.namespace
- wait until operator installation completes

```
    deployments = [
        {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-operator'}
    ]

    daemon_sets = [
        {'namespace': 'openshift-sriov-network-operator', 'name': 'network-resources-injector'},
        {'namespace': 'openshift-sriov-network-operator', 'name': 'operator-webhook'},
        {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-config-daemon'}
    ]
```

SR-IOV Network Node Policy can be further defined per physical interface

Example

```
    "policy": [
        {
            "interface": "ens1f0",
            "type": "netdevice",
            "name": "ens1f0net",
            "resource": "ens1f0net",
            "vfs": "64",
            "range": "0-31"
        },
        {
            "interface": "ens1f0",
            "type": "vfio-pci",
            "name": "ens1f0dpdk",
            "resource": "ens1f0dpdk",
            "vfs": "64",
            "range": "32-63"
        }
    ]
```

Note:
- sriov.policy.interface must be defined
- sriov.policy.type must be defined and one of ['netdevice', 'vfio-pci']
- sriov.policy.name is optional and defaults to sriov.policy.interface with net or dpdk suffix
- sriov.policy.resource is optional and defaults to sriov.policy.interface with net or dpdk suffix
- sriov.policy.range is optional and must be used in case VF type split on a single interface. defaults to None

Resulting SriovNetworkNodePolicy CR that is applied (if does not exist yet - checked by name)

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: {sriov.policy.name}
  namespace: {sriov.namespace}
spec:
  deviceType: {sriov.policy.type}
  isRdma: false
  nicSelector:
    pfNames:
    - {sriov.policy.interface}#{sriov.policy.range}   -- if range defined
    - {sriov.policy.interface}                        -- if range not defined
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  numVfs: {sriov.policy.vfs}
  resourceName: {sriov.policy.resource}
```

Example output

```
Wait for deployments ready...
- openshift-sriov-network-operator/sriov-network-operator
Wait for deamon sets ready...
- openshift-sriov-network-operator/network-resources-injector
- openshift-sriov-network-operator/operator-webhook
- openshift-sriov-network-operator/sriov-network-config-daemon
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f0net
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f0#0-31
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f0net

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f0dpdk
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f0#32-63
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f0dpdk


Completed tasks
- SR-IOV Operator installed
- SR-IOV Node Network Policy created
```

If policy is created, network node reloads may occur
- the workflow waits for sriov.wait_not_ready seconds for any node reload
- if reload is detected, then it waits sriov.wait_ready seconds for all nodes to be ready

[Back](../BareMetalCluster.md)
