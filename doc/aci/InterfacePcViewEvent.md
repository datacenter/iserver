# Node Interface - Port Channel (PC)

## Event view

```
# iserver get aci intf pc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Port Channel Event Logs last 10y [#29]
------------------------------------------------

+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code     | Cause     | Created Time                  | Description                         | Change Set                                                                      |
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215670 | port-up   | 2023-06-04T18:38:23.660+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-04T18:38:23.604+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), operVlans (New: 2-3,6-7,12-15,17-18), resetCtr (New: 1) | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215671 | port-down | 2023-06-04T18:48:31.988+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-04T18:48:31.954+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215670 | port-up   | 2023-06-04T18:55:25.157+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-04T18:55:25.103+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), operVlans (New: 2-3,6-7,12-15,17-18), resetCtr (New: 2) | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po3       | Info | E4215671 | port-down | 2023-06-07T11:56:52.522+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-07T11:56:52.487+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215671 | port-down | 2023-06-07T11:57:06.899+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-07T11:57:06.850+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215671 | port-down | 2023-06-07T17:03:04.226+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-07T17:03:04.142+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po4       | Info | E4215671 | port-down | 2023-06-07T18:12:47.290+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-07T18:12:47.256+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po4       | Info | E4215670 | port-up   | 2023-06-07T18:23:25.667+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-07T18:23:25.612+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 2)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po5       | Info | E4215671 | port-down | 2023-06-07T18:50:05.492+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-07T18:50:05.467+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po5       | Info | E4215670 | port-up   | 2023-06-07T19:00:37.580+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-07T19:00:37.529+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 2)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po6       | Info | E4215671 | port-down | 2023-06-12T11:29:04.671+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:59, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215670 | port-up   | 2023-06-12T11:31:16.883+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:16.829+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po4       | Info | E4215670 | port-up   | 2023-06-12T11:31:21.584+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:21.500+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po6       | Info | E4215670 | port-up   | 2023-06-12T11:31:21.660+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:21.568+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po3       | Info | E4215670 | port-up   | 2023-06-12T11:31:24.831+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:24.778+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po5       | Info | E4215670 | port-up   | 2023-06-12T11:31:24.555+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:24.455+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215670 | port-up   | 2023-06-12T11:31:26.518+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:26.478+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), operVlans (New: 3-4,17-20), resetCtr (New: 1)           | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215671 | port-down | 2023-06-18T09:45:00.384+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:45, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215671 | port-down | 2023-06-18T09:45:00.395+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:46, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po3       | Info | E4215671 | port-down | 2023-06-18T09:45:00.406+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:65, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po4       | Info | E4215671 | port-down | 2023-06-18T09:45:00.373+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:44, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po5       | Info | E4215671 | port-down | 2023-06-18T09:45:00.437+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:66, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po6       | Info | E4215671 | port-down | 2023-06-18T09:45:00.449+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:67, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po3       | Info | E4215670 | port-up   | 2023-06-18T09:47:18.583+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:18.508+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po4       | Info | E4215670 | port-up   | 2023-06-18T09:47:19.606+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:19.532+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Info | E4215670 | port-up   | 2023-06-18T09:47:22.832+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:22.662+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po5       | Info | E4215670 | port-up   | 2023-06-18T09:47:22.717+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:22.621+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), operVlans (New: 1,4-5,11-16,20), resetCtr (New: 1)      | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po6       | Info | E4215670 | port-up   | 2023-06-18T09:47:23.015+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:22.928+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215670 | port-up   | 2023-06-18T09:47:29.670+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:29.600+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf pc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

{
    "duration": 3930,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 1426,
        "disconnect_time": 0,
        "mo_time": 1815,
        "total_time": 3241
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

True	1426	-	connect apic21o.emea-sp.cisco.com:443
True	321	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	489	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	309	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	297	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	399	112	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfacePc.md)