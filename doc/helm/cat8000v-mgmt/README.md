# Helm: Cat8000v with SNMP/Netconf management options

This document extends [basic cat8000v deployment](../cat8000v-basic/README.md) with:
- snmp access
- netconf access

Helm package sources are [here](../../../samples/ocp/helm/cat8000v-mgmt/).

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

## SNMP Service Template

```
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-snmp
  namespace: {{ .Release.Namespace }}
spec:
  externalTrafficPolicy: Cluster
  ports:
  - port: 161
    protocol: UDP
    targetPort: 161
  selector:
    special: {{ .Release.Name }}
  type: NodePort
```

## Netconf Service Template

```
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-netconf
  namespace: {{ .Release.Namespace }}
spec:
  externalTrafficPolicy: Cluster
  ports:
  - port: 830
    protocol: TCP
    targetPort: 830
  selector:
    special: {{ .Release.Name }}
  type: NodePort
```

## Helm deployment

```
$ helm install my-c8kv ./cat8000v-mgmt/ -n default
NAME: my-c8kv
LAST DEPLOYED: Fri Oct  6 08:49:35 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

## VNF state

```
# iserver get k8s vm --name my-c8kv

+-----------------+-----------------------------------+-----+--------+-----------+--------------------------+------------+----------------------------+----------------+---------+-------+---------+-------+
| VM              | Label                             | CPU | Memory | Disks     | DV Name                  | DV Storage | DV Source                  | Interfaces     | Created | Ready | Status  | Age   |
+-----------------+-----------------------------------+-----+--------+-----------+--------------------------+------------+----------------------------+----------------+---------+-------+---------+-------+
| default/my-c8kv | app:my-c8kv                       | 1   | None   | rootdisk  | default/vm-my-c8kv-image | 10Gi       | pvc:default:cat8000v-image | default (masq) | ✓       | ✓     | Running | 3h41m |
|                 | app.kubernetes.io/managed-by:Helm |     |        | cdromdisk |                          |            |                            |                |         |       |         |       |
+-----------------+-----------------------------------+-----+--------+-----------+--------------------------+------------+----------------------------+----------------+---------+-------+---------+-------+
```

```
# iserver get k8s vmi --name my-c8kv

+-----------------+------------------------------+---------+-----+--------+---------------------+--------------------------+--------------------+---------+------------+----------------------+-------+
| VM              | Label                        | Node    | CPU | Memory | Disk                | PVC                      | Interface          | State   | Phase      | Timestamp            | Age   |
+-----------------+------------------------------+---------+-----+--------+---------------------+--------------------------+--------------------+---------+------------+----------------------+-------+
| default/my-c8kv | kubevirt.io/domain:my-c8kv   | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | default/vm-my-c8kv-image | 10.128.1.99 (masq) | Running | Pending    | 2023-10-09T15:16:55Z | 3h41m |
|                 | kubevirt.io/nodeName:ocp-bm1 |         |     |        | cdromdisk/sda - 1Gi | default/my-c8kv-day0     |                    |         | Scheduling | 2023-10-09T15:18:29Z |       |
|                 | special:my-c8kv              |         |     |        |                     |                          |                    |         | Scheduled  | 2023-10-09T15:18:31Z |       |
|                 |                              |         |     |        |                     |                          |                    |         | Running    | 2023-10-09T15:18:32Z |       |
+-----------------+------------------------------+---------+-----+--------+---------------------+--------------------------+--------------------+---------+------------+----------------------+-------+
```

```
# iserver get ocp vm --name my-c8kv

+-----------------+---------+-----+--------+---------------------+--------------------+---------+-------+---------+-------------------------+---------------+----+-------+
| VM              | Node    | CPU | Memory | Disks               | Interfaces         | State   | Ready | Failure | Service                 | NodePort      | LM | Age   |
+-----------------+---------+-----+--------+---------------------+--------------------+---------+-------+---------+-------------------------+---------------+----+-------+
| default/my-c8kv | ocp-bm1 | 1   | 4Gi    | rootdisk/vda - 10Gi | 10.128.1.99 (masq) | Running | V     | --      | default/my-c8kv-netconf | 830:32669/TCP | X  | 3h40m |
|                 |         |     |        | cdromdisk/sda - 1Gi |                    |         |       |         | default/my-c8kv-snmp    | 161:32379/UDP |    |       |
|                 |         |     |        |                     |                    |         |       |         | default/my-c8kv-ssh     | 22:30016/TCP  |    |       |
+-----------------+---------+-----+--------+---------------------+--------------------+---------+-------+---------+-------------------------+---------------+----+-------+
```

## SSH functional test

```
$ ssh -p 30016 admin@10.58.29.84
Password:

my-c8kv#
```

## SNMP functional test

```
$ snmpwalk -c public -v2c 10.58.29.84:30129 1.3.6.1.2.1.1.1
iso.3.6.1.2.1.1.1.0 = STRING: "Cisco IOS Software [Bengaluru], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.6.5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Wed 25-Jan-23 16:0"
```

## Netconf functional test

```
$ ssh -p 32045 admin@10.58.29.84 -s netconf
admin@10.58.29.84's password:
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
<capability>urn:ietf:params:netconf:base:1.1</capability>
<capability>urn:ietf:params:netconf:capability:writable-running:1.0</capability>
...
```

## NSO

```
nso@ncs# show running-config devices device my-cat8kv-mgmt
devices device my-cat8kv-mgmt
 address   10.58.29.84
 port      32385
 device-type cli ned-id cisco-ios-cli-6.99
 state admin-state unlocked
!
```

```
# devices device my-cat8kv-mgmt sync-from
result true
```

```
nso@ncs# show running-config devices device my-cat8kv-mgmt config
devices device my-cat8kv-mgmt
 config
  hostname        my-c8kv
  tailfned police cirmode
  version         17.6
...
```

[Back](../README.md)