# UDN w/L2 Topology - Step 3: Virtual Machine

[[Back]](./overview.md) [[Prev](./pod.md)] [[Next]](./task.md)

## Connection to POD CIDR

- Virtual Machine **may** connect to Kubernetes POD CIDR as primary interface
- if it does, the default route is via this interface

## Connection to primary UDN w/l2 topology

- Virtual Machine **may** connect to udn as primary interface
- [namespace](../namespace.md) must be labeled as primary enabled
- [udn](./udn.md) must be configured with role:Primary
- the udn/nad name is not explicitly defined, `l2bridge` binding value is used instead

```
  template:
    spec:
      domain:
        devices:
          interfaces:
          - binding:
              name: l2bridge
            name: default
      networks:
      - name: default
        pod: {}
```

## Connection to secondary UDN w/l2 topology

- Virtual Machine **may** connect to udn and that can be localnet
- no namespace label required
- [udn](./udn.md) must be configured with role:Secondary
- secondary interface name mapped to Multus network using NAD reference

```
  template:
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: net1
      networks:
      - multus:
          networkName: island-p/sl2
        name: net1
```

## CIDR example

```
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-p
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: island-p
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
        storageClassName: lvms-vg1
        volumeMode: Block
      source:
        http:
          url: http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2
  runStrategy: Always
  template:
    metadata:
      labels:
        app: c8kv1
        kubevirt.io/domain: c8kv1
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          - cdrom:
              bus: sata
              readyOnly: true
            name: day0
          interfaces:
          - binding:
              name: l2bridge
            name: default
          - bridge: {}
            name: net1
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv1
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island-p/sl2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: island-p
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: island-p
        name: day0
```

## Virtual Machine state example

```
+----+-------------+-------+-----+-----+---------------------+-------+-----------------------------------------+-----------------------+---------+-------+
| ID | VM Instance | Node  | CPU | Mem | Disk                | PVC   | Interface                               | Svc                   | State   | Age   |
+----+-------------+-------+-----+-----+---------------------+-------+-----------------------------------------+-----------------------+---------+-------+
| 1  | island-p    | bm1-1 | 1   | 4Gi | rootdisk/vda - 10Gi | c8kv1 | [default] 66.66.0.16 (pod:l2bridge)     | NodePort:TCP/22:30999 | Running | 1h16m |
|    | c8kv1       |       |     |     | day0                | ---   | [net1] 66.66.1.9 (multus:island-p/sl2)  |                       |         |       |
+----+-------------+-------+-----+-----+---------------------+-------+-----------------------------------------+-----------------------+---------+-------+
```

## IP Stack

```
interface GigabitEthernet1
 ip address dhcp
 negotiation auto
!
interface GigabitEthernet2
 ip address dhcp
 negotiation auto
!
```

```
c8kv1#show interfaces
GigabitEthernet1 is up, line protocol is up 
  Hardware is vNIC, address is 0a58.4242.0010 (bia 0a58.4242.0010)
  Internet address is 66.66.0.16/24
GigabitEthernet2 is up, line protocol is up
  Hardware is vNIC, address is 0265.2bc5.ba2e (bia 0265.2bc5.ba2e)
  Internet address is 66.66.1.9/24
```

```
c8kv1#show ip route
S*    0.0.0.0/0 [254/0] via 66.66.0.1
      66.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C        66.66.0.0/24 is directly connected, GigabitEthernet1
L        66.66.0.16/32 is directly connected, GigabitEthernet1
C        66.66.1.0/24 is directly connected, GigabitEthernet2
L        66.66.1.9/32 is directly connected, GigabitEthernet2
      169.254.0.0/32 is subnetted, 1 subnets
S        169.254.1.1 [254/0] via 66.66.0.1, GigabitEthernet1
```

[[Back]](./overview.md) [[Prev](./pod.md)] [[Next]](./task.md)