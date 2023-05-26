# Node Interface

## Multiple nodes selection

Usage:
- define node name multiple times
- each name is checked against node names in selected APIC
- nodes selected based on full or partial name match
- name 'any' and 'all' matches [all nodes](./ProtocolNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if multiple nodes are defined, last-used-node-name per apic is not updated

Example:

```
DOC_TEMPLATE:get_aci_proto_cdp.interface_nodes:iserver.output.default
```

[[Back]](./Protocol.md)