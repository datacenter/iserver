
# OpenShift Container Platform (OCP)

## Create OCP Cluster in vCenter

Example:

```
# iserver create ocp cluster .\samples\ocp\cluster\vcenter\devel
```

where the directory must contain cluster definition and pull secret. That's all you need to do.

The rest of document explains what is happening once you execute the command and how cluster definition files are used.

Workflow follows [vsphere-ipi installation procedure](https://docs.openshift.com/container-platform/4.13/installing/installing_vsphere/installing-vsphere-installer-provisioned.html)

### Step 1: Create installer virtual machine

- create installer virtual machine in vcenter following the user-defined cluster settings

Example: vcenter settings

```
vcenter:
  name: vc-iks-kali-eu-spdc.cisco.com
  ip: 10.58.29.66
  port: 443
  username: administrator@vsphere.local
  password: whatever
  datacenter: k8s-DC
  datastore: EU-SPDC-k8s-Datastore-WNAS
  cluster: k8s-racks
  folder: OCP-Devel
  network: vk8s_1
```

Example: installer virtual machine settings

```
installer:
  ks:
    folder: linux-ks
  iso:
    destination: linux-iso/Fedora-Server-dvd-x86_64-36-1.5.iso
  vm:
    name: ocp-devel-installer
    cpu: 1
    memory: 2048
    disk:
      size: 50
    ip: 10.58.24.161
    username: root
    password: cisco
```

- iso image can be pre-uploaded to vcenter and iso.destination defines the name of the iso file
- if iso.source is defined and iso.destination does not exist, workflow will upload local iso file to vcenter
- virtual machine is created from iso with generated kickstart file mounted as cdrom device
- workflow waits until ssh access to virtual machine.

Example: create workflow output

```
Input parameters verification...
vsphere-ipi ocp creation workflow...
Selecting the first available host: esx71.emea-sp.cisco.com
Virtual Machine created: ocp-devel-installer
Cdrom added to virtual machine
Cdrom added to virtual machine
The current powerState is: poweredOff
Virtual Machine powered on: ocp-devel-installer
Wait for SSH access with 3600 seconds timeout
```

![OcpVcenterInstaller](images/ocp_vcenter_installer.png)

### Step 2: Prepare installer virtual machine

The starting point of this step is fresh-installed Linux VM that needs to be further configured
- load necessary system packages
- prepare dhcpd configuration and start dhcpd
- prepare dns configuration and start named
- generate ssh key (ed25519) for cluster node SSH access

Note: dhcpd and named configuration files are generated based on user input

```
dns:
  managed: True
  forwarders: 144.254.71.184
```

```
dhcp:
  subnet: 10.58.24.160/28
  gateway: 10.58.24.174
  range: 10.58.24.164-10.58.24.172
  dns:
    servers: 144.254.71.184
    domain: cisco.com
  ntp:
    servers: 144.254.15.78
    timezone: Europe/Rome
```

```
ocp:
  name: Milan-Kali-Devel
  cluster:
    domain: ocp.lan
    api_vip: 10.58.24.162
    ingress_vip: 10.58.24.163
```

Generated /etc/dhcp/dhcpd.conf

```
authoritative;
ddns-update-style interim;
allow booting;
allow bootp;
allow unknown-clients;
ignore client-updates;
default-lease-time 14400;
max-lease-time 14400;

subnet 10.58.24.160 netmask 255.255.255.240 {
    range                           10.58.24.164 10.58.24.172;
    option routers                  10.58.24.174;
    option subnet-mask              255.255.255.240;
    option domain-name              "ocp.lan";
    option domain-name-servers      10.58.24.161;
    option ntp-servers              144.254.15.78;
}
```

Generated /etc/named.conf

```
options {
    listen-on port 53 { 127.0.0.1; 10.58.24.161; };
    directory       "/var/named";
    dump-file       "/var/named/data/cache_dump.db";
    statistics-file "/var/named/data/named_stats.txt";
    memstatistics-file "/var/named/data/named_mem_stats.txt";
    recursing-file  "/var/named/data/named.recursing";
    secroots-file   "/var/named/data/named.secroots";
    allow-query     { localhost; 10.58.24.160/28; };
    recursion yes;

    dnssec-enable no;
    dnssec-validation no;

    # Using Google DNS
    forwarders {
        144.254.71.184;
    };

    /* Path to ISC DLV key */
    bindkeys-file "/etc/named.root.key";

    managed-keys-directory "/var/named/dynamic";

    pid-file "/run/named/named.pid";
    session-keyfile "/run/named/session.key";
};

logging {
    channel default_debug {
            file "data/named.run";
            severity dynamic;
    };
};

zone "." IN {
    type hint;
    file "named.ca";
};

zone "ocp.lan" {
    type master;
    file "/etc/named/zones/db.ocp.lan";
};

zone "24.58.10.in-addr.arpa" {
    type master;
    file "/etc/named/zones/db.reverse";
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
```

Generated  /etc/named/zones/db.ocp.lan
```
$TTL    604800
@       IN      SOA     ocp.lan. root.ocp.lan (
      2023071201     ; Serial
             604800     ; Refresh
              86400     ; Retry
            2419200     ; Expire
             604800     ; Minimum
)
                 NS     ocp.lan.

ocp.lan.         IN    A    10.58.24.161
api.devel.ocp.lan.        IN    A    10.58.24.162
*.apps.devel.ocp.lan.     IN    A    10.58.24.163
```

### Step 3: Prepare openshift installer binaries

- openshift installer downloaded from https://mirror.openshift.com/pub/openshift-v4/amd64/clients/ocp
- openshift release controller in user input
- oc binary downloaded from the same location

```
ocp:
  release: 4.11.3
  source: web
```

- upload tarballs to installer virtual machine
- unpack
- move oc to /usr/local/bin

```
[root@ocp-devel-installer ~]# ls /usr/local/bin/
kubectl  oc
```

### Step 4: Prepare config.yaml

- OCP configuration yaml file generated based on user input.

```
ocp:
  name: Milan-Kali-Devel
  installation: vsphere-ipi
  release: 4.11.3
  source: web
  cluster:
    name: devel
    domain: ocp.lan
    api_vip: 10.58.24.162
    ingress_vip: 10.58.24.163
    master:
      hyperthreading: True
      replicas: 3
      cpu: 4
      memory: 16384
      disk:
        size: 120
    worker:
      hyperthreading: True
      replicas: 3
      cpu: 4
      memory: 8192
      disk:
        size: 120
```

- with optional http proxy settings

```
proxy:
  enabled: True
  http: http://proxy.esl.cisco.com:80
  https: http://proxy.esl.cisco.com:80
```

- with optional additional ssh key

```
ssh:
  - 'ssh-ed25519 AAAA... user@host'
```

- embed user provided pull-secret into configuration yaml
- follow user provided cni settings

Example: OpenShiftSDN

```
cni:
  type: OpenShiftSDN
  v4cidr: 10.128.0.0/14
  v4hostPrefix: 23
  v4serviceNetwork: 172.30.0.0/16
```

Example: Calico with BGP settings

```
cni:
  type: Calico
  v4cidr: 10.128.0.0/14
  v4hostPrefix: 23
  v4serviceNetwork: 172.30.0.0/16

bgp:
  local_as: 65321
  remote_as: 50000
  peer:
  - 10.58.24.108
  - 10.58.24.109
  mesh: true
  external_ips:
  - 172.70.66.0/24
  - 172.70.66.66/32,1:128
  - 172.70.66.67/32,1:128
```

Example: generated config.yaml

```
apiVersion: v1
baseDomain: ocp.lan
proxy:
  httpProxy: http://proxy.esl.cisco.com:80
  httpsProxy: http://proxy.esl.cisco.com:80
  noProxy: localhost,.ocp.lan,vc-iks-kali-eu-spdc.cisco.com,10.58.29.66,esx71.emea-sp.cisco.com,esx72.emea-sp.cisco.com,10.58.24.161,10.58.24.162,10.58.24.163,10.58.24.164,10.58.24.165,10.58.24.166,10.58.24.167,10.58.24.168,10.58.24.169,10.58.24.170,10.58.24.171,10.58.24.172
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 3
  platform:
    vsphere:
      cpus: 4
      coresPerSocket: 2
      memoryMB: 8192
      osDisk:
        diskSizeGB: 120
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
  platform:
    vsphere:
      cpus: 4
      coresPerSocket: 2
      memoryMB: 16384
      osDisk:
        diskSizeGB: 120
metadata:
  name: devel
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.58.24.160/28
  networkType: OpenShiftSDN
  serviceNetwork:
  - 172.30.0.0/16
platform:
  vsphere:
    vcenter: vc-iks-kali-eu-spdc.cisco.com
    username: administrator@vsphere.local
    password: "!Cisc0_123"
    datacenter: k8s-DC
    defaultDatastore: EU-SPDC-k8s-Datastore-WNAS
    folder: /k8s-DC/vm/OCP-Devel
    diskType: thin
    network: vk8s_1
    cluster: k8s-racks
    apiVIP: 10.58.24.162
    ingressVIP: 10.58.24.163
fips: false
pullSecret: '{"auths":{"cloud.openshift.com":{"auth":"...","email":"akaliwod@cisco.com"}}}'
sshKey: 'ssh-ed25519 AAAA... root@ocp-devel-installer'
```
### Step 5: Calico CNI

If Calico CNI is defined:
- download calico manifests from https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests
- download calicoctl
- optionally prepare bgp.yaml configuration

Version and calicoctl is user-controlled and follows the default settings i.e.

```
calico:
  version: 3.20
  calicoctl: https://github.com/projectcalico/calicoctl/releases/download/v3.20.6/calicoctl-linux-amd64
```

Optional http proxy settings are used during download.

### Step 6: Add vCenter root CA certificates to your system trust

- download certification bundle from vcenter
- unzip
- copy relevant files to /etc/pki/ca-trust/source/anchors
- update CA trust settings

### Step 7: Run openshift-install

- execute openshift-install command on the installer virtual machine using generated config.yaml
- wait until installer finishes

```
DEBUG Cluster is initialized
INFO Waiting up to 10m0s (until 9:09PM) for the openshift-console route to be created...
DEBUG Route found in openshift-console namespace: console
DEBUG OpenShift console route is admitted
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run
INFO     export KUBECONFIG=/root/install/auth/kubeconfig
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.devel.ocp.lan
INFO Login to the console with user: "kubeadmin", and password: "5JZq4-RIaJ9-zQ2Ee-EkcjX"
DEBUG Time elapsed per stage:
DEBUG      pre-bootstrap: 38s
DEBUG          bootstrap: 31s
DEBUG             master: 56s
DEBUG Bootstrap Complete: 17m29s
DEBUG                API: 1m59s
DEBUG  Bootstrap Destroy: 40s
DEBUG  Cluster Operators: 13m23s
DEBUG            Console: 1s
INFO Time elapsed: 35m41s
```

### Step 8: Prepare kubeconfig

- prepare kubeconfig binary in /usr/local/bin
- make sure KUBECONFIG env variable is configured upon ssh login (/root/.bashrc)

```
[root@ocp-devel-installer ~]# kubectl get ns
NAME                                               STATUS   AGE
default                                            Active   56m
kube-node-lease                                    Active   56m
kube-public                                        Active   56m
kube-system                                        Active   56m
openshift                                          Active   44m
...
```

### Step 9: Check OCP state

- execute script that checks OCP cluster state using kubectl command
- expected state is that all nodes are in Ready state

```
NAME                       STATUS   ROLES    AGE     VERSION
devel-fnrrp-master-0       Ready    master   24m     v1.24.0+b62823b
devel-fnrrp-master-1       Ready    master   24m     v1.24.0+b62823b
devel-fnrrp-master-2       Ready    master   24m     v1.24.0+b62823b
devel-fnrrp-worker-db2jd   Ready    worker   9m21s   v1.24.0+b62823b
devel-fnrrp-worker-fvwck   Ready    worker   9m13s   v1.24.0+b62823b
devel-fnrrp-worker-tprng   Ready    worker   9m15s   v1.24.0+b62823b
```

![OcpVcenterFolder](images/ocp_vcenter_folder.png)

### Step 10: iserver tasks

- copy kubeconfig
- copy kubeadmin
- create ocp cluster settings

```
# iserver get ocp cluster --cluster Milan-Kali-Devel --view kc --verify
|
+------------------+-------------+---------+--------------+------------+-------------------+--------------+--------------+---------+
| Name             | Type        | Release | CNI          | Kubeconfig | API FQDN          | API VIP      | API DNS      | K8s API |
+------------------+-------------+---------+--------------+------------+-------------------+--------------+--------------+---------+
| Milan-Kali-Devel | vsphere-ipi | 4.11.3  | OpenShiftSDN | ✓          | api.devel.ocp.lan | 10.58.24.162 | 10.58.24.162 | ✓      |
+------------------+-------------+---------+--------------+------------+-------------------+--------------+--------------+---------+
```

```
# iserver get ocp cluster --cluster Milan-Kali-Devel --view console
|
+------------------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
| Name             | Console URL                                          | Expected Resolved IP | DNS Resolved IP | Authentication FQDN                | Expected Resolved IP | DNS Resolved IP | Username  | Password                |
+------------------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
| Milan-Kali-Devel | https://console-openshift-console.apps.devel.ocp.lan | 10.58.24.163         | 10.58.24.163    | oauth-openshift.apps.devel.ocp.lan | 10.58.24.163         | 10.58.24.163    | kubeadmin | 5JZq4-RIaJ9-zQ2Ee-EkcjX |
+------------------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
```

Note:
- depending on the dns setup, you may need to configure local dns resolution

Example: /etc/hosts

```
10.58.24.162	api.devel.ocp.lan
10.58.24.163    oauth-openshift.apps.devel.ocp.lan
10.58.24.163    console-openshift-console.apps.devel.ocp.lan
```

![OcpVcenterLogin](images/ocp_vcenter_login.png)

![OcpVcenterConsole](images/ocp_vcenter_console.png)

[[Back]](./README.md)