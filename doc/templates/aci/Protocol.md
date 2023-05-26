# Node Protocol

## Node selection options

- protocol information is by default [single node](./ProtocolNode.md) specific
- define [multiple nodes](./ProtocolNodes.md) or [all nodes](./ProtocolNodesAll.md) to get broader view

Note: the more selected nodes, the longer it takes to run command to completion

## Filter options

Node protocol command supports custom set of rules to filter the protocol related information.

Check the options with --help or in the documentation below.

## Output options

Node protocol information is shown in table format. Check -o option for different groups of protocol attributes.

Verbose option is flat and provides complete collected information for every matching node selection and filtering criteria.

Option json prints properly formatted output that can be further analyzed with e.g. jq tool.

## Supported protocols

- AIB
- [ARP](./ProtocolArp.md)
- [BFD](./ProtocolBfd.md)
- [BGP](./ProtocolBgp.md)
- [CDP](./ProtocolCdp.md)
- COOP
- EIGRP
- [HSRP](./ProtocolHsrp.md)
- IGMP
- IGMP Snoop
- [IPv4](./ProtocolIpv4.md)
- [IPv6](./ProtocolIpv6.md)
- [ISIS](./ProtocolIsis.md)
- [LACP](./ProtocolLacp.md)
- [LLDP](./ProtocolLldp.md)
- [ND](./ProtocolNd.md)
- OSPF
- OSPFv3
- PIM
- PIMv6
- RIBv4
- RIBv6
- TWAMP

[[Back]](./README.md)