# Empty Disk

An emptyDisk works similar to an emptyDir in Kubernetes.

An extra sparse qcow2 disk will be allocated and it will live as long as the VM. Thus it will survive guest side VM reboots, but not a VM re-creation.

## Example (cirros05.yaml)

```
spec:
  template:
    spec:
      volumes:
        - name: containerdisk
          containerDisk:
            image: quay.io/kubevirt/cirros-container-disk-demo
```

### Launcher

```
# oc get pod virt-launcher-cirros05-sws4v -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.128.2.27"
          ],
          "default": true,
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.128.2.27"
          ],
          "default": true,
          "dns": {}
      }]
    kubectl.kubernetes.io/default-container: compute
    kubevirt.io/domain: cirros05
    kubevirt.io/migrationTransportUnix: "true"
    post.hook.backup.velero.io/command: '["/usr/bin/virt-freezer", "--unfreeze", "--name",
      "cirros05", "--namespace", "default"]'
    post.hook.backup.velero.io/container: compute
    pre.hook.backup.velero.io/command: '["/usr/bin/virt-freezer", "--freeze", "--name",
      "cirros05", "--namespace", "default"]'
    pre.hook.backup.velero.io/container: compute
    traffic.sidecar.istio.io/kubevirtInterfaces: k6t-eth0
  creationTimestamp: "2023-03-14T17:28:20Z"
  generateName: virt-launcher-cirros05-
  labels:
    kubevirt.io: virt-launcher
    kubevirt.io/created-by: 99d288da-82e5-4f86-a3cb-20f19dbd087e
    kubevirt.io/domain: cirros05
    vm.kubevirt.io/name: cirros05
  name: virt-launcher-cirros05-sws4v
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachineInstance
    name: cirros05
    uid: 99d288da-82e5-4f86-a3cb-20f19dbd087e
  resourceVersion: "19176626"
  uid: 4a957d74-fd0e-4b48-b03e-9567e27fb3a8
spec:
  automountServiceAccountToken: false
  containers:
  - command:
    - /usr/bin/virt-launcher-monitor
    - --qemu-timeout
    - 270s
    - --name
    - cirros05
    - --uid
    - 99d288da-82e5-4f86-a3cb-20f19dbd087e
    - --namespace
    - default
    - --kubevirt-share-dir
    - /var/run/kubevirt
    - --ephemeral-disk-dir
    - /var/run/kubevirt-ephemeral-disks
    - --container-disk-dir
    - /var/run/kubevirt/container-disks
    - --grace-period-seconds
    - "45"
    - --hook-sidecars
    - "0"
    - --ovmf-path
    - /usr/share/OVMF
    - --run-as-nonroot
    env:
    - name: XDG_CACHE_HOME
      value: /var/run/kubevirt-private
    - name: XDG_CONFIG_HOME
      value: /var/run/kubevirt-private
    - name: XDG_RUNTIME_DIR
      value: /var/run
    - name: POD_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imagePullPolicy: IfNotPresent
    name: compute
    resources:
      limits:
        devices.kubevirt.io/kvm: "1"
        devices.kubevirt.io/tun: "1"
        devices.kubevirt.io/vhost-net: "1"
      requests:
        cpu: 100m
        devices.kubevirt.io/kvm: "1"
        devices.kubevirt.io/tun: "1"
        devices.kubevirt.io/vhost-net: "1"
        ephemeral-storage: 50M
        memory: 1266Mi
    securityContext:
      capabilities:
        add:
        - NET_BIND_SERVICE
        - SYS_PTRACE
        drop:
        - NET_RAW
      privileged: false
      runAsGroup: 107
      runAsNonRoot: true
      runAsUser: 107
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/kubevirt-private
      name: private
    - mountPath: /var/run/kubevirt
      name: public
    - mountPath: /var/run/kubevirt-ephemeral-disks
      name: ephemeral-disks
    - mountPath: /var/run/kubevirt/container-disks
      mountPropagation: HostToContainer
      name: container-disks
    - mountPath: /var/run/kubevirt/hotplug-disks
      mountPropagation: HostToContainer
      name: hotplug-disks
    - mountPath: /var/run/libvirt
      name: libvirt-runtime
    - mountPath: /var/run/kubevirt/sockets
      name: sockets
    - mountPath: /var/run/kubevirt-private/vmi-disks/rootdisk
      name: rootdisk
  dnsPolicy: ClusterFirst
  enableServiceLinks: false
  hostname: cirros05
  imagePullSecrets:
  - name: default-dockercfg-9tgqh
  nodeName: kubevirt-nn4bm-worker-9fxdj
  nodeSelector:
    kubevirt.io/schedulable: "true"
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  readinessGates:
  - conditionType: kubevirt.io/virtual-machine-unpaused
  restartPolicy: Never
  schedulerName: default-scheduler
  securityContext:
    runAsGroup: 107
    runAsNonRoot: true
    runAsUser: 107
    seLinuxOptions:
      type: virt_launcher.process
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 60
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  - effect: NoSchedule
    key: node.kubernetes.io/memory-pressure
    operator: Exists
  volumes:
  - emptyDir: {}
    name: private
  - emptyDir: {}
    name: public
  - emptyDir: {}
    name: sockets
  - name: rootdisk
    persistentVolumeClaim:
      claimName: cirros05
  - emptyDir: {}
    name: virt-bin-share-dir
  - emptyDir: {}
    name: libvirt-runtime
  - emptyDir: {}
    name: ephemeral-disks
  - emptyDir: {}
    name: container-disks
  - emptyDir: {}
    name: hotplug-disks
status:
  conditions:
  - lastProbeTime: "2023-03-14T17:28:20Z"
    lastTransitionTime: "2023-03-14T17:28:20Z"
    message: the virtual machine is not paused
    reason: NotPaused
    status: "True"
    type: kubevirt.io/virtual-machine-unpaused
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:28:20Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:28:33Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:28:33Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:28:20Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://5d65f9be2aa1cbe57e5f2dc94c49b186211067dcb4ab8b7e5d90fa50c0476913
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imageID: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:1a7996616acb7a7e0e5616be3fa2f591c663999d89f53c3cd1affda5b1ea3db1
    lastState: {}
    name: compute
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2023-03-14T17:28:32Z"
  hostIP: 10.58.24.218
  phase: Running
  podIP: 10.128.2.27
  podIPs:
  - ip: 10.128.2.27
  qosClass: Burstable
  startTime: "2023-03-14T17:28:20Z"
```

### OS View

```
# fdisk -l /dev/vdb
Disk /dev/vdb: 1 GiB, 1073741824 bytes, 2097152 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

# fdisk -l /dev/vdc
Disk /dev/vdc: 2 GiB, 2147483648 bytes, 4194304 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

The disk is really empty, so...

```
# fdisk /dev/vdb

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p):

Using default response p.
Partition number (1-4, default 1):
First sector (2048-2097151, default 2048):
Last sector, +sectors or +size{K,M,G,T,P} (2048-2097151, default 2097151):

Created a new partition 1 of type 'Linux' and of size 1023 MiB.

Command (m for help): p
Disk /dev/vdb: 1 GiB, 1073741824 bytes, 2097152 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2e6cd680

Device     Boot Start     End Sectors  Size Id Type
/dev/vdb1        2048 2097151 2095104 1023M 83 Linux

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

Then filesystem

```
# mkfs.ext3 /dev/vdb1
mke2fs 1.42.12 (29-Aug-2014)
Creating filesystem with 261888 4k blocks and 65536 inodes
Filesystem UUID: 0a7be4cf-9a07-4393-aedc-3d9ecb6438eb
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376

Allocating group tables: done
Writing inode tables: done
Creating journal (4096 blocks): done
Writing superblocks and filesystem accounting information: done
```

Finally mount

```
# mount /dev/vdb1 /extra1/
# ls -lta /extra1/
total 21
drwxr-xr-x    3 root     root          4096 Mar 14 18:42 .
drwx------    2 root     root         16384 Mar 14 18:42 lost+found
drwxr-xr-x   22 root     root          1024 Mar 14 18:33 ..
```

### Qemu

Files on the worker node

```
/var/lib/kubelet/pods/4a957d74-fd0e-4b48-b03e-9567e27fb3a8/volumes/kubernetes.io~empty-dir/libvirt-runtime/empty-disks/extra1.qcow2
/var/lib/kubelet/pods/4a957d74-fd0e-4b48-b03e-9567e27fb3a8/volumes/kubernetes.io~empty-dir/libvirt-runtime/empty-disks/extra2.qcow2
```

```
107      2999559 2999353  0 17:28 ?        00:00:10 /usr/libexec/qemu-kvm
  -name guest=default_cirros05,debug-threads=on
  -S
  -object {
    "qom-type":"secret",
    "id":"masterKey0",
    "format":"raw",
    "file":"/var/run/kubevirt-private/libvirt/qemu/lib/domain-1-default_cirros05/master-key.aes"
  }
  -machine pc-q35-rhel8.6.0,usb=off,dump-guest-core=off,memory-backend=pc.ram
  -accel kvm
  -cpu Cascadelake-Server,ss=on,hypervisor=on,tsc-adjust=on,umip=on,pku=on,md-clear=on,stibp=on,arch-capabilities=on,xsaves=on,ibpb=on,ibrs=on,amd-stibp=on,amd-ssbd=on,rdctl-no=on,ibrs
  -all=on,skip-l1dfl-vmentry=on,mds-no=on,pschange-mc-no=on,hle=off,erms=off,rtm=off,mpx=off,avx512vnni=off,xgetbv1=off
  -m 1024
  -object {
    "qom-type":"memory-backend-ram",
    "id":"pc.ram",
    "size":1073741824
  }
  -overcommit mem-lock=off
  -smp 1,sockets=1,dies=1,cores=1,threads=1
  -object {
    "qom-type":"iothread",
    "id":"iothread1"
  }
  -uuid f94dfe6f-22e8-5781-9101-e3fbbce803c3
  -smbios type=1,manufacturer=Red Hat,product=Container-native virtualization,version=4.11.3,uuid=f94dfe6f-22e8-5781-9101-e3fbbce803c3,sku=4.11.3,family=Red Hat
  -no-user-config
  -nodefaults
  -c hardev socket,id=charmonitor,fd=19,server=on,wait=off
  -mon chardev=charmonitor,id=monitor,mode=control
  -rtc base=utc
  -no-shutdown
  -boot strict=on
  -device pcie-root-port,port=16,chassis=1,id=pci.1,bus=pcie.0,multifunction=on,addr=0x2
  -device pcie-root-port,port=17,chassis=2,id=pci.2,bus=pcie.0,addr=0x2.0x1
  -device pcie-root-port,port=18,chassis=3,id=pci.3,bus=pcie.0,addr=0x2.0x2
  -device pcie-root-port,port=19,chassis=4,id=pci.4,bus=pcie.0,addr=0x2.0x3
  -device pcie-root-port,port=20,chassis=5,id=pci.5,bus=pcie.0,addr=0x2.0x4
  -device pcie-root-port,port=21,chassis=6,id=pci.6,bus=pcie.0,addr=0x2.0x5
  -device pcie-root-port,port=22,chassis=7,id=pci.7,bus=pcie.0,addr=0x2.0x6
  -device pcie-root-port,port=23,chassis=8,id=pci.8,bus=pcie.0,addr=0x2.0x7
  -device pcie-root-port,port=24,chassis=9,id=pci.9,bus=pcie.0,addr=0x3
  -device virtio-scsi-pci-non-transitional,id=scsi0,bus=pci.2,addr=0x0
  -device virtio-serial-pci-non-transitional,id=virtio-serial0,bus=pci.3,addr=0x0
  -blockdev {
    "driver":"file",
    "filename":"/var/run/kubevirt-private/vmi-disks/rootdisk/disk.img",
    "node-name":"libvirt-3-storage",
    "cache": {
      "direct":true,
      "no-flush":false
    },
    "auto-read-only":true,
    "discard":"unmap"
  }
  -blockdev {
    "node-name":"libvirt-3-format",
    "read-only":false,
    "discard":"unmap",
    "cache": {
      "direct":true,
      "no-flush":false
    },
    "driver":"raw",
    "file":"libvirt-3-storage"
  }
  -device virtio-blk-pci-non-transitional,bus=pci.4,addr=0x0,drive=libvirt-3-format,id=ua-rootdisk,bootindex=1,write-cache=on,werror=stop,rerror=stop
  -blockdev {
    "driver":"file",
    "filename":
    "/var/run/libvirt/empty-disks/extra1.qcow2",
    "node-name":"libvirt-2-storage",
    "cache":{
      "direct":true,"no-flush":false
    },
    "auto-read-only":true,
    "discard":"unmap"
  }
  -blockdev {
    "node-name":"libvirt-2-format",
    "read-only":false,
    "discard":"unmap",
    "cache":{
      "direct":true,
      "no-flush":false
    },
    "driver":"qcow2",
    "file":"libvirt-2-storage"
  }
  -device virtio-blk-pci-non-transitional,bus=pci.5,addr=0x0,drive=libvirt-2-format,id=ua-extra1,write-cache=on,werror=stop,rerror=stop
  -blockdev {"driver":"file","filename":"/var/run/libvirt/empty-disks/extra2.qcow2","node-name":"libvirt-1-storage","cache":{"direct":true,"no-flush":false},"auto-read-only":true,"discard":"unmap"} -blockdev {"no
de-name":"libvirt-1-format","read-only":false,"discard":"unmap","cache":{"direct":true,"no-flush":false},"driver":"qcow2","file":"libvirt-1-storage"} -device virtio-blk-pci-non-transitional,bus=pci.6,addr=0x0,drive=libvirt-1-format,id=ua-extra2,write-cache=on,werror=stop,re
rror=stop -netdev tap,fd=20,id=hostua-default,vhost=on,vhostfd=22 -device virtio-net-pci-non-transitional,host_mtu=1450,netdev=hostua-default,id=ua-default,mac=02:6c:cf:00:00:24,bus=pci.1,addr=0x0,romfile= -chardev socket,id=charserial0,fd=17,server=on,wait=off -device isa-
serial,chardev=charserial0,id=serial0 -chardev socket,id=charchannel0,fd=18,server=on,wait=off -device virtserialport,bus=virtio-serial0.0,nr=1,chardev=charchannel0,id=channel0,name=org.qemu.guest_agent.0 -audiodev {"id":"audio1","driver":"none"} -vnc vnc=unix:/var/run/kube
virt-private/99d288da-82e5-4f86-a3cb-20f19dbd087e/virt-vnc,audiodev=audio1 -device VGA,id=video0,vgamem_mb=16,bus=pcie.0,addr=0x1 -device virtio-balloon-pci-non-transitional,id=balloon0,bus=pci.7,addr=0x0 -object {"qom-type":"rng-random","id":"objrng0","filename":"/dev/uran
dom"} -device virtio-rng-pci-non-transitional,rng=objrng0,id=rng0,bus=pci.8,addr=0x0 -sandbox on,obsolete=deny,elevateprivileges=deny,spawn=deny,resourcecontrol=deny -msg timestamp=on
```