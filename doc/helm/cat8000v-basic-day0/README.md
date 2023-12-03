# Helm: Basic Cat8000v deployment

Requirements:
- cat8000v image loaded into pvc ([example](../cat8000v/image.md))

Helm package sources are [here](../../../samples/ocp/helm/cat8000v-basic-day0/).

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
ip http secure-server
!
line con 0
    length 0
line vty 0 4
    length 0
```

## Helm deployment

Option: using helm command (day0 must be prepared offline)

```
$ helm install my-c8kv ./cat8000v-basic -n default
NAME: my-c8kv
LAST DEPLOYED: Fri Oct  6 07:24:33 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

Option: using iserver (day0 handled automatically)

```
# iserver create helm release --chart cat8000v-basic-day0 --name my-c8kv
Cluster: Milan-BM1
Day0 generation done via tools
Day0 iso generated: /tmp/1e358f97-d4c4-41c3-871c-2000b2e39f03/config.iso
Data volume created: default/my-c8kv-day0
Upload iso to data volume completed: default/my-c8kv-day0
Helm release created

+-----------+---------+----------+-----------------------------------------+----------+---------------------------+-------------+--------------------+---------------+
| Namespace | Name    | Revision | Updated                                 | Status   | Chart - Version           | App Version | Day0 PVC Namespace | Day0 PVC Name |
+-----------+---------+----------+-----------------------------------------+----------+---------------------------+-------------+--------------------+---------------+
| default   | my-c8kv | 1        | 2023-10-09 14:25:17.784139086 +0000 UTC | deployed | cat8000v-basic-day0-1.0.0 | 1.0.0       | default            | my-c8kv-day0  |
+-----------+---------+----------+-----------------------------------------+----------+---------------------------+-------------+--------------------+---------------+
```

## VNF State

```
# iserver get k8s vm --name my-c8kv
+-----------------+-----------------------------------+-----+--------+-----------+--------------------------+------------+----------------------------+----------------+---------+-------+---------+-------+
| VM              | Label                             | CPU | Memory | Disks     | DV Name                  | DV Storage | DV Source                  | Interfaces     | Created | Ready | Status  | Age   |
+-----------------+-----------------------------------+-----+--------+-----------+--------------------------+------------+----------------------------+----------------+---------+-------+---------+-------+
| default/my-c8kv | app:my-c8kv                       | 1   | None   | rootdisk  | default/vm-my-c8kv-image | 10Gi       | pvc:default:cat8000v-image | default (masq) | V       | V     | Running | 2h18m |
|                 | app.kubernetes.io/managed-by:Helm |     |        | cdromdisk |                          |            |                            |                |         |       |         |       |
+-----------------+-----------------------------------+-----+--------+-----------+--------------------------+------------+----------------------------+----------------+---------+-------+---------+-------+
```

```
# iserver get k8s vmi --name my-c8kv
+-----------------+------------------------------+---------+-----+--------+---------------------+--------------------------+--------------------+---------+------------+----------------------+-------+
| VM              | Label                        | Node    | CPU | Memory | Disk                | PVC                      | Interface          | State   | Phase      | Timestamp            | Age   |
+-----------------+------------------------------+---------+-----+--------+---------------------+--------------------------+--------------------+---------+------------+----------------------+-------+
| default/my-c8kv | kubevirt.io/domain:my-c8kv   | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | default/vm-my-c8kv-image | 10.128.1.67 (masq) | Running | Pending    | 2023-10-09T14:25:19Z | 2h18m |
|                 | kubevirt.io/nodeName:ocp-bm1 |         |     |        | cdromdisk/sda - 1Gi | default/my-c8kv-day0     |                    |         | Scheduling | 2023-10-09T14:26:47Z |       |
|                 | special:my-c8kv              |         |     |        |                     |                          |                    |         | Scheduled  | 2023-10-09T14:26:49Z |       |
|                 |                              |         |     |        |                     |                          |                    |         | Running    | 2023-10-09T14:26:51Z |       |
+-----------------+------------------------------+---------+-----+--------+---------------------+--------------------------+--------------------+---------+------------+----------------------+-------+
```

```
# iserver get ocp vm --name my-c8kv
+-----------------+---------+-----+--------+---------------------+--------------------+---------+-------+---------+---------------------+--------------+----+-------+
| VM              | Node    | CPU | Memory | Disks               | Interfaces         | State   | Ready | Failure | Service             | NodePort     | LM | Age   |
+-----------------+---------+-----+--------+---------------------+--------------------+---------+-------+---------+---------------------+--------------+----+-------+
| default/my-c8kv | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | 10.128.1.67 (masq) | Running | V     | --      | default/my-c8kv-ssh | 22:31195/TCP | X  | 2h19m |
|                 |         |     |        | cdromdisk/sda - 1Gi |                    |         |       |         |                     |              |    |       |
+-----------------+---------+-----+--------+---------------------+--------------------+---------+-------+---------+---------------------+--------------+----+-------+
```

## Functional test

```
$ ssh -p 31995 admin@10.58.29.84
Password:

my-c8kv#show ip int br
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.0.2.2        YES DHCP   up                    up
```

[Back](../README.md)