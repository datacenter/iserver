# Compute Blade

## Managed Object

```
Managed Object			:	ComputeBlade
--------------
class_id                        :ComputeBlade
admin_power                     :policy
admin_state                     :in-service
asset_tag                       :
assigned_to_dn                  :org-root/org-EU-SPN/ls-esx52-eu-spdc
association                     :associated
availability                    :unavailable
available_memory                :393216
chassis_id                      :2
check_point                     :discovered
child_action                    :None
conn_path                       :A,B
conn_status                     :A,B
descr                           :
discovery                       :complete
discovery_status                :
dn                              :sys/chassis-2/blade-2
flt_aggr                        :0
fsm_descr                       :
fsm_flags                       :
fsm_prev                        :TurnupSuccess
fsm_progr                       :100
fsm_rmt_inv_err_code            :none
fsm_rmt_inv_err_descr           :
fsm_rmt_inv_rslt                :
fsm_stage_descr                 :
fsm_stamp                       :2022-12-01T04:36:48.811
fsm_status                      :nop
fsm_try                         :0
int_id                          :213098
kmip_fault                      :no
kmip_fault_description          :Unavailable
lc                              :discovered
lc_ts                           :1970-01-01T01:00:00.000
local_id                        :
low_voltage_memory              :regular-voltage
managing_inst                   :A
memory_speed                    :2666
mfg_time                        :2020-04-06T01:00:00.000
model                           :UCSB-B200-M5
name                            :
num_of40_g_adaptors_with_old_fw :0
num_of40_g_adaptors_with_unknown_fw:0
num_of_adaptors                 :2
num_of_cores                    :40
num_of_cores_enabled            :40
num_of_cpus                     :2
num_of_eth_host_ifs             :8
num_of_fc_host_ifs              :0
num_of_threads                  :80
oper_power                      :on
oper_pwr_trans_src              :software_mcserver
oper_qualifier                  :
oper_qualifier_reason           :N/A
oper_state                      :ok
operability                     :operable
original_uuid                   :7416340d-6922-47f7-8924-050b800c4eb7
part_number                     :68-5800-07
policy_level                    :0
policy_owner                    :local
presence                        :equipped
revision                        :0
rn                              :blade-2
sacl                            :None
scaled_mode                     :none
serial                          :FLM24140BJB
server_id                       :2/2
slot_id                         :2
status                          :None
storage_oper_qualifier          :unknown
total_memory                    :393216
usr_lbl                         :
uuid                            :315220a5-2121-4e5b-0101-e1dc0000011f
vendor                          :Cisco Systems Inc
vid                             :V07
```

## Properties

```
[
    "DUMMY_DIRTY",
    "_ManagedObject__internal_prop",
    "_ManagedObject__parent_dn",
    "_ManagedObject__parent_mo",
    "_ManagedObject__set_prop",
    "_ManagedObject__status",
    "_ManagedObject__xtra_props",
    "_ManagedObject__xtra_props_dirty_mask",
    "__class__",
    "__deepcopy__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__json__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
    "_child",
    "_class_id",
    "_dirty_mask",
    "_dn_set",
    "_handle",
    "_is_unknown_property",
    "_rn_set",
    "_set_child_of_parent_mo",
    "_set_mo_prop_value",
    "_set_parent_mo_or_dn",
    "admin_power",
    "admin_state",
    "asset_tag",
    "assigned_to_dn",
    "association",
    "attr_get",
    "attr_set",
    "availability",
    "available_memory",
    "chassis_id",
    "check_point",
    "check_prop_match",
    "child",
    "child_action",
    "child_add",
    "child_count",
    "child_is_dirty",
    "child_mark_clean",
    "child_remove",
    "child_to_xml",
    "clone",
    "conn_path",
    "conn_status",
    "consts",
    "descr",
    "dirty_mask",
    "discovery",
    "discovery_status",
    "dn",
    "elem_create",
    "flt_aggr",
    "from_xml",
    "fsm_descr",
    "fsm_flags",
    "fsm_prev",
    "fsm_progr",
    "fsm_rmt_inv_err_code",
    "fsm_rmt_inv_err_descr",
    "fsm_rmt_inv_rslt",
    "fsm_stage_descr",
    "fsm_stamp",
    "fsm_status",
    "fsm_try",
    "get_class_id",
    "get_handle",
    "int_id",
    "is_dirty",
    "kmip_fault",
    "kmip_fault_description",
    "lc",
    "lc_ts",
    "local_id",
    "low_voltage_memory",
    "make_rn",
    "managing_inst",
    "mark_clean",
    "mark_dirty",
    "memory_speed",
    "mfg_time",
    "mo_meta",
    "model",
    "name",
    "naming_props",
    "num_of40_g_adaptors_with_old_fw",
    "num_of40_g_adaptors_with_unknown_fw",
    "num_of_adaptors",
    "num_of_cores",
    "num_of_cores_enabled",
    "num_of_cpus",
    "num_of_eth_host_ifs",
    "num_of_fc_host_ifs",
    "num_of_threads",
    "oper_power",
    "oper_pwr_trans_src",
    "oper_qualifier",
    "oper_qualifier_reason",
    "oper_state",
    "operability",
    "original_uuid",
    "parent_mo",
    "part_number",
    "policy_level",
    "policy_owner",
    "presence",
    "prop_map",
    "prop_meta",
    "revision",
    "rn",
    "rn_get_special_case",
    "rn_is_special_case",
    "sacl",
    "scaled_mode",
    "serial",
    "server_id",
    "set_prop_multiple",
    "show_hierarchy",
    "show_tree",
    "slot_id",
    "status",
    "storage_oper_qualifier",
    "sync_mo",
    "to_xml",
    "total_memory",
    "usr_lbl",
    "uuid",
    "vendor",
    "vid",
    "write_object"
]
```

## Meta

```
[EquipmentChassis]
  |-ComputeBlade
     |-AaaEpAuthProfile
     |  |-AaaEpUser
     |     |-AaaCimcSession
     |-AaaEpUser
     |  |-AaaCimcSession
     |-AdaptorHostIfConfig
     |-AdaptorUnit
     |  |-AdaptorExtEthIf
     |  |  |-AdaptorEthPortBySizeLargeStats
     |  |  |  |-AdaptorEthPortBySizeLargeStatsHist
     |  |  |-AdaptorEthPortBySizeSmallStats
     |  |  |  |-AdaptorEthPortBySizeSmallStatsHist
     |  |  |-AdaptorEthPortErrStats
     |  |  |  |-AdaptorEthPortErrStatsHist
     |  |  |-AdaptorEthPortMcastStats
     |  |  |  |-AdaptorEthPortMcastStatsHist
     |  |  |-AdaptorEthPortOutsizedStats
     |  |  |  |-AdaptorEthPortOutsizedStatsHist
     |  |  |-AdaptorEthPortStats
     |  |  |  |-AdaptorEthPortStatsHist
     |  |  |-AdaptorExtEthIfFsm
     |  |  |  |-AdaptorExtEthIfFsmStage
     |  |  |-AdaptorExtEthIfFsmTask
     |  |  |-DcxVIf
     |  |  |  |-FaultInst
     |  |  |-EventInst
     |  |  |-FabricEthMonSrcEp
     |  |  |-FaultInst
     |  |-AdaptorExtEthIfPc
     |  |  |-AdaptorExtEthIfPcEp
     |  |  |-DcxVIf
     |  |     |-FaultInst
     |  |-AdaptorHostEthIf
     |  |  |-AdaptorAzureQosProfile
     |  |  |-AdaptorEthAdvFilterProfile
     |  |  |-AdaptorEthArfsProfile
     |  |  |-AdaptorEthCompQueueProfile
     |  |  |-AdaptorEthFailoverProfile
     |  |  |-AdaptorEthGENEVEProfile
     |  |  |-AdaptorEthInterruptProfile
     |  |  |-AdaptorEthInterruptScalingProfile
     |  |  |-AdaptorEthNVGREProfile
     |  |  |-AdaptorEthOffloadProfile
     |  |  |-AdaptorEthPortBySizeLargeStats
     |  |  |  |-AdaptorEthPortBySizeLargeStatsHist
     |  |  |-AdaptorEthPortBySizeSmallStats
     |  |  |  |-AdaptorEthPortBySizeSmallStatsHist
     |  |  |-AdaptorEthPortErrStats
     |  |  |  |-AdaptorEthPortErrStatsHist
     |  |  |-AdaptorEthPortMcastStats
     |  |  |  |-AdaptorEthPortMcastStatsHist
     |  |  |-AdaptorEthPortOutsizedStats
     |  |  |  |-AdaptorEthPortOutsizedStatsHist
     |  |  |-AdaptorEthPortStats
     |  |  |  |-AdaptorEthPortStatsHist
     |  |  |-AdaptorEthRecvQueueProfile
     |  |  |-AdaptorEthRoCEProfile
     |  |  |-AdaptorEthVxLANProfile
     |  |  |-AdaptorEthWorkQueueProfile
     |  |  |-AdaptorExtIpV6RssHashProfile
     |  |  |-AdaptorFcOEIf
     |  |  |  |-DcxVIf
     |  |  |     |-FaultInst
     |  |  |-AdaptorHostEthIfFsm
     |  |  |  |-AdaptorHostEthIfFsmStage
     |  |  |-AdaptorHostEthIfFsmTask
     |  |  |-AdaptorIpV4RssHashProfile
     |  |  |-AdaptorIpV6RssHashProfile
     |  |  |-AdaptorPTP
     |  |  |-AdaptorRssProfile
     |  |  |-AdaptorUsnicConnDef
     |  |  |  |-AdaptorEthCompQueueProfile
     |  |  |  |-AdaptorEthFailoverProfile
     |  |  |  |-AdaptorEthInterruptProfile
     |  |  |  |-AdaptorEthInterruptScalingProfile
     |  |  |  |-AdaptorEthOffloadProfile
     |  |  |  |-AdaptorEthRecvQueueProfile
     |  |  |  |-AdaptorEthWorkQueueProfile
     |  |  |  |-AdaptorExtIpV6RssHashProfile
     |  |  |  |-AdaptorIpV4RssHashProfile
     |  |  |  |-AdaptorIpV6RssHashProfile
     |  |  |  |-AdaptorRssProfile
     |  |  |-AdaptorVlan
     |  |  |  |-AdaptorEtherIfStats
     |  |  |  |  |-AdaptorEtherIfStatsHist
     |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIPv4Dhcp
     |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIPv4IscsiAddr
     |  |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIPv4PooledIscsiAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIPv4Dns
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIPv4StaticRoute
     |  |  |  |-VnicIScsiAutoTargetIf
     |  |  |  |-VnicIScsiStaticTargetIf
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicLun
     |  |  |  |-VnicIpV4MgmtPooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4PooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |  |-VnicIpV4StaticAddr
     |  |  |-AdaptorVmmqConnDef
     |  |  |  |-AdaptorEthCompQueueProfile
     |  |  |  |-AdaptorEthInterruptProfile
     |  |  |  |-AdaptorEthRecvQueueProfile
     |  |  |  |-AdaptorEthRoCEProfile
     |  |  |  |-AdaptorEthWorkQueueProfile
     |  |  |  |-AdaptorRssProfile
     |  |  |-AdaptorVnicStats
     |  |  |  |-AdaptorVnicStatsHist
     |  |  |-DcxVIf
     |  |  |  |-FaultInst
     |  |  |-DhcpAcquired
     |  |  |-EventInst
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-MgmtIf
     |  |  |  |-DhcpAcquired
     |  |  |  |-EventInst
     |  |  |  |-FaultInst
     |  |  |  |-MgmtIPv6IfConfig
     |  |  |  |  |-MgmtIPv6IfAddr
     |  |  |  |     |-EventInst
     |  |  |  |     |-FaultInst
     |  |  |  |     |-MgmtIPv6IfAddrFsm
     |  |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |  |  |     |-MgmtIPv6IfAddrFsmTask
     |  |  |  |-MgmtIfFsm
     |  |  |  |  |-MgmtIfFsmStage
     |  |  |  |-MgmtIfFsmTask
     |  |  |-NetworkIfStats
     |  |-AdaptorHostFcIf
     |  |  |-AdaptorFcCdbWorkQueueProfile
     |  |  |-AdaptorFcErrorRecoveryProfile
     |  |  |-AdaptorFcFnicProfile
     |  |  |-AdaptorFcIfEventStats
     |  |  |  |-AdaptorFcIfEventStatsHist
     |  |  |-AdaptorFcIfFC4Stats
     |  |  |  |-AdaptorFcIfFC4StatsHist
     |  |  |-AdaptorFcIfFrameStats
     |  |  |  |-AdaptorFcIfFrameStatsHist
     |  |  |-AdaptorFcInterruptProfile
     |  |  |-AdaptorFcOEIf
     |  |  |  |-DcxVIf
     |  |  |     |-FaultInst
     |  |  |-AdaptorFcPortFLogiProfile
     |  |  |-AdaptorFcPortPLogiProfile
     |  |  |-AdaptorFcPortProfile
     |  |  |-AdaptorFcPortStats
     |  |  |  |-AdaptorFcPortStatsHist
     |  |  |-AdaptorFcRecvQueueProfile
     |  |  |-AdaptorFcVhbaTypeProfile
     |  |  |-AdaptorFcWorkQueueProfile
     |  |  |-AdaptorHostFcIfFsm
     |  |  |  |-AdaptorHostFcIfFsmStage
     |  |  |-AdaptorHostFcIfFsmTask
     |  |  |-AdaptorVnicStats
     |  |  |  |-AdaptorVnicStatsHist
     |  |  |-AdaptorVsan
     |  |  |-DcxVIf
     |  |  |  |-FaultInst
     |  |  |-EventInst
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-NetworkIfStats
     |  |-AdaptorHostIscsiIf
     |  |  |-AdaptorIscsiProt
     |  |  |-AdaptorIscsiTargetIf
     |  |  |-AdaptorProtocolProfile
     |  |  |-AdaptorVlan
     |  |  |  |-AdaptorEtherIfStats
     |  |  |  |  |-AdaptorEtherIfStatsHist
     |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIPv4Dhcp
     |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIPv4IscsiAddr
     |  |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIPv4PooledIscsiAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIPv4Dns
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIPv4StaticRoute
     |  |  |  |-VnicIScsiAutoTargetIf
     |  |  |  |-VnicIScsiStaticTargetIf
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicLun
     |  |  |  |-VnicIpV4MgmtPooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4PooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |  |-VnicIpV4StaticAddr
     |  |  |-AdaptorVnicStats
     |  |  |  |-AdaptorVnicStatsHist
     |  |  |-FabricNetflowIPv4Addr
     |  |  |-FaultInst
     |  |  |-NetworkIfStats
     |  |  |-VnicIPv4Dhcp
     |  |  |-VnicIPv4Dns
     |  |  |-VnicIPv4IscsiAddr
     |  |  |  |-VnicIPv4Dns
     |  |  |-VnicIPv4PooledIscsiAddr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIpV4History
     |  |  |-VnicIPv4StaticRoute
     |  |  |-VnicIpV4MgmtPooledAddr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIpV4History
     |  |  |-VnicIpV4PooledAddr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIpV4History
     |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |-VnicIpV4StaticAddr
     |  |-AdaptorHostPort
     |  |-AdaptorHostScsiIf
     |  |  |-AdaptorHostScsiLunRef
     |  |  |-AdaptorVnicStats
     |  |  |  |-AdaptorVnicStatsHist
     |  |  |-FaultInst
     |  |  |-NetworkIfStats
     |  |-AdaptorHostServiceEthIf
     |  |  |-AdaptorVlan
     |  |  |  |-AdaptorEtherIfStats
     |  |  |  |  |-AdaptorEtherIfStatsHist
     |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIPv4Dhcp
     |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIPv4IscsiAddr
     |  |  |  |  |-VnicIPv4Dns
     |  |  |  |-VnicIPv4PooledIscsiAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIPv4Dns
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIPv4StaticRoute
     |  |  |  |-VnicIScsiAutoTargetIf
     |  |  |  |-VnicIScsiStaticTargetIf
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicLun
     |  |  |  |-VnicIpV4MgmtPooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4PooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |  |-VnicIpV4StaticAddr
     |  |  |-AdaptorVnicStats
     |  |  |  |-AdaptorVnicStatsHist
     |  |  |-DcxVIf
     |  |  |  |-FaultInst
     |  |  |-FaultInst
     |  |  |-NetworkIfStats
     |  |-AdaptorMenloDcePortStats
     |  |  |-AdaptorMenloDcePortStatsHist
     |  |-AdaptorMenloEthErrorStats
     |  |  |-AdaptorMenloEthErrorStatsHist
     |  |-AdaptorMenloEthStats
     |  |  |-AdaptorMenloEthStatsHist
     |  |-AdaptorMenloFcErrorStats
     |  |  |-AdaptorMenloFcErrorStatsHist
     |  |-AdaptorMenloFcStats
     |  |  |-AdaptorMenloFcStatsHist
     |  |-AdaptorMenloHostPortStats
     |  |  |-AdaptorMenloHostPortStatsHist
     |  |-AdaptorMenloMcpuErrorStats
     |  |  |-AdaptorMenloMcpuErrorStatsHist
     |  |-AdaptorMenloMcpuStats
     |  |  |-AdaptorMenloMcpuStatsHist
     |  |-AdaptorMenloNetEgStats
     |  |  |-AdaptorMenloNetEgStatsHist
     |  |-AdaptorMenloNetInStats
     |  |  |-AdaptorMenloNetInStatsHist
     |  |-AdaptorMenloQErrorStats
     |  |  |-AdaptorMenloQErrorStatsHist
     |  |-AdaptorMenloQStats
     |  |  |-AdaptorMenloQStatsHist
     |  |-AdaptorUnitExtn
     |  |  |-EquipmentInventoryStatus
     |  |  |  |-FaultInst
     |  |  |-FaultInst
     |  |-DcxNs
     |  |  |-FaultInst
     |  |-EquipmentInventoryStatus
     |  |  |-FaultInst
     |  |-EquipmentPOST
     |  |-EquipmentPciDef
     |  |-FaultInst
     |  |-MgmtController
     |     |-CimcvmediaActualMountList
     |     |  |-CimcvmediaActualMountEntry
     |     |  |  |-FaultInst
     |     |  |-CimcvmediaExtMgmtRuleEntry
     |     |-EventInst
     |     |-FabricLocale
     |     |  |-AdaptorExtEthIfPc
     |     |  |  |-AdaptorExtEthIfPcEp
     |     |  |  |-DcxVIf
     |     |  |     |-FaultInst
     |     |  |-DcxVc
     |     |  |  |-FabricNetGroupRef
     |     |  |  |  |-FaultInst
     |     |  |  |-FabricSanGroupRef
     |     |  |  |  |-FaultInst
     |     |  |  |-FaultInst
     |     |  |  |-SwCmclan
     |     |  |  |  |-FabricNetGroupRef
     |     |  |  |     |-FaultInst
     |     |  |  |-SwNetflowMonitorRef
     |     |  |  |-SwUlan
     |     |  |  |-SwVlan
     |     |  |  |  |-FabricNetflowIPv4Addr
     |     |  |  |  |-FaultInst
     |     |  |  |-SwVsan
     |     |  |     |-SwFcZoneSet
     |     |  |        |-SwFcServerZoneGroup
     |     |  |        |  |-SwZoneInitiatorMember
     |     |  |        |     |-SwFcZone
     |     |  |        |        |-SwZoneTargetMember
     |     |  |        |-SwFcUserZoneGroup
     |     |  |           |-SwFcUserZone
     |     |  |              |-SwFcEndpoint
     |     |  |-FabricPath
     |     |     |-DcxVc
     |     |     |  |-FabricNetGroupRef
     |     |     |  |  |-FaultInst
     |     |     |  |-FabricSanGroupRef
     |     |     |  |  |-FaultInst
     |     |     |  |-FaultInst
     |     |     |  |-SwCmclan
     |     |     |  |  |-FabricNetGroupRef
     |     |     |  |     |-FaultInst
     |     |     |  |-SwNetflowMonitorRef
     |     |     |  |-SwUlan
     |     |     |  |-SwVlan
     |     |     |  |  |-FabricNetflowIPv4Addr
     |     |     |  |  |-FaultInst
     |     |     |  |-SwVsan
     |     |     |     |-SwFcZoneSet
     |     |     |        |-SwFcServerZoneGroup
     |     |     |        |  |-SwZoneInitiatorMember
     |     |     |        |     |-SwFcZone
     |     |     |        |        |-SwZoneTargetMember
     |     |     |        |-SwFcUserZoneGroup
     |     |     |           |-SwFcUserZone
     |     |     |              |-SwFcEndpoint
     |     |     |-FabricPathConn
     |     |     |  |-FabricPathEp
     |     |     |     |-PortTrustMode
     |     |     |-FabricPathEp
     |     |        |-PortTrustMode
     |     |-FaultInst
     |     |-FirmwareBootDefinition
     |     |  |-FirmwareBootUnit
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareInstallable
     |     |  |  |  |-FirmwareUcscInfo
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUcscInfo
     |     |-FirmwareImage
     |     |  |-EventInst
     |     |  |-FaultInst
     |     |  |-FirmwareImageFsm
     |     |  |  |-FirmwareImageFsmStage
     |     |  |-FirmwareImageFsmTask
     |     |  |-FirmwareInstallable
     |     |  |  |-FirmwareUcscInfo
     |     |  |-FirmwareModule
     |     |-FirmwareRunning
     |     |  |-FirmwareServicePack
     |     |-FirmwareUpdatable
     |     |  |-FaultInst
     |     |  |-FirmwareInstallable
     |     |     |-FirmwareUcscInfo
     |     |-MgmtCimcSecureBoot
     |     |-MgmtCmcSecureBoot
     |     |-MgmtConnection
     |     |  |-FaultInst
     |     |-MgmtControllerFsm
     |     |  |-MgmtControllerFsmStage
     |     |-MgmtControllerFsmTask
     |     |-MgmtHealthStatus
     |     |  |-FaultInst
     |     |  |-MgmtHealthAttr
     |     |-MgmtIf
     |     |  |-DhcpAcquired
     |     |  |-EventInst
     |     |  |-FaultInst
     |     |  |-MgmtIPv6IfConfig
     |     |  |  |-MgmtIPv6IfAddr
     |     |  |     |-EventInst
     |     |  |     |-FaultInst
     |     |  |     |-MgmtIPv6IfAddrFsm
     |     |  |     |  |-MgmtIPv6IfAddrFsmStage
     |     |  |     |-MgmtIPv6IfAddrFsmTask
     |     |  |-MgmtIfFsm
     |     |  |  |-MgmtIfFsmStage
     |     |  |-MgmtIfFsmTask
     |     |-MgmtInterface
     |     |  |-FaultInst
     |     |  |-MgmtVnet
     |     |     |-VnicIpV4MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4PooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4StaticAddr
     |     |     |-VnicIpV6MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV6History
     |     |     |-VnicIpV6StaticAddr
     |     |-MgmtKvmCertificate
     |     |  |-FaultInst
     |     |-MgmtProfDerivedInterface
     |     |  |-MgmtVnet
     |     |     |-VnicIpV4MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4PooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4StaticAddr
     |     |     |-VnicIpV6MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV6History
     |     |     |-VnicIpV6StaticAddr
     |     |-MgmtSpdmCertificateInventory
     |     |  |-MgmtSpdmCertificateData
     |     |-MgmtSwPersonalities
     |     |  |-MgmtSwPersonality
     |     |-MgmtSwPersonalitiesInventory
     |     |  |-MgmtSwPersonality
     |     |-MgmtUsbNicMgmtIf
     |     |-SysdebugMEpLog
     |     |  |-FaultInst
     |     |-VnicIpV4PooledAddr
     |     |  |-FaultInst
     |     |  |-VnicIpV4History
     |     |-VnicIpV4ProfDerivedAddr
     |     |-VnicIpV4StaticAddr
     |-BiosUnit
     |  |-BiosBOT
     |  |  |-BiosBootDevGrp
     |  |     |-BiosBootDev
     |  |-BiosSettings
     |  |  |-BiosTokenFeatureGroup
     |  |  |  |-BiosTokenParam
     |  |  |     |-BiosTokenSettings
     |  |  |-BiosTokenParam
     |  |  |  |-BiosTokenSettings
     |  |  |-BiosVfACPI10Support
     |  |  |-BiosVfASPMSupport
     |  |  |-BiosVfAllUSBDevices
     |  |  |-BiosVfAltitude
     |  |  |-BiosVfAssertNMIOnPERR
     |  |  |-BiosVfAssertNMIOnSERR
     |  |  |-BiosVfBMEDMAMitigation
     |  |  |-BiosVfBootOptionRetry
     |  |  |-BiosVfCPUHardwarePowerManagement
     |  |  |-BiosVfCPUPerformance
     |  |  |-BiosVfConsistentDeviceNameControl
     |  |  |-BiosVfConsoleRedirection
     |  |  |-BiosVfCoreMultiProcessing
     |  |  |-BiosVfDDR3VoltageSelection
     |  |  |-BiosVfDRAMClockThrottling
     |  |  |-BiosVfDirectCacheAccess
     |  |  |-BiosVfDramRefreshRate
     |  |  |-BiosVfEnergyPerformanceTuning
     |  |  |-BiosVfEnhancedIntelSpeedStepTech
     |  |  |-BiosVfEnhancedPowerCappingSupport
     |  |  |-BiosVfExecuteDisableBit
     |  |  |-BiosVfFRB2Timer
     |  |  |-BiosVfFrequencyFloorOverride
     |  |  |-BiosVfFrontPanelLockout
     |  |  |-BiosVfIOEMezz1OptionROM
     |  |  |-BiosVfIOENVMe1OptionROM
     |  |  |-BiosVfIOENVMe2OptionROM
     |  |  |-BiosVfIOESlot1OptionROM
     |  |  |-BiosVfIOESlot2OptionROM
     |  |  |-BiosVfIntegratedGraphics
     |  |  |-BiosVfIntegratedGraphicsApertureSize
     |  |  |-BiosVfIntelEntrySASRAIDModule
     |  |  |-BiosVfIntelHyperThreadingTech
     |  |  |-BiosVfIntelTrustedExecutionTechnology
     |  |  |-BiosVfIntelTurboBoostTech
     |  |  |-BiosVfIntelVTForDirectedIO
     |  |  |-BiosVfIntelVirtualizationTechnology
     |  |  |-BiosVfInterleaveConfiguration
     |  |  |-BiosVfLocalX2Apic
     |  |  |-BiosVfLvDIMMSupport
     |  |  |-BiosVfMaxVariableMTRRSetting
     |  |  |-BiosVfMaximumMemoryBelow4GB
     |  |  |-BiosVfMemoryMappedIOAbove4GB
     |  |  |-BiosVfMirroringMode
     |  |  |-BiosVfNUMAOptimized
     |  |  |-BiosVfOSBootWatchdogTimer
     |  |  |-BiosVfOSBootWatchdogTimerPolicy
     |  |  |-BiosVfOSBootWatchdogTimerTimeout
     |  |  |-BiosVfOnboardGraphics
     |  |  |-BiosVfOnboardSATAController
     |  |  |-BiosVfOnboardStorage
     |  |  |-BiosVfOptionROMEnable
     |  |  |-BiosVfOptionROMLoad
     |  |  |-BiosVfOutOfBandManagement
     |  |  |-BiosVfPCHSATAMode
     |  |  |-BiosVfPCILOMPortsConfiguration
     |  |  |-BiosVfPCIROMCLP
     |  |  |-BiosVfPCISlotLinkSpeed
     |  |  |-BiosVfPCISlotOptionROMEnable
     |  |  |-BiosVfPOSTErrorPause
     |  |  |-BiosVfPSTATECoordination
     |  |  |-BiosVfPackageCStateLimit
     |  |  |-BiosVfPanicAndHighWatermark
     |  |  |-BiosVfProcessorC1E
     |  |  |-BiosVfProcessorC3Report
     |  |  |-BiosVfProcessorC6Report
     |  |  |-BiosVfProcessorC7Report
     |  |  |-BiosVfProcessorCMCI
     |  |  |-BiosVfProcessorCState
     |  |  |-BiosVfProcessorEnergyConfiguration
     |  |  |-BiosVfProcessorPrefetchConfig
     |  |  |-BiosVfQPILinkFrequencySelect
     |  |  |-BiosVfQPISnoopMode
     |  |  |-BiosVfQuietBoot
     |  |  |-BiosVfRedirectionAfterBIOSPOST
     |  |  |-BiosVfResumeOnACPowerLoss
     |  |  |-BiosVfSBMezz1OptionROM
     |  |  |-BiosVfSBNVMe1OptionROM
     |  |  |-BiosVfSIOC1OptionROM
     |  |  |-BiosVfSIOC2OptionROM
     |  |  |-BiosVfScrubPolicies
     |  |  |-BiosVfSelectMemoryRASConfiguration
     |  |  |-BiosVfSerialPortAEnable
     |  |  |-BiosVfSparingMode
     |  |  |-BiosVfSriovConfig
     |  |  |-BiosVfTPMPendingOperation
     |  |  |-BiosVfTPMSupport
     |  |  |-BiosVfTrustedPlatformModule
     |  |  |-BiosVfUCSMBootModeControl
     |  |  |-BiosVfUCSMBootOrderRuleControl
     |  |  |-BiosVfUEFIOSUseLegacyVideo
     |  |  |-BiosVfUSBBootConfig
     |  |  |-BiosVfUSBConfiguration
     |  |  |-BiosVfUSBFrontPanelAccessLock
     |  |  |-BiosVfUSBPortConfiguration
     |  |  |-BiosVfUSBSystemIdlePowerOptimizingSetting
     |  |  |-BiosVfVGAPriority
     |  |  |-BiosVfWorkloadConfiguration
     |  |-FaultInst
     |  |-FirmwareBootDefinition
     |  |  |-FirmwareBootUnit
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareInstallable
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareServicePack
     |  |  |-FirmwareUcscInfo
     |  |-FirmwareRunning
     |  |  |-FirmwareServicePack
     |  |-FirmwareUpdatable
     |     |-FaultInst
     |     |-FirmwareInstallable
     |        |-FirmwareUcscInfo
     |-BiosVIdentityParams
     |-CimcvmediaMountConfigDef
     |  |-CimcvmediaConfigMountEntry
     |-ComputeAdminAck
     |  |-FaultInst
     |  |-TrigLocalSched
     |     |-TrigAbsWindow
     |     |-TrigLocalAbsWindow
     |     |-TrigRecurrWindow
     |-ComputeBladeFsm
     |  |-ComputeBladeFsmStage
     |-ComputeBladeFsmTask
     |-ComputeBoard
     |  |-ComputeIOHub
     |  |  |-ComputeIOHubEnvStats
     |  |  |  |-ComputeIOHubEnvStatsHist
     |  |  |-FaultInst
     |  |-ComputeMbPowerStats
     |  |  |-ComputeMbPowerStatsHist
     |  |-ComputeMbTempStats
     |  |  |-ComputeMbTempStatsHist
     |  |-ComputePCIeFatalCompletionStats
     |  |-ComputePCIeFatalProtocolStats
     |  |-ComputePCIeFatalReceiveStats
     |  |-ComputePCIeFatalStats
     |  |-ComputeRackUnitMbTempStats
     |  |  |-ComputeRackUnitMbTempStatsHist
     |  |-ComputeRtcBattery
     |  |  |-FaultInst
     |  |-CoprocessorCard
     |  |-EquipmentTpm
     |  |  |-FaultInst
     |  |-FaultInst
     |  |-GraphicsCard
     |  |  |-EquipmentInventoryStatus
     |  |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-GraphicsController
     |  |-LstorageLocal
     |  |-LstorageLocalDef
     |  |-LstorageRemote
     |  |  |-LstorageLogin
     |  |-LstorageRemoteDef
     |  |  |-LstorageLogin
     |  |-MemoryArray
     |  |  |-FaultInst
     |  |  |-MemoryArrayEnvStats
     |  |  |  |-MemoryArrayEnvStatsHist
     |  |  |-MemoryPersistentMemoryUnit
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareBootDefinition
     |  |  |  |  |-FirmwareBootUnit
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |  |-FirmwareServicePack
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareRunning
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-MemoryErrorStats
     |  |  |  |-MemoryUnitEnvStats
     |  |  |     |-MemoryUnitEnvStatsHist
     |  |  |-MemoryUnit
     |  |     |-EquipmentInventoryStatus
     |  |     |  |-FaultInst
     |  |     |-FaultInst
     |  |     |-MemoryErrorStats
     |  |     |-MemoryUnitEnvStats
     |  |        |-MemoryUnitEnvStatsHist
     |  |-MemoryBufferUnit
     |  |  |-FaultInst
     |  |  |-MemoryBufferUnitEnvStats
     |  |     |-MemoryBufferUnitEnvStatsHist
     |  |-MemoryPersistentMemoryConfiguration
     |  |  |-FaultInst
     |  |  |-MemoryPersistentMemoryConfigResult
     |  |  |  |-FaultInst
     |  |  |  |-MemoryPersistentMemoryNamespaceConfigResult
     |  |  |     |-FaultInst
     |  |  |-MemoryPersistentMemoryRegion
     |  |     |-MemoryPersistentMemoryNamespace
     |  |        |-FaultInst
     |  |-PciSwitch
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-PciLink
     |  |-ProcessorUnit
     |  |  |-EquipmentInventoryStatus
     |  |  |  |-FaultInst
     |  |  |-FaultInst
     |  |  |-ProcessorCacheMemStats
     |  |  |-ProcessorCore
     |  |  |  |-ProcessorThread
     |  |  |-ProcessorEnvStats
     |  |  |  |-ProcessorEnvStatsHist
     |  |  |-ProcessorErrorStats
     |  |  |-ProcessorExecStats
     |  |  |-ProcessorIOStats
     |  |  |-ProcessorMiscStats
     |  |  |-ProcessorPCIBusStats
     |  |  |-ProcessorPMUStats
     |  |  |-ProcessorSecurityStats
     |  |-SecurityUnit
     |  |  |-EquipmentInventoryStatus
     |  |     |-FaultInst
     |  |-StorageController
     |  |  |-EquipmentInventoryStatus
     |  |  |  |-FaultInst
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-LstorageControllerDef
     |  |  |  |-LstorageControllerModeConfig
     |  |  |  |-LstorageControllerQualifier
     |  |  |-MgmtController
     |  |  |  |-CimcvmediaActualMountList
     |  |  |  |  |-CimcvmediaActualMountEntry
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-CimcvmediaExtMgmtRuleEntry
     |  |  |  |-EventInst
     |  |  |  |-FabricLocale
     |  |  |  |  |-AdaptorExtEthIfPc
     |  |  |  |  |  |-AdaptorExtEthIfPcEp
     |  |  |  |  |  |-DcxVIf
     |  |  |  |  |     |-FaultInst
     |  |  |  |  |-DcxVc
     |  |  |  |  |  |-FabricNetGroupRef
     |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FabricSanGroupRef
     |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-SwCmclan
     |  |  |  |  |  |  |-FabricNetGroupRef
     |  |  |  |  |  |     |-FaultInst
     |  |  |  |  |  |-SwNetflowMonitorRef
     |  |  |  |  |  |-SwUlan
     |  |  |  |  |  |-SwVlan
     |  |  |  |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-SwVsan
     |  |  |  |  |     |-SwFcZoneSet
     |  |  |  |  |        |-SwFcServerZoneGroup
     |  |  |  |  |        |  |-SwZoneInitiatorMember
     |  |  |  |  |        |     |-SwFcZone
     |  |  |  |  |        |        |-SwZoneTargetMember
     |  |  |  |  |        |-SwFcUserZoneGroup
     |  |  |  |  |           |-SwFcUserZone
     |  |  |  |  |              |-SwFcEndpoint
     |  |  |  |  |-FabricPath
     |  |  |  |     |-DcxVc
     |  |  |  |     |  |-FabricNetGroupRef
     |  |  |  |     |  |  |-FaultInst
     |  |  |  |     |  |-FabricSanGroupRef
     |  |  |  |     |  |  |-FaultInst
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-SwCmclan
     |  |  |  |     |  |  |-FabricNetGroupRef
     |  |  |  |     |  |     |-FaultInst
     |  |  |  |     |  |-SwNetflowMonitorRef
     |  |  |  |     |  |-SwUlan
     |  |  |  |     |  |-SwVlan
     |  |  |  |     |  |  |-FabricNetflowIPv4Addr
     |  |  |  |     |  |  |-FaultInst
     |  |  |  |     |  |-SwVsan
     |  |  |  |     |     |-SwFcZoneSet
     |  |  |  |     |        |-SwFcServerZoneGroup
     |  |  |  |     |        |  |-SwZoneInitiatorMember
     |  |  |  |     |        |     |-SwFcZone
     |  |  |  |     |        |        |-SwZoneTargetMember
     |  |  |  |     |        |-SwFcUserZoneGroup
     |  |  |  |     |           |-SwFcUserZone
     |  |  |  |     |              |-SwFcEndpoint
     |  |  |  |     |-FabricPathConn
     |  |  |  |     |  |-FabricPathEp
     |  |  |  |     |     |-PortTrustMode
     |  |  |  |     |-FabricPathEp
     |  |  |  |        |-PortTrustMode
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareBootDefinition
     |  |  |  |  |-FirmwareBootUnit
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |  |-FirmwareServicePack
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareImage
     |  |  |  |  |-EventInst
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareImageFsm
     |  |  |  |  |  |-FirmwareImageFsmStage
     |  |  |  |  |-FirmwareImageFsmTask
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareModule
     |  |  |  |-FirmwareRunning
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUpdatable
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |     |-FirmwareUcscInfo
     |  |  |  |-MgmtCimcSecureBoot
     |  |  |  |-MgmtCmcSecureBoot
     |  |  |  |-MgmtConnection
     |  |  |  |  |-FaultInst
     |  |  |  |-MgmtControllerFsm
     |  |  |  |  |-MgmtControllerFsmStage
     |  |  |  |-MgmtControllerFsmTask
     |  |  |  |-MgmtHealthStatus
     |  |  |  |  |-FaultInst
     |  |  |  |  |-MgmtHealthAttr
     |  |  |  |-MgmtIf
     |  |  |  |  |-DhcpAcquired
     |  |  |  |  |-EventInst
     |  |  |  |  |-FaultInst
     |  |  |  |  |-MgmtIPv6IfConfig
     |  |  |  |  |  |-MgmtIPv6IfAddr
     |  |  |  |  |     |-EventInst
     |  |  |  |  |     |-FaultInst
     |  |  |  |  |     |-MgmtIPv6IfAddrFsm
     |  |  |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |  |  |  |     |-MgmtIPv6IfAddrFsmTask
     |  |  |  |  |-MgmtIfFsm
     |  |  |  |  |  |-MgmtIfFsmStage
     |  |  |  |  |-MgmtIfFsmTask
     |  |  |  |-MgmtInterface
     |  |  |  |  |-FaultInst
     |  |  |  |  |-MgmtVnet
     |  |  |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-VnicIpV4History
     |  |  |  |     |-VnicIpV4PooledAddr
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-VnicIpV4History
     |  |  |  |     |-VnicIpV4StaticAddr
     |  |  |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-VnicIpV6History
     |  |  |  |     |-VnicIpV6StaticAddr
     |  |  |  |-MgmtKvmCertificate
     |  |  |  |  |-FaultInst
     |  |  |  |-MgmtProfDerivedInterface
     |  |  |  |  |-MgmtVnet
     |  |  |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-VnicIpV4History
     |  |  |  |     |-VnicIpV4PooledAddr
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-VnicIpV4History
     |  |  |  |     |-VnicIpV4StaticAddr
     |  |  |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |  |     |  |-FaultInst
     |  |  |  |     |  |-VnicIpV6History
     |  |  |  |     |-VnicIpV6StaticAddr
     |  |  |  |-MgmtSpdmCertificateInventory
     |  |  |  |  |-MgmtSpdmCertificateData
     |  |  |  |-MgmtSwPersonalities
     |  |  |  |  |-MgmtSwPersonality
     |  |  |  |-MgmtSwPersonalitiesInventory
     |  |  |  |  |-MgmtSwPersonality
     |  |  |  |-MgmtUsbNicMgmtIf
     |  |  |  |-SysdebugMEpLog
     |  |  |  |  |-FaultInst
     |  |  |  |-VnicIpV4PooledAddr
     |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4History
     |  |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |  |-VnicIpV4StaticAddr
     |  |  |-StorageDrive
     |  |  |-StorageEmbeddedStorage
     |  |  |-StorageEnclosure
     |  |  |  |-EventInst
     |  |  |  |-FaultInst
     |  |  |  |-StorageEnclosureDiskSlotEp
     |  |  |  |  |-FaultInst
     |  |  |  |  |-StorageControllerRef
     |  |  |  |-StorageEnclosureFsm
     |  |  |  |  |-StorageEnclosureFsmStage
     |  |  |  |-StorageEnclosureFsmTask
     |  |  |  |-StorageHddMotherBoardTempStats
     |  |  |  |  |-StorageHddMotherBoardTempStatsHist
     |  |  |  |-StorageLocalDisk
     |  |  |     |-EquipmentLocatorLed
     |  |  |     |  |-EquipmentLocatorLedFsm
     |  |  |     |  |  |-EquipmentLocatorLedFsmStage
     |  |  |     |  |-EquipmentLocatorLedFsmTask
     |  |  |     |  |-EventInst
     |  |  |     |  |-FaultInst
     |  |  |     |-EventInst
     |  |  |     |-FaultInst
     |  |  |     |-FirmwareBootDefinition
     |  |  |     |  |-FirmwareBootUnit
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-FirmwareInstallable
     |  |  |     |  |  |  |-FirmwareUcscInfo
     |  |  |     |  |  |-FirmwareServicePack
     |  |  |     |  |-FirmwareUcscInfo
     |  |  |     |-FirmwareRunning
     |  |  |     |  |-FirmwareServicePack
     |  |  |     |-MgmtController
     |  |  |     |  |-CimcvmediaActualMountList
     |  |  |     |  |  |-CimcvmediaActualMountEntry
     |  |  |     |  |  |  |-FaultInst
     |  |  |     |  |  |-CimcvmediaExtMgmtRuleEntry
     |  |  |     |  |-EventInst
     |  |  |     |  |-FabricLocale
     |  |  |     |  |  |-AdaptorExtEthIfPc
     |  |  |     |  |  |  |-AdaptorExtEthIfPcEp
     |  |  |     |  |  |  |-DcxVIf
     |  |  |     |  |  |     |-FaultInst
     |  |  |     |  |  |-DcxVc
     |  |  |     |  |  |  |-FabricNetGroupRef
     |  |  |     |  |  |  |  |-FaultInst
     |  |  |     |  |  |  |-FabricSanGroupRef
     |  |  |     |  |  |  |  |-FaultInst
     |  |  |     |  |  |  |-FaultInst
     |  |  |     |  |  |  |-SwCmclan
     |  |  |     |  |  |  |  |-FabricNetGroupRef
     |  |  |     |  |  |  |     |-FaultInst
     |  |  |     |  |  |  |-SwNetflowMonitorRef
     |  |  |     |  |  |  |-SwUlan
     |  |  |     |  |  |  |-SwVlan
     |  |  |     |  |  |  |  |-FabricNetflowIPv4Addr
     |  |  |     |  |  |  |  |-FaultInst
     |  |  |     |  |  |  |-SwVsan
     |  |  |     |  |  |     |-SwFcZoneSet
     |  |  |     |  |  |        |-SwFcServerZoneGroup
     |  |  |     |  |  |        |  |-SwZoneInitiatorMember
     |  |  |     |  |  |        |     |-SwFcZone
     |  |  |     |  |  |        |        |-SwZoneTargetMember
     |  |  |     |  |  |        |-SwFcUserZoneGroup
     |  |  |     |  |  |           |-SwFcUserZone
     |  |  |     |  |  |              |-SwFcEndpoint
     |  |  |     |  |  |-FabricPath
     |  |  |     |  |     |-DcxVc
     |  |  |     |  |     |  |-FabricNetGroupRef
     |  |  |     |  |     |  |  |-FaultInst
     |  |  |     |  |     |  |-FabricSanGroupRef
     |  |  |     |  |     |  |  |-FaultInst
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-SwCmclan
     |  |  |     |  |     |  |  |-FabricNetGroupRef
     |  |  |     |  |     |  |     |-FaultInst
     |  |  |     |  |     |  |-SwNetflowMonitorRef
     |  |  |     |  |     |  |-SwUlan
     |  |  |     |  |     |  |-SwVlan
     |  |  |     |  |     |  |  |-FabricNetflowIPv4Addr
     |  |  |     |  |     |  |  |-FaultInst
     |  |  |     |  |     |  |-SwVsan
     |  |  |     |  |     |     |-SwFcZoneSet
     |  |  |     |  |     |        |-SwFcServerZoneGroup
     |  |  |     |  |     |        |  |-SwZoneInitiatorMember
     |  |  |     |  |     |        |     |-SwFcZone
     |  |  |     |  |     |        |        |-SwZoneTargetMember
     |  |  |     |  |     |        |-SwFcUserZoneGroup
     |  |  |     |  |     |           |-SwFcUserZone
     |  |  |     |  |     |              |-SwFcEndpoint
     |  |  |     |  |     |-FabricPathConn
     |  |  |     |  |     |  |-FabricPathEp
     |  |  |     |  |     |     |-PortTrustMode
     |  |  |     |  |     |-FabricPathEp
     |  |  |     |  |        |-PortTrustMode
     |  |  |     |  |-FaultInst
     |  |  |     |  |-FirmwareBootDefinition
     |  |  |     |  |  |-FirmwareBootUnit
     |  |  |     |  |  |  |-FaultInst
     |  |  |     |  |  |  |-FirmwareInstallable
     |  |  |     |  |  |  |  |-FirmwareUcscInfo
     |  |  |     |  |  |  |-FirmwareServicePack
     |  |  |     |  |  |-FirmwareUcscInfo
     |  |  |     |  |-FirmwareImage
     |  |  |     |  |  |-EventInst
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-FirmwareImageFsm
     |  |  |     |  |  |  |-FirmwareImageFsmStage
     |  |  |     |  |  |-FirmwareImageFsmTask
     |  |  |     |  |  |-FirmwareInstallable
     |  |  |     |  |  |  |-FirmwareUcscInfo
     |  |  |     |  |  |-FirmwareModule
     |  |  |     |  |-FirmwareRunning
     |  |  |     |  |  |-FirmwareServicePack
     |  |  |     |  |-FirmwareUpdatable
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-FirmwareInstallable
     |  |  |     |  |     |-FirmwareUcscInfo
     |  |  |     |  |-MgmtCimcSecureBoot
     |  |  |     |  |-MgmtCmcSecureBoot
     |  |  |     |  |-MgmtConnection
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |-MgmtControllerFsm
     |  |  |     |  |  |-MgmtControllerFsmStage
     |  |  |     |  |-MgmtControllerFsmTask
     |  |  |     |  |-MgmtHealthStatus
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-MgmtHealthAttr
     |  |  |     |  |-MgmtIf
     |  |  |     |  |  |-DhcpAcquired
     |  |  |     |  |  |-EventInst
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-MgmtIPv6IfConfig
     |  |  |     |  |  |  |-MgmtIPv6IfAddr
     |  |  |     |  |  |     |-EventInst
     |  |  |     |  |  |     |-FaultInst
     |  |  |     |  |  |     |-MgmtIPv6IfAddrFsm
     |  |  |     |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |  |     |  |  |     |-MgmtIPv6IfAddrFsmTask
     |  |  |     |  |  |-MgmtIfFsm
     |  |  |     |  |  |  |-MgmtIfFsmStage
     |  |  |     |  |  |-MgmtIfFsmTask
     |  |  |     |  |-MgmtInterface
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-MgmtVnet
     |  |  |     |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-VnicIpV4History
     |  |  |     |  |     |-VnicIpV4PooledAddr
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-VnicIpV4History
     |  |  |     |  |     |-VnicIpV4StaticAddr
     |  |  |     |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-VnicIpV6History
     |  |  |     |  |     |-VnicIpV6StaticAddr
     |  |  |     |  |-MgmtKvmCertificate
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |-MgmtProfDerivedInterface
     |  |  |     |  |  |-MgmtVnet
     |  |  |     |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-VnicIpV4History
     |  |  |     |  |     |-VnicIpV4PooledAddr
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-VnicIpV4History
     |  |  |     |  |     |-VnicIpV4StaticAddr
     |  |  |     |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |     |  |     |  |-FaultInst
     |  |  |     |  |     |  |-VnicIpV6History
     |  |  |     |  |     |-VnicIpV6StaticAddr
     |  |  |     |  |-MgmtSpdmCertificateInventory
     |  |  |     |  |  |-MgmtSpdmCertificateData
     |  |  |     |  |-MgmtSwPersonalities
     |  |  |     |  |  |-MgmtSwPersonality
     |  |  |     |  |-MgmtSwPersonalitiesInventory
     |  |  |     |  |  |-MgmtSwPersonality
     |  |  |     |  |-MgmtUsbNicMgmtIf
     |  |  |     |  |-SysdebugMEpLog
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |-VnicIpV4PooledAddr
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |  |-VnicIpV4History
     |  |  |     |  |-VnicIpV4ProfDerivedAddr
     |  |  |     |  |-VnicIpV4StaticAddr
     |  |  |     |-StorageControllerEp
     |  |  |     |-StorageDiskEnvStats
     |  |  |     |  |-StorageDiskEnvStatsHist
     |  |  |     |-StorageLocalDiskFsm
     |  |  |     |  |-StorageLocalDiskFsmStage
     |  |  |     |-StorageLocalDiskFsmTask
     |  |  |     |-StorageLocalDiskPartition
     |  |  |     |-StorageOperation
     |  |  |     |-StorageSasPort
     |  |  |     |-StorageSsdHealthStats
     |  |  |        |-StorageSsdHealthStatsHist
     |  |  |-StorageLocalDisk
     |  |  |  |-EquipmentLocatorLed
     |  |  |  |  |-EquipmentLocatorLedFsm
     |  |  |  |  |  |-EquipmentLocatorLedFsmStage
     |  |  |  |  |-EquipmentLocatorLedFsmTask
     |  |  |  |  |-EventInst
     |  |  |  |  |-FaultInst
     |  |  |  |-EventInst
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareBootDefinition
     |  |  |  |  |-FirmwareBootUnit
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |  |-FirmwareServicePack
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareRunning
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-MgmtController
     |  |  |  |  |-CimcvmediaActualMountList
     |  |  |  |  |  |-CimcvmediaActualMountEntry
     |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-CimcvmediaExtMgmtRuleEntry
     |  |  |  |  |-EventInst
     |  |  |  |  |-FabricLocale
     |  |  |  |  |  |-AdaptorExtEthIfPc
     |  |  |  |  |  |  |-AdaptorExtEthIfPcEp
     |  |  |  |  |  |  |-DcxVIf
     |  |  |  |  |  |     |-FaultInst
     |  |  |  |  |  |-DcxVc
     |  |  |  |  |  |  |-FabricNetGroupRef
     |  |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |  |-FabricSanGroupRef
     |  |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |  |-SwCmclan
     |  |  |  |  |  |  |  |-FabricNetGroupRef
     |  |  |  |  |  |  |     |-FaultInst
     |  |  |  |  |  |  |-SwNetflowMonitorRef
     |  |  |  |  |  |  |-SwUlan
     |  |  |  |  |  |  |-SwVlan
     |  |  |  |  |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |  |-SwVsan
     |  |  |  |  |  |     |-SwFcZoneSet
     |  |  |  |  |  |        |-SwFcServerZoneGroup
     |  |  |  |  |  |        |  |-SwZoneInitiatorMember
     |  |  |  |  |  |        |     |-SwFcZone
     |  |  |  |  |  |        |        |-SwZoneTargetMember
     |  |  |  |  |  |        |-SwFcUserZoneGroup
     |  |  |  |  |  |           |-SwFcUserZone
     |  |  |  |  |  |              |-SwFcEndpoint
     |  |  |  |  |  |-FabricPath
     |  |  |  |  |     |-DcxVc
     |  |  |  |  |     |  |-FabricNetGroupRef
     |  |  |  |  |     |  |  |-FaultInst
     |  |  |  |  |     |  |-FabricSanGroupRef
     |  |  |  |  |     |  |  |-FaultInst
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-SwCmclan
     |  |  |  |  |     |  |  |-FabricNetGroupRef
     |  |  |  |  |     |  |     |-FaultInst
     |  |  |  |  |     |  |-SwNetflowMonitorRef
     |  |  |  |  |     |  |-SwUlan
     |  |  |  |  |     |  |-SwVlan
     |  |  |  |  |     |  |  |-FabricNetflowIPv4Addr
     |  |  |  |  |     |  |  |-FaultInst
     |  |  |  |  |     |  |-SwVsan
     |  |  |  |  |     |     |-SwFcZoneSet
     |  |  |  |  |     |        |-SwFcServerZoneGroup
     |  |  |  |  |     |        |  |-SwZoneInitiatorMember
     |  |  |  |  |     |        |     |-SwFcZone
     |  |  |  |  |     |        |        |-SwZoneTargetMember
     |  |  |  |  |     |        |-SwFcUserZoneGroup
     |  |  |  |  |     |           |-SwFcUserZone
     |  |  |  |  |     |              |-SwFcEndpoint
     |  |  |  |  |     |-FabricPathConn
     |  |  |  |  |     |  |-FabricPathEp
     |  |  |  |  |     |     |-PortTrustMode
     |  |  |  |  |     |-FabricPathEp
     |  |  |  |  |        |-PortTrustMode
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareBootDefinition
     |  |  |  |  |  |-FirmwareBootUnit
     |  |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |  |  |-FirmwareServicePack
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareImage
     |  |  |  |  |  |-EventInst
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FirmwareImageFsm
     |  |  |  |  |  |  |-FirmwareImageFsmStage
     |  |  |  |  |  |-FirmwareImageFsmTask
     |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |  |-FirmwareModule
     |  |  |  |  |-FirmwareRunning
     |  |  |  |  |  |-FirmwareServicePack
     |  |  |  |  |-FirmwareUpdatable
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |     |-FirmwareUcscInfo
     |  |  |  |  |-MgmtCimcSecureBoot
     |  |  |  |  |-MgmtCmcSecureBoot
     |  |  |  |  |-MgmtConnection
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-MgmtControllerFsm
     |  |  |  |  |  |-MgmtControllerFsmStage
     |  |  |  |  |-MgmtControllerFsmTask
     |  |  |  |  |-MgmtHealthStatus
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-MgmtHealthAttr
     |  |  |  |  |-MgmtIf
     |  |  |  |  |  |-DhcpAcquired
     |  |  |  |  |  |-EventInst
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-MgmtIPv6IfConfig
     |  |  |  |  |  |  |-MgmtIPv6IfAddr
     |  |  |  |  |  |     |-EventInst
     |  |  |  |  |  |     |-FaultInst
     |  |  |  |  |  |     |-MgmtIPv6IfAddrFsm
     |  |  |  |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |  |  |  |  |     |-MgmtIPv6IfAddrFsmTask
     |  |  |  |  |  |-MgmtIfFsm
     |  |  |  |  |  |  |-MgmtIfFsmStage
     |  |  |  |  |  |-MgmtIfFsmTask
     |  |  |  |  |-MgmtInterface
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-MgmtVnet
     |  |  |  |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-VnicIpV4History
     |  |  |  |  |     |-VnicIpV4PooledAddr
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-VnicIpV4History
     |  |  |  |  |     |-VnicIpV4StaticAddr
     |  |  |  |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-VnicIpV6History
     |  |  |  |  |     |-VnicIpV6StaticAddr
     |  |  |  |  |-MgmtKvmCertificate
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-MgmtProfDerivedInterface
     |  |  |  |  |  |-MgmtVnet
     |  |  |  |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-VnicIpV4History
     |  |  |  |  |     |-VnicIpV4PooledAddr
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-VnicIpV4History
     |  |  |  |  |     |-VnicIpV4StaticAddr
     |  |  |  |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |  |  |     |  |-FaultInst
     |  |  |  |  |     |  |-VnicIpV6History
     |  |  |  |  |     |-VnicIpV6StaticAddr
     |  |  |  |  |-MgmtSpdmCertificateInventory
     |  |  |  |  |  |-MgmtSpdmCertificateData
     |  |  |  |  |-MgmtSwPersonalities
     |  |  |  |  |  |-MgmtSwPersonality
     |  |  |  |  |-MgmtSwPersonalitiesInventory
     |  |  |  |  |  |-MgmtSwPersonality
     |  |  |  |  |-MgmtUsbNicMgmtIf
     |  |  |  |  |-SysdebugMEpLog
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-VnicIpV4PooledAddr
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-VnicIpV4History
     |  |  |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |  |  |-VnicIpV4StaticAddr
     |  |  |  |-StorageControllerEp
     |  |  |  |-StorageDiskEnvStats
     |  |  |  |  |-StorageDiskEnvStatsHist
     |  |  |  |-StorageLocalDiskFsm
     |  |  |  |  |-StorageLocalDiskFsmStage
     |  |  |  |-StorageLocalDiskFsmTask
     |  |  |  |-StorageLocalDiskPartition
     |  |  |  |-StorageOperation
     |  |  |  |-StorageSasPort
     |  |  |  |-StorageSsdHealthStats
     |  |  |     |-StorageSsdHealthStatsHist
     |  |  |-StorageLocalDiskConfigDef
     |  |  |  |-LstorageSecurity
     |  |  |  |  |-LstorageDriveSecurity
     |  |  |  |     |-LstorageLocal
     |  |  |  |     |-LstorageRemote
     |  |  |  |        |-LstorageLogin
     |  |  |  |-StorageLocalDiskPartition
     |  |  |-StorageLocalDiskEp
     |  |  |-StorageLocalLun
     |  |  |-StorageMezzFlashLife
     |  |  |  |-FaultInst
     |  |  |-StorageNvmeStats
     |  |  |  |-StorageNvmeStatsHist
     |  |  |-StorageNvmeStorage
     |  |  |-StorageOnboardDevice
     |  |  |  |-FirmwareBootDefinition
     |  |  |  |  |-FirmwareBootUnit
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |  |-FirmwareServicePack
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareRunning
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUpdatable
     |  |  |     |-FaultInst
     |  |  |     |-FirmwareInstallable
     |  |  |        |-FirmwareUcscInfo
     |  |  |-StorageOperation
     |  |  |-StorageRaidBattery
     |  |  |  |-FaultInst
     |  |  |  |-StorageOperation
     |  |  |  |-StorageTransportableFlashModule
     |  |  |-StorageVirtualDrive
     |  |  |  |-FaultInst
     |  |  |  |-StorageControllerEp
     |  |  |  |-StorageLunDisk
     |  |  |  |-StorageOperation
     |  |  |  |-StorageScsiLunRef
     |  |  |  |-StorageVDMemberEp
     |  |  |     |-FaultInst
     |  |  |-StorageVirtualDriveEp
     |  |-StorageFlexFlashController
     |  |  |-EventInst
     |  |  |-FaultInst
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-StorageFlexFlashCard
     |  |  |  |-FaultInst
     |  |  |  |-StorageFlexFlashDrive
     |  |  |     |-FaultInst
     |  |  |-StorageFlexFlashControllerFsm
     |  |  |  |-StorageFlexFlashControllerFsmStage
     |  |  |-StorageFlexFlashControllerFsmTask
     |  |  |-StorageFlexFlashVirtualDrive
     |  |  |  |-FaultInst
     |  |  |-StorageLocalDiskConfigDef
     |  |     |-LstorageSecurity
     |  |     |  |-LstorageDriveSecurity
     |  |     |     |-LstorageLocal
     |  |     |     |-LstorageRemote
     |  |     |        |-LstorageLogin
     |  |     |-StorageLocalDiskPartition
     |  |-StorageLocalDiskSlotEp
     |  |  |-FaultInst
     |  |-StorageMiniStorage
     |  |  |-EquipmentInventoryStatus
     |  |  |  |-FaultInst
     |  |  |-StorageControllerReference
     |  |-StorageNvmeSwitch
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |     |-FirmwareServicePack
     |  |-StorageSasExpander
     |     |-FaultInst
     |     |-FirmwareBootDefinition
     |     |  |-FirmwareBootUnit
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareInstallable
     |     |  |  |  |-FirmwareUcscInfo
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUcscInfo
     |     |-FirmwareRunning
     |     |  |-FirmwareServicePack
     |     |-MgmtController
     |     |  |-CimcvmediaActualMountList
     |     |  |  |-CimcvmediaActualMountEntry
     |     |  |  |  |-FaultInst
     |     |  |  |-CimcvmediaExtMgmtRuleEntry
     |     |  |-EventInst
     |     |  |-FabricLocale
     |     |  |  |-AdaptorExtEthIfPc
     |     |  |  |  |-AdaptorExtEthIfPcEp
     |     |  |  |  |-DcxVIf
     |     |  |  |     |-FaultInst
     |     |  |  |-DcxVc
     |     |  |  |  |-FabricNetGroupRef
     |     |  |  |  |  |-FaultInst
     |     |  |  |  |-FabricSanGroupRef
     |     |  |  |  |  |-FaultInst
     |     |  |  |  |-FaultInst
     |     |  |  |  |-SwCmclan
     |     |  |  |  |  |-FabricNetGroupRef
     |     |  |  |  |     |-FaultInst
     |     |  |  |  |-SwNetflowMonitorRef
     |     |  |  |  |-SwUlan
     |     |  |  |  |-SwVlan
     |     |  |  |  |  |-FabricNetflowIPv4Addr
     |     |  |  |  |  |-FaultInst
     |     |  |  |  |-SwVsan
     |     |  |  |     |-SwFcZoneSet
     |     |  |  |        |-SwFcServerZoneGroup
     |     |  |  |        |  |-SwZoneInitiatorMember
     |     |  |  |        |     |-SwFcZone
     |     |  |  |        |        |-SwZoneTargetMember
     |     |  |  |        |-SwFcUserZoneGroup
     |     |  |  |           |-SwFcUserZone
     |     |  |  |              |-SwFcEndpoint
     |     |  |  |-FabricPath
     |     |  |     |-DcxVc
     |     |  |     |  |-FabricNetGroupRef
     |     |  |     |  |  |-FaultInst
     |     |  |     |  |-FabricSanGroupRef
     |     |  |     |  |  |-FaultInst
     |     |  |     |  |-FaultInst
     |     |  |     |  |-SwCmclan
     |     |  |     |  |  |-FabricNetGroupRef
     |     |  |     |  |     |-FaultInst
     |     |  |     |  |-SwNetflowMonitorRef
     |     |  |     |  |-SwUlan
     |     |  |     |  |-SwVlan
     |     |  |     |  |  |-FabricNetflowIPv4Addr
     |     |  |     |  |  |-FaultInst
     |     |  |     |  |-SwVsan
     |     |  |     |     |-SwFcZoneSet
     |     |  |     |        |-SwFcServerZoneGroup
     |     |  |     |        |  |-SwZoneInitiatorMember
     |     |  |     |        |     |-SwFcZone
     |     |  |     |        |        |-SwZoneTargetMember
     |     |  |     |        |-SwFcUserZoneGroup
     |     |  |     |           |-SwFcUserZone
     |     |  |     |              |-SwFcEndpoint
     |     |  |     |-FabricPathConn
     |     |  |     |  |-FabricPathEp
     |     |  |     |     |-PortTrustMode
     |     |  |     |-FabricPathEp
     |     |  |        |-PortTrustMode
     |     |  |-FaultInst
     |     |  |-FirmwareBootDefinition
     |     |  |  |-FirmwareBootUnit
     |     |  |  |  |-FaultInst
     |     |  |  |  |-FirmwareInstallable
     |     |  |  |  |  |-FirmwareUcscInfo
     |     |  |  |  |-FirmwareServicePack
     |     |  |  |-FirmwareUcscInfo
     |     |  |-FirmwareImage
     |     |  |  |-EventInst
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareImageFsm
     |     |  |  |  |-FirmwareImageFsmStage
     |     |  |  |-FirmwareImageFsmTask
     |     |  |  |-FirmwareInstallable
     |     |  |  |  |-FirmwareUcscInfo
     |     |  |  |-FirmwareModule
     |     |  |-FirmwareRunning
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUpdatable
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareInstallable
     |     |  |     |-FirmwareUcscInfo
     |     |  |-MgmtCimcSecureBoot
     |     |  |-MgmtCmcSecureBoot
     |     |  |-MgmtConnection
     |     |  |  |-FaultInst
     |     |  |-MgmtControllerFsm
     |     |  |  |-MgmtControllerFsmStage
     |     |  |-MgmtControllerFsmTask
     |     |  |-MgmtHealthStatus
     |     |  |  |-FaultInst
     |     |  |  |-MgmtHealthAttr
     |     |  |-MgmtIf
     |     |  |  |-DhcpAcquired
     |     |  |  |-EventInst
     |     |  |  |-FaultInst
     |     |  |  |-MgmtIPv6IfConfig
     |     |  |  |  |-MgmtIPv6IfAddr
     |     |  |  |     |-EventInst
     |     |  |  |     |-FaultInst
     |     |  |  |     |-MgmtIPv6IfAddrFsm
     |     |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |     |  |  |     |-MgmtIPv6IfAddrFsmTask
     |     |  |  |-MgmtIfFsm
     |     |  |  |  |-MgmtIfFsmStage
     |     |  |  |-MgmtIfFsmTask
     |     |  |-MgmtInterface
     |     |  |  |-FaultInst
     |     |  |  |-MgmtVnet
     |     |  |     |-VnicIpV4MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4PooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4StaticAddr
     |     |  |     |-VnicIpV6MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV6History
     |     |  |     |-VnicIpV6StaticAddr
     |     |  |-MgmtKvmCertificate
     |     |  |  |-FaultInst
     |     |  |-MgmtProfDerivedInterface
     |     |  |  |-MgmtVnet
     |     |  |     |-VnicIpV4MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4PooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4StaticAddr
     |     |  |     |-VnicIpV6MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV6History
     |     |  |     |-VnicIpV6StaticAddr
     |     |  |-MgmtSpdmCertificateInventory
     |     |  |  |-MgmtSpdmCertificateData
     |     |  |-MgmtSwPersonalities
     |     |  |  |-MgmtSwPersonality
     |     |  |-MgmtSwPersonalitiesInventory
     |     |  |  |-MgmtSwPersonality
     |     |  |-MgmtUsbNicMgmtIf
     |     |  |-SysdebugMEpLog
     |     |  |  |-FaultInst
     |     |  |-VnicIpV4PooledAddr
     |     |  |  |-FaultInst
     |     |  |  |-VnicIpV4History
     |     |  |-VnicIpV4ProfDerivedAddr
     |     |  |-VnicIpV4StaticAddr
     |     |-StorageOnboardDevice
     |     |  |-FirmwareBootDefinition
     |     |  |  |-FirmwareBootUnit
     |     |  |  |  |-FaultInst
     |     |  |  |  |-FirmwareInstallable
     |     |  |  |  |  |-FirmwareUcscInfo
     |     |  |  |  |-FirmwareServicePack
     |     |  |  |-FirmwareUcscInfo
     |     |  |-FirmwareRunning
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUpdatable
     |     |     |-FaultInst
     |     |     |-FirmwareInstallable
     |     |        |-FirmwareUcscInfo
     |     |-StorageSasUpLink
     |-ComputeBoardConnector
     |-ComputeBoardController
     |  |-MgmtController
     |     |-CimcvmediaActualMountList
     |     |  |-CimcvmediaActualMountEntry
     |     |  |  |-FaultInst
     |     |  |-CimcvmediaExtMgmtRuleEntry
     |     |-EventInst
     |     |-FabricLocale
     |     |  |-AdaptorExtEthIfPc
     |     |  |  |-AdaptorExtEthIfPcEp
     |     |  |  |-DcxVIf
     |     |  |     |-FaultInst
     |     |  |-DcxVc
     |     |  |  |-FabricNetGroupRef
     |     |  |  |  |-FaultInst
     |     |  |  |-FabricSanGroupRef
     |     |  |  |  |-FaultInst
     |     |  |  |-FaultInst
     |     |  |  |-SwCmclan
     |     |  |  |  |-FabricNetGroupRef
     |     |  |  |     |-FaultInst
     |     |  |  |-SwNetflowMonitorRef
     |     |  |  |-SwUlan
     |     |  |  |-SwVlan
     |     |  |  |  |-FabricNetflowIPv4Addr
     |     |  |  |  |-FaultInst
     |     |  |  |-SwVsan
     |     |  |     |-SwFcZoneSet
     |     |  |        |-SwFcServerZoneGroup
     |     |  |        |  |-SwZoneInitiatorMember
     |     |  |        |     |-SwFcZone
     |     |  |        |        |-SwZoneTargetMember
     |     |  |        |-SwFcUserZoneGroup
     |     |  |           |-SwFcUserZone
     |     |  |              |-SwFcEndpoint
     |     |  |-FabricPath
     |     |     |-DcxVc
     |     |     |  |-FabricNetGroupRef
     |     |     |  |  |-FaultInst
     |     |     |  |-FabricSanGroupRef
     |     |     |  |  |-FaultInst
     |     |     |  |-FaultInst
     |     |     |  |-SwCmclan
     |     |     |  |  |-FabricNetGroupRef
     |     |     |  |     |-FaultInst
     |     |     |  |-SwNetflowMonitorRef
     |     |     |  |-SwUlan
     |     |     |  |-SwVlan
     |     |     |  |  |-FabricNetflowIPv4Addr
     |     |     |  |  |-FaultInst
     |     |     |  |-SwVsan
     |     |     |     |-SwFcZoneSet
     |     |     |        |-SwFcServerZoneGroup
     |     |     |        |  |-SwZoneInitiatorMember
     |     |     |        |     |-SwFcZone
     |     |     |        |        |-SwZoneTargetMember
     |     |     |        |-SwFcUserZoneGroup
     |     |     |           |-SwFcUserZone
     |     |     |              |-SwFcEndpoint
     |     |     |-FabricPathConn
     |     |     |  |-FabricPathEp
     |     |     |     |-PortTrustMode
     |     |     |-FabricPathEp
     |     |        |-PortTrustMode
     |     |-FaultInst
     |     |-FirmwareBootDefinition
     |     |  |-FirmwareBootUnit
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareInstallable
     |     |  |  |  |-FirmwareUcscInfo
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUcscInfo
     |     |-FirmwareImage
     |     |  |-EventInst
     |     |  |-FaultInst
     |     |  |-FirmwareImageFsm
     |     |  |  |-FirmwareImageFsmStage
     |     |  |-FirmwareImageFsmTask
     |     |  |-FirmwareInstallable
     |     |  |  |-FirmwareUcscInfo
     |     |  |-FirmwareModule
     |     |-FirmwareRunning
     |     |  |-FirmwareServicePack
     |     |-FirmwareUpdatable
     |     |  |-FaultInst
     |     |  |-FirmwareInstallable
     |     |     |-FirmwareUcscInfo
     |     |-MgmtCimcSecureBoot
     |     |-MgmtCmcSecureBoot
     |     |-MgmtConnection
     |     |  |-FaultInst
     |     |-MgmtControllerFsm
     |     |  |-MgmtControllerFsmStage
     |     |-MgmtControllerFsmTask
     |     |-MgmtHealthStatus
     |     |  |-FaultInst
     |     |  |-MgmtHealthAttr
     |     |-MgmtIf
     |     |  |-DhcpAcquired
     |     |  |-EventInst
     |     |  |-FaultInst
     |     |  |-MgmtIPv6IfConfig
     |     |  |  |-MgmtIPv6IfAddr
     |     |  |     |-EventInst
     |     |  |     |-FaultInst
     |     |  |     |-MgmtIPv6IfAddrFsm
     |     |  |     |  |-MgmtIPv6IfAddrFsmStage
     |     |  |     |-MgmtIPv6IfAddrFsmTask
     |     |  |-MgmtIfFsm
     |     |  |  |-MgmtIfFsmStage
     |     |  |-MgmtIfFsmTask
     |     |-MgmtInterface
     |     |  |-FaultInst
     |     |  |-MgmtVnet
     |     |     |-VnicIpV4MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4PooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4StaticAddr
     |     |     |-VnicIpV6MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV6History
     |     |     |-VnicIpV6StaticAddr
     |     |-MgmtKvmCertificate
     |     |  |-FaultInst
     |     |-MgmtProfDerivedInterface
     |     |  |-MgmtVnet
     |     |     |-VnicIpV4MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4PooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV4History
     |     |     |-VnicIpV4StaticAddr
     |     |     |-VnicIpV6MgmtPooledAddr
     |     |     |  |-FaultInst
     |     |     |  |-VnicIpV6History
     |     |     |-VnicIpV6StaticAddr
     |     |-MgmtSpdmCertificateInventory
     |     |  |-MgmtSpdmCertificateData
     |     |-MgmtSwPersonalities
     |     |  |-MgmtSwPersonality
     |     |-MgmtSwPersonalitiesInventory
     |     |  |-MgmtSwPersonality
     |     |-MgmtUsbNicMgmtIf
     |     |-SysdebugMEpLog
     |     |  |-FaultInst
     |     |-VnicIpV4PooledAddr
     |     |  |-FaultInst
     |     |  |-VnicIpV4History
     |     |-VnicIpV4ProfDerivedAddr
     |     |-VnicIpV4StaticAddr
     |-ComputeExtBoard
     |  |-BiosUnit
     |  |  |-BiosBOT
     |  |  |  |-BiosBootDevGrp
     |  |  |     |-BiosBootDev
     |  |  |-BiosSettings
     |  |  |  |-BiosTokenFeatureGroup
     |  |  |  |  |-BiosTokenParam
     |  |  |  |     |-BiosTokenSettings
     |  |  |  |-BiosTokenParam
     |  |  |  |  |-BiosTokenSettings
     |  |  |  |-BiosVfACPI10Support
     |  |  |  |-BiosVfASPMSupport
     |  |  |  |-BiosVfAllUSBDevices
     |  |  |  |-BiosVfAltitude
     |  |  |  |-BiosVfAssertNMIOnPERR
     |  |  |  |-BiosVfAssertNMIOnSERR
     |  |  |  |-BiosVfBMEDMAMitigation
     |  |  |  |-BiosVfBootOptionRetry
     |  |  |  |-BiosVfCPUHardwarePowerManagement
     |  |  |  |-BiosVfCPUPerformance
     |  |  |  |-BiosVfConsistentDeviceNameControl
     |  |  |  |-BiosVfConsoleRedirection
     |  |  |  |-BiosVfCoreMultiProcessing
     |  |  |  |-BiosVfDDR3VoltageSelection
     |  |  |  |-BiosVfDRAMClockThrottling
     |  |  |  |-BiosVfDirectCacheAccess
     |  |  |  |-BiosVfDramRefreshRate
     |  |  |  |-BiosVfEnergyPerformanceTuning
     |  |  |  |-BiosVfEnhancedIntelSpeedStepTech
     |  |  |  |-BiosVfEnhancedPowerCappingSupport
     |  |  |  |-BiosVfExecuteDisableBit
     |  |  |  |-BiosVfFRB2Timer
     |  |  |  |-BiosVfFrequencyFloorOverride
     |  |  |  |-BiosVfFrontPanelLockout
     |  |  |  |-BiosVfIOEMezz1OptionROM
     |  |  |  |-BiosVfIOENVMe1OptionROM
     |  |  |  |-BiosVfIOENVMe2OptionROM
     |  |  |  |-BiosVfIOESlot1OptionROM
     |  |  |  |-BiosVfIOESlot2OptionROM
     |  |  |  |-BiosVfIntegratedGraphics
     |  |  |  |-BiosVfIntegratedGraphicsApertureSize
     |  |  |  |-BiosVfIntelEntrySASRAIDModule
     |  |  |  |-BiosVfIntelHyperThreadingTech
     |  |  |  |-BiosVfIntelTrustedExecutionTechnology
     |  |  |  |-BiosVfIntelTurboBoostTech
     |  |  |  |-BiosVfIntelVTForDirectedIO
     |  |  |  |-BiosVfIntelVirtualizationTechnology
     |  |  |  |-BiosVfInterleaveConfiguration
     |  |  |  |-BiosVfLocalX2Apic
     |  |  |  |-BiosVfLvDIMMSupport
     |  |  |  |-BiosVfMaxVariableMTRRSetting
     |  |  |  |-BiosVfMaximumMemoryBelow4GB
     |  |  |  |-BiosVfMemoryMappedIOAbove4GB
     |  |  |  |-BiosVfMirroringMode
     |  |  |  |-BiosVfNUMAOptimized
     |  |  |  |-BiosVfOSBootWatchdogTimer
     |  |  |  |-BiosVfOSBootWatchdogTimerPolicy
     |  |  |  |-BiosVfOSBootWatchdogTimerTimeout
     |  |  |  |-BiosVfOnboardGraphics
     |  |  |  |-BiosVfOnboardSATAController
     |  |  |  |-BiosVfOnboardStorage
     |  |  |  |-BiosVfOptionROMEnable
     |  |  |  |-BiosVfOptionROMLoad
     |  |  |  |-BiosVfOutOfBandManagement
     |  |  |  |-BiosVfPCHSATAMode
     |  |  |  |-BiosVfPCILOMPortsConfiguration
     |  |  |  |-BiosVfPCIROMCLP
     |  |  |  |-BiosVfPCISlotLinkSpeed
     |  |  |  |-BiosVfPCISlotOptionROMEnable
     |  |  |  |-BiosVfPOSTErrorPause
     |  |  |  |-BiosVfPSTATECoordination
     |  |  |  |-BiosVfPackageCStateLimit
     |  |  |  |-BiosVfPanicAndHighWatermark
     |  |  |  |-BiosVfProcessorC1E
     |  |  |  |-BiosVfProcessorC3Report
     |  |  |  |-BiosVfProcessorC6Report
     |  |  |  |-BiosVfProcessorC7Report
     |  |  |  |-BiosVfProcessorCMCI
     |  |  |  |-BiosVfProcessorCState
     |  |  |  |-BiosVfProcessorEnergyConfiguration
     |  |  |  |-BiosVfProcessorPrefetchConfig
     |  |  |  |-BiosVfQPILinkFrequencySelect
     |  |  |  |-BiosVfQPISnoopMode
     |  |  |  |-BiosVfQuietBoot
     |  |  |  |-BiosVfRedirectionAfterBIOSPOST
     |  |  |  |-BiosVfResumeOnACPowerLoss
     |  |  |  |-BiosVfSBMezz1OptionROM
     |  |  |  |-BiosVfSBNVMe1OptionROM
     |  |  |  |-BiosVfSIOC1OptionROM
     |  |  |  |-BiosVfSIOC2OptionROM
     |  |  |  |-BiosVfScrubPolicies
     |  |  |  |-BiosVfSelectMemoryRASConfiguration
     |  |  |  |-BiosVfSerialPortAEnable
     |  |  |  |-BiosVfSparingMode
     |  |  |  |-BiosVfSriovConfig
     |  |  |  |-BiosVfTPMPendingOperation
     |  |  |  |-BiosVfTPMSupport
     |  |  |  |-BiosVfTrustedPlatformModule
     |  |  |  |-BiosVfUCSMBootModeControl
     |  |  |  |-BiosVfUCSMBootOrderRuleControl
     |  |  |  |-BiosVfUEFIOSUseLegacyVideo
     |  |  |  |-BiosVfUSBBootConfig
     |  |  |  |-BiosVfUSBConfiguration
     |  |  |  |-BiosVfUSBFrontPanelAccessLock
     |  |  |  |-BiosVfUSBPortConfiguration
     |  |  |  |-BiosVfUSBSystemIdlePowerOptimizingSetting
     |  |  |  |-BiosVfVGAPriority
     |  |  |  |-BiosVfWorkloadConfiguration
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-FirmwareUpdatable
     |  |     |-FaultInst
     |  |     |-FirmwareInstallable
     |  |        |-FirmwareUcscInfo
     |  |-ComputeBoardController
     |  |  |-MgmtController
     |  |     |-CimcvmediaActualMountList
     |  |     |  |-CimcvmediaActualMountEntry
     |  |     |  |  |-FaultInst
     |  |     |  |-CimcvmediaExtMgmtRuleEntry
     |  |     |-EventInst
     |  |     |-FabricLocale
     |  |     |  |-AdaptorExtEthIfPc
     |  |     |  |  |-AdaptorExtEthIfPcEp
     |  |     |  |  |-DcxVIf
     |  |     |  |     |-FaultInst
     |  |     |  |-DcxVc
     |  |     |  |  |-FabricNetGroupRef
     |  |     |  |  |  |-FaultInst
     |  |     |  |  |-FabricSanGroupRef
     |  |     |  |  |  |-FaultInst
     |  |     |  |  |-FaultInst
     |  |     |  |  |-SwCmclan
     |  |     |  |  |  |-FabricNetGroupRef
     |  |     |  |  |     |-FaultInst
     |  |     |  |  |-SwNetflowMonitorRef
     |  |     |  |  |-SwUlan
     |  |     |  |  |-SwVlan
     |  |     |  |  |  |-FabricNetflowIPv4Addr
     |  |     |  |  |  |-FaultInst
     |  |     |  |  |-SwVsan
     |  |     |  |     |-SwFcZoneSet
     |  |     |  |        |-SwFcServerZoneGroup
     |  |     |  |        |  |-SwZoneInitiatorMember
     |  |     |  |        |     |-SwFcZone
     |  |     |  |        |        |-SwZoneTargetMember
     |  |     |  |        |-SwFcUserZoneGroup
     |  |     |  |           |-SwFcUserZone
     |  |     |  |              |-SwFcEndpoint
     |  |     |  |-FabricPath
     |  |     |     |-DcxVc
     |  |     |     |  |-FabricNetGroupRef
     |  |     |     |  |  |-FaultInst
     |  |     |     |  |-FabricSanGroupRef
     |  |     |     |  |  |-FaultInst
     |  |     |     |  |-FaultInst
     |  |     |     |  |-SwCmclan
     |  |     |     |  |  |-FabricNetGroupRef
     |  |     |     |  |     |-FaultInst
     |  |     |     |  |-SwNetflowMonitorRef
     |  |     |     |  |-SwUlan
     |  |     |     |  |-SwVlan
     |  |     |     |  |  |-FabricNetflowIPv4Addr
     |  |     |     |  |  |-FaultInst
     |  |     |     |  |-SwVsan
     |  |     |     |     |-SwFcZoneSet
     |  |     |     |        |-SwFcServerZoneGroup
     |  |     |     |        |  |-SwZoneInitiatorMember
     |  |     |     |        |     |-SwFcZone
     |  |     |     |        |        |-SwZoneTargetMember
     |  |     |     |        |-SwFcUserZoneGroup
     |  |     |     |           |-SwFcUserZone
     |  |     |     |              |-SwFcEndpoint
     |  |     |     |-FabricPathConn
     |  |     |     |  |-FabricPathEp
     |  |     |     |     |-PortTrustMode
     |  |     |     |-FabricPathEp
     |  |     |        |-PortTrustMode
     |  |     |-FaultInst
     |  |     |-FirmwareBootDefinition
     |  |     |  |-FirmwareBootUnit
     |  |     |  |  |-FaultInst
     |  |     |  |  |-FirmwareInstallable
     |  |     |  |  |  |-FirmwareUcscInfo
     |  |     |  |  |-FirmwareServicePack
     |  |     |  |-FirmwareUcscInfo
     |  |     |-FirmwareImage
     |  |     |  |-EventInst
     |  |     |  |-FaultInst
     |  |     |  |-FirmwareImageFsm
     |  |     |  |  |-FirmwareImageFsmStage
     |  |     |  |-FirmwareImageFsmTask
     |  |     |  |-FirmwareInstallable
     |  |     |  |  |-FirmwareUcscInfo
     |  |     |  |-FirmwareModule
     |  |     |-FirmwareRunning
     |  |     |  |-FirmwareServicePack
     |  |     |-FirmwareUpdatable
     |  |     |  |-FaultInst
     |  |     |  |-FirmwareInstallable
     |  |     |     |-FirmwareUcscInfo
     |  |     |-MgmtCimcSecureBoot
     |  |     |-MgmtCmcSecureBoot
     |  |     |-MgmtConnection
     |  |     |  |-FaultInst
     |  |     |-MgmtControllerFsm
     |  |     |  |-MgmtControllerFsmStage
     |  |     |-MgmtControllerFsmTask
     |  |     |-MgmtHealthStatus
     |  |     |  |-FaultInst
     |  |     |  |-MgmtHealthAttr
     |  |     |-MgmtIf
     |  |     |  |-DhcpAcquired
     |  |     |  |-EventInst
     |  |     |  |-FaultInst
     |  |     |  |-MgmtIPv6IfConfig
     |  |     |  |  |-MgmtIPv6IfAddr
     |  |     |  |     |-EventInst
     |  |     |  |     |-FaultInst
     |  |     |  |     |-MgmtIPv6IfAddrFsm
     |  |     |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |     |  |     |-MgmtIPv6IfAddrFsmTask
     |  |     |  |-MgmtIfFsm
     |  |     |  |  |-MgmtIfFsmStage
     |  |     |  |-MgmtIfFsmTask
     |  |     |-MgmtInterface
     |  |     |  |-FaultInst
     |  |     |  |-MgmtVnet
     |  |     |     |-VnicIpV4MgmtPooledAddr
     |  |     |     |  |-FaultInst
     |  |     |     |  |-VnicIpV4History
     |  |     |     |-VnicIpV4PooledAddr
     |  |     |     |  |-FaultInst
     |  |     |     |  |-VnicIpV4History
     |  |     |     |-VnicIpV4StaticAddr
     |  |     |     |-VnicIpV6MgmtPooledAddr
     |  |     |     |  |-FaultInst
     |  |     |     |  |-VnicIpV6History
     |  |     |     |-VnicIpV6StaticAddr
     |  |     |-MgmtKvmCertificate
     |  |     |  |-FaultInst
     |  |     |-MgmtProfDerivedInterface
     |  |     |  |-MgmtVnet
     |  |     |     |-VnicIpV4MgmtPooledAddr
     |  |     |     |  |-FaultInst
     |  |     |     |  |-VnicIpV4History
     |  |     |     |-VnicIpV4PooledAddr
     |  |     |     |  |-FaultInst
     |  |     |     |  |-VnicIpV4History
     |  |     |     |-VnicIpV4StaticAddr
     |  |     |     |-VnicIpV6MgmtPooledAddr
     |  |     |     |  |-FaultInst
     |  |     |     |  |-VnicIpV6History
     |  |     |     |-VnicIpV6StaticAddr
     |  |     |-MgmtSpdmCertificateInventory
     |  |     |  |-MgmtSpdmCertificateData
     |  |     |-MgmtSwPersonalities
     |  |     |  |-MgmtSwPersonality
     |  |     |-MgmtSwPersonalitiesInventory
     |  |     |  |-MgmtSwPersonality
     |  |     |-MgmtUsbNicMgmtIf
     |  |     |-SysdebugMEpLog
     |  |     |  |-FaultInst
     |  |     |-VnicIpV4PooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV4History
     |  |     |-VnicIpV4ProfDerivedAddr
     |  |     |-VnicIpV4StaticAddr
     |  |-ComputeMbPowerStats
     |  |  |-ComputeMbPowerStatsHist
     |  |-ComputeMbTempStats
     |  |  |-ComputeMbTempStatsHist
     |  |-EquipmentHealthLed
     |  |  |-ComputeHealthLedSensorAlarm
     |  |  |-FaultInst
     |  |-EquipmentLocatorLed
     |  |  |-EquipmentLocatorLedFsm
     |  |  |  |-EquipmentLocatorLedFsmStage
     |  |  |-EquipmentLocatorLedFsmTask
     |  |  |-EventInst
     |  |  |-FaultInst
     |  |-FaultInst
     |  |-MgmtController
     |  |  |-CimcvmediaActualMountList
     |  |  |  |-CimcvmediaActualMountEntry
     |  |  |  |  |-FaultInst
     |  |  |  |-CimcvmediaExtMgmtRuleEntry
     |  |  |-EventInst
     |  |  |-FabricLocale
     |  |  |  |-AdaptorExtEthIfPc
     |  |  |  |  |-AdaptorExtEthIfPcEp
     |  |  |  |  |-DcxVIf
     |  |  |  |     |-FaultInst
     |  |  |  |-DcxVc
     |  |  |  |  |-FabricNetGroupRef
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-FabricSanGroupRef
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-FaultInst
     |  |  |  |  |-SwCmclan
     |  |  |  |  |  |-FabricNetGroupRef
     |  |  |  |  |     |-FaultInst
     |  |  |  |  |-SwNetflowMonitorRef
     |  |  |  |  |-SwUlan
     |  |  |  |  |-SwVlan
     |  |  |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |  |  |-FaultInst
     |  |  |  |  |-SwVsan
     |  |  |  |     |-SwFcZoneSet
     |  |  |  |        |-SwFcServerZoneGroup
     |  |  |  |        |  |-SwZoneInitiatorMember
     |  |  |  |        |     |-SwFcZone
     |  |  |  |        |        |-SwZoneTargetMember
     |  |  |  |        |-SwFcUserZoneGroup
     |  |  |  |           |-SwFcUserZone
     |  |  |  |              |-SwFcEndpoint
     |  |  |  |-FabricPath
     |  |  |     |-DcxVc
     |  |  |     |  |-FabricNetGroupRef
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |-FabricSanGroupRef
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |-FaultInst
     |  |  |     |  |-SwCmclan
     |  |  |     |  |  |-FabricNetGroupRef
     |  |  |     |  |     |-FaultInst
     |  |  |     |  |-SwNetflowMonitorRef
     |  |  |     |  |-SwUlan
     |  |  |     |  |-SwVlan
     |  |  |     |  |  |-FabricNetflowIPv4Addr
     |  |  |     |  |  |-FaultInst
     |  |  |     |  |-SwVsan
     |  |  |     |     |-SwFcZoneSet
     |  |  |     |        |-SwFcServerZoneGroup
     |  |  |     |        |  |-SwZoneInitiatorMember
     |  |  |     |        |     |-SwFcZone
     |  |  |     |        |        |-SwZoneTargetMember
     |  |  |     |        |-SwFcUserZoneGroup
     |  |  |     |           |-SwFcUserZone
     |  |  |     |              |-SwFcEndpoint
     |  |  |     |-FabricPathConn
     |  |  |     |  |-FabricPathEp
     |  |  |     |     |-PortTrustMode
     |  |  |     |-FabricPathEp
     |  |  |        |-PortTrustMode
     |  |  |-FaultInst
     |  |  |-FirmwareBootDefinition
     |  |  |  |-FirmwareBootUnit
     |  |  |  |  |-FaultInst
     |  |  |  |  |-FirmwareInstallable
     |  |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |  |-FirmwareServicePack
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareImage
     |  |  |  |-EventInst
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareImageFsm
     |  |  |  |  |-FirmwareImageFsmStage
     |  |  |  |-FirmwareImageFsmTask
     |  |  |  |-FirmwareInstallable
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareModule
     |  |  |-FirmwareRunning
     |  |  |  |-FirmwareServicePack
     |  |  |-FirmwareUpdatable
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareInstallable
     |  |  |     |-FirmwareUcscInfo
     |  |  |-MgmtCimcSecureBoot
     |  |  |-MgmtCmcSecureBoot
     |  |  |-MgmtConnection
     |  |  |  |-FaultInst
     |  |  |-MgmtControllerFsm
     |  |  |  |-MgmtControllerFsmStage
     |  |  |-MgmtControllerFsmTask
     |  |  |-MgmtHealthStatus
     |  |  |  |-FaultInst
     |  |  |  |-MgmtHealthAttr
     |  |  |-MgmtIf
     |  |  |  |-DhcpAcquired
     |  |  |  |-EventInst
     |  |  |  |-FaultInst
     |  |  |  |-MgmtIPv6IfConfig
     |  |  |  |  |-MgmtIPv6IfAddr
     |  |  |  |     |-EventInst
     |  |  |  |     |-FaultInst
     |  |  |  |     |-MgmtIPv6IfAddrFsm
     |  |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |  |  |     |-MgmtIPv6IfAddrFsmTask
     |  |  |  |-MgmtIfFsm
     |  |  |  |  |-MgmtIfFsmStage
     |  |  |  |-MgmtIfFsmTask
     |  |  |-MgmtInterface
     |  |  |  |-FaultInst
     |  |  |  |-MgmtVnet
     |  |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |     |  |-FaultInst
     |  |  |     |  |-VnicIpV4History
     |  |  |     |-VnicIpV4PooledAddr
     |  |  |     |  |-FaultInst
     |  |  |     |  |-VnicIpV4History
     |  |  |     |-VnicIpV4StaticAddr
     |  |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |     |  |-FaultInst
     |  |  |     |  |-VnicIpV6History
     |  |  |     |-VnicIpV6StaticAddr
     |  |  |-MgmtKvmCertificate
     |  |  |  |-FaultInst
     |  |  |-MgmtProfDerivedInterface
     |  |  |  |-MgmtVnet
     |  |  |     |-VnicIpV4MgmtPooledAddr
     |  |  |     |  |-FaultInst
     |  |  |     |  |-VnicIpV4History
     |  |  |     |-VnicIpV4PooledAddr
     |  |  |     |  |-FaultInst
     |  |  |     |  |-VnicIpV4History
     |  |  |     |-VnicIpV4StaticAddr
     |  |  |     |-VnicIpV6MgmtPooledAddr
     |  |  |     |  |-FaultInst
     |  |  |     |  |-VnicIpV6History
     |  |  |     |-VnicIpV6StaticAddr
     |  |  |-MgmtSpdmCertificateInventory
     |  |  |  |-MgmtSpdmCertificateData
     |  |  |-MgmtSwPersonalities
     |  |  |  |-MgmtSwPersonality
     |  |  |-MgmtSwPersonalitiesInventory
     |  |  |  |-MgmtSwPersonality
     |  |  |-MgmtUsbNicMgmtIf
     |  |  |-SysdebugMEpLog
     |  |  |  |-FaultInst
     |  |  |-VnicIpV4PooledAddr
     |  |  |  |-FaultInst
     |  |  |  |-VnicIpV4History
     |  |  |-VnicIpV4ProfDerivedAddr
     |  |  |-VnicIpV4StaticAddr
     |  |-PowerBudget
     |     |-FaultInst
     |     |-PowerProfiledPower
     |-ComputeFactoryResetOperation
     |-ComputeFwSyncAck
     |  |-FaultInst
     |  |-TrigLocalSched
     |     |-TrigAbsWindow
     |     |-TrigLocalAbsWindow
     |     |-TrigRecurrWindow
     |-ComputeHostUtilityOs
     |  |-MgmtUsbNicMgmtIf
     |-ComputeKvmMgmtPolicy
     |  |-MgmtKvmCertificate
     |     |-FaultInst
     |-ComputeMemoryConfiguration
     |-ComputePersonality
     |-ComputePhysicalExtension
     |  |-FaultInst
     |-ComputePhysicalFsm
     |  |-ComputePhysicalFsmStage
     |-ComputePhysicalFsmTask
     |-ComputePnuOSImage
     |-ComputePoolable
     |  |-ComputePoolPolicyRef
     |-ComputeRebootLog
     |-ComputeScrubPolicy
     |-DiagSrvCtrl
     |  |-DiagRslt
     |  |  |-DiagLogEp
     |  |-DiagRunPolicy
     |  |  |-DiagMemoryTest
     |  |-EtherServerIntFIo
     |     |-EquipmentXcvr
     |     |-EtherErrStats
     |     |  |-EtherErrStatsHist
     |     |-EtherLossStats
     |     |  |-EtherLossStatsHist
     |     |-EtherPauseStats
     |     |  |-EtherPauseStatsHist
     |     |-EtherRxStats
     |     |  |-EtherRxStatsHist
     |     |-EtherServerIntFIoFsm
     |     |  |-EtherServerIntFIoFsmStage
     |     |-EtherServerIntFIoFsmTask
     |     |-EtherTxStats
     |     |  |-EtherTxStatsHist
     |     |-EventInst
     |     |-FaultInst
     |     |-LldpAcquired
     |     |-PortDomainEp
     |     |-PortTrustMode
     |     |-SwUlan
     |-EquipmentBeaconLed
     |  |-EquipmentBeaconLedFsm
     |  |  |-EquipmentBeaconLedFsmStage
     |  |-EquipmentBeaconLedFsmTask
     |  |-EventInst
     |  |-FaultInst
     |-EquipmentHealthLed
     |  |-ComputeHealthLedSensorAlarm
     |  |-FaultInst
     |-EquipmentIOExpander
     |-EquipmentIndicatorLed
     |-EquipmentInventoryStatus
     |  |-FaultInst
     |-EquipmentLocatorLed
     |  |-EquipmentLocatorLedFsm
     |  |  |-EquipmentLocatorLedFsmStage
     |  |-EquipmentLocatorLedFsmTask
     |  |-EventInst
     |  |-FaultInst
     |-EquipmentPOST
     |-EventInst
     |-FabricLocale
     |  |-AdaptorExtEthIfPc
     |  |  |-AdaptorExtEthIfPcEp
     |  |  |-DcxVIf
     |  |     |-FaultInst
     |  |-DcxVc
     |  |  |-FabricNetGroupRef
     |  |  |  |-FaultInst
     |  |  |-FabricSanGroupRef
     |  |  |  |-FaultInst
     |  |  |-FaultInst
     |  |  |-SwCmclan
     |  |  |  |-FabricNetGroupRef
     |  |  |     |-FaultInst
     |  |  |-SwNetflowMonitorRef
     |  |  |-SwUlan
     |  |  |-SwVlan
     |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |-FaultInst
     |  |  |-SwVsan
     |  |     |-SwFcZoneSet
     |  |        |-SwFcServerZoneGroup
     |  |        |  |-SwZoneInitiatorMember
     |  |        |     |-SwFcZone
     |  |        |        |-SwZoneTargetMember
     |  |        |-SwFcUserZoneGroup
     |  |           |-SwFcUserZone
     |  |              |-SwFcEndpoint
     |  |-FabricPath
     |     |-DcxVc
     |     |  |-FabricNetGroupRef
     |     |  |  |-FaultInst
     |     |  |-FabricSanGroupRef
     |     |  |  |-FaultInst
     |     |  |-FaultInst
     |     |  |-SwCmclan
     |     |  |  |-FabricNetGroupRef
     |     |  |     |-FaultInst
     |     |  |-SwNetflowMonitorRef
     |     |  |-SwUlan
     |     |  |-SwVlan
     |     |  |  |-FabricNetflowIPv4Addr
     |     |  |  |-FaultInst
     |     |  |-SwVsan
     |     |     |-SwFcZoneSet
     |     |        |-SwFcServerZoneGroup
     |     |        |  |-SwZoneInitiatorMember
     |     |        |     |-SwFcZone
     |     |        |        |-SwZoneTargetMember
     |     |        |-SwFcUserZoneGroup
     |     |           |-SwFcUserZone
     |     |              |-SwFcEndpoint
     |     |-FabricPathConn
     |     |  |-FabricPathEp
     |     |     |-PortTrustMode
     |     |-FabricPathEp
     |        |-PortTrustMode
     |-FaultInst
     |-FaultSuppressTask
     |  |-FaultInst
     |  |-TrigLocalSched
     |     |-TrigAbsWindow
     |     |-TrigLocalAbsWindow
     |     |-TrigRecurrWindow
     |-FirmwareImageLock
     |-FirmwareStatus
     |  |-FaultInst
     |-LsIdentityInfo
     |  |-FaultInst
     |-LsbootDef
     |  |-LsbootBootSecurity
     |  |-LsbootEFIShell
     |  |-LsbootIScsi
     |  |  |-LsbootIScsiImagePath
     |  |     |-LsbootUEFIBootParam
     |  |-LsbootLan
     |  |  |-LsbootLanImagePath
     |  |     |-LsbootUEFIBootParam
     |  |     |-VnicIpV4StaticAddr
     |  |-LsbootSan
     |  |  |-LsbootSanCatSanImage
     |  |     |-LsbootSanCatSanImagePath
     |  |        |-LsbootUEFIBootParam
     |  |-LsbootStorage
     |  |  |-LsbootLocalStorage
     |  |  |  |-LsbootDefaultLocalImage
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootEmbeddedLocalDiskImage
     |  |  |  |  |-LsbootEmbeddedLocalDiskImagePath
     |  |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootEmbeddedLocalLunImage
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootLocalDiskImage
     |  |  |  |  |-LsbootLocalDiskImagePath
     |  |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootLocalHddImage
     |  |  |  |  |-LsbootLocalLunImagePath
     |  |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootNvme
     |  |  |  |  |-LsbootNvmeDiskSsd
     |  |  |  |  |-LsbootNvmePciSsd
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootUsbExternalImage
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootUsbFlashStorageImage
     |  |  |  |  |-LsbootUEFIBootParam
     |  |  |  |-LsbootUsbInternalImage
     |  |  |     |-LsbootUEFIBootParam
     |  |  |-LsbootSanImage
     |  |     |-LsbootSanImagePath
     |  |        |-LsbootUEFIBootParam
     |  |-LsbootVirtualMedia
     |-LstorageProfile
     |  |-LstorageControllerDef
     |  |  |-LstorageControllerModeConfig
     |  |  |-LstorageControllerQualifier
     |  |-LstorageDasScsiLun
     |  |  |-FaultInst
     |  |  |-StorageLocalDiskConfigDef
     |  |     |-LstorageSecurity
     |  |     |  |-LstorageDriveSecurity
     |  |     |     |-LstorageLocal
     |  |     |     |-LstorageRemote
     |  |     |        |-LstorageLogin
     |  |     |-StorageLocalDiskPartition
     |  |-LstorageLunSetConfig
     |  |  |-LstorageLunSetDiskSlot
     |  |  |-LstorageVirtualDriveDef
     |  |-LstorageSecurity
     |     |-LstorageDriveSecurity
     |        |-LstorageLocal
     |        |-LstorageRemote
     |           |-LstorageLogin
     |-MemoryRuntime
     |  |-MemoryRuntimeHist
     |-MgmtController
     |  |-CimcvmediaActualMountList
     |  |  |-CimcvmediaActualMountEntry
     |  |  |  |-FaultInst
     |  |  |-CimcvmediaExtMgmtRuleEntry
     |  |-EventInst
     |  |-FabricLocale
     |  |  |-AdaptorExtEthIfPc
     |  |  |  |-AdaptorExtEthIfPcEp
     |  |  |  |-DcxVIf
     |  |  |     |-FaultInst
     |  |  |-DcxVc
     |  |  |  |-FabricNetGroupRef
     |  |  |  |  |-FaultInst
     |  |  |  |-FabricSanGroupRef
     |  |  |  |  |-FaultInst
     |  |  |  |-FaultInst
     |  |  |  |-SwCmclan
     |  |  |  |  |-FabricNetGroupRef
     |  |  |  |     |-FaultInst
     |  |  |  |-SwNetflowMonitorRef
     |  |  |  |-SwUlan
     |  |  |  |-SwVlan
     |  |  |  |  |-FabricNetflowIPv4Addr
     |  |  |  |  |-FaultInst
     |  |  |  |-SwVsan
     |  |  |     |-SwFcZoneSet
     |  |  |        |-SwFcServerZoneGroup
     |  |  |        |  |-SwZoneInitiatorMember
     |  |  |        |     |-SwFcZone
     |  |  |        |        |-SwZoneTargetMember
     |  |  |        |-SwFcUserZoneGroup
     |  |  |           |-SwFcUserZone
     |  |  |              |-SwFcEndpoint
     |  |  |-FabricPath
     |  |     |-DcxVc
     |  |     |  |-FabricNetGroupRef
     |  |     |  |  |-FaultInst
     |  |     |  |-FabricSanGroupRef
     |  |     |  |  |-FaultInst
     |  |     |  |-FaultInst
     |  |     |  |-SwCmclan
     |  |     |  |  |-FabricNetGroupRef
     |  |     |  |     |-FaultInst
     |  |     |  |-SwNetflowMonitorRef
     |  |     |  |-SwUlan
     |  |     |  |-SwVlan
     |  |     |  |  |-FabricNetflowIPv4Addr
     |  |     |  |  |-FaultInst
     |  |     |  |-SwVsan
     |  |     |     |-SwFcZoneSet
     |  |     |        |-SwFcServerZoneGroup
     |  |     |        |  |-SwZoneInitiatorMember
     |  |     |        |     |-SwFcZone
     |  |     |        |        |-SwZoneTargetMember
     |  |     |        |-SwFcUserZoneGroup
     |  |     |           |-SwFcUserZone
     |  |     |              |-SwFcEndpoint
     |  |     |-FabricPathConn
     |  |     |  |-FabricPathEp
     |  |     |     |-PortTrustMode
     |  |     |-FabricPathEp
     |  |        |-PortTrustMode
     |  |-FaultInst
     |  |-FirmwareBootDefinition
     |  |  |-FirmwareBootUnit
     |  |  |  |-FaultInst
     |  |  |  |-FirmwareInstallable
     |  |  |  |  |-FirmwareUcscInfo
     |  |  |  |-FirmwareServicePack
     |  |  |-FirmwareUcscInfo
     |  |-FirmwareImage
     |  |  |-EventInst
     |  |  |-FaultInst
     |  |  |-FirmwareImageFsm
     |  |  |  |-FirmwareImageFsmStage
     |  |  |-FirmwareImageFsmTask
     |  |  |-FirmwareInstallable
     |  |  |  |-FirmwareUcscInfo
     |  |  |-FirmwareModule
     |  |-FirmwareRunning
     |  |  |-FirmwareServicePack
     |  |-FirmwareUpdatable
     |  |  |-FaultInst
     |  |  |-FirmwareInstallable
     |  |     |-FirmwareUcscInfo
     |  |-MgmtCimcSecureBoot
     |  |-MgmtCmcSecureBoot
     |  |-MgmtConnection
     |  |  |-FaultInst
     |  |-MgmtControllerFsm
     |  |  |-MgmtControllerFsmStage
     |  |-MgmtControllerFsmTask
     |  |-MgmtHealthStatus
     |  |  |-FaultInst
     |  |  |-MgmtHealthAttr
     |  |-MgmtIf
     |  |  |-DhcpAcquired
     |  |  |-EventInst
     |  |  |-FaultInst
     |  |  |-MgmtIPv6IfConfig
     |  |  |  |-MgmtIPv6IfAddr
     |  |  |     |-EventInst
     |  |  |     |-FaultInst
     |  |  |     |-MgmtIPv6IfAddrFsm
     |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |  |  |     |-MgmtIPv6IfAddrFsmTask
     |  |  |-MgmtIfFsm
     |  |  |  |-MgmtIfFsmStage
     |  |  |-MgmtIfFsmTask
     |  |-MgmtInterface
     |  |  |-FaultInst
     |  |  |-MgmtVnet
     |  |     |-VnicIpV4MgmtPooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV4History
     |  |     |-VnicIpV4PooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV4History
     |  |     |-VnicIpV4StaticAddr
     |  |     |-VnicIpV6MgmtPooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV6History
     |  |     |-VnicIpV6StaticAddr
     |  |-MgmtKvmCertificate
     |  |  |-FaultInst
     |  |-MgmtProfDerivedInterface
     |  |  |-MgmtVnet
     |  |     |-VnicIpV4MgmtPooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV4History
     |  |     |-VnicIpV4PooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV4History
     |  |     |-VnicIpV4StaticAddr
     |  |     |-VnicIpV6MgmtPooledAddr
     |  |     |  |-FaultInst
     |  |     |  |-VnicIpV6History
     |  |     |-VnicIpV6StaticAddr
     |  |-MgmtSpdmCertificateInventory
     |  |  |-MgmtSpdmCertificateData
     |  |-MgmtSwPersonalities
     |  |  |-MgmtSwPersonality
     |  |-MgmtSwPersonalitiesInventory
     |  |  |-MgmtSwPersonality
     |  |-MgmtUsbNicMgmtIf
     |  |-SysdebugMEpLog
     |  |  |-FaultInst
     |  |-VnicIpV4PooledAddr
     |  |  |-FaultInst
     |  |  |-VnicIpV4History
     |  |-VnicIpV4ProfDerivedAddr
     |  |-VnicIpV4StaticAddr
     |-MgmtKmipCertPolicy
     |-MgmtSecurity
     |  |-MgmtKmip
     |-MgmtSpdmCertificatePolicy
     |  |-MgmtSpdmCertificate
     |-MoKvCfgHolder
     |  |-MoIpV4AddrKv
     |  |  |-FaultInst
     |  |-MoIpV6AddrKv
     |  |  |-FaultInst
     |  |-MoKv
     |  |-MoVnicKv
     |-MoKvInvHolder
     |  |-MoInvKv
     |-OsAgent
     |-OsInstance
     |  |-OsEthBondIntf
     |  |  |-OsARPLinkMonitoringPolicy
     |  |  |  |-OsARPTarget
     |  |  |-OsEthBondModeActiveBackup
     |  |  |  |-OsPrimarySlave
     |  |  |-OsEthBondModeBalancedALB
     |  |  |  |-OsPrimarySlave
     |  |  |-OsEthBondModeBalancedRR
     |  |  |  |-OsPrimarySlave
     |  |  |-OsEthBondModeBalancedTLB
     |  |  |  |-OsPrimarySlave
     |  |  |-OsEthBondModeBalancedXOR
     |  |  |  |-OsPrimarySlave
     |  |  |-OsEthBondModeBroadcast
     |  |  |  |-OsPrimarySlave
     |  |  |-OsEthIntf
     |  |  |-OsMiiLinkMonitoringPolicy
     |  |-OsEthIntf
     |-PciEquipSlot
     |  |-FaultInst
     |-PciUnit
     |-PowerBudget
     |  |-FaultInst
     |  |-PowerProfiledPower
     |-ProcessorRuntime
     |  |-ProcessorRuntimeHist
     |-SolIf
     |-StorageEnclosure
     |  |-EventInst
     |  |-FaultInst
     |  |-StorageEnclosureDiskSlotEp
     |  |  |-FaultInst
     |  |  |-StorageControllerRef
     |  |-StorageEnclosureFsm
     |  |  |-StorageEnclosureFsmStage
     |  |-StorageEnclosureFsmTask
     |  |-StorageHddMotherBoardTempStats
     |  |  |-StorageHddMotherBoardTempStatsHist
     |  |-StorageLocalDisk
     |     |-EquipmentLocatorLed
     |     |  |-EquipmentLocatorLedFsm
     |     |  |  |-EquipmentLocatorLedFsmStage
     |     |  |-EquipmentLocatorLedFsmTask
     |     |  |-EventInst
     |     |  |-FaultInst
     |     |-EventInst
     |     |-FaultInst
     |     |-FirmwareBootDefinition
     |     |  |-FirmwareBootUnit
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareInstallable
     |     |  |  |  |-FirmwareUcscInfo
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUcscInfo
     |     |-FirmwareRunning
     |     |  |-FirmwareServicePack
     |     |-MgmtController
     |     |  |-CimcvmediaActualMountList
     |     |  |  |-CimcvmediaActualMountEntry
     |     |  |  |  |-FaultInst
     |     |  |  |-CimcvmediaExtMgmtRuleEntry
     |     |  |-EventInst
     |     |  |-FabricLocale
     |     |  |  |-AdaptorExtEthIfPc
     |     |  |  |  |-AdaptorExtEthIfPcEp
     |     |  |  |  |-DcxVIf
     |     |  |  |     |-FaultInst
     |     |  |  |-DcxVc
     |     |  |  |  |-FabricNetGroupRef
     |     |  |  |  |  |-FaultInst
     |     |  |  |  |-FabricSanGroupRef
     |     |  |  |  |  |-FaultInst
     |     |  |  |  |-FaultInst
     |     |  |  |  |-SwCmclan
     |     |  |  |  |  |-FabricNetGroupRef
     |     |  |  |  |     |-FaultInst
     |     |  |  |  |-SwNetflowMonitorRef
     |     |  |  |  |-SwUlan
     |     |  |  |  |-SwVlan
     |     |  |  |  |  |-FabricNetflowIPv4Addr
     |     |  |  |  |  |-FaultInst
     |     |  |  |  |-SwVsan
     |     |  |  |     |-SwFcZoneSet
     |     |  |  |        |-SwFcServerZoneGroup
     |     |  |  |        |  |-SwZoneInitiatorMember
     |     |  |  |        |     |-SwFcZone
     |     |  |  |        |        |-SwZoneTargetMember
     |     |  |  |        |-SwFcUserZoneGroup
     |     |  |  |           |-SwFcUserZone
     |     |  |  |              |-SwFcEndpoint
     |     |  |  |-FabricPath
     |     |  |     |-DcxVc
     |     |  |     |  |-FabricNetGroupRef
     |     |  |     |  |  |-FaultInst
     |     |  |     |  |-FabricSanGroupRef
     |     |  |     |  |  |-FaultInst
     |     |  |     |  |-FaultInst
     |     |  |     |  |-SwCmclan
     |     |  |     |  |  |-FabricNetGroupRef
     |     |  |     |  |     |-FaultInst
     |     |  |     |  |-SwNetflowMonitorRef
     |     |  |     |  |-SwUlan
     |     |  |     |  |-SwVlan
     |     |  |     |  |  |-FabricNetflowIPv4Addr
     |     |  |     |  |  |-FaultInst
     |     |  |     |  |-SwVsan
     |     |  |     |     |-SwFcZoneSet
     |     |  |     |        |-SwFcServerZoneGroup
     |     |  |     |        |  |-SwZoneInitiatorMember
     |     |  |     |        |     |-SwFcZone
     |     |  |     |        |        |-SwZoneTargetMember
     |     |  |     |        |-SwFcUserZoneGroup
     |     |  |     |           |-SwFcUserZone
     |     |  |     |              |-SwFcEndpoint
     |     |  |     |-FabricPathConn
     |     |  |     |  |-FabricPathEp
     |     |  |     |     |-PortTrustMode
     |     |  |     |-FabricPathEp
     |     |  |        |-PortTrustMode
     |     |  |-FaultInst
     |     |  |-FirmwareBootDefinition
     |     |  |  |-FirmwareBootUnit
     |     |  |  |  |-FaultInst
     |     |  |  |  |-FirmwareInstallable
     |     |  |  |  |  |-FirmwareUcscInfo
     |     |  |  |  |-FirmwareServicePack
     |     |  |  |-FirmwareUcscInfo
     |     |  |-FirmwareImage
     |     |  |  |-EventInst
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareImageFsm
     |     |  |  |  |-FirmwareImageFsmStage
     |     |  |  |-FirmwareImageFsmTask
     |     |  |  |-FirmwareInstallable
     |     |  |  |  |-FirmwareUcscInfo
     |     |  |  |-FirmwareModule
     |     |  |-FirmwareRunning
     |     |  |  |-FirmwareServicePack
     |     |  |-FirmwareUpdatable
     |     |  |  |-FaultInst
     |     |  |  |-FirmwareInstallable
     |     |  |     |-FirmwareUcscInfo
     |     |  |-MgmtCimcSecureBoot
     |     |  |-MgmtCmcSecureBoot
     |     |  |-MgmtConnection
     |     |  |  |-FaultInst
     |     |  |-MgmtControllerFsm
     |     |  |  |-MgmtControllerFsmStage
     |     |  |-MgmtControllerFsmTask
     |     |  |-MgmtHealthStatus
     |     |  |  |-FaultInst
     |     |  |  |-MgmtHealthAttr
     |     |  |-MgmtIf
     |     |  |  |-DhcpAcquired
     |     |  |  |-EventInst
     |     |  |  |-FaultInst
     |     |  |  |-MgmtIPv6IfConfig
     |     |  |  |  |-MgmtIPv6IfAddr
     |     |  |  |     |-EventInst
     |     |  |  |     |-FaultInst
     |     |  |  |     |-MgmtIPv6IfAddrFsm
     |     |  |  |     |  |-MgmtIPv6IfAddrFsmStage
     |     |  |  |     |-MgmtIPv6IfAddrFsmTask
     |     |  |  |-MgmtIfFsm
     |     |  |  |  |-MgmtIfFsmStage
     |     |  |  |-MgmtIfFsmTask
     |     |  |-MgmtInterface
     |     |  |  |-FaultInst
     |     |  |  |-MgmtVnet
     |     |  |     |-VnicIpV4MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4PooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4StaticAddr
     |     |  |     |-VnicIpV6MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV6History
     |     |  |     |-VnicIpV6StaticAddr
     |     |  |-MgmtKvmCertificate
     |     |  |  |-FaultInst
     |     |  |-MgmtProfDerivedInterface
     |     |  |  |-MgmtVnet
     |     |  |     |-VnicIpV4MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4PooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV4History
     |     |  |     |-VnicIpV4StaticAddr
     |     |  |     |-VnicIpV6MgmtPooledAddr
     |     |  |     |  |-FaultInst
     |     |  |     |  |-VnicIpV6History
     |     |  |     |-VnicIpV6StaticAddr
     |     |  |-MgmtSpdmCertificateInventory
     |     |  |  |-MgmtSpdmCertificateData
     |     |  |-MgmtSwPersonalities
     |     |  |  |-MgmtSwPersonality
     |     |  |-MgmtSwPersonalitiesInventory
     |     |  |  |-MgmtSwPersonality
     |     |  |-MgmtUsbNicMgmtIf
     |     |  |-SysdebugMEpLog
     |     |  |  |-FaultInst
     |     |  |-VnicIpV4PooledAddr
     |     |  |  |-FaultInst
     |     |  |  |-VnicIpV4History
     |     |  |-VnicIpV4ProfDerivedAddr
     |     |  |-VnicIpV4StaticAddr
     |     |-StorageControllerEp
     |     |-StorageDiskEnvStats
     |     |  |-StorageDiskEnvStatsHist
     |     |-StorageLocalDiskFsm
     |     |  |-StorageLocalDiskFsmStage
     |     |-StorageLocalDiskFsmTask
     |     |-StorageLocalDiskPartition
     |     |-StorageOperation
     |     |-StorageSasPort
     |     |-StorageSsdHealthStats
     |        |-StorageSsdHealthStatsHist
     |-StorageVirtualDriveContainer
     |  |-StorageVirtualDrive
     |     |-FaultInst
     |     |-StorageControllerEp
     |     |-StorageLunDisk
     |     |-StorageOperation
     |     |-StorageScsiLunRef
     |     |-StorageVDMemberEp
     |        |-FaultInst
     |-SwUlan
     |-SysdebugDiagnosticLog

ClassId                         ComputeBlade
-------                         ------------
xml_attribute                   :computeBlade
rn                              :blade-[slot_id]
min_version                     :1.0(1e)
access                          :InputOutput
access_privilege                :['admin', 'pn-equipment', 'pn-maintenance', 'pn-policy']
parents                         :['equipmentChassis']
children                        :['aaaEpAuthProfile', 'aaaEpUser', 'adaptorHostIfConfig', 'adaptorUnit', 'biosUnit', 'biosVIdentityParams', 'cimcvmediaMountConfigDef', 'computeAdminAck', 'computeBladeFsm', 'computeBladeFsmTask', 'computeBoard', 'computeBoardConnector', 'computeBoardController', 'computeExtBoard', 'computeFactoryResetOperation', 'computeFwSyncAck', 'computeHostUtilityOs', 'computeKvmMgmtPolicy', 'computeMemoryConfiguration', 'computePersonality', 'computePhysicalExtension', 'computePhysicalFsm', 'computePhysicalFsmTask', 'computePnuOSImage', 'computePoolable', 'computeRebootLog', 'computeScrubPolicy', 'diagSrvCtrl', 'equipmentBeaconLed', 'equipmentHealthLed', 'equipmentIOExpander', 'equipmentIndicatorLed', 'equipmentInventoryStatus', 'equipmentLocatorLed', 'equipmentPOST', 'eventInst', 'fabricLocale', 'faultInst', 'faultSuppressTask', 'firmwareImageLock', 'firmwareStatus', 'lsIdentityInfo', 'lsbootDef', 'lstorageProfile', 'memoryRuntime', 'mgmtController', 'mgmtKmipCertPolicy', 'mgmtSecurity', 'mgmtSpdmCertificatePolicy', 'moKvCfgHolder', 'moKvInvHolder', 'osAgent', 'osInstance', 'pciEquipSlot', 'pciUnit', 'powerBudget', 'processorRuntime', 'solIf', 'storageEnclosure', 'storageVirtualDriveContainer', 'swUlan', 'sysdebugDiagnosticLog']

Property                        admin_power
--------                        -----------
xml_attribute                   :adminPower
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['admin-down', 'admin-up', 'bios-password-reset-immediate', 'bmc-reset-immediate', 'bmc-reset-wait', 'cmos-reset-immediate', 'cycle-immediate', 'cycle-wait', 'diagnostic-interrupt', 'hard-reset-immediate', 'hard-reset-wait', 'ipmi-reset', 'kvm-reset', 'policy']
range_val                       :[]

Property                        admin_state
--------                        -----------
xml_attribute                   :adminState
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['in-maintenance', 'in-service', 'out-of-service']
range_val                       :[]

Property                        asset_tag
--------                        ---------
xml_attribute                   :assetTag
field_type                      :string
min_version                     :3.2(1d)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}
value_set                       :[]
range_val                       :[]

Property                        assigned_to_dn
--------                        --------------
xml_attribute                   :assignedToDn
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :256
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        association
--------                        -----------
xml_attribute                   :association
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['associated', 'establishing', 'failed', 'none', 'removing', 'throttled']
range_val                       :[]

Property                        availability
--------                        ------------
xml_attribute                   :availability
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['available', 'unavailable']
range_val                       :[]

Property                        available_memory
--------                        ----------------
xml_attribute                   :availableMemory
field_type                      :uint
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_id
--------                        ----------
xml_attribute                   :chassisId
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['N/A']
range_val                       :['0-255']

Property                        check_point
--------                        -----------
xml_attribute                   :checkPoint
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['deep-checkpoint', 'discovered', 'removing', 'shallow-checkpoint', 'unknown']
range_val                       :[]

Property                        child_action
--------                        ------------
xml_attribute                   :childAction
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}
value_set                       :[]
range_val                       :[]

Property                        conn_path
--------                        ---------
xml_attribute                   :connPath
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}
value_set                       :[]
range_val                       :[]

Property                        conn_status
--------                        -----------
xml_attribute                   :connStatus
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}
value_set                       :[]
range_val                       :[]

Property                        descr
--------                        -----
xml_attribute                   :descr
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}
value_set                       :[]
range_val                       :[]

Property                        discovery
--------                        ---------
xml_attribute                   :discovery
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['complete', 'diagnostics-complete', 'diagnostics-failed', 'diagnostics-in-progress', 'efidiagnostics-in-progress', 'failed', 'fru-identity-indeterminate', 'fru-not-ready', 'fru-state-indeterminate', 'illegal-fru', 'in-progress', 'insufficiently-equipped', 'invalid-adaptor-iocard', 'malformed-fru-info', 'retry', 'throttled', 'undiscovered', 'user-acknowledged', 'waiting-for-mgmt-ack', 'waiting-for-user-ack']
range_val                       :[]

Property                        discovery_status
--------                        ----------------
xml_attribute                   :discoveryStatus
field_type                      :string
min_version                     :2.5(1a)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}
value_set                       :[]
range_val                       :[]

Property                        dn
--------                        --
xml_attribute                   :dn
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :256
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        flt_aggr
--------                        --------
xml_attribute                   :fltAggr
field_type                      :ulong
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        fsm_descr
--------                        ---------
xml_attribute                   :fsmDescr
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        fsm_flags
--------                        ---------
xml_attribute                   :fsmFlags
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :['0-4294967295']

Property                        fsm_prev
--------                        --------
xml_attribute                   :fsmPrev
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['ActivateAdaptorActivateLocal', 'ActivateAdaptorActivatePeer', 'ActivateAdaptorAssertBypassWait', 'ActivateAdaptorBegin', 'ActivateAdaptorCheckPowerAvailability', 'ActivateAdaptorDeassertResetBypass', 'ActivateAdaptorFail', 'ActivateAdaptorPowerDeployWait', 'ActivateAdaptorPowerOn', 'ActivateAdaptorReset', 'ActivateAdaptorSuccess', 'ActivateBIOSActivate', 'ActivateBIOSBegin', 'ActivateBIOSCheckPowerAvailability', 'ActivateBIOSClear', 'ActivateBIOSFail', 'ActivateBIOSPollActivateStatus', 'ActivateBIOSPollClearStatus', 'ActivateBIOSPowerDeployWait', 'ActivateBIOSPowerOff', 'ActivateBIOSPowerOn', 'ActivateBIOSSuccess', 'ActivateBIOSUpdateTokens', 'AssociateActivateAdaptorNwFwLocal', 'AssociateActivateAdaptorNwFwPeer', 'AssociateActivateBios', 'AssociateActivateIBMCFw', 'AssociateAssertBypassWait', 'AssociateBegin', 'AssociateBiosImgUpdate', 'AssociateBiosPostCompletion', 'AssociateBladePowerOff', 'AssociateBmcConfigPnuOS', 'AssociateBmcPreconfigPnuOSLocal', 'AssociateBmcPreconfigPnuOSPeer', 'AssociateBmcUnconfigPnuOS', 'AssociateBootHost', 'AssociateBootPnuos', 'AssociateBootWait', 'AssociateCalculateVlanGroupForHostOSLocal', 'AssociateCalculateVlanGroupForHostOSPeer', 'AssociateCheckPowerAvailability', 'AssociateCiscoOSOpenGate', 'AssociateClearBiosUpdate', 'AssociateConfigCimcVMedia', 'AssociateConfigExtMgmtGw', 'AssociateConfigExtMgmtRules', 'AssociateConfigFanSpeed', 'AssociateConfigFlexFlash', 'AssociateConfigHostOsAnnotations', 'AssociateConfigMgmtIpRules', 'AssociateConfigServerIdentity', 'AssociateConfigSoL', 'AssociateConfigUserAccess', 'AssociateConfigUuid', 'AssociateCopyRemote', 'AssociateDeassertResetBypass', 'AssociateDeleteCurlDownloadedImages', 'AssociateDeleteImagesRemote', 'AssociateDownloadImages', 'AssociateFail', 'AssociateGraphicsImageUpdate', 'AssociateHagHostOSConnect', 'AssociateHagPnuOSConnect', 'AssociateHagPnuOSDisconnect', 'AssociateHbaImgUpdate', 'AssociateHostOSConfig', 'AssociateHostOSConnect', 'AssociateHostOSIdent', 'AssociateHostOSPolicy', 'AssociateHostOSValidate', 'AssociateLocalDiskFwUpdate', 'AssociateMarkAdapterForReboot', 'AssociateMswitchImgUpdate', 'AssociateNicConfigHostOSLocal', 'AssociateNicConfigHostOSPeer', 'AssociateNicConfigParamsHostOSLocal', 'AssociateNicConfigParamsHostOSPeer', 'AssociateNicConfigPnuOSLocal', 'AssociateNicConfigPnuOSPeer', 'AssociateNicConfigServiceInfraLocal', 'AssociateNicConfigServiceInfraPeer', 'AssociateNicImgUpdate', 'AssociateNicUnconfigPnuOSLocal', 'AssociateNicUnconfigPnuOSPeer', 'AssociateOobPollSasExpanderActivateStatus', 'AssociateOobPollSasExpanderBootImgActivateStatus', 'AssociateOobPollSasExpanderUpdateStatus', 'AssociateOobSasExpanderBootImgActivate', 'AssociateOobSasExpanderImgActivate', 'AssociateOobSasExpanderImgUpdate', 'AssociateOobStorageConfig', 'AssociateOobStorageInventory', 'AssociatePciSwitchImageUpdate', 'AssociatePersistentMemoryDimmFwUpdate', 'AssociatePnuOSCatalog', 'AssociatePnuOSConfig', 'AssociatePnuOSIdent', 'AssociatePnuOSInventory', 'AssociatePnuOSLocalDiskConfig', 'AssociatePnuOSPeripheralComponentConfig', 'AssociatePnuOSPolicy', 'AssociatePnuOSSelfTest', 'AssociatePnuOSUnloadDrivers', 'AssociatePnuOSValidate', 'AssociatePollBiosActivateStatus', 'AssociatePollBiosUpdateStatus', 'AssociatePollBoardCtrlPowerCycle', 'AssociatePollBoardCtrlUpdateStatus', 'AssociatePollClearBiosUpdateStatus', 'AssociatePowerCycleBoard', 'AssociatePowerDeployWait', 'AssociatePowerOn', 'AssociatePowerOnPreConfig', 'AssociatePreSanitize', 'AssociatePrepareForBoot', 'AssociateResetIBMC', 'AssociateRestoreVdStatus', 'AssociateSanitize', 'AssociateSasExpanderImgUpdate', 'AssociateSerialDebugPnuOSConnect', 'AssociateSerialDebugPnuOSDisconnect', 'AssociateSharedComponentsOobInventory', 'AssociateSharedComponentsOobInventoryPeer', 'AssociateSolRedirectDisable', 'AssociateSolRedirectEnable', 'AssociateStorageCtlrImgUpdate', 'AssociateSuccess', 'AssociateSwConfigHostOSLocal', 'AssociateSwConfigHostOSPeer', 'AssociateSwConfigPnuOSLocal', 'AssociateSwConfigPnuOSPeer', 'AssociateSwConfigPortNivLocal', 'AssociateSwConfigPortNivPeer', 'AssociateSwConfigServiceInfraLocal', 'AssociateSwConfigServiceInfraPeer', 'AssociateSwUnconfigPnuOSLocal', 'AssociateSwUnconfigPnuOSPeer', 'AssociateSyncPowerState', 'AssociateUnconfigCimcVMedia', 'AssociateUnconfigExtMgmtGw', 'AssociateUnconfigExtMgmtRules', 'AssociateUnlockFirmwareImage', 'AssociateUpdateAdaptorNwFwLocal', 'AssociateUpdateAdaptorNwFwPeer', 'AssociateUpdateBiosRequest', 'AssociateUpdateBoardCtrlRequest', 'AssociateUpdateIBMCFw', 'AssociateVerifyFcZoneConfig', 'AssociateWaitForAdaptorNwFwUpdateLocal', 'AssociateWaitForAdaptorNwFwUpdatePeer', 'AssociateWaitForBorderConfigCompletionLocal', 'AssociateWaitForBorderConfigCompletionPeer', 'AssociateWaitForIBMCFwUpdate', 'BiosPasswordResetBegin', 'BiosPasswordResetBladePowerOn', 'BiosPasswordResetCheckPowerAvailability', 'BiosPasswordResetExecute', 'BiosPasswordResetFail', 'BiosPasswordResetPowerDeployWait', 'BiosPasswordResetPreSanitize', 'BiosPasswordResetReconfigBios', 'BiosPasswordResetReconfigUuid', 'BiosPasswordResetSanitize', 'BiosPasswordResetSuccess', 'BiosRecoveryBegin', 'BiosRecoveryCheckPowerAvailability', 'BiosRecoveryCleanup', 'BiosRecoveryFail', 'BiosRecoveryPowerDeployWait', 'BiosRecoveryPreSanitize', 'BiosRecoveryReset', 'BiosRecoverySanitize', 'BiosRecoverySetupVmediaLocal', 'BiosRecoverySetupVmediaPeer', 'BiosRecoveryShutdown', 'BiosRecoveryStart', 'BiosRecoveryStopVMediaLocal', 'BiosRecoveryStopVMediaPeer', 'BiosRecoverySuccess', 'BiosRecoveryTeardownVmediaLocal', 'BiosRecoveryTeardownVmediaPeer', 'BiosRecoveryWait', 'CimcSecurityConfigBegin', 'CimcSecurityConfigFail', 'CimcSecurityConfigKmipCertConfig', 'CimcSecurityConfigKmipSaveCert', 'CimcSecurityConfigSuccess', 'CimcSecurityUnconfigBegin', 'CimcSecurityUnconfigFail', 'CimcSecurityUnconfigKmipDelCert', 'CimcSecurityUnconfigSuccess', 'CimcSessionDeleteBegin', 'CimcSessionDeleteExecute', 'CimcSessionDeleteFail', 'CimcSessionDeleteSuccess', 'CmosResetBegin', 'CmosResetBladePowerOn', 'CmosResetCheckPowerAvailability', 'CmosResetExecute', 'CmosResetFail', 'CmosResetPowerDeployWait', 'CmosResetPreSanitize', 'CmosResetReconfigBios', 'CmosResetReconfigUuid', 'CmosResetSanitize', 'CmosResetSuccess', 'ConfigBoardBegin', 'ConfigBoardConfigMemoryPolicy', 'ConfigBoardFail', 'ConfigBoardSuccess', 'ConfigSoLBegin', 'ConfigSoLExecute', 'ConfigSoLFail', 'ConfigSoLSuccess', 'ConfigureServerPersonalityBegin', 'ConfigureServerPersonalityExecute', 'ConfigureServerPersonalityFail', 'ConfigureServerPersonalitySuccess', 'DecommissionBegin', 'DecommissionCleanupCIMC', 'DecommissionCleanupPortConfigLocal', 'DecommissionCleanupPortConfigPeer', 'DecommissionExecute', 'DecommissionFail', 'DecommissionPrecleanupPortConfig', 'DecommissionStopVMediaLocal', 'DecommissionStopVMediaPeer', 'DecommissionSuccess', 'DecommissionUnconfigExtMgmtGw', 'DecommissionUnconfigExtMgmtRules', 'DiagBegin', 'DiagBiosPostCompletion', 'DiagCheckPowerAvailability', 'DiagDisableScriptableVMedia', 'DiagFail', 'DiagHagConnect', 'DiagHagDisconnect', 'DiagLogTransfer', 'DiagPnuOSIdent', 'DiagPowerOn', 'DiagPowerOnWait', 'DiagPreSanitize', 'DiagPreconfigVmediaLocal', 'DiagPreconfigVmediaPeer', 'DiagRunTests', 'DiagSanitize', 'DiagSerialDebugConnect', 'DiagSerialDebugDisconnect', 'DiagSetupBootEnvironment', 'DiagSetupVmediaLocal', 'DiagSetupVmediaPeer', 'DiagShutdown', 'DiagSuccess', 'DiagTearDownBootEnvironment', 'DiagTeardownVmediaLocal', 'DiagTeardownVmediaPeer', 'DiagWaitForDebug', 'DiagnosticInterruptBegin', 'DiagnosticInterruptExecute', 'DiagnosticInterruptFail', 'DiagnosticInterruptSuccess', 'DisassociateBegin', 'DisassociateBiosPostCompletion', 'DisassociateBmcConfigPnuOS', 'DisassociateBmcPreconfigPnuOSLocal', 'DisassociateBmcPreconfigPnuOSPeer', 'DisassociateBmcUnconfigPnuOS', 'DisassociateBootPnuos', 'DisassociateBootWait', 'DisassociateCheckPowerAvailability', 'DisassociateConfigBios', 'DisassociateConfigFlexFlashScrub', 'DisassociateConfigKvmMgmtDefaultSetting', 'DisassociateConfigUserAccess', 'DisassociateDeassertResetBypass', 'DisassociateFail', 'DisassociateHagPnuOSConnect', 'DisassociateHagPnuOSDisconnect', 'DisassociateHandlePooling', 'DisassociateNicConfigPnuOSLocal', 'DisassociateNicConfigPnuOSPeer', 'DisassociateNicUnconfigHostOSLocal', 'DisassociateNicUnconfigHostOSPeer', 'DisassociateNicUnconfigPnuOSLocal', 'DisassociateNicUnconfigPnuOSPeer', 'DisassociateNicUnconfigServiceInfraLocal', 'DisassociateNicUnconfigServiceInfraPeer', 'DisassociateOobDiskScrub', 'DisassociatePnuOSCatalog', 'DisassociatePnuOSIdent', 'DisassociatePnuOSPolicy', 'DisassociatePnuOSScrub', 'DisassociatePnuOSSelfTest', 'DisassociatePnuOSUnconfig', 'DisassociatePnuOSValidate', 'DisassociatePowerDeployWait', 'DisassociatePowerOn', 'DisassociatePreSanitize', 'DisassociateResetSecureBootConfig', 'DisassociateSanitize', 'DisassociateSerialDebugPnuOSConnect', 'DisassociateSerialDebugPnuOSDisconnect', 'DisassociateShutdown', 'DisassociateSolRedirectDisable', 'DisassociateSolRedirectEnable', 'DisassociateSuccess', 'DisassociateSwConfigPnuOSLocal', 'DisassociateSwConfigPnuOSPeer', 'DisassociateSwConfigPortNivLocal', 'DisassociateSwConfigPortNivPeer', 'DisassociateSwUnconfigHostOSLocal', 'DisassociateSwUnconfigHostOSPeer', 'DisassociateSwUnconfigPnuOSLocal', 'DisassociateSwUnconfigPnuOSPeer', 'DisassociateUnconfigBios', 'DisassociateUnconfigCimcVMedia', 'DisassociateUnconfigExtMgmtGw', 'DisassociateUnconfigExtMgmtRules', 'DisassociateUnconfigFlexFlash', 'DisassociateUnconfigServerIdentity', 'DisassociateUnconfigSoL', 'DisassociateUnconfigUuid', 'DisassociateVerifyFcZoneConfig', 'DiscoverBegin', 'DiscoverBiosPostCompletion', 'DiscoverBladeBootPnuos', 'DiscoverBladeBootWait', 'DiscoverBladePowerOn', 'DiscoverBladeReadSmbios', 'DiscoverBmcConfigPnuOS', 'DiscoverBmcFactoryReset', 'DiscoverBmcInventory', 'DiscoverBmcPreConfigPnuOSLocal', 'DiscoverBmcPreConfigPnuOSPeer', 'DiscoverBmcPresence', 'DiscoverBmcShutdownDiscovered', 'DiscoverCheckAdaptorFw40GCap', 'DiscoverCheckPowerAvailability', 'DiscoverConfigBMCPowerParams', 'DiscoverConfigFeLocal', 'DiscoverConfigFePeer', 'DiscoverConfigFlexFlashScrub', 'DiscoverConfigUserAccess', 'DiscoverFail', 'DiscoverHagConnect', 'DiscoverHagDisconnect', 'DiscoverHandlePooling', 'DiscoverNicConfigPnuOSLocal', 'DiscoverNicConfigPnuOSPeer', 'DiscoverNicPresenceLocal', 'DiscoverNicPresencePeer', 'DiscoverNicUnconfigPnuOSLocal', 'DiscoverNicUnconfigPnuOSPeer', 'DiscoverOobStorageInventory', 'DiscoverPnuOSCatalog', 'DiscoverPnuOSIdent', 'DiscoverPnuOSInventory', 'DiscoverPnuOSPolicy', 'DiscoverPnuOSPowerProfiling', 'DiscoverPnuOSScrub', 'DiscoverPnuOSSelfTest', 'DiscoverPostScrubOobStorageInventory', 'DiscoverPowerDeployWait', 'DiscoverPreSanitize', 'DiscoverSanitize', 'DiscoverSendBmcProfilingDone', 'DiscoverSendBmcProfilingInit', 'DiscoverSerialDebugConnect', 'DiscoverSerialDebugDisconnect', 'DiscoverSetupVmediaLocal', 'DiscoverSetupVmediaPeer', 'DiscoverSharedComponentsOobInventory', 'DiscoverSharedComponentsOobInventoryPeer', 'DiscoverSolRedirectDisable', 'DiscoverSolRedirectEnable', 'DiscoverSuccess', 'DiscoverSwConfigPnuOSLocal', 'DiscoverSwConfigPnuOSPeer', 'DiscoverSwUnconfigPnuOSLocal', 'DiscoverSwUnconfigPnuOSPeer', 'DiscoverTeardownVmediaLocal', 'DiscoverTeardownVmediaPeer', 'DiscoverUnconfigCimcVMedia', 'DiscoverUnconfigExtMgmtGw', 'DiscoverUnconfigExtMgmtRules', 'DiskZoningInventoryBegin', 'DiskZoningInventoryBootHost', 'DiskZoningInventoryBootWait', 'DiskZoningInventoryFail', 'DiskZoningInventoryPreSanitize', 'DiskZoningInventorySanitize', 'DiskZoningInventoryShutdown', 'DiskZoningInventoryStorageInventory', 'DiskZoningInventorySuccess', 'EnableCimcSecureBootActivate', 'EnableCimcSecureBootBegin', 'EnableCimcSecureBootFail', 'EnableCimcSecureBootPollUpdateStatus', 'EnableCimcSecureBootReset', 'EnableCimcSecureBootSuccess', 'EnableCimcSecureBootUpdateRequest', 'ExecuteActionsBegin', 'ExecuteActionsBiosPostCompletion', 'ExecuteActionsExecutePMAction', 'ExecuteActionsFail', 'ExecuteActionsPowerOn', 'ExecuteActionsSoftShutdown', 'ExecuteActionsSuccess', 'FlashControllerBegin', 'FlashControllerFail', 'FlashControllerSuccess', 'FlashControllerUpdateFlashLife', 'FwUpgradeActivateAdaptorNwFwLocal', 'FwUpgradeActivateAdaptorNwFwPeer', 'FwUpgradeActivateBios', 'FwUpgradeActivateIBMCFw', 'FwUpgradeAssertBypassWait', 'FwUpgradeBegin', 'FwUpgradeBiosImgUpdate', 'FwUpgradeBiosPostCompletion', 'FwUpgradeBladePowerOff', 'FwUpgradeBmcConfigPnuOS', 'FwUpgradeBmcPreconfigPnuOSLocal', 'FwUpgradeBmcPreconfigPnuOSPeer', 'FwUpgradeBmcUnconfigPnuOS', 'FwUpgradeBootPnuos', 'FwUpgradeBootWait', 'FwUpgradeCheckPowerAvailability', 'FwUpgradeCiscoOSOpenGate', 'FwUpgradeClearBiosUpdate', 'FwUpgradeCopyRemote', 'FwUpgradeDeassertResetBypass', 'FwUpgradeDeleteCurlDownloadedImages', 'FwUpgradeDeleteImagesRemote', 'FwUpgradeDownloadImages', 'FwUpgradeFail', 'FwUpgradeGraphicsImageUpdate', 'FwUpgradeHagPnuOSConnect', 'FwUpgradeHagPnuOSDisconnect', 'FwUpgradeHbaImgUpdate', 'FwUpgradeLocalDiskFwUpdate', 'FwUpgradeMswitchImgUpdate', 'FwUpgradeNicConfigPnuOSLocal', 'FwUpgradeNicConfigPnuOSPeer', 'FwUpgradeNicImgUpdate', 'FwUpgradeNicUnconfigPnuOSLocal', 'FwUpgradeNicUnconfigPnuOSPeer', 'FwUpgradeOobPollSasExpanderActivateStatus', 'FwUpgradeOobPollSasExpanderBootImgActivateStatus', 'FwUpgradeOobPollSasExpanderUpdateStatus', 'FwUpgradeOobSasExpanderBootImgActivate', 'FwUpgradeOobSasExpanderImgActivate', 'FwUpgradeOobSasExpanderImgUpdate', 'FwUpgradeOobStorageInventory', 'FwUpgradePciSwitchImageUpdate', 'FwUpgradePersistentMemoryDimmFwUpdate', 'FwUpgradePnuOSCatalog', 'FwUpgradePnuOSConfig', 'FwUpgradePnuOSIdent', 'FwUpgradePnuOSInventory', 'FwUpgradePnuOSPolicy', 'FwUpgradePnuOSSelfTest', 'FwUpgradePnuOSUnloadDrivers', 'FwUpgradePnuOSValidate', 'FwUpgradePollBiosActivateStatus', 'FwUpgradePollBiosUpdateStatus', 'FwUpgradePollBoardCtrlPowerCycle', 'FwUpgradePollBoardCtrlUpdateStatus', 'FwUpgradePollClearBiosUpdateStatus', 'FwUpgradePowerCycleBoard', 'FwUpgradePowerDeployWait', 'FwUpgradePowerOn', 'FwUpgradePreSanitize', 'FwUpgradeResetIBMC', 'FwUpgradeSanitize', 'FwUpgradeSasExpanderImgUpdate', 'FwUpgradeSerialDebugPnuOSConnect', 'FwUpgradeSerialDebugPnuOSDisconnect', 'FwUpgradeShutdown', 'FwUpgradeSolRedirectDisable', 'FwUpgradeSolRedirectEnable', 'FwUpgradeStorageCtlrImgUpdate', 'FwUpgradeSuccess', 'FwUpgradeSwConfigPnuOSLocal', 'FwUpgradeSwConfigPnuOSPeer', 'FwUpgradeSwConfigPortNivLocal', 'FwUpgradeSwConfigPortNivPeer', 'FwUpgradeSwUnconfigPnuOSLocal', 'FwUpgradeSwUnconfigPnuOSPeer', 'FwUpgradeUnconfigCimcVMedia', 'FwUpgradeUnconfigExtMgmtGw', 'FwUpgradeUnconfigExtMgmtRules', 'FwUpgradeUnlockFirmwareImage', 'FwUpgradeUpdateAdaptorNwFwLocal', 'FwUpgradeUpdateAdaptorNwFwPeer', 'FwUpgradeUpdateBiosRequest', 'FwUpgradeUpdateBoardCtrlRequest', 'FwUpgradeUpdateIBMCFw', 'FwUpgradeWaitForAdaptorNwFwUpdateLocal', 'FwUpgradeWaitForAdaptorNwFwUpdatePeer', 'FwUpgradeWaitForIBMCFwUpdate', 'HardShutdownBegin', 'HardShutdownExecute', 'HardShutdownFail', 'HardShutdownSuccess', 'HardresetBegin', 'HardresetCheckPowerAvailability', 'HardresetExecute', 'HardresetFail', 'HardresetPowerDeployWait', 'HardresetPreSanitize', 'HardresetSanitize', 'HardresetSuccess', 'NvmeSwitchRecoveryBegin', 'NvmeSwitchRecoveryCheckStatus', 'NvmeSwitchRecoveryExecute', 'NvmeSwitchRecoveryFail', 'NvmeSwitchRecoverySuccess', 'NvmeSwitchRecoveryWaitForAck', 'OobStorageAdminConfigBegin', 'OobStorageAdminConfigBootHost', 'OobStorageAdminConfigBootWait', 'OobStorageAdminConfigCheckPowerAvailability', 'OobStorageAdminConfigFail', 'OobStorageAdminConfigOobStorageConfig', 'OobStorageAdminConfigOobStorageInventory', 'OobStorageAdminConfigPowerDeployWait', 'OobStorageAdminConfigPreSanitize', 'OobStorageAdminConfigSanitize', 'OobStorageAdminConfigShutdown', 'OobStorageAdminConfigSuccess', 'OobStorageAdminConfigTearDownVMediaLocal', 'OobStorageAdminConfigTearDownVMediaPeer', 'PowerCapBegin', 'PowerCapConfig', 'PowerCapFail', 'PowerCapSuccess', 'PowercycleBegin', 'PowercycleCheckPowerAvailability', 'PowercycleExecute', 'PowercycleFail', 'PowercyclePowerDeployWait', 'PowercyclePreSanitize', 'PowercycleSanitize', 'PowercycleSuccess', 'ReinitializeVirtualDriveBegin', 'ReinitializeVirtualDriveExecuteVDAction', 'ReinitializeVirtualDriveFail', 'ReinitializeVirtualDriveSuccess', 'ResetBmcBegin', 'ResetBmcExecute', 'ResetBmcFail', 'ResetBmcSuccess', 'ResetIpmiBegin', 'ResetIpmiExecute', 'ResetIpmiFail', 'ResetIpmiSuccess', 'ResetKvmBegin', 'ResetKvmExecute', 'ResetKvmFail', 'ResetKvmSuccess', 'ResetMemoryErrorsBegin', 'ResetMemoryErrorsExecute', 'ResetMemoryErrorsFail', 'ResetMemoryErrorsSuccess', 'ServiceInfraDeployBegin', 'ServiceInfraDeployFail', 'ServiceInfraDeployNicConfigLocal', 'ServiceInfraDeployNicConfigPeer', 'ServiceInfraDeploySuccess', 'ServiceInfraDeploySwConfigLocal', 'ServiceInfraDeploySwConfigPeer', 'ServiceInfraWithdrawBegin', 'ServiceInfraWithdrawFail', 'ServiceInfraWithdrawNicUnConfigLocal', 'ServiceInfraWithdrawNicUnConfigPeer', 'ServiceInfraWithdrawSuccess', 'ServiceInfraWithdrawSwUnConfigLocal', 'ServiceInfraWithdrawSwUnConfigPeer', 'SoftShutdownBegin', 'SoftShutdownExecute', 'SoftShutdownFail', 'SoftShutdownSuccess', 'SoftresetBegin', 'SoftresetCheckPowerAvailability', 'SoftresetExecute', 'SoftresetFail', 'SoftresetPowerDeployWait', 'SoftresetPreSanitize', 'SoftresetSanitize', 'SoftresetSuccess', 'SwConnUpdA', 'SwConnUpdB', 'SwConnUpdBegin', 'SwConnUpdFail', 'SwConnUpdSuccess', 'TurnupBegin', 'TurnupCheckPowerAvailability', 'TurnupExecute', 'TurnupFail', 'TurnupPowerDeployWait', 'TurnupSuccess', 'UnconfigSoLBegin', 'UnconfigSoLExecute', 'UnconfigSoLFail', 'UnconfigSoLSuccess', 'UpdateAdaptorBegin', 'UpdateAdaptorCheckPowerAvailability', 'UpdateAdaptorFail', 'UpdateAdaptorPollUpdateStatusLocal', 'UpdateAdaptorPollUpdateStatusPeer', 'UpdateAdaptorPowerDeployWait', 'UpdateAdaptorPowerOff', 'UpdateAdaptorPowerOn', 'UpdateAdaptorSuccess', 'UpdateAdaptorUpdateRequestLocal', 'UpdateAdaptorUpdateRequestPeer', 'UpdateBIOSBegin', 'UpdateBIOSClear', 'UpdateBIOSFail', 'UpdateBIOSPollClearStatus', 'UpdateBIOSPollUpdateStatus', 'UpdateBIOSSuccess', 'UpdateBIOSUpdateRequest', 'UpdateBoardControllerBegin', 'UpdateBoardControllerCheckPowerAvailability', 'UpdateBoardControllerFail', 'UpdateBoardControllerPollBoardCtrlPowerCycle', 'UpdateBoardControllerPollUpdateStatus', 'UpdateBoardControllerPowerCycleBoard', 'UpdateBoardControllerPowerDeployWait', 'UpdateBoardControllerPrepareForUpdate', 'UpdateBoardControllerServerPowerOff', 'UpdateBoardControllerServerPowerOn', 'UpdateBoardControllerSuccess', 'UpdateBoardControllerUpdateRequest', 'clearTPMBegin', 'clearTPMBiosPostCompletion', 'clearTPMBladePowerOff', 'clearTPMBladePowerOn', 'clearTPMBootHost', 'clearTPMClear', 'clearTPMFail', 'clearTPMPreSanitize', 'clearTPMReadSmBios', 'clearTPMReconfigBios', 'clearTPMSanitize', 'clearTPMSetupVmedia', 'clearTPMStopVMediaLocal', 'clearTPMStopVMediaPeer', 'clearTPMSuccess', 'clearTPMUnconfigVmedia', 'nop', 'updateExtUsersBegin', 'updateExtUsersDeploy', 'updateExtUsersFail', 'updateExtUsersSuccess']
range_val                       :[]

Property                        fsm_progr
--------                        ---------
xml_attribute                   :fsmProgr
field_type                      :byte
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :['0-100']

Property                        fsm_rmt_inv_err_code
--------                        --------------------
xml_attribute                   :fsmRmtInvErrCode
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['ERR-2fa-auth-retry', 'ERR-ACTIVATE-failed', 'ERR-ACTIVATE-in-progress', 'ERR-ACTIVATE-retry', 'ERR-BIOS-TOKENS-OLD-BIOS', 'ERR-BIOS-TOKENS-OLD-CIMC', 'ERR-BIOS-network-boot-order-not-found', 'ERR-BOARDCTRLUPDATE-ignore', 'ERR-DIAG-cancelled', 'ERR-DIAG-fsm-restarted', 'ERR-DIAG-test-failed', 'ERR-DNLD-authentication-failure', 'ERR-DNLD-hostkey-mismatch', 'ERR-DNLD-invalid-image', 'ERR-DNLD-no-file', 'ERR-DNLD-no-space', 'ERR-DNLD-usb-unmounted', 'ERR-DNS-delete-error', 'ERR-DNS-get-error', 'ERR-DNS-set-error', 'ERR-Diagnostics-in-progress', 'ERR-Diagnostics-memtest-in-progress', 'ERR-Diagnostics-network-in-progress', 'ERR-FILTER-illegal-format', 'ERR-FSM-no-such-state', 'ERR-HOST-fru-identity-mismatch', 'ERR-HTTP-set-error', 'ERR-HTTPS-set-error', 'ERR-IBMC-analyze-results', 'ERR-IBMC-connect-error', 'ERR-IBMC-connector-info-retrieval-error', 'ERR-IBMC-fru-retrieval-error', 'ERR-IBMC-invalid-end-point-config', 'ERR-IBMC-results-not-ready', 'ERR-MAX-subscriptions-allowed-error', 'ERR-MO-CONFIG-child-object-cant-be-configured', 'ERR-MO-META-no-such-object-class', 'ERR-MO-PROPERTY-no-such-property', 'ERR-MO-PROPERTY-value-out-of-range', 'ERR-MO-access-denied', 'ERR-MO-deletion-rule-violation', 'ERR-MO-duplicate-object', 'ERR-MO-illegal-containment', 'ERR-MO-illegal-creation', 'ERR-MO-illegal-iterator-state', 'ERR-MO-illegal-object-lifecycle-transition', 'ERR-MO-naming-rule-violation', 'ERR-MO-object-not-found', 'ERR-MO-resource-allocation', 'ERR-NTP-delete-error', 'ERR-NTP-get-error', 'ERR-NTP-set-error', 'ERR-POWER-CAP-UNSUPPORTED', 'ERR-POWER-PROFILE-IN-PROGRESS', 'ERR-SERVER-mis-connect', 'ERR-SWITCH-invalid-if-config', 'ERR-TOKEN-request-denied', 'ERR-UNABLE-TO-FETCH-BIOS-SETTINGS', 'ERR-UPDATE-failed', 'ERR-UPDATE-in-progress', 'ERR-UPDATE-retry', 'ERR-aaa-config-modify-error', 'ERR-acct-realm-set-error', 'ERR-admin-passwd-set', 'ERR-auth-issue', 'ERR-auth-realm-get-error', 'ERR-auth-realm-set-error', 'ERR-authentication', 'ERR-authorization-required', 'ERR-cli-session-limit-reached', 'ERR-create-keyring', 'ERR-create-locale', 'ERR-create-role', 'ERR-create-tp', 'ERR-create-user', 'ERR-delete-locale', 'ERR-delete-role', 'ERR-delete-session', 'ERR-delete-user', 'ERR-downgrade-fail', 'ERR-efi-Diagnostics--in-progress', 'ERR-enable-mgmt-conn', 'ERR-ep-set-error', 'ERR-get-max-http-user-sessions', 'ERR-http-initializing', 'ERR-insufficiently-equipped', 'ERR-internal-error', 'ERR-ldap-delete-error', 'ERR-ldap-get-error', 'ERR-ldap-group-modify-error', 'ERR-ldap-group-set-error', 'ERR-ldap-set-error', 'ERR-locale-set-error', 'ERR-max-userid-sessions-reached', 'ERR-missing-method', 'ERR-modify-locale', 'ERR-modify-role', 'ERR-modify-user', 'ERR-modify-user-locale', 'ERR-modify-user-role', 'ERR-provider-group-modify-error', 'ERR-provider-group-set-error', 'ERR-radius-get-error', 'ERR-radius-global-set-error', 'ERR-radius-group-set-error', 'ERR-radius-set-error', 'ERR-request-timeout', 'ERR-reset-adapter', 'ERR-role-set-error', 'ERR-secondary-node', 'ERR-service-not-ready', 'ERR-session-cache-full', 'ERR-session-not-found', 'ERR-set-key-cert', 'ERR-set-login-profile', 'ERR-set-min-passphrase-length', 'ERR-set-network', 'ERR-set-password-strength-check', 'ERR-set-port-channel', 'ERR-store-pre-login-banner-msg', 'ERR-tacacs-enable-error', 'ERR-tacacs-global-set-error', 'ERR-tacacs-group-set-error', 'ERR-tacacs-plus-get-error', 'ERR-tacacs-set-error', 'ERR-test-error-1', 'ERR-test-error-2', 'ERR-timezone-set-error', 'ERR-user-account-expired', 'ERR-user-passwd-expired', 'ERR-user-set-error', 'ERR-xml-parse-error', 'none']
range_val                       :['0-4294967295']

Property                        fsm_rmt_inv_err_descr
--------                        ---------------------
xml_attribute                   :fsmRmtInvErrDescr
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        fsm_rmt_inv_rslt
--------                        ----------------
xml_attribute                   :fsmRmtInvRslt
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}
value_set                       :[]
range_val                       :[]

Property                        fsm_stage_descr
--------                        ---------------
xml_attribute                   :fsmStageDescr
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        fsm_stamp
--------                        ---------
xml_attribute                   :fsmStamp
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}
value_set                       :['never']
range_val                       :[]

Property                        fsm_status
--------                        ----------
xml_attribute                   :fsmStatus
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['ActivateAdaptorActivateLocal', 'ActivateAdaptorActivatePeer', 'ActivateAdaptorAssertBypassWait', 'ActivateAdaptorBegin', 'ActivateAdaptorCheckPowerAvailability', 'ActivateAdaptorDeassertResetBypass', 'ActivateAdaptorFail', 'ActivateAdaptorPowerDeployWait', 'ActivateAdaptorPowerOn', 'ActivateAdaptorReset', 'ActivateAdaptorSuccess', 'ActivateBIOSActivate', 'ActivateBIOSBegin', 'ActivateBIOSCheckPowerAvailability', 'ActivateBIOSClear', 'ActivateBIOSFail', 'ActivateBIOSPollActivateStatus', 'ActivateBIOSPollClearStatus', 'ActivateBIOSPowerDeployWait', 'ActivateBIOSPowerOff', 'ActivateBIOSPowerOn', 'ActivateBIOSSuccess', 'ActivateBIOSUpdateTokens', 'AssociateActivateAdaptorNwFwLocal', 'AssociateActivateAdaptorNwFwPeer', 'AssociateActivateBios', 'AssociateActivateIBMCFw', 'AssociateAssertBypassWait', 'AssociateBegin', 'AssociateBiosImgUpdate', 'AssociateBiosPostCompletion', 'AssociateBladePowerOff', 'AssociateBmcConfigPnuOS', 'AssociateBmcPreconfigPnuOSLocal', 'AssociateBmcPreconfigPnuOSPeer', 'AssociateBmcUnconfigPnuOS', 'AssociateBootHost', 'AssociateBootPnuos', 'AssociateBootWait', 'AssociateCalculateVlanGroupForHostOSLocal', 'AssociateCalculateVlanGroupForHostOSPeer', 'AssociateCheckPowerAvailability', 'AssociateCiscoOSOpenGate', 'AssociateClearBiosUpdate', 'AssociateConfigCimcVMedia', 'AssociateConfigExtMgmtGw', 'AssociateConfigExtMgmtRules', 'AssociateConfigFanSpeed', 'AssociateConfigFlexFlash', 'AssociateConfigHostOsAnnotations', 'AssociateConfigMgmtIpRules', 'AssociateConfigServerIdentity', 'AssociateConfigSoL', 'AssociateConfigUserAccess', 'AssociateConfigUuid', 'AssociateCopyRemote', 'AssociateDeassertResetBypass', 'AssociateDeleteCurlDownloadedImages', 'AssociateDeleteImagesRemote', 'AssociateDownloadImages', 'AssociateFail', 'AssociateGraphicsImageUpdate', 'AssociateHagHostOSConnect', 'AssociateHagPnuOSConnect', 'AssociateHagPnuOSDisconnect', 'AssociateHbaImgUpdate', 'AssociateHostOSConfig', 'AssociateHostOSConnect', 'AssociateHostOSIdent', 'AssociateHostOSPolicy', 'AssociateHostOSValidate', 'AssociateLocalDiskFwUpdate', 'AssociateMarkAdapterForReboot', 'AssociateMswitchImgUpdate', 'AssociateNicConfigHostOSLocal', 'AssociateNicConfigHostOSPeer', 'AssociateNicConfigParamsHostOSLocal', 'AssociateNicConfigParamsHostOSPeer', 'AssociateNicConfigPnuOSLocal', 'AssociateNicConfigPnuOSPeer', 'AssociateNicConfigServiceInfraLocal', 'AssociateNicConfigServiceInfraPeer', 'AssociateNicImgUpdate', 'AssociateNicUnconfigPnuOSLocal', 'AssociateNicUnconfigPnuOSPeer', 'AssociateOobPollSasExpanderActivateStatus', 'AssociateOobPollSasExpanderBootImgActivateStatus', 'AssociateOobPollSasExpanderUpdateStatus', 'AssociateOobSasExpanderBootImgActivate', 'AssociateOobSasExpanderImgActivate', 'AssociateOobSasExpanderImgUpdate', 'AssociateOobStorageConfig', 'AssociateOobStorageInventory', 'AssociatePciSwitchImageUpdate', 'AssociatePersistentMemoryDimmFwUpdate', 'AssociatePnuOSCatalog', 'AssociatePnuOSConfig', 'AssociatePnuOSIdent', 'AssociatePnuOSInventory', 'AssociatePnuOSLocalDiskConfig', 'AssociatePnuOSPeripheralComponentConfig', 'AssociatePnuOSPolicy', 'AssociatePnuOSSelfTest', 'AssociatePnuOSUnloadDrivers', 'AssociatePnuOSValidate', 'AssociatePollBiosActivateStatus', 'AssociatePollBiosUpdateStatus', 'AssociatePollBoardCtrlPowerCycle', 'AssociatePollBoardCtrlUpdateStatus', 'AssociatePollClearBiosUpdateStatus', 'AssociatePowerCycleBoard', 'AssociatePowerDeployWait', 'AssociatePowerOn', 'AssociatePowerOnPreConfig', 'AssociatePreSanitize', 'AssociatePrepareForBoot', 'AssociateResetIBMC', 'AssociateRestoreVdStatus', 'AssociateSanitize', 'AssociateSasExpanderImgUpdate', 'AssociateSerialDebugPnuOSConnect', 'AssociateSerialDebugPnuOSDisconnect', 'AssociateSharedComponentsOobInventory', 'AssociateSharedComponentsOobInventoryPeer', 'AssociateSolRedirectDisable', 'AssociateSolRedirectEnable', 'AssociateStorageCtlrImgUpdate', 'AssociateSuccess', 'AssociateSwConfigHostOSLocal', 'AssociateSwConfigHostOSPeer', 'AssociateSwConfigPnuOSLocal', 'AssociateSwConfigPnuOSPeer', 'AssociateSwConfigPortNivLocal', 'AssociateSwConfigPortNivPeer', 'AssociateSwConfigServiceInfraLocal', 'AssociateSwConfigServiceInfraPeer', 'AssociateSwUnconfigPnuOSLocal', 'AssociateSwUnconfigPnuOSPeer', 'AssociateSyncPowerState', 'AssociateUnconfigCimcVMedia', 'AssociateUnconfigExtMgmtGw', 'AssociateUnconfigExtMgmtRules', 'AssociateUnlockFirmwareImage', 'AssociateUpdateAdaptorNwFwLocal', 'AssociateUpdateAdaptorNwFwPeer', 'AssociateUpdateBiosRequest', 'AssociateUpdateBoardCtrlRequest', 'AssociateUpdateIBMCFw', 'AssociateVerifyFcZoneConfig', 'AssociateWaitForAdaptorNwFwUpdateLocal', 'AssociateWaitForAdaptorNwFwUpdatePeer', 'AssociateWaitForBorderConfigCompletionLocal', 'AssociateWaitForBorderConfigCompletionPeer', 'AssociateWaitForIBMCFwUpdate', 'BiosPasswordResetBegin', 'BiosPasswordResetBladePowerOn', 'BiosPasswordResetCheckPowerAvailability', 'BiosPasswordResetExecute', 'BiosPasswordResetFail', 'BiosPasswordResetPowerDeployWait', 'BiosPasswordResetPreSanitize', 'BiosPasswordResetReconfigBios', 'BiosPasswordResetReconfigUuid', 'BiosPasswordResetSanitize', 'BiosPasswordResetSuccess', 'BiosRecoveryBegin', 'BiosRecoveryCheckPowerAvailability', 'BiosRecoveryCleanup', 'BiosRecoveryFail', 'BiosRecoveryPowerDeployWait', 'BiosRecoveryPreSanitize', 'BiosRecoveryReset', 'BiosRecoverySanitize', 'BiosRecoverySetupVmediaLocal', 'BiosRecoverySetupVmediaPeer', 'BiosRecoveryShutdown', 'BiosRecoveryStart', 'BiosRecoveryStopVMediaLocal', 'BiosRecoveryStopVMediaPeer', 'BiosRecoverySuccess', 'BiosRecoveryTeardownVmediaLocal', 'BiosRecoveryTeardownVmediaPeer', 'BiosRecoveryWait', 'CimcSecurityConfigBegin', 'CimcSecurityConfigFail', 'CimcSecurityConfigKmipCertConfig', 'CimcSecurityConfigKmipSaveCert', 'CimcSecurityConfigSuccess', 'CimcSecurityUnconfigBegin', 'CimcSecurityUnconfigFail', 'CimcSecurityUnconfigKmipDelCert', 'CimcSecurityUnconfigSuccess', 'CimcSessionDeleteBegin', 'CimcSessionDeleteExecute', 'CimcSessionDeleteFail', 'CimcSessionDeleteSuccess', 'CmosResetBegin', 'CmosResetBladePowerOn', 'CmosResetCheckPowerAvailability', 'CmosResetExecute', 'CmosResetFail', 'CmosResetPowerDeployWait', 'CmosResetPreSanitize', 'CmosResetReconfigBios', 'CmosResetReconfigUuid', 'CmosResetSanitize', 'CmosResetSuccess', 'ConfigBoardBegin', 'ConfigBoardConfigMemoryPolicy', 'ConfigBoardFail', 'ConfigBoardSuccess', 'ConfigSoLBegin', 'ConfigSoLExecute', 'ConfigSoLFail', 'ConfigSoLSuccess', 'ConfigureServerPersonalityBegin', 'ConfigureServerPersonalityExecute', 'ConfigureServerPersonalityFail', 'ConfigureServerPersonalitySuccess', 'DecommissionBegin', 'DecommissionCleanupCIMC', 'DecommissionCleanupPortConfigLocal', 'DecommissionCleanupPortConfigPeer', 'DecommissionExecute', 'DecommissionFail', 'DecommissionPrecleanupPortConfig', 'DecommissionStopVMediaLocal', 'DecommissionStopVMediaPeer', 'DecommissionSuccess', 'DecommissionUnconfigExtMgmtGw', 'DecommissionUnconfigExtMgmtRules', 'DiagBegin', 'DiagBiosPostCompletion', 'DiagCheckPowerAvailability', 'DiagDisableScriptableVMedia', 'DiagFail', 'DiagHagConnect', 'DiagHagDisconnect', 'DiagLogTransfer', 'DiagPnuOSIdent', 'DiagPowerOn', 'DiagPowerOnWait', 'DiagPreSanitize', 'DiagPreconfigVmediaLocal', 'DiagPreconfigVmediaPeer', 'DiagRunTests', 'DiagSanitize', 'DiagSerialDebugConnect', 'DiagSerialDebugDisconnect', 'DiagSetupBootEnvironment', 'DiagSetupVmediaLocal', 'DiagSetupVmediaPeer', 'DiagShutdown', 'DiagSuccess', 'DiagTearDownBootEnvironment', 'DiagTeardownVmediaLocal', 'DiagTeardownVmediaPeer', 'DiagWaitForDebug', 'DiagnosticInterruptBegin', 'DiagnosticInterruptExecute', 'DiagnosticInterruptFail', 'DiagnosticInterruptSuccess', 'DisassociateBegin', 'DisassociateBiosPostCompletion', 'DisassociateBmcConfigPnuOS', 'DisassociateBmcPreconfigPnuOSLocal', 'DisassociateBmcPreconfigPnuOSPeer', 'DisassociateBmcUnconfigPnuOS', 'DisassociateBootPnuos', 'DisassociateBootWait', 'DisassociateCheckPowerAvailability', 'DisassociateConfigBios', 'DisassociateConfigFlexFlashScrub', 'DisassociateConfigKvmMgmtDefaultSetting', 'DisassociateConfigUserAccess', 'DisassociateDeassertResetBypass', 'DisassociateFail', 'DisassociateHagPnuOSConnect', 'DisassociateHagPnuOSDisconnect', 'DisassociateHandlePooling', 'DisassociateNicConfigPnuOSLocal', 'DisassociateNicConfigPnuOSPeer', 'DisassociateNicUnconfigHostOSLocal', 'DisassociateNicUnconfigHostOSPeer', 'DisassociateNicUnconfigPnuOSLocal', 'DisassociateNicUnconfigPnuOSPeer', 'DisassociateNicUnconfigServiceInfraLocal', 'DisassociateNicUnconfigServiceInfraPeer', 'DisassociateOobDiskScrub', 'DisassociatePnuOSCatalog', 'DisassociatePnuOSIdent', 'DisassociatePnuOSPolicy', 'DisassociatePnuOSScrub', 'DisassociatePnuOSSelfTest', 'DisassociatePnuOSUnconfig', 'DisassociatePnuOSValidate', 'DisassociatePowerDeployWait', 'DisassociatePowerOn', 'DisassociatePreSanitize', 'DisassociateResetSecureBootConfig', 'DisassociateSanitize', 'DisassociateSerialDebugPnuOSConnect', 'DisassociateSerialDebugPnuOSDisconnect', 'DisassociateShutdown', 'DisassociateSolRedirectDisable', 'DisassociateSolRedirectEnable', 'DisassociateSuccess', 'DisassociateSwConfigPnuOSLocal', 'DisassociateSwConfigPnuOSPeer', 'DisassociateSwConfigPortNivLocal', 'DisassociateSwConfigPortNivPeer', 'DisassociateSwUnconfigHostOSLocal', 'DisassociateSwUnconfigHostOSPeer', 'DisassociateSwUnconfigPnuOSLocal', 'DisassociateSwUnconfigPnuOSPeer', 'DisassociateUnconfigBios', 'DisassociateUnconfigCimcVMedia', 'DisassociateUnconfigExtMgmtGw', 'DisassociateUnconfigExtMgmtRules', 'DisassociateUnconfigFlexFlash', 'DisassociateUnconfigServerIdentity', 'DisassociateUnconfigSoL', 'DisassociateUnconfigUuid', 'DisassociateVerifyFcZoneConfig', 'DiscoverBegin', 'DiscoverBiosPostCompletion', 'DiscoverBladeBootPnuos', 'DiscoverBladeBootWait', 'DiscoverBladePowerOn', 'DiscoverBladeReadSmbios', 'DiscoverBmcConfigPnuOS', 'DiscoverBmcFactoryReset', 'DiscoverBmcInventory', 'DiscoverBmcPreConfigPnuOSLocal', 'DiscoverBmcPreConfigPnuOSPeer', 'DiscoverBmcPresence', 'DiscoverBmcShutdownDiscovered', 'DiscoverCheckAdaptorFw40GCap', 'DiscoverCheckPowerAvailability', 'DiscoverConfigBMCPowerParams', 'DiscoverConfigFeLocal', 'DiscoverConfigFePeer', 'DiscoverConfigFlexFlashScrub', 'DiscoverConfigUserAccess', 'DiscoverFail', 'DiscoverHagConnect', 'DiscoverHagDisconnect', 'DiscoverHandlePooling', 'DiscoverNicConfigPnuOSLocal', 'DiscoverNicConfigPnuOSPeer', 'DiscoverNicPresenceLocal', 'DiscoverNicPresencePeer', 'DiscoverNicUnconfigPnuOSLocal', 'DiscoverNicUnconfigPnuOSPeer', 'DiscoverOobStorageInventory', 'DiscoverPnuOSCatalog', 'DiscoverPnuOSIdent', 'DiscoverPnuOSInventory', 'DiscoverPnuOSPolicy', 'DiscoverPnuOSPowerProfiling', 'DiscoverPnuOSScrub', 'DiscoverPnuOSSelfTest', 'DiscoverPostScrubOobStorageInventory', 'DiscoverPowerDeployWait', 'DiscoverPreSanitize', 'DiscoverSanitize', 'DiscoverSendBmcProfilingDone', 'DiscoverSendBmcProfilingInit', 'DiscoverSerialDebugConnect', 'DiscoverSerialDebugDisconnect', 'DiscoverSetupVmediaLocal', 'DiscoverSetupVmediaPeer', 'DiscoverSharedComponentsOobInventory', 'DiscoverSharedComponentsOobInventoryPeer', 'DiscoverSolRedirectDisable', 'DiscoverSolRedirectEnable', 'DiscoverSuccess', 'DiscoverSwConfigPnuOSLocal', 'DiscoverSwConfigPnuOSPeer', 'DiscoverSwUnconfigPnuOSLocal', 'DiscoverSwUnconfigPnuOSPeer', 'DiscoverTeardownVmediaLocal', 'DiscoverTeardownVmediaPeer', 'DiscoverUnconfigCimcVMedia', 'DiscoverUnconfigExtMgmtGw', 'DiscoverUnconfigExtMgmtRules', 'DiskZoningInventoryBegin', 'DiskZoningInventoryBootHost', 'DiskZoningInventoryBootWait', 'DiskZoningInventoryFail', 'DiskZoningInventoryPreSanitize', 'DiskZoningInventorySanitize', 'DiskZoningInventoryShutdown', 'DiskZoningInventoryStorageInventory', 'DiskZoningInventorySuccess', 'EnableCimcSecureBootActivate', 'EnableCimcSecureBootBegin', 'EnableCimcSecureBootFail', 'EnableCimcSecureBootPollUpdateStatus', 'EnableCimcSecureBootReset', 'EnableCimcSecureBootSuccess', 'EnableCimcSecureBootUpdateRequest', 'ExecuteActionsBegin', 'ExecuteActionsBiosPostCompletion', 'ExecuteActionsExecutePMAction', 'ExecuteActionsFail', 'ExecuteActionsPowerOn', 'ExecuteActionsSoftShutdown', 'ExecuteActionsSuccess', 'FlashControllerBegin', 'FlashControllerFail', 'FlashControllerSuccess', 'FlashControllerUpdateFlashLife', 'FwUpgradeActivateAdaptorNwFwLocal', 'FwUpgradeActivateAdaptorNwFwPeer', 'FwUpgradeActivateBios', 'FwUpgradeActivateIBMCFw', 'FwUpgradeAssertBypassWait', 'FwUpgradeBegin', 'FwUpgradeBiosImgUpdate', 'FwUpgradeBiosPostCompletion', 'FwUpgradeBladePowerOff', 'FwUpgradeBmcConfigPnuOS', 'FwUpgradeBmcPreconfigPnuOSLocal', 'FwUpgradeBmcPreconfigPnuOSPeer', 'FwUpgradeBmcUnconfigPnuOS', 'FwUpgradeBootPnuos', 'FwUpgradeBootWait', 'FwUpgradeCheckPowerAvailability', 'FwUpgradeCiscoOSOpenGate', 'FwUpgradeClearBiosUpdate', 'FwUpgradeCopyRemote', 'FwUpgradeDeassertResetBypass', 'FwUpgradeDeleteCurlDownloadedImages', 'FwUpgradeDeleteImagesRemote', 'FwUpgradeDownloadImages', 'FwUpgradeFail', 'FwUpgradeGraphicsImageUpdate', 'FwUpgradeHagPnuOSConnect', 'FwUpgradeHagPnuOSDisconnect', 'FwUpgradeHbaImgUpdate', 'FwUpgradeLocalDiskFwUpdate', 'FwUpgradeMswitchImgUpdate', 'FwUpgradeNicConfigPnuOSLocal', 'FwUpgradeNicConfigPnuOSPeer', 'FwUpgradeNicImgUpdate', 'FwUpgradeNicUnconfigPnuOSLocal', 'FwUpgradeNicUnconfigPnuOSPeer', 'FwUpgradeOobPollSasExpanderActivateStatus', 'FwUpgradeOobPollSasExpanderBootImgActivateStatus', 'FwUpgradeOobPollSasExpanderUpdateStatus', 'FwUpgradeOobSasExpanderBootImgActivate', 'FwUpgradeOobSasExpanderImgActivate', 'FwUpgradeOobSasExpanderImgUpdate', 'FwUpgradeOobStorageInventory', 'FwUpgradePciSwitchImageUpdate', 'FwUpgradePersistentMemoryDimmFwUpdate', 'FwUpgradePnuOSCatalog', 'FwUpgradePnuOSConfig', 'FwUpgradePnuOSIdent', 'FwUpgradePnuOSInventory', 'FwUpgradePnuOSPolicy', 'FwUpgradePnuOSSelfTest', 'FwUpgradePnuOSUnloadDrivers', 'FwUpgradePnuOSValidate', 'FwUpgradePollBiosActivateStatus', 'FwUpgradePollBiosUpdateStatus', 'FwUpgradePollBoardCtrlPowerCycle', 'FwUpgradePollBoardCtrlUpdateStatus', 'FwUpgradePollClearBiosUpdateStatus', 'FwUpgradePowerCycleBoard', 'FwUpgradePowerDeployWait', 'FwUpgradePowerOn', 'FwUpgradePreSanitize', 'FwUpgradeResetIBMC', 'FwUpgradeSanitize', 'FwUpgradeSasExpanderImgUpdate', 'FwUpgradeSerialDebugPnuOSConnect', 'FwUpgradeSerialDebugPnuOSDisconnect', 'FwUpgradeShutdown', 'FwUpgradeSolRedirectDisable', 'FwUpgradeSolRedirectEnable', 'FwUpgradeStorageCtlrImgUpdate', 'FwUpgradeSuccess', 'FwUpgradeSwConfigPnuOSLocal', 'FwUpgradeSwConfigPnuOSPeer', 'FwUpgradeSwConfigPortNivLocal', 'FwUpgradeSwConfigPortNivPeer', 'FwUpgradeSwUnconfigPnuOSLocal', 'FwUpgradeSwUnconfigPnuOSPeer', 'FwUpgradeUnconfigCimcVMedia', 'FwUpgradeUnconfigExtMgmtGw', 'FwUpgradeUnconfigExtMgmtRules', 'FwUpgradeUnlockFirmwareImage', 'FwUpgradeUpdateAdaptorNwFwLocal', 'FwUpgradeUpdateAdaptorNwFwPeer', 'FwUpgradeUpdateBiosRequest', 'FwUpgradeUpdateBoardCtrlRequest', 'FwUpgradeUpdateIBMCFw', 'FwUpgradeWaitForAdaptorNwFwUpdateLocal', 'FwUpgradeWaitForAdaptorNwFwUpdatePeer', 'FwUpgradeWaitForIBMCFwUpdate', 'HardShutdownBegin', 'HardShutdownExecute', 'HardShutdownFail', 'HardShutdownSuccess', 'HardresetBegin', 'HardresetCheckPowerAvailability', 'HardresetExecute', 'HardresetFail', 'HardresetPowerDeployWait', 'HardresetPreSanitize', 'HardresetSanitize', 'HardresetSuccess', 'NvmeSwitchRecoveryBegin', 'NvmeSwitchRecoveryCheckStatus', 'NvmeSwitchRecoveryExecute', 'NvmeSwitchRecoveryFail', 'NvmeSwitchRecoverySuccess', 'NvmeSwitchRecoveryWaitForAck', 'OobStorageAdminConfigBegin', 'OobStorageAdminConfigBootHost', 'OobStorageAdminConfigBootWait', 'OobStorageAdminConfigCheckPowerAvailability', 'OobStorageAdminConfigFail', 'OobStorageAdminConfigOobStorageConfig', 'OobStorageAdminConfigOobStorageInventory', 'OobStorageAdminConfigPowerDeployWait', 'OobStorageAdminConfigPreSanitize', 'OobStorageAdminConfigSanitize', 'OobStorageAdminConfigShutdown', 'OobStorageAdminConfigSuccess', 'OobStorageAdminConfigTearDownVMediaLocal', 'OobStorageAdminConfigTearDownVMediaPeer', 'PowerCapBegin', 'PowerCapConfig', 'PowerCapFail', 'PowerCapSuccess', 'PowercycleBegin', 'PowercycleCheckPowerAvailability', 'PowercycleExecute', 'PowercycleFail', 'PowercyclePowerDeployWait', 'PowercyclePreSanitize', 'PowercycleSanitize', 'PowercycleSuccess', 'ReinitializeVirtualDriveBegin', 'ReinitializeVirtualDriveExecuteVDAction', 'ReinitializeVirtualDriveFail', 'ReinitializeVirtualDriveSuccess', 'ResetBmcBegin', 'ResetBmcExecute', 'ResetBmcFail', 'ResetBmcSuccess', 'ResetIpmiBegin', 'ResetIpmiExecute', 'ResetIpmiFail', 'ResetIpmiSuccess', 'ResetKvmBegin', 'ResetKvmExecute', 'ResetKvmFail', 'ResetKvmSuccess', 'ResetMemoryErrorsBegin', 'ResetMemoryErrorsExecute', 'ResetMemoryErrorsFail', 'ResetMemoryErrorsSuccess', 'ServiceInfraDeployBegin', 'ServiceInfraDeployFail', 'ServiceInfraDeployNicConfigLocal', 'ServiceInfraDeployNicConfigPeer', 'ServiceInfraDeploySuccess', 'ServiceInfraDeploySwConfigLocal', 'ServiceInfraDeploySwConfigPeer', 'ServiceInfraWithdrawBegin', 'ServiceInfraWithdrawFail', 'ServiceInfraWithdrawNicUnConfigLocal', 'ServiceInfraWithdrawNicUnConfigPeer', 'ServiceInfraWithdrawSuccess', 'ServiceInfraWithdrawSwUnConfigLocal', 'ServiceInfraWithdrawSwUnConfigPeer', 'SoftShutdownBegin', 'SoftShutdownExecute', 'SoftShutdownFail', 'SoftShutdownSuccess', 'SoftresetBegin', 'SoftresetCheckPowerAvailability', 'SoftresetExecute', 'SoftresetFail', 'SoftresetPowerDeployWait', 'SoftresetPreSanitize', 'SoftresetSanitize', 'SoftresetSuccess', 'SwConnUpdA', 'SwConnUpdB', 'SwConnUpdBegin', 'SwConnUpdFail', 'SwConnUpdSuccess', 'TurnupBegin', 'TurnupCheckPowerAvailability', 'TurnupExecute', 'TurnupFail', 'TurnupPowerDeployWait', 'TurnupSuccess', 'UnconfigSoLBegin', 'UnconfigSoLExecute', 'UnconfigSoLFail', 'UnconfigSoLSuccess', 'UpdateAdaptorBegin', 'UpdateAdaptorCheckPowerAvailability', 'UpdateAdaptorFail', 'UpdateAdaptorPollUpdateStatusLocal', 'UpdateAdaptorPollUpdateStatusPeer', 'UpdateAdaptorPowerDeployWait', 'UpdateAdaptorPowerOff', 'UpdateAdaptorPowerOn', 'UpdateAdaptorSuccess', 'UpdateAdaptorUpdateRequestLocal', 'UpdateAdaptorUpdateRequestPeer', 'UpdateBIOSBegin', 'UpdateBIOSClear', 'UpdateBIOSFail', 'UpdateBIOSPollClearStatus', 'UpdateBIOSPollUpdateStatus', 'UpdateBIOSSuccess', 'UpdateBIOSUpdateRequest', 'UpdateBoardControllerBegin', 'UpdateBoardControllerCheckPowerAvailability', 'UpdateBoardControllerFail', 'UpdateBoardControllerPollBoardCtrlPowerCycle', 'UpdateBoardControllerPollUpdateStatus', 'UpdateBoardControllerPowerCycleBoard', 'UpdateBoardControllerPowerDeployWait', 'UpdateBoardControllerPrepareForUpdate', 'UpdateBoardControllerServerPowerOff', 'UpdateBoardControllerServerPowerOn', 'UpdateBoardControllerSuccess', 'UpdateBoardControllerUpdateRequest', 'clearTPMBegin', 'clearTPMBiosPostCompletion', 'clearTPMBladePowerOff', 'clearTPMBladePowerOn', 'clearTPMBootHost', 'clearTPMClear', 'clearTPMFail', 'clearTPMPreSanitize', 'clearTPMReadSmBios', 'clearTPMReconfigBios', 'clearTPMSanitize', 'clearTPMSetupVmedia', 'clearTPMStopVMediaLocal', 'clearTPMStopVMediaPeer', 'clearTPMSuccess', 'clearTPMUnconfigVmedia', 'nop', 'updateExtUsersBegin', 'updateExtUsersDeploy', 'updateExtUsersFail', 'updateExtUsersSuccess']
range_val                       :[]

Property                        fsm_try
--------                        -------
xml_attribute                   :fsmTry
field_type                      :byte
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        int_id
--------                        ------
xml_attribute                   :intId
field_type                      :string
min_version                     :1.0(1e)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['none']
range_val                       :['0-4294967295']

Property                        kmip_fault
--------                        ----------
xml_attribute                   :kmipFault
field_type                      :string
min_version                     :3.2(1d)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['false', 'no', 'true', 'yes']
range_val                       :[]

Property                        kmip_fault_description
--------                        ----------------------
xml_attribute                   :kmipFaultDescription
field_type                      :string
min_version                     :3.2(1d)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        lc
--------                        --
xml_attribute                   :lc
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['decommission', 'discovered', 'migrate', 'rediscover', 'remove', 'resetToFactory', 'undiscovered', 'upgrade-firmware']
range_val                       :[]

Property                        lc_ts
--------                        -----
xml_attribute                   :lcTs
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}
value_set                       :[]
range_val                       :[]

Property                        local_id
--------                        --------
xml_attribute                   :localId
field_type                      :string
min_version                     :2.1(2a)
access                          :READ_ONLY
min_length                      :0
max_length                      :256
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        low_voltage_memory
--------                        ------------------
xml_attribute                   :lowVoltageMemory
field_type                      :string
min_version                     :1.4(1i)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['low-voltage', 'not-applicable', 'regular-voltage']
range_val                       :[]

Property                        managing_inst
--------                        -------------
xml_attribute                   :managingInst
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['A', 'B', 'NONE']
range_val                       :[]

Property                        memory_speed
--------                        ------------
xml_attribute                   :memorySpeed
field_type                      :string
min_version                     :1.4(1i)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['not-applicable', 'unspecified']
range_val                       :['0-65535']

Property                        mfg_time
--------                        --------
xml_attribute                   :mfgTime
field_type                      :string
min_version                     :2.0(1m)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}
value_set                       :['not-applicable']
range_val                       :[]

Property                        model
--------                        -----
xml_attribute                   :model
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        name
--------                        ----
xml_attribute                   :name
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :[\-\.:_a-zA-Z0-9]{0,16}
value_set                       :[]
range_val                       :[]

Property                        num_of40_g_adaptors_with_old_fw
--------                        -------------------------------
xml_attribute                   :numOf40GAdaptorsWithOldFw
field_type                      :byte
min_version                     :3.1(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of40_g_adaptors_with_unknown_fw
--------                        -----------------------------------
xml_attribute                   :numOf40GAdaptorsWithUnknownFw
field_type                      :byte
min_version                     :3.1(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_adaptors
--------                        ---------------
xml_attribute                   :numOfAdaptors
field_type                      :byte
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_cores
--------                        ------------
xml_attribute                   :numOfCores
field_type                      :ushort
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_cores_enabled
--------                        --------------------
xml_attribute                   :numOfCoresEnabled
field_type                      :ushort
min_version                     :1.3(1c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_cpus
--------                        -----------
xml_attribute                   :numOfCpus
field_type                      :byte
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_eth_host_ifs
--------                        -------------------
xml_attribute                   :numOfEthHostIfs
field_type                      :ushort
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_fc_host_ifs
--------                        ------------------
xml_attribute                   :numOfFcHostIfs
field_type                      :ushort
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        num_of_threads
--------                        --------------
xml_attribute                   :numOfThreads
field_type                      :ushort
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        oper_power
--------                        ----------
xml_attribute                   :operPower
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['degraded', 'error', 'failed', 'not-supported', 'off', 'offduty', 'offline', 'ok', 'on', 'online', 'power-save', 'test', 'unknown']
range_val                       :[]

Property                        oper_pwr_trans_src
--------                        ------------------
xml_attribute                   :operPwrTransSrc
field_type                      :string
min_version                     :3.0(2c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['software', 'software_mcserver', 'unknown', 'user-fp', 'user-unknown']
range_val                       :[]

Property                        oper_qualifier
--------                        --------------
xml_attribute                   :operQualifier
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :((defaultValue|not-applicable|cpu-voltage|adaptor-voltage|hba-voltage|compute-post-failure|memory-power|nic-power|memory-inoperable|nic-inoperable|compute-power|power-inoperable|compute-thermal|cpu-perf|adaptor-perf|hba-perf|cpu-thermal|adaptor-thermal|hba-thermal|compute-inoperable|memory-voltage|removed|nic-voltage|network-misconfig|cpu-power|adaptor-power|hba-power|compute-voltage|cpu-inoperable|adaptor-inoperable|hba-inoperable|config|memory-perf|nic-perf|adaptor-mismatch|memory-thermal|nic-thermal|mismatch|compute-perf),){0,38}(defaultValue|not-applicable|cpu-voltage|adaptor-voltage|hba-voltage|compute-post-failure|memory-power|nic-power|memory-inoperable|nic-inoperable|compute-power|power-inoperable|compute-thermal|cpu-perf|adaptor-perf|hba-perf|cpu-thermal|adaptor-thermal|hba-thermal|compute-inoperable|memory-voltage|removed|nic-voltage|network-misconfig|cpu-power|adaptor-power|hba-power|compute-voltage|cpu-inoperable|adaptor-inoperable|hba-inoperable|config|memory-perf|nic-perf|adaptor-mismatch|memory-thermal|nic-thermal|mismatch|compute-perf){0,1}
value_set                       :[]
range_val                       :[]

Property                        oper_qualifier_reason
--------                        ---------------------
xml_attribute                   :operQualifierReason
field_type                      :string
min_version                     :3.2(3a)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}
value_set                       :[]
range_val                       :[]

Property                        oper_state
--------                        ----------
xml_attribute                   :operState
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['bios-password-reset', 'bios-restore', 'cmos-reset', 'compute-failed', 'compute-mismatch', 'config', 'config-failure', 'decomissioning', 'degraded', 'diagnostics', 'diagnostics-failed', 'disabled', 'discovery', 'discovery-failed', 'inaccessible', 'indeterminate', 'inoperable', 'maintenance', 'maintenance-failed', 'ok', 'pending-reassociation', 'pending-reboot', 'power-off', 'power-problem', 'removed', 'restart', 'svnic-not-present', 'test', 'test-failed', 'thermal-problem', 'unassociated', 'unconfig', 'unconfig-failed', 'voltage-problem']
range_val                       :[]

Property                        operability
--------                        -----------
xml_attribute                   :operability
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['accessibility-problem', 'auto-upgrade', 'backplane-port-problem', 'bios-post-timeout', 'chassis-intrusion', 'chassis-limit-exceeded', 'config', 'decomissioning', 'degraded', 'dimm-disabled', 'disabled', 'discovery', 'discovery-failed', 'equipment-problem', 'fabric-conn-problem', 'fabric-unsupported-conn', 'identify', 'identity-unestablishable', 'inoperable', 'link-activate-blocked', 'malformed-fru', 'non-optimal', 'non-optimal-severe', 'not-supported', 'operable', 'peer-comm-problem', 'peer-dimm-disabled', 'performance-problem', 'post-failure', 'power-problem', 'powered-off', 'removed', 'thermal-problem', 'unknown', 'unsupported-config', 'upgrade-problem', 'voltage-problem']
range_val                       :[]

Property                        original_uuid
--------                        -------------
xml_attribute                   :originalUuid
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0
value_set                       :[]
range_val                       :[]

Property                        part_number
--------                        -----------
xml_attribute                   :partNumber
field_type                      :string
min_version                     :2.0(3a)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        policy_level
--------                        ------------
xml_attribute                   :policyLevel
field_type                      :uint
min_version                     :2.1(1a)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        policy_owner
--------                        ------------
xml_attribute                   :policyOwner
field_type                      :string
min_version                     :2.1(1a)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['local', 'pending-policy', 'policy']
range_val                       :[]

Property                        presence
--------                        --------
xml_attribute                   :presence
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['empty', 'equipped', 'equipped-deprecated', 'equipped-identity-unestablishable', 'equipped-not-primary', 'equipped-slave', 'equipped-unsupported', 'equipped-with-malformed-fru', 'inaccessible', 'mismatch', 'mismatch-identity-unestablishable', 'mismatch-slave', 'missing', 'missing-slave', 'unauthorized', 'unknown']
range_val                       :[]

Property                        revision
--------                        --------
xml_attribute                   :revision
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        rn
--------                        --
xml_attribute                   :rn
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :256
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        sacl
--------                        ----
xml_attribute                   :sacl
field_type                      :string
min_version                     :3.0(2c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}
value_set                       :[]
range_val                       :[]

Property                        scaled_mode
--------                        -----------
xml_attribute                   :scaledMode
field_type                      :string
min_version                     :2.2(2c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['none', 'scaled', 'single']
range_val                       :[]

Property                        serial
--------                        ------
xml_attribute                   :serial
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        server_id
--------                        ---------
xml_attribute                   :serverId
field_type                      :string
min_version                     :1.4(1i)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        slot_id
--------                        -------
xml_attribute                   :slotId
field_type                      :uint
min_version                     :1.0(1e)
access                          :NAMING
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :['1-8']

Property                        status
--------                        ------
xml_attribute                   :status
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}
value_set                       :[]
range_val                       :[]

Property                        storage_oper_qualifier
--------                        ----------------------
xml_attribute                   :storageOperQualifier
field_type                      :string
min_version                     :3.2(3a)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['accessibility-problem', 'auto-upgrade', 'backplane-port-problem', 'bios-post-timeout', 'chassis-intrusion', 'chassis-limit-exceeded', 'config', 'decomissioning', 'degraded', 'dimm-disabled', 'disabled', 'discovery', 'discovery-failed', 'equipment-problem', 'fabric-conn-problem', 'fabric-unsupported-conn', 'identify', 'identity-unestablishable', 'inoperable', 'link-activate-blocked', 'malformed-fru', 'non-optimal', 'non-optimal-severe', 'not-supported', 'operable', 'peer-comm-problem', 'peer-dimm-disabled', 'performance-problem', 'post-failure', 'power-problem', 'powered-off', 'removed', 'thermal-problem', 'unknown', 'unsupported-config', 'upgrade-problem', 'voltage-problem']
range_val                       :[]

Property                        total_memory
--------                        ------------
xml_attribute                   :totalMemory
field_type                      :uint
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        usr_lbl
--------                        -------
xml_attribute                   :usrLbl
field_type                      :string
min_version                     :1.4(1i)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}
value_set                       :[]
range_val                       :[]

Property                        uuid
--------                        ----
xml_attribute                   :uuid
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0
value_set                       :[]
range_val                       :[]

Property                        vendor
--------                        ------
xml_attribute                   :vendor
field_type                      :string
min_version                     :1.0(1e)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        vid
--------                        ---
xml_attribute                   :vid
field_type                      :string
min_version                     :2.0(3a)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]
```