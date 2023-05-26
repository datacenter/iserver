# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
Cisco | UCSS-S3260

## /redfish/v1/Managers

```{
    "@odata.context": "/redfish/v1/$metadata#Managers",
    "@odata.id": "/redfish/v1/Managers",
    "@odata.type": "#ManagerCollection.ManagerCollection",
    "Description": "Collection of Managers",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Manager Collection"
}
```

## /redfish/v1/Managers/BMC1

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/BMC1/Actions/Manager.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.BiosFwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.BiosFwActivate"
            },
            "#CiscoUCSExtensions.ExportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.ExportConfig"
            },
            "#CiscoUCSExtensions.FwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.FwActivate"
            },
            "#CiscoUCSExtensions.ImportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.ImportConfig"
            },
            "#CiscoUCSExtensions.TechSupportExport": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.TechSupportExport"
            }
        }
    },
    "AutoDSTEnabled": false,
    "CommandShell": {
        "ConnectTypesSupported": [
            "IPMI"
        ],
        "ServiceEnabled": false
    },
    "Description": "",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/BMC1/EthernetInterfaces"
    },
    "FirmwareVersion": "4.1(3d)",
    "GraphicalConsole": {
        "ConnectTypesSupported": [
            "KVMIP"
        ],
        "MaxConcurrentSessions": 4,
        "ServiceEnabled": true
    },
    "Id": "BMC1",
    "Links": {
        "ManagerForChassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1"
            }
        ],
        "ManagerForServers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808"
            }
        ],
        "ManagerInChassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
        }
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Managers/BMC1/LogServices"
    },
    "ManagerType": "BMC",
    "Model": "UCSC-C3K-M4SRB",
    "Name": "Baseboard Management Controller",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/BMC1/NetworkProtocol"
    },
    "RemoteAccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "RemoteRedfishServiceUri": "/redfish/v1",
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/BMC1/SerialInterfaces"
    },
    "ServiceEntryPointUUID": "937E6EE7-0EA5-42CE-9EAE-A960BF1F0BAD",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "937E6EE7-0EA5-42CE-9EAE-A960BF1F0BAD",
    "VirtualMedia": {
        "@odata.id": "/redfish/v1/Managers/BMC1/VirtualMedia"
    }
}
```

## /redfish/v1/Managers/BMC1/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/EthernetInterfaces",
    "@odata.id": "/redfish/v1/Managers/BMC1/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this Manager",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/EthernetInterfaces/NICs"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Managers/BMC1/EthernetInterfaces/NICs

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/EthernetInterfaces/NICs",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "AutoNeg": false,
    "DHCPv4": {
        "DHCPEnabled": false,
        "UseDNSServers": false,
        "UseDomainName": false,
        "UseGateway": false,
        "UseNTPServers": false,
        "UseStaticRoutes": false
    },
    "DHCPv6": {
        "OperatingMode": "Disabled",
        "UseDNSServers": false,
        "UseDomainName": false,
        "UseNTPServers": false
    },
    "Description": "Manager Network Interface",
    "FullDuplex": false,
    "HostName": "ynas-eu-spdc-FCH21067808",
    "IPv4Addresses": [
        {
            "Address": "10.58.50.35",
            "AddressOrigin": "Static",
            "Gateway": "10.58.50.62",
            "SubnetMask": "255.255.255.224"
        }
    ],
    "IPv6Addresses": [
        {
            "Address": "::",
            "AddressOrigin": "Static",
            "PrefixLength": 64
        }
    ],
    "IPv6DefaultGateway": "::",
    "IPv6StaticDefaultGateways": [
        {
            "Address": "::"
        }
    ],
    "Id": "NICs",
    "InterfaceEnabled": true,
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
        }
    },
    "MACAddress": "70:DB:98:06:7D:71",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "PermanentMACAddress": "70:DB:98:06:7D:71",
    "StatelessAddressAutoConfig": {
        "IPv4AutoConfigEnabled": false,
        "IPv6AutoConfigEnabled": false
    },
    "StaticNameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "VLAN": {
        "VLANEnable": false,
        "VLANId": 12
    }
}
```

## /redfish/v1/Managers/BMC1/LogServices

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices",
    "@odata.type": "#LogServiceCollection.LogServiceCollection",
    "Description": "Collection of Log Services for this Manager",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Log Service Collection"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL",
    "@odata.type": "#LogService.v1_1_1.LogService",
    "Actions": {
        "#LogService.ClearLog": {
            "target": "/redfish/v1/Managers/BMC1/LogServices/SEL/Actions/LogService.ClearLog"
        }
    },
    "DateTime": "Tue Nov 29 12:04:25 2022",
    "DateTimeLocalOffset": "+01:00",
    "Description": "SEL Log Service",
    "Entries": {
        "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries"
    },
    "Id": "SEL",
    "LogEntryType": "SEL",
    "MaxNumberOfRecords": 3008,
    "Name": "SEL Log Service",
    "OverWritePolicy": "NeverOverWrites",
    "ServiceEnabled": true
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries",
    "@odata.type": "#LogEntryCollection.LogEntryCollection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1164",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:19:21 ",
            "Description": "Log Entry 1164",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1164",
            "EventTimestamp": "2022-06-13 12:19:21 ",
            "EventType": "ResourceAdded",
            "Id": "1164",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1164"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1163",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:19:16 ",
            "Description": "Log Entry 1163",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1163",
            "EventTimestamp": "2022-06-13 12:19:16 ",
            "EventType": "StatusChange",
            "Id": "1163",
            "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
            "Name": "Log Entry 1163"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1162",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:19:16 ",
            "Description": "Log Entry 1162",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1162",
            "EventTimestamp": "2022-06-13 12:19:16 ",
            "EventType": "Alert",
            "Id": "1162",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
            "Name": "Log Entry 1162"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1161",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:17:54 ",
            "Description": "Log Entry 1161",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1161",
            "EventTimestamp": "2022-06-13 12:17:54 ",
            "EventType": "StatusChange",
            "Id": "1161",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
            "Name": "Log Entry 1161"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1160",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:17:54 ",
            "Description": "Log Entry 1160",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1160",
            "EventTimestamp": "2022-06-13 12:17:54 ",
            "EventType": "StatusChange",
            "Id": "1160",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
            "Name": "Log Entry 1160"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1159",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:17:33 ",
            "Description": "Log Entry 1159",
            "EntryCode": "Device Removed / Device Absent",
            "EntryType": "SEL",
            "EventId": "1159",
            "EventTimestamp": "2022-06-13 12:17:33 ",
            "EventType": "ResourceRemoved",
            "Id": "1159",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
            "Name": "Log Entry 1159"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1158",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 12:17:28 ",
            "Description": "Log Entry 1158",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1158",
            "EventTimestamp": "2022-06-13 12:17:28 ",
            "EventType": "Alert",
            "Id": "1158",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
            "Name": "Log Entry 1158"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1157",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 08:46:05 ",
            "Description": "Log Entry 1157",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1157",
            "EventTimestamp": "2022-06-13 08:46:05 ",
            "EventType": "ResourceAdded",
            "Id": "1157",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1157"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1156",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 08:45:59 ",
            "Description": "Log Entry 1156",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1156",
            "EventTimestamp": "2022-06-13 08:45:59 ",
            "EventType": "StatusChange",
            "Id": "1156",
            "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
            "Name": "Log Entry 1156"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1155",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 08:45:59 ",
            "Description": "Log Entry 1155",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1155",
            "EventTimestamp": "2022-06-13 08:45:59 ",
            "EventType": "Alert",
            "Id": "1155",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
            "Name": "Log Entry 1155"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1154",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 08:44:41 ",
            "Description": "Log Entry 1154",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1154",
            "EventTimestamp": "2022-06-13 08:44:41 ",
            "EventType": "StatusChange",
            "Id": "1154",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
            "Name": "Log Entry 1154"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1153",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 08:44:41 ",
            "Description": "Log Entry 1153",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1153",
            "EventTimestamp": "2022-06-13 08:44:41 ",
            "EventType": "StatusChange",
            "Id": "1153",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
            "Name": "Log Entry 1153"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1152",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-13 08:44:09 ",
            "Description": "Log Entry 1152",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1152",
            "EventTimestamp": "2022-06-13 08:44:09 ",
            "EventType": "ResourceAdded",
            "Id": "1152",
            "Message": "MAIN_POWER_PRS: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1152"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1151",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1151",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1151",
            "EventTimestamp": "[System Boot]",
            "EventType": "StatusChange",
            "Id": "1151",
            "Message": "LED_HLTH_STATUS: Platform sensor, GREEN was asserted",
            "Name": "Log Entry 1151"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1150",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1150",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1150",
            "EventTimestamp": "[System Boot]",
            "EventType": "StatusChange",
            "Id": "1150",
            "Message": "LED_HLTH_STATUS: Platform sensor, ON event was asserted",
            "Name": "Log Entry 1150"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1149",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1149",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1149",
            "EventTimestamp": "[System Boot]",
            "EventType": "ResourceAdded",
            "Id": "1149",
            "Message": "P1_PRESENT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1149"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1148",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1148",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1148",
            "EventTimestamp": "[System Boot]",
            "EventType": "ResourceAdded",
            "Id": "1148",
            "Message": "SB_MEZZ1_PRES: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1148"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1147",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1147",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1147",
            "EventTimestamp": "[System Boot]",
            "EventType": "ResourceAdded",
            "Id": "1147",
            "Message": "P2_PRESENT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1147"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1146",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1146",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1146",
            "EventTimestamp": "[System Boot]",
            "EventType": "ResourceAdded",
            "Id": "1146",
            "Message": "SB_BOOTSSD2_PRES: Drive Slot sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1146"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1145",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1145",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1145",
            "EventTimestamp": "[System Boot]",
            "EventType": "ResourceAdded",
            "Id": "1145",
            "Message": "SB_BOOTSSD1_PRES: Drive Slot sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1145"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1144",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1144",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1144",
            "EventTimestamp": "[System Boot]",
            "EventType": "StatusChange",
            "Id": "1144",
            "Message": "LED_TEMP_STATUS: Platform sensor, GREEN was asserted",
            "Name": "Log Entry 1144"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1143",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1143",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1143",
            "EventTimestamp": "[System Boot]",
            "EventType": "StatusChange",
            "Id": "1143",
            "Message": "LED_TEMP_STATUS: Platform sensor, ON event was asserted",
            "Name": "Log Entry 1143"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1142",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "[System Boot]",
            "Description": "Log Entry 1142",
            "EntryCode": "Predictive Failure deasserted",
            "EntryType": "SEL",
            "EventId": "1142",
            "EventTimestamp": "[System Boot]",
            "EventType": "Alert",
            "Id": "1142",
            "Message": "FRU_MB POWER_ON_FAIL: Platform sensor for FRU_MB, Predictive Failure deasserted",
            "Name": "Log Entry 1142"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1141",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:45:53 ",
            "Description": "Log Entry 1141",
            "EntryCode": "Device Removed / Device Absent",
            "EntryType": "SEL",
            "EventId": "1141",
            "EventTimestamp": "2022-06-08 16:45:53 ",
            "EventType": "ResourceRemoved",
            "Id": "1141",
            "Message": "MAIN_POWER_PRS: Presence sensor, Device Removed / Device Absent was asserted",
            "Name": "Log Entry 1141"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1140",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:45:52 ",
            "Description": "Log Entry 1140",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1140",
            "EventTimestamp": "2022-06-08 16:45:52 ",
            "EventType": "Alert",
            "Id": "1140",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
            "Name": "Log Entry 1140"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1139",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:43:36 ",
            "Description": "Log Entry 1139",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1139",
            "EventTimestamp": "2022-06-08 16:43:36 ",
            "EventType": "ResourceAdded",
            "Id": "1139",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1139"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1138",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:43:31 ",
            "Description": "Log Entry 1138",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1138",
            "EventTimestamp": "2022-06-08 16:43:31 ",
            "EventType": "StatusChange",
            "Id": "1138",
            "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
            "Name": "Log Entry 1138"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1137",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:43:30 ",
            "Description": "Log Entry 1137",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1137",
            "EventTimestamp": "2022-06-08 16:43:30 ",
            "EventType": "Alert",
            "Id": "1137",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
            "Name": "Log Entry 1137"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1136",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:42:12 ",
            "Description": "Log Entry 1136",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1136",
            "EventTimestamp": "2022-06-08 16:42:12 ",
            "EventType": "StatusChange",
            "Id": "1136",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
            "Name": "Log Entry 1136"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1135",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:42:12 ",
            "Description": "Log Entry 1135",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1135",
            "EventTimestamp": "2022-06-08 16:42:12 ",
            "EventType": "StatusChange",
            "Id": "1135",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
            "Name": "Log Entry 1135"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1134",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:41:45 ",
            "Description": "Log Entry 1134",
            "EntryCode": "Device Removed / Device Absent",
            "EntryType": "SEL",
            "EventId": "1134",
            "EventTimestamp": "2022-06-08 16:41:45 ",
            "EventType": "ResourceRemoved",
            "Id": "1134",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
            "Name": "Log Entry 1134"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1133",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2022-06-08 16:41:44 ",
            "Description": "Log Entry 1133",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1133",
            "EventTimestamp": "2022-06-08 16:41:44 ",
            "EventType": "Alert",
            "Id": "1133",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
            "Name": "Log Entry 1133"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1132",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:06:04 ",
            "Description": "Log Entry 1132",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1132",
            "EventTimestamp": "2021-12-31 11:06:04 ",
            "EventType": "ResourceAdded",
            "Id": "1132",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1132"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1131",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:06:02 ",
            "Description": "Log Entry 1131",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1131",
            "EventTimestamp": "2021-12-31 11:06:02 ",
            "EventType": "StatusChange",
            "Id": "1131",
            "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
            "Name": "Log Entry 1131"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1130",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:06:01 ",
            "Description": "Log Entry 1130",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1130",
            "EventTimestamp": "2021-12-31 11:06:01 ",
            "EventType": "Alert",
            "Id": "1130",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
            "Name": "Log Entry 1130"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1129",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:04:45 ",
            "Description": "Log Entry 1129",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1129",
            "EventTimestamp": "2021-12-31 11:04:45 ",
            "EventType": "StatusChange",
            "Id": "1129",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
            "Name": "Log Entry 1129"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1128",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:04:45 ",
            "Description": "Log Entry 1128",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1128",
            "EventTimestamp": "2021-12-31 11:04:45 ",
            "EventType": "StatusChange",
            "Id": "1128",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
            "Name": "Log Entry 1128"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1127",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:04:23 ",
            "Description": "Log Entry 1127",
            "EntryCode": "Device Removed / Device Absent",
            "EntryType": "SEL",
            "EventId": "1127",
            "EventTimestamp": "2021-12-31 11:04:23 ",
            "EventType": "ResourceRemoved",
            "Id": "1127",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
            "Name": "Log Entry 1127"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1126",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-31 11:04:18 ",
            "Description": "Log Entry 1126",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1126",
            "EventTimestamp": "2021-12-31 11:04:18 ",
            "EventType": "Alert",
            "Id": "1126",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
            "Name": "Log Entry 1126"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1125",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:16:02 ",
            "Description": "Log Entry 1125",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1125",
            "EventTimestamp": "2021-12-20 20:16:02 ",
            "EventType": "ResourceAdded",
            "Id": "1125",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1125"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1124",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:15:54 ",
            "Description": "Log Entry 1124",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1124",
            "EventTimestamp": "2021-12-20 20:15:54 ",
            "EventType": "StatusChange",
            "Id": "1124",
            "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
            "Name": "Log Entry 1124"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1123",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:15:53 ",
            "Description": "Log Entry 1123",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1123",
            "EventTimestamp": "2021-12-20 20:15:53 ",
            "EventType": "Alert",
            "Id": "1123",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
            "Name": "Log Entry 1123"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1122",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:14:34 ",
            "Description": "Log Entry 1122",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1122",
            "EventTimestamp": "2021-12-20 20:14:34 ",
            "EventType": "StatusChange",
            "Id": "1122",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
            "Name": "Log Entry 1122"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1121",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:14:34 ",
            "Description": "Log Entry 1121",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1121",
            "EventTimestamp": "2021-12-20 20:14:34 ",
            "EventType": "StatusChange",
            "Id": "1121",
            "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
            "Name": "Log Entry 1121"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1120",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:14:13 ",
            "Description": "Log Entry 1120",
            "EntryCode": "Device Removed / Device Absent",
            "EntryType": "SEL",
            "EventId": "1120",
            "EventTimestamp": "2021-12-20 20:14:13 ",
            "EventType": "ResourceRemoved",
            "Id": "1120",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
            "Name": "Log Entry 1120"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1119",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 20:14:06 ",
            "Description": "Log Entry 1119",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1119",
            "EventTimestamp": "2021-12-20 20:14:06 ",
            "EventType": "Alert",
            "Id": "1119",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
            "Name": "Log Entry 1119"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1118",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 13:45:32 ",
            "Description": "Log Entry 1118",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1118",
            "EventTimestamp": "2021-12-20 13:45:32 ",
            "EventType": "Alert",
            "Id": "1118",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
            "Name": "Log Entry 1118"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1117",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 13:45:29 ",
            "Description": "Log Entry 1117",
            "EntryCode": "Monitor",
            "EntryType": "SEL",
            "EventId": "1117",
            "EventTimestamp": "2021-12-20 13:45:29 ",
            "EventType": "Alert",
            "Id": "1117",
            "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Not Available Power Limiting:Available ",
            "Name": "Log Entry 1117"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1116",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 13:45:00 ",
            "Description": "Log Entry 1116",
            "EntryCode": "Device Inserted / Device Present",
            "EntryType": "SEL",
            "EventId": "1116",
            "EventTimestamp": "2021-12-20 13:45:00 ",
            "EventType": "ResourceAdded",
            "Id": "1116",
            "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
            "Name": "Log Entry 1116"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1115",
            "@odata.type": "#LogEntry.v1_4_0.LogEntry",
            "Created": "2021-12-20 13:44:56 ",
            "Description": "Log Entry 1115",
            "EntryCode": "State Asserted",
            "EntryType": "SEL",
            "EventId": "1115",
            "EventTimestamp": "2021-12-20 13:44:56 ",
            "EventType": "StatusChange",
            "Id": "1115",
            "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
            "Name": "Log Entry 1115"
        }
    ],
    "Members@odata.count": 50,
    "Name": "Log Service Collection"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1115

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1115",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 13:44:56 ",
    "Description": "Log Entry 1115",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1115",
    "EventTimestamp": "2021-12-20 13:44:56 ",
    "EventType": "StatusChange",
    "Id": "1115",
    "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
    "Name": "Log Entry 1115",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1116

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1116",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 13:45:00 ",
    "Description": "Log Entry 1116",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1116",
    "EventTimestamp": "2021-12-20 13:45:00 ",
    "EventType": "ResourceAdded",
    "Id": "1116",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1116",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1117

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1117",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 13:45:29 ",
    "Description": "Log Entry 1117",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1117",
    "EventTimestamp": "2021-12-20 13:45:29 ",
    "EventType": "Alert",
    "Id": "1117",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Not Available Power Limiting:Available ",
    "Name": "Log Entry 1117",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1118

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1118",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 13:45:32 ",
    "Description": "Log Entry 1118",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1118",
    "EventTimestamp": "2021-12-20 13:45:32 ",
    "EventType": "Alert",
    "Id": "1118",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
    "Name": "Log Entry 1118",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1119

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1119",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:14:06 ",
    "Description": "Log Entry 1119",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1119",
    "EventTimestamp": "2021-12-20 20:14:06 ",
    "EventType": "Alert",
    "Id": "1119",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
    "Name": "Log Entry 1119",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1120

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1120",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:14:13 ",
    "Description": "Log Entry 1120",
    "EntryCode": "Device Removed / Device Absent",
    "EntryType": "SEL",
    "EventId": "1120",
    "EventTimestamp": "2021-12-20 20:14:13 ",
    "EventType": "ResourceRemoved",
    "Id": "1120",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
    "Name": "Log Entry 1120",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1121

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1121",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:14:34 ",
    "Description": "Log Entry 1121",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1121",
    "EventTimestamp": "2021-12-20 20:14:34 ",
    "EventType": "StatusChange",
    "Id": "1121",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
    "Name": "Log Entry 1121",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1122

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1122",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:14:34 ",
    "Description": "Log Entry 1122",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1122",
    "EventTimestamp": "2021-12-20 20:14:34 ",
    "EventType": "StatusChange",
    "Id": "1122",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
    "Name": "Log Entry 1122",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1123

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1123",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:15:53 ",
    "Description": "Log Entry 1123",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1123",
    "EventTimestamp": "2021-12-20 20:15:53 ",
    "EventType": "Alert",
    "Id": "1123",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
    "Name": "Log Entry 1123",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1124

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1124",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:15:54 ",
    "Description": "Log Entry 1124",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1124",
    "EventTimestamp": "2021-12-20 20:15:54 ",
    "EventType": "StatusChange",
    "Id": "1124",
    "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
    "Name": "Log Entry 1124",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1125

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1125",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-20 20:16:02 ",
    "Description": "Log Entry 1125",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1125",
    "EventTimestamp": "2021-12-20 20:16:02 ",
    "EventType": "ResourceAdded",
    "Id": "1125",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1125",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1126

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1126",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:04:18 ",
    "Description": "Log Entry 1126",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1126",
    "EventTimestamp": "2021-12-31 11:04:18 ",
    "EventType": "Alert",
    "Id": "1126",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
    "Name": "Log Entry 1126",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1127

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1127",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:04:23 ",
    "Description": "Log Entry 1127",
    "EntryCode": "Device Removed / Device Absent",
    "EntryType": "SEL",
    "EventId": "1127",
    "EventTimestamp": "2021-12-31 11:04:23 ",
    "EventType": "ResourceRemoved",
    "Id": "1127",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
    "Name": "Log Entry 1127",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1128

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1128",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:04:45 ",
    "Description": "Log Entry 1128",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1128",
    "EventTimestamp": "2021-12-31 11:04:45 ",
    "EventType": "StatusChange",
    "Id": "1128",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
    "Name": "Log Entry 1128",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1129

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1129",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:04:45 ",
    "Description": "Log Entry 1129",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1129",
    "EventTimestamp": "2021-12-31 11:04:45 ",
    "EventType": "StatusChange",
    "Id": "1129",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
    "Name": "Log Entry 1129",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1130

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1130",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:06:01 ",
    "Description": "Log Entry 1130",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1130",
    "EventTimestamp": "2021-12-31 11:06:01 ",
    "EventType": "Alert",
    "Id": "1130",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
    "Name": "Log Entry 1130",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1131

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1131",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:06:02 ",
    "Description": "Log Entry 1131",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1131",
    "EventTimestamp": "2021-12-31 11:06:02 ",
    "EventType": "StatusChange",
    "Id": "1131",
    "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
    "Name": "Log Entry 1131",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1132

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1132",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2021-12-31 11:06:04 ",
    "Description": "Log Entry 1132",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1132",
    "EventTimestamp": "2021-12-31 11:06:04 ",
    "EventType": "ResourceAdded",
    "Id": "1132",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1132",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1133

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1133",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:41:44 ",
    "Description": "Log Entry 1133",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1133",
    "EventTimestamp": "2022-06-08 16:41:44 ",
    "EventType": "Alert",
    "Id": "1133",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
    "Name": "Log Entry 1133",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1134

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1134",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:41:45 ",
    "Description": "Log Entry 1134",
    "EntryCode": "Device Removed / Device Absent",
    "EntryType": "SEL",
    "EventId": "1134",
    "EventTimestamp": "2022-06-08 16:41:45 ",
    "EventType": "ResourceRemoved",
    "Id": "1134",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
    "Name": "Log Entry 1134",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1135

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1135",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:42:12 ",
    "Description": "Log Entry 1135",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1135",
    "EventTimestamp": "2022-06-08 16:42:12 ",
    "EventType": "StatusChange",
    "Id": "1135",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
    "Name": "Log Entry 1135",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1136

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1136",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:42:12 ",
    "Description": "Log Entry 1136",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1136",
    "EventTimestamp": "2022-06-08 16:42:12 ",
    "EventType": "StatusChange",
    "Id": "1136",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
    "Name": "Log Entry 1136",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1137

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1137",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:43:30 ",
    "Description": "Log Entry 1137",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1137",
    "EventTimestamp": "2022-06-08 16:43:30 ",
    "EventType": "Alert",
    "Id": "1137",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
    "Name": "Log Entry 1137",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1138

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1138",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:43:31 ",
    "Description": "Log Entry 1138",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1138",
    "EventTimestamp": "2022-06-08 16:43:31 ",
    "EventType": "StatusChange",
    "Id": "1138",
    "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
    "Name": "Log Entry 1138",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1139

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1139",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:43:36 ",
    "Description": "Log Entry 1139",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1139",
    "EventTimestamp": "2022-06-08 16:43:36 ",
    "EventType": "ResourceAdded",
    "Id": "1139",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1139",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1140

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1140",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:45:52 ",
    "Description": "Log Entry 1140",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1140",
    "EventTimestamp": "2022-06-08 16:45:52 ",
    "EventType": "Alert",
    "Id": "1140",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
    "Name": "Log Entry 1140",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1141

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1141",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-08 16:45:53 ",
    "Description": "Log Entry 1141",
    "EntryCode": "Device Removed / Device Absent",
    "EntryType": "SEL",
    "EventId": "1141",
    "EventTimestamp": "2022-06-08 16:45:53 ",
    "EventType": "ResourceRemoved",
    "Id": "1141",
    "Message": "MAIN_POWER_PRS: Presence sensor, Device Removed / Device Absent was asserted",
    "Name": "Log Entry 1141",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1142

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1142",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1142",
    "EntryCode": "Predictive Failure deasserted",
    "EntryType": "SEL",
    "EventId": "1142",
    "EventTimestamp": "[System Boot]",
    "EventType": "Alert",
    "Id": "1142",
    "Message": "FRU_MB POWER_ON_FAIL: Platform sensor for FRU_MB, Predictive Failure deasserted",
    "Name": "Log Entry 1142",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1143

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1143",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1143",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1143",
    "EventTimestamp": "[System Boot]",
    "EventType": "StatusChange",
    "Id": "1143",
    "Message": "LED_TEMP_STATUS: Platform sensor, ON event was asserted",
    "Name": "Log Entry 1143",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1144

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1144",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1144",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1144",
    "EventTimestamp": "[System Boot]",
    "EventType": "StatusChange",
    "Id": "1144",
    "Message": "LED_TEMP_STATUS: Platform sensor, GREEN was asserted",
    "Name": "Log Entry 1144",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1145

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1145",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1145",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1145",
    "EventTimestamp": "[System Boot]",
    "EventType": "ResourceAdded",
    "Id": "1145",
    "Message": "SB_BOOTSSD1_PRES: Drive Slot sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1145",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1146

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1146",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1146",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1146",
    "EventTimestamp": "[System Boot]",
    "EventType": "ResourceAdded",
    "Id": "1146",
    "Message": "SB_BOOTSSD2_PRES: Drive Slot sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1146",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1147

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1147",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1147",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1147",
    "EventTimestamp": "[System Boot]",
    "EventType": "ResourceAdded",
    "Id": "1147",
    "Message": "P2_PRESENT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1147",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1148

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1148",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1148",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1148",
    "EventTimestamp": "[System Boot]",
    "EventType": "ResourceAdded",
    "Id": "1148",
    "Message": "SB_MEZZ1_PRES: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1148",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1149

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1149",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1149",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1149",
    "EventTimestamp": "[System Boot]",
    "EventType": "ResourceAdded",
    "Id": "1149",
    "Message": "P1_PRESENT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1149",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1150

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1150",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1150",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1150",
    "EventTimestamp": "[System Boot]",
    "EventType": "StatusChange",
    "Id": "1150",
    "Message": "LED_HLTH_STATUS: Platform sensor, ON event was asserted",
    "Name": "Log Entry 1150",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1151

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1151",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "[System Boot]",
    "Description": "Log Entry 1151",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1151",
    "EventTimestamp": "[System Boot]",
    "EventType": "StatusChange",
    "Id": "1151",
    "Message": "LED_HLTH_STATUS: Platform sensor, GREEN was asserted",
    "Name": "Log Entry 1151",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1152

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1152",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 08:44:09 ",
    "Description": "Log Entry 1152",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1152",
    "EventTimestamp": "2022-06-13 08:44:09 ",
    "EventType": "ResourceAdded",
    "Id": "1152",
    "Message": "MAIN_POWER_PRS: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1152",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1153

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1153",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 08:44:41 ",
    "Description": "Log Entry 1153",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1153",
    "EventTimestamp": "2022-06-13 08:44:41 ",
    "EventType": "StatusChange",
    "Id": "1153",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
    "Name": "Log Entry 1153",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1154

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1154",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 08:44:41 ",
    "Description": "Log Entry 1154",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1154",
    "EventTimestamp": "2022-06-13 08:44:41 ",
    "EventType": "StatusChange",
    "Id": "1154",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
    "Name": "Log Entry 1154",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1155

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1155",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 08:45:59 ",
    "Description": "Log Entry 1155",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1155",
    "EventTimestamp": "2022-06-13 08:45:59 ",
    "EventType": "Alert",
    "Id": "1155",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
    "Name": "Log Entry 1155",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1156

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1156",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 08:45:59 ",
    "Description": "Log Entry 1156",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1156",
    "EventTimestamp": "2022-06-13 08:45:59 ",
    "EventType": "StatusChange",
    "Id": "1156",
    "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
    "Name": "Log Entry 1156",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1157

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1157",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 08:46:05 ",
    "Description": "Log Entry 1157",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1157",
    "EventTimestamp": "2022-06-13 08:46:05 ",
    "EventType": "ResourceAdded",
    "Id": "1157",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1157",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1158

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1158",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:17:28 ",
    "Description": "Log Entry 1158",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1158",
    "EventTimestamp": "2022-06-13 12:17:28 ",
    "EventType": "Alert",
    "Id": "1158",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Not Available ",
    "Name": "Log Entry 1158",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1159

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1159",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:17:33 ",
    "Description": "Log Entry 1159",
    "EntryCode": "Device Removed / Device Absent",
    "EntryType": "SEL",
    "EventId": "1159",
    "EventTimestamp": "2022-06-13 12:17:33 ",
    "EventType": "ResourceRemoved",
    "Id": "1159",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Removed / Device Absent was asserted",
    "Name": "Log Entry 1159",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1160

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1160",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:17:54 ",
    "Description": "Log Entry 1160",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1160",
    "EventTimestamp": "2022-06-13 12:17:54 ",
    "EventType": "StatusChange",
    "Id": "1160",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (first of pair) was asserted",
    "Name": "Log Entry 1160",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1161

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1161",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:17:54 ",
    "Description": "Log Entry 1161",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1161",
    "EventTimestamp": "2022-06-13 12:17:54 ",
    "EventType": "StatusChange",
    "Id": "1161",
    "Message": "System Software event: System Event sensor, Timestamp Clock Synch (second of pair) was asserted",
    "Name": "Log Entry 1161",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1162

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1162",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:19:16 ",
    "Description": "Log Entry 1162",
    "EntryCode": "Monitor",
    "EntryType": "SEL",
    "EventId": "1162",
    "EventTimestamp": "2022-06-13 12:19:16 ",
    "EventType": "Alert",
    "Id": "1162",
    "Message": "Node Manager: Operational Capabilities, Policy Interface:Available Monitoring:Available Power Limiting:Available ",
    "Name": "Log Entry 1162",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1163

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1163",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:19:16 ",
    "Description": "Log Entry 1163",
    "EntryCode": "State Asserted",
    "EntryType": "SEL",
    "EventId": "1163",
    "EventTimestamp": "2022-06-13 12:19:16 ",
    "EventType": "StatusChange",
    "Id": "1163",
    "Message": "System Software event: System Event sensor, OEM System Boot Event was asserted",
    "Name": "Log Entry 1163",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1164

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/LogServices/Members/$entity/Entries/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/LogServices/SEL/Entries/1164",
    "@odata.type": "#LogEntry.v1_4_0.LogEntry",
    "Created": "2022-06-13 12:19:21 ",
    "Description": "Log Entry 1164",
    "EntryCode": "Device Inserted / Device Present",
    "EntryType": "SEL",
    "EventId": "1164",
    "EventTimestamp": "2022-06-13 12:19:21 ",
    "EventType": "ResourceAdded",
    "Id": "1164",
    "Message": "BIOS_POST_CMPLT: Presence sensor, Device Inserted / Device Present was asserted",
    "Name": "Log Entry 1164",
    "Severity": "OK"
}
```

## /redfish/v1/Managers/BMC1/NetworkProtocol

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/NetworkProtocol",
    "@odata.id": "/redfish/v1/Managers/BMC1/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_5_0.ManagerNetworkProtocol",
    "Description": "Manager Network Service",
    "HTTPS": {
        "ProtocolEnabled": false
    },
    "HostName": "ynas-eu-spdc-FCH21067808",
    "IPMI": {
        "Port": 623,
        "ProtocolEnabled": false
    },
    "Id": "ManagerNetworkProtocol",
    "KVMIP": {
        "Port": 2068,
        "ProtocolEnabled": true
    },
    "Name": "Manager Network Protocol",
    "VirtualMedia": {
        "Port": 2068,
        "ProtocolEnabled": true
    }
}
```

## /redfish/v1/Managers/BMC1/SerialInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/SerialInterfaces",
    "@odata.id": "/redfish/v1/Managers/BMC1/SerialInterfaces",
    "@odata.type": "#SerialInterfaceCollection.SerialInterfaceCollection",
    "Description": "Collection of Serial Interfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/SerialInterfaces/TTY0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Serial Interface Collection"
}
```

## /redfish/v1/Managers/BMC1/SerialInterfaces/TTY0

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/SerialInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/SerialInterfaces/TTY0",
    "@odata.type": "#SerialInterface.v1_1_3.SerialInterface",
    "BitRate": "115200",
    "ConnectorType": "DB9 Female",
    "DataBits": "8",
    "Description": "Management for Serial Interface",
    "FlowControl": "None",
    "Id": "TTY0",
    "InterfaceEnabled": false,
    "Name": "Manager Serial Interface 1",
    "Parity": "None",
    "PinOut": "Cisco",
    "SignalType": "Rs232",
    "StopBits": "1"
}
```

## /redfish/v1/Managers/BMC1/VirtualMedia

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/BMC1/VirtualMedia",
    "@odata.type": "#VirtualMediaCollection.VirtualMediaCollection",
    "Description": "Redfish-BMC Virtual Media Service Settings",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/VirtualMedia/0"
        },
        {
            "@odata.id": "/redfish/v1/Managers/BMC1/VirtualMedia/1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Virtual Media Services"
}
```

## /redfish/v1/Managers/BMC1/VirtualMedia/0

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/VirtualMedia/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/VirtualMedia/0",
    "@odata.type": "#VirtualMedia.v1_3_1.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/0/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "Image@Redfish.AllowableValues": [
                "This parameter shall specify the string URI of the remote media to be attached to the virtual media. (Required)"
            ],
            "Inserted@Redfish.AllowableValues": [
                "true"
            ],
            "Password@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the password to be used when accessing the URI specified by the Image parameter."
            ],
            "TransferMethod@Redfish.AllowableValues": [
                "Stream"
            ],
            "TransferProtocolType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "UserName@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the username to be used when accessing the URI specified by the Image parameter."
            ],
            "WriteProtected@Redfish.AllowableValues": [
                "true"
            ],
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/0/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "NotConnected",
    "Description": "Virtual Media Settings",
    "Id": "0",
    "Image": null,
    "ImageName": null,
    "Inserted": false,
    "MediaTypes": [
        "CD",
        "DVD"
    ],
    "Name": "Virtual CD",
    "Password": null,
    "TransferMethod": null,
    "TransferProtocolType": null,
    "UserName": null,
    "WriteProtected": true
}
```

## /redfish/v1/Managers/BMC1/VirtualMedia/1

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/VirtualMedia/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/BMC1/VirtualMedia/1",
    "@odata.type": "#VirtualMedia.v1_3_1.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/1/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "Image@Redfish.AllowableValues": [
                "This parameter shall specify the string URI of the remote media to be attached to the virtual media. (Required)"
            ],
            "Inserted@Redfish.AllowableValues": [
                "true"
            ],
            "Password@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the password to be used when accessing the URI specified by the Image parameter."
            ],
            "TransferMethod@Redfish.AllowableValues": [
                "Stream"
            ],
            "TransferProtocolType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "UserName@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the username to be used when accessing the URI specified by the Image parameter."
            ],
            "WriteProtected@Redfish.AllowableValues": [
                "true"
            ],
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/1/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "NotConnected",
    "Description": "Virtual Media Settings",
    "Id": "1",
    "Image": null,
    "ImageName": null,
    "Inserted": false,
    "MediaTypes": [
        "Floppy",
        "USBStick"
    ],
    "Name": "Virtual Removable Disk",
    "Password": null,
    "TransferMethod": null,
    "TransferProtocolType": null,
    "UserName": null,
    "WriteProtected": true
}
```

## /redfish/v1/Managers/CIMC

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/CIMC",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/CIMC/Actions/Manager.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ExportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Passphrase@Redfish.AllowableValues": [
                    "Passphrase"
                ],
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ExportConfig"
            },
            "#CiscoUCSExtensions.FwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.FwActivate"
            },
            "#CiscoUCSExtensions.ImportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Passphrase@Redfish.AllowableValues": [
                    "Passphrase"
                ],
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ImportConfig"
            },
            "#CiscoUCSExtensions.TechSupportExport": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.TechSupportExport"
            }
        }
    },
    "AutoDSTEnabled": false,
    "CommandShell": {
        "ConnectTypesSupported": [
            "SSH",
            "IPMI",
            "Oem"
        ],
        "MaxConcurrentSessions": 4,
        "ServiceEnabled": true
    },
    "DateTime": "Tue Nov 29 12:00:24 2022",
    "DateTimeLocalOffset": "+01:00",
    "Description": "ynas-eu-spdc",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces"
    },
    "FirmwareVersion": "4.1(3d)",
    "GraphicalConsole": {
        "ConnectTypesSupported": [
            "Oem"
        ],
        "MaxConcurrentSessions": 4,
        "ServiceEnabled": true
    },
    "Id": "CIMC",
    "Links": {
        "ManagerForChassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC"
            }
        ],
        "ManagerForServers": [
            {
                "@odata.id": "/redfish/v1/Systems/FOX2034GCLV"
            }
        ],
        "ManagerInChassis": {
            "@odata.id": "/redfish/v1/Chassis/CMC"
        }
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Managers/CIMC/LogServices"
    },
    "ManagerType": "ManagementController",
    "Model": "UCSS-S3260-BASE",
    "Name": "Cisco Integrated Management Controller",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol"
    },
    "RemoteAccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "RemoteRedfishServiceUri": "/redfish/v1",
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VirtualMedia": {
        "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia"
    }
}
```

## /redfish/v1/Managers/CIMC/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/EthernetInterfaces",
    "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this Manager",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces/NICs"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Managers/CIMC/EthernetInterfaces/NICs

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces/NICs",
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
        "OperatingMode": "Disabled",
        "UseDNSServers": false,
        "UseDomainName": false,
        "UseNTPServers": false
    },
    "Description": "Manager Network Interface",
    "FullDuplex": true,
    "HostName": "ynasc1-eu-spdc-FCH20487P5X-1",
    "IPv4Addresses": [
        {
            "Address": "10.58.50.34",
            "AddressOrigin": "Static",
            "Gateway": "10.58.50.62",
            "SubnetMask": "255.255.255.224"
        }
    ],
    "IPv6Addresses": [
        {
            "Address": "::",
            "AddressOrigin": "Static",
            "PrefixLength": 64
        }
    ],
    "IPv6DefaultGateway": "::",
    "IPv6StaticDefaultGateways": [
        {
            "Address": "::"
        }
    ],
    "Id": "NICs",
    "InterfaceEnabled": true,
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/CMC"
        }
    },
    "MACAddress": "2C:5A:0F:6F:6B:F1",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "PermanentMACAddress": "2C:5A:0F:6F:6B:F1",
    "SpeedMbps": 1024,
    "StatelessAddressAutoConfig": {
        "IPv4AutoConfigEnabled": false,
        "IPv6AutoConfigEnabled": false
    },
    "StaticNameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "VLAN": {
        "VLANEnable": false,
        "VLANId": 12
    }
}
```

## /redfish/v1/Managers/CIMC/LogServices

```
```

## /redfish/v1/Managers/CIMC/NetworkProtocol

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/NetworkProtocol",
    "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_5_0.ManagerNetworkProtocol",
    "DHCP": {
        "Port": null,
        "ProtocolEnabled": false
    },
    "DHCPv6": {
        "Port": null,
        "ProtocolEnabled": false
    },
    "Description": "Manager Network Service",
    "HTTP": {
        "Port": 80,
        "ProtocolEnabled": true
    },
    "HTTPS": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates"
        },
        "Port": 443,
        "ProtocolEnabled": true
    },
    "HostName": "ynasc1-eu-spdc-FCH20487P5X-1",
    "IPMI": {
        "Port": 623,
        "ProtocolEnabled": false
    },
    "Id": "ManagerNetworkProtocol",
    "NTP": {
        "NTPServers": [
            "ntp.esl.cisco.com"
        ],
        "Port": 123,
        "ProtocolEnabled": true
    },
    "Name": "Manager Network Protocol",
    "SNMP": {
        "CommunityStrings": [
            {
                "AccessMode": null,
                "CommunityString": ""
            }
        ],
        "HideCommunityStrings": false,
        "Port": 161,
        "ProtocolEnabled": false
    },
    "SSH": {
        "Port": 22,
        "ProtocolEnabled": true
    }
}
```

## /redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/NetworkProtocol/HTTPS/Certificates",
    "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "A Collection of Certificate resource instances.",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1

```{
    "@odata.context": "/redfish/v1/$metadata#Managers/Members/$entity/NetworkProtocol/HTTPS/Certificates/Members/$entity",
    "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1",
    "@odata.type": "#Certificate.v1_0_1.Certificate",
    "CertificateString": "-----BEGIN CERTIFICATE-----\nMIIDrTCCApWgAwIBAgIUNrsaSK2rntBjAV+lvMkUU9OLekowDQYJKoZIhvcNAQEN\nBQAwYzELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExETAPBgNVBAcM\nCFNhbiBKb3NlMRQwEgYDVQQKDAtTZWxmIFNpZ25lZDEWMBQGA1UEAwwNQy1zZXJp\nZXMgQ0lNQzAeFw0yMjA3MDcxNDM0MDNaFw0yNDEwMDkxNDM0MDNaMGMxCzAJBgNV\nBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMREwDwYDVQQHDAhTYW4gSm9zZTEU\nMBIGA1UECgwLU2VsZiBTaWduZWQxFjAUBgNVBAMMDUMtc2VyaWVzIENJTUMwggEi\nMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC4M1+vjmnAN1oeDNQBx/Qh2luD\nmsupFAREqV0P9gJl8aPxA1rcgnFz3Qx8GGgw9e03Wa3E3MT3yIt7KM5nbWzc1siX\nLGE9EaZh9LuuHybBblyVjvHmoKztJCP3Wcq9hYKqBqooBu8mDMLsJ3q5fbqtKF9L\nrKRYGjW8glFxyBiFvrOSEVLZlLJftwAW4+TIRjWvM3mYkVD+Sz3UPUQEzMb0Dfeh\n8CRS9K2qH2AVQHokRCxTFNSqelmyQoLpABEmEjRLvWVDNgcb+kAZsUmCxALAttkj\nPc++wa5wETCynt9QPI/QlMo+3V2yuSffH/OOBhhRXcE7fy8J26k67ce+0P9hAgMB\nAAGjWTBXMAkGA1UdEwQCMAAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwEQYJYIZIAYb4\nQgEBBAQDAgZAMCIGA1UdEQQbMBmCF3luYXNjLWV1LXNwZGMuY2lzY28uY29tMA0G\nCSqGSIb3DQEBDQUAA4IBAQBi2cnUlox7Heamd9h+6GKTOj7K8CCtkFdltnETq3B4\ne/pxb+pBDLAb4IltJJPnrXYkyAzizl902uypXEb+0oRiaDevPnbtYL2vO2PNIo0i\ndzuPNZP0k6DKr8W1lE9ZlyLJWuFBqRNn59qv3ONG3+R75iJ4xrz9FfFbPJE4KSrj\nrWHW5lWNJqBo7I0RmN2wq0SR6DgU8jgdZfT43MAo0g0N86BL1rnKYpNwyTB45gGM\n3l3arl83tJKcn/sfESZqizn+7SYAIEoLoHxVbeMMg/pI2gL+9kDdQpZe8oWxXryf\nXCkcaL9/nhrvxdL8lL77sAKseh/qQmcckBZcR0Azx4/x\n-----END CERTIFICATE-----\n",
    "CertificateType": "PEM",
    "Id": "Certificate",
    "Issuer": {
        "City": " San Jose",
        "CommonName": " C-series CIMC",
        "Country": " US",
        "Organization": " Self Signed",
        "State": " California"
    },
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate",
    "Subject": {
        "City": " San Jose",
        "CommonName": " C-series CIMC",
        "Country": " US",
        "Organization": " Self Signed",
        "State": " California"
    },
    "ValidNotAfter": "Oct  9 14:34:03 2024 GMT",
    "ValidNotBefore": "Jul  7 14:34:03 2022 GMT"
}
```

## /redfish/v1/Managers/CIMC/SerialInterfaces

```null
```

## /redfish/v1/Managers/CIMC/VirtualMedia

```null
```

