# UDN and Virtual Machine - Task

[[Back]](../README.md) [[Prev]](../create/vm_crd.md) [[Next]](../get/vm.md)

## Input

> [!NOTE]
> Data volume w/pvc and user defined networks pre-created

```
[
    {
        "k8s": {
            "description": "udn c8kv3 - udn primary and udn secondary s1-l2",
            "namespace": "island",
            "items": [
                {
                    "__type__": "config-map",
                    "name": "c8kv3-day0",
                    "content": {
                        "iosxe_config.txt": {
                            "file": "C:\\tmp\\c8kv.txt",
                            "vars": {
                                "HOSTNAME": "c8kv3",
                                "DOMAIN": "domain.com",
                                "USERNAME": "admin",
                                "PASSWORD": "password"
                            }
                        }
                    }
                },
                {
                    "__type__": "virtual-machine",
                    "name": "c8kv3",
                    "template": "c8kv",
                    "url": "http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2",
                    "pvc": "default/c8kv-17.06.05",
                    "day0": "c8kv3-day0",
                    "interface": [
                        {
                            "name": "default",
                            "type": "udn-l2-primary"
                        },
                        {
                            "name": "net1",
                            "type": "bridge",
                            "nad": "s1-l2"
                        }
                    ],
                    "node": "bm1-3",
                    "stop-on-delete": true,
                    "sleep-on-delete": 60
                }
            ]
        }
    }
]
```

```
hostname ${HOSTNAME}
ip domain name ${DOMAIN}
aaa new-model
aaa authentication login default local
aaa authorization exec default local
username ${USERNAME} privilege 15 secret ${PASSWORD}
no ip http secure-server
crypto key generate rsa modulus 2048
ip ssh version 2
interface GigabitEthernet1
  ip address dhcp
  no shutdown
interface GigabitEthernet2
  ip address dhcp
  no shutdown
ip http secure-server
line con 0
  length 0
line vty 0 4
  length 0
```

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

Kubernetes Workflow - Config Map - Create
=========================================

OpenShift Cluster: bm1

Create ConfigMap
----------------
- namespace: island
- name: c8kv3-day0

~~~
apiVersion: v1
data:
  iosxe_config.txt: |-
    hostname c8kv3
    ip domain name domain.com
    aaa new-model
    aaa authentication login default local
    aaa authorization exec default local
    username admin privilege 15 secret password
    no ip http secure-server
    crypto key generate rsa modulus 2048
    ip ssh version 2
    interface GigabitEthernet1
      ip address dhcp
      no shutdown
    interface GigabitEthernet2
      ip address dhcp
      no shutdown
    ip http secure-server
    line con 0
      length 0
    line vty 0 4
      length 0
kind: ConfigMap
metadata:
  name: c8kv3-day0
  namespace: island

~~~
ConfigMap [island/c8kv3-day0] created
- wait for ConfigMap island/c8kv3-day0 [timeout:60s]

Completed tasks
- config map created

Kubernetes Workflow - Virtual Machine - Create
==============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: island
- name: c8kv3

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv3
  namespace: island
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv3
      namespace: island
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
        app: c8kv3
        kubevirt.io/domain: c8kv3
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
      hostname: c8kv3
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island/s1-l2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-3
      volumes:
      - dataVolume:
          name: c8kv3
          namespace: island
        name: rootdisk
      - configMap:
          name: c8kv3-day0
          namespace: island
        name: day0

~~~
VirtualMachine [island/c8kv3] created
- wait for VirtualMachine island/c8kv3 [timeout:60s]
- wait for VirtualMachine island/c8kv3 [timeout:360s] with {"status": "Running"}

Completed tasks
- virtual machine created
```

[[Back]](../README.md) [[Prev]](../create/vm_crd.md) [[Next]](../get/vm.md)