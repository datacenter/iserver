# Redfish Oem Resources

Vendor | Model
--- | ---
HPE | vServer

```
# iserver get redfish endpoint
    --cache hpe-proliant-dl360-gen10-plus-vyrbx9uj4s-2.55-on
    --type hpe
    --ip 10.58.24.211
    --port 49153
    --username administrator
    --password ******
    --oem
    --deep
    --max 0

/redfish/v1/
------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOServiceExt.HpeiLOServiceExt",
            "@odata.type": "#HpeiLOServiceExt.v2_3_0.HpeiLOServiceExt",
            "Links": {
                "ResourceDirectory": {
                    "@odata.id": "/redfish/v1/ResourceDirectory"
                }
            },
            "Manager": [
                {
                    "DefaultLanguage": "en",
                    "FQDN": null,
                    "HostName": "ILOVYRBX9UJ4S",
                    "IPManager": {
                        "BiosManaged": false,
                        "FirmwareManaged": false,
                        "ManagerProductName": "HPE OneView",
                        "ManagerType": "OneView",
                        "ManagerUrl": {
                            "xref": "https://10.29.152.124"
                        },
                        "ManagerVersion": "6.60.00",
                        "Name": "Management Console Information",
                        "OvManagesiLOIP": false,
                        "SppVersion": null,
                        "StorageManaged": false,
                        "Type": "HPQ_iLOManagerDescriptor/1.1.0",
                        "iLOManaged": true,
                        "type": "IpManagerBlob"
                    },
                    "Languages": [
                        {
                            "Language": "en",
                            "TranslationName": "English",
                            "Version": "2.55"
                        }
                    ],
                    "ManagerFirmwareVersion": "2.55",
                    "ManagerType": "iLO 5",
                    "Status": {
                        "Health": "OK"
                    }
                }
            ],
            "Moniker": {
                "ADVLIC": "iLO Advanced",
                "BMC": "iLO",
                "BSYS": "BladeSystem",
                "CLASS": "Baseboard Management Controller",
                "FEDGRP": "DEFAULT",
                "IPROV": "Intelligent Provisioning",
                "PRODABR": "iLO",
                "PRODFAM": "Integrated Lights-Out",
                "PRODGEN": "iLO 5",
                "PRODNAM": "Integrated Lights-Out 5",
                "PRODTAG": "HPE iLO 5",
                "STDLIC": "iLO Standard",
                "SUMABR": "SUM",
                "SUMGR": "Smart Update Manager",
                "SYSFAM": "ProLiant",
                "SYSMGMT": "Enhanced",
                "VENDABR": "HPE",
                "VENDNAM": "Hewlett-Packard Enterprise",
                "VNIC": "Virtual NIC",
                "WWW": "www.hpe.com",
                "WWWAHSV": "www.hpe.com/servers/ahsv",
                "WWWBMC": "www.hpe.com/servers/ilo",
                "WWWDOC": "www.hpe.com/support/ilo-docs",
                "WWWERS": "www.hpe.com/services/getconnected",
                "WWWGLIS": "www.hpe.com/glis",
                "WWWINFOSIGHT": "infosight.hpe.com",
                "WWWIOL": "www.hpe.com/info/insightonline",
                "WWWLIC": "www.hpe.com/info/ilo",
                "WWWLML": "www.hpe.com/support",
                "WWWPASS": "www.hpe.com/support/hpesc",
                "WWWPRV": "www.hpe.com/info/privacy",
                "WWWQSPEC": "www.hpe.com/info/qs",
                "WWWRESTDOC": "www.hpe.com/us/en/servers/restful-api.html",
                "WWWSUP": "www.hpe.com/support/ilo5",
                "WWWSWLIC": "www.hpe.com/software/SWLicensing"
            },
            "Sessions": {
                "CertCommonName": "ILOVYRBX9UJ4S",
                "CertificateLoginEnabled": false,
                "KerberosEnabled": false,
                "LDAPAuthLicenced": true,
                "LDAPEnabled": false,
                "LocalLoginEnabled": true,
                "LoginFailureDelay": 0,
                "LoginHint": {
                    "Hint": "POST to /Sessions to login using the following JSON object:",
                    "HintPOSTData": {
                        "Password": "password",
                        "UserName": "username"
                    }
                },
                "SecurityOverride": false,
                "ServerName": "VYRBX9UJ4S.cisco.lab"
            },
            "System": [
                {
                    "Status": {
                        "Health": "OK"
                    }
                }
            ],
            "Time": "2022-08-03T17:11:28Z"
        }
    }
}

/redfish/v1/AccountService
--------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOAccountService.HpeiLOAccountService",
            "@odata.id": "/redfish/v1/AccountService",
            "@odata.type": "#HpeiLOAccountService.v2_3_0.HpeiLOAccountService",
            "Actions": {
                "#HpeiLOAccountService.ImportKerberosKeytab": {
                    "target": "/redfish/v1/AccountService/Actions/Oem/Hpe/HpeiLOAccountService.ImportKerberosKeytab"
                }
            },
            "AuthFailureDelayTimeSeconds": 10,
            "AuthFailureLoggingThreshold": 3,
            "AuthFailuresBeforeDelay": 1,
            "DefaultPassword": null,
            "DefaultUserName": null,
            "DirectorySettings": {
                "LdapAuthenticationMode": "Disabled",
                "LdapCaCertificateLoaded": false,
                "LdapCaCertificates": {
                    "@odata.id": "/redfish/v1/AccountService/ExternalAccountProviders/LDAP/Certificates"
                },
                "LdapServerPort": 636
            },
            "DirectoryTest": {
                "@odata.id": "/redfish/v1/AccountService/DirectoryTest"
            },
            "EnforcePasswordComplexity": false,
            "Id": "AccountService",
            "KerberosSettings": {
                "KDCServerPort": 88,
                "KerberosRealm": ""
            },
            "MinPasswordLength": 8
        }
    }
}

/redfish/v1/AccountService/Accounts/1
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOAccount.HpeiLOAccount",
            "@odata.type": "#HpeiLOAccount.v2_2_0.HpeiLOAccount",
            "LoginName": "Administrator",
            "Privileges": {
                "HostBIOSConfigPriv": true,
                "HostNICConfigPriv": true,
                "HostStorageConfigPriv": true,
                "LoginPriv": true,
                "RemoteConsolePriv": true,
                "SystemRecoveryConfigPriv": true,
                "UserConfigPriv": true,
                "VirtualMediaPriv": true,
                "VirtualPowerAndResetPriv": true,
                "iLOConfigPriv": true
            },
            "ServiceAccount": false
        }
    }
}

/redfish/v1/AccountService/Accounts/2
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOAccount.HpeiLOAccount",
            "@odata.type": "#HpeiLOAccount.v2_2_0.HpeiLOAccount",
            "LoginName": "engineer",
            "Privileges": {
                "HostBIOSConfigPriv": false,
                "HostNICConfigPriv": false,
                "HostStorageConfigPriv": false,
                "LoginPriv": true,
                "RemoteConsolePriv": false,
                "SystemRecoveryConfigPriv": false,
                "UserConfigPriv": false,
                "VirtualMediaPriv": false,
                "VirtualPowerAndResetPriv": false,
                "iLOConfigPriv": false
            },
            "ServiceAccount": false
        }
    }
}

/redfish/v1/AccountService/Accounts/3
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOAccount.HpeiLOAccount",
            "@odata.type": "#HpeiLOAccount.v2_2_0.HpeiLOAccount",
            "LoginName": "complab",
            "Privileges": {
                "HostBIOSConfigPriv": true,
                "HostNICConfigPriv": true,
                "HostStorageConfigPriv": true,
                "LoginPriv": true,
                "RemoteConsolePriv": true,
                "SystemRecoveryConfigPriv": false,
                "UserConfigPriv": true,
                "VirtualMediaPriv": true,
                "VirtualPowerAndResetPriv": true,
                "iLOConfigPriv": true
            },
            "ServiceAccount": false
        }
    }
}

/redfish/v1/AccountService/Accounts/4
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOAccount.HpeiLOAccount",
            "@odata.type": "#HpeiLOAccount.v2_2_0.HpeiLOAccount",
            "LoginName": "Admin Account for HPE OneView",
            "Privileges": {
                "HostBIOSConfigPriv": true,
                "HostNICConfigPriv": true,
                "HostStorageConfigPriv": true,
                "LoginPriv": true,
                "RemoteConsolePriv": true,
                "SystemRecoveryConfigPriv": false,
                "UserConfigPriv": true,
                "VirtualMediaPriv": true,
                "VirtualPowerAndResetPriv": true,
                "iLOConfigPriv": true
            },
            "ServiceAccount": false
        }
    }
}

/redfish/v1/AccountService/Roles/dirgroup9d4546a03a03bb977c03086a
-----------------------------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeDirectoryGroup.HpeDirectoryGroup",
            "@odata.type": "#HpeDirectoryGroup.v1_0_0.HpeDirectoryGroup",
            "GroupDn": "Authenticated Users",
            "GroupSid": "S-1-5-11"
        }
    }
}

/redfish/v1/AccountService/Roles/dirgroupb3d8954f6ebbe735764e9f7c
-----------------------------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeDirectoryGroup.HpeDirectoryGroup",
            "@odata.type": "#HpeDirectoryGroup.v1_0_0.HpeDirectoryGroup",
            "GroupDn": "Administrators",
            "GroupSid": ""
        }
    }
}

/redfish/v1/Chassis/1
---------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeServerChassis.HpeServerChassis",
            "@odata.type": "#HpeServerChassis.v2_3_1.HpeServerChassis",
            "Actions": {
                "#HpeServerChassis.DisableMCTPOnServer": {
                    "target": "/redfish/v1/Chassis/1/Actions/Oem/Hpe/HpeServerChassis.DisableMCTPOnServer"
                },
                "#HpeServerChassis.FactoryResetMCTP": {
                    "target": "/redfish/v1/Chassis/1/Actions/Oem/Hpe/HpeServerChassis.FactoryResetMCTP"
                }
            },
            "ElConfigOverride": false,
            "Firmware": {
                "PlatformDefinitionTable": {
                    "Current": {
                        "VersionString": "9.2.0 Build 35"
                    }
                },
                "PowerManagementController": {
                    "Current": {
                        "VersionString": "1.0.7"
                    }
                },
                "PowerManagementControllerBootloader": {
                    "Current": {
                        "Family": "25",
                        "VersionString": "1.1"
                    }
                },
                "SPSFirmwareVersionData": {
                    "Current": {
                        "VersionString": "4.4.4.53"
                    }
                },
                "SystemProgrammableLogicDevice": {
                    "Current": {
                        "VersionString": "0x15"
                    }
                }
            },
            "Links": {
                "Devices": {
                    "@odata.id": "/redfish/v1/Chassis/1/Devices"
                }
            },
            "MCTPEnabledOnServer": true,
            "SmartStorageBattery": [
                {
                    "ChargeLevelPercent": 99,
                    "FirmwareVersion": "0.70",
                    "Index": 1,
                    "MaximumCapWatts": 96,
                    "Model": "875241-B21",
                    "ProductName": "HPE Smart Storage Battery ",
                    "RemainingChargeTimeSeconds": 29,
                    "SerialNumber": "6WQXK0JWYF441K",
                    "SparePartNumber": "878643-001",
                    "Status": {
                        "Health": "OK",
                        "State": "Enabled"
                    }
                }
            ],
            "SystemMaintenanceSwitches": {
                "Sw1": "Off",
                "Sw10": "Off",
                "Sw11": "Off",
                "Sw12": "Off",
                "Sw2": "Off",
                "Sw3": "Off",
                "Sw4": "Off",
                "Sw5": "Off",
                "Sw6": "Off",
                "Sw7": "Off",
                "Sw8": "Off",
                "Sw9": "Off"
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeNetworkAdapterStatus.HpeNetworkAdapterStatus",
            "@odata.type": "#HpeNetworkAdapterStatus.v1_0_0.HpeNetworkAdapterStatus",
            "MemberContents": "AllDevices"
        }
    }
}

/redfish/v1/Chassis/1/Power
---------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpePowerMetricsExt.HpePowerMetricsExt",
            "@odata.type": "#HpePowerMetricsExt.v2_3_0.HpePowerMetricsExt",
            "BrownoutRecoveryEnabled": true,
            "HasCpuPowerMetering": true,
            "HasDimmPowerMetering": true,
            "HasGpuPowerMetering": false,
            "HasPowerMetering": true,
            "HighEfficiencyMode": "Balanced",
            "Links": {
                "FastPowerMeter": {
                    "@odata.id": "/redfish/v1/Chassis/1/Power/FastPowerMeter"
                },
                "FederatedGroupCapping": {
                    "@odata.id": "/redfish/v1/Chassis/1/Power/FederatedGroupCapping"
                },
                "PowerMeter": {
                    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerMeter"
                },
                "SlowPowerMeter": {
                    "@odata.id": "/redfish/v1/Chassis/1/Power/SlowPowerMeter"
                }
            },
            "MinimumSafelyAchievableCap": null,
            "MinimumSafelyAchievableCapValid": false,
            "SNMPPowerThresholdAlert": {
                "DurationInMin": 0,
                "ThresholdWatts": 0,
                "Trigger": "Disabled"
            }
        }
    }
}

/redfish/v1/Chassis/1/Thermal
-----------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeThermalExt.HpeThermalExt",
            "@odata.type": "#HpeThermalExt.v2_0_0.HpeThermalExt",
            "FanPercentMinimum": 0,
            "ThermalConfiguration": "OptimalCooling"
        }
    }
}

/redfish/v1/EventService
------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeEventService.HpeEventService",
            "@odata.id": "/redfish/v1/EventService",
            "@odata.type": "#HpeEventService.v2_1_0.HpeEventService",
            "Actions": {
                "#HpeEventService.ImportCACertificate": {
                    "target": "/redfish/v1/EventService/Actions/Oem/Hpe/HpeEventService.ImportCACertificate"
                }
            },
            "CACertificates": {
                "@odata.id": "/redfish/v1/EventService/CACertificates"
            },
            "Id": "EventService",
            "RequestedMaxEventsToQueueDefault": 3,
            "RetireOldEventInMinutesDefault": 10,
            "TTLCountDefault": 999999,
            "TTLUnitsDefault": "minutes"
        }
    }
}

/redfish/v1/EventService/Subscriptions/1
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeEventDestination.HpeEventDestination",
            "@odata.type": "#HpeEventDestination.v2_1_0.HpeEventDestination",
            "DeliveryRetryAttempts": 1440,
            "DeliveryRetryIntervalInSeconds": 60,
            "MutualAuthenticationEnabled": false,
            "RequestedMaxEventsToQueue": 64,
            "RetireOldEventInMinutes": 10
        }
    }
}

/redfish/v1/Managers/1
----------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLO.HpeiLO",
            "@odata.type": "#HpeiLO.v2_8_0.HpeiLO",
            "Actions": {
                "#HpeiLO.ClearHotKeys": {
                    "target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.ClearHotKeys"
                },
                "#HpeiLO.ClearRestApiState": {
                    "target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.ClearRestApiState"
                },
                "#HpeiLO.DisableiLOFunctionality": {
                    "target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.DisableiLOFunctionality"
                },
                "#HpeiLO.RequestFirmwareAndOsRecovery": {
                    "target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.RequestFirmwareAndOsRecovery"
                },
                "#HpeiLO.ResetToFactoryDefaults": {
                    "ResetType@Redfish.AllowableValues": [
                        "Default"
                    ],
                    "target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.ResetToFactoryDefaults"
                }
            },
            "ClearRestApiStatus": "DataPresent",
            "ConfigurationLimitations": "None",
            "ConfigurationSettings": "Current",
            "FederationConfig": {
                "IPv6MulticastScope": "Site",
                "MulticastAnnouncementInterval": 600,
                "MulticastDiscovery": "Enabled",
                "MulticastTimeToLive": 5,
                "iLOFederationManagement": "Enabled"
            },
            "Firmware": {
                "Current": {
                    "Date": "Oct 01 2021",
                    "DebugBuild": false,
                    "MajorVersion": 2,
                    "MinorVersion": 55,
                    "VersionString": "iLO 5 v2.55"
                }
            },
            "FrontPanelUSB": {
                "State": "Ready"
            },
            "IdleConnectionTimeoutMinutes": 30,
            "IntegratedRemoteConsole": {
                "HotKeys": [
                    {
                        "KeySequence": [
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE"
                        ],
                        "Name": "Ctrl-T"
                    },
                    {
                        "KeySequence": [
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE"
                        ],
                        "Name": "Ctrl-U"
                    },
                    {
                        "KeySequence": [
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE"
                        ],
                        "Name": "Ctrl-V"
                    },
                    {
                        "KeySequence": [
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE"
                        ],
                        "Name": "Ctrl-W"
                    },
                    {
                        "KeySequence": [
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE"
                        ],
                        "Name": "Ctrl-X"
                    },
                    {
                        "KeySequence": [
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE",
                            "NONE"
                        ],
                        "Name": "Ctrl-Y"
                    }
                ],
                "LockKey": {
                    "CustomKeySequence": [
                        "NONE",
                        "NONE",
                        "NONE",
                        "NONE",
                        "NONE"
                    ],
                    "LockOption": "Disabled"
                },
                "TrustedCertificateRequired": false
            },
            "License": {
                "LicenseKey": "XXXXX-XXXXX-XXXXX-XXXXX-MQ9LH",
                "LicenseString": "iLO Advanced",
                "LicenseType": "Perpetual"
            },
            "Links": {
                "ActiveHealthSystem": {
                    "@odata.id": "/redfish/v1/Managers/1/ActiveHealthSystem"
                },
                "BackupRestoreService": {
                    "@odata.id": "/redfish/v1/Managers/1/BackupRestoreService"
                },
                "DateTimeService": {
                    "@odata.id": "/redfish/v1/Managers/1/DateTime"
                },
                "EmbeddedMediaService": {
                    "@odata.id": "/redfish/v1/Managers/1/EmbeddedMedia"
                },
                "FederationDispatch": {
                    "extref": "/dispatch"
                },
                "FederationGroups": {
                    "@odata.id": "/redfish/v1/Managers/1/FederationGroups"
                },
                "FederationPeers": {
                    "@odata.id": "/redfish/v1/Managers/1/FederationPeers"
                },
                "GUIService": {
                    "@odata.id": "/redfish/v1/Managers/1/GUIService"
                },
                "LicenseService": {
                    "@odata.id": "/redfish/v1/Managers/1/LicenseService"
                },
                "RemoteSupport": {
                    "@odata.id": "/redfish/v1/Managers/1/RemoteSupportService"
                },
                "SNMPService": {
                    "@odata.id": "/redfish/v1/Managers/1/SnmpService"
                },
                "SecurityService": {
                    "@odata.id": "/redfish/v1/Managers/1/SecurityService"
                },
                "Thumbnail": {
                    "extref": "/images/thumbnail.bmp"
                },
                "VSPLogLocation": {
                    "extref": "/sol.log.gz"
                }
            },
            "PersistentMouseKeyboardEnabled": false,
            "PhysicalMonitorHealthStatusEnabled": true,
            "RIBCLEnabled": true,
            "RemoteConsoleThumbnailEnabled": true,
            "RequireHostAuthentication": false,
            "RequiredLoginForiLORBSU": false,
            "SerialCLISpeed": 9600,
            "SerialCLIStatus": "EnabledAuthReq",
            "SerialCLIUART": "Present",
            "VSPDlLoggingEnabled": false,
            "VSPLogDownloadEnabled": false,
            "VideoPresenceDetectOverride": true,
            "VideoPresenceDetectOverrideSupported": true,
            "VirtualNICEnabled": false,
            "WebGuiEnabled": true,
            "iLOFunctionalityEnabled": true,
            "iLOFunctionalityRequired": false,
            "iLOIPduringPOSTEnabled": true,
            "iLORBSUEnabled": true,
            "iLOSelfTestResults": [
                {
                    "Notes": "",
                    "SelfTestName": "NVRAMData",
                    "Status": "OK"
                },
                {
                    "Notes": "Controller firmware revision  2.11.00  ",
                    "SelfTestName": "EmbeddedFlash",
                    "Status": "OK"
                },
                {
                    "Notes": "",
                    "SelfTestName": "EEPROM",
                    "Status": "OK"
                },
                {
                    "Notes": "",
                    "SelfTestName": "HostRom",
                    "Status": "OK"
                },
                {
                    "Notes": "",
                    "SelfTestName": "SupportedHost",
                    "Status": "OK"
                },
                {
                    "Notes": "Version 1.0.7",
                    "SelfTestName": "PowerManagementController",
                    "Status": "Informational"
                },
                {
                    "Notes": "ProLiant DL360 Gen10 Plus System Programmable Logic Device 0x15",
                    "SelfTestName": "CPLDPAL0",
                    "Status": "Informational"
                },
                {
                    "Notes": "",
                    "SelfTestName": "ASICFuses",
                    "Status": "OK"
                }
            ],
            "iLOServicePort": {
                "MassStorageAuthenticationRequired": false,
                "USBEthernetAdaptersEnabled": true,
                "USBFlashDriveEnabled": true,
                "iLOServicePortEnabled": true
            }
        }
    }
}

/redfish/v1/Managers/1/BackupRestoreService/BackupFiles
-------------------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOBackupFilesInformation.HpeiLOBackupFilesInformation",
            "@odata.type": "#HpeiLOBackupFilesInformation.v1_0_0.HpeiLOBackupFilesInformation",
            "BackupFileCount": 0,
            "BackupFilesAllowed": 1
        }
    }
}

/redfish/v1/Managers/1/EthernetInterfaces/1
-------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOEthernetNetworkInterface.HpeiLOEthernetNetworkInterface",
            "@odata.type": "#HpeiLOEthernetNetworkInterface.v2_2_1.HpeiLOEthernetNetworkInterface",
            "ConfigurationSettings": "Current",
            "DHCPv4": {
                "ClientIdType": "Default",
                "Enabled": false,
                "UseDNSServers": false,
                "UseDomainName": false,
                "UseGateway": false,
                "UseNTPServers": false,
                "UseStaticRoutes": false,
                "UseWINSServers": false
            },
            "DHCPv6": {
                "StatefulModeEnabled": true,
                "StatelessModeEnabled": true,
                "UseDNSServers": true,
                "UseDomainName": true,
                "UseNTPServers": false,
                "UseRapidCommit": false
            },
            "DomainName": "",
            "HostName": "ILOVYRBX9UJ4S",
            "IPv4": {
                "DDNSRegistration": true,
                "DNSServers": [
                    "10.29.143.10",
                    "0.0.0.0",
                    "0.0.0.0"
                ],
                "StaticRoutes": [
                    {
                        "Destination": "0.0.0.0",
                        "Gateway": "0.0.0.0",
                        "SubnetMask": "0.0.0.0"
                    },
                    {
                        "Destination": "0.0.0.0",
                        "Gateway": "0.0.0.0",
                        "SubnetMask": "0.0.0.0"
                    },
                    {
                        "Destination": "0.0.0.0",
                        "Gateway": "0.0.0.0",
                        "SubnetMask": "0.0.0.0"
                    }
                ],
                "WINSRegistration": true,
                "WINSServers": [
                    "0.0.0.0",
                    "0.0.0.0"
                ]
            },
            "IPv6": {
                "DDNSRegistration": true,
                "DNSServers": [
                    "::",
                    "::",
                    "::"
                ],
                "SLAACEnabled": true,
                "StaticDefaultGateway": "::",
                "StaticRoutes": [
                    {
                        "Destination": "::",
                        "Gateway": "::",
                        "PrefixLength": null,
                        "Status": "Unknown"
                    },
                    {
                        "Destination": "::",
                        "Gateway": "::",
                        "PrefixLength": null,
                        "Status": "Unknown"
                    },
                    {
                        "Destination": "::",
                        "Gateway": "::",
                        "PrefixLength": null,
                        "Status": "Unknown"
                    }
                ]
            },
            "InterfaceType": "Dedicated",
            "NICEnabled": true,
            "NICSupportsIPv6": true,
            "PingGatewayOnStartup": true
        }
    }
}

/redfish/v1/Managers/1/EthernetInterfaces/2
-------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOEthernetNetworkInterface.HpeiLOEthernetNetworkInterface",
            "@odata.type": "#HpeiLOEthernetNetworkInterface.v2_2_1.HpeiLOEthernetNetworkInterface",
            "ConfigurationSettings": "Current",
            "DHCPv4": {
                "ClientIdType": "Default",
                "Enabled": true,
                "UseDNSServers": true,
                "UseDomainName": true,
                "UseGateway": true,
                "UseNTPServers": true,
                "UseStaticRoutes": true,
                "UseWINSServers": true
            },
            "DHCPv6": {
                "StatefulModeEnabled": true,
                "StatelessModeEnabled": true,
                "UseDNSServers": true,
                "UseDomainName": true,
                "UseNTPServers": true,
                "UseRapidCommit": false
            },
            "DomainName": "",
            "HostName": "ILOVYRBX9UJ4S",
            "IPv4": {
                "DDNSRegistration": true,
                "DNSServers": [
                    "0.0.0.0",
                    "0.0.0.0",
                    "0.0.0.0"
                ],
                "StaticRoutes": [
                    {
                        "Destination": "0.0.0.0",
                        "Gateway": "0.0.0.0",
                        "SubnetMask": "0.0.0.0"
                    },
                    {
                        "Destination": "0.0.0.0",
                        "Gateway": "0.0.0.0",
                        "SubnetMask": "0.0.0.0"
                    },
                    {
                        "Destination": "0.0.0.0",
                        "Gateway": "0.0.0.0",
                        "SubnetMask": "0.0.0.0"
                    }
                ],
                "WINSRegistration": true,
                "WINSServers": [
                    "0.0.0.0",
                    "0.0.0.0"
                ]
            },
            "IPv6": {
                "DDNSRegistration": true,
                "DNSServers": [
                    "::",
                    "::",
                    "::"
                ],
                "SLAACEnabled": true,
                "StaticDefaultGateway": "::",
                "StaticRoutes": [
                    {
                        "Destination": "::",
                        "Gateway": "::",
                        "PrefixLength": null,
                        "Status": "Unknown"
                    },
                    {
                        "Destination": "::",
                        "Gateway": "::",
                        "PrefixLength": null,
                        "Status": "Unknown"
                    },
                    {
                        "Destination": "::",
                        "Gateway": "::",
                        "PrefixLength": null,
                        "Status": "Unknown"
                    }
                ]
            },
            "InterfaceType": "Shared",
            "NICEnabled": false,
            "NICSupportsIPv6": true,
            "PingGatewayOnStartup": true,
            "SharedNetworkPortOptions": {
                "NIC": "FlexibleLOM/OCP",
                "Port": 1
            },
            "SupportsFlexibleLOM": true,
            "SupportsLOM": false
        }
    }
}

/redfish/v1/Managers/1/EthernetInterfaces/3
-------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOEthernetNetworkInterface.HpeiLOEthernetNetworkInterface",
            "@odata.type": "#HpeiLOEthernetNetworkInterface.v2_2_1.HpeiLOEthernetNetworkInterface",
            "ConfigurationSettings": "Current",
            "InterfaceType": "HostInterface",
            "NICSupportsIPv6": false
        }
    }
}

/redfish/v1/Managers/1/NetworkProtocol
--------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOManagerNetworkService.HpeiLOManagerNetworkService",
            "@odata.type": "#HpeiLOManagerNetworkService.v2_2_0.HpeiLOManagerNetworkService",
            "Actions": {
                "#HpeiLOManagerNetworkService.SendTestAlertMail": {
                    "target": "/redfish/v1/Managers/1/NetworkProtocol/Actions/Oem/Hpe/HpeiLOManagerNetworkService.SendTestAlertMail"
                },
                "#HpeiLOManagerNetworkService.SendTestSyslog": {
                    "target": "/redfish/v1/Managers/1/NetworkProtocol/Actions/Oem/Hpe/HpeiLOManagerNetworkService.SendTestSyslog"
                }
            },
            "AlertMailEmail": "",
            "AlertMailEnabled": false,
            "AlertMailSMTPAuthEnabled": false,
            "AlertMailSMTPAuthPw": null,
            "AlertMailSMTPAuthUser": "",
            "AlertMailSMTPPort": 25,
            "AlertMailSMTPSecureEnabled": true,
            "AlertMailSMTPServer": "",
            "AlertMailSenderDomain": "",
            "ConfigurationSettings": "Current",
            "FederationEnabled": true,
            "FederationSupported": true,
            "Links": {
                "EthernetInterfaces": {
                    "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces"
                },
                "SNMPService": {
                    "@odata.id": "/redfish/v1/Managers/1/SnmpService"
                }
            },
            "RemoteSyslogEnabled": false,
            "RemoteSyslogPort": 514,
            "RemoteSyslogServer": "",
            "SNMPTrapPort": 162,
            "SerialOverLanLogging": false,
            "VirtualMediaEncryptionEnabled": true,
            "XMLResponseEnabled": true
        }
    }
}

/redfish/v1/Managers/1/SnmpService
----------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSnmpServiceExt.HpeiLOSnmpServiceExt",
            "@odata.type": "#HpeiLOSnmpServiceExt.v2_0_0.HpeiLOSnmpServiceExt",
            "SNMPColdStartTrapBroadcast": true
        }
    }
}

/redfish/v1/Managers/1/VirtualMedia/1
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOVirtualMedia.HpeiLOVirtualMedia",
            "@odata.type": "#HpeiLOVirtualMedia.v2_2_0.HpeiLOVirtualMedia",
            "Actions": {
                "#HpeiLOVirtualMedia.EjectVirtualMedia": {
                    "target": "/redfish/v1/Managers/1/VirtualMedia/1/Actions/Oem/Hpe/HpeiLOVirtualMedia.EjectVirtualMedia"
                },
                "#HpeiLOVirtualMedia.InsertVirtualMedia": {
                    "target": "/redfish/v1/Managers/1/VirtualMedia/1/Actions/Oem/Hpe/HpeiLOVirtualMedia.InsertVirtualMedia"
                }
            }
        }
    }
}

/redfish/v1/Managers/1/VirtualMedia/2
-------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOVirtualMedia.HpeiLOVirtualMedia",
            "@odata.type": "#HpeiLOVirtualMedia.v2_2_0.HpeiLOVirtualMedia",
            "Actions": {
                "#HpeiLOVirtualMedia.EjectVirtualMedia": {
                    "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.EjectVirtualMedia"
                },
                "#HpeiLOVirtualMedia.InsertVirtualMedia": {
                    "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.InsertVirtualMedia"
                }
            },
            "BootOnNextServerReset": false
        }
    }
}

/redfish/v1/Systems/1
---------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeComputerSystemExt.HpeComputerSystemExt",
            "@odata.type": "#HpeComputerSystemExt.v2_9_0.HpeComputerSystemExt",
            "Actions": {
                "#HpeComputerSystemExt.PowerButton": {
                    "PushType@Redfish.AllowableValues": [
                        "Press",
                        "PressAndHold"
                    ],
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.PowerButton"
                },
                "#HpeComputerSystemExt.RestoreManufacturingDefaults": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.RestoreManufacturingDefaults"
                },
                "#HpeComputerSystemExt.RestoreSystemDefaults": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.RestoreSystemDefaults"
                },
                "#HpeComputerSystemExt.SecureSystemErase": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.SecureSystemErase"
                },
                "#HpeComputerSystemExt.ServerIntelligentDiagnosticsMode": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.ServerIntelligentDiagnosticsMode"
                },
                "#HpeComputerSystemExt.ServerSafeMode": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.ServerSafeMode"
                },
                "#HpeComputerSystemExt.SystemReset": {
                    "ResetType@Redfish.AllowableValues": [
                        "ColdBoot",
                        "AuxCycle"
                    ],
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.SystemReset"
                }
            },
            "AggregateHealthStatus": {
                "AgentlessManagementService": "Ready",
                "BiosOrHardwareHealth": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "FanRedundancy": "Redundant",
                "Fans": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Memory": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Network": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "PowerSupplies": {
                    "PowerSuppliesMismatch": false,
                    "Status": {
                        "Health": "OK"
                    }
                },
                "PowerSupplyRedundancy": "Redundant",
                "Processors": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "SmartStorageBattery": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Storage": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Temperatures": {
                    "Status": {
                        "Health": "OK"
                    }
                }
            },
            "Bios": {
                "Backup": {
                    "Date": "05/26/2021",
                    "Family": "U46",
                    "VersionString": "U46 v1.42 (05/26/2021)"
                },
                "Current": {
                    "Date": "11/29/2021",
                    "Family": "U46",
                    "VersionString": "U46 v1.56 (11/29/2021)"
                },
                "UefiClass": 2
            },
            "CriticalTempRemainOff": false,
            "CurrentPowerOnTimeSeconds": 1659546593,
            "DeviceDiscoveryComplete": {
                "AMSDeviceDiscovery": "Complete",
                "DeviceDiscovery": "vMainDeviceDiscoveryComplete",
                "SmartArrayDiscovery": "Complete"
            },
            "ElapsedEraseTimeInMinutes": 0,
            "EndOfPostDelaySeconds": null,
            "EstimatedEraseTimeInMinutes": 0,
            "HostOS": {
                "OsName": "VMware ESXi",
                "OsSysDescription": "VMkernel VYRBX9UJ4S.cisco.lab 7.0.0 #1 SMP Release build-16324942 Jun  2 2020 10:08:07 x86_64 x86_64 x86_64 ESXi",
                "OsType": 25,
                "OsVersion": "7.0.0 Build-16324942 Patch 25"
            },
            "IntelligentProvisioningAlwaysOn": true,
            "IntelligentProvisioningIndex": 9,
            "IntelligentProvisioningLocation": "System Board",
            "IntelligentProvisioningVersion": "3.64.2",
            "IsColdBooting": false,
            "Links": {
                "EthernetInterfaces": {
                    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces"
                },
                "NetworkAdapters": {
                    "@odata.id": "/redfish/v1/Systems/1/BaseNetworkAdapters"
                },
                "PCIDevices": {
                    "@odata.id": "/redfish/v1/Systems/1/PCIDevices"
                },
                "PCISlots": {
                    "@odata.id": "/redfish/v1/Systems/1/PCISlots"
                },
                "SUT": {
                    "@odata.id": "/redfish/v1/Systems/1/hpsut"
                },
                "SecureEraseReportService": {
                    "@odata.id": "/redfish/v1/Systems/1/SecureEraseReportService"
                },
                "SmartStorage": {
                    "@odata.id": "/redfish/v1/Systems/1/SmartStorage"
                },
                "USBDevices": {
                    "@odata.id": "/redfish/v1/Systems/1/USBDevices"
                },
                "USBPorts": {
                    "@odata.id": "/redfish/v1/Systems/1/USBPorts"
                },
                "WorkloadPerformanceAdvisor": {
                    "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor"
                }
            },
            "PCAPartNumber": "P09120-111",
            "PCASerialNumber": "PZCRC0BRHF005L",
            "PostDiscoveryCompleteTimeStamp": "2022-07-19T05:09:26Z",
            "PostDiscoveryMode": null,
            "PostMode": null,
            "PostState": "FinishedPost",
            "PowerAllocationLimit": 1600,
            "PowerAutoOn": "Restore",
            "PowerOnDelay": "Minimum",
            "PowerOnMinutes": 159973,
            "PowerRegulatorMode": "Dynamic",
            "PowerRegulatorModesSupported": [
                "OSControl",
                "Dynamic",
                "Max",
                "Min"
            ],
            "SMBIOS": {
                "extref": "/smbios"
            },
            "ServerFQDN": "10.29.152.144",
            "ServerIntelligentDiagnosticsModeEnabled": false,
            "ServerSafeModeEnabled": false,
            "SystemROMAndiLOEraseComponentStatus": {
                "BIOSSettingsEraseStatus": "Idle",
                "iLOSettingsEraseStatus": "Idle"
            },
            "SystemROMAndiLOEraseStatus": "Idle",
            "SystemUsage": {
                "AvgCPU0Freq": 0,
                "AvgCPU1Freq": 21,
                "CPU0Power": 53,
                "CPU1Power": 47,
                "CPUICUtil": 0,
                "CPUUtil": 0,
                "IOBusUtil": 0,
                "JitterCount": 4,
                "MemoryBusUtil": 0
            },
            "UserDataEraseComponentStatus": {},
            "UserDataEraseStatus": "Idle",
            "VirtualProfile": "Inactive"
        }
    }
}

/redfish/v1/Systems/1/Memory
----------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeAdvancedMemoryProtection.HpeAdvancedMemoryProtection",
            "@odata.type": "#HpeAdvancedMemoryProtection.v2_0_0.HpeAdvancedMemoryProtection",
            "AmpModeActive": "AdvancedECC",
            "AmpModeStatus": "AdvancedECC",
            "AmpModeSupported": [
                "AdvancedECC",
                "IntrasocketMirroring",
                "A3DC"
            ],
            "MemoryList": [
                {
                    "BoardCpuNumber": 1,
                    "BoardNumberOfSockets": 16,
                    "BoardOperationalFrequency": 2933,
                    "BoardOperationalVoltage": 1200,
                    "BoardTotalMemorySize": 16384
                },
                {
                    "BoardCpuNumber": 2,
                    "BoardNumberOfSockets": 16,
                    "BoardOperationalFrequency": 2933,
                    "BoardOperationalVoltage": 1200,
                    "BoardTotalMemorySize": 16384
                }
            ]
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm1
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm10
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm11
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm12
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm13
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm14
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "Attributes": [
                "HpeSmartMemory"
            ],
            "BaseModuleType": "RDIMM",
            "DIMMStatus": "GoodInUse",
            "MaxOperatingSpeedMTs": 3200,
            "MinimumVoltageVoltsX10": 12,
            "PartNumber": "P11443-091",
            "VendorName": "SK Hynix"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm15
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm16
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm2
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm3
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm4
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm5
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm6
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm7
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm8
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc1dimm9
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm1
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm10
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm11
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm12
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm13
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm14
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "Attributes": [
                "HpeSmartMemory"
            ],
            "BaseModuleType": "RDIMM",
            "DIMMStatus": "GoodInUse",
            "MaxOperatingSpeedMTs": 3200,
            "MinimumVoltageVoltsX10": 12,
            "PartNumber": "P11443-091",
            "VendorName": "SK Hynix"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm15
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm16
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm2
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm3
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm4
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm5
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm6
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm7
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm8
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/Memory/proc2dimm9
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    }
}

/redfish/v1/Systems/1/NetworkInterfaces
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeNetworkInterfaceStatus.HpeNetworkInterfaceStatus",
            "@odata.type": "#HpeNetworkInterfaceStatus.v1_0_0.HpeNetworkInterfaceStatus",
            "MemberContents": "AllDevices"
        }
    }
}

/redfish/v1/Systems/1/Processors/1
----------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeProcessorExt.HpeProcessorExt",
            "@odata.type": "#HpeProcessorExt.v2_0_0.HpeProcessorExt",
            "AssetTag": "UNKNOWN",
            "Cache": [
                {
                    "Associativity": "8waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 2240,
                    "Location": "Internal",
                    "MaximumSizeKB": 2240,
                    "Name": "L1-Cache",
                    "Policy": "WriteBack",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "20waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 35840,
                    "Location": "Internal",
                    "MaximumSizeKB": 35840,
                    "Name": "L2-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "12waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 43008,
                    "Location": "Internal",
                    "MaximumSizeKB": 43008,
                    "Name": "L3-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                }
            ],
            "Characteristics": [
                "64Bit",
                "MultiCore",
                "HwThread",
                "ExecuteProtection",
                "EnhancedVirtualization",
                "PowerPerfControl"
            ],
            "ConfigStatus": {
                "Populated": true,
                "State": "Enabled"
            },
            "CoresEnabled": 28,
            "ExternalClockMHz": 100,
            "MicrocodePatches": [
                {
                    "CpuId": "0x000606A4",
                    "Date": "2020-08-17T00:00:00Z",
                    "PatchId": "0x0B000280"
                },
                {
                    "CpuId": "0x000606A5",
                    "Date": "2021-03-08T00:00:00Z",
                    "PatchId": "0x0C0002F0"
                },
                {
                    "CpuId": "0x000606A6",
                    "Date": "2021-09-10T00:00:00Z",
                    "PatchId": "0x0D0002F2"
                }
            ],
            "PartNumber": "",
            "RatedSpeedMHz": 2000,
            "SerialNumber": "",
            "VoltageVoltsX10": 16
        }
    }
}

/redfish/v1/Systems/1/Processors/2
----------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeProcessorExt.HpeProcessorExt",
            "@odata.type": "#HpeProcessorExt.v2_0_0.HpeProcessorExt",
            "AssetTag": "UNKNOWN",
            "Cache": [
                {
                    "Associativity": "8waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 2240,
                    "Location": "Internal",
                    "MaximumSizeKB": 2240,
                    "Name": "L1-Cache",
                    "Policy": "WriteBack",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "20waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 35840,
                    "Location": "Internal",
                    "MaximumSizeKB": 35840,
                    "Name": "L2-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "12waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 43008,
                    "Location": "Internal",
                    "MaximumSizeKB": 43008,
                    "Name": "L3-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                }
            ],
            "Characteristics": [
                "64Bit",
                "MultiCore",
                "HwThread",
                "ExecuteProtection",
                "EnhancedVirtualization",
                "PowerPerfControl"
            ],
            "ConfigStatus": {
                "Populated": true,
                "State": "Enabled"
            },
            "CoresEnabled": 28,
            "ExternalClockMHz": 100,
            "MicrocodePatches": [
                {
                    "CpuId": "0x000606A4",
                    "Date": "2020-08-17T00:00:00Z",
                    "PatchId": "0x0B000280"
                },
                {
                    "CpuId": "0x000606A5",
                    "Date": "2021-03-08T00:00:00Z",
                    "PatchId": "0x0C0002F0"
                },
                {
                    "CpuId": "0x000606A6",
                    "Date": "2021-09-10T00:00:00Z",
                    "PatchId": "0x0D0002F2"
                }
            ],
            "PartNumber": "",
            "RatedSpeedMHz": 2000,
            "SerialNumber": "",
            "VoltageVoltsX10": 16
        }
    }
}

/redfish/v1/Systems/1/bios
--------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/"
                },
                "Boot": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/"
                },
                "KmsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/"
                },
                "Mappings": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/mappings/"
                },
                "ServerConfigLock": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/"
                },
                "TlsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/"
                },
                "iScsi": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"1D9FCF6419ED0C0C0C42B979DC024DFF\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/
---------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/"
                },
                "Boot": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/"
                },
                "KmsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/"
                },
                "Mappings": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/mappings/"
                },
                "ServerConfigLock": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/"
                },
                "TlsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/"
                },
                "iScsi": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"1D9FCF6419ED0C0C0C42B979DC024DFF\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/boot
---------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"8A7B2429C5664C4C4C1ADDE811DA8FDB\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/boot/
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"8A7B2429C5664C4C4C1ADDE811DA8FDB\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/iscsi
----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"CB481BE787534A4A4A1EC439DA313400\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/iscsi/
-----------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"CB481BE787534A4A4A1EC439DA313400\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig
--------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"A6A5128F2F03080808E00797569D11A6\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"A6A5128F2F03080808E00797569D11A6\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock
---------------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"38D6FCD3F5C05F5F5FA4075B84BC26B2\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/
----------------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"38D6FCD3F5C05F5F5FA4075B84BC26B2\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig
--------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"232BE31B46AC494949B10E80334FBD02\""
            }
        }
    }
}

/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"232BE31B46AC494949B10E80334FBD02\""
            }
        }
    }
}

/redfish/v1/UpdateService
-------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOUpdateServiceExt.HpeiLOUpdateServiceExt",
            "@odata.type": "#HpeiLOUpdateServiceExt.v2_1_4.HpeiLOUpdateServiceExt",
            "Accept3rdPartyFirmware": false,
            "Actions": {
                "#HpeiLOUpdateServiceExt.AddFromUri": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.AddFromUri"
                },
                "#HpeiLOUpdateServiceExt.DeleteInstallSets": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteInstallSets"
                },
                "#HpeiLOUpdateServiceExt.DeleteMaintenanceWindows": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteMaintenanceWindows"
                },
                "#HpeiLOUpdateServiceExt.DeleteUnlockedComponents": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteUnlockedComponents"
                },
                "#HpeiLOUpdateServiceExt.DeleteUpdateTaskQueueItems": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteUpdateTaskQueueItems"
                },
                "#HpeiLOUpdateServiceExt.RemoveLanguagePack": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.RemoveLanguagePack"
                },
                "#HpeiLOUpdateServiceExt.SetDefaultLanguage": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.SetDefaultLanguage"
                },
                "#HpeiLOUpdateServiceExt.StartFirmwareIntegrityCheck": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.StartFirmwareIntegrityCheck"
                }
            },
            "Capabilities": {
                "PLDMFirmwareUpdate": true,
                "UpdateFWPKG": true
            },
            "ComponentRepository": {
                "@odata.id": "/redfish/v1/UpdateService/ComponentRepository"
            },
            "CurrentTime": "2022-08-03T17:14:57Z",
            "DowngradePolicy": "AllowDowngrade",
            "FirmwareIntegrity": {
                "EnableBackgroundScan": false,
                "LastScanResult": "OK",
                "LastScanTime": "1970-01-01T00:02:04Z",
                "OnIntegrityFailure": "LogOnly",
                "ScanEveryDays": 7
            },
            "InstallSets": {
                "@odata.id": "/redfish/v1/UpdateService/InstallSets"
            },
            "InvalidImageRepository": {
                "@odata.id": "/redfish/v1/UpdateService/InvalidImageRepository"
            },
            "MaintenanceWindows": {
                "@odata.id": "/redfish/v1/UpdateService/MaintenanceWindows"
            },
            "State": "Idle",
            "UpdateTaskQueue": {
                "@odata.id": "/redfish/v1/UpdateService/UpdateTaskQueue"
            }
        }
    }
}

/redfish/v1/UpdateService/ComponentRepository
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeComponentRepositoryInformation.HpeComponentRepositoryInformation",
            "@odata.type": "#HpeComponentRepositoryInformation.v2_0_0.HpeComponentRepositoryInformation",
            "ComponentCount": 7,
            "FreeSizeBytes": 920829952,
            "TotalSizeBytes": 1073168384
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/1
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
            "DeviceContext": "System Board",
            "Targets": [
                "4764a662-b342-4fc7-9ce9-258c5d99e815",
                "c0bcf2b9-1141-49af-aab8-c73791f0349c"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/10
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "3f30a329-d03c-46b8-8f0e-9567fad4ea9f",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/11
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "System Board"
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/12
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "ac963eeb-ed78-4f36-c18c-29d85f34a0ac",
            "DeviceContext": "System Board"
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/13
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "System Board"
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/14
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "Embedded Device"
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/15
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "PCI-E Slot 1",
            "DeviceInstance": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "Targets": [
                "a6b1a447-382a-5a4f-1000-10e215900293"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/16
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "PCI-E Slot 13",
            "DeviceInstance": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "Targets": [
                "a6b1a447-382a-5a4f-1b4b-22411590030f"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/17
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "OCP 3.0 Slot 10",
            "DeviceInstance": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "Targets": [
                "a6b1a447-382a-5a4f-8086-1521808600a3"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/18
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "Embedded Device",
            "DeviceInstance": "PciRoot(0x0)/Pci(0x1C,0x4)/Pci(0x0,0x1)",
            "Targets": [
                "a6b1a447-382a-5a4f-102b-0538159000e4"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/19
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port 1I Box 1 Bay 1",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/2
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "00000000-0000-0000-0000-000001553436"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/20
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port 1I Box 1 Bay 3",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/21
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Slot=13:Bay=1",
            "Targets": [
                "562340a5-3053-3030-3438-304b58414c42"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/22
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Slot=13:Bay=2",
            "Targets": [
                "562340a5-3053-3030-3438-304b58414c42"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/23
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port=1I:Box=1:Bay=1",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/24
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port=1I:Box=1:Bay=3",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/25
----------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port=1I:Box=1:Bay=2",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/3
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "00000000-0000-0000-0000-000001553436"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/4
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/5
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "9e48a28a-586c-4519-8405-a04f84e27f0f",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "00000000-0000-0000-0000-000000504d05"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/6
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "6bb86077-0275-4614-aae1-86618e8b1c27",
            "DeviceContext": "Bay 1",
            "Targets": [
                "0102bd05-0001-0000-0000-0cf38db966ea"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/7
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "6bb86077-0275-4614-aae1-86618e8b1c27",
            "DeviceContext": "Bay 2",
            "Targets": [
                "0102bd05-0001-0000-0000-0cf38db966ea"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/8
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "c734e171-8721-48c9-9ed6-d5bc7da5ef8d",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "a6b1a447-382a-5a4f-3c10-87800a000303"
            ]
        }
    }
}

/redfish/v1/UpdateService/FirmwareInventory/9
---------------------------------------------
{
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "b34e5677-21dc-45d3-872b-42f76fee9053",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "a6b1a447-382a-5a4f-3c10-87800a000101"
            ]
        }
    }
}
```