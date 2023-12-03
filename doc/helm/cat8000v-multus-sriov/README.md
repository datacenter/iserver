# Helm: Cat8000v with mix of Multus and SR-IOV Interface

This document extends [basic cat8000v management](../cat8000v-mgmt/README.md) with multus interface

Helm package sources are [here](../../../samples/ocp/helm/cat8000v-multus-sriov/).

## Multus Configuration

```
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  namespace: {{ .Release.Namespace }}
  name: {{ .Release.Name }}-nic1
spec:
  config: '{
            "cniVersion": "0.3.1",
            "name": "{{ .Release.Name }}-net1",
            "type": "macvlan",
            "master": "{{ .Values.multus.nic1.master }}",
            "mode": "bridge",
            "ipam": {
              "type": "static",
              "addresses": [
                {
                  "address": "{{ .Values.multus.nic1.ip }}/{{ .Values.multus.nic1.prefix }}"
                }
              ]
            }
          }'
```

## SR-IOV Configuration

Note:
- sriov network node policy custom resource is expected to be pre-configured
- it is referred inside sriov network definition using resourceName

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
    ip address {{ .Values.multus.nic1.ip }} {{ .Values.multus.nic1.netmask }}
    no shutdown
!
interface GigabitEthernet3
    ip address {{ .Values.sriov.nic2.ip }} {{ .Values.sriov.nic2.netmask }}
    no shutdown
!
ip route 0.0.0.0 0.0.0.0 {{ .Values.sriov.nic2.gateway }}
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
$ iserver create helm release --chart cat8000v-multus-sriov --name my-c8kv-multus-sriov
Cluster: Milan-BM1
Day0 generation done via tools
Day0 configuration uploaded: /tmp/303afc16-994a-4870-bcfb-bc5d1ab1ce2e/iosxe_config.txt => /tmp/3162c606-d3dd-4171-840e-9e213767a9bb/iosxe_config.txt
Generate iso: genisoimage -r -o /tmp/3162c606-d3dd-4171-840e-9e213767a9bb/config.iso /tmp/3162c606-d3dd-4171-840e-9e213767a9bb/iosxe_config.txt
I: -input-charset not specified, using utf-8 (detected in locale settings)
Total translation table size: 0
Total rockridge attributes bytes: 257
Total directory bytes: 0
Path table size(bytes): 10
Max brk space used 0
176 extents written (0 MB)
Day0 iso generated: /tmp/3162c606-d3dd-4171-840e-9e213767a9bb/config.iso
Day0 downloaded: /tmp/3162c606-d3dd-4171-840e-9e213767a9bb/config.iso => /tmp/303afc16-994a-4870-bcfb-bc5d1ab1ce2e/config.iso
Day0 uploaded for virctl upload: /tmp/303afc16-994a-4870-bcfb-bc5d1ab1ce2e/config.iso => /tmp/config.iso
Data volume created: default/my-c8kv-multus-sriov-day0
Wait till pvc default/my-c8kv-multus-sriov-day0 reaches bound state
Upload iso to data volume: virtctl image-upload dv my-c8kv-multus-sriov-day0 --no-create --insecure --image-path /tmp/config.iso
Using existing PVC default/my-c8kv-multus-sriov-day0
Uploading data to https://cdi-uploadproxy-openshift-cnv.apps.ocp-bm1.ocp.lan

 352.00 KiB / 352.00 KiB [==========================================] 100.00% 0s

Uploading data completed successfully, waiting for processing to complete, you can hit ctrl-c without interrupting the progress
Processing completed successfully
Uploading /tmp/config.iso completed successfully
Upload iso to data volume completed: default/my-c8kv-multus-sriov-day0
Helm release created

+-----------+----------------------+----------+-----------------------------------------+----------+-----------------------------+-------------+--------------------+---------------------------+
| Namespace | Name                 | Revision | Updated                                 | Status   | Chart - Version             | App Version | Day0 PVC Namespace | Day0 PVC Name             |
+-----------+----------------------+----------+-----------------------------------------+----------+-----------------------------+-------------+--------------------+---------------------------+
| default   | my-c8kv-multus-sriov | 1        | 2023-10-10 09:25:03.301374295 +0000 UTC | deployed | cat8000v-multus-sriov-1.0.0 | 1.0.0       | default            | my-c8kv-multus-sriov-day0 |
+-----------+----------------------+----------+-----------------------------------------+----------+-----------------------------+-------------+--------------------+---------------------------+
```

## VNF state

```
$ iserver get k8s vm --name my-c8kv-multus-sriov -v all

Virtual Machine [#1]
--------------------

+------------------------------+-----------------------------------+-----+--------+-----------+----------------+---------+-------+---------+-----+
| VM                           | Label                             | CPU | Memory | Disks     | Interfaces     | Created | Ready | Status  | Age |
+------------------------------+-----------------------------------+-----+--------+-----------+----------------+---------+-------+---------+-----+
| default/my-c8kv-multus-sriov | app:my-c8kv-multus-sriov          | 1   | None   | rootdisk  | default (masq) | ✓       | ✓     | Running | 4m  |
|                              | app.kubernetes.io/managed-by:Helm |     |        | cdromdisk | nic1           |         |       |         |     |
|                              |                                   |     |        |           | nic2 (sriov)   |         |       |         |     |
+------------------------------+-----------------------------------+-----+--------+-----------+----------------+---------+-------+---------+-----+

Virtual Machine - Data Volume [#1]
----------------------------------

+------------------------------+-----------+---------------------------------------+------------+----------------------------+
| VM                           | Disks     | DV Name                               | DV Storage | DV Source                  |
+------------------------------+-----------+---------------------------------------+------------+----------------------------+
| default/my-c8kv-multus-sriov | rootdisk  | default/vm-my-c8kv-multus-sriov-image | 10Gi       | pvc:default:cat8000v-image |
|                              | cdromdisk |                                       |            |                            |
+------------------------------+-----------+---------------------------------------+------------+----------------------------+
```

```
$ iserver get k8s vmi --name my-c8kv-multus-sriov -v all

Virtual Machine Instance [#1]
-----------------------------

+------------------------------+-----------------------------------------+---------+-----+--------+---------------------+---------------------+-------+
| VM                           | Label                                   | Node    | CPU | Memory | Disk                | Interface           | State |
+------------------------------+-----------------------------------------+---------+-----+--------+---------------------+---------------------+-------+
| default/my-c8kv-multus-sriov | kubevirt.io/domain:my-c8kv-multus-sriov | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | 10.128.1.210 (masq) | 4m    |
|                              | kubevirt.io/nodeName:ocp-bm1            |         |     |        | cdromdisk/sda - 1Gi | 192.168.10.20       |       |
|                              | special:my-c8kv-multus-sriov            |         |     |        |                     | nic2 (sriov)        |       |
+------------------------------+-----------------------------------------+---------+-----+--------+---------------------+---------------------+-------+

Virtual Machine Instance - PVC [#1]
-----------------------------------

+------------------------------+---------------------+---------------------------------------+
| VM                           | Disk                | PVC                                   |
+------------------------------+---------------------+---------------------------------------+
| default/my-c8kv-multus-sriov | rootdisk/vda - 10Gi | default/vm-my-c8kv-multus-sriov-image |
|                              | cdromdisk/sda - 1Gi | default/my-c8kv-multus-sriov-day0     |
+------------------------------+---------------------+---------------------------------------+

Virtual Machine Instance - Phase Transitions [#1]
-------------------------------------------------

+------------------------------+---------+------------+----------------------+-----+
| VM                           | State   | Phase      | Timestamp            | Age |
+------------------------------+---------+------------+----------------------+-----+
| default/my-c8kv-multus-sriov | Running | Pending    | 2023-10-10T09:25:04Z | 4m  |
|                              |         | Scheduling | 2023-10-10T09:26:06Z |     |
|                              |         | Scheduled  | 2023-10-10T09:26:09Z |     |
|                              |         | Running    | 2023-10-10T09:26:12Z |     |
+------------------------------+---------+------------+----------------------+-----+
```

```
$ iserver get ocp vm --name my-c8kv-multus-sriov -v default -v intf
                                                                      -
OCP VM [#1]
-----------

+------------------------------+---------+-----+--------+---------------------+---------------------+---------+-------+---------+--------------------------------------+---------------+----+-----+
| VM                           | Node    | CPU | Memory | Disks               | Interfaces          | State   | Ready | Failure | Service                              | NodePort      | LM | Age |
+------------------------------+---------+-----+--------+---------------------+---------------------+---------+-------+---------+--------------------------------------+---------------+----+-----+
| default/my-c8kv-multus-sriov | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | 10.128.1.210 (masq) | Running | ✓     | --      | default/my-c8kv-multus-sriov-netconf | 830:31280/TCP | ✗  | 4m  |
|                              |         |     |        | cdromdisk/sda - 1Gi | 192.168.10.20       |         |       |         | default/my-c8kv-multus-sriov-snmp    | 161:30181/UDP |    |     |
|                              |         |     |        |                     | nic2 (sriov)        |         |       |         | default/my-c8kv-multus-sriov-ssh     | 22:30184/TCP  |    |     |
+------------------------------+---------+-----+--------+---------------------+---------------------+---------+-------+---------+--------------------------------------+---------------+----+-----+

Kubernetes Networking
---------------------

+------------------------------+-----------+-------------------+---------------+------+-----+-------+--------+-----------------------------------+----------+----------+--------+-------------+-----+
| VM                           | Interface | MAC               | IP            | Masq | Pod | SRIOV | Multus | Network                           | VLAN Tag | Resource | Policy | Device Type | NIC |
+------------------------------+-----------+-------------------+---------------+------+-----+-------+--------+-----------------------------------+----------+----------+--------+-------------+-----+
| default/my-c8kv-multus-sriov | default   | 02:c5:6d:00:00:3b | 10.128.1.210  | ✓    | ✓   |       |        |                                   |          |          |        |             |     |
|                              | nic1      | 02:c5:6d:00:00:3c | 192.168.10.20 |      |     |       | ✓      | default/my-c8kv-multus-sriov-nic1 |          |          |        |             |     |
|                              | nic2      | 02:c5:6d:00:00:3d |               |      |     | ✓     | ✓      | default/my-c8kv-multus-sriov-nic2 |          |          |        |             |     |
+------------------------------+-----------+-------------------+---------------+------+-----+-------+--------+-----------------------------------+----------+----------+--------+------------
```

## Functional test

```
$ ssh -p 30184 admin@10.58.29.84
Password:

my-c8kv-multus-sriov#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.0.2.2        YES DHCP   up                    up
GigabitEthernet2       192.168.10.20   YES TFTP   up                    up
GigabitEthernet3       15.20.16.15     YES TFTP   up                    up
my-c8kv-multus-sriov#ping 15.20.16.254
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 15.20.16.254, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```
