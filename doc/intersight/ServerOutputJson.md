# Intersight Server

## JSON output

```
# iserver get server --group test -o json

[
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GGY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9bf46176752d35e4426e",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9bf46176752d35e4426e"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c886176752d35e477e4",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477e4"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c886176752d35e477ea",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477ea"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c886176752d35e477f0",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477f0"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [],
            "AssetTag": "022C2F4",
            "AvailableMemory": 393216,
            "BiosBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9bff6176752d35e4471c",
                "ObjectType": "bios.BootMode",
                "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9bff6176752d35e4471c"
            },
            "BiosPostComplete": false,
            "BiosTokenSettings": null,
            "BiosVfSelectMemoryRasConfiguration": {
                "ClassId": "mo.MoRef",
                "Moid": "60d5fbe96176752d35a30aa7",
                "ObjectType": "bios.VfSelectMemoryRasConfiguration",
                "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30aa7"
            },
            "Biosunits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9bfe6176752d35e446cf",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9bfe6176752d35e446cf"
                }
            ],
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c416176752d35e45e43",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9c416176752d35e45e43"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c056176752d35e44930",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9c056176752d35e44930"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c2d6176752d35e45801",
                "ObjectType": "boot.DeviceBootSecurity",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9c2d6176752d35e45801"
            },
            "BootDeviceBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c2d6176752d35e457e2",
                "ObjectType": "boot.DeviceBootMode",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9c2d6176752d35e457e2"
            },
            "BootHddDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "60000c0b6176752d35b76e3e",
                    "ObjectType": "boot.HddDevice",
                    "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c0b6176752d35b76e3e"
                }
            ],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "60000c046176752d35b76bb3",
                    "ObjectType": "boot.PxeDevice",
                    "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000c046176752d35b76bb3"
                }
            ],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6013f1496176752d35458e49",
                    "ObjectType": "boot.VmediaDevice",
                    "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1496176752d35458e49"
                }
            ],
            "ClassId": "compute.RackUnit",
            "ComputePersonality": [],
            "ConnectionStatus": "",
            "CreateTime": "2020-12-20T18:46:25.383Z",
            "DeviceMoId": "5fdf9be76f72612d300a8d81",
            "Dn": "sys/rack-unit-1",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "Fanmodules": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d71",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d71"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d73",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d73"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d75",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d75"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d77",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d77"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d79",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d79"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d7b",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7b"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c106176752d35e44d7d",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7d"
                }
            ],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c7f6176752d35e473d9",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9c7f6176752d35e473d9"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.50.41",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.50.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "Avocent",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5fdf9c016176752d35e44795",
                        "ObjectType": "compute.RackUnit",
                        "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c016176752d35e44795"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": null,
                "ComputeRackUnit": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c016176752d35e44795",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c016176752d35e44795"
                },
                "CreateTime": "2020-12-20T18:46:44.288Z",
                "DeviceMoId": "5fdf9be76f72612d300a8d81",
                "Dn": "sys/rack-unit-1/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2023-11-16T01:48:02.452Z",
                "Moid": "5fdf9c146176752d35e44eca",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "5fdf9be76f72612d300a8d81"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c016176752d35e44795",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c016176752d35e44795"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9be76f72612d300a8d81",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9be76f72612d300a8d81"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "IntersightStandalone",
            "MemoryArrays": [],
            "MemorySpeed": "2933",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.50.41",
            "ModTime": "2023-12-01T05:12:39.502Z",
            "Model": "UCSC-C240-M5SN",
            "Moid": "5fdf9c016176752d35e44795",
            "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
            "NumAdaptors": 1,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 4,
            "NumFcHostInterfaces": 4,
            "NumThreads": 80,
            "ObjectType": "compute.RackUnit",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "",
            "Operability": "",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "5fdf9be76f72612d300a8d81"
            ],
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c546176752d35e465cd",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cd"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c546176752d35e465cf",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cf"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c546176752d35e465d1",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d1"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c546176752d35e465d3",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d3"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c546176752d35e465d9",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d9"
                }
            ],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "IMCM5",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "Psus": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c0d6176752d35e44cf7",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf7"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c0d6176752d35e44cf9",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf9"
                }
            ],
            "RackEnclosureSlot": null,
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 14,
                "AppPartitionNumber": 226,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2020-12-20T18:46:00.104Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5fdf9be86f72612d300a8d87",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/5fdf9be86f72612d300a8d87"
                    }
                ],
                "ConnectionId": "f333e59b15fc770847aae7df5bfbdf86:ea06cce9-5f8f-4e27-9c64-058aab5f3201",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T05:12:39.272Z",
                "ConnectorVersion": "1.0.11-3136",
                "CreateTime": "2020-12-20T18:45:59.948Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9be76f72612d300a8d72",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/5fdf9be76f72612d300a8d72"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9be76f72612d300a8d82",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/5fdf9be76f72612d300a8d82"
                },
                "DeviceExternalIpAddress": "173.38.209.7",
                "DeviceHostname": [
                    "comp-1-p2b-eu-spdc-WZP23400AJW"
                ],
                "DeviceIpAddress": [
                    "10.58.50.41"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T05:12:39.284Z",
                "Moid": "5fdf9be76f72612d300a8d81",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "5fdf9be76f72612d300a8d81"
                ],
                "ParentConnection": null,
                "ParentSignature": {
                    "ClassId": "asset.ParentConnectionSignature",
                    "DeviceId": "",
                    "NodeId": "",
                    "ObjectType": "asset.ParentConnectionSignature",
                    "Signature": "",
                    "TimeStamp": "0001-01-01T00:00:00Z"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCSC-C240-M5SN"
                ],
                "PlatformType": "IMCM5",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxj4nSgORfUCi8Wu9pl4l\nfghC4ZBURr1Y0GuLmeXsIbbjNitlcFU+CJmmc7gCGM8pPBGOAq5HfKKSrgKIMB/1\nLkEruC5N5xtVeggTolrwVSr4gXsUZXaQx0A6wMLzEW8CJfe5fnfW9s5PdoRuWoFw\nJxjDtAev/TrUKNnDSFS3drZGMW4sha1S954jW4tXbkVMUKl8XkUWbFSHVlOfc/Ct\nft8y44QVHkgBH2CdrqNxBe2WgfHKHeosyVm1XYNkDJYdYnwfclflifutXeQqF9DH\n4dyTKE8bg9qLAx+A59lP1g1cBS0H8UdcVlEbKOsARDemecF0Y35EhH6gX69jP1MG\n/QIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "WZP23400AJW"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": null,
                "Vendor": "Cisco Systems Inc"
            },
            "Revision": "",
            "Rn": "",
            "SasExpanders": [],
            "Serial": "WZP23400AJW",
            "ServerId": 1,
            "ServiceProfile": "",
            "SharedScope": "",
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                },
                {
                    "Key": "psirt",
                    "Value": "ready"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c526176752d35e46529",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9c526176752d35e46529"
            },
            "TopologyScanStatus": "",
            "TotalMemory": 393216,
            "TunneledKvm": true,
            "UnitPersonality": [],
            "UserLabel": "comp-1-p2b-eu-spdc-WZP23400AJW",
            "Uuid": "488930EF-5754-434B-B570-C2BD8359E739",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.50.41"
        },
        "Moid": "5fdf9c016176752d35e44795",
        "Ancestors": [],
        "DeviceMoId": "5fdf9be76f72612d300a8d81",
        "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AJW",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 393216,
        "TotalMemory": 393216,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "AvailableMemoryUnit": "384 [GiB]",
        "AvailableMemoryGB": 384,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": null,
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Rack Server",
                "Model": "UCSC-C240-M5SN",
                "Vendor": "Cisco Systems Inc",
                "Serial": "WZP23400AJW",
                "Pid": "UCSC-C240-M5SN",
                "ChassisMoid": null,
                "ServerType": "Rack",
                "ServerPid": "UCSC-C240-M5SN",
                "ServerSerial": "WZP23400AJW"
            }
        ],
        "InventoryServerPid": "UCSC-C240-M5SN",
        "InventoryServerSerial": "WZP23400AJW",
        "Groups": "p2b,test,power",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.50.41",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.50.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "Avocent",
            "TunneledKvm": true
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [
            {
                "Key": "psirt",
                "Value": "ready"
            }
        ],
        "ManagementIp": "10.58.50.41",
        "Redfish": {
            "Capable": true,
            "Enabled": true
        },
        "UCSM": {
            "Capable": false,
            "Enabled": false
        },
        "IMC": {
            "Capable": true,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "5fdf9be76f72612d300a8d81",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2020-12-20T18:46:00.104Z",
            "PlatformType": "IMCM5",
            "ConnectorVersion": "1.0.11-3136",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "173.38.209.7",
            "ConnectionStatusLastChangeTime": "2023-12-01T05:12:39.272Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GGY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c6b6176752d35e46d1c",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c6b6176752d35e46d1c"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cfe6176752d35e4aa7f",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa7f"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cfe6176752d35e4aa85",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa85"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cfe6176752d35e4aa8b",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa8b"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [],
            "AssetTag": "022C2F7",
            "AvailableMemory": 393216,
            "BiosBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c756176752d35e4704d",
                "ObjectType": "bios.BootMode",
                "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9c756176752d35e4704d"
            },
            "BiosPostComplete": false,
            "BiosTokenSettings": null,
            "BiosVfSelectMemoryRasConfiguration": {
                "ClassId": "mo.MoRef",
                "Moid": "60d5ee256176752d359b9914",
                "ObjectType": "bios.VfSelectMemoryRasConfiguration",
                "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee256176752d359b9914"
            },
            "Biosunits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c736176752d35e46f8c",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9c736176752d35e46f8c"
                }
            ],
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9cb86176752d35e48ebd",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9cb86176752d35e48ebd"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9c7c6176752d35e472bd",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9c7c6176752d35e472bd"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9ca56176752d35e4844f",
                "ObjectType": "boot.DeviceBootSecurity",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9ca56176752d35e4844f"
            },
            "BootDeviceBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9ca46176752d35e483e0",
                "ObjectType": "boot.DeviceBootMode",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9ca46176752d35e483e0"
            },
            "BootHddDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "60000c066176752d35b76c32",
                    "ObjectType": "boot.HddDevice",
                    "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c066176752d35b76c32"
                }
            ],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "60000bff6176752d35b769c9",
                    "ObjectType": "boot.PxeDevice",
                    "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bff6176752d35b769c9"
                }
            ],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6013f1466176752d35458cdb",
                    "ObjectType": "boot.VmediaDevice",
                    "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1466176752d35458cdb"
                }
            ],
            "ClassId": "compute.RackUnit",
            "ComputePersonality": [],
            "ConnectionStatus": "",
            "CreateTime": "2020-12-20T18:48:24.465Z",
            "DeviceMoId": "5fdf9c676f72612d300a9c8d",
            "Dn": "sys/rack-unit-1",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "Fanmodules": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e4777c",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777c"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e4777e",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777e"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e47780",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47780"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e47782",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47782"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e47784",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47784"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e47786",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47786"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c876176752d35e47788",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47788"
                }
            ],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cf66176752d35e4a75b",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9cf66176752d35e4a75b"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.50.42",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.50.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "Avocent",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5fdf9c786176752d35e47110",
                        "ObjectType": "compute.RackUnit",
                        "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c786176752d35e47110"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": null,
                "ComputeRackUnit": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c786176752d35e47110",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c786176752d35e47110"
                },
                "CreateTime": "2020-12-20T18:48:43.538Z",
                "DeviceMoId": "5fdf9c676f72612d300a9c8d",
                "Dn": "sys/rack-unit-1/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2022-12-12T09:28:16.781Z",
                "Moid": "5fdf9c8b6176752d35e47959",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "5fdf9c676f72612d300a9c8d"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c786176752d35e47110",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c786176752d35e47110"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c676f72612d300a9c8d",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9c676f72612d300a9c8d"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "IntersightStandalone",
            "MemoryArrays": [],
            "MemorySpeed": "2933",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.50.42",
            "ModTime": "2023-12-01T20:29:27.016Z",
            "Model": "UCSC-C240-M5SN",
            "Moid": "5fdf9c786176752d35e47110",
            "Name": "comp-2-p2b-eu-spdc-WZP23400AK4",
            "NumAdaptors": 1,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 4,
            "NumFcHostInterfaces": 4,
            "NumThreads": 80,
            "ObjectType": "compute.RackUnit",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "",
            "Operability": "",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "5fdf9c676f72612d300a9c8d"
            ],
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9ccb6176752d35e496d1",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d1"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9ccb6176752d35e496d3",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d3"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9ccb6176752d35e496d5",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9ccb6176752d35e496d7",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d7"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9ccb6176752d35e496da",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496da"
                }
            ],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "IMCM5",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "Psus": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c856176752d35e476b8",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476b8"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c856176752d35e476ba",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476ba"
                }
            ],
            "RackEnclosureSlot": null,
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 14,
                "AppPartitionNumber": 71,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2020-12-20T18:48:08.061Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5fdf9c686f72612d300a9c90",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/5fdf9c686f72612d300a9c90"
                    }
                ],
                "ConnectionId": "268da2c6ff5a59811fd06a0997350da6:5917ed40-f56d-40c8-a1bc-822397c3d636",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T20:29:26.594Z",
                "ConnectorVersion": "1.0.11-3136",
                "CreateTime": "2020-12-20T18:48:07.916Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c676f72612d300a9c84",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/5fdf9c676f72612d300a9c84"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9c676f72612d300a9c8e",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/5fdf9c676f72612d300a9c8e"
                },
                "DeviceExternalIpAddress": "173.38.209.6",
                "DeviceHostname": [
                    "comp-2-p2b-eu-spdc-WZP23400AK4"
                ],
                "DeviceIpAddress": [
                    "10.58.50.42"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T20:29:26.607Z",
                "Moid": "5fdf9c676f72612d300a9c8d",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "5fdf9c676f72612d300a9c8d"
                ],
                "ParentConnection": null,
                "ParentSignature": {
                    "ClassId": "asset.ParentConnectionSignature",
                    "DeviceId": "",
                    "NodeId": "",
                    "ObjectType": "asset.ParentConnectionSignature",
                    "Signature": "",
                    "TimeStamp": "0001-01-01T00:00:00Z"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCSC-C240-M5SN"
                ],
                "PlatformType": "IMCM5",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqmUVV/cclSdCDDsCCN8+\nrTqn5Jk5Htq2/As1iLNxQfbipUON3u4JF/zhDXnweJcvNq8b5aGLembth1pSkr9u\nW05ejiwzOSKrhuPMY8mtH280lNge/zVAj4T8WNMSwfwrJSc9pg2Mo5VEn9NZyhS8\nDCSHEr26+G6ODERUniKrkwLw2TuSPu7oqfTUxGpqy1s0m50y3r+ezn2lT0DW3pv/\nuS6ZiosMxyMycv0aQ2zBL9QUeJE5d+JIinjRfjx/FKzkU03Yo2BdJSrEbKRGZML+\n1+8f45IFlUwKBVc2DnXr65VZFe9OOOTNYFR+jU1s5URVYjonO8CxAlig9DUSKl4R\nTwIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "WZP23400AK4"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": null,
                "Vendor": "Cisco Systems Inc"
            },
            "Revision": "",
            "Rn": "",
            "SasExpanders": [],
            "Serial": "WZP23400AK4",
            "ServerId": 1,
            "ServiceProfile": "",
            "SharedScope": "",
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                },
                {
                    "Key": "psirt",
                    "Value": "ready"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9cc96176752d35e49601",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9cc96176752d35e49601"
            },
            "TopologyScanStatus": "",
            "TotalMemory": 393216,
            "TunneledKvm": true,
            "UnitPersonality": [],
            "UserLabel": "comp-2-p2b-eu-spdc-WZP23400AK4",
            "Uuid": "B813910F-BFD2-439F-9C3B-75B376C5B160",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.50.42"
        },
        "Moid": "5fdf9c786176752d35e47110",
        "Ancestors": [],
        "DeviceMoId": "5fdf9c676f72612d300a9c8d",
        "Name": "comp-2-p2b-eu-spdc-WZP23400AK4",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AK4",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 393216,
        "TotalMemory": 393216,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "AvailableMemoryUnit": "384 [GiB]",
        "AvailableMemoryGB": 384,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": null,
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Rack Server",
                "Model": "UCSC-C240-M5SN",
                "Vendor": "Cisco Systems Inc",
                "Serial": "WZP23400AK4",
                "Pid": "UCSC-C240-M5SN",
                "ChassisMoid": null,
                "ServerType": "Rack",
                "ServerPid": "UCSC-C240-M5SN",
                "ServerSerial": "WZP23400AK4"
            }
        ],
        "InventoryServerPid": "UCSC-C240-M5SN",
        "InventoryServerSerial": "WZP23400AK4",
        "Groups": "p2b,test,power",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.50.42",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.50.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "Avocent",
            "TunneledKvm": true
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [
            {
                "Key": "psirt",
                "Value": "ready"
            }
        ],
        "ManagementIp": "10.58.50.42",
        "Redfish": {
            "Capable": true,
            "Enabled": true
        },
        "UCSM": {
            "Capable": false,
            "Enabled": false
        },
        "IMC": {
            "Capable": true,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "5fdf9c676f72612d300a9c8d",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2020-12-20T18:48:08.061Z",
            "PlatformType": "IMCM5",
            "ConnectorVersion": "1.0.11-3136",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "173.38.209.6",
            "ConnectionStatusLastChangeTime": "2023-12-01T20:29:26.594Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G..",
            "FlagManagement": ":GGY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cf56176752d35e4a70f",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cf56176752d35e4a70f"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d896176752d35e4e0b6",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0b6"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d896176752d35e4e0bc",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0bc"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d896176752d35e4e0c2",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0c2"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [],
            "AssetTag": "022C2CE",
            "AvailableMemory": 393216,
            "BiosBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9d006176752d35e4aae0",
                "ObjectType": "bios.BootMode",
                "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9d006176752d35e4aae0"
            },
            "BiosPostComplete": false,
            "BiosTokenSettings": null,
            "BiosVfSelectMemoryRasConfiguration": {
                "ClassId": "mo.MoRef",
                "Moid": "60d5ee266176752d359b9a6f",
                "ObjectType": "bios.VfSelectMemoryRasConfiguration",
                "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee266176752d359b9a6f"
            },
            "Biosunits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cfd6176752d35e4aa25",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9cfd6176752d35e4aa25"
                }
            ],
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9d426176752d35e4c645",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9d426176752d35e4c645"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9d066176752d35e4aebe",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9d066176752d35e4aebe"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9d2f6176752d35e4bf2f",
                "ObjectType": "boot.DeviceBootSecurity",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9d2f6176752d35e4bf2f"
            },
            "BootDeviceBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9d2e6176752d35e4bef4",
                "ObjectType": "boot.DeviceBootMode",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9d2e6176752d35e4bef4"
            },
            "BootHddDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "60000c046176752d35b76bd5",
                    "ObjectType": "boot.HddDevice",
                    "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c046176752d35b76bd5"
                }
            ],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "60000bfd6176752d35b7692a",
                    "ObjectType": "boot.PxeDevice",
                    "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bfd6176752d35b7692a"
                }
            ],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6013f1486176752d35458daf",
                    "ObjectType": "boot.VmediaDevice",
                    "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1486176752d35458daf"
                }
            ],
            "ClassId": "compute.RackUnit",
            "ComputePersonality": [],
            "ConnectionStatus": "",
            "CreateTime": "2020-12-20T18:50:42.597Z",
            "DeviceMoId": "5fdf9cf26f72612d300aaca0",
            "Dn": "sys/rack-unit-1",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "Fanmodules": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b355",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b355"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b357",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b357"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b359",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b359"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b35b",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35b"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b35d",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35d"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b35f",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35f"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d116176752d35e4b361",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b361"
                }
            ],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d806176752d35e4de4d",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9d806176752d35e4de4d"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.50.43",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.50.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "Avocent",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5fdf9d026176752d35e4ac4e",
                        "ObjectType": "compute.RackUnit",
                        "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9d026176752d35e4ac4e"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": null,
                "ComputeRackUnit": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d026176752d35e4ac4e",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9d026176752d35e4ac4e"
                },
                "CreateTime": "2020-12-20T18:51:01.737Z",
                "DeviceMoId": "5fdf9cf26f72612d300aaca0",
                "Dn": "sys/rack-unit-1/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2023-11-16T02:15:14.838Z",
                "Moid": "5fdf9d156176752d35e4b534",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "on",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "5fdf9cf26f72612d300aaca0"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d026176752d35e4ac4e",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9d026176752d35e4ac4e"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cf26f72612d300aaca0",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9cf26f72612d300aaca0"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "IntersightStandalone",
            "MemoryArrays": [],
            "MemorySpeed": "2933",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.50.43",
            "ModTime": "2023-12-01T22:41:35.443Z",
            "Model": "UCSC-C240-M5SN",
            "Moid": "5fdf9d026176752d35e4ac4e",
            "Name": "comp-3-p2b-eu-spdc-WZP23400AKL",
            "NumAdaptors": 1,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 4,
            "NumFcHostInterfaces": 4,
            "NumThreads": 80,
            "ObjectType": "compute.RackUnit",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "",
            "Operability": "",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "5fdf9cf26f72612d300aaca0"
            ],
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d556176752d35e4cd3d",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd3d"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d556176752d35e4cd41",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd41"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d556176752d35e4cd43",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd43"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d556176752d35e4cd48",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd48"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d566176752d35e4cd4a",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d566176752d35e4cd4a"
                }
            ],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "IMCM5",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "Psus": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d0f6176752d35e4b2a3",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9d0f6176752d35e4b2a3"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9d0f6176752d35e4b2a5",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9d0f6176752d35e4b2a5"
                }
            ],
            "RackEnclosureSlot": null,
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 14,
                "AppPartitionNumber": 130,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2020-12-20T18:50:26.206Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5fdf9cf26f72612d300aaca3",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/5fdf9cf26f72612d300aaca3"
                    }
                ],
                "ConnectionId": "e73499a43c52cfbb4df6d917dfff2ef8:cdbb75dd-b09e-4f96-84c4-0995d282dd7f",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T22:41:35.389Z",
                "ConnectorVersion": "1.0.11-3136",
                "CreateTime": "2020-12-20T18:50:26.185Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cf26f72612d300aac97",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/5fdf9cf26f72612d300aac97"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5fdf9cf26f72612d300aaca1",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/5fdf9cf26f72612d300aaca1"
                },
                "DeviceExternalIpAddress": "173.38.209.11",
                "DeviceHostname": [
                    "comp-3-p2b-eu-spdc-WZP23400AKL"
                ],
                "DeviceIpAddress": [
                    "10.58.50.43"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T22:41:35.402Z",
                "Moid": "5fdf9cf26f72612d300aaca0",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "5fdf9cf26f72612d300aaca0"
                ],
                "ParentConnection": null,
                "ParentSignature": {
                    "ClassId": "asset.ParentConnectionSignature",
                    "DeviceId": "",
                    "NodeId": "",
                    "ObjectType": "asset.ParentConnectionSignature",
                    "Signature": "",
                    "TimeStamp": "0001-01-01T00:00:00Z"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCSC-C240-M5SN"
                ],
                "PlatformType": "IMCM5",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6kdJeo46ZC/3DP7mP1eY\nrRZx402181jXB+OWNmZAXsbqq10lhjE58w4OCo7oOUQnahgpI/pNSJmsBEs2Tm0M\nvvmAjyUQW8jcYtDlBM9K502MRyxYu4Up2eCTz47bFwOrd30XfYpHqjEdHhIjjljG\nf3dt7k0f+Q7REpv5pROVRl39WQZSqz2ujQq3IUh5T45xPhDH0UfqAFA7HAGZH86i\nH/wJzWCT89ZwkHJSmOSja78SNhAQVAw+AbjZcWJgTEmBy7Zw0/WUlU7vIyaEOiZU\nRCXA3fTS+yLFkLChoM6KsYTRxfa1Oy7OgIKS3B/hMiPky8ate4eyN/9LBMtLvtO7\nTQIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "WZP23400AKL"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": null,
                "Vendor": "Cisco Systems Inc"
            },
            "Revision": "",
            "Rn": "",
            "SasExpanders": [],
            "Serial": "WZP23400AKL",
            "ServerId": 1,
            "ServiceProfile": "",
            "SharedScope": "",
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                },
                {
                    "Key": "psirt",
                    "Value": "ready"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "5fdf9d536176752d35e4cc5f",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9d536176752d35e4cc5f"
            },
            "TopologyScanStatus": "",
            "TotalMemory": 393216,
            "TunneledKvm": false,
            "UnitPersonality": [],
            "UserLabel": "comp-3-p2b-eu-spdc-WZP23400AKL",
            "Uuid": "11942B96-9C29-4871-924F-F42877A98020",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.50.43"
        },
        "Moid": "5fdf9d026176752d35e4ac4e",
        "Ancestors": [],
        "DeviceMoId": "5fdf9cf26f72612d300aaca0",
        "Name": "comp-3-p2b-eu-spdc-WZP23400AKL",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AKL",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 393216,
        "TotalMemory": 393216,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "AvailableMemoryUnit": "384 [GiB]",
        "AvailableMemoryGB": 384,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": null,
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Rack Server",
                "Model": "UCSC-C240-M5SN",
                "Vendor": "Cisco Systems Inc",
                "Serial": "WZP23400AKL",
                "Pid": "UCSC-C240-M5SN",
                "ChassisMoid": null,
                "ServerType": "Rack",
                "ServerPid": "UCSC-C240-M5SN",
                "ServerSerial": "WZP23400AKL"
            }
        ],
        "InventoryServerPid": "UCSC-C240-M5SN",
        "InventoryServerSerial": "WZP23400AKL",
        "Groups": "p2b,test,power",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.50.43",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.50.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "Avocent",
            "TunneledKvm": false
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [
            {
                "Key": "psirt",
                "Value": "ready"
            }
        ],
        "ManagementIp": "10.58.50.43",
        "Redfish": {
            "Capable": true,
            "Enabled": true
        },
        "UCSM": {
            "Capable": false,
            "Enabled": false
        },
        "IMC": {
            "Capable": true,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "5fdf9cf26f72612d300aaca0",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2020-12-20T18:50:26.206Z",
            "PlatformType": "IMCM5",
            "ConnectorVersion": "1.0.11-3136",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "173.38.209.11",
            "ConnectionStatusLastChangeTime": "2023-12-01T22:41:35.389Z",
            "Connected": true
        },
        "LocatorLedOn": true,
        "FlagState": "P+ H L",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GGY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385018c76752d313964b35d",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6385018c76752d313964b35d"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385018c76752d313964b35f",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6385018c76752d313964b35f"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [],
            "AssetTag": "Unknown",
            "AvailableMemory": 524288,
            "BiosBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "638501fa76752d313964c6e3",
                "ObjectType": "bios.BootMode",
                "link": "https://www.intersight.com/api/v1/bios/BootModes/638501fa76752d313964c6e3"
            },
            "BiosPostComplete": false,
            "BiosTokenSettings": null,
            "BiosVfSelectMemoryRasConfiguration": null,
            "Biosunits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f976752d313964c6ce",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/638501f976752d313964c6ce"
                }
            ],
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "6385021f76752d313964d00a",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/6385021f76752d313964d00a"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "6385021176752d313964cbe0",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/6385021176752d313964cbe0"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": {
                "ClassId": "mo.MoRef",
                "Moid": "638501cf76752d313964bfea",
                "ObjectType": "boot.DeviceBootSecurity",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/638501cf76752d313964bfea"
            },
            "BootDeviceBootmode": {
                "ClassId": "mo.MoRef",
                "Moid": "6385021b76752d313964ce2e",
                "ObjectType": "boot.DeviceBootMode",
                "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/6385021b76752d313964ce2e"
            },
            "BootHddDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6543c32276752d39014afb27",
                    "ObjectType": "boot.HddDevice",
                    "link": "https://www.intersight.com/api/v1/boot/HddDevices/6543c32276752d39014afb27"
                }
            ],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "656a0dbf76752d39014f335a",
                    "ObjectType": "boot.VmediaDevice",
                    "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/656a0dbf76752d39014f335a"
                }
            ],
            "ClassId": "compute.RackUnit",
            "ComputePersonality": [],
            "ConnectionStatus": "",
            "CreateTime": "2022-11-28T18:44:30.302Z",
            "DeviceMoId": "638501816f72612d317dabd7",
            "Dn": "sys/rack-unit-1",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "Fanmodules": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5c6",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5c6"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5c8",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5c8"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5ca",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5ca"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5cc",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5cc"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5ce",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5ce"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5d0",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5d0"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5d2",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5d2"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501f176752d313964c5d4",
                    "ObjectType": "equipment.FanModule",
                    "link": "https://www.intersight.com/api/v1/equipment/FanModules/638501f176752d313964c5d4"
                }
            ],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385019776752d313964b5dd",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6385019776752d313964b5dd"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.53.35",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.53.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": true,
            "KvmVendor": "Cisco Systems",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6385018e76752d313964b3b5",
                        "ObjectType": "compute.RackUnit",
                        "link": "https://www.intersight.com/api/v1/compute/RackUnits/6385018e76752d313964b3b5"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": null,
                "ComputeRackUnit": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385018e76752d313964b3b5",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/6385018e76752d313964b3b5"
                },
                "CreateTime": "2022-11-28T18:46:42.645Z",
                "DeviceMoId": "638501816f72612d317dabd7",
                "Dn": "sys/rack-unit-1/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2022-11-28T18:46:42.667Z",
                "Moid": "6385021276752d313964cc11",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "638501816f72612d317dabd7"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385018e76752d313964b3b5",
                    "ObjectType": "compute.RackUnit",
                    "link": "https://www.intersight.com/api/v1/compute/RackUnits/6385018e76752d313964b3b5"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501816f72612d317dabd7",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/638501816f72612d317dabd7"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "IntersightStandalone",
            "MemoryArrays": [],
            "MemorySpeed": "3200",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.53.35",
            "ModTime": "2023-12-03T00:26:24.707Z",
            "Model": "UCSC-C225-M6S",
            "Moid": "6385018e76752d313964b3b5",
            "Name": "comp3-p4b-eu-spdc-WZP262207UM",
            "NumAdaptors": 2,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 1,
            "NumEthHostInterfaces": 14,
            "NumFcHostInterfaces": 6,
            "NumThreads": 128,
            "ObjectType": "compute.RackUnit",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "",
            "Operability": "",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "638501816f72612d317dabd7"
            ],
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501a376752d313964b7ab",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/638501a376752d313964b7ab"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501a376752d313964b7ad",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/638501a376752d313964b7ad"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501a376752d313964b7af",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/638501a376752d313964b7af"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501a376752d313964b7b1",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/638501a376752d313964b7b1"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501a376752d313964b7b3",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/638501a376752d313964b7b3"
                }
            ],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "IMCRack",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "Psus": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385021976752d313964cdf2",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/6385021976752d313964cdf2"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385021976752d313964cdf4",
                    "ObjectType": "equipment.Psu",
                    "link": "https://www.intersight.com/api/v1/equipment/Psus/6385021976752d313964cdf4"
                }
            ],
            "RackEnclosureSlot": null,
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 14,
                "AppPartitionNumber": 198,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2022-11-28T18:44:17.856Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "638501816f72612d317dabda",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/638501816f72612d317dabda"
                    }
                ],
                "ConnectionId": "b408d2fcbbebde8b61918478899ad3a7:4c114db8-ada8-4079-9644-7167c35c5cf9",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-03T00:26:24.649Z",
                "ConnectorVersion": "1.0.11-3273",
                "CreateTime": "2022-11-28T18:44:17.794Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501816f72612d317dabc8",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/638501816f72612d317dabc8"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "638501816f72612d317dabd8",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/638501816f72612d317dabd8"
                },
                "DeviceExternalIpAddress": "64.103.36.135",
                "DeviceHostname": [
                    "comp3-p4b-eu-spdc-WZP262207UM"
                ],
                "DeviceIpAddress": [
                    "10.58.53.35"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-03T00:26:27.55Z",
                "Moid": "638501816f72612d317dabd7",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "638501816f72612d317dabd7"
                ],
                "ParentConnection": null,
                "ParentSignature": null,
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCSC-C225-M6S"
                ],
                "PlatformType": "IMCRack",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwS22K1x0DFs2ZuajNwpB\n/bG41ueFsLbMs1MnUi09zSLzntTs9fev8j7irmYX85wIez7IOvALVGNqbEX5mMHn\nQ8wIyxX0YxArCAf9btSZvlg19X9SKAglYp9nnz8HPs9Ksx2JoLtIfu/PQTJ2ZSME\naXXtVDCd7ou7xbSbBF7WiUDkupdK0Sv5X/MQflS/pu7/uIhnwCFDbstT2zgu8tpZ\nW+WfSus/QOmOK8KcAQBL0KU5F2lEpPIPlqcuojC2x0Rq/dB1yGd+mmQu0/Qdu68i\njfgRCw9z/HhLPfODVARnOJnYyKBReM8Jn6uLoMN5UpdoRNMHaUtOlT4R3FT6IyKp\nAQIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "WZP262207UM"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": null,
                "Vendor": "Cisco Systems Inc"
            },
            "Revision": "",
            "Rn": "",
            "SasExpanders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385019a76752d313964b660",
                    "ObjectType": "storage.SasExpander",
                    "link": "https://www.intersight.com/api/v1/storage/SasExpanders/6385019a76752d313964b660"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6385019a76752d313964b662",
                    "ObjectType": "storage.SasExpander",
                    "link": "https://www.intersight.com/api/v1/storage/SasExpanders/6385019a76752d313964b662"
                }
            ],
            "Serial": "WZP262207UM",
            "ServerId": 1,
            "ServiceProfile": "",
            "SharedScope": "",
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                },
                {
                    "Key": "psirt",
                    "Value": "ready"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "6385022376752d313964d0e8",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/6385022376752d313964d0e8"
            },
            "TopologyScanStatus": "",
            "TotalMemory": 524288,
            "TunneledKvm": false,
            "UnitPersonality": [],
            "UserLabel": "comp3-p4b-eu-spdc-WZP262207UM",
            "Uuid": "C2DE66B5-AF1D-497A-9391-7666177332BC",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.53.35"
        },
        "Moid": "6385018e76752d313964b3b5",
        "Ancestors": [],
        "DeviceMoId": "638501816f72612d317dabd7",
        "Name": "comp3-p4b-eu-spdc-WZP262207UM",
        "Model": "UCSC-C225-M6S",
        "Serial": "WZP262207UM",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 1,
        "NumCpuCores": 64,
        "NumThreads": 128,
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "1S 64C 128T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": null,
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C225-M6S",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Rack Server",
                "Model": "UCSC-C225-M6S",
                "Vendor": "Cisco Systems Inc",
                "Serial": "WZP262207UM",
                "Pid": "UCSC-C225-M6S",
                "ChassisMoid": null,
                "ServerType": "Rack",
                "ServerPid": "UCSC-C225-M6S",
                "ServerSerial": "WZP262207UM"
            }
        ],
        "InventoryServerPid": "UCSC-C225-M6S",
        "InventoryServerSerial": "WZP262207UM",
        "Groups": "test",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.53.35",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.53.62",
                    "Dn": "sys/rack-unit-1/mgmt/if-1",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 1,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "MgmtInterface"
                }
            ],
            "KvmServerStateEnabled": true,
            "KvmVendor": "Cisco Systems",
            "TunneledKvm": false
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [
            {
                "Key": "psirt",
                "Value": "ready"
            }
        ],
        "ManagementIp": "10.58.53.35",
        "Redfish": {
            "Capable": true,
            "Enabled": true
        },
        "UCSM": {
            "Capable": false,
            "Enabled": false
        },
        "IMC": {
            "Capable": true,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "638501816f72612d317dabd7",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2022-11-28T18:44:17.856Z",
            "PlatformType": "IMCRack",
            "ConnectorVersion": "1.0.11-3273",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "64.103.36.135",
            "ConnectionStatusLastChangeTime": "2023-12-03T00:26:24.649Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4e76752d3901eb3b32",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4e76752d3901eb3b32"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4e76752d3901eb3b59",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4e76752d3901eb3b59"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4b76752d3901eb37c1",
                    "ObjectType": "equipment.Chassis",
                    "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                }
            ],
            "AssetTag": "",
            "AvailableMemory": 524288,
            "BiosBootmode": null,
            "BiosPostComplete": false,
            "BiosTokenSettings": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4e76752d3901eb3bb9",
                "ObjectType": "bios.TokenSettings",
                "link": "https://www.intersight.com/api/v1/bios/TokenSettings/6501db4e76752d3901eb3bb9"
            },
            "BiosUnits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4e76752d3901eb3b63",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/6501db4e76752d3901eb3b63"
                }
            ],
            "BiosVfSelectMemoryRasConfiguration": null,
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4e76752d3901eb3bee",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/6501db4e76752d3901eb3bee"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb3882",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/6501db4c76752d3901eb3882"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": null,
            "BootDeviceBootmode": null,
            "BootHddDevices": [],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [],
            "ChassisId": "2",
            "ClassId": "compute.Blade",
            "ComputePersonality": [],
            "CreateTime": "2023-09-13T15:54:52.287Z",
            "DeviceMoId": "6501db456f726131016b7aea",
            "Dn": "sys/chassis-2/blade-1",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "EquipmentChassis": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "EquipmentIoExpanders": [],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4d76752d3901eb39fb",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6501db4d76752d3901eb39fb"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.41",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.5",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4c76752d3901eb3851",
                        "ObjectType": "compute.Blade",
                        "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3851"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4b76752d3901eb37c1",
                        "ObjectType": "equipment.Chassis",
                        "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3851",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3851"
                },
                "ComputeRackUnit": null,
                "CreateTime": "2023-09-13T15:54:52.948Z",
                "DeviceMoId": "6501db456f726131016b7aea",
                "Dn": "sys/chassis-2/blade-1/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2023-09-13T15:54:53.553Z",
                "Moid": "6501db4c76752d3901eb393b",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3851",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3851"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aea",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/6501db456f726131016b7aea"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "UCSM",
            "MemoryArrays": [],
            "MemorySpeed": "2666",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.52.41, 10.58.26.5",
            "ModTime": "2023-10-26T16:51:51.926Z",
            "Model": "UCSB-B200-M5",
            "Moid": "6501db4c76752d3901eb3851",
            "Name": "FI-ucsb1-eu-spdc-2-1",
            "NumAdaptors": 2,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 8,
            "NumFcHostInterfaces": 0,
            "NumThreads": 80,
            "ObjectType": "compute.Blade",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "ok",
            "Operability": "operable",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "6501db456f726131016b7aea"
            ],
            "Parent": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb385c",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/6501db4c76752d3901eb385c"
                }
            ],
            "PciNodes": [],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "UCSFI",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 13,
                "AppPartitionNumber": 84,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2023-09-13T15:54:45.974Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aed",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aed"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aee",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aee"
                    }
                ],
                "ConnectionId": "d1b367932349a7337fca45793620279e:848e760a-bf08-40ac-a7b2-cfc679df0eea",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
                "ConnectorVersion": "1.0.11-4665",
                "CreateTime": "2023-09-13T15:54:45.905Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7ad3",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/6501db456f726131016b7ad3"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aeb",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/6501db456f726131016b7aeb"
                },
                "DeviceExternalIpAddress": "10.0.169.80",
                "DeviceHostname": [
                    "FI-ucsb1-eu-spdc"
                ],
                "DeviceIpAddress": [
                    "10.58.24.17",
                    "10.58.24.18",
                    "10.58.24.19"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T19:41:43.284Z",
                "Moid": "6501db456f726131016b7aea",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "ParentConnection": null,
                "ParentSignature": null,
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCS-FI-6454"
                ],
                "PlatformType": "UCSFI",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqLWPrQ0XQyasWeQGlBDc\nwFDK5hBWFYE/sEijwVNCuEozwSy1p3BwNPuScU7MhMrTn33RvQktqzAMe6DnXV5f\nPRJ3iVs6syKoIVXMS6CLLur4f5c5B6aI906fqBJpsW9K9XVMCwIaFy539F8mJEz8\nez5NUrYPX3D0TeNQryUxWYUE7uejdjj+7Ukb1Kg3cTRRjmQwdSlB6NOFDsEfcC05\nSTf7B4J/bk1IahdllHTOvLz4BD8t7/6U/kCzf68nuhOk25//pMUcr0xTR6ltcW0R\n4Fc5hE6giEZKgTUiL7nDZhl2pibOKGfNvZGyXXYeVqp4BS5bBFD//GZmDf0Clm8/\n0wIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "FDO241604GJ",
                    "FDO241604KU"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7af4",
                    "ObjectType": "asset.Target",
                    "link": "https://www.intersight.com/api/v1/asset/Targets/6501db456f726131016b7af4"
                },
                "Vendor": "Cisco Systems, Inc."
            },
            "Revision": "0",
            "Rn": "",
            "ScaledMode": "none",
            "Serial": "FLM241501FB",
            "ServiceProfile": "org-root/org-EU-SPN/ls-esx51-eu-spdc",
            "SharedScope": "",
            "SlotId": 1,
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb37fc",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/6501db4c76752d3901eb37fc"
            },
            "TotalMemory": 524288,
            "TunneledKvm": false,
            "UserLabel": "",
            "Uuid": "315220a5-2121-4e5b-0101-e1dc0000010f",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.52.41"
        },
        "Moid": "6501db4c76752d3901eb3851",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            }
        ],
        "DeviceMoId": "6501db456f726131016b7aea",
        "Name": "FI-ucsb1-eu-spdc-2-1",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501FB",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": "6501db4b76752d3901eb37c1",
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Blade Server",
                "Model": "UCSB-B200-M5",
                "Vendor": "Cisco Systems Inc",
                "Serial": "FLM241501FB",
                "Pid": "UCSB-B200-M5",
                "ChassisMoid": "6501db4b76752d3901eb37c1",
                "ServerType": "Blade",
                "ServerPid": "UCSB-B200-M5",
                "ServerSerial": "FLM241501FB"
            }
        ],
        "InventoryServerPid": "UCSB-B200-M5",
        "InventoryServerSerial": "FLM241501FB",
        "Groups": "test,power,ucsm",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.41",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.5",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "TunneledKvm": false
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [],
        "ManagementIp": "10.58.52.41",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "6501db456f726131016b7aea",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2023-09-13T15:54:45.974Z",
            "PlatformType": "UCSFI",
            "ConnectorVersion": "1.0.11-4665",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "10.0.169.80",
            "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3813",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4c76752d3901eb3813"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3864",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4c76752d3901eb3864"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4b76752d3901eb37c1",
                    "ObjectType": "equipment.Chassis",
                    "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                }
            ],
            "AssetTag": "",
            "AvailableMemory": 524288,
            "BiosBootmode": null,
            "BiosPostComplete": false,
            "BiosTokenSettings": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb383d",
                "ObjectType": "bios.TokenSettings",
                "link": "https://www.intersight.com/api/v1/bios/TokenSettings/6501db4c76752d3901eb383d"
            },
            "BiosUnits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4d76752d3901eb39db",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/6501db4d76752d3901eb39db"
                }
            ],
            "BiosVfSelectMemoryRasConfiguration": null,
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4d76752d3901eb39a7",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/6501db4d76752d3901eb39a7"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb3890",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/6501db4c76752d3901eb3890"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": null,
            "BootDeviceBootmode": null,
            "BootHddDevices": [],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [],
            "ChassisId": "2",
            "ClassId": "compute.Blade",
            "ComputePersonality": [],
            "CreateTime": "2023-09-13T15:54:52.147Z",
            "DeviceMoId": "6501db456f726131016b7aea",
            "Dn": "sys/chassis-2/blade-2",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "EquipmentChassis": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "EquipmentIoExpanders": [],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb38d5",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6501db4c76752d3901eb38d5"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.42",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-2/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.6",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-2/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4c76752d3901eb3803",
                        "ObjectType": "compute.Blade",
                        "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3803"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4b76752d3901eb37c1",
                        "ObjectType": "equipment.Chassis",
                        "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3803",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3803"
                },
                "ComputeRackUnit": null,
                "CreateTime": "2023-09-13T15:54:52.157Z",
                "DeviceMoId": "6501db456f726131016b7aea",
                "Dn": "sys/chassis-2/blade-2/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2023-11-25T02:20:09.633Z",
                "Moid": "6501db4c76752d3901eb380f",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3803",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3803"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aea",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/6501db456f726131016b7aea"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "UCSM",
            "MemoryArrays": [],
            "MemorySpeed": "2666",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.52.42, 10.58.26.6",
            "ModTime": "2023-12-02T15:17:46.9Z",
            "Model": "UCSB-B200-M5",
            "Moid": "6501db4c76752d3901eb3803",
            "Name": "FI-ucsb1-eu-spdc-2-2",
            "NumAdaptors": 2,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 8,
            "NumFcHostInterfaces": 0,
            "NumThreads": 80,
            "ObjectType": "compute.Blade",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "ok",
            "Operability": "operable",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "6501db456f726131016b7aea"
            ],
            "Parent": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3811",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/6501db4c76752d3901eb3811"
                }
            ],
            "PciNodes": [],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "UCSFI",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 13,
                "AppPartitionNumber": 84,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2023-09-13T15:54:45.974Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aed",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aed"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aee",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aee"
                    }
                ],
                "ConnectionId": "d1b367932349a7337fca45793620279e:848e760a-bf08-40ac-a7b2-cfc679df0eea",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
                "ConnectorVersion": "1.0.11-4665",
                "CreateTime": "2023-09-13T15:54:45.905Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7ad3",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/6501db456f726131016b7ad3"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aeb",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/6501db456f726131016b7aeb"
                },
                "DeviceExternalIpAddress": "10.0.169.80",
                "DeviceHostname": [
                    "FI-ucsb1-eu-spdc"
                ],
                "DeviceIpAddress": [
                    "10.58.24.17",
                    "10.58.24.18",
                    "10.58.24.19"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T19:41:43.284Z",
                "Moid": "6501db456f726131016b7aea",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "ParentConnection": null,
                "ParentSignature": null,
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCS-FI-6454"
                ],
                "PlatformType": "UCSFI",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqLWPrQ0XQyasWeQGlBDc\nwFDK5hBWFYE/sEijwVNCuEozwSy1p3BwNPuScU7MhMrTn33RvQktqzAMe6DnXV5f\nPRJ3iVs6syKoIVXMS6CLLur4f5c5B6aI906fqBJpsW9K9XVMCwIaFy539F8mJEz8\nez5NUrYPX3D0TeNQryUxWYUE7uejdjj+7Ukb1Kg3cTRRjmQwdSlB6NOFDsEfcC05\nSTf7B4J/bk1IahdllHTOvLz4BD8t7/6U/kCzf68nuhOk25//pMUcr0xTR6ltcW0R\n4Fc5hE6giEZKgTUiL7nDZhl2pibOKGfNvZGyXXYeVqp4BS5bBFD//GZmDf0Clm8/\n0wIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "FDO241604GJ",
                    "FDO241604KU"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7af4",
                    "ObjectType": "asset.Target",
                    "link": "https://www.intersight.com/api/v1/asset/Targets/6501db456f726131016b7af4"
                },
                "Vendor": "Cisco Systems, Inc."
            },
            "Revision": "0",
            "Rn": "",
            "ScaledMode": "none",
            "Serial": "FLM24140BJB",
            "ServiceProfile": "org-root/org-EU-SPN/ls-esx52-eu-spdc",
            "SharedScope": "",
            "SlotId": 2,
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb37fc",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/6501db4c76752d3901eb37fc"
            },
            "TotalMemory": 524288,
            "TunneledKvm": false,
            "UserLabel": "",
            "Uuid": "315220a5-2121-4e5b-0101-e1dc0000011f",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.52.42"
        },
        "Moid": "6501db4c76752d3901eb3803",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            }
        ],
        "DeviceMoId": "6501db456f726131016b7aea",
        "Name": "FI-ucsb1-eu-spdc-2-2",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140BJB",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": "6501db4b76752d3901eb37c1",
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Blade Server",
                "Model": "UCSB-B200-M5",
                "Vendor": "Cisco Systems Inc",
                "Serial": "FLM24140BJB",
                "Pid": "UCSB-B200-M5",
                "ChassisMoid": "6501db4b76752d3901eb37c1",
                "ServerType": "Blade",
                "ServerPid": "UCSB-B200-M5",
                "ServerSerial": "FLM24140BJB"
            }
        ],
        "InventoryServerPid": "UCSB-B200-M5",
        "InventoryServerSerial": "FLM24140BJB",
        "Groups": "test,power,ucsm",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.42",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-2/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.6",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-2/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "TunneledKvm": false
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [],
        "ManagementIp": "10.58.52.42",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "6501db456f726131016b7aea",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2023-09-13T15:54:45.974Z",
            "PlatformType": "UCSFI",
            "ConnectorVersion": "1.0.11-4665",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "10.0.169.80",
            "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4d76752d3901eb3972",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4d76752d3901eb3972"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4f76752d3901eb3c71",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4f76752d3901eb3c71"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4b76752d3901eb37c1",
                    "ObjectType": "equipment.Chassis",
                    "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                }
            ],
            "AssetTag": "",
            "AvailableMemory": 524288,
            "BiosBootmode": null,
            "BiosPostComplete": false,
            "BiosTokenSettings": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4d76752d3901eb3995",
                "ObjectType": "bios.TokenSettings",
                "link": "https://www.intersight.com/api/v1/bios/TokenSettings/6501db4d76752d3901eb3995"
            },
            "BiosUnits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3892",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/6501db4c76752d3901eb3892"
                }
            ],
            "BiosVfSelectMemoryRasConfiguration": null,
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4f76752d3901eb3cd0",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/6501db4f76752d3901eb3cd0"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb38a9",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/6501db4c76752d3901eb38a9"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": null,
            "BootDeviceBootmode": null,
            "BootHddDevices": [],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [],
            "ChassisId": "2",
            "ClassId": "compute.Blade",
            "ComputePersonality": [],
            "CreateTime": "2023-09-13T15:54:52.38Z",
            "DeviceMoId": "6501db456f726131016b7aea",
            "Dn": "sys/chassis-2/blade-3",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "EquipmentChassis": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "EquipmentIoExpanders": [],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4f76752d3901eb3cda",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6501db4f76752d3901eb3cda"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.43",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-3/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.0",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.7",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-3/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4c76752d3901eb387e",
                        "ObjectType": "compute.Blade",
                        "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb387e"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4b76752d3901eb37c1",
                        "ObjectType": "equipment.Chassis",
                        "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb387e",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb387e"
                },
                "ComputeRackUnit": null,
                "CreateTime": "2023-09-13T15:54:54.844Z",
                "DeviceMoId": "6501db456f726131016b7aea",
                "Dn": "sys/chassis-2/blade-3/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2023-09-13T15:54:55.044Z",
                "Moid": "6501db4e76752d3901eb3bf4",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb387e",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb387e"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aea",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/6501db456f726131016b7aea"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "UCSM",
            "MemoryArrays": [],
            "MemorySpeed": "2666",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.52.43, 10.58.26.7",
            "ModTime": "2023-10-26T16:51:52.143Z",
            "Model": "UCSB-B200-M5",
            "Moid": "6501db4c76752d3901eb387e",
            "Name": "FI-ucsb1-eu-spdc-2-3",
            "NumAdaptors": 2,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 8,
            "NumFcHostInterfaces": 0,
            "NumThreads": 80,
            "ObjectType": "compute.Blade",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "ok",
            "Operability": "operable",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "6501db456f726131016b7aea"
            ],
            "Parent": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4e76752d3901eb3af8",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/6501db4e76752d3901eb3af8"
                }
            ],
            "PciNodes": [],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "UCSFI",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 13,
                "AppPartitionNumber": 84,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2023-09-13T15:54:45.974Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aed",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aed"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aee",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aee"
                    }
                ],
                "ConnectionId": "d1b367932349a7337fca45793620279e:848e760a-bf08-40ac-a7b2-cfc679df0eea",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
                "ConnectorVersion": "1.0.11-4665",
                "CreateTime": "2023-09-13T15:54:45.905Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7ad3",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/6501db456f726131016b7ad3"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aeb",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/6501db456f726131016b7aeb"
                },
                "DeviceExternalIpAddress": "10.0.169.80",
                "DeviceHostname": [
                    "FI-ucsb1-eu-spdc"
                ],
                "DeviceIpAddress": [
                    "10.58.24.17",
                    "10.58.24.18",
                    "10.58.24.19"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T19:41:43.284Z",
                "Moid": "6501db456f726131016b7aea",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "ParentConnection": null,
                "ParentSignature": null,
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCS-FI-6454"
                ],
                "PlatformType": "UCSFI",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqLWPrQ0XQyasWeQGlBDc\nwFDK5hBWFYE/sEijwVNCuEozwSy1p3BwNPuScU7MhMrTn33RvQktqzAMe6DnXV5f\nPRJ3iVs6syKoIVXMS6CLLur4f5c5B6aI906fqBJpsW9K9XVMCwIaFy539F8mJEz8\nez5NUrYPX3D0TeNQryUxWYUE7uejdjj+7Ukb1Kg3cTRRjmQwdSlB6NOFDsEfcC05\nSTf7B4J/bk1IahdllHTOvLz4BD8t7/6U/kCzf68nuhOk25//pMUcr0xTR6ltcW0R\n4Fc5hE6giEZKgTUiL7nDZhl2pibOKGfNvZGyXXYeVqp4BS5bBFD//GZmDf0Clm8/\n0wIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "FDO241604GJ",
                    "FDO241604KU"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7af4",
                    "ObjectType": "asset.Target",
                    "link": "https://www.intersight.com/api/v1/asset/Targets/6501db456f726131016b7af4"
                },
                "Vendor": "Cisco Systems, Inc."
            },
            "Revision": "0",
            "Rn": "",
            "ScaledMode": "none",
            "Serial": "FLM241501CT",
            "ServiceProfile": "org-root/org-EU-SPN/ls-esx53-eu-spdc",
            "SharedScope": "",
            "SlotId": 3,
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb37fc",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/6501db4c76752d3901eb37fc"
            },
            "TotalMemory": 524288,
            "TunneledKvm": false,
            "UserLabel": "",
            "Uuid": "315220a5-2121-4e5b-0101-e1dc0000014e",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.52.43"
        },
        "Moid": "6501db4c76752d3901eb387e",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            }
        ],
        "DeviceMoId": "6501db456f726131016b7aea",
        "Name": "FI-ucsb1-eu-spdc-2-3",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501CT",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": "6501db4b76752d3901eb37c1",
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Blade Server",
                "Model": "UCSB-B200-M5",
                "Vendor": "Cisco Systems Inc",
                "Serial": "FLM241501CT",
                "Pid": "UCSB-B200-M5",
                "ChassisMoid": "6501db4b76752d3901eb37c1",
                "ServerType": "Blade",
                "ServerPid": "UCSB-B200-M5",
                "ServerSerial": "FLM241501CT"
            }
        ],
        "InventoryServerPid": "UCSB-B200-M5",
        "InventoryServerSerial": "FLM241501CT",
        "Groups": "test,power,ucsm",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.43",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-3/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.0",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.7",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-3/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "TunneledKvm": false
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [],
        "ManagementIp": "10.58.52.43",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "6501db456f726131016b7aea",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2023-09-13T15:54:45.974Z",
            "PlatformType": "UCSFI",
            "ConnectorVersion": "1.0.11-4665",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "10.0.169.80",
            "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G",
            "FlagManagement": ":GY",
            "FlagWorkflow": ":"
        },
        "StateEnabled": true,
        "IntersightObject": {
            "AccountMoid": "5be4b2ce67626c6d661ca38d",
            "Adapters": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb381b",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4c76752d3901eb381b"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4d76752d3901eb3976",
                    "ObjectType": "adapter.Unit",
                    "link": "https://www.intersight.com/api/v1/adapter/Units/6501db4d76752d3901eb3976"
                }
            ],
            "AdminPowerState": "policy",
            "AlarmSummary": {
                "ClassId": "compute.AlarmSummary",
                "Critical": 0,
                "Health": "Healthy",
                "Info": 0,
                "ObjectType": "compute.AlarmSummary",
                "Suppressed": false,
                "SuppressedCritical": 0,
                "SuppressedInfo": 0,
                "SuppressedWarning": 0,
                "Warning": 0
            },
            "Alerts": [],
            "Ancestors": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4b76752d3901eb37c1",
                    "ObjectType": "equipment.Chassis",
                    "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                }
            ],
            "AssetTag": "",
            "AvailableMemory": 524288,
            "BiosBootmode": null,
            "BiosPostComplete": false,
            "BiosTokenSettings": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb3841",
                "ObjectType": "bios.TokenSettings",
                "link": "https://www.intersight.com/api/v1/bios/TokenSettings/6501db4c76752d3901eb3841"
            },
            "BiosUnits": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4e76752d3901eb3ac3",
                    "ObjectType": "bios.Unit",
                    "link": "https://www.intersight.com/api/v1/bios/Units/6501db4e76752d3901eb3ac3"
                }
            ],
            "BiosVfSelectMemoryRasConfiguration": null,
            "Bmc": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb382d",
                "ObjectType": "management.Controller",
                "link": "https://www.intersight.com/api/v1/management/Controllers/6501db4c76752d3901eb382d"
            },
            "Board": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb381d",
                "ObjectType": "compute.Board",
                "link": "https://www.intersight.com/api/v1/compute/Boards/6501db4c76752d3901eb381d"
            },
            "BootCddDevices": [],
            "BootDeviceBootSecurity": null,
            "BootDeviceBootmode": null,
            "BootHddDevices": [],
            "BootIscsiDevices": [],
            "BootNvmeDevices": [],
            "BootPchStorageDevices": [],
            "BootPxeDevices": [],
            "BootSanDevices": [],
            "BootSdDevices": [],
            "BootUefiShellDevices": [],
            "BootUsbDevices": [],
            "BootVmediaDevices": [],
            "ChassisId": "2",
            "ClassId": "compute.Blade",
            "ComputePersonality": [],
            "CreateTime": "2023-09-13T15:54:52.185Z",
            "DeviceMoId": "6501db456f726131016b7aea",
            "Dn": "sys/chassis-2/blade-4",
            "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
            "EquipmentChassis": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "EquipmentIoExpanders": [],
            "FaultSummary": 0,
            "FrontPanelLockState": "Unlock",
            "GenericInventoryHolders": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb382f",
                    "ObjectType": "inventory.GenericInventoryHolder",
                    "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6501db4c76752d3901eb382f"
                }
            ],
            "GraphicsCards": [],
            "HardwareUuid": "",
            "InventoryDeviceInfo": null,
            "IsUpgraded": false,
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.44",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-4/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.8",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-4/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "Lifecycle": "None",
            "LocatorLed": {
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4c76752d3901eb3817",
                        "ObjectType": "compute.Blade",
                        "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3817"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db4b76752d3901eb37c1",
                        "ObjectType": "equipment.Chassis",
                        "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
                    }
                ],
                "ClassId": "equipment.LocatorLed",
                "Color": "unknown",
                "ComputeBlade": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3817",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3817"
                },
                "ComputeRackUnit": null,
                "CreateTime": "2023-09-13T15:54:52.227Z",
                "DeviceMoId": "6501db456f726131016b7aea",
                "Dn": "sys/chassis-2/blade-4/locator-led",
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "EquipmentChassis": null,
                "EquipmentFex": null,
                "InventoryDeviceInfo": null,
                "ModTime": "2023-09-13T15:54:52.654Z",
                "Moid": "6501db4c76752d3901eb382b",
                "NetworkElement": null,
                "ObjectType": "equipment.LocatorLed",
                "OperState": "off",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "Parent": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4c76752d3901eb3817",
                    "ObjectType": "compute.Blade",
                    "link": "https://www.intersight.com/api/v1/compute/Blades/6501db4c76752d3901eb3817"
                },
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "RegisteredDevice": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aea",
                    "ObjectType": "asset.DeviceRegistration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/6501db456f726131016b7aea"
                },
                "Rn": "",
                "SharedScope": "",
                "StoragePhysicalDisk": null,
                "Tags": []
            },
            "ManagementMode": "UCSM",
            "MemoryArrays": [],
            "MemorySpeed": "2666",
            "MgmtIdentity": null,
            "MgmtIpAddress": "10.58.52.44, 10.58.26.8",
            "ModTime": "2023-10-26T16:51:51.89Z",
            "Model": "UCSB-B200-M5",
            "Moid": "6501db4c76752d3901eb3817",
            "Name": "FI-ucsb1-eu-spdc-2-4",
            "NumAdaptors": 2,
            "NumCpuCores": 40,
            "NumCpuCoresEnabled": 40,
            "NumCpus": 2,
            "NumEthHostInterfaces": 8,
            "NumFcHostInterfaces": 0,
            "NumThreads": 80,
            "ObjectType": "compute.Blade",
            "OperPowerState": "on",
            "OperReason": [],
            "OperState": "ok",
            "Operability": "operable",
            "Owners": [
                "5be4b2ce67626c6d661ca38d",
                "6501db456f726131016b7aea"
            ],
            "Parent": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            },
            "PciDevices": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db4d76752d3901eb3961",
                    "ObjectType": "pci.Device",
                    "link": "https://www.intersight.com/api/v1/pci/Devices/6501db4d76752d3901eb3961"
                }
            ],
            "PciNodes": [],
            "PermissionResources": [
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "5dee1d736972652d321d26b5",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "625706a06972652d3202a8f9",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                },
                {
                    "ClassId": "mo.MoRef",
                    "Moid": "6242d1016972652d32eda017",
                    "ObjectType": "organization.Organization",
                    "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                }
            ],
            "PlatformType": "UCSFI",
            "Presence": "equipped",
            "PreviousFru": null,
            "Processors": [],
            "RegisteredDevice": {
                "Account": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca38d",
                    "ObjectType": "iam.Account",
                    "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
                },
                "AccountMoid": "5be4b2ce67626c6d661ca38d",
                "Ancestors": [],
                "ApiVersion": 13,
                "AppPartitionNumber": 84,
                "ClaimedByUser": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4ab2367626c6d661c1514",
                    "ObjectType": "iam.User",
                    "link": "https://www.intersight.com/api/v1/iam/Users/5be4ab2367626c6d661c1514"
                },
                "ClaimedByUserName": "ttrabatt@cisco.com",
                "ClaimedTime": "2023-09-13T15:54:45.974Z",
                "ClassId": "asset.DeviceRegistration",
                "ClusterMembers": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aed",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aed"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6501db456f726131016b7aee",
                        "ObjectType": "asset.ClusterMember",
                        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/6501db456f726131016b7aee"
                    }
                ],
                "ConnectionId": "d1b367932349a7337fca45793620279e:848e760a-bf08-40ac-a7b2-cfc679df0eea",
                "ConnectionReason": "",
                "ConnectionStatus": "Connected",
                "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
                "ConnectorVersion": "1.0.11-4665",
                "CreateTime": "2023-09-13T15:54:45.905Z",
                "DeviceClaim": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7ad3",
                    "ObjectType": "asset.DeviceClaim",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/6501db456f726131016b7ad3"
                },
                "DeviceConfiguration": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7aeb",
                    "ObjectType": "asset.DeviceConfiguration",
                    "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/6501db456f726131016b7aeb"
                },
                "DeviceExternalIpAddress": "10.0.169.80",
                "DeviceHostname": [
                    "FI-ucsb1-eu-spdc"
                ],
                "DeviceIpAddress": [
                    "10.58.24.17",
                    "10.58.24.18",
                    "10.58.24.19"
                ],
                "DomainGroup": {
                    "ClassId": "mo.MoRef",
                    "Moid": "5be4b2ce67626c6d661ca39c",
                    "ObjectType": "iam.DomainGroup",
                    "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5be4b2ce67626c6d661ca39c"
                },
                "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
                "ExecutionMode": "Normal",
                "ModTime": "2023-12-01T19:41:43.284Z",
                "Moid": "6501db456f726131016b7aea",
                "ObjectType": "asset.DeviceRegistration",
                "Owners": [
                    "5be4b2ce67626c6d661ca38d",
                    "6501db456f726131016b7aea"
                ],
                "ParentConnection": null,
                "ParentSignature": null,
                "PermissionResources": [
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "5dee1d736972652d321d26b5",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "625706a06972652d3202a8f9",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
                    },
                    {
                        "ClassId": "mo.MoRef",
                        "Moid": "6242d1016972652d32eda017",
                        "ObjectType": "organization.Organization",
                        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
                    }
                ],
                "Pid": [
                    "UCS-FI-6454"
                ],
                "PlatformType": "UCSFI",
                "ProxyApp": "astro",
                "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqLWPrQ0XQyasWeQGlBDc\nwFDK5hBWFYE/sEijwVNCuEozwSy1p3BwNPuScU7MhMrTn33RvQktqzAMe6DnXV5f\nPRJ3iVs6syKoIVXMS6CLLur4f5c5B6aI906fqBJpsW9K9XVMCwIaFy539F8mJEz8\nez5NUrYPX3D0TeNQryUxWYUE7uejdjj+7Ukb1Kg3cTRRjmQwdSlB6NOFDsEfcC05\nSTf7B4J/bk1IahdllHTOvLz4BD8t7/6U/kCzf68nuhOk25//pMUcr0xTR6ltcW0R\n4Fc5hE6giEZKgTUiL7nDZhl2pibOKGfNvZGyXXYeVqp4BS5bBFD//GZmDf0Clm8/\n0wIDAQAB\n-----END RSA PUBLIC KEY-----\n",
                "ReadOnly": false,
                "SecurityToken": null,
                "Serial": [
                    "FDO241604GJ",
                    "FDO241604KU"
                ],
                "SharedScope": "",
                "Tags": [],
                "Target": {
                    "ClassId": "mo.MoRef",
                    "Moid": "6501db456f726131016b7af4",
                    "ObjectType": "asset.Target",
                    "link": "https://www.intersight.com/api/v1/asset/Targets/6501db456f726131016b7af4"
                },
                "Vendor": "Cisco Systems, Inc."
            },
            "Revision": "0",
            "Rn": "",
            "ScaledMode": "none",
            "Serial": "FLM24140B0B",
            "ServiceProfile": "org-root/org-EU-SPN/ls-esx54-eu-spdc",
            "SharedScope": "",
            "SlotId": 4,
            "StorageControllers": [],
            "StorageEnclosures": [],
            "Tags": [
                {
                    "Key": "Intersight.LicenseTier",
                    "Value": "Advantage"
                }
            ],
            "TopSystem": {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4c76752d3901eb37fc",
                "ObjectType": "top.System",
                "link": "https://www.intersight.com/api/v1/top/Systems/6501db4c76752d3901eb37fc"
            },
            "TotalMemory": 524288,
            "TunneledKvm": false,
            "UserLabel": "",
            "Uuid": "315220a5-2121-4e5b-0101-e1dc0000015e",
            "Vendor": "Cisco Systems Inc",
            "Vmedia": null,
            "ManagementIp": "10.58.52.44"
        },
        "Moid": "6501db4c76752d3901eb3817",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6501db4b76752d3901eb37c1",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/6501db4b76752d3901eb37c1"
            }
        ],
        "DeviceMoId": "6501db456f726131016b7aea",
        "Name": "FI-ucsb1-eu-spdc-2-4",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140B0B",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "Vendor": "Cisco Systems Inc",
        "Cpu": "2S 40C 80T",
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ChassisMoid": "6501db4b76752d3901eb37c1",
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "Connected": true,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Server",
                "Name": "Blade Server",
                "Model": "UCSB-B200-M5",
                "Vendor": "Cisco Systems Inc",
                "Serial": "FLM24140B0B",
                "Pid": "UCSB-B200-M5",
                "ChassisMoid": "6501db4b76752d3901eb37c1",
                "ServerType": "Blade",
                "ServerPid": "UCSB-B200-M5",
                "ServerSerial": "FLM24140B0B"
            }
        ],
        "InventoryServerPid": "UCSB-B200-M5",
        "InventoryServerSerial": "FLM24140B0B",
        "Groups": "test,power,ucsm",
        "AlarmSummary": {
            "__Output": {
                "Critical": "Red",
                "Warning": "Yellow",
                "Info": "Blue",
                "Cleared": "Green"
            },
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "KvmInfo": {
            "KvmIpAddresses": [
                {
                    "Address": "10.58.52.44",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.52.62",
                    "Dn": "sys/chassis-2/blade-4/mgmt/ipv4-static-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.224",
                    "Type": "VnicIpV4StaticAddr"
                },
                {
                    "Address": "10.58.26.8",
                    "Category": "Equipment",
                    "ClassId": "compute.IpAddress",
                    "DefaultGateway": "10.58.26.62",
                    "Dn": "sys/chassis-2/blade-4/mgmt/ipv4-prof-addr",
                    "HttpPort": 80,
                    "HttpsPort": 443,
                    "KvmPort": 2068,
                    "KvmVlan": 0,
                    "Name": "Outband",
                    "ObjectType": "compute.IpAddress",
                    "Subnet": "255.255.255.192",
                    "Type": "VnicIpV4ProfDerivedAddr"
                }
            ],
            "KvmServerStateEnabled": false,
            "KvmVendor": "",
            "TunneledKvm": false
        },
        "LicenseInfo": {
            "Tier": "Advantage"
        },
        "Tags": [],
        "ManagementIp": "10.58.52.44",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "ConnectorInfo": {
            "__Output": {
                "ConnectionStatus": "Green"
            },
            "Moid": "6501db456f726131016b7aea",
            "ClaimedByUserName": "ttrabatt@cisco.com",
            "ClaimedTime": "2023-09-13T15:54:45.974Z",
            "PlatformType": "UCSFI",
            "ConnectorVersion": "1.0.11-4665",
            "ConnectionStatus": "Connected",
            "DeviceExternalIpAddress": "10.0.169.80",
            "ConnectionStatusLastChangeTime": "2023-12-01T19:41:43.272Z",
            "Connected": true
        },
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    }
]
```

Developer output

```
# iserver get server --group test -o json

{
    "duration": 8882,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6679
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
        "lines": 39
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:30:43.404456	True	3230	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:30:45.264318	True	1854	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:30:46.942839	True	1595	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)