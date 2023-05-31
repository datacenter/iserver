# Node Interface

## Node selection options

- interface information is by default [single node](./InterfaceNode.md) specific
- define [multiple nodes](./InterfaceNodes.md) or [all nodes](./InterfaceNodesAll.md) to get broader view
- select [multiple apics](./InterfaceApics.md) for multi-APIC view

Note: the more selected nodes, the longer it takes to run command to completion

## Filter options

Each interface command supports custom set of rules to filter the interfaces from the selected nodes.

Check the options with --help or in the documentation below.

## View options

Selected interfaces are shown in table format. Check --view for different groups of interface attributes.

Verbose view is flat and provides complete collected information for every interface matching node selection and filtering criteria.

## Output options

Option default prints table or flat data while option json prints properly formatted output that can be further analyzed with e.g. jq tool.

## Supported interfaces

- [CloudSec](./InterfaceCloudSec.md)
- [Encapsulated Routed](./InterfaceL3e.md)
- [FC](./InterfaceFc.md)
- [FC PC](./InterfaceFcPc.md)
- [Looback](./InterfaceLoopback.md)
- [MACsec](./InterfaceMacSec.md)
- [Management](./InterfaceMgmt.md)
- [Phy](./InterfacePhy.md)
- [PC](./InterfacePc.md)
- [SVI](./InterfaceSvi.md)
- [Tunnel](./InterfaceTunnel.md)
- [VFC](./InterfaceVfc.md)
- [VPC](./InterfaceVpc.md)

## Related

- Find interface by IP
- Find interface by MAC
- Interface summary

[[Back]](./README.md)