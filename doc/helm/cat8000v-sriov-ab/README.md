# Helm: Cat8000v with 2x SR-IOV Interfaces

This document extends [basic cat8000v management](../cat8000v-mgmt/README.md) with SR-IOV enabled interface

Helm package sources are [here](../../../samples/ocp/helm/cat8000v-sriov-ab/).

## SR-IOV Configuration

Note:
- sriov network node policy custom resource is expected to be pre-configured
- it is referred inside sriov network definition using resourceName

SR-IOV Node Policy (reference)

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  creationTimestamp: "2023-10-04T14:22:23Z"
  generation: 1
  name: policy-ens3f0-dpdk
  namespace: openshift-sriov-network-operator
  resourceVersion: "163312222"
  uid: c1f5b95b-03c3-4163-992f-ddcee566d20b
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - ens3f0#8-15
  nodeSelector:
    topology.topolvm.io/node: ocp-bm1
  numVfs: 16
  priority: 99
  resourceName: ens3f0dpdk
```

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  creationTimestamp: "2023-10-04T14:22:23Z"
  generation: 1
  name: policy-ens3f1-dpdk
  namespace: openshift-sriov-network-operator
  resourceVersion: "163312222"
  uid: c1f5b95b-03c3-4163-992f-ddcee566d20b
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - ens3f1#8-15
  nodeSelector:
    topology.topolvm.io/node: ocp-bm1
  numVfs: 16
  priority: 99
  resourceName: ens3f1dpdk
```

SR-IOV Network Templates

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: {{ .Release.Name }}-nic1
  namespace: openshift-sriov-network-operator
spec:
  resourceName: {{ .Values.sriov.nic1.policy }}
  networkNamespace: {{ .Release.Namespace }}
  vlan: {{ .Values.sriov.nic1.vlan }}
```

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: {{ .Release.Name }}-nic2
  namespace: openshift-sriov-network-operator
spec:
  resourceName: {{ .Values.sriov.nic2.policy }}
  networkNamespace: {{ .Release.Namespace }}
  vlan: {{ .Values.sriov.nic2.vlan }}
```

## Day0 Configuration

Notes:
- day0 configuration below requires iserver-based helm release deployment that supports day0 automatic generation with variable replacement
- if you want standard helm, make sure you create day0 pvc manually following [procedure](../cat8000v/day0.md) and make sure to adjust the day0 pvc references in vm template


```
hostname {{ .Release.Name }}
ip domain name {{ .Values.day0.domain }}
!
aaa new-model
aaa authentication login default local
aaa authorization exec default local
username {{ .Values.day0.username }} privilege 15 secret {{ .Values.day0.password }}
!
no ip http secure-server
crypto key generate rsa modulus 2048
ip ssh version 2
!
vrf definition Mgmt-intf
 address-family ipv4
 exit-address-family
!
interface GigabitEthernet1
    vrf forwarding Mgmt-intf
    ip address dhcp
    no shutdown
!
interface GigabitEthernet2
    ip address {{ .Values.sriov.nic1.ip }} {{ .Values.sriov.nic1.netmask }}
    no shutdown
!
interface GigabitEthernet3
    ip address {{ .Values.sriov.nic2.ip }} {{ .Values.sriov.nic2.netmask }}
    no shutdown
!
ip route 0.0.0.0 0.0.0.0 {{ .Values.sriov.nic1.gateway }}
!
ip http secure-server
!
restconf
!
netconf-yang
!
snmp-server community public RO
snmp-server manager
!
line con 0
    length 0
line vty 0 4
    length 0
```

## Helm deployment

Option: using iserver (day0 handled automatically)

```
$ iserver create helm release --chart cat8000v-sriov-ab --name my-c8kv-sriov-ab
Cluster: Milan-BM1
Day0 generation done via tools
Day0 configuration uploaded: /tmp/52baaf91-6d06-4414-986a-d4d31160d814/iosxe_config.txt => /tmp/f1042f34-7b45-4d60-afa0-fe769bee5f2c/iosxe_config.txt
Generate iso: genisoimage -r -o /tmp/f1042f34-7b45-4d60-afa0-fe769bee5f2c/config.iso /tmp/f1042f34-7b45-4d60-afa0-fe769bee5f2c/iosxe_config.txt
I: -input-charset not specified, using utf-8 (detected in locale settings)
Total translation table size: 0
Total rockridge attributes bytes: 257
Total directory bytes: 0
Path table size(bytes): 10
Max brk space used 0
176 extents written (0 MB)
Day0 iso generated: /tmp/f1042f34-7b45-4d60-afa0-fe769bee5f2c/config.iso
Day0 downloaded: /tmp/f1042f34-7b45-4d60-afa0-fe769bee5f2c/config.iso => /tmp/52baaf91-6d06-4414-986a-d4d31160d814/config.iso
Day0 uploaded for virctl upload: /tmp/52baaf91-6d06-4414-986a-d4d31160d814/config.iso => /tmp/config.iso
Data volume created: default/my-c8kv-sriov-ab-day0
Wait till pvc default/my-c8kv-sriov-ab-day0 reaches bound state
Upload iso to data volume: virtctl image-upload dv my-c8kv-sriov-ab-day0 --no-create --insecure --image-path /tmp/config.iso
Using existing PVC default/my-c8kv-sriov-ab-day0
Uploading data to https://cdi-uploadproxy-openshift-cnv.apps.ocp-bm1.ocp.lan

 352.00 KiB / 352.00 KiB [==========================================] 100.00% 0s

Uploading data completed successfully, waiting for processing to complete, you can hit ctrl-c without interrupting the progress
Processing completed successfully
Uploading /tmp/config.iso completed successfully
Upload iso to data volume completed: default/my-c8kv-sriov-ab-day0
Helm release created

+-----------+------------------+----------+-----------------------------------------+----------+-------------------------+-------------+--------------------+-----------------------+
| Namespace | Name             | Revision | Updated                                 | Status   | Chart - Version         | App Version | Day0 PVC Namespace | Day0 PVC Name         |
+-----------+------------------+----------+-----------------------------------------+----------+-------------------------+-------------+--------------------+-----------------------+
| default   | my-c8kv-sriov-ab | 1        | 2023-10-10 08:24:43.938398994 +0000 UTC | deployed | cat8000v-sriov-ab-1.0.0 | 1.0.0       | default            | my-c8kv-sriov-ab-day0 |
+-----------+------------------+----------+-----------------------------------------+----------+-------------------------+-------------+--------------------+-----------------------+
```

## VNF state

```
$ iserver get k8s vm --name my-c8kv-sriov-ab -v all

Virtual Machine [#1]
--------------------

+--------------------------+-----------------------------------+-----+--------+-----------+----------------+---------+-------+---------+-----+
| VM                       | Label                             | CPU | Memory | Disks     | Interfaces     | Created | Ready | Status  | Age |
+--------------------------+-----------------------------------+-----+--------+-----------+----------------+---------+-------+---------+-----+
| default/my-c8kv-sriov-ab | app:my-c8kv-sriov-ab              | 1   | None   | rootdisk  | default (masq) | ✓       | ✓     | Running | 1m  |
|                          | app.kubernetes.io/managed-by:Helm |     |        | cdromdisk | nic1 (sriov)   |         |       |         |     |
|                          |                                   |     |        |           | nic2 (sriov)   |         |       |         |     |
+--------------------------+-----------------------------------+-----+--------+-----------+----------------+---------+-------+---------+-----+

Virtual Machine - Data Volume [#1]
----------------------------------

+--------------------------+-----------+-----------------------------------+------------+----------------------------+
| VM                       | Disks     | DV Name                           | DV Storage | DV Source                  |
+--------------------------+-----------+-----------------------------------+------------+----------------------------+
| default/my-c8kv-sriov-ab | rootdisk  | default/vm-my-c8kv-sriov-ab-image | 10Gi       | pvc:default:cat8000v-image |
|                          | cdromdisk |                                   |            |                            |
+--------------------------+-----------+-----------------------------------+------------+----------------------------+
```

```
$ iserver get k8s vmi --name my-c8kv-sriov-ab -v all

Virtual Machine Instance [#1]
-----------------------------

+--------------------------+-------------------------------------+---------+-----+--------+---------------------+---------------------+-------+
| VM                       | Label                               | Node    | CPU | Memory | Disk                | Interface           | State |
+--------------------------+-------------------------------------+---------+-----+--------+---------------------+---------------------+-------+
| default/my-c8kv-sriov-ab | kubevirt.io/domain:my-c8kv-sriov-ab | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | 10.128.1.139 (masq) | 1m    |
|                          | kubevirt.io/nodeName:ocp-bm1        |         |     |        | cdromdisk/sda - 1Gi | nic1 (sriov)        |       |
|                          | special:my-c8kv-sriov-ab            |         |     |        |                     | nic2 (sriov)        |       |
+--------------------------+-------------------------------------+---------+-----+--------+---------------------+---------------------+-------+

Virtual Machine Instance - PVC [#1]
-----------------------------------

+--------------------------+---------------------+-----------------------------------+
| VM                       | Disk                | PVC                               |
+--------------------------+---------------------+-----------------------------------+
| default/my-c8kv-sriov-ab | rootdisk/vda - 10Gi | default/vm-my-c8kv-sriov-ab-image |
|                          | cdromdisk/sda - 1Gi | default/my-c8kv-sriov-ab-day0     |
+--------------------------+---------------------+-----------------------------------+

Virtual Machine Instance - Phase Transitions [#1]
-------------------------------------------------

+--------------------------+---------+------------+----------------------+-----+
| VM                       | State   | Phase      | Timestamp            | Age |
+--------------------------+---------+------------+----------------------+-----+
| default/my-c8kv-sriov-ab | Running | Pending    | 2023-10-10T08:30:45Z | 1m  |
|                          |         | Scheduling | 2023-10-10T08:31:50Z |     |
|                          |         | Scheduled  | 2023-10-10T08:31:53Z |     |
|                          |         | Running    | 2023-10-10T08:31:57Z |     |
+--------------------------+---------+------------+----------------------+-----+
```

```
$ iserver get ocp vm --name my-c8kv-sriov-ab
                                                                      |
OCP VM [#1]
-----------

+--------------------------+---------+-----+--------+---------------------+---------------------+---------+-------+---------+----------------------------------+---------------+----+-----+
| VM                       | Node    | CPU | Memory | Disks               | Interfaces          | State   | Ready | Failure | Service                          | NodePort      | LM | Age |
+--------------------------+---------+-----+--------+---------------------+---------------------+---------+-------+---------+----------------------------------+---------------+----+-----+
| default/my-c8kv-sriov-ab | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | 10.128.1.139 (masq) | Running | ✓     | --      | default/my-c8kv-sriov-ab-netconf | 830:32751/TCP | ✗  | 1m  |
|                          |         |     |        | cdromdisk/sda - 1Gi | nic1 (sriov)        |         |       |         | default/my-c8kv-sriov-ab-snmp    | 161:32320/UDP |    |     |
|                          |         |     |        |                     | nic2 (sriov)        |         |       |         | default/my-c8kv-sriov-ab-ssh     | 22:31111/TCP  |    |     |
+--------------------------+---------+-----+--------+---------------------+---------------------+---------+-------+---------+----------------------------------+---------------+----+-----+
```

```
$ iserver get ocp vm --name my-c8kv-sriov-ab -v intf
                                                                      |
Kubernetes Networking
---------------------

+--------------------------+-----------+-------------------+--------------+------+-----+-------+--------+-----------------------+----------+------------+--------------------+-------------+-----------------+
| VM                       | Interface | MAC               | IP           | Masq | Pod | SRIOV | Multus | Network               | VLAN Tag | Resource   | Policy             | Device Type | NIC             |
+--------------------------+-----------+-------------------+--------------+------+-----+-------+--------+-----------------------+----------+------------+--------------------+-------------+-----------------+
| default/my-c8kv-sriov-ab | default   | 02:c5:6d:00:00:28 | 10.128.1.139 | ✓    | ✓   |       |        |                       |          |            |                    |             |                 |
|                          | nic1      | 02:c5:6d:00:00:29 |              |      |     | ✓     | ✓      | my-c8kv-sriov-ab-nic1 | 808      | ens3f0dpdk | policy-ens3f0-dpdk | vfio-pci    | ['ens3f0#8-15'] |
|                          | nic2      | 02:c5:6d:00:00:2a |              |      |     | ✓     | ✓      | my-c8kv-sriov-ab-nic2 | 807      | ens3f1dpdk | policy-ens3f1-dpdk | vfio-pci    | ['ens3f1#8-15'] |
+--------------------------+-----------+-------------------+--------------+------+-----+-------+--------+-----------------------+----------+------------+--------------------+-------------+-----------------+
```
## Functional test

```
$ ssh -p 31111 admin@10.58.29.84
Password:

my-c8kv-sriov-ab#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.0.2.2        YES DHCP   up                    up
GigabitEthernet2       15.20.16.15     YES TFTP   up                    up
GigabitEthernet3       15.20.17.15     YES TFTP   up                    up
my-c8kv-sriov-ab#ping 15.20.16.254
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 15.20.16.254, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
my-c8kv-sriov-ab#ping 15.20.17.254
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 15.20.17.254, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
```

[Back](../README.md)