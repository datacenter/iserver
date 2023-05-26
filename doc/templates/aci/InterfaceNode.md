# Node Interface

## Single node selection

Usage:
- define node name (or part of node name)
- if value matches multiple nodes, then command follows [multiple nodes](./InterfaceNodes.md) behavior
- name 'any' and 'all' matches [all nodes](./InterfaceNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if node name is left undefined, last-used-node-name per apic is used

Example:

```
DOC_TEMPLATE:get_aci_intf_mgmt.state_node:iserver.output.default
```

[[Back]](./Interface.md)