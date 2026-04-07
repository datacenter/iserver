# UDN w/L3 Topology - Step 3: Virtual Machine

[[Back]](./overview.md) [[Prev](./pod.md)] [[Next]](./task.md)


> [!CAUTION]
> IP DHCP fails on primary interface; this is known OpenShift limitation that has no path to resolution

## Connection to POD CIDR

- Virtual Machine **may** connect to Kubernetes POD CIDR as primary interface
- if it does, the default route is via this interface

## Connection to primary UDN w/l3 topology

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

## Connection to secondary UDN w/l3 topology

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
          networkName: island-q/sl3
        name: net1
```

## CIDR example

```
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-q
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: island-q
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
          networkName: island-q/sl3
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: island-q
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: island-q
        name: day0
```

## Virtual Machine state example

```
+----+-------------+-------+-----+-----+---------------------+-------+-----------------------------------------+-----------------------+---------+-------+
| ID | VM Instance | Node  | CPU | Mem | Disk                | PVC   | Interface                               | Svc                   | State   | Age   |
+----+-------------+-------+-----+-----+---------------------+-------+-----------------------------------------+-----------------------+---------+-------+
| 1  | island-q    | bm1-1 | 1   | 4Gi | rootdisk/vda - 10Gi | c8kv1 | [default] 66.66.0.30 (pod:l2bridge)     | NodePort:TCP/22:31148 | Running | 1h44m |
|    | c8kv1       |       |     |     | day0                | ---   | [net1] 66.66.1.7 (multus:island-q/sl3)  |                       |         |       |
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
c8kv1#show ip int br
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       unassigned      YES DHCP   up                    up
GigabitEthernet2       66.66.1.7       YES DHCP   up                    up
```

[[Back]](./overview.md) [[Prev](./pod.md)] [[Next]](./task.md)