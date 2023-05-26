# Node Protocol

## Single node selection

Usage:
- define node name (or part of node name)
- if value matches multiple nodes, then command follows [multiple nodes](./ProtocolNodes.md) behavior
- name 'any' and 'all' matches [all nodes](./ProtocolNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if node name is left undefined, last-used-node-name per apic is used

Example:

```
DOC_TEMPLATE:get_aci_proto_cdp.interface_node:iserver.output.default
```

[[Back]](./Protocol.md)