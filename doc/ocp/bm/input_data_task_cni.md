# Task: cni

- enable OVS CNI based on https://github.com/k8snetworkplumbingwg/ovs-cni

Example:

```
    "cni": {
        "ovs": "0.39.0"
    }
```

Make sure that cni.ovs contains version value available at [releases](https://github.com/k8snetworkplumbingwg/ovs-cni/releases)

Expected outcome

```
$ ls -lta /var/lib/cni/bin/ovs
-rwxr-xr-x. 1 core core 13521372 Jun 11 07:17 /var/lib/cni/bin/ovs

$ /var/lib/cni/bin/ovs -v
CNI OVS bridge plugin version unknown
CNI protocol versions supported: 0.1.0, 0.2.0, 0.3.0, 0.3.1, 0.4.0, 1.0.0, 1.1.0
```

[Back](./input_data_tasks.md)