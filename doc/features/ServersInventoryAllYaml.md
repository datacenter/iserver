# Servers inventory in YAML format

Use YAML (-o yaml) output format.

```
# iserver get servers -o yaml

- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 5e8c4ecd6f72612d302b11a6
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.34
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5e8c4ed26176752d32d51c40
  Name: esx2-eu-spdc-FCH2004V1PV
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2004V1PV
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 5ecf82676f72612d30687409
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.60
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5ecf828a6176752d35b7eb9a
  Name: mgmt-p4a-eu-spdc-WZP22520Y9D
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y9D
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 1
    Info: 0
    Warning: 0
  AvailableMemory: 196608
  AvailableMemoryGB: 192
  AvailableMemoryUnit: 192 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 5ecf86d86f72612d3068b4bc
  FlagManagement: Cri
  FlagState: P- C(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.51
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 5ecf86f16176752d35b94401
  Name: comp1-p2a-eu-spdc-WZP22511E6V
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22511E6V
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: false
  Cpu: 2S 24C 48T
  DeviceMoId: 5ecf87bc6f72612d3068c346
  FlagManagement: cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.56
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 5ecf87c56176752d35b97fa4
  Name: znas-eu-spdc-WZP22511E3P
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22511E3P
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 5fa045b46f72612d3086c548
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.35
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fa045ce6176752d35c9d2f5
  Name: esx3-eu-spdc-FCH2004V0RW
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2004V0RW
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 36C 72T
  DeviceMoId: 5fa0489f6f72612d30878741
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.50
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fa048b06176752d35cae964
  Name: esx5-eu-spdc-FCH2017V024
  NumCpuCores: 36
  NumCpus: 2
  NumThreads: 72
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V024
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 5fa04a9e6f72612d30880e03
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.40
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fa04aa26176752d35cba3c9
  Name: mgmt-p1-eu-spdc-WZP2252176Z
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP2252176Z
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 44C 88T
  DeviceMoId: 5fa04b536f72612d30883fd0
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.41
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fa04baa6176752d35cc0518
  Name: aio-1-p1-eu-spdc-WZP22490ZCU
  NumCpuCores: 44
  NumCpus: 2
  NumThreads: 88
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22490ZCU
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 5fa04be16f72612d30886344
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.42
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fa04c3a6176752d35cc3569
  Name: aio-2-p1-eu-spdc-WZP22520Y69
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y69
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 44C 88T
  DeviceMoId: 5fa04cb86f72612d30889bc8
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.43
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fa04cc16176752d35cc60ce
  Name: aio-3-p1-eu-spdc-WZP22520Y54
  NumCpuCores: 44
  NumCpus: 2
  NumThreads: 88
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y54
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 5fa04dd16f72612d3088e6b1
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.44
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fa04e266176752d35cce224
  Name: comp1-p1-eu-spdc-WZP22520Y9J
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y9J
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 5fa04e6c6f72612d30890d70
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.45
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fa04e8e6176752d35cd0c4e
  Name: comp2-p1-spdc-WZP22520Y95
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y95
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: false
  Cpu: 2S 28C 56T
  DeviceMoId: 5fa051776f72612d3089d7e9
  FlagManagement: cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.47
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fa051816176752d35ce095c
  Name: comp4-p1-eu-spdc-FCH2016V23J
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2016V23J
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: false
  Cpu: 2S 28C 56T
  DeviceMoId: 5fa052926f72612d308a2325
  FlagManagement: cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.48
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fa052a26176752d35ce6572
  Name: comp5-p1-eu-spdc-FCH2017V0TN
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V0TN
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 5fa1a78b6f72612d30e49bd3
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.52
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 5fa1a79b6176752d35486b5c
  Name: tnas-eu-spdc-WZP22511E68
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22511E68
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdf9be76f72612d300a8d81
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: p2b,pod2b,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.41
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SN
  Moid: 5fdf9c016176752d35e44795
  Name: comp-1-p2b-eu-spdc-WZP23400AJW
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WZP23400AJW
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SN
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdf9c676f72612d300a9c8d
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: p2b,pod2b,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.42
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SN
  Moid: 5fdf9c786176752d35e47110
  Name: comp-2-p2b-eu-spdc-WZP23400AK4
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WZP23400AK4
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SN
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdf9cf26f72612d300aaca0
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: p2b,pod2b,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.43
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SN
  Moid: 5fdf9d026176752d35e4ac4e
  Name: comp-3-p2b-eu-spdc-WZP23400AKL
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WZP23400AKL
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SN
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdfa1686f72612d300b383f
  FlagManagement: CRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p2b,pod2b,test,self-test-power,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.44
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fdfa1806176752d35e678c2
  Name: comp-4-p2b-eu-spdc-WMP240400FM
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP240400FM
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdfdc206f72612d30120ab4
  FlagManagement: CRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p2b,pod2b,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.45
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fdfdc3b6176752d35fce0a9
  Name: comp-5-p2b-eu-spdc-WMP2404000R
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP2404000R
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdfe4666f72612d30130510
  FlagManagement: CRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p2b,pod2b,test,self-test-power,self-test-locator,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.46
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fdfe47f6176752d35001995
  Name: comp-6-p2b-eu-spdc-WMP24040059
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP24040059
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdfe7d86f72612d30136fed
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: p2b,pod2b,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.47
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fdfe80d6176752d3502b008
  Name: comp-7-p2b-eu-spdc-WMP24040061
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP24040061
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 5fe295916f72612d306438ac
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.57
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fe295aa6176752d35119a62
  Name: esx6-eu-spdc-FCH2006V04E
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2006V04E
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 1
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 5fe32eb66f72612d3075c96a
  FlagManagement: Cri
  FlagState: P+ C(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.58
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fe32f176176752d354c125a
  Name: esx7-eu-spdc-FCH2004V0M6
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2004V0M6
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 5fe32f4d6f72612d3075db4b
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.59
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 5fe32f536176752d354c2ade
  Name: esx8-eu-spdc-FCH2017V0T1
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V0T1
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 6026a9096f72612d305e7b8b
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.55
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SN
  Moid: 6026a92e6176752d350ac89a
  Name: POD-4A-AIO-1-WZP23400AK9
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23400AK9
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SN
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 6026a9976f72612d305e8e4c
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.56
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SN
  Moid: 6026a9ba6176752d350b0bc2
  Name: POD-4A-AIO-2-WZP23400AK7
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23400AK7
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SN
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 6026aa376f72612d305ea314
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.57
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SN
  Moid: 6026aa596176752d350b5bd5
  Name: POD-4A-AIO-3-WZP23400AM2
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23400AM2
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SN
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 6026aade6f72612d305eb7fd
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.54
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026ab006176752d350bb5b4
  Name: comp1-p4A-eu-spdc
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WMP24040045
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6026ab6f6f72612d305ec984
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.58
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026ab926176752d350bfa1f
  Name: comp2-p4a-eu-spdc-WZP22520B04
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520B04
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 1
    Info: 0
    Warning: 0
  AvailableMemory: 196608
  AvailableMemoryGB: 192
  AvailableMemoryUnit: 192 [GiB]
  Connected: false
  Cpu: 2S 16C 32T
  DeviceMoId: 6026ae116f72612d305f1e80
  FlagManagement: cri
  FlagState: P- C(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.53
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026ae316176752d350d1cf6
  Name: comp3-p2a-eu-spdc-WZP2335149W
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP2335149W
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 196608
  AvailableMemoryGB: 192
  AvailableMemoryUnit: 192 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 6026aefd6f72612d305f3c94
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.54
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026af226176752d350d8b38
  Name: comp4-p2a-eu-spdc-WZP22520Y8W
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y8W
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 6026afe76f72612d305f5af6
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.37
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026b0086176752d350dec89
  Name: esx01-eu-spdc-WZP22520Y99
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y99
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6026b0a16f72612d305f7116
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.36
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026b0c56176752d350e3741
  Name: esx00-eu-spdc-WZP22520AXQ
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520AXQ
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 6026b2376f72612d305fa447
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.59
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026b2946176752d350ef654
  Name: comp3-p4a-eu-spdc-WZP22520Y8X
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22520Y8X
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: false
  Cpu: 2S 48C 96T
  DeviceMoId: 6026b5846f72612d30b98bb0
  FlagManagement: cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.41
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 6026b5ab6176752d35104d78
  Name: aio1-p5g-eu-spdc-WZP23450C7D
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23450C7D
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: false
  Cpu: 2S 48C 96T
  DeviceMoId: 6026b6346f72612d30b997b6
  FlagManagement: cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.42
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 6026b65f6176752d35109d55
  Name: aio2-p5g-eu-spdc-WZP23450C8M
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23450C8M
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6026b8a26f72612d30b9b627
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.51
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 6026b9a26176752d3537f191
  Name: aio3-p5g-eu-spdc-WZP23450C8K
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WZP23450C8K
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6026b9416f72612d30b9be8a
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.49
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026bb9c6176752d353915f2
  Name: cu-p5g-eu-spdc-WZP23440N11
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23440N11
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: false
  Cpu: 2S 48C 96T
  DeviceMoId: 6026bbb86f72612d30b9e10d
  FlagManagement: cri
  FlagState: P+ H L
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: true
  ManagementIp: 10.58.29.50
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026bc4e6176752d3539ad8b
  Name: core-p5g-eu-spdc-WZP23440N02
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23440N02
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G..
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6026c0336f72612d30ba2932
  FlagManagement: CRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.39
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6026c0526176752d353b8b29
  Name: esx22-eu-spdc-WZP2343171Y
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WZP2343171Y
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 6061d69a6f72612d30c09961
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.244.70
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6061d6c06176752d357360aa
  Name: ' C220-WZP23360FH9'
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23360FH9
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 606323916f72612d30e34f36
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.244.186
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 606323a46176752d350804cb
  Name: ' C220-WZP23350ZAQ'
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23350ZAQ
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 56C 112T
  DeviceMoId: 60632bb46f72612d30e4222e
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.244.236
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 60632bda6176752d350b9fc0
  Name: C240-WZP232102PH
  NumCpuCores: 56
  NumCpus: 2
  NumThreads: 112
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP232102PH
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 1
    Info: 0
    Warning: 0
  AvailableMemory: 327680
  AvailableMemoryGB: 320
  AvailableMemoryUnit: 320 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 60632d896f72612d30e45356
  FlagManagement: Cri
  FlagState: P+ C(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.250.241
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 60632dcf6176752d350c72bc
  Name: C220-231
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23240NNZ
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 65536
  UsedMemoryGB: 64
  UsedMemoryPct: 16
  UsedMemoryPctUnit: 16%
  UsedMemoryUnit: 64 [GiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 6098fe506f72612d30e78ffb
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.33
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 6098fe686176752d35a6dbc8
  Name: esx91-eu-spdc-WZP234411LW
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP234411LW
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 196608
  AvailableMemoryGB: 192
  AvailableMemoryUnit: 192 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 5ecf87256f72612d3068b971
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.52
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 61260a8076752d3131235d3a
  Name: comp2-p2a-eu-spdc-WZP22511E6G
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP22511E6G
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 61320ad96f72612d300340e7
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: pod2b
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.40
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 61324fa676752d3131fd5d08
  Name: esx20-eu-spdc-WMP24040053
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP24040053
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 48C 48T
  DeviceMoId: 6139bd1a6f72612d30db6982
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.48
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M5SX
  Moid: 6139bd4e76752d3137136802
  Name: du-p5g-eu-spdc-WZP2526088F
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP2526088F
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 6141c1e76f72612d30d2b35f
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.37
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 6141c1f676752d313775876f
  Name: esx95-eu-spdc-FCH2017V241
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V241
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 6141c3186f72612d30d2d8f8
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.35
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 6141c32376752d313775f536
  Name: esx93-eu-spdc-FCH2108V1HE
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2108V1HE
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 1
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 6141c37c6f72612d30d2e54d
  FlagManagement: Cri
  FlagState: P+ W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.34
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 6141c3ad76752d31377629ad
  Name: esx92-eu-spdc-FCH2017V2AF
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V2AF
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 2
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 6141c3976f72612d30d2e7d0
  FlagManagement: Cri
  FlagState: P- W(2)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (2)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.25.36
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 6141c3b676752d3137762cf2
  Name: esx94-eu-spdc-FCH2017V2AH
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V2AH
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 6169b3926f72612d30589b53
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.60
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 6169b3bd76752d313972fba0
  Name: esx9-eu-spdc-FCH2016V23J
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2016V23J
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 6169b7086f72612d3058fe9b
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.61
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 6169b76576752d313973e815
  Name: esx10-eu-spdc-FCH2017V0TN
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V0TN
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 616ea3296f72612d30e81fe9
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.51
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 616ea34876752d3139b2261f
  Name: esx11-eu-spdc-FCH2050V125
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2050V125
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 1
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P+ W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.198
  ManagementMode: UCSM
  Model: UCSC-C240-M4S
  Moid: 61c35fad76752d3139f50e2d
  Name: berlin-ucsm-2
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH1930V0PH
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4S
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 1
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P+ W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.195
  ManagementMode: UCSM
  Model: UCSC-C240-M4S
  Moid: 61c35fad76752d3139f50e3e
  Name: berlin-ucsm-6
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH1930V0KM
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4S
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 720896
  AvailableMemoryGB: 704
  AvailableMemoryUnit: 704 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.199
  ManagementMode: UCSM
  Model: UCSC-C240-M5SX
  Moid: 61c35fad76752d3139f50e50
  Name: berlin-ucsm-1
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WZP21490417
  TotalMemory: 720896
  TotalMemoryGB: 704
  TotalMemoryUnit: 704 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M5SX
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 1
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P- W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.197
  ManagementMode: UCSM
  Model: UCSC-C240-M4SX
  Moid: 61c35fad76752d3139f50e78
  Name: berlin-ucsm-4
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH1916V1CT
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4SX
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.YYYY
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 2
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P+ W(2)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (2)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.206
  ManagementMode: UCSM
  Model: UCSC-C240-M4SX
  Moid: 61c35fad76752d3139f50e88
  Name: berlin-ucsm-5
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH1916V0UY
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4SX
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 1
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P+ W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.194
  ManagementMode: UCSM
  Model: UCSC-C220-M4S
  Moid: 61c35fad76752d3139f50eae
  Name: berlin-ucsm-8
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH1849V26H
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 1
  AvailableMemory: 786432
  AvailableMemoryGB: 768
  AvailableMemoryUnit: 768 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P- W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.205
  ManagementMode: UCSM
  Model: UCSC-C240-M4S
  Moid: 61c35fad76752d3139f50efa
  Name: berlin-ucsm-7
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH1930V1LA
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4S
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 20C 40T
  DeviceMoId: 61df0d3c6f72612d307e5a50
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.34
  ManagementMode: IntersightStandalone
  Model: SE-NODE-G2
  Moid: 61df0d5676752d3139507e9e
  Name: sn12-eu-spdc-WZP23430C4D
  NumCpuCores: 20
  NumCpus: 2
  NumThreads: 40
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23430C4D
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) SE-NODE-G2
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 1
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 20C 40T
  DeviceMoId: 61df0df76f72612d307e6ad3
  FlagManagement: Cri
  FlagState: P+ C(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.35
  ManagementMode: IntersightStandalone
  Model: SE-NODE-G2
  Moid: 61df0e1476752d313950b310
  Name: sn13-eu-spdc-WZP234301R9
  NumCpuCores: 20
  NumCpus: 2
  NumThreads: 40
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP234301R9
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) SE-NODE-G2
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 20C 40T
  DeviceMoId: 61df11db6f72612d307ebf0f
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.33
  ManagementMode: IntersightStandalone
  Model: SE-NODE-G2
  Moid: 61df120b76752d3139518492
  Name: sn11-eu-spdc-WZP23430C4N
  NumCpuCores: 20
  NumCpus: 2
  NumThreads: 40
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP23430C4N
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) SE-NODE-G2
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 131072
  AvailableMemoryGB: 128
  AvailableMemoryUnit: 128 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 61e998396f72612d305682d9
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p3b
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.49
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M4SX
  Moid: 61e9985676752d3139e59f59
  Name: comp2-p3b-eu-spdc-FCH2017V1J8
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V1J8
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 0
  AvailableMemory: 131072
  AvailableMemoryGB: 128
  AvailableMemoryUnit: 128 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 61e99b2d6f72612d3056bb7d
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p3b
  Health: Healthy (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.50
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M4SX
  Moid: 61e99b6176752d3139e62d14
  Name: comp3-p3b-eu-spdc-FCH2017V1J5
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V1J5
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 61e99f9c6f72612d3057152d
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p3b
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.57
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 61e99fb976752d3139e71340
  Name: comp4-p3b-eu-spdc-FCH2108V1FC
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2108V1FC
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 61e9a19a6f72612d30573d28
  FlagManagement: Cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p3b
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.58
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 61e9a1ba76752d3139e778f3
  Name: comp5-p3b-eu-spdc-FCH2017V1Y6
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V1Y6
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 61e9a40d6f72612d30576dcc
  FlagManagement: CRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p3b
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.59
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 61e9a43176752d3139e7f79a
  Name: comp6-p3b-eu-spdc-FCH2017V24J
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: FCH2017V24J
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 131072
  AvailableMemoryGB: 128
  AvailableMemoryUnit: 128 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 61fa65ab6f72612d300ab92a
  FlagManagement: CRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p3b
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.48
  ManagementMode: IntersightStandalone
  Model: UCSC-C240-M4SX
  Moid: 61fa65c276752d3139491f4a
  Name: comp1-p3b-eu-spdc-FCH2017V1J7
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: FCH2017V1J7
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C240-M4SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.55
  ManagementMode: UCSM
  Model: HXAF220C-M5SN
  Moid: 62d157fd76752d313915f4f6
  Name: HX1-eu-spdc-2
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WZP24100SN0
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) HXAF220C-M5SN
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 786432
  AvailableMemoryGB: 768
  AvailableMemoryUnit: 768 [GiB]
  Connected: true
  Cpu: 2S 52C 104T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.59
  ManagementMode: UCSM
  Model: HXAF240C-M5SX
  Moid: 62d157fe76752d313915f512
  Name: HX1-eu-spdc-6
  NumCpuCores: 52
  NumCpus: 2
  NumThreads: 104
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WMP250901AY
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  Type: Rack
  TypeModel: (R) HXAF240C-M5SX
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 3
    Info: 3
    Warning: 4
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P+ C(3)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (3)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.57
  ManagementMode: UCSM
  Model: HXAF220C-M5SN
  Moid: 62d157fe76752d313915f529
  Name: HX1-eu-spdc-4
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WZP24100SMP
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) HXAF220C-M5SN
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 786432
  AvailableMemoryGB: 768
  AvailableMemoryUnit: 768 [GiB]
  Connected: true
  Cpu: 2S 52C 104T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.58
  ManagementMode: UCSM
  Model: HXAF240C-M5SX
  Moid: 62d157fe76752d313915f549
  Name: HX1-eu-spdc-5
  NumCpuCores: 52
  NumCpus: 2
  NumThreads: 104
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WMP250901B0
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  Type: Rack
  TypeModel: (R) HXAF240C-M5SX
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 786432
  AvailableMemoryGB: 768
  AvailableMemoryUnit: 768 [GiB]
  Connected: true
  Cpu: 2S 52C 104T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.54
  ManagementMode: UCSM
  Model: HXAF240C-M5SX
  Moid: 62d157fe76752d313915f563
  Name: HX1-eu-spdc-7
  NumCpuCores: 52
  NumCpus: 2
  NumThreads: 104
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WMP2509019D
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  Type: Rack
  TypeModel: (R) HXAF240C-M5SX
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.53
  ManagementMode: UCSM
  Model: HXAF220C-M5SN
  Moid: 62e2b54b76752d3139eab326
  Name: HX1-eu-spdc-3
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WZP24100SML
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) HXAF220C-M5SN
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 2
    Info: 2
    Warning: 6
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 62d157f56f72612d31c554a7
  FlagManagement: Cu
  FlagState: P- C(2)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (2)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.24.56
  ManagementMode: UCSM
  Model: HXAF220C-M5SN
  Moid: 62ebeb3876752d3139464b1f
  Name: HX1-eu-spdc-1
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: false
    Enabled: false
  Serial: WZP24100SMV
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) HXAF220C-M5SN
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.RRRR
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 1
  AvailableMemory: 688128
  AvailableMemoryGB: 672
  AvailableMemoryUnit: 672 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 61c35fa36f72612d3005590c
  FlagManagement: Cu
  FlagState: P+ W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.49.234.196
  ManagementMode: UCSM
  Model: UCSC-C220-M4S
  Moid: 6311aae876752d31398e1a50
  Name: berlin-ucsm-3
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH2031V0YM
  TotalMemory: 688128
  TotalMemoryGB: 672
  TotalMemoryUnit: 672 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: true
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6336f14d6f72612d31d41b72
  FlagManagement: CRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.38
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 6336f19576752d3139f05a4b
  Name: esx21-eu-spdc-WZP23440N1P
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WZP23440N1P
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 32768
  AvailableMemoryGB: 32
  AvailableMemoryUnit: 32 [GiB]
  Connected: true
  Cpu: 2S 56C 112T
  DeviceMoId: 637b897f6f72612d39f8b9e9
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.242.29.174
  ManagementMode: IntersightStandalone
  Model: ProLiant DL360 Gen10 Plus
  Moid: 637b898f76752d3139ba61cc
  Name: HPE-ProLiant DL360 Gen10 Plus-VYRBX9UJ4S
  NumCpuCores: 56
  NumCpus: 2
  NumThreads: 112
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: VYRBX9UJ4S
  TotalMemory: 32768
  TotalMemoryGB: 32
  TotalMemoryUnit: 32 [GiB]
  Type: Rack
  TypeModel: (R) ProLiant DL360 Gen10 Plus
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 131072
  AvailableMemoryGB: 128
  AvailableMemoryUnit: 128 [GiB]
  Connected: true
  Cpu: 2S 56C 112T
  DeviceMoId: 637b8a016f72612d39f8bfa7
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.44.182.90
  ManagementMode: IntersightStandalone
  Model: PowerEdge R650
  Moid: 637b8a1276752d3139ba7805
  Name: Dell-PowerEdge R650-YGFCBTJSO8WOMR
  NumCpuCores: 56
  NumCpus: 2
  NumThreads: 112
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: YGFCBTJSO8WOMR
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  Type: Rack
  TypeModel: (R) PowerEdge R650
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 637ca8cd6f72612d3130bddc
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.52
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 637ca9b576752d3139eea04f
  Name: esx12-eu-spdc-FCH2049V1WU
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2049V1WU
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 1
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 16C 32T
  DeviceMoId: 637cadbb6f72612d3130e87a
  FlagManagement: Cri
  FlagState: P+ W(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Warnings (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.53
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 637caeb676752d3139ef7b01
  Name: esx13-eu-spdc-FCH2018V027
  NumCpuCores: 16
  NumCpus: 2
  NumThreads: 32
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2018V027
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.YYYY
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 36C 72T
  DeviceMoId: 637ce9916f72612d3132dcb3
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.36
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 637ce9a576752d3139f994e1
  Name: esx4-eu-spdc-FCH2016V2BE
  NumCpuCores: 36
  NumCpus: 2
  NumThreads: 72
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2016V2BE
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 637d60986f72612d31377620
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.28.33
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 637d61fd76752d31390ef488
  Name: esx1-eu-spdc-FCH2017V0T3
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V0T3
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 1
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 637d63196f72612d313788d7
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.29.42
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 637d65ac76752d3139102834
  Name: esx14-eu-spdc-FCH2017V0TE
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH2017V0TE
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 1
    Info: 1
    Warning: 1
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 28C 56T
  DeviceMoId: 637f58116f72612d31490de7
  FlagManagement: CRi
  FlagState: P+ C(1)
  FlagWorkflow: ''
  Groups: ''
  Health: Critical (1)
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.60
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M4S
  Moid: 637f588776752d313966cb9d
  Name: comp7-p3b-eu-spdc-FCH2023V2A4
  NumCpuCores: 28
  NumCpus: 2
  NumThreads: 56
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: FCH2023V2A4
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M4S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 128C 256T
  DeviceMoId: 6384d44a6f72612d317bfc51
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.53.34
  ManagementMode: IntersightStandalone
  Model: UCSC-C245-M6SX
  Moid: 6384d45476752d31395c7874
  Name: comp2-p4b-eu-spdc-WZP26360D3D
  NumCpuCores: 128
  NumCpus: 2
  NumThreads: 256
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP26360D3D
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C245-M6SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 1S 64C 128T
  DeviceMoId: 638501816f72612d317dabd7
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.53.35
  ManagementMode: IntersightStandalone
  Model: UCSC-C225-M6S
  Moid: 6385018e76752d313964b3b5
  Name: comp3-p4b-eu-spdc-WZP262207UM
  NumCpuCores: 64
  NumCpus: 1
  NumThreads: 128
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP262207UM
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C225-M6S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 1S 32C 64T
  DeviceMoId: 638502356f72612d317db208
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.53.36
  ManagementMode: IntersightStandalone
  Model: UCSC-C225-M6S
  Moid: 6385028e76752d313964e821
  Name: comp4-p4b-eu-spdc-WZP262207VP
  NumCpuCores: 32
  NumCpus: 1
  NumThreads: 64
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP262207VP
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C225-M6S
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 48C 96T
  DeviceMoId: 6388e7616f72612d31a41c5c
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.53.33
  ManagementMode: IntersightStandalone
  Model: UCSC-C245-M6SX
  Moid: 6388e77876752d313919a95d
  Name: comp1-p4b-eu-spdc-WZP26360D36
  NumCpuCores: 48
  NumCpus: 2
  NumThreads: 96
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: WZP26360D36
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C245-M6SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: false
  Cpu: 2S 24C 48T
  DeviceMoId: 5efdfb7e6f72612d30e4501e
  FlagManagement: cri
  FlagState: P- H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: ''
  ManagementMode: IntersightStandalone
  Model: UCSC-C3K-M4SRB
  Moid: 5efdfb996176752d3559b9d5
  Name: C3X60M4-FCH21067808
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH21067808
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Blade
  TypeModel: (B) UCSC-C3K-M4SRB
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :RR.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 61bb97146f72612d301e5946
  FlagManagement: Cri
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: ''
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: ''
  ManagementMode: IntersightStandalone
  Model: UCSC-C3K-M4SRB
  Moid: 61bb973176752d3139b05b78
  Name: ynas-eu-spdc-FCH21067808
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: false
  Serial: FCH21067808
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Blade
  TypeModel: (B) UCSC-C3K-M4SRB
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.41
  ManagementMode: UCSM
  Model: UCSB-B200-M5
  Moid: 6335c26e76752d3139b9694c
  Name: FI-ucsb1-eu-spdc-2-1
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FLM241501FB
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M5
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.42
  ManagementMode: UCSM
  Model: UCSB-B200-M5
  Moid: 6335c45976752d3139b9bf94
  Name: FI-ucsb1-eu-spdc-2-2
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FLM24140BJB
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M5
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 9
    Info: 0
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ C(9)
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Critical (9)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.33
  ManagementMode: UCSM
  Model: UCSB-B200-M4
  Moid: 6335e1f376752d3139bf12b8
  Name: FI-ucsb1-eu-spdc-1-1
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH205371PZ
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M4
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 9
    Info: 1
    Warning: 0
  AvailableMemory: 524288
  AvailableMemoryGB: 512
  AvailableMemoryUnit: 512 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ C(9)
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Critical (9)
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.34
  ManagementMode: UCSM
  Model: UCSB-B200-M4
  Moid: 6337014c76752d3139f2f459
  Name: FI-ucsb1-eu-spdc-1-2
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH20527XXD
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M4
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.RRRR
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.35
  ManagementMode: UCSM
  Model: UCSB-B200-M4
  Moid: 6337063276752d3139f3cc83
  Name: FI-ucsb1-eu-spdc-1-3
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH20437VXH
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M4
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 262144
  AvailableMemoryGB: 256
  AvailableMemoryUnit: 256 [GiB]
  Connected: true
  Cpu: 2S 24C 48T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.36
  ManagementMode: UCSM
  Model: UCSB-B200-M4
  Moid: 63371c9176752d3139f7da74
  Name: FI-ucsb1-eu-spdc-1-4
  NumCpuCores: 24
  NumCpus: 2
  NumThreads: 48
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FCH205371UU
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M4
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 196608
  AvailableMemoryGB: 192
  AvailableMemoryUnit: 192 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.44
  ManagementMode: UCSM
  Model: UCSB-B200-M5
  Moid: 63371c9176752d3139f7da78
  Name: FI-ucsb1-eu-spdc-2-4
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FLM24140B0B
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M5
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
- AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 196608
  AvailableMemoryGB: 192
  AvailableMemoryUnit: 192 [GiB]
  Connected: true
  Cpu: 2S 40C 80T
  DeviceMoId: 618942976f72612d309dfbe1
  FlagManagement: CU
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: power,ucsm
  Health: Healthy
  IMC:
    Capable: false
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.52.43
  ManagementMode: UCSM
  Model: UCSB-B200-M5
  Moid: 63371c9176752d3139f7da82
  Name: FI-ucsb1-eu-spdc-2-3
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: false
    Enabled: false
  Serial: FLM241501CT
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  Type: Blade
  TypeModel: (B) UCSB-B200-M5
  UCSM:
    Capable: true
    Enabled: true
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  Workflow:
    Last: []
    LatestMoid: null
    Running: null
  __Output:
    FlagState: :GG.G
```

Developer output

```
# iserver get servers -o yaml

Developer output

{
    "duration": 6640,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 6073
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
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
        "read": true,
        "lines": 48
    }
}

Log: isctl
-----------

2022-12-13 16:57:41.256610	True	2298	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:57:42.147315	True	887	10	isctl get compute blade   -o json --top 100
2022-12-13 16:57:42.575228	True	381	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:57:42.735903	True	544	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:57:42.000Z"  -o json --top 100
2022-12-13 16:57:43.674639	True	1490	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:57:44.147600	True	473	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
```
