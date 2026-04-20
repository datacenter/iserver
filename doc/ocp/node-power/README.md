# Node Power Management

Unlike [bare metal host power management](../metal-kubed/README.md), these workflows perform the node power management tasks via [ssh](../Access.md) and include kubernetes-friendly steps such as cordon and drain before shutting down or reloading the node.

Command | Intent | Details
--- | --- | ---
iserver set ocp node shutdown | graceful shutdown of node | [Link](./shutdown.md)
iserver set ocp node reload | graceful reload of node | [Link](./reload.md)
iserver set ocp node reboot | reboot a node (aka brut-mode) | [Link](./reboot.md)

[[Back]](../Operations.md)