# OVNKubernetes BGP - Delete route advertisement

[[Back]](./README.md)

> [!NOTE]
> Use `__all__` value for all route advertisement configurations

```
# iserver delete ocp ovn-bgp --mode ra-config --config cudn

OpenShift Workflow - OVNKubernetes - Delete route advertisement
===============================================================

OpenShift Cluster: bm7

Delete RouteAdvertisements
--------------------------
- name: cudn
- deleted
- wait for no RouteAdvertisement cudn [timeout:60s]

Completed tasks
- OVN route advertisement deleted
```

[[Back]](./README.md)