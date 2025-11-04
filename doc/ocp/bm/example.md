# OpenShift Installation Example

- 3 node cluster
- Cilium EE
- post installation tasks

```
Checking user input...
Checking openshift API...
- API token filename: /home/user/.itool/openshift/token
- Token file read successful
- Pull secret filename: /home/user/.itool/openshift/pull_secret.txt
- Pull secret file read successful
- RedHat Console API connection sucessfull
Cilium manifests verification enabled
- manifests type: clife
- cilium version: v1.17.6-cee.1

Web server is local
Upload directory found: /home/user/image
Check local web server http access...
Test file uploaded locally to web server and then downloaded successfully via http
Redfish endpoint: 10.20.20.10
- ChassisType: Rack
- Model: Cisco UCS
- SerialNumber: SERIAL1
- PowerState: On
- Detected chassis type: Rack
Virtual Media [0]
- Name: Virtual CD
- Inserted: False
- MediaTypes: ['CD', 'DVD']
- ConnectedVia: NotConnected
- State: Disabled
- Health: OK
Virtual media test
- filename to be uploaded to web server: image.iso
Creating file in local web server: image.iso
- url: http://10.50.50.50:8080/image.iso
- virtual media inserted [id:0]
- virtual media mapped
- virtual media ejected
Deleting file in local web server: image.iso
- web server file deleted
Boot settings
- boot source override enabled: Once
- boot source override target: Hdd
- target values: ['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags']
- enabled values: ['Once', 'Continuous', 'Disabled']
- Cd, Hdd and None found in target values
- Once and Disabled found in enabled values
- Boot from Cd override enabled successfully
- Boot override disabled successfully
System power actions
- ComputerSystem.Reset action found
- Allowed values: ['On', 'ForceOff', 'GracefulShutdown', 'GracefulRestart', 'ForceRestart', 'Nmi', 'PowerCycle']
- Compute reset actions check successful
Redfish endpoint: 10.20.20.11
- ChassisType: Rack
- Model: Cisco UCS
- SerialNumber: SERIAL2
- PowerState: On
- Detected chassis type: Rack
Virtual Media [0]
- Name: Virtual CD
- Inserted: False
- MediaTypes: ['CD', 'DVD']
- ConnectedVia: NotConnected
- State: Disabled
- Health: OK
Virtual media test
- filename to be uploaded to web server: image.iso
Creating file in local web server: image.iso
- url: http://10.50.50.50:8080/image.iso
- virtual media inserted [id:0]
- virtual media mapped
- virtual media ejected
Deleting file in local web server: image.iso
- web server file deleted
Boot settings
- boot source override enabled: Once
- boot source override target: Hdd
- target values: ['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags']
- enabled values: ['Once', 'Continuous', 'Disabled']
- Cd, Hdd and None found in target values
- Once and Disabled found in enabled values
- Boot from Cd override enabled successfully
- Boot override disabled successfully
System power actions
- ComputerSystem.Reset action found
- Allowed values: ['On', 'ForceOff', 'GracefulShutdown', 'GracefulRestart', 'ForceRestart', 'Nmi', 'PowerCycle']
- Compute reset actions check successful
Redfish endpoint: 10.20.20.12
- ChassisType: Rack
- Model: Cisco UCS
- SerialNumber: SERIAL3
- PowerState: On
- Detected chassis type: Rack
Virtual Media [0]
- Name: Virtual CD
- Inserted: False
- MediaTypes: ['CD', 'DVD']
- ConnectedVia: NotConnected
- State: Disabled
- Health: OK
Virtual media test
- filename to be uploaded to web server: image.iso
Creating file in local web server: image.iso
- url: http://10.50.50.50:8080/image.iso
- virtual media inserted [id:0]
- virtual media mapped
- virtual media ejected
Deleting file in local web server: image.iso
- web server file deleted
Boot settings
- boot source override enabled: Once
- boot source override target: Hdd
- target values: ['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags']
- enabled values: ['Once', 'Continuous', 'Disabled']
- Cd, Hdd and None found in target values
- Once and Disabled found in enabled values
- Boot from Cd override enabled successfully
- Boot override disabled successfully
System power actions
- ComputerSystem.Reset action found
- Allowed values: ['On', 'ForceOff', 'GracefulShutdown', 'GracefulRestart', 'ForceRestart', 'Nmi', 'PowerCycle']
- Compute reset actions check successful

Checking cluster fqdn resolution
Cluster FQDNs resolved correctly

Cluster Data
------------
{
    "name": "bm1",
    "openshift_version": "4.18.9",
    "base_dns_domain": "ocp.domain.com",
    "ssh_public_key": "...",
    "cpu_architecture": "x86_64",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "high_availability_mode": "Full",
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com",
    "network_type": "Cilium",
    "disk_encryption": {
        "enable_on": "none",
        "mode": "tpmv2"
    },
    "pull_secret": "..."
}

Infra Data
----------
{
    "cpu_architecture": "x86_64",
    "openshift_version": "4.18.9",
    "proxy": {
        "http_proxy": "http://proxy.domain.com:80",
        "https_proxy": "http://proxy.domain.com:80",
        "no_proxy": "domain.com"
    },
    "ssh_authorized_key": "...",
    "static_network_config": [
        {
            "mac_interface_map": [
                {
                    "logical_nic_name": "eno7",
                    "mac_address": "aa:aa:aa:aa:aa:aa"
                },
                {
                    "logical_nic_name": "eno8",
                    "mac_address": "bb:bb:bb:bb:bb:bb"
                }
            ],
            "network_yaml": "interfaces:\r\n- name: eno7\r\n  type: ethernet\r\n  state: up\r\n- name: eno8\r\n  type: ethernet\r\n  state: up\r\n- name: bond1\r\n  type: bond\r\n  state: up\r\n  link-aggregation:\r\n    mode: 802.3ad\r\n    options:\r\n      lacp_rate: slow\r\n    port:\r\n    - eno7\r\n    - eno8\r\n- name: bond1.666\r\n  type: vlan\r\n  state: up\r\n  vlan:\r\n    base-iface: bond1\r\n    id: 666\r\n  ipv4:\r\n    address:\r\n    - ip: 10.10.10.10\r\n      prefix-length: 28\r\n    dhcp: false\r\n    enabled: true\r\nroutes:\r\n  config:\r\n  - destination: 0.0.0.0/0\r\n    next-hop-address: 10.10.10.254\r\n    next-hop-interface: bond1.666\r\ndns-resolver:\r\n  config:\r\n    search:\r\n    - domain.com\r\n    server:\r\n    - 100.100.50.100"
        },
        {
            "mac_interface_map": [
                {
                    "logical_nic_name": "eno7",
                    "mac_address": "aa:aa:aa:aa:aa:aa"
                },
                {
                    "logical_nic_name": "eno8",
                    "mac_address": "bb:bb:bb:bb:bb:bb"
                }
            ],
            "network_yaml": "interfaces:\r\n- name: eno7\r\n  type: ethernet\r\n  state: up\r\n- name: eno8\r\n  type: ethernet\r\n  state: up\r\n- name: bond1\r\n  type: bond\r\n  state: up\r\n  link-aggregation:\r\n    mode: 802.3ad\r\n    options:\r\n      lacp_rate: slow\r\n    port:\r\n    - eno7\r\n    - eno8\r\n- name: bond1.666\r\n  type: vlan\r\n  state: up\r\n  vlan:\r\n    base-iface: bond1\r\n    id: 666\r\n  ipv4:\r\n    address:\r\n    - ip: 10.10.10.11\r\n      prefix-length: 28\r\n    dhcp: false\r\n    enabled: true\r\nroutes:\r\n  config:\r\n  - destination: 0.0.0.0/0\r\n    next-hop-address: 10.10.10.254\r\n    next-hop-interface: bond1.666\r\ndns-resolver:\r\n  config:\r\n    search:\r\n    - domain.com\r\n    server:\r\n    - 100.100.50.100"
        },
        {
            "mac_interface_map": [
                {
                    "logical_nic_name": "eno7",
                    "mac_address": "aa:aa:aa:aa:aa:aa"
                },
                {
                    "logical_nic_name": "eno8",
                    "mac_address": "bb:bb:bb:bb:bb:bb"
                }
            ],
            "network_yaml": "interfaces:\r\n- name: eno7\r\n  type: ethernet\r\n  state: up\r\n- name: eno8\r\n  type: ethernet\r\n  state: up\r\n- name: bond1\r\n  type: bond\r\n  state: up\r\n  link-aggregation:\r\n    mode: 802.3ad\r\n    options:\r\n      lacp_rate: slow\r\n    port:\r\n    - eno7\r\n    - eno8\r\n- name: bond1.666\r\n  type: vlan\r\n  state: up\r\n  vlan:\r\n    base-iface: bond1\r\n    id: 666\r\n  ipv4:\r\n    address:\r\n    - ip: 10.10.10.12\r\n      prefix-length: 28\r\n    dhcp: false\r\n    enabled: true\r\nroutes:\r\n  config:\r\n  - destination: 0.0.0.0/0\r\n    next-hop-address: 10.10.10.254\r\n    next-hop-interface: bond1.666\r\ndns-resolver:\r\n  config:\r\n    search:\r\n    - domain.com\r\n    server:\r\n    - 100.100.50.100"
        }
    ],
    "additional_trust_bundle": "",
    "image_type": "full-iso",
    "name": "bm1_infra-env",
    "pull_secret": "..."
}
Cluster created: bm1 [cluster-id]
Cluster install config cni patched: Cilium
Infra created: infra-id
Manifest created: ...

Download ISO
------------
- url: https://.../full.iso
- ssl verify: True
- timeout: 600
- target filename: /tmp/cluster-id.iso

Redfish vmedia mapping created successfuly: 10.20.20.10
Redfish boot source set to cd successful: 10.20.20.10
Power cycle: 10.20.20.10
Server booted: 10.20.20.10
Redfish vmedia mapping created successfuly: 10.20.20.11
Redfish boot source set to cd successful: 10.20.20.11
Power cycle: 10.20.20.11
Server booted: 10.20.20.11
Redfish vmedia mapping created successfuly: 10.20.20.12
Redfish boot source set to cd successful: 10.20.20.12
Power cycle: 10.20.20.12
Server booted: 10.20.20.12
Wait for all the servers discovered...
Change hostnames and roles
- Server [10.20.20.10] hostname [bm1-1] role [auto-assign]
- Server [10.20.20.11] hostname [bm1-2] role [auto-assign]
- Server [10.20.20.12] hostname [bm1-3] role [auto-assign]
REST API successful
Update ntp [ntp.domain.com]
REST API successful
Update api 10.10.10.100 and ingress vip 10.10.10.101
REST API successful
Wait for cluster ready to be installed...
Start installation request...
Wait for installation started [cluster-id]...
Status changed to preparing-for-installation
Status changed to installing
Cluster reached desired state: installing
Changing servers to boot from hdd with optional vmedia eject
- 10.20.20.10
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful
- 10.20.20.11
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful
- 10.20.20.12
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful

Host 10.20.20.10 status changed to installing

Host 10.20.20.11 status changed to installing

Host 10.20.20.12 status changed to installing

Host 10.20.20.10 status changed to installing-in-progress

Host 10.20.20.12 status changed to installing-in-progress

Host 10.20.20.11 status changed to installing-in-progress

Host 10.20.20.11 status changed to installed

Host 10.20.20.10 status changed to installed

Host 10.20.20.12 status changed to installed

Installation finished...
Redfish vmedia eject successful: 10.20.20.10
Redfish vmedia eject successful: 10.20.20.11
Redfish vmedia eject successful: 10.20.20.12
Collecting cluster information...

Cluster console access
----------------------
URL      : https://console-openshift-console.apps.bm1.ocp.domain.com
Username : kubeadmin
Password : ...


Kubeconfig
----------

apiVersion: v1
clusters:
- cluster:
    server: https://api.bm1.ocp.domain.com:6443
  name: bm1
contexts:
- context:
    cluster: bm1
    user: admin
  name: admin
current-context: admin
kind: Config
preferences: {}
users:
- name: admin

Create ocp connector: bm1 [kubeconfig:/tmp/cluster-id.kubeconfig] [domain:None]
Ocp connector created
Kubeadmin updated
SSH public key updated
SSH access configured in connector
Helm and virtctl access configured in connector
Check ssh access...
Prepare kubeconfig...
Kubeconfig upload successful
Kubeconfig chmod successful
Required /etc/hosts entries
10.10.10.100	api.bm1.ocp.domain.com
10.10.10.101	oauth-openshift.apps.bm1.ocp.domain.com
10.10.10.101	console-openshift-console.apps.bm1.ocp.domain.com
10.10.10.101	grafana-openshift-monitoring.apps.bm1.ocp.domain.com
10.10.10.101	thanos-querier-openshift-monitoring.apps.bm1.ocp.domain.com
10.10.10.101	prometheus-k8s-openshift-monitoring.apps.bm1.ocp.domain.com
10.10.10.101	alertmanager-main-openshift-monitoring.apps.bm1.ocp.domain.com
10.10.10.101	hyperconverged-cluster-cli-download-openshift-cnv.apps.bm1.ocp.domain.com
OpenShift bare metal installation completed successfully
Management ip [10.10.10.10] information saved

Cluster configuration...
------------------------
- kubernetes handler ready
- management node ssh handler ready
- directory with files to apply not found
Run tasks...

Run command: oc get node
------------------------
NAME    STATUS   ROLES                         AGE   VERSION
bm1-1   Ready    control-plane,master,worker   54m   v1.31.7
bm1-2   Ready    control-plane,master,worker   58m   v1.31.7
bm1-3   Ready    control-plane,master,worker   26m   v1.31.7


Task cli bashrc
---------------
{
    "enabled": true,
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com"
}
Download /var/home/core/.bashrc

# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

unset rc

export HTTP_PROXY=http://proxy.domain.com:80
export HTTPS_PROXY=http://proxy.domain.com:80
export NO_PROXY=domain.com


Upload /var/home/core/.bashrc
.bashrc uploaded with proxy settings

Task cli cilium
---------------
{
    "enabled": true,
    "version_url": "https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt",
    "version": "v0.18.6",
    "download_url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz"
}

OpenShift Cluster
-----------------
- cluster: bm1
- api [/home/user/.itool/ocp-clusters/bm1/kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:/home/user/.itool/ocp-clusters/bm1/ssh.pub]: ok
- management node [10.10.10.10] [key:/home/user/.itool/ocp-clusters/bm1/ssh.pub]: ok
- cli cilium: not found

Downloading cilium binary from https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz
Uploading cilium binary to cluster management node
Unpack
Change file flags
Cilium binary ready to be used
cilium-cli: v0.18.6 compiled with go1.24.5 on linux/amd64
cilium image (default): v1.18.0
cilium image (stable): v1.18.2
cilium image (running): unknown. Unable to obtain cilium version. Reason: release: not found


Task cli hubble
---------------
{
    "enabled": true,
    "version_url": "https://raw.githubusercontent.com/cilium/hubble/main/stable.txt",
    "version": "v1.18.0",
    "download_url": "https://github.com/cilium/hubble/releases/download/v1.18.0/hubble-linux-amd64.tar.gz"
}

OpenShift Cluster
-----------------
- cluster: bm1
- api [/home/user/.itool/ocp-clusters/bm1/kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:/home/user/.itool/ocp-clusters/bm1/ssh.pub]: ok
- management node [10.10.10.10] [key:/home/user/.itool/ocp-clusters/bm1/ssh.pub]: ok
- cli hubble: not found

Downloading hubble binary from https://github.com/cilium/hubble/releases/download/v1.18.0/hubble-linux-amd64.tar.gz
Uploading hubble binary to cluster management node
Unpack
Change file flags
Hubble binary ready to be used
hubble v1.18.0@HEAD-766e8c9 compiled with go1.24.5 on linux/amd64


Task cli helm
-------------
{
    "enabled": true,
    "version_url": "https://get.helm.sh/helm-latest-version",
    "version": "v3.19.0",
    "download_url": "https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz"
}

OpenShift Cluster
-----------------
- cluster: bm1
- api [/home/user/.itool/ocp-clusters/bm1/kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:/home/user/.itool/ocp-clusters/bm1/ssh.pub]: ok
- management node [10.10.10.10] [key:/home/user/.itool/ocp-clusters/bm1/ssh.pub]: ok
- cli helm: not found

Downloading helm binary from https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz
Uploading helm binary to cluster management node
Unpack
Copy helm to /usr/local/bin
Remove local files
Change file flags
Helm binary ready to be used
version.BuildInfo{Version:"v3.19.0", GitCommit:"3d8990f0836691f0229297773f3524598f46bda6", GitTreeState:"clean", GoVersion:"go1.24.7"}

Task identity
-------------
{
    "cluster": "bm1",
    "admin": [
        "__ALL__"
    ],
    "provider": "custom",
    "htpasswd": "..."
}

OpenShift Cluster
-----------------
- cluster: bm1
- api [/home/user/.itool/ocp-clusters/bm1/kubeconfig]: ok
- dns resolution: ok

Secret openshift-config/htpass-secret created
OAuth updated with htpasswd
Add username aaa to cluster admins group
Add username bbb to cluster admins group

Completed tasks
- secret configured
- OAuth updated
- cluster admins updated
- identity provider configured

Task ssh
--------
{
    "cluster": "bm1",
    "keys": [
        "..."
    ]
}

OpenShift Cluster
-----------------
- cluster: bm1
- api [/home/user/.itool/ocp-clusters/bm1/kubeconfig]: ok
- dns resolution: ok

Wait for machine config pool update...
- master
- worker

Completed tasks
- SSH keys added

Run command: cilium status -n cilium
------------------------------------
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 3, Ready: 3/3, Available: 3/3
DaemonSet              cilium-envoy             Desired: 3, Ready: 3/3, Available: 3/3
Deployment             cilium-operator          Desired: 2, Ready: 2/2, Available: 2/2
Containers:            cilium                   Running: 3
                       cilium-envoy             Running: 3
                       cilium-operator          Running: 2
                       clustermesh-apiserver    
                       hubble-relay             
Cluster Pods:          112/112 managed by Cilium

Run command: cilium config view -n cilium
-----------------------------------------
...
```