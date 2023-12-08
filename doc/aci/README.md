# APIC

Uses APIC GET API calls to provide the configuration and operational state of ACI fabric via CLI.

## Usage

APIC can be [pre-defined](./Controller.md) and then used in with '--apic <name>' option. Last used apic name becomes default one.

Example:

```
# iserver get aci node --apic myapic
```

Alternatively, APIC access authentication details can be defined in each command execution.

```
# iserver get aci epg --ip 10.1.1.1 --username admin --password secret
```

## Tenant

![Chassis](images/tenant_policy_model.png)

- [Tenant](./Tenant.md)
- [Application Profile](./ApplicationProfile.md)
- [Endpoint Group](./ApplicationEpg.md)
- [Bridge Domain](./BridgeDomain.md)
- [L2 Out](./L2Out.md)
- [L3 Out and SR-MPLS VRF L3 Out](./L3Out.md)
- Contract
  - [Standard](./ContractStandard.md)
  - [Taboo](./ContractTaboo.md)
  - [Filter](./ContractFilter.md)
- [VRF](./Vrf.md)

## Inventory

- [Node](./Node.md)
- Interface
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
- Protocol
  - [ARP](./ProtocolArp.md)
  - [BFD](./ProtocolBfd.md)
  - [BGP](./ProtocolBgp.md)
  - [CDP](./ProtocolCdp.md)
  - [HSRP](./ProtocolHsrp.md)
  - [IPv4](./ProtocolIpv4.md)
  - [IPv6](./ProtocolIpv6.md)
  - [ISIS](./ProtocolIsis.md)
  - [LACP](./ProtocolLacp.md)
  - [LLDP](./ProtocolLldp.md)
  - [ND](./ProtocolNd.md)
- [Endpoint](./Endpoint.md)

## Fabric Access

### Domain

- [Phy](./DomainPhy.md)
- [L2](./DomainL2.md)
- [L3](./DomainL3.md)
- [VMM](./DomainVmm.md)

### Pool

- [VLAN](./PoolVlan.md)

### AEP

- [Attachable Access Entity Profile](./Aaep.md)

### Policy Group

- [Port](./PgAccessInterfacePort.md)
- [PC/VPC](./PgAccessInterfaceVpc.md)

### Interface Policy

- [Auth](./PolicyAuth.md)
- [CDP](./PolicyCdp.md)
- [CoPP](./PolicyCopp.md)
- [DPP](./PolicyDpp.md)
- [FC](./PolicyFc.md)
- [Flap](./PolicyFlap.md)
- [L2](./PolicyL2.md)
- [LACP](./PolicyLacp.md)
- [LACP Member](./PolicyLacpMember.md)
- [Link](./PolicyLink.md)
- [Link FC](./PolicyLinkFc.md)
- [LLDP](./PolicyLldp.md)
- [MCP](./PolicyMcp.md)
- [PFC](./PolicyPfc.md)
- [Port Security](./PolicyPortsec.md)
- [Slow Drain](./PolicyDrain.md)
- [Storm Control](./PolicyStomr.md)
- [STP](./PolicyStp.md)
- [SyncE](./PolicySynce.md)
- [Transceiver](./PolicyTransceiver.md)

## System

- [Fault](./SystemFault.md)

## Cross Domain

- [PSIRT](./XdPsirt.md)
- [Server](./XdServer.md)

[[Back]](../../README.md)