# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/Managers

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerCollection.ManagerCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers",
    "@odata.type": "#ManagerCollection.ManagerCollection",
    "Description": "Managers view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Managers"
}
```

## /redfish/v1/Managers/1

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.etag": "W/\"4D2215B6\"",
    "@odata.id": "/redfish/v1/Managers/1",
    "@odata.type": "#Manager.v1_5_1.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart",
                "GracefulRestart"
            ],
            "target": "/redfish/v1/Managers/1/Actions/Manager.Reset"
        }
    },
    "CommandShell": {
        "ConnectTypesSupported": [
            "SSH",
            "Oem"
        ],
        "MaxConcurrentSessions": 9,
        "ServiceEnabled": true
    },
    "DateTime": "2022-08-03T17:11:30Z",
    "DateTimeLocalOffset": "+00:00",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces"
    },
    "FirmwareVersion": "iLO 5 v2.55",
    "GraphicalConsole": {
        "ConnectTypesSupported": [
            "KVMIP"
        ],
        "MaxConcurrentSessions": 10,
        "ServiceEnabled": true
    },
    "HostInterfaces": {
        "@odata.id": "/redfish/v1/Managers/1/HostInterfaces"
    },
    "Id": "1",
    "Links": {
        "ManagerForChassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "ManagerForServers": [
            {
                "@odata.id": "/redfish/v1/Systems/1"
            }
        ],
        "ManagerInChassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Managers/1/LogServices"
    },
    "ManagerType": "BMC",
    "Model": "iLO 5",
    "Name": "Manager",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/1/NetworkProtocol"
    },
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
    },
    "SerialConsole": {
        "ConnectTypesSupported": [
            "SSH",
            "IPMI",
            "Oem"
        ],
        "MaxConcurrentSessions": 13,
        "ServiceEnabled": true
    },
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/1/SerialInterface"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "8216b0ce-df09-50c8-bf08-1eb1a473abff",
    "VirtualMedia": {
        "@odata.id": "/redfish/v1/Managers/1/VirtualMedia"
    }
}
```

## /redfish/v1/Managers/1/ActiveHealthSystem

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOActiveHealthSystem.HpeiLOActiveHealthSystem",
    "@odata.etag": "W/\"B2FA3342\"",
    "@odata.id": "/redfish/v1/Managers/1/ActiveHealthSystem",
    "@odata.type": "#HpeiLOActiveHealthSystem.v2_5_0.HpeiLOActiveHealthSystem",
    "AHSEnabled": true,
    "AHSFileEnd": "2022-08-03T00:00:00Z",
    "AHSFileStart": "2021-08-18T00:00:00Z",
    "AHSStatus": {
        "HardwareEnabled": true,
        "SoftwareEnabled": true,
        "TemporaryHoldEnabled": false
    },
    "Actions": {
        "#HpeiLOActiveHealthSystem.CaptureSystemLog": {
            "target": "/redfish/v1/Managers/1/ActiveHealthSystem/Actions/HpeiLOActiveHealthSystem.CaptureSystemLog"
        },
        "#HpeiLOActiveHealthSystem.ClearLog": {
            "target": "/redfish/v1/Managers/1/ActiveHealthSystem/Actions/HpeiLOActiveHealthSystem.ClearLog"
        },
        "#HpeiLOActiveHealthSystem.LogAmplifierData": {
            "target": "/redfish/v1/Managers/1/ActiveHealthSystem/Actions/HpeiLOActiveHealthSystem.LogAmplifierData"
        },
        "#HpeiLOActiveHealthSystem.LogMilestone": {
            "target": "/redfish/v1/Managers/1/ActiveHealthSystem/Actions/HpeiLOActiveHealthSystem.LogMilestone"
        }
    },
    "Id": "ActiveHealthSystem",
    "Links": {
        "AHSLocation": {
            "extref": "/ahsdata/HPE_VYRBX9UJ4S_20220803.ahs?downloadAll=1"
        },
        "InfoSight": {
            "extref": "/ahsdata/HPE_VYRBX9UJ4S_20220803.ahs?minimalDL=1&&days=1"
        },
        "RecentWeek": {
            "extref": "/ahsdata/HPE_VYRBX9UJ4S_20220803.ahs?days=7"
        }
    },
    "LocationParameters": {
        "case_no": "This query parameter may be added to the AHS location URI to insert the case number into the AHS log header. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?downloadAll=1&&case_no=abc123.",
        "co_name": "This query parameter may be added to the AHS location URI to insert the company name into the AHS log header. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?downloadAll=1&&co_name=myCompany.",
        "contact_name": "This query parameter may be added to the AHS location URI to insert the contact name into the AHS log header. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?downloadAll=1&&contact_name=JohnDoe.",
        "days": "This query parameter should be used to download the last N days of the AHS log, from today's date. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?days=7.",
        "downloadAll": "This query parameter should be used to download the entire AHS log. For example, http://iloname.example.net/ahsdata/HPE_x0xxxxxxxxx_20140821.ahs?downloadAll=1.",
        "email": "This query parameter may be added to the AHS location URI to insert the contacts email address into the AHS log header. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?downloadAll=1&&email=abc@xyz.com.",
        "from": "This query parameter must be added with the 'to' query parameter to the AHS location URI to limit the range of data returned. 'downloadAll' or 'days' parameters should not be used with this query parameter. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?from=2014-03-01&&to=2014-03-30.",
        "phone": "This query parameter may be added to the AHS location URI to insert the contacts phone number into the AHS log header. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?downloadAll=1&&contact_name=JohnDoe&&phone=555-555-5555.",
        "to": "This query parameter must be added with the 'from' query parameter to the AHS location URI to limit the range of data returned. 'downloadAll' or 'days' parameters should not be used with this query parameter. For example, http://iloname.example.net/ahsdata/HPE_xxxxxxxxxx_20140821.ahs?from=2014-03-01&&to=2014-03-30."
    },
    "Name": "Active Health System"
}
```

## /redfish/v1/Managers/1/BackupRestoreService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOBackupRestoreService.HpeiLOBackupRestoreService",
    "@odata.etag": "W/\"D863AC37\"",
    "@odata.id": "/redfish/v1/Managers/1/BackupRestoreService",
    "@odata.type": "#HpeiLOBackupRestoreService.v2_2_0.HpeiLOBackupRestoreService",
    "BackupFileLocation": "/bkupdata/HPE_VYRBX9UJ4S_20220803_1713.bak",
    "BackupFiles": {
        "@odata.id": "/redfish/v1/Managers/1/BackupRestoreService/BackupFiles"
    },
    "HttpPushUri": "/cgi-bin/uploadRestoreFile",
    "Id": "BackupRestoreService",
    "Name": "Backup Restore Service"
}
```

## /redfish/v1/Managers/1/BackupRestoreService/BackupFiles

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOBackupFileCollection.HpeiLOBackupFileCollection",
    "@odata.etag": "W/\"AC303DD3\"",
    "@odata.id": "/redfish/v1/Managers/1/BackupRestoreService/BackupFiles",
    "@odata.type": "#HpeiLOBackupFileCollection.HpeiLOBackupFileCollection",
    "Description": "Backup File Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Backup File Collection",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOBackupFilesInformation.HpeiLOBackupFilesInformation",
            "@odata.type": "#HpeiLOBackupFilesInformation.v1_0_0.HpeiLOBackupFilesInformation",
            "BackupFileCount": 0,
            "BackupFilesAllowed": 1
        }
    }
}
```

## /redfish/v1/Managers/1/DateTime

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLODateTime.HpeiLODateTime",
    "@odata.etag": "W/\"39402D1A\"",
    "@odata.id": "/redfish/v1/Managers/1/DateTime",
    "@odata.type": "#HpeiLODateTime.v2_0_0.HpeiLODateTime",
    "ConfigurationSettings": "Current",
    "DateTime": "2022-08-03T17:13:32Z",
    "Id": "DateTime",
    "Links": {
        "EthernetNICs": {
            "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces"
        }
    },
    "NTPServers": [
        "10.29.152.124",
        ""
    ],
    "Name": "iLO Date and Time Settings",
    "PropagateTimeToHost": false,
    "StaticNTPServers": [
        "10.29.152.124",
        ""
    ],
    "TimeZone": {
        "Index": 15,
        "Name": "Greenwich Mean Time, Casablanca, Monrovia",
        "UtcOffset": "+00:00",
        "Value": "GMT-0"
    },
    "TimeZoneList": [
        {
            "Index": 0,
            "Name": "International Date Line West",
            "UtcOffset": "-12:00",
            "Value": "GMT+12:00"
        },
        {
            "Index": 1,
            "Name": "Midway Island, Samoa",
            "UtcOffset": "-11:00",
            "Value": "SST+11:00"
        },
        {
            "Index": 2,
            "Name": "Hawaii",
            "UtcOffset": "-10:00",
            "Value": "HST+10:00"
        },
        {
            "Index": 3,
            "Name": "Marquesas",
            "UtcOffset": "-09:30",
            "Value": "MART+9:30"
        },
        {
            "Index": 4,
            "Name": "Alaska",
            "UtcOffset": "-09:00",
            "Value": "AKST+9:00AKDT+08:00:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 5,
            "Name": "Pacific Time(US & Canada), Tijuana, Portland",
            "UtcOffset": "-08:00",
            "Value": "PST+8:00PDT+07:00:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 6,
            "Name": "Arizona, Chihuahua, La Paz, Mazatlan, Mountain Time (US & Canad",
            "UtcOffset": "-07:00",
            "Value": "MST+7:00MDT+06:00:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 7,
            "Name": "Central America, Central Time(US & Canada)",
            "UtcOffset": "-06:00",
            "Value": "CST+6:00CDT+05:00:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 8,
            "Name": "Bogota, Lima, Quito, Eastern Time(US & Canada)",
            "UtcOffset": "-05:00",
            "Value": "EST+5:00EDT+04:00:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 9,
            "Name": "Caracas, Georgetown",
            "UtcOffset": "-04:00",
            "Value": "VET+4:00"
        },
        {
            "Index": 10,
            "Name": "Atlantic Time(Canada), Santiago",
            "UtcOffset": "-04:00",
            "Value": "AST+4:00ADT+03:00:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 11,
            "Name": "Newfoundland",
            "UtcOffset": "-03:30",
            "Value": "NST+3:30NDT+02:30:00,M3.2.0/02:00:00,M11.1.0/02:00:00"
        },
        {
            "Index": 12,
            "Name": "Brasilia, Buenos Aires, Greenland",
            "UtcOffset": "-03:00",
            "Value": "ART+3:00"
        },
        {
            "Index": 13,
            "Name": "Mid-Atlantic",
            "UtcOffset": "-02:00",
            "Value": "GST+2:00"
        },
        {
            "Index": 14,
            "Name": "Azores, Cape Verde Is.",
            "UtcOffset": "-01:00",
            "Value": "CVT+1:00"
        },
        {
            "Index": 15,
            "Name": "Greenwich Mean Time, Casablanca, Monrovia",
            "UtcOffset": "+00:00",
            "Value": "GMT-0"
        },
        {
            "Index": 16,
            "Name": "Dublin, London",
            "UtcOffset": "+00:00",
            "Value": "WET-0WEST-1,M3.5.0/01:00:00,M10.5.0/02:00:00"
        },
        {
            "Index": 17,
            "Name": "Amsterdam, Berlin, Bern, Rome, Paris, West Central Africa",
            "UtcOffset": "+01:00",
            "Value": "CET-1:00CEST-02:00:00,M3.5.0/01:00:00,M10.5.0/01:00:00"
        },
        {
            "Index": 18,
            "Name": "Athens, Bucharest, Cairo, Jerusalem",
            "UtcOffset": "+02:00",
            "Value": "EET-2:00EEST-03:00:00,M3.5.0/01:00:00,M10.5.0/01:00:00"
        },
        {
            "Index": 19,
            "Name": "Baghdad, Kuwait, Riyadh, Moscow, Istanbul, Nairobi",
            "UtcOffset": "+03:00",
            "Value": "AST-3:00"
        },
        {
            "Index": 20,
            "Name": "Tehran",
            "UtcOffset": "+03:30",
            "Value": "IRST-3:30IRDT-04:30:00,80/00:00:00,264/00:00:00"
        },
        {
            "Index": 21,
            "Name": "Abu Dhabi, Muscat, Baku, Tbilisi, Yerevan",
            "UtcOffset": "+04:00",
            "Value": "GST-4:00"
        },
        {
            "Index": 22,
            "Name": "Kabul",
            "UtcOffset": "+04:30",
            "Value": "AFT-4:30"
        },
        {
            "Index": 23,
            "Name": "Ekaterinburg, Islamabad, Karachi, Tashkent",
            "UtcOffset": "+05:00",
            "Value": "YEKT-5:00"
        },
        {
            "Index": 24,
            "Name": "Chennai, Kolkata, Mumbai, New Delhi",
            "UtcOffset": "+05:30",
            "Value": "IST-5:30"
        },
        {
            "Index": 25,
            "Name": "Kathmandu",
            "UtcOffset": "+05:45",
            "Value": "NPT-5:45"
        },
        {
            "Index": 26,
            "Name": "Almaty, Dhaka, Sri Jayawardenepura",
            "UtcOffset": "+06:00",
            "Value": "ALMT-6:00"
        },
        {
            "Index": 27,
            "Name": "Rangoon",
            "UtcOffset": "+06:30",
            "Value": "MMT-6:30"
        },
        {
            "Index": 28,
            "Name": "Bangkok, Hanio, Jakarta, Novosibirsk, Astana, Krasnoyarsk",
            "UtcOffset": "+07:00",
            "Value": "ICT-7:00"
        },
        {
            "Index": 29,
            "Name": "Beijing, Chongqing, Hong Kong, Urumqi, Taipei, Perth",
            "UtcOffset": "+08:00",
            "Value": "CST-8:00"
        },
        {
            "Index": 30,
            "Name": "Eucla",
            "UtcOffset": "+08:45",
            "Value": "ACWST-08:45"
        },
        {
            "Index": 31,
            "Name": "Osaka, Sapporo, Tokyo, Seoul, Yakutsk",
            "UtcOffset": "+09:00",
            "Value": "JST-9:00"
        },
        {
            "Index": 32,
            "Name": "Adelaide, Darwin",
            "UtcOffset": "+09:30",
            "Value": "ACST-9:30ACDT-10:30:00,M10.1.0/02:00:00,M4.1.0/02:00:00"
        },
        {
            "Index": 33,
            "Name": "Canberra, Melbourne, Sydney, Guam, Hobart, Vladivostok",
            "UtcOffset": "+10:00",
            "Value": "AEST-10:00AEDT-11:00:00,M10.1.0/02:00:00,M4.1.0/02:00:00"
        },
        {
            "Index": 34,
            "Name": "Lord Howe",
            "UtcOffset": "+10:30",
            "Value": "LHST-10:30LHDT11:00"
        },
        {
            "Index": 35,
            "Name": "Chatham",
            "UtcOffset": "+10:45",
            "Value": "CHAST-10:45CHADT-11:45"
        },
        {
            "Index": 36,
            "Name": "Magadan, Solomon Is., New Caledonia",
            "UtcOffset": "+11:00",
            "Value": "MAGT-11:00"
        },
        {
            "Index": 37,
            "Name": "Auckland, Wellington, Fiji, Kamchatka, Marshall Is.",
            "UtcOffset": "+12:00",
            "Value": "NZST-12:00NZDT-13:00:00,M9.5.0/02:00:00,M4.1.0/02:00:00"
        },
        {
            "Index": 38,
            "Name": "Nuku'alofa",
            "UtcOffset": "+13:00",
            "Value": "TKT-13:00"
        },
        {
            "Index": 39,
            "Name": "Line Islands",
            "UtcOffset": "+14:00",
            "Value": "LINT-14:00"
        },
        {
            "Index": 40,
            "Name": "Unspecified Time Zone",
            "UtcOffset": "+00:00",
            "Value": "GMT-0"
        }
    ]
}
```

## /redfish/v1/Managers/1/EmbeddedMedia

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOEmbeddedMedia.HpeiLOEmbeddedMedia",
    "@odata.etag": "W/\"C488FC11\"",
    "@odata.id": "/redfish/v1/Managers/1/EmbeddedMedia",
    "@odata.type": "#HpeiLOEmbeddedMedia.v2_0_0.HpeiLOEmbeddedMedia",
    "Controller": {
        "Firmware": {
            "Current": {
                "VersionString": "02.11.00"
            }
        },
        "Status": {
            "Health": "OK",
            "State": "Enabled"
        }
    },
    "Id": "EmbeddedMedia",
    "Name": "Embedded Media Service"
}
```

## /redfish/v1/Managers/1/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.etag": "W/\"E589C4BF\"",
    "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Configuration of Manager Network Interfaces",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/1"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/2"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/3"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Manager Network Interfaces"
}
```

## /redfish/v1/Managers/1/EthernetInterfaces/1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"D6626C80\"",
    "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "AutoNeg": true,
    "DHCPv4": {
        "DHCPEnabled": false,
        "UseDNSServers": false,
        "UseDomainName": false,
        "UseGateway": false,
        "UseNTPServers": false,
        "UseStaticRoutes": false
    },
    "DHCPv6": {
        "OperatingMode": "Stateful",
        "UseDNSServers": true,
        "UseDomainName": true,
        "UseNTPServers": false,
        "UseRapidCommit": false
    },
    "Description": "Configuration of this Manager Network Interface",
    "FQDN": null,
    "FullDuplex": true,
    "HostName": "ILOVYRBX9UJ4S",
    "IPv4Addresses": [
        {
            "Address": "10.242.29.174",
            "AddressOrigin": "Static",
            "Gateway": "10.29.152.1",
            "SubnetMask": "255.255.255.0"
        }
    ],
    "IPv4StaticAddresses": [
        {
            "Address": "10.242.29.174",
            "Gateway": "10.29.152.1",
            "SubnetMask": "255.255.255.0"
        }
    ],
    "IPv6AddressPolicyTable": [
        {
            "Label": null,
            "Precedence": 35,
            "Prefix": "::ffff:0:0/96"
        }
    ],
    "IPv6Addresses": [
        {
            "Address": "FE80::B67A:F1FF:FEBD:4C94",
            "AddressOrigin": "SLAAC",
            "AddressState": "Preferred",
            "PrefixLength": 64
        }
    ],
    "IPv6DefaultGateway": "::",
    "IPv6StaticAddresses": [
        {
            "Address": "::",
            "PrefixLength": null
        },
        {
            "Address": "::",
            "PrefixLength": null
        },
        {
            "Address": "::",
            "PrefixLength": null
        },
        {
            "Address": "::",
            "PrefixLength": null
        }
    ],
    "IPv6StaticDefaultGateways": [
        {
            "Address": "::"
        }
    ],
    "Id": "1",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkUp",
    "MACAddress": "B4:7A:F1:BD:4C:94",
    "MaxIPv6StaticAddresses": 4,
    "Name": "Manager Dedicated Network Interface",
    "NameServers": [
        "10.29.143.10"
    ],
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
    },
    "PermanentMACAddress": "B4:7A:F1:BD:4C:94",
    "SpeedMbps": 1000,
    "StatelessAddressAutoConfig": {
        "IPv6AutoConfigEnabled": true
    },
    "StaticNameServers": [
        "10.29.143.10",
        "0.0.0.0",
        "0.0.0.0",
        "::",
        "::",
        "::"
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VLAN": {
        "VLANEnable": false,
        "VLANId": null
    }
}
```

## /redfish/v1/Managers/1/EthernetInterfaces/2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"CEE83B4D\"",
    "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "AutoNeg": null,
    "DHCPv4": {
        "DHCPEnabled": true,
        "UseDNSServers": true,
        "UseDomainName": true,
        "UseGateway": true,
        "UseNTPServers": true,
        "UseStaticRoutes": true
    },
    "DHCPv6": {
        "OperatingMode": "Stateful",
        "UseDNSServers": true,
        "UseDomainName": true,
        "UseNTPServers": true,
        "UseRapidCommit": false
    },
    "Description": "Configuration of this Manager Network Interface",
    "FQDN": null,
    "FullDuplex": false,
    "HostName": "ILOVYRBX9UJ4S",
    "IPv4Addresses": [
        {
            "Address": "0.0.0.0",
            "AddressOrigin": "DHCP",
            "Gateway": "0.0.0.0",
            "SubnetMask": "0.0.0.0"
        }
    ],
    "IPv4StaticAddresses": [],
    "IPv6AddressPolicyTable": [
        {
            "Label": null,
            "Precedence": 35,
            "Prefix": "::ffff:0:0/96"
        }
    ],
    "IPv6Addresses": [],
    "IPv6DefaultGateway": "::",
    "IPv6StaticAddresses": [
        {
            "Address": "::",
            "PrefixLength": null
        },
        {
            "Address": "::",
            "PrefixLength": null
        },
        {
            "Address": "::",
            "PrefixLength": null
        },
        {
            "Address": "::",
            "PrefixLength": null
        }
    ],
    "IPv6StaticDefaultGateways": [
        {
            "Address": "::"
        }
    ],
    "Id": "2",
    "InterfaceEnabled": false,
    "LinkStatus": null,
    "MACAddress": "B4:7A:F1:BD:4C:95",
    "MaxIPv6StaticAddresses": 4,
    "Name": "Manager Shared Network Interface",
    "NameServers": [],
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
    },
    "PermanentMACAddress": "B4:7A:F1:BD:4C:95",
    "SpeedMbps": null,
    "StatelessAddressAutoConfig": {
        "IPv6AutoConfigEnabled": true
    },
    "StaticNameServers": [
        "0.0.0.0",
        "0.0.0.0",
        "0.0.0.0",
        "::",
        "::",
        "::"
    ],
    "Status": {
        "Health": null,
        "State": "Disabled"
    },
    "VLAN": {
        "VLANEnable": false,
        "VLANId": null
    }
}
```

## /redfish/v1/Managers/1/EthernetInterfaces/3

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"574A9F3A\"",
    "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Configuration of this Manager USB Ethernet Interface available for access from Host.",
    "IPv4Addresses": [],
    "IPv4StaticAddresses": [],
    "IPv6AddressPolicyTable": [],
    "IPv6Addresses": [],
    "IPv6StaticAddresses": [],
    "IPv6StaticDefaultGateways": [],
    "Id": "3",
    "InterfaceEnabled": false,
    "LinkStatus": null,
    "Links": {
        "HostInterface": {
            "@odata.id": "/redfish/v1/Managers/1/HostInterfaces/1"
        }
    },
    "MACAddress": "0A:CA:FE:F0:0D:04",
    "Name": "Manager Virtual Network Interface",
    "NameServers": [],
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOEthernetNetworkInterface.HpeiLOEthernetNetworkInterface",
            "@odata.type": "#HpeiLOEthernetNetworkInterface.v2_2_1.HpeiLOEthernetNetworkInterface",
            "ConfigurationSettings": "Current",
            "InterfaceType": "HostInterface",
            "NICSupportsIPv6": false
        }
    },
    "PermanentMACAddress": "0A:CA:FE:F0:0D:04",
    "StaticNameServers": [],
    "Status": {
        "Health": null,
        "State": "Disabled"
    }
}
```

## /redfish/v1/Managers/1/FederationGroups

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOFederationGroupCollection.HpeiLOFederationGroupCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/FederationGroups",
    "@odata.type": "#HpeiLOFederationGroupCollection.HpeiLOFederationGroupCollection",
    "Description": "HPE iLO Federation view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/FederationGroups/DEFAULT"
        }
    ],
    "Members@odata.count": 1,
    "Name": "HPE iLO Federation"
}
```

## /redfish/v1/Managers/1/FederationGroups/DEFAULT

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOFederationGroup.HpeiLOFederationGroup",
    "@odata.etag": "W/\"A1508BC0\"",
    "@odata.id": "/redfish/v1/Managers/1/FederationGroups/DEFAULT",
    "@odata.type": "#HpeiLOFederationGroup.v2_0_0.HpeiLOFederationGroup",
    "Id": "DEFAULT",
    "Name": "DEFAULT",
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
    }
}
```

## /redfish/v1/Managers/1/FederationPeers

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOFederationPeersCollection.HpeiLOFederationPeersCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/FederationPeers",
    "@odata.type": "#HpeiLOFederationPeersCollection.HpeiLOFederationPeersCollection",
    "Description": " FederationPeers view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/FederationPeers/DEFAULT"
        }
    ],
    "Members@odata.count": 1,
    "Name": "FederationPeers"
}
```

## /redfish/v1/Managers/1/FederationPeers/DEFAULT

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOFederationPeers.HpeiLOFederationPeers",
    "@odata.etag": "W/\"DA65011E\"",
    "@odata.id": "/redfish/v1/Managers/1/FederationPeers/DEFAULT",
    "@odata.type": "#HpeiLOFederationPeers.v2_0_0.HpeiLOFederationPeers",
    "Id": "DEFAULT",
    "Name": "DEFAULT",
    "Peers": [
        {
            "HttpErrorCode": 0,
            "ManagerIPAddress": "10.29.153.169",
            "Time": "2022-08-03T17:09:01Z",
            "URL": "http://10.29.153.169:80/",
            "UUID": "c8247a9e-cb82-5c64-889e-f0e64cef0e92"
        },
        {
            "HttpErrorCode": 0,
            "ManagerIPAddress": "10.29.153.99",
            "Time": "2022-08-03T17:06:18Z",
            "URL": "http://10.29.153.99:80/",
            "UUID": "a776f12b-8389-57c4-af50-9f2ab9e3a162"
        },
        {
            "HttpErrorCode": 0,
            "ManagerIPAddress": "10.29.152.65",
            "Time": "2022-08-03T17:06:28Z",
            "URL": "http://10.29.152.65:80/",
            "UUID": "6217f66d-e269-5897-8716-dc7cb0c02145"
        }
    ]
}
```

## /redfish/v1/Managers/1/GUIService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOGUIService.HpeiLOGUIService",
    "@odata.etag": "W/\"8DA7E8E4\"",
    "@odata.id": "/redfish/v1/Managers/1/GUIService",
    "@odata.type": "#HpeiLOGUIService.v1_1_0.HpeiLOGUIService",
    "Description": "iLO GUI Service",
    "Features": {
        "AhsViewer": true,
        "AnonymousData": true,
        "BiosPrivilege": true,
        "CacSmartcard": true,
        "ComputeCloudConsoleFlag": false,
        "CoolingModuleSupport": false,
        "DotNetConsole": true,
        "EAPTLSSupport": false,
        "Encryption": true,
        "EventDetails": true,
        "ExternalMonitor": true,
        "Federation": true,
        "HighEfficiencyMode": true,
        "HostNicPrivilege": true,
        "IntelligentProvisioning": true,
        "IpManager": true,
        "IpxeBoot": true,
        "JavaConsole": true,
        "Kerberos": true,
        "Licensing": true,
        "Mobile": true,
        "PowerDiscovery": true,
        "RIBCL": true,
        "RecoverySet": true,
        "RemoteConsoleSecurity": true,
        "RemoteSupport": true,
        "Repository": true,
        "SecurityDashboard": true,
        "ServiceAccount": true,
        "SharedNicOcp": true,
        "SingleSignOn": true,
        "StoragePrivilege": true,
        "SwapROM": true,
        "SystemAutoHeal": true,
        "SystemDefaults": true,
        "ThermalGraph": true,
        "Thumbnail": true,
        "UefiSerialDbgMsg": true,
        "UpdateService": true,
        "VirtualMedia": true
    },
    "Id": "GUIService",
    "Name": "GUI Service",
    "TreeList": [
        {
            "LangKey": "info",
            "TabSet": "information",
            "Tabs": [
                {
                    "LangKey": "overview",
                    "Link": "summary.html",
                    "Text": "Overview"
                },
                {
                    "LangKey": "secDashboard",
                    "Link": "security_dashboard.html",
                    "Text": "Security Dashboard"
                },
                {
                    "LangKey": "sessions",
                    "Link": "info_sessions.html",
                    "Text": "Session List"
                },
                {
                    "LangKey": "iLOLog",
                    "Link": "info_log.html",
                    "Text": "iLO Event Log"
                },
                {
                    "LangKey": "iml",
                    "Link": "info_iml.html",
                    "Text": "Integrated Management Log"
                },
                {
                    "LangKey": "sl",
                    "Link": "info_sl.html",
                    "Text": "Security Log"
                },
                {
                    "LangKey": "ers_nav_tab_bb",
                    "Link": "admin_ers_bb.html",
                    "Text": "Active Health System Log"
                },
                {
                    "LangKey": "diag",
                    "Link": "info_diagnostics.html",
                    "Text": "Diagnostics"
                }
            ],
            "Text": "Information"
        },
        {
            "LangKey": "sysInfo",
            "TabSet": "sysInfo",
            "Tabs": [
                {
                    "LangKey": "summary",
                    "Link": "info_system.html",
                    "Text": "Summary"
                },
                {
                    "LangKey": "proc",
                    "Link": "info_system_proc.html",
                    "Text": "Processors"
                },
                {
                    "LangKey": "mem",
                    "Link": "info_system_mem.html",
                    "Text": "Memory"
                },
                {
                    "LangKey": "nic",
                    "Link": "info_system_nic.html",
                    "Text": "Network"
                },
                {
                    "LangKey": "inventory",
                    "Link": "info_system_inventory.html",
                    "Text": "Device Inventory"
                },
                {
                    "LangKey": "storage",
                    "Link": "info_system_drives.html",
                    "Text": "Storage"
                }
            ],
            "Text": "System Information"
        },
        {
            "LangKey": "firmware",
            "RightHandMenu": "fw_sw_rhMenu.html",
            "TabSet": "firmware",
            "Tabs": [
                {
                    "LangKey": "FwInfo",
                    "Link": "fw_sw_firmware.html",
                    "Text": "Firmware"
                },
                {
                    "LangKey": "software",
                    "Link": "fw_sw_software.html",
                    "Text": "Software"
                },
                {
                    "LangKey": "maintenanceWindows",
                    "Link": "fw_sw_MaintenanceWindows.html",
                    "Text": "Maintenance Windows"
                },
                {
                    "LangKey": "repo",
                    "Link": "fw_sw_iLORepo.html",
                    "Text": "iLO Repository"
                },
                {
                    "LangKey": "installSets",
                    "Link": "fw_sw_InstallSets.html",
                    "Text": "Install Sets"
                },
                {
                    "LangKey": "installationQueue",
                    "Link": "fw_sw_InstallationQueue.html",
                    "Text": "Installation Queue"
                }
            ],
            "Text": "Firmware & OS Software"
        },
        {
            "Features": "federation",
            "LangKey": "fed",
            "TabSet": "federation",
            "Tabs": [
                {
                    "LangKey": "setup",
                    "Link": "admin_multi_config.html",
                    "Text": "Setup"
                },
                {
                    "LangKey": "moverview",
                    "Link": "multi_summary.html",
                    "Text": "Multi-System View"
                },
                {
                    "LangKey": "mnodemap",
                    "Link": "multi_nodemap.html",
                    "Text": "[Debug] Multi-System Map"
                },
                {
                    "LangKey": "mvm",
                    "Link": "multi_vm.html",
                    "Text": "Group Virtual Media"
                },
                {
                    "LangKey": "mPwr",
                    "Link": "multi_power.html",
                    "Text": "Group Power"
                },
                {
                    "LangKey": "mPwrSettings",
                    "Link": "multi_power_settings.html",
                    "Text": "Group Power Settings"
                },
                {
                    "LangKey": "mfirmware",
                    "Link": "multi_firmware.html",
                    "Text": "Group Firmware Update"
                },
                {
                    "LangKey": "mlicense",
                    "Link": "multi_license.html",
                    "Text": "Group Licensing"
                },
                {
                    "LangKey": "mconfig",
                    "Link": "multi_config.html",
                    "Text": "Group Configuration"
                }
            ],
            "Text": "iLO Federation"
        },
        {
            "LangKey": "rc",
            "TabSet": "rc",
            "Tabs": [
                {
                    "LangKey": "launch",
                    "Link": "rc_info.html",
                    "Text": "Launch"
                },
                {
                    "LangKey": "vm",
                    "Link": "vm.html",
                    "Text": "Virtual Media"
                },
                {
                    "LangKey": "hotKey",
                    "Link": "rc_hotkeys.html",
                    "Text": "Hot Keys"
                },
                {
                    "LangKey": "security",
                    "Link": "admin_security_remote.html",
                    "Text": "Security"
                }
            ],
            "Text": "Remote Console & Media"
        },
        {
            "Features": "power_management",
            "LangKey": "pwrMgmt",
            "TabSet": "pwrMgmt",
            "Tabs": [
                {
                    "LangKey": "pwrServer",
                    "Link": "power_server.html",
                    "Text": "Server Power"
                },
                {
                    "LangKey": "pwrMeter",
                    "Link": "power_meter.html",
                    "Text": "Power Meter"
                },
                {
                    "LangKey": "pwrSettings",
                    "Link": "power_settings.html",
                    "Text": "Power Settings"
                },
                {
                    "LangKey": "pwr",
                    "Link": "info_system_power.html",
                    "Text": "Power"
                },
                {
                    "LangKey": "fans",
                    "Link": "info_system_fans.html",
                    "Text": "Fans"
                },
                {
                    "LangKey": "temp",
                    "Link": "info_system_temps.html",
                    "Text": "Temperatures"
                }
            ],
            "Text": "Power & Thermal"
        },
        {
            "Features": "ist",
            "LangKey": "IST",
            "TabSet": "ist",
            "Tabs": [
                {
                    "LangKey": "perfSettings",
                    "Link": "perf_settings.html",
                    "Text": "Settings"
                },
                {
                    "LangKey": "perfMonitoring",
                    "Link": "perf_monitor.html",
                    "Text": "Monitoring"
                },
                {
                    "LangKey": "perfAdvisory",
                    "Link": "perf_advisory.html",
                    "Text": "Workload Advisor"
                }
            ],
            "Text": "Performance"
        },
        {
            "Features": "dedicated_nic",
            "LangKey": "dedicateNIC",
            "TabSet": "net0",
            "Tabs": [
                {
                    "LangKey": "summary",
                    "Link": "network_summary.html?intf=0",
                    "Text": "Summary"
                },
                {
                    "LangKey": "general",
                    "Link": "network_general.html?intf=0",
                    "Text": "General"
                },
                {
                    "LangKey": "ipv4",
                    "Link": "network_ipv4.html?intf=0",
                    "Text": "IPv4"
                },
                {
                    "LangKey": "ipv6",
                    "Link": "network_ipv6.html?intf=0",
                    "Text": "IPv6"
                },
                {
                    "LangKey": "sntp",
                    "Link": "network_sntp.html?intf=0",
                    "Text": "SNTP"
                }
            ],
            "Text": "iLO Dedicated Network Port"
        },
        {
            "Features": "snp",
            "LangKey": "sharedNIC",
            "TabSet": "net1",
            "Tabs": [
                {
                    "LangKey": "summary",
                    "Link": "network_summary.html?intf=1",
                    "Text": "Summary"
                },
                {
                    "LangKey": "general",
                    "Link": "network_general.html?intf=1",
                    "Text": "General"
                },
                {
                    "LangKey": "ipv4",
                    "Link": "network_ipv4.html?intf=1",
                    "Text": "IPv4"
                },
                {
                    "LangKey": "ipv6",
                    "Link": "network_ipv6.html?intf=1",
                    "Text": "IPv6"
                },
                {
                    "LangKey": "sntp",
                    "Link": "network_sntp.html?intf=1",
                    "Text": "SNTP"
                }
            ],
            "Text": "Shared Network Port"
        },
        {
            "Features": "ers",
            "LangKey": "ers_nav_tab",
            "TabSet": "ers",
            "Tabs": [
                {
                    "LangKey": "ers_nav_tab_reg",
                    "Link": "admin_ers_cfg_d.html",
                    "Text": "Registration"
                },
                {
                    "LangKey": "ers_nav_tab_se",
                    "Link": "admin_ers_se.html",
                    "Text": "Service Events"
                },
                {
                    "LangKey": "ers_nav_tab_data",
                    "Link": "admin_ers_dc.html",
                    "Text": "Data Collections"
                }
            ],
            "Text": "Remote Support"
        },
        {
            "Features": "admin",
            "LangKey": "admin",
            "TabSet": "admin",
            "Tabs": [
                {
                    "LangKey": "usrAdm",
                    "Link": "admin_user.html",
                    "Text": "User Administration"
                },
                {
                    "LangKey": "dirGrp",
                    "Link": "admin_group.html",
                    "Text": "Directory Groups"
                },
                {
                    "LangKey": "bootOrder",
                    "Link": "boot_order.html",
                    "Text": "Boot Order"
                },
                {
                    "LangKey": "lic",
                    "Link": "admin_license.html",
                    "Text": "Licensing"
                },
                {
                    "LangKey": "kyMgr",
                    "Link": "admin_keymgr_eskm.html",
                    "Text": "Key Manager"
                },
                {
                    "LangKey": "lang",
                    "Link": "admin_language.html",
                    "Text": "Language"
                },
                {
                    "LangKey": "fwVerify",
                    "Link": "admin_fw_verify.html",
                    "Text": "Firmware Verification"
                }
            ],
            "Text": "Administration"
        },
        {
            "Features": "sec",
            "LangKey": "security",
            "TabSet": "security",
            "Tabs": [
                {
                    "LangKey": "accessSet",
                    "Link": "admin_settings.html",
                    "Text": "Access Settings"
                },
                {
                    "LangKey": "servicePort",
                    "Link": "admin_service_port.html",
                    "Text": "iLO Service Port"
                },
                {
                    "LangKey": "sshKey",
                    "Link": "admin_security_sshKey.html",
                    "Text": "Secure Shell Key"
                },
                {
                    "LangKey": "certMap",
                    "Link": "admin_security_certmap.html",
                    "Text": "Certificate Map"
                },
                {
                    "LangKey": "certauth",
                    "Link": "admin_security_certauth.html",
                    "Text": "CAC/Smartcard"
                },
                {
                    "LangKey": "sslCert",
                    "Link": "admin_security_sslCert.html",
                    "Text": "SSL Certificate"
                },
                {
                    "LangKey": "dir",
                    "Link": "admin_security_directory.html",
                    "Text": "Directory"
                },
                {
                    "LangKey": "encrypt",
                    "Link": "admin_security_encrypt.html",
                    "Text": "Encryption"
                },
                {
                    "LangKey": "hpSSO",
                    "Link": "admin_security_HPsso.html",
                    "Text": "HPE SSO"
                },
                {
                    "LangKey": "banner",
                    "Link": "admin_security_banner.html",
                    "Text": "Login Security Banner"
                }
            ],
            "Text": "Security"
        },
        {
            "Features": "Mgmt",
            "LangKey": "manage",
            "TabSet": "management",
            "Tabs": [
                {
                    "LangKey": "snmpSet",
                    "Link": "admin_manage.html",
                    "Text": "SNMP Settings"
                },
                {
                    "LangKey": "amail",
                    "Link": "admin_manage_alertmail.html",
                    "Text": "AlertMail"
                },
                {
                    "LangKey": "rslog",
                    "Link": "admin_manage_syslog.html",
                    "Text": "Remote Syslog"
                }
            ],
            "Text": "Management"
        },
        {
            "Features": "ipmanager",
            "LangKey": "HPE OneView",
            "Link": "info_ipmanager.html",
            "Text": "HPE OneView"
        },
        {
            "LangKey": "lifecycleMgmt",
            "TabSet": "lifecycle",
            "Tabs": [
                {
                    "LangKey": "alwaysIP",
                    "Link": "info_ip_always_on.html",
                    "Text": "Intelligent Provisioning"
                },
                {
                    "LangKey": "decommission",
                    "Link": "decommission.html",
                    "Text": "Decommission"
                },
                {
                    "LangKey": "backup",
                    "Link": "admin_backup.html",
                    "Text": "Backup & Restore"
                }
            ],
            "Text": "Lifecycle Management"
        }
    ]
}
```

## /redfish/v1/Managers/1/HostInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#HostInterfaceCollection.HostInterfaceCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/HostInterfaces",
    "@odata.type": "#HostInterfaceCollection.HostInterfaceCollection",
    "Description": "Configuration of Host Interfaces",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/HostInterfaces/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Host Interfaces"
}
```

## /redfish/v1/Managers/1/HostInterfaces/1

```{
    "@odata.context": "/redfish/v1/$metadata#HostInterface.HostInterface",
    "@odata.etag": "W/\"B34B5ADE\"",
    "@odata.id": "/redfish/v1/Managers/1/HostInterfaces/1",
    "@odata.type": "#HostInterface.v1_1_1.HostInterface",
    "ExternallyAccessible": false,
    "HostInterfaceType": "NetworkHostInterface",
    "Id": "1",
    "InterfaceEnabled": false,
    "ManagerEthernetInterface": {
        "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/3"
    },
    "Name": "USB Virtual Ethernet Interface",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/1/NetworkProtocol"
    },
    "Status": {
        "State": "Disabled"
    }
}
```

## /redfish/v1/Managers/1/LicenseService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOLicenseCollection.HpeiLOLicenseCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/LicenseService",
    "@odata.type": "#HpeiLOLicenseCollection.HpeiLOLicenseCollection",
    "Description": "iLO License Service View",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/LicenseService/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "iLO License Service"
}
```

## /redfish/v1/Managers/1/LicenseService/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOLicense.HpeiLOLicense",
    "@odata.etag": "W/\"B5838BDB\"",
    "@odata.id": "/redfish/v1/Managers/1/LicenseService/1",
    "@odata.type": "#HpeiLOLicense.v2_3_0.HpeiLOLicense",
    "Confirmation": {
        "Code": "",
        "Message": "Confirmed.",
        "Service": "www.hpe.com/glis",
        "Status": true
    },
    "ConfirmationRequest": {
        "EON": {
            "License": "iLO Advanced",
            "LicenseKey": "3Q898-LM9ZN-H7WTJ-6J8DS-MQ9LH",
            "Quantity": 1,
            "State": "confirmed"
        },
        "Signer": "iLO",
        "System": {
            "ChipId": "D53514189AF2D015",
            "Product": "ProLiant DL360 Gen10 Plus",
            "SerialNumber": "VYRBX9UJ4S"
        }
    },
    "Description": "iLO License View",
    "Id": "1",
    "License": "iLO Advanced",
    "LicenseClass": "FQL",
    "LicenseErr": "",
    "LicenseExpire": "",
    "LicenseFeatures": {
        "DirectoryAuth": true,
        "DowngradePolicy": true,
        "EmailAlert": true,
        "FWScan": true,
        "Federation": true,
        "Jitter": true,
        "KD": true,
        "KeyMgr": true,
        "MURC": true,
        "ODIM": false,
        "PowerReg": true,
        "RC": true,
        "Recovery": true,
        "RemoteSyslog": true,
        "Scrncap": true,
        "SecureErase": true,
        "SmartCard": true,
        "SuiteB": true,
        "TextCons": true,
        "VM": true,
        "VMScript": true,
        "VSPLogging": true
    },
    "LicenseInstallDate": "18 Aug 2021",
    "LicenseKey": "XXXXX-XXXXX-XXXXX-XXXXX-MQ9LH",
    "LicenseSeats": 1,
    "LicenseTier": "ADV",
    "LicenseType": "Perpetual",
    "Name": "iLO License"
}
```

## /redfish/v1/Managers/1/LogServices

```
```

## /redfish/v1/Managers/1/LogServices/IEL

```
```

## /redfish/v1/Managers/1/NetworkProtocol

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerNetworkProtocol.ManagerNetworkProtocol",
    "@odata.etag": "W/\"9134B0A3\"",
    "@odata.id": "/redfish/v1/Managers/1/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_0_0.ManagerNetworkProtocol",
    "FQDN": "",
    "HTTP": {
        "Port": 80,
        "ProtocolEnabled": true
    },
    "HTTPS": {
        "Port": 443,
        "ProtocolEnabled": true
    },
    "HostName": "ILOVYRBX9UJ4S",
    "IPMI": {
        "Port": 623,
        "ProtocolEnabled": false
    },
    "Id": "NetworkProtocol",
    "KVMIP": {
        "Port": 4443,
        "ProtocolEnabled": true
    },
    "Name": "Manager Network Services",
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
    },
    "SNMP": {
        "Port": 161,
        "ProtocolEnabled": true
    },
    "SSDP": {
        "NotifyIPv6Scope": "Site",
        "NotifyMulticastIntervalSeconds": 600,
        "NotifyTTL": 5,
        "Port": 1900,
        "ProtocolEnabled": true
    },
    "SSH": {
        "Port": 22,
        "ProtocolEnabled": true
    },
    "Status": {
        "State": "Enabled"
    },
    "VirtualMedia": {
        "Port": 17988,
        "ProtocolEnabled": true
    }
}
```

## /redfish/v1/Managers/1/RemoteSupportService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeRemoteSupport.HpeRemoteSupport",
    "@odata.etag": "W/\"BF0214E1\"",
    "@odata.id": "/redfish/v1/Managers/1/RemoteSupportService",
    "@odata.type": "#HpeRemoteSupport.v2_6_0.HpeRemoteSupport",
    "Actions": {
        "#HpeRemoteSupport.ClearServiceEventLog": {
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.ClearServiceEventLog"
        },
        "#HpeRemoteSupport.CompleteDirectConnectRegistration": {
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.CompleteDirectConnectRegistration"
        },
        "#HpeRemoteSupport.DisableRemoteSupport": {
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.DisableRemoteSupport"
        },
        "#HpeRemoteSupport.RegisterDeviceToRemoteSupport": {
            "ConnectionType@Redfish.AllowableValues": [
                "DirectConnect",
                "CentralConnect"
            ],
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.RegisterDeviceToRemoteSupport"
        },
        "#HpeRemoteSupport.ServerMaintenance": {
            "MaintenanceMode@Redfish.AllowableValues": [
                "Clear",
                "Set"
            ],
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.ServerMaintenance"
        },
        "#HpeRemoteSupport.TriggerDataCollection": {
            "DataType@Redfish.AllowableValues": [
                "ActiveHealthSystemData",
                "L2CollectionData"
            ],
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.TriggerDataCollection"
        },
        "#HpeRemoteSupport.TriggerTestEvent": {
            "target": "/redfish/v1/Managers/1/RemoteSupportService/Actions/HpeRemoteSupport.TriggerTestEvent"
        }
    },
    "Id": "RemoteSupportService",
    "LastTransmissionError": "No error",
    "LastTransmissionType": "NoTransmission",
    "MaintenanceModeEnabled": false,
    "ProxySettings": {},
    "RemoteSupportEnabled": false,
    "ServiceEventLogs": {
        "@odata.id": "/redfish/v1/Managers/1/RemoteSupportService/ServiceEventLogs"
    }
}
```

## /redfish/v1/Managers/1/RemoteSupportService/ServiceEventLogs

```{
    "@odata.context": "/redfish/v1/$metadata#LogEntryCollection.LogEntryCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/RemoteSupportService/ServiceEventLogs",
    "@odata.type": "#LogEntryCollection.LogEntryCollection",
    "Description": "Service Event Logs View",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Service Event Logs"
}
```

## /redfish/v1/Managers/1/SecurityService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSecurityService.HpeSecurityService",
    "@odata.etag": "W/\"E1869379\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService",
    "@odata.type": "#HpeSecurityService.v2_3_1.HpeSecurityService",
    "CurrentCipher": "ECDHE-RSA-AES256-GCM-SHA384",
    "Id": "SecurityService",
    "Links": {
        "CertAuth": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication"
        },
        "ESKM": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/ESKM"
        },
        "HttpsCert": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/HttpsCert"
        },
        "SSO": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SSO"
        },
        "SecurityDashboard": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard"
        }
    },
    "LoginSecurityBanner": {
        "IsEnabled": false
    },
    "PlatformCert": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/PlatformCert/Certificates"
        }
    },
    "PlatformCertUpdate": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/PlatformCertUpdate/Certificates"
        }
    },
    "SSHHostKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9gjASuefc09WXwOJVec3LbsCa0eenI+TMyoN718Nzq1OIMCgpYi7xHXxSoKq4MdLH2nUxtEp6pEflzenbuDWZKWtjEjmQ/syA0jGQAGRsoH8XXesQqiDhB05en9VNbHIRkKvzV3wcVYK9wLiJE6wEJhAbskYZ8tZTgPGZkIFemFOpDFVx5dyG/TkS85iZV+T2P3rTrnvaDYUCIP0FrXIcGegYjZxb5tDLKvZ6lNCf13jnjuyIGZXpfnZ8Bv79H7DuStRpIDwS7ATx7I7lusdGL/z1xWOiJY1yX0xnbCwO/hFVW5XpNZBqvyoML+W5TCoaNSux09ME/mdkqLBsO7jZ",
    "SecurityState": "Production",
    "SecurityState@Redfish.AllowableValues": [
        "Production",
        "HighSecurity",
        "FIPS"
    ],
    "SystemIAK": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SystemIAK/Certificates"
        }
    },
    "SystemIDevID": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SystemIDevID/Certificates"
        }
    },
    "iLOIDevID": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/iLOIDevID/Certificates"
        }
    },
    "iLOLDevID": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/iLOLDevID/Certificates"
        }
    }
}
```

## /redfish/v1/Managers/1/SecurityService/CertificateAuthentication

```{
    "@odata.context": "/redfish/v1/$metadata#HpeCertAuth.HpeCertAuth",
    "@odata.etag": "W/\"ACE7CC89\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication",
    "@odata.type": "#HpeCertAuth.v1_1_0.HpeCertAuth",
    "Actions": {
        "#HpeCertAuth.DeleteCRL": {
            "target": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication/Actions/HpeCertAuth.DeleteCRL"
        },
        "#HpeCertAuth.ImportCACertificate": {
            "target": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication/Actions/HpeCertAuth.ImportCACertificate"
        },
        "#HpeCertAuth.ImportCRL": {
            "target": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication/Actions/HpeCertAuth.ImportCRL"
        }
    },
    "CACertificates": {
        "@odata.id": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication/CACertificates"
    },
    "CRLIssuer": null,
    "CRLSerial": null,
    "CertificateLoginEnabled": false,
    "Id": "CertificateAuthentication",
    "LDAPCertificateNameMapping": "SANUPN",
    "Links": {
        "UserCertificateMapping": {
            "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping"
        }
    },
    "OCSPUri": "",
    "StrictCACModeEnabled": false
}
```

## /redfish/v1/Managers/1/SecurityService/CertificateAuthentication/CACertificates

```{
    "@odata.context": "/redfish/v1/$metadata#HpeCertificateCollection.HpeCertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/CertificateAuthentication/CACertificates",
    "@odata.type": "#HpeCertificateCollection.HpeCertificateCollection",
    "Description": "Trusted CA Certificates for Certificate Authentication",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "CA Certificates"
}
```

## /redfish/v1/Managers/1/SecurityService/ESKM

```{
    "@odata.context": "/redfish/v1/$metadata#HpeESKM.HpeESKM",
    "@odata.etag": "W/\"075B3A10\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/ESKM",
    "@odata.type": "#HpeESKM.v2_0_0.HpeESKM",
    "Actions": {
        "#HpeESKM.ClearESKMLog": {
            "target": "/redfish/v1/Managers/1/SecurityService/ESKM/Actions/HpeESKM.ClearESKMLog"
        },
        "#HpeESKM.TestESKMConnections": {
            "target": "/redfish/v1/Managers/1/SecurityService/ESKM/Actions/HpeESKM.TestESKMConnections"
        }
    },
    "Id": "ESKM",
    "KeyManagerConfig": {
        "AccountGroup": "",
        "AccountName": "ilo-b47af1bd4c94",
        "ESKMLocalCACertificateName": "",
        "ImportedCertificateIssuer": "",
        "ImportedCertificateSubject": ""
    },
    "KeyServerRedundancyReq": false,
    "PrimaryKeyServerAddress": null,
    "PrimaryKeyServerPort": null,
    "SecondaryKeyServerAddress": null,
    "SecondaryKeyServerPort": null
}
```

## /redfish/v1/Managers/1/SecurityService/HttpsCert

```{
    "@odata.context": "/redfish/v1/$metadata#HpeHttpsCert.HpeHttpsCert",
    "@odata.etag": "W/\"BC4E5327\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/HttpsCert",
    "@odata.type": "#HpeHttpsCert.v2_0_0.HpeHttpsCert",
    "Actions": {
        "#HpeHttpsCert.GenerateCSR": {
            "target": "/redfish/v1/Managers/1/SecurityService/HttpsCert/Actions/HpeHttpsCert.GenerateCSR"
        },
        "#HpeHttpsCert.ImportCertificate": {
            "target": "/redfish/v1/Managers/1/SecurityService/HttpsCert/Actions/HpeHttpsCert.ImportCertificate"
        }
    },
    "CertificateSigningRequest": null,
    "Id": "HttpsCert",
    "X509CertificateInformation": {
        "Issuer": "CN = Default Issuer (Do not trust), O = Hewlett Packard Enterprise, OU = ISS, L = Americas, ST = Houston, C = US",
        "SerialNumber": "e8:10:fe:1e:eb:2b:a0:b2",
        "Subject": "CN = ILOVYRBX9UJ4S, O = Hewlett Packard Enterprise, OU = ISS, L = Americas, ST = Houston, C = US",
        "ValidNotAfter": "2036-08-17T06:07:37Z",
        "ValidNotBefore": "2021-08-18T06:07:37Z"
    }
}
```

## /redfish/v1/Managers/1/SecurityService/PlatformCert/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/PlatformCert/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "Platform Certificate Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Platform Certificate Collection"
}
```

## /redfish/v1/Managers/1/SecurityService/PlatformCertUpdate/Certificates

```null
```

## /redfish/v1/Managers/1/SecurityService/SSO

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSSO.HpeiLOSSO",
    "@odata.etag": "W/\"40B50C2B\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SSO",
    "@odata.type": "#HpeiLOSSO.v2_0_0.HpeiLOSSO",
    "Actions": {
        "#HpeiLOSSO.DeleteAllSSORecords": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.DeleteAllSSORecords"
        },
        "#HpeiLOSSO.DeleteSSORecordbyNumber": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.DeleteSSORecordbyNumber"
        },
        "#HpeiLOSSO.ImportCertificate": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.ImportCertificate"
        },
        "#HpeiLOSSO.ImportDNSName": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.ImportDNSName"
        }
    },
    "Id": "SSO",
    "ManagerTrustedCertificates": [
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SSO/#ManagerTrustedCertificates/1/",
            "Certificate": "-----BEGIN CERTIFICATE-----\nMIIEHzCCAwegAwIBAgICfDUwDQYJKoZIhvcNAQELBQAwejELMAkGA1UEBhMCVVMxEzARBgNVBAgM\nCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEjMCEGA1UECgwaSGV3bGV0dCBQYWNrYXJk\nIEVudGVycHJpc2UxHTAbBgNVBAMMFE9uZVZpZXczLmNvbXBsYWIubGFiMB4XDTE5MDcxMTIwNDk1\nM1oXDTI5MDcxMTIwNDk1M1owejELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQ\nBgNVBAcMCVBhbG8gQWx0bzEjMCEGA1UECgwaSGV3bGV0dCBQYWNrYXJkIEVudGVycHJpc2UxHTAb\nBgNVBAMMFE9uZVZpZXczLmNvbXBsYWIubGFiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC\nAQEAtNa25GpSVANlMtL8UhNjSNKpDcCLMbfrVesrO2b89u/rxpuaQRPu4B0ykFjmdmkKY6sFJPMl\nL3crORMSzonWseoBP2r2I92as+iLL84/Xm7OpBKMBU2MNxxNoM7DEDJQK7MKcv4mMXPP5QIAGNr3\nbiItjJvNTsJBOAdEtRRJsfj+27yw2A/bVmrnBvx17ewYxjY9xSzmPdcnMgHLcWALeN09w1g8FWLw\nbJp91nDbIEycGWwuLQDtv0p4291OVoaM5SQLcBF7zezovU13A55vd0eDtHHJeKqxk7fwZ6kEvEoh\nzodTqH2UPCqrGrrst0iKAfHCVlws4y1iJh3E1b6NqwIDAQABo4GuMIGrMIGJBgNVHREEgYEwf4IU\nT25lVmlldzMuY29tcGxhYi5sYWKCCE9uZVZpZXczhwQKHZh8gg0xMC4yOS4xNTIuMTI0hxD+gAAA\nAAAAAH6AzTdUhmTnghlmZTgwOjo3ZTgwOmNkMzc6NTQ4Njo2NGU3ghtbZmU4MDo6N2U4MDpjZDM3\nOjU0ODY6NjRlN10wHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMA0GCSqGSIb3DQEBCwUA\nA4IBAQAoGZzuJ7sI9+5XPs3E3xyzr9A98KoaJKg9toQogcoT0zl6agOdImqzrV6HOklaRTRKWswV\nQwpLGkfdT/YkQAx6fnfhAK7lB1+Fz8RWFE7440ooLS0tMchhhhW/TL1ZGG3Ec3HDTjYjwMlfkTqE\nTkygdd+rh97SxuDRryTUukBnrH++m/IQfB9nKSOVIjdfgJ7mbpOr5tc5+ozIwgDoMW4kXZV/gVPJ\nwCwf3vEZB/qjxru87xNmUErFQICqcvzATMEFMvCoOzCGwKua6uWTP1B7rfpRwnm3vp+mKNy8+sut\nTm5zDMc3m4c53uDGlaal/aGfmZAsH240gGaYPltFj/tI\n-----END CERTIFICATE-----",
            "CertificateDetails": {
                "Issuer": "OneView3.complab.lab",
                "Subject": "OneView3.complab.lab",
                "ValidNotAfter": "2029-07-11T20:49:53Z",
                "ValidNotBefore": "2019-07-11T20:49:53Z"
            },
            "RecordType": "Certificate",
            "SerialNumber": 1,
            "ServerName": "OneView3.complab.lab",
            "Status": "OK"
        }
    ],
    "SSOsettings": {
        "AdminPrivilege": {
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
        "OperatorPrivilege": {
            "HostBIOSConfigPriv": true,
            "HostNICConfigPriv": false,
            "HostStorageConfigPriv": false,
            "LoginPriv": true,
            "RemoteConsolePriv": true,
            "SystemRecoveryConfigPriv": false,
            "UserConfigPriv": false,
            "VirtualMediaPriv": true,
            "VirtualPowerAndResetPriv": true,
            "iLOConfigPriv": false
        },
        "SSOTrustMode": "TrustbyCert",
        "UserPrivilege": {
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
        }
    }
}
```

## /redfish/v1/Managers/1/SecurityService/SSO/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSSO.HpeiLOSSO",
    "@odata.etag": "W/\"40B50C2B\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SSO",
    "@odata.type": "#HpeiLOSSO.v2_0_0.HpeiLOSSO",
    "Actions": {
        "#HpeiLOSSO.DeleteAllSSORecords": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.DeleteAllSSORecords"
        },
        "#HpeiLOSSO.DeleteSSORecordbyNumber": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.DeleteSSORecordbyNumber"
        },
        "#HpeiLOSSO.ImportCertificate": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.ImportCertificate"
        },
        "#HpeiLOSSO.ImportDNSName": {
            "target": "/redfish/v1/Managers/1/SecurityService/SSO/Actions/HpeiLOSSO.ImportDNSName"
        }
    },
    "Id": "SSO",
    "ManagerTrustedCertificates": [
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SSO/#ManagerTrustedCertificates/1/",
            "Certificate": "-----BEGIN CERTIFICATE-----\nMIIEHzCCAwegAwIBAgICfDUwDQYJKoZIhvcNAQELBQAwejELMAkGA1UEBhMCVVMxEzARBgNVBAgM\nCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEjMCEGA1UECgwaSGV3bGV0dCBQYWNrYXJk\nIEVudGVycHJpc2UxHTAbBgNVBAMMFE9uZVZpZXczLmNvbXBsYWIubGFiMB4XDTE5MDcxMTIwNDk1\nM1oXDTI5MDcxMTIwNDk1M1owejELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQ\nBgNVBAcMCVBhbG8gQWx0bzEjMCEGA1UECgwaSGV3bGV0dCBQYWNrYXJkIEVudGVycHJpc2UxHTAb\nBgNVBAMMFE9uZVZpZXczLmNvbXBsYWIubGFiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC\nAQEAtNa25GpSVANlMtL8UhNjSNKpDcCLMbfrVesrO2b89u/rxpuaQRPu4B0ykFjmdmkKY6sFJPMl\nL3crORMSzonWseoBP2r2I92as+iLL84/Xm7OpBKMBU2MNxxNoM7DEDJQK7MKcv4mMXPP5QIAGNr3\nbiItjJvNTsJBOAdEtRRJsfj+27yw2A/bVmrnBvx17ewYxjY9xSzmPdcnMgHLcWALeN09w1g8FWLw\nbJp91nDbIEycGWwuLQDtv0p4291OVoaM5SQLcBF7zezovU13A55vd0eDtHHJeKqxk7fwZ6kEvEoh\nzodTqH2UPCqrGrrst0iKAfHCVlws4y1iJh3E1b6NqwIDAQABo4GuMIGrMIGJBgNVHREEgYEwf4IU\nT25lVmlldzMuY29tcGxhYi5sYWKCCE9uZVZpZXczhwQKHZh8gg0xMC4yOS4xNTIuMTI0hxD+gAAA\nAAAAAH6AzTdUhmTnghlmZTgwOjo3ZTgwOmNkMzc6NTQ4Njo2NGU3ghtbZmU4MDo6N2U4MDpjZDM3\nOjU0ODY6NjRlN10wHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMA0GCSqGSIb3DQEBCwUA\nA4IBAQAoGZzuJ7sI9+5XPs3E3xyzr9A98KoaJKg9toQogcoT0zl6agOdImqzrV6HOklaRTRKWswV\nQwpLGkfdT/YkQAx6fnfhAK7lB1+Fz8RWFE7440ooLS0tMchhhhW/TL1ZGG3Ec3HDTjYjwMlfkTqE\nTkygdd+rh97SxuDRryTUukBnrH++m/IQfB9nKSOVIjdfgJ7mbpOr5tc5+ozIwgDoMW4kXZV/gVPJ\nwCwf3vEZB/qjxru87xNmUErFQICqcvzATMEFMvCoOzCGwKua6uWTP1B7rfpRwnm3vp+mKNy8+sut\nTm5zDMc3m4c53uDGlaal/aGfmZAsH240gGaYPltFj/tI\n-----END CERTIFICATE-----",
            "CertificateDetails": {
                "Issuer": "OneView3.complab.lab",
                "Subject": "OneView3.complab.lab",
                "ValidNotAfter": "2029-07-11T20:49:53Z",
                "ValidNotBefore": "2019-07-11T20:49:53Z"
            },
            "RecordType": "Certificate",
            "SerialNumber": 1,
            "ServerName": "OneView3.complab.lab",
            "Status": "OK"
        }
    ],
    "SSOsettings": {
        "AdminPrivilege": {
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
        "OperatorPrivilege": {
            "HostBIOSConfigPriv": true,
            "HostNICConfigPriv": false,
            "HostStorageConfigPriv": false,
            "LoginPriv": true,
            "RemoteConsolePriv": true,
            "SystemRecoveryConfigPriv": false,
            "UserConfigPriv": false,
            "VirtualMediaPriv": true,
            "VirtualPowerAndResetPriv": true,
            "iLOConfigPriv": false
        },
        "SSOTrustMode": "TrustbyCert",
        "UserPrivilege": {
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
        }
    }
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityDashboard.HpeiLOSecurityDashboard",
    "@odata.etag": "W/\"543055B3\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard",
    "@odata.type": "#HpeiLOSecurityDashboard.v1_0_0.HpeiLOSecurityDashboard",
    "Id": "SecurityDashboard",
    "OverallSecurityStatus": "Risk",
    "SecurityParameters": {
        "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams"
    },
    "ServerConfigurationLockStatus": "Disabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParamCollection.HpeiLOSecurityParamCollection",
    "@odata.etag": "W/\"F25B88E1\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams",
    "@odata.type": "#HpeiLOSecurityParamCollection.HpeiLOSecurityParamCollection",
    "Description": "iLO Security Parameter Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/0"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/1"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/2"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/3"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/4"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/5"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/6"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/7"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/8"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/9"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/10"
        }
    ],
    "Members@odata.count": 11,
    "Name": "Security Parameter Collection"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/0

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/0",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Id": "0",
    "Ignore": false,
    "Name": "Security Override Switch",
    "SecurityStatus": "Ok",
    "State": "Off"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/1",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Id": "1",
    "Ignore": false,
    "Name": "IPMI/DCMI Over LAN",
    "SecurityStatus": "Ok",
    "State": "Disabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/10

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/10",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Id": "10",
    "Ignore": false,
    "Name": "Last Firmware Scan Result",
    "SecurityStatus": "Ok",
    "State": "Ok"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/2

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/2",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Id": "2",
    "Ignore": false,
    "Name": "Minimum Password Length",
    "SecurityStatus": "Ok",
    "State": "Ok"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/3",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Description": "The Require Login for iLO RBSU setting is disabled. This configuration allows unauthenticated iLO access through the UEFI System Utilities.",
    "Id": "3",
    "Ignore": false,
    "Name": "Require Login for iLO RBSU",
    "RecommendedAction": "Enable the Require Login for iLO RBSU setting.",
    "SecurityStatus": "Risk",
    "State": "Disabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/4

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/4",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Id": "4",
    "Ignore": false,
    "Name": "Authentication Failure Logging",
    "SecurityStatus": "Ok",
    "State": "Enabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/5

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/5",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Description": "The UEFI Secure Boot setting is disabled. In this configuration, the UEFI system firmware does not validate the boot loader, Option ROM firmware, and other system software executables for trusted signatures. This configuration breaks the chain of trust established by iLO from power-on",
    "Id": "5",
    "Ignore": false,
    "Name": "Secure Boot",
    "RecommendedAction": "Enable the Secure Boot setting in the UEFI System Utilities.",
    "SecurityStatus": "Risk",
    "State": "Disabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/6

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/6",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Description": "The Password Complexity setting is disabled. This configuration increases system vulnerability to attack.",
    "Id": "6",
    "Ignore": false,
    "Name": "Password Complexity",
    "RecommendedAction": "Enable the \"Password Complexity\" setting.",
    "SecurityStatus": "Risk",
    "State": "Disabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/7

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/7",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Id": "7",
    "Ignore": false,
    "Name": "Require Host Authentication",
    "SecurityStatus": "Ok",
    "State": "Disabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/8

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/8",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Description": "SNMPv1 is enabled. This configuration increases system vulnerability to attack.",
    "Id": "8",
    "Ignore": false,
    "Name": "SNMPv1",
    "RecommendedAction": "Disable the SNMPv1 protocol.",
    "SecurityStatus": "Risk",
    "State": "Enabled"
}
```

## /redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/9

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSecurityParam.HpeiLOSecurityParam",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SecurityDashboard/SecurityParams/9",
    "@odata.type": "#HpeiLOSecurityParam.v1_1_0.HpeiLOSecurityParam",
    "Description": "Management processor's default self-signed certificate is in use.",
    "Id": "9",
    "Ignore": false,
    "Name": "Default SSL Certificate In Use",
    "RecommendedAction": "Import a certificate signed by a trusted certificate authority.",
    "SecurityStatus": "Risk",
    "State": "True"
}
```

## /redfish/v1/Managers/1/SecurityService/SystemIAK/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SystemIAK/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "System IAK Certificate Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "System IAK Certificate Collection"
}
```

## /redfish/v1/Managers/1/SecurityService/SystemIDevID/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/SystemIDevID/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "System Dev ID Certificate Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "System Dev ID Certificate Collection"
}
```

## /redfish/v1/Managers/1/SecurityService/iLOIDevID/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/iLOIDevID/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "iLO IDevID Certificate Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "iLO IDevID Certificate Collection"
}
```

## /redfish/v1/Managers/1/SecurityService/iLOLDevID/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Managers/1/SecurityService/iLOLDevID/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "iLO LDevID Certificate Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "iLO LDevID Certificate Collection"
}
```

## /redfish/v1/Managers/1/SerialInterface

```{
    "@odata.context": "/redfish/v1/$metadata#SerialInterfaceCollection.SerialInterfaceCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/SerialInterface",
    "@odata.type": "#SerialInterfaceCollection.SerialInterfaceCollection",
    "Description": "iLO Serial Interface Settings",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/SerialInterface/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Serial Interface"
}
```

## /redfish/v1/Managers/1/SerialInterface/1

```{
    "@odata.context": "/redfish/v1/$metadata#SerialInterface.SerialInterface",
    "@odata.etag": "W/\"C62A0798\"",
    "@odata.id": "/redfish/v1/Managers/1/SerialInterface/1",
    "@odata.type": "#SerialInterface.v1_1_7.SerialInterface",
    "BitRate": "9600",
    "Description": "Serial Interface",
    "Id": "1",
    "InterfaceEnabled": true,
    "Name": "SerialInterface"
}
```

## /redfish/v1/Managers/1/SnmpService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOSnmpService.HpeiLOSnmpService",
    "@odata.etag": "W/\"0A3B3DB7\"",
    "@odata.id": "/redfish/v1/Managers/1/SnmpService",
    "@odata.type": "#HpeiLOSnmpService.v2_3_0.HpeiLOSnmpService",
    "Actions": {
        "#HpeiLOSnmpService.SendSNMPTestAlert": {
            "target": "/redfish/v1/Managers/1/SnmpService/Actions/HpeiLOSnmpService.SendSNMPTestAlert"
        }
    },
    "AlertDestinationAssociations": [
        {
            "SNMPAlertProtocol": "SNMPv3Trap",
            "SecurityName": "oneview_5441437a626f38457739726b"
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        },
        {
            "SNMPAlertProtocol": null,
            "SecurityName": null
        }
    ],
    "AlertDestinations": [
        "10.29.152.124",
        null,
        null,
        null,
        null,
        null,
        null,
        null
    ],
    "AlertsEnabled": true,
    "Contact": "",
    "Description": "SNMP Service Status",
    "Id": "SnmpService",
    "Location": "",
    "Name": "SNMP Service",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSnmpServiceExt.HpeiLOSnmpServiceExt",
            "@odata.type": "#HpeiLOSnmpServiceExt.v2_0_0.HpeiLOSnmpServiceExt",
            "SNMPColdStartTrapBroadcast": true
        }
    },
    "PeriodicHSATrapConfig": "Disabled",
    "ReadCommunities": [
        "",
        "",
        ""
    ],
    "Role": "",
    "RoleDetail": "",
    "SNMPAlertDestinations": {
        "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPAlertDestinations"
    },
    "SNMPUsers": {
        "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPUsers"
    },
    "SNMPv1Enabled": true,
    "SNMPv3EngineID": "0x800000E804324D323133323034374B",
    "SNMPv3InformRetryAttempt": 2,
    "SNMPv3InformRetryIntervalSeconds": 15,
    "Status": {
        "State": "Enabled"
    },
    "TrapCommunities": [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    "TrapSourceHostname": "Manager",
    "Users": [
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "SHA",
            "PrivacyProtocol": "AES",
            "SecurityName": "oneview_5441437a626f38457739726b",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        },
        {
            "AuthProtocol": "MD5",
            "PrivacyProtocol": "DES",
            "SecurityName": "",
            "UserEngineID": null
        }
    ]
}
```

## /redfish/v1/Managers/1/SnmpService/SNMPAlertDestinations

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSNMPAlertDestinationCollection.HpeSNMPAlertDestinationCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPAlertDestinations",
    "@odata.type": "#HpeSNMPAlertDestinationCollection.HpeSNMPAlertDestinationCollection",
    "Description": "SNMP Alert Destination Collection view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPAlertDestinations/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "SNMP Alert Destination Collection"
}
```

## /redfish/v1/Managers/1/SnmpService/SNMPAlertDestinations/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSNMPAlertDestination.HpeSNMPAlertDestination",
    "@odata.etag": "W/\"A45D0C9F\"",
    "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPAlertDestinations/1",
    "@odata.type": "#HpeSNMPAlertDestination.v2_0_0.HpeSNMPAlertDestination",
    "AlertDestination": "10.29.152.124",
    "Id": "1",
    "SNMPAlertProtocol": "SNMPv3Trap",
    "SNMPv3User": {
        "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPUsers/3"
    },
    "SecurityName": "oneview_5441437a626f38457739726b",
    "TrapCommunity": ""
}
```

## /redfish/v1/Managers/1/SnmpService/SNMPUsers

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSNMPUsersCollection.HpeSNMPUsersCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPUsers",
    "@odata.type": "#HpeSNMPUsersCollection.HpeSNMPUsersCollection",
    "Description": "SNMPv3 Users Collection view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPUsers/3"
        }
    ],
    "Members@odata.count": 1,
    "Name": "SNMPv3 User Collection"
}
```

## /redfish/v1/Managers/1/SnmpService/SNMPUsers/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSNMPUser.HpeSNMPUser",
    "@odata.etag": "W/\"587E6648\"",
    "@odata.id": "/redfish/v1/Managers/1/SnmpService/SNMPUsers/3",
    "@odata.type": "#HpeSNMPUser.v2_1_0.HpeSNMPUser",
    "AuthProtocol": "SHA",
    "Id": "3",
    "PrivacyProtocol": "AES",
    "SecurityName": "oneview_5441437a626f38457739726b",
    "UserEngineID": null
}
```

## /redfish/v1/Managers/1/VirtualMedia

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMediaCollection.VirtualMediaCollection",
    "@odata.etag": "W/\"570254F2\"",
    "@odata.id": "/redfish/v1/Managers/1/VirtualMedia",
    "@odata.type": "#VirtualMediaCollection.VirtualMediaCollection",
    "Description": "iLO Virtual Media Services Settings",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/1/VirtualMedia/1"
        },
        {
            "@odata.id": "/redfish/v1/Managers/1/VirtualMedia/2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Virtual Media Services"
}
```

## /redfish/v1/Managers/1/VirtualMedia/1

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.etag": "W/\"3B0F66BA\"",
    "@odata.id": "/redfish/v1/Managers/1/VirtualMedia/1",
    "@odata.type": "#VirtualMedia.v1_2_0.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/1/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/1/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "NotConnected",
    "Description": "Virtual Removable Media",
    "Id": "1",
    "Image": "",
    "Inserted": false,
    "MediaTypes": [
        "Floppy",
        "USBStick"
    ],
    "Name": "VirtualMedia",
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
    },
    "WriteProtected": true
}
```

## /redfish/v1/Managers/1/VirtualMedia/2

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.etag": "W/\"14700DD6\"",
    "@odata.id": "/redfish/v1/Managers/1/VirtualMedia/2",
    "@odata.type": "#VirtualMedia.v1_2_0.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "NotConnected",
    "Description": "Virtual Removable Media",
    "Id": "2",
    "Image": "",
    "Inserted": false,
    "MediaTypes": [
        "CD",
        "DVD"
    ],
    "Name": "VirtualMedia",
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
    },
    "WriteProtected": true
}
```

