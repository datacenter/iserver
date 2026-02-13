# Cilium Configuration

## Overview

Cilium day2 configuration changes must be done by altering `ciliumconfig` custom resource. The `cilium-config` config map in `cilium` namespace must not be changed as it will be overwritten by Cilium operator anyway.

```
$ oc get ciliumconfigs.cilium.io 
NAME           AGE
ciliumconfig   103d
```

Any value or processing error in configuration is shown in status of the `ciliumconfig` custom resource.

Configuration change may or may not require cilium agent restart, in some cases restart is triggered automatically. However, it is not well documented or consistent as such it is safer to always restart the cilium agent daemons.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium config | get cilium configuration | [Link](./get_config.md)
iserver get ocp cilium config -v map | get cilium config map | [Link](./get_config_map.md)
iserver get ocp cilium config -v state | get cilium config state only | [Link](./get_config_state.md)
iserver get ocp cilium config -v all | get all cilium config details  | [Link](./get_config_all.md)
iserver set ocp cilium config | set cilium config | [Link](./set_config.md)

[[Back]](../Operations.md)