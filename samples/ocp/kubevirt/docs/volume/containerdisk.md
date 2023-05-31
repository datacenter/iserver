# Container Disk

Container Disk is an option for volume source and provides an ability to store and distribute VM disks in the container image registry.

No network shared storage devices are utilized by containerDisks. The disks are pulled from the container registry and reside on the local node hosting the VMs that consume the disks.

Container Disk is ephemeral storage devices that can be assigned to any number of active VirtualMachineInstances.
This makes it an ideal tool for users who want to replicate a large number of VM workloads that do not require persistent data.

## Container Disk - Source registry (cirros04.yaml)

```
spec:
  template:
    spec:
      volumes:
        - name: containerdisk
          containerDisk:
            image: quay.io/kubevirt/cirros-container-disk-demo
```

Virtual machine volume is stored as a file in the host filesystem where vm is running on. It can be also checked on launcher pod

```
# ls -lta /var/lib/kubelet/pods/2adff9f9-c30a-4b45-b4f7-d6981634d957/volumes/kubernetes.io~empty-dir/container-disks
total 12420
drwxrwxrwx.  2 root root       43 Mar 14 16:01 .
srwxr-xr-x.  1  107  107        0 Mar 14 16:01 disk_0.sock
drwxr-xr-x. 10 root root      166 Mar 14 16:01 ..
-r--r-----.  1  107  107 12716032 Jan  1  1970 disk_0.img
```

```

# oc get pod virt-launcher-cirros04-wltw8 -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.128.2.13"
          ],
          "default": true,
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.128.2.13"
          ],
          "default": true,
          "dns": {}
      }]
    kubectl.kubernetes.io/default-container: compute
    kubevirt.io/domain: cirros04
    kubevirt.io/migrationTransportUnix: "true"
    post.hook.backup.velero.io/command: '["/usr/bin/virt-freezer", "--unfreeze", "--name",
      "cirros04", "--namespace", "default"]'
    post.hook.backup.velero.io/container: compute
    pre.hook.backup.velero.io/command: '["/usr/bin/virt-freezer", "--freeze", "--name",
      "cirros04", "--namespace", "default"]'
    pre.hook.backup.velero.io/container: compute
    traffic.sidecar.istio.io/kubevirtInterfaces: k6t-eth0
  creationTimestamp: "2023-03-14T16:01:15Z"
  generateName: virt-launcher-cirros04-
  labels:
    kubevirt.io: virt-launcher
    kubevirt.io/created-by: ad372581-45cb-4811-9432-0ee96f689247
    kubevirt.io/domain: cirros04
    kubevirt.io/size: small
    vm.kubevirt.io/name: cirros04
  name: virt-launcher-cirros04-wltw8
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachineInstance
    name: cirros04
    uid: ad372581-45cb-4811-9432-0ee96f689247
  resourceVersion: "19035023"
  uid: 2adff9f9-c30a-4b45-b4f7-d6981634d957
spec:
  automountServiceAccountToken: false
  containers:
  - command:
    - /usr/bin/virt-launcher-monitor
    - --qemu-timeout
    - 333s
    - --name
    - cirros04
    - --uid
    - ad372581-45cb-4811-9432-0ee96f689247
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
        memory: "315783240"
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
  - args:
    - --copy-path
    - /var/run/kubevirt-ephemeral-disks/container-disk-data/ad372581-45cb-4811-9432-0ee96f689247/disk_0
    command:
    - /usr/bin/container-disk
    image: quay.io/kubevirt/cirros-container-disk-demo
    imagePullPolicy: Always
    name: volumecontainerdisk
    resources:
      limits:
        cpu: 100m
        memory: 40M
      requests:
        cpu: 10m
        ephemeral-storage: 50M
        memory: 1M
    securityContext:
      runAsNonRoot: true
      runAsUser: 107
      seLinuxOptions:
        level: s0
        type: virt_launcher.process
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/kubevirt-ephemeral-disks/container-disk-data/ad372581-45cb-4811-9432-0ee96f689247
      name: container-disks
    - mountPath: /usr/bin
      name: virt-bin-share-dir
  dnsPolicy: ClusterFirst
  enableServiceLinks: false
  hostname: cirros04
  imagePullSecrets:
  - name: default-dockercfg-9tgqh
  initContainers:
  - command:
    - /usr/bin/cp
    - /usr/bin/container-disk
    - /init/usr/bin/container-disk
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imagePullPolicy: IfNotPresent
    name: container-disk-binary
    resources:
      limits:
        cpu: 100m
        memory: 40M
      requests:
        cpu: 10m
        memory: 1M
    securityContext:
      privileged: false
      runAsGroup: 107
      runAsNonRoot: true
      runAsUser: 107
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /init/usr/bin
      name: virt-bin-share-dir
  - args:
    - --no-op
    command:
    - /usr/bin/container-disk
    image: quay.io/kubevirt/cirros-container-disk-demo
    imagePullPolicy: Always
    name: volumecontainerdisk-init
    resources:
      limits:
        cpu: 100m
        memory: 40M
      requests:
        cpu: 10m
        ephemeral-storage: 50M
        memory: 1M
    securityContext:
      runAsNonRoot: true
      runAsUser: 107
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/kubevirt-ephemeral-disks/container-disk-data/ad372581-45cb-4811-9432-0ee96f689247
      name: container-disks
    - mountPath: /usr/bin
      name: virt-bin-share-dir
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
  - lastProbeTime: "2023-03-14T16:01:15Z"
    lastTransitionTime: "2023-03-14T16:01:15Z"
    message: the virtual machine is not paused
    reason: NotPaused
    status: "True"
    type: kubevirt.io/virtual-machine-unpaused
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T16:01:26Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T16:01:29Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T16:01:29Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T16:01:15Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://29d7aaa0d6692f9a788975f2e63f9bc3499072f4d66e2e3b12eba87a55c5e2cb
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imageID: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:1a7996616acb7a7e0e5616be3fa2f591c663999d89f53c3cd1affda5b1ea3db1
    lastState: {}
    name: compute
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2023-03-14T16:01:27Z"
  - containerID: cri-o://12a4cc30b07faf9d307ec45f077ea93534e83b1f24dc07c9d57103519ba5eee8
    image: quay.io/kubevirt/cirros-container-disk-demo:latest
    imageID: quay.io/kubevirt/cirros-container-disk-demo@sha256:0e5ac38b20abcc7752293425b239a147868facd62cd5030dede6da6f2fc526a1
    lastState: {}
    name: volumecontainerdisk
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2023-03-14T16:01:29Z"
  hostIP: 10.58.24.218
  initContainerStatuses:
  - containerID: cri-o://d914b4fd224dd0f2dfdcb9740c83a21f7aa501eb7db5dac71c9bc9d3c7ff2f7d
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imageID: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:1a7996616acb7a7e0e5616be3fa2f591c663999d89f53c3cd1affda5b1ea3db1
    lastState: {}
    name: container-disk-binary
    ready: true
    restartCount: 0
    state:
      terminated:
        containerID: cri-o://d914b4fd224dd0f2dfdcb9740c83a21f7aa501eb7db5dac71c9bc9d3c7ff2f7d
        exitCode: 0
        finishedAt: "2023-03-14T16:01:17Z"
        reason: Completed
        startedAt: "2023-03-14T16:01:17Z"
  - containerID: cri-o://c59980878189e5530ba71802dba5e4d59312afd9aee41e222c9f16899a0d2e8a
    image: quay.io/kubevirt/cirros-container-disk-demo:latest
    imageID: quay.io/kubevirt/cirros-container-disk-demo@sha256:0e5ac38b20abcc7752293425b239a147868facd62cd5030dede6da6f2fc526a1
    lastState: {}
    name: volumecontainerdisk-init
    ready: true
    restartCount: 0
    state:
      terminated:
        containerID: cri-o://c59980878189e5530ba71802dba5e4d59312afd9aee41e222c9f16899a0d2e8a
        exitCode: 0
        finishedAt: "2023-03-14T16:01:26Z"
        reason: Completed
        startedAt: "2023-03-14T16:01:26Z"
  phase: Running
  podIP: 10.128.2.13
  podIPs:
  - ip: 10.128.2.13
  qosClass: Burstable
  startTime: "2023-03-14T16:01:15Z"
```
