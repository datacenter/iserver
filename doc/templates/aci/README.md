
# APIC

Uses APIC GET API calls to provide the configuration and operational state of ACI fabric via CLI.

## Usage

APIC can be [pre-defined](./Controller.md) and then used in with '--apic <name>' option. Last used apic name becomes default one.

Example:

```
# iserver get aci nodes --apic myapic
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
- [Contract](./Contract.md)
- [VRF](./Vrf.md)

## Inventory

- [Node](./Node.md)
- [Interface](./Interface.md)
- [Protocol](./Protocol.md)

## Endpoint

- [Endpoint](./Endpoint.md)

## Policy

Policy Group
- [access interface](./PgAccessInterface.md)

Policy
- access global
- access interface

Pool
- [VLAN](./PoolVlan.md)

Domain
- [Phy](./DomainPhy.md)
- [L2](./DomainL2.md)
- [L3](./DomainL3.md)
- [VMM](./DomainVmm.md)

## Cross Domain

- [Server](./XdServer.md)
