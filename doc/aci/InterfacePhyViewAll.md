# Node Interface - Physical

## All view

```
# iserver get aci intf phy
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id 1/24
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#1]
--------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/24      | up    | disabled  | down | sfp-missing | leaf | switched |    | 3C:13:CC:B9:ED:C8 | trunk | 100G  | full   | 9000 | disable-fec | 
+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+

+----------------------+-----------+------+---------+---------+---------+------+------+----+-----+----+
| Node                 | Interface | Oper | Present | State   | Optics  | Name | Type | PN | Rev | SN |
+----------------------+-----------+------+---------+---------+---------+------+------+----+-----+----+
| pod-1/bl2205-eu-spdc | 1/24      | down | no      | removed | unknown |      |      |    |     |    | 
+----------------------+-----------+------+---------+---------+---------+------+------+----+-----+----+

+----------------------+-----------+------+-----+---------------+---------+
| Node                 | Interface | Oper | EPG | Bridge Domain | Subnets |
+----------------------+-----------+------+-----+---------------+---------+
| pod-1/bl2205-eu-spdc | 1/24      | down |     |               |         | 
+----------------------+-----------+------+-----+---------------+---------+

+----------------------+-----------+------+---------+---------+------------+-----+---------------+------------+--------------+-----------------+
| Node                 | Interface | Oper | Native  | Primary | Oper Vlans | EPG | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+----------------------+-----------+------+---------+---------+------------+-----+---------------+------------+--------------+-----------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | unknown | vlan-1  |            |     |               |            |              |                 | 
+----------------------+-----------+------+---------+---------+------------+-----+---------------+------------+--------------+-----------------+

+----------------------+-----------+------+-----------------+-----------------+-----------------+
| Node                 | Interface | Oper | Load Interval 1 | Load Interval 2 | Load Interval 3 |
+----------------------+-----------+------+-----------------+-----------------+-----------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | 30              | 300             | 0               | 
+----------------------+-----------+------+-----------------+-----------------+-----------------+

+----------------------+-----------+------+----------+------------+----------------+
| Node                 | Interface | Oper | Eee Lat  | Eee Lpi    | Eee State      |
+----------------------+-----------+------+----------+------------+----------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | variable | aggressive | not-applicable | 
+----------------------+-----------+------+----------+------------+----------------+

+----------------------+-----------+------+-----------------+--------------+-------------+------------------+--------------+
| Node                 | Interface | Oper | CDP System Name | CDP Platform | CDP Port ID | LLDP System Name | LLDP Port ID |
+----------------------+-----------+------+-----------------+--------------+-------------+------------------+--------------+
| pod-1/bl2205-eu-spdc | 1/24      | down |                 |              |             |                  |              | 
+----------------------+-----------+------+-----------------+--------------+-------------+------------------+--------------+

+----------------------+-----------+------+-----------------+----------+---------+------------+-------+
| Node                 | Interface | Oper | CDP System Name | Platform | Port ID | Capability | State |
+----------------------+-----------+------+-----------------+----------+---------+------------+-------+
| pod-1/bl2205-eu-spdc | 1/24      | down |                 |          |         |            |       | 
+----------------------+-----------+------+-----------------+----------+---------+------------+-------+

+----------------------+-----------+------+------------------+---------+------------+---------+----------+-------+
| Node                 | Interface | Oper | LLDP System Name | Port ID | Capability | Mgmt IP | Mgmt MAC | State |
+----------------------+-----------+------+------------------+---------+------------+---------+----------+-------+
| pod-1/bl2205-eu-spdc | 1/24      | down |                  |         |            |         |          |       | 
+----------------------+-----------+------+------------------+---------+------------+---------+----------+-------+

+----------------------+-----------+------+------+-------------------+-------------------+------------+-----------+-----+-----+------+-----+
| Node                 | Interface | Oper | Type | Policy Group Type | Policy Group Name | Link Level | Link Flap | CDP | MCP | LLDP | STP |
+----------------------+-----------+------+------+-------------------+-------------------+------------+-----------+-----+-----+------+-----+
| pod-1/bl2205-eu-spdc | 1/24      | down | leaf |                   |                   |            |           |     |     |      |     | 
+----------------------+-----------+------+------+-------------------+-------------------+------------+-----------+-----+-----+------+-----+

+----------------------+-----------+------+------+------------------------+--------------------+-------------------+-------------------+-------------------------+
| Node                 | Interface | Oper | Type | Leaf Interface Profile | Interface Selector | Policy Group Type | Policy Group Name | Attached Entity Profile |
+----------------------+-----------+------+------+------------------------+--------------------+-------------------+-------------------+-------------------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | leaf |                        |                    |                   |                   |                         | 
+----------------------+-----------+------+------+------------------------+--------------------+-------------------+-------------------+-------------------------+

+----------------------+-----------+------+------+-------------------+-------------------------+-------------+-------------+
| Node                 | Interface | Oper | Type | Policy Group Name | Attached Entity Profile | Domain Type | Domain Name |
+----------------------+-----------+------+------+-------------------+-------------------------+-------------+-------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | leaf |                   |                         |             |             | 
+----------------------+-----------+------+------+-------------------+-------------------------+-------------+-------------+

+----------------------+-----------+-------+------+---------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| Node                 | Interface | Admin | Oper | Class         | Rx Admit [B] | Rx Admin | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin | Tx Drop [B] | Tx Drop |
+----------------------+-----------+-------+------+---------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| pod-1/bl2205-eu-spdc | eth1/24   | up    | down | control-plane | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | level1        | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | level2        | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | level3        | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | level4        | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | level5        | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | level6        | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | policy-plane  | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
|                      |           |       |      | span          | 0            | 0        | 0           | 0       | 0            | 0        | 0           | 0       | 
+----------------------+-----------+-------+------+---------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+

+----------------------+-----------+------+---------+-----------+-----------+----+----+----------------+---------------+---------------+---------------+---------------+----------------+
| Node                 | Interface | Oper | Packets | Broadcast | Multicast | Rx | Tx | Size up to 64B | Size 65-1270B | Size 128-255B | Size 256-511B | Size 512-1023 | Size 1024-1518 |
+----------------------+-----------+------+---------+-----------+-----------+----+----+----------------+---------------+---------------+---------------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | 0       | 0         | 0         | 0  | 0  | 0              | 0             | 0             | 0             | 0             | 0              | 
+----------------------+-----------+------+---------+-----------+-----------+----+----+----------------+---------------+---------------+---------------+---------------+----------------+

+----------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| Node                 | Interface | Oper | Oversize | Undersize | Rx giant | Rx oversize | Tx giant | Tx oversize | Collisions | CRC errors | Drops |
+----------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| pod-1/bl2205-eu-spdc | 1/24      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
+----------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+

Interface Phy - Faults [#0]
---------------------------
None

Interface Phy - Fault Records last 10y [#4]
-------------------------------------------

+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+-------------------------------------------+
| Node                 | Interface | Sev  | Code  | Cause                   | Created Time                  | Lifecycle        | Description                               |
+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+-------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Warn | F0546 | interface-physical-down | 2023-06-18T09:41:41.337+02:00 | soaking          | Port is down, reason:down(down), used by: | 
| pod-1/bl2205-eu-spdc | eth1/24   | Warn | F0546 | interface-physical-down | 2023-06-18T09:41:48.833+02:00 | soaking-clearing | Port is down, reason:down(down), used by: | 
| pod-1/bl2205-eu-spdc | eth1/24   | --   | F0546 | interface-physical-down | 2023-06-18T09:44:07.548+02:00 | retaining        | Port is down, reason:down(down), used by: | 
| pod-1/bl2205-eu-spdc | eth1/24   | --   | F0546 | interface-physical-down | 2023-06-18T10:44:09.092+02:00 |                  | Port is down, reason:down(down), used by: | 
+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+-------------------------------------------+

Interface Phy - Event Logs last 10y [#12]
-----------------------------------------

+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code     | Cause               | Created Time                  | Description                     | Change Set                                                                       |
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4208843 | transition          | 2023-06-12T09:55:44.533+02:00 | PhysIf eth1/24 modified         | adminSt:down, autoNeg:on, breakT:nonbroken, brkoutMap:none, bw:0, delay:1,       | 
|                      |           |      |          |                     |                               |                                 | dfeDelayMs:0, dot1qEtherType:0x8100, emiRetrain:disable, enablePoap:no,          | 
|                      |           |      |          |                     |                               |                                 | ethpmCfgFailedTs:00:00:00:00.000, ethpmCfgState:0, fcotChannelNumber:Channel32,  | 
|                      |           |      |          |                     |                               |                                 | fecMode:inherit, id:eth1/24, inhBw:unspecified,                                  | 
|                      |           |      |          |                     |                               |                                 | isReflectiveRelayCfgSupported:Supported, layer:Layer2, linkDebounce:100,         | 
|                      |           |      |          |                     |                               |                                 | linkFlapErrorMax:30, linkFlapErrorSeconds:420, linkLog:default, mdix:auto,       | 
|                      |           |      |          |                     |                               |                                 | medium:broadcast, mode:trunk, mtu:9000, portPhyMediaType:auto, portT:leaf,       | 
|                      |           |      |          |                     |                               |                                 | prioFlowCtrl:auto, reflectiveRelayEn:off, routerMac:not-applicable,              | 
|                      |           |      |          |                     |                               |                                 | snmpTrapSt:enable, spanMode:not-a-span-dest, speed:inherit,                      | 
|                      |           |      |          |                     |                               |                                 | switchingSt:disabled, trunkLog:default, usage:blacklist                          | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4205128 | port-down           | 2023-06-12T09:55:46.398+02:00 | Port is down.                   | bdlPortNum:255, bfdState:5, channelingSt:unknown, ltlProgrammed:no,              | 
|                      |           |      |          |                     |                               |                                 | operSt:down, pcMode:on, summOperSt:down, uptime:00:00:00:00.000                  | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4205128 | port-down           | 2023-06-12T09:55:46.060+02:00 | Port is down.                   | bdlPortNum:255, bfdState:5, channelingSt:unknown, ltlProgrammed:no,              | 
|                      |           |      |          |                     |                               |                                 | operSt:down, pcMode:on, summOperSt:down, uptime:00:00:00:00.000                  | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4210003 | transceiver-removed | 2023-06-12T09:55:48.164+02:00 | Transceiver has been removed    | actualType:unknown, baseResvd1:0, baseResvd2:0, baseResvd3:0, baseResvd4:0,0,0,  | 
|                      |           |      |          |                     |                               |                                 | brIn100MHz:0, brMaxMargin:0, brMinMargin:0, ccex:0, ccid:0, connectType:0,       | 
|                      |           |      |          |                     |                               |                                 | dateCode:0,0,0,0,0,0,0,0,                                                        | 
|                      |           |      |          |                     |                               |                                 | description:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, diagMonType:0,            | 
|                      |           |      |          |                     |                               |                                 | distIn100mFor9u:0, distIn10mFor50u:0, distIn10mFor60u:0, distIn1mForCu:0,        | 
|                      |           |      |          |                     |                               |                                 | distInKmFor9u:0, encoding:0, enhOption:0, extOption:0,0, fCTxType:0, fcotNum:0,  | 
|                      |           |      |          |                     |                               |                                 | fcotStatus:0, fcotType:0, flags:ok, gigEthCC:0, isFcotPresent:no, maxSpeed:11,   | 
|                      |           |      |          |                     |                               |                                 | minSpeed:11, partNumber:0,0,0,0,0,0,0,0,0,0,0, sff8472Compl:0, state:removed,    | 
|                      |           |      |          |                     |                               |                                 | type:unknown,                                                                    | 
|                      |           |      |          |                     |                               |                                 | vendorData:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,      | 
|                      |           |      |          |                     |                               |                                 | vendorId:0,0,0, vendorName:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,                      | 
|                      |           |      |          |                     |                               |                                 | vendorPn:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, vendorRev:0,0,0,0,                     | 
|                      |           |      |          |                     |                               |                                 | vendorSn:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, versionId:0,0,0,0,0,                   | 
|                      |           |      |          |                     |                               |                                 | xcvrCode:0,0,0,0,0,0,0,0, xcvrExtId:0, xcvrId:0                                  | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4215671 | port-down           | 2023-06-12T09:55:48.159+02:00 | Port is down. Reason: sfpAbsent | accessVlan:vlan-0, backplaneMac:3C:13:CC:B9:ED:C8, bundleBupId:1,                | 
|                      |           |      |          |                     |                               |                                 | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,             | 
|                      |           |      |          |                     |                               |                                 | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,             | 
|                      |           |      |          |                     |                               |                                 | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:28, lastErrors:0,    | 
|                      |           |      |          |                     |                               |                                 | lastLinkStChg:1970-01-01T00:00:00.000+00:00, media:2, nativeVlan:vlan-0,         | 
|                      |           |      |          |                     |                               |                                 | numOfSI:0, operBitset:19, operDceMode:edge, operDuplex:full, operEEERxWkTime:0,  | 
|                      |           |      |          |                     |                               |                                 | operEEEState:not-applicable, operEEETxWkTime:0, operErrDisQual:none,             | 
|                      |           |      |          |                     |                               |                                 | operFecMode:disable-fec, operFlowCtrl:0, operMdix:auto, operMode:trunk,          | 
|                      |           |      |          |                     |                               |                                 | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:00:00:00:00:00:00,    | 
|                      |           |      |          |                     |                               |                                 | operSpeed:100G, operSt:down, operStQual:sfp-missing, operStQualCode:0,           | 
|                      |           |      |          |                     |                               |                                 | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,   | 
|                      |           |      |          |                     |                               |                                 | usage:blacklist, userCfgdFlags:0, vdcId:1                                        | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4210003 | transceiver-removed | 2023-06-12T09:55:49.864+02:00 | Transceiver has been removed    | actualType:unknown, baseResvd1:0, baseResvd2:0, baseResvd3:0, baseResvd4:0,0,0,  | 
|                      |           |      |          |                     |                               |                                 | brIn100MHz:0, brMaxMargin:0, brMinMargin:0, ccex:0, ccid:0, connectType:0,       | 
|                      |           |      |          |                     |                               |                                 | dateCode:0,0,0,0,0,0,0,0,                                                        | 
|                      |           |      |          |                     |                               |                                 | description:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, diagMonType:0,            | 
|                      |           |      |          |                     |                               |                                 | distIn100mFor9u:0, distIn10mFor50u:0, distIn10mFor60u:0, distIn1mForCu:0,        | 
|                      |           |      |          |                     |                               |                                 | distInKmFor9u:0, encoding:0, enhOption:0, extOption:0,0, fCTxType:0, fcotNum:0,  | 
|                      |           |      |          |                     |                               |                                 | fcotStatus:0, fcotType:0, flags:ok, gigEthCC:0, isFcotPresent:no, maxSpeed:11,   | 
|                      |           |      |          |                     |                               |                                 | minSpeed:11, partNumber:0,0,0,0,0,0,0,0,0,0,0, sff8472Compl:0, state:removed,    | 
|                      |           |      |          |                     |                               |                                 | type:unknown,                                                                    | 
|                      |           |      |          |                     |                               |                                 | vendorData:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,      | 
|                      |           |      |          |                     |                               |                                 | vendorId:0,0,0, vendorName:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,                      | 
|                      |           |      |          |                     |                               |                                 | vendorPn:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, vendorRev:0,0,0,0,                     | 
|                      |           |      |          |                     |                               |                                 | vendorSn:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, versionId:0,0,0,0,0,                   | 
|                      |           |      |          |                     |                               |                                 | xcvrCode:0,0,0,0,0,0,0,0, xcvrExtId:0, xcvrId:0                                  | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4215671 | port-down           | 2023-06-12T09:55:49.855+02:00 | Port is down. Reason: sfpAbsent | accessVlan:vlan-0, backplaneMac:3C:13:CC:B9:ED:C8, bundleBupId:1,                | 
|                      |           |      |          |                     |                               |                                 | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,             | 
|                      |           |      |          |                     |                               |                                 | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,             | 
|                      |           |      |          |                     |                               |                                 | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:28, lastErrors:0,    | 
|                      |           |      |          |                     |                               |                                 | lastLinkStChg:1970-01-01T00:00:00.000+00:00, media:2, nativeVlan:vlan-0,         | 
|                      |           |      |          |                     |                               |                                 | numOfSI:0, operBitset:19, operDceMode:edge, operDuplex:full, operEEERxWkTime:0,  | 
|                      |           |      |          |                     |                               |                                 | operEEEState:not-applicable, operEEETxWkTime:0, operErrDisQual:none,             | 
|                      |           |      |          |                     |                               |                                 | operFecMode:disable-fec, operFlowCtrl:0, operMdix:auto, operMode:trunk,          | 
|                      |           |      |          |                     |                               |                                 | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:00:00:00:00:00:00,    | 
|                      |           |      |          |                     |                               |                                 | operSpeed:100G, operSt:down, operStQual:sfp-missing, operStQualCode:0,           | 
|                      |           |      |          |                     |                               |                                 | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,   | 
|                      |           |      |          |                     |                               |                                 | usage:blacklist, userCfgdFlags:0, vdcId:1                                        | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4208843 | transition          | 2023-06-12T11:30:18.372+02:00 | PhysIf eth1/24 modified         | ethpmCfgFailedBmp (New: ), ethpmCfgFailedTs (New: 00:00:00:00.000),              | 
|                      |           |      |          |                     |                               |                                 | ethpmCfgState (New: 0)                                                           | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4205128 | port-down           | 2023-06-18T09:41:47.238+02:00 | Port is down.                   | bdlPortNum:255, bfdState:5, channelingSt:unknown, ltlProgrammed:no,              | 
|                      |           |      |          |                     |                               |                                 | operSt:down, pcMode:on, summOperSt:down, uptime:00:00:00:00.000                  | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4210003 | transceiver-removed | 2023-06-18T09:41:48.842+02:00 | Transceiver has been removed    | actualType:unknown, baseResvd1:0, baseResvd2:0, baseResvd3:0, baseResvd4:0,0,0,  | 
|                      |           |      |          |                     |                               |                                 | brIn100MHz:0, brMaxMargin:0, brMinMargin:0, ccex:0, ccid:0, connectType:0,       | 
|                      |           |      |          |                     |                               |                                 | dateCode:0,0,0,0,0,0,0,0,                                                        | 
|                      |           |      |          |                     |                               |                                 | description:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, diagMonType:0,            | 
|                      |           |      |          |                     |                               |                                 | distIn100mFor9u:0, distIn10mFor50u:0, distIn10mFor60u:0, distIn1mForCu:0,        | 
|                      |           |      |          |                     |                               |                                 | distInKmFor9u:0, encoding:0, enhOption:0, extOption:0,0, fCTxType:0, fcotNum:0,  | 
|                      |           |      |          |                     |                               |                                 | fcotStatus:0, fcotType:0, flags:ok, gigEthCC:0, isFcotPresent:no, maxSpeed:11,   | 
|                      |           |      |          |                     |                               |                                 | minSpeed:11, partNumber:0,0,0,0,0,0,0,0,0,0,0, sff8472Compl:0, state:removed,    | 
|                      |           |      |          |                     |                               |                                 | type:unknown,                                                                    | 
|                      |           |      |          |                     |                               |                                 | vendorData:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,      | 
|                      |           |      |          |                     |                               |                                 | vendorId:0,0,0, vendorName:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,                      | 
|                      |           |      |          |                     |                               |                                 | vendorPn:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, vendorRev:0,0,0,0,                     | 
|                      |           |      |          |                     |                               |                                 | vendorSn:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, versionId:0,0,0,0,0,                   | 
|                      |           |      |          |                     |                               |                                 | xcvrCode:0,0,0,0,0,0,0,0, xcvrExtId:0, xcvrId:0                                  | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4215671 | port-down           | 2023-06-18T09:41:48.838+02:00 | Port is down. Reason: sfpAbsent | accessVlan (New: vlan-0), allowedVlans (New: ), backplaneMac (New:               | 
|                      |           |      |          |                     |                               |                                 | 3C:13:CC:B9:ED:C8), bundleBupId (New: 1), cfgAccessVlan (New: vlan-0),           | 
|                      |           |      |          |                     |                               |                                 | cfgNativeVlan (New: vlan-0), currErrIndex (New: 4294967295), diags (New: none),  | 
|                      |           |      |          |                     |                               |                                 | encap (New: 3), errVlans (New: ), intfT (New: phy), iod (New: 28), lastErrors    | 
|                      |           |      |          |                     |                               |                                 | (New: 0), media (New: 2), nativeVlan (New: vlan-0), operBitset (New: 19),        | 
|                      |           |      |          |                     |                               |                                 | operDceMode (New: edge), operDuplex (New: full), operEEEState (New:              | 
|                      |           |      |          |                     |                               |                                 | not-applicable), operErrDisQual (New: none), operFecMode (New: disable-fec),     | 
|                      |           |      |          |                     |                               |                                 | operMdix (New: auto), operMode (New: trunk), operSpeed (New: 100G), operSt       | 
|                      |           |      |          |                     |                               |                                 | (New: down), operStQual (New: sfp-missing), primaryVlan (New: vlan-1), siList    | 
|                      |           |      |          |                     |                               |                                 | (New: ), txT (New: unknown), usage (New: blacklist), vdcId (New: 1)              | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/24   | Info | E4208843 | transition          | 2023-06-18T09:45:16.531+02:00 | PhysIf eth1/24 modified         | ethpmCfgFailedBmp (New: ), ethpmCfgFailedTs (New: 00:00:00:00.000),              | 
|                      |           |      |          |                     |                               |                                 | ethpmCfgState (New: 0)                                                           | 
+----------------------+-----------+------+----------+---------------------+-------------------------------+---------------------------------+----------------------------------------------------------------------------------+

Interface Phy - Audit Logs last 10y [#0]
----------------------------------------
None
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id 1/24
    --view all

{
    "duration": 14304,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 447,
        "disconnect_time": 0,
        "mo_time": 11112,
        "total_time": 11559
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	447	-	connect apic21o.emea-sp.cisco.com:443
True	360	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	937	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	353	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	338	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	58	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=rmonEtherStats
True	393	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmFcot
True	382	42	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=l1LoadP
True	388	42	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=l1EeeP
True	433	7	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	356	10	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	646	7	apic21o.emea-sp.cisco.com:443 mo uni/infra/nodecfgcont/node-2205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	317	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-HX1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	330	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-Infra-BGP_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	346	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-ESX22-CDC-22_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	352	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-HX1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	373	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	344	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-UCSB1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	363	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-SPN_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	381	324	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/qosmIfClass
True	549	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1189	1000	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1104	935	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	522	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfacePhy.md)