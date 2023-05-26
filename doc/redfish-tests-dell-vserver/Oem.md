# Redfish Oem Resources

Vendor | Model
--- | ---
Dell | vServer

```
# iserver get redfish endpoint
    --cache dell-poweredge-r650-ygfcbtjso8womr-5.10.00.00-on
    --type dell
    --ip 10.58.24.210
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
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellServiceRoot.DellServiceRoot",
            "@odata.type": "#DellServiceRoot.v1_0_0.DellServiceRoot",
            "IsBranded": 0,
            "ManagerMACAddress": "b0:7b:25:d1:5a:5a",
            "ServiceTag": "U8OIL5X"
        }
    }
}

/redfish/v1/CertificateService/CertificateLocations
---------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "HWCertificates": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/HWCertificates/SecurityCertificate.2"
                }
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1
-------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellChassis": {
                "@odata.context": "/redfish/v1/$metadata#DellChassis.DellChassis",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis/mainsystemchassis",
                "@odata.type": "#DellChassis.v1_0_0.DellChassis",
                "CanBeFRUed": true,
                "Description": "This resource shall provide information about the enclosure or chassis the system is in.",
                "Id": "mainsystemchassis",
                "Links": {
                    "ComputerSystem": {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                    }
                },
                "Name": "DellChassis",
                "SystemID": 2322
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1
--------------------------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": {
                "@odata.context": "/redfish/v1/$metadata#DellFC.DellFC",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFC/FC.Slot.1-1",
                "@odata.type": "#DellFC.v1_3_0.DellFC",
                "Bus": 23,
                "CableLengthMetres": null,
                "ChipType": null,
                "Device": 0,
                "DeviceDescription": "Fibre Channel in Slot 1 Port 1",
                "DeviceName": "Port 0: Emulex LightPulse LPe32002-M2-D 2-Port 32Gb Fibre  - FC ",
                "EFIVersion": "12.0.257.5",
                "FCTapeEnable": "Disabled",
                "FabricLoginRetryCount": 0,
                "FabricLoginTimeout": 0,
                "FamilyVersion": "03.00.14",
                "FramePayloadSize": null,
                "Function": 0,
                "HardZoneAddress": 0,
                "HardZoneEnable": "Disabled",
                "Id": "FC.Slot.1-1",
                "IdentifierType": null,
                "LinkDownTimeout": 0,
                "LoopResetDelay": 0,
                "Name": "DellFC",
                "PartNumber": "0MHFHK",
                "PortDownRetryCount": 0,
                "PortDownTimeout": 0,
                "PortLoginRetryCount": 0,
                "PortLoginTimeout": 1,
                "Revision": null,
                "SecondFCTargetLUN": 0,
                "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
                "SerialNumber": "MYFLPB38BTM033",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null
            },
            "DellFCCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellFCCapabilities.DellFCCapabilities",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCCapabilities/FC.Slot.1-1",
                "@odata.type": "#DellFCCapabilities.v1_0_0.DellFCCapabilities",
                "FCMaxNumberExchanges": 6144,
                "FCMaxNumberOutStandingCommands": 12289,
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "Id": "FC.Slot.1-1",
                "Name": "DellFCCapabilities",
                "OnChipThermalSensor": "Supported",
                "PersistencePolicySupport": "Supported",
                "uEFISupport": "Supported"
            },
            "DellFCPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellFCPortMetrics.DellFCPortMetrics",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCPortMetrics/FC.Slot.1-1",
                "@odata.type": "#DellFCPortMetrics.v1_1_1.DellFCPortMetrics",
                "FCInvalidCRCs": 0,
                "FCLinkFailures": 0,
                "FCLossOfSignals": 0,
                "FCRxKBCount": 0,
                "FCRxSequences": null,
                "FCRxTotalFrames": 0,
                "FCTxKBCount": 0,
                "FCTxSequences": null,
                "FCTxTotalFrames": 0,
                "Id": "FC.Slot.1-1",
                "Name": "DellFCPortMetrics",
                "OSDriverState": "Operational",
                "PortStatus": "Down"
            },
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": null,
            "DellNICCapabilities": null,
            "DellNICPortMetrics": null
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2
--------------------------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": {
                "@odata.context": "/redfish/v1/$metadata#DellFC.DellFC",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFC/FC.Slot.1-2",
                "@odata.type": "#DellFC.v1_3_0.DellFC",
                "Bus": 23,
                "CableLengthMetres": null,
                "ChipType": null,
                "Device": 0,
                "DeviceDescription": "Fibre Channel in Slot 1 Port 2",
                "DeviceName": "Port 1: Emulex LightPulse LPe32002-M2-D 2-Port 32Gb Fibre  - FC ",
                "EFIVersion": "12.0.257.5",
                "FCTapeEnable": "Disabled",
                "FabricLoginRetryCount": 0,
                "FabricLoginTimeout": 0,
                "FamilyVersion": "03.00.14",
                "FramePayloadSize": null,
                "Function": 1,
                "HardZoneAddress": 0,
                "HardZoneEnable": "Disabled",
                "Id": "FC.Slot.1-2",
                "IdentifierType": null,
                "LinkDownTimeout": 0,
                "LoopResetDelay": 0,
                "Name": "DellFC",
                "PartNumber": "0MHFHK",
                "PortDownRetryCount": 0,
                "PortDownTimeout": 0,
                "PortLoginRetryCount": 0,
                "PortLoginTimeout": 1,
                "Revision": null,
                "SecondFCTargetLUN": 0,
                "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
                "SerialNumber": "MYFLPB38BTM033",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null
            },
            "DellFCCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellFCCapabilities.DellFCCapabilities",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCCapabilities/FC.Slot.1-2",
                "@odata.type": "#DellFCCapabilities.v1_0_0.DellFCCapabilities",
                "FCMaxNumberExchanges": 6144,
                "FCMaxNumberOutStandingCommands": 12289,
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "Id": "FC.Slot.1-2",
                "Name": "DellFCCapabilities",
                "OnChipThermalSensor": "Supported",
                "PersistencePolicySupport": "Supported",
                "uEFISupport": "Supported"
            },
            "DellFCPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellFCPortMetrics.DellFCPortMetrics",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCPortMetrics/FC.Slot.1-2",
                "@odata.type": "#DellFCPortMetrics.v1_1_1.DellFCPortMetrics",
                "FCInvalidCRCs": 0,
                "FCLinkFailures": 0,
                "FCLossOfSignals": 0,
                "FCRxKBCount": 0,
                "FCRxSequences": null,
                "FCRxTotalFrames": 0,
                "FCTxKBCount": 0,
                "FCTxSequences": null,
                "FCTxTotalFrames": 0,
                "Id": "FC.Slot.1-2",
                "Name": "DellFCPortMetrics",
                "OSDriverState": "Operational",
                "PortStatus": "Down"
            },
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": null,
            "DellNICCapabilities": null,
            "DellNICPortMetrics": null
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1
----------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:FC.Slot.1-1",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Fibre Channel in Slot 1 Port 1",
                "FQDD": "NetworkTransceiver.Integrated.1:FC.Slot.1-1",
                "Id": "NetworkTransceiver.Integrated.1:FC.Slot.1-1",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "AFBR-57G5MZ-ELX",
                "Revision": " ",
                "SerialNumber": "AD1827G03D5",
                "VendorName": "AVAGO"
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2
----------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:FC.Slot.1-2",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Fibre Channel in Slot 1 Port 2",
                "FQDD": "NetworkTransceiver.Integrated.1:FC.Slot.1-2",
                "Id": "NetworkTransceiver.Integrated.1:FC.Slot.1-2",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "AFBR-57G5MZ-ELX",
                "Revision": " ",
                "SerialNumber": "AD1827G03R3",
                "VendorName": "AVAGO"
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1
--------------------------------------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNIC/NIC.Embedded.1-1-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 4,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": "1.39",
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Embedded NIC 1 Port 1 Partition 1",
                "EFIVersion": "21.6.12",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Embedded.1-1-1",
                "FamilyVersion": "21.80.8",
                "Id": "NIC.Embedded.1-1-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Embedded.1-1-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2021-07-14T03:23:00+00:00",
                "LinkDuplex": "Unknown",
                "MediaType": "Base T",
                "Name": "DellNIC",
                "NicMode": "Unknown",
                "PCIDeviceID": "165f",
                "PCISubDeviceID": "08ff",
                "PCISubVendorID": "1028",
                "PCIVendorID": "14e4",
                "PartNumber": null,
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Broadcom Gigabit Ethernet BCM5720 - 70:B5:E8:F0:25:52",
                "Protocol": "NIC",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": null,
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Broadcom Corp",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.1-1-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "NotSupported",
                "ETS": "NotSupported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Embedded.1-1-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "NotSupported",
                "RDMASupport": "NotSupported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "NotSupported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.1-1-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Embedded.1-1-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": null,
                "RDMARxTotalPackets": null,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": null,
                "RDMATxTotalPackets": null,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 0,
                "RxBytes": 0,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": null,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 0,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 0,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:35-05:00",
                "TxBroadcast": 0,
                "TxBytes": 0,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 0,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 0
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1
--------------------------------------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNIC/NIC.Embedded.2-1-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 4,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": "1.39",
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Embedded NIC 1 Port 2 Partition 1",
                "EFIVersion": "21.6.12",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Embedded.2-1-1",
                "FamilyVersion": "21.80.8",
                "Id": "NIC.Embedded.2-1-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Embedded.2-1-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2021-07-02T22:29:07+00:00",
                "LinkDuplex": "Unknown",
                "MediaType": "Base T",
                "Name": "DellNIC",
                "NicMode": "Unknown",
                "PCIDeviceID": "165f",
                "PCISubDeviceID": "08ff",
                "PCISubVendorID": "1028",
                "PCIVendorID": "14e4",
                "PartNumber": null,
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Broadcom Gigabit Ethernet BCM5720 - 70:B5:E8:F0:25:53",
                "Protocol": "NIC",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": null,
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Broadcom Corp",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.2-1-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "NotSupported",
                "ETS": "NotSupported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Embedded.2-1-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "NotSupported",
                "RDMASupport": "NotSupported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "NotSupported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.2-1-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Embedded.2-1-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": null,
                "RDMARxTotalPackets": null,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": null,
                "RDMATxTotalPackets": null,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 0,
                "RxBytes": 0,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": null,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 0,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 0,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:30-05:00",
                "TxBroadcast": 0,
                "TxBytes": 0,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 0,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 0
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1
--------------------------------------------------------------------------------------------------
{
    "Oem": {}
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1
--------------------------------------------------------------------------------------------------
{
    "Oem": {}
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1
------------------------------------------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNIC/NIC.Integrated.1-1-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 49,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": null,
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Integrated NIC 1 Port 1 Partition 1",
                "EFIVersion": "14.22.15",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Integrated.1-1-1",
                "FamilyVersion": "16.28.45.12",
                "Id": "NIC.Integrated.1-1-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Integrated.1-1-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "LinkDuplex": "FullDuplex",
                "MediaType": "SFF_CAGE",
                "Name": "DellNIC",
                "NicMode": "Enabled",
                "PCIDeviceID": "1017",
                "PCISubDeviceID": "0097",
                "PCISubVendorID": "15b3",
                "PCIVendorID": "15b3",
                "PartNumber": "04TRD3",
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter - B8:CE:F6:94:F0:B8",
                "Protocol": "NIC,RDMA",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": "INJBNM414TJ0AL",
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Mellanox Technologies, Inc.",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-1-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "Supported",
                "ETS": "Supported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Integrated.1-1-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "Supported",
                "RDMASupport": "Supported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "Supported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-1-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Integrated.1-1-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": 0,
                "RDMARxTotalPackets": 0,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": 0,
                "RDMATxTotalPackets": 0,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 4304449747,
                "RxBytes": 828323997018,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": 0,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 963469206,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 969898405,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:40-05:00",
                "TxBroadcast": 82721,
                "TxBytes": 15381706231,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 545996,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 25776787
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1
------------------------------------------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNIC/NIC.Integrated.1-2-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 49,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": null,
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Integrated NIC 1 Port 2 Partition 1",
                "EFIVersion": "14.22.15",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Integrated.1-2-1",
                "FamilyVersion": "16.28.45.12",
                "Id": "NIC.Integrated.1-2-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Integrated.1-2-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "LinkDuplex": "FullDuplex",
                "MediaType": "SFF_CAGE",
                "Name": "DellNIC",
                "NicMode": "Enabled",
                "PCIDeviceID": "1017",
                "PCISubDeviceID": "0097",
                "PCISubVendorID": "15b3",
                "PCIVendorID": "15b3",
                "PartNumber": "04TRD3",
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter - B8:CE:F6:94:F0:B9",
                "Protocol": "NIC,RDMA",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": "INJBNM414TJ0AL",
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Mellanox Technologies, Inc.",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-2-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "Supported",
                "ETS": "Supported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Integrated.1-2-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "Supported",
                "RDMASupport": "Supported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "Supported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-2-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Integrated.1-2-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": 0,
                "RDMARxTotalPackets": 0,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": 0,
                "RDMATxTotalPackets": 0,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 3865711632,
                "RxBytes": 720933706011,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": 0,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 831027785,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 855696971,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:40-05:00",
                "TxBroadcast": 1,
                "TxBytes": 14852656,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 206286,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 0
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1
------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:NIC.Integrated.1-1",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Integrated NIC 1 Port 1",
                "FQDD": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-1",
                "Id": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-1",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "FTLX8571D3BCL-C2",
                "Revision": "A",
                "SerialNumber": "FNS1651019S",
                "VendorName": "CISCO-FINISAR"
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2
------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:NIC.Integrated.1-2",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Integrated NIC 1 Port 2",
                "FQDD": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-2",
                "Id": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-2",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "FTLX8571D3BCL-C2",
                "Revision": "A",
                "SerialNumber": "FNS18270TMW",
                "VendorName": "CISCO-FINISAR"
            }
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM0123VR
-----------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1MEM0123VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM4567VR
-----------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1MEM4567VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1Temp
------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1Temp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1VCOREVR
---------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1VCOREVR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM0123VR
-----------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2MEM0123VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM4567VR
-----------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2MEM4567VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2Temp
------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2Temp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2VCOREVR
---------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2VCOREVR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1A
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1B
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1C
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1D
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2A
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2B
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2C
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2D
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3A
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3B
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3C
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3D
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4A
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4B
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4C
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4D
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Current1
---------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS1Current1",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Voltage
--------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS1Voltage",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Current2
---------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS2Current2",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Voltage
--------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS2Voltage",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardExhaustTemp
--------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardExhaustTemp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardInletTemp
------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardInletTemp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardPwrConsumption
-----------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardPwrConsumption",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1
-------------------------------------
{
    "Actions": {
        "Oem": {
            "#OemManager.v1_3_0.OemManager#OemManager.ExportSystemConfiguration": {
                "ExportFormat@Redfish.AllowableValues": [
                    "XML",
                    "JSON"
                ],
                "ExportUse@Redfish.AllowableValues": [
                    "Default",
                    "Clone",
                    "Replace"
                ],
                "ShareParameters": {
                    "IgnoreCertificateWarning@Redfish.AllowableValues": [
                        "Disabled",
                        "Enabled"
                    ],
                    "ProxySupport@Redfish.AllowableValues": [
                        "Disabled",
                        "EnabledProxyDefault",
                        "Enabled"
                    ],
                    "ProxyType@Redfish.AllowableValues": [
                        "HTTP",
                        "SOCKS4"
                    ],
                    "ShareType@Redfish.AllowableValues": [
                        "LOCAL",
                        "NFS",
                        "CIFS",
                        "HTTP",
                        "HTTPS"
                    ]
                },
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/EID_674_Manager.ExportSystemConfiguration"
            },
            "#OemManager.v1_3_0.OemManager#OemManager.ImportSystemConfiguration": {
                "HostPowerState@Redfish.AllowableValues": [
                    "On",
                    "Off"
                ],
                "ImportSystemConfiguration@Redfish.AllowableValues": [
                    "TimeToWait",
                    "ImportBuffer"
                ],
                "ShareParameters": {
                    "IgnoreCertificateWarning@Redfish.AllowableValues": [
                        "Disabled",
                        "Enabled"
                    ],
                    "ProxySupport@Redfish.AllowableValues": [
                        "Disabled",
                        "EnabledProxyDefault",
                        "Enabled"
                    ],
                    "ProxyType@Redfish.AllowableValues": [
                        "HTTP",
                        "SOCKS4"
                    ],
                    "ShareType@Redfish.AllowableValues": [
                        "LOCAL",
                        "NFS",
                        "CIFS",
                        "HTTP",
                        "HTTPS"
                    ]
                },
                "ShutdownType@Redfish.AllowableValues": [
                    "Graceful",
                    "Forced",
                    "NoReboot"
                ],
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/EID_674_Manager.ImportSystemConfiguration"
            },
            "#OemManager.v1_3_0.OemManager#OemManager.ImportSystemConfigurationPreview": {
                "ImportSystemConfigurationPreview@Redfish.AllowableValues": [
                    "ImportBuffer"
                ],
                "ShareParameters": {
                    "IgnoreCertificateWarning@Redfish.AllowableValues": [
                        "Disabled",
                        "Enabled"
                    ],
                    "ProxySupport@Redfish.AllowableValues": [
                        "Disabled",
                        "EnabledProxyDefault",
                        "Enabled"
                    ],
                    "ProxyType@Redfish.AllowableValues": [
                        "HTTP",
                        "SOCKS4"
                    ],
                    "ShareType@Redfish.AllowableValues": [
                        "LOCAL",
                        "NFS",
                        "CIFS",
                        "HTTP",
                        "HTTPS"
                    ]
                },
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/EID_674_Manager.ImportSystemConfigurationPreview"
            },
            "DellManager.v1_0_0#DellManager.ResetToDefaults": {
                "ResetType@Redfish.AllowableValues": [
                    "All",
                    "ResetAllWithRootDefaults",
                    "Default"
                ],
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/DellManager.ResetToDefaults"
            }
        }
    },
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "DellAttributes": [
                    {
                        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1"
                    }
                ],
                "DellAttributes@odata.count": 3,
                "DellJobService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService"
                },
                "DellLCService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService"
                },
                "DellLicensableDeviceCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices"
                },
                "DellLicenseCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses"
                },
                "DellLicenseManagementService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService"
                },
                "DellOpaqueManagementDataCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellOpaqueManagementData"
                },
                "DellPersistentStorageService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService"
                },
                "DellSwitchConnectionCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections"
                },
                "DellSwitchConnectionService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService"
                },
                "DellSystemManagementService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService"
                },
                "DellSystemQuickSyncCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellSystemQuickSync"
                },
                "DellTimeService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService"
                },
                "DellUSBDeviceCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellUSBDevices"
                },
                "DelliDRACCardService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService"
                },
                "DellvFlashCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellvFlash"
                },
                "Jobs": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DelliDRACCard": {
                "@odata.context": "/redfish/v1/$metadata#DelliDRACCard.DelliDRACCard",
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCard/iDRAC.Embedded.1-1_0x23_IDRACinfo",
                "@odata.type": "#DelliDRACCard.v1_1_0.DelliDRACCard",
                "Description": "An instance of DelliDRACCard will have data specific to the Integrated Dell Remote Access Controller (iDRAC) in the managed system.",
                "IPMIVersion": "2.0",
                "Id": "iDRAC.Embedded.1-1_0x23_IDRACinfo",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-10-26T20:21:26+00:00",
                "Name": "DelliDRACCard",
                "URLString": "https://10.44.182.90:443"
            }
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings
-----------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings
----------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings
---------------------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1
---------------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#DellSerialInterface.SerialDataClear": {
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1/Actions/Oem/DellSerialInterface.SerialDataClear"
            },
            "#DellSerialInterface.SerialDataExport": {
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1/Actions/Oem/DellSerialInterface.SerialDataExport"
            }
        }
    }
}

/redfish/v1/Registries/BiosAttributeRegistry.v1_0_0
---------------------------------------------------
{
    "Oem": {}
}

/redfish/v1/Registries/BootSourcesRegistry.v1_0_0
-------------------------------------------------
{
    "Oem": {}
}

/redfish/v1/Systems/System.Embedded.1
-------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "BootOrder": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources"
                },
                "DellBIOSService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService"
                },
                "DellBootSources": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources"
                },
                "DellChassisCollection": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis"
                },
                "DellGPUSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellGPUSensors"
                },
                "DellMetricService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService"
                },
                "DellNumericSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors"
                },
                "DellOSDeploymentService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService"
                },
                "DellPSNumericSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors"
                },
                "DellPresenceAndStatusSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPresenceAndStatusSensors"
                },
                "DellRaidService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService"
                },
                "DellRollupStatusCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus"
                },
                "DellSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors"
                },
                "DellSlotCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots"
                },
                "DellSoftwareInstallationService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService"
                },
                "DellVideoCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo"
                },
                "DellVideoNetworkCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideoNetwork"
                }
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellSystem": {
                "@odata.context": "/redfish/v1/$metadata#DellSystem.DellSystem",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystem/System.Embedded.1",
                "@odata.type": "#DellSystem.v1_3_0.DellSystem",
                "BIOSReleaseDate": "05/28/2021",
                "BaseBoardChassisSlot": "NA",
                "BatteryRollupStatus": "OK",
                "BladeGeometry": "NotApplicable",
                "CMCIP": null,
                "CPURollupStatus": "OK",
                "ChassisModel": "",
                "ChassisName": "Main System Chassis",
                "ChassisServiceTag": "U8OIL5X",
                "ChassisSystemHeightUnit": 1,
                "CurrentRollupStatus": "OK",
                "EstimatedExhaustTemperatureCelsius": 255,
                "EstimatedSystemAirflowCFM": 255,
                "ExpressServiceCode": "2440875279",
                "FanRollupStatus": "OK",
                "IDSDMRollupStatus": null,
                "Id": "System.Embedded.1",
                "IntrusionRollupStatus": "OK",
                "IsOEMBranded": "False",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-30T23:00:48+00:00",
                "LicensingRollupStatus": "OK",
                "ManagedSystemSize": "1 U",
                "MaxCPUSockets": 2,
                "MaxDIMMSlots": 32,
                "MaxPCIeSlots": 3,
                "MemoryOperationMode": "OptimizerMode",
                "Name": "DellSystem",
                "NodeID": "U8OIL5X",
                "PSRollupStatus": "OK",
                "PlatformGUID": "3346464f-c0b1-3880-4410-00344c4c4544",
                "PopulatedDIMMSlots": 16,
                "PopulatedPCIeSlots": 1,
                "PowerCapEnabledState": "Disabled",
                "SDCardRollupStatus": null,
                "SELRollupStatus": "OK",
                "ServerAllocationWatts": null,
                "StorageRollupStatus": "OK",
                "SysMemErrorMethodology": "Multi-bitECC",
                "SysMemFailOverState": "NotInUse",
                "SysMemLocation": "SystemBoardOrMotherboard",
                "SysMemPrimaryStatus": "OK",
                "SystemGeneration": "15G Monolithic",
                "SystemID": 2322,
                "SystemRevision": "I",
                "TempRollupStatus": "OK",
                "TempStatisticsRollupStatus": "OK",
                "UUID": "4c4c4544-0034-4410-8038-b1c04f464633",
                "VoltRollupStatus": "OK",
                "smbiosGUID": "44454c4c-3400-1044-8038-b1c04f464633"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Bios
------------------------------------------
{
    "Actions": {
        "Oem": {
            "#DellBios.RunBIOSLiveScanning": {
                "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Actions/Oem/DellBios.RunBIOSLiveScanning"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Bios/Settings
---------------------------------------------------
{
    "Actions": {
        "Oem": {
            "DellManager.v1_0_0#DellManager.ClearPending": {
                "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Settings/Actions/Oem/DellManager.ClearPending"
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Oem/Dell/DellMemory/DIMM.Socket.A1",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Oem/Dell/DellMemory/DIMM.Socket.A2",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Oem/Dell/DellMemory/DIMM.Socket.A3",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A3",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Oem/Dell/DellMemory/DIMM.Socket.A4",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A4",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Oem/Dell/DellMemory/DIMM.Socket.A5",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A5",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Oem/Dell/DellMemory/DIMM.Socket.A6",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A6",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Oem/Dell/DellMemory/DIMM.Socket.A7",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A7",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Oem/Dell/DellMemory/DIMM.Socket.A8",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A8",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Oem/Dell/DellMemory/DIMM.Socket.B1",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Oem/Dell/DellMemory/DIMM.Socket.B2",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Oem/Dell/DellMemory/DIMM.Socket.B3",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B3",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Oem/Dell/DellMemory/DIMM.Socket.B4",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B4",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Oem/Dell/DellMemory/DIMM.Socket.B5",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B5",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Oem/Dell/DellMemory/DIMM.Socket.B6",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B6",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Oem/Dell/DellMemory/DIMM.Socket.B7",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B7",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8
-----------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Oem/Dell/DellMemory/DIMM.Socket.B8",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B8",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings
-----------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "AHCI.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.2-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "AHCI.Embedded.2-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "P2PBridge.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.2-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "P2PBridge.Embedded.2-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0/Oem/Dell/DellPCIeFunctions/ISABridge.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "ISABridge.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4/Oem/Dell/DellPCIeFunctions/SMBus.Embedded.3-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "SMBus.Embedded.3-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0
-----------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0/Oem/Dell/DellPCIeFunctions/Disk.Bay.9:Enclosure.Internal.0-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "4XOrX4",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "Disk.Bay.9:Enclosure.Internal.0-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "2.5InchDriveFormFactor",
                "SlotType": "PCIExpressGen4SFF-8639"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0
-----------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0/Oem/Dell/DellPCIeFunctions/Disk.Bay.8:Enclosure.Internal.0-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "4XOrX4",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "Disk.Bay.8:Enclosure.Internal.0-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "2.5InchDriveFormFactor",
                "SlotType": "PCIExpressGen4SFF-8639"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0
-----------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0/Oem/Dell/DellPCIeFunctions/RAID.SL.3-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "RAID.SL.3-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-30T23:00:48+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0/Oem/Dell/DellPCIeFunctions/FC.Slot.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "16XOrX16",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "FC.Slot.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-29T01:38:52+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "LongLength",
                "SlotType": "PCIExpressGen4"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1/Oem/Dell/DellPCIeFunctions/FC.Slot.1-2",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "16XOrX16",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "FC.Slot.1-2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-29T01:38:52+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "LongLength",
                "SlotType": "PCIExpressGen4"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0
-------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0/Oem/Dell/DellPCIeFunctions/Video.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "Video.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0
-------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0/Oem/Dell/DellPCIeFunctions/NIC.Embedded.1-1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Embedded.1-1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-14T03:23:00+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1
-------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1/Oem/Dell/DellPCIeFunctions/NIC.Embedded.2-1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Embedded.2-1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T22:29:07+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Integrated.1-1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1
---------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-2-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Integrated.1-2-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0
-------------------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0/Oem/Dell/DellPCIeFunctions/AHCI.SL.6-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "AHCI.SL.6-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellAccelerators": null,
            "DellProcessor": {
                "@odata.context": "/redfish/v1/$metadata#DellProcessor.DellProcessor",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1/Oem/Dell/DellProcessors/CPU.Socket.1",
                "@odata.type": "#DellProcessor.v1_1_0.DellProcessor",
                "CPUFamily": "Intel(R)Xeon(TM)",
                "CPUStatus": "CPUEnabled",
                "Cache1Associativity": "12-WaySet-Associative",
                "Cache1ErrorMethodology": "Parity",
                "Cache1InstalledSizeKB": 2240,
                "Cache1Level": "L1",
                "Cache1Location": "Internal",
                "Cache1PrimaryStatus": "OK",
                "Cache1SRAMType": "Unknown",
                "Cache1SizeKB": 2240,
                "Cache1Type": "Unified",
                "Cache1WritePolicy": "WriteBack",
                "Cache2Associativity": "20-WaySet-Associative",
                "Cache2ErrorMethodology": "Single-bitECC",
                "Cache2InstalledSizeKB": 35840,
                "Cache2Level": "L2",
                "Cache2Location": "Internal",
                "Cache2PrimaryStatus": "OK",
                "Cache2SRAMType": "Unknown",
                "Cache2SizeKB": 35840,
                "Cache2Type": "Unified",
                "Cache2WritePolicy": "WriteBack",
                "Cache3Associativity": "12-WaySet-Associative",
                "Cache3ErrorMethodology": "Single-bitECC",
                "Cache3InstalledSizeKB": 43008,
                "Cache3Level": "L3",
                "Cache3Location": "Internal",
                "Cache3PrimaryStatus": "OK",
                "Cache3SRAMType": "Unknown",
                "Cache3SizeKB": 43008,
                "Cache3Type": "Unified",
                "Cache3WritePolicy": "WriteBack",
                "CurrentClockSpeedMhz": 2000,
                "ExternalBusClockSpeedMhz": 11200,
                "HyperThreadingCapable": "Yes",
                "HyperThreadingEnabled": "Yes",
                "Id": "CPU.Socket.1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellProcessor",
                "TurboModeCapable": "Yes",
                "TurboModeEnabled": "Yes",
                "VirtualizationTechnologyCapable": "Yes",
                "VirtualizationTechnologyEnabled": "Yes",
                "Volts": "1.6"
            },
            "PowerMetrics": null,
            "ThermalMetrics": null
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2
-------------------------------------------------------------
{
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellAccelerators": null,
            "DellProcessor": {
                "@odata.context": "/redfish/v1/$metadata#DellProcessor.DellProcessor",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2/Oem/Dell/DellProcessors/CPU.Socket.2",
                "@odata.type": "#DellProcessor.v1_1_0.DellProcessor",
                "CPUFamily": "Intel(R)Xeon(TM)",
                "CPUStatus": "CPUEnabled",
                "Cache1Associativity": "12-WaySet-Associative",
                "Cache1ErrorMethodology": "Parity",
                "Cache1InstalledSizeKB": 2240,
                "Cache1Level": "L1",
                "Cache1Location": "Internal",
                "Cache1PrimaryStatus": "OK",
                "Cache1SRAMType": "Unknown",
                "Cache1SizeKB": 2240,
                "Cache1Type": "Unified",
                "Cache1WritePolicy": "WriteBack",
                "Cache2Associativity": "20-WaySet-Associative",
                "Cache2ErrorMethodology": "Single-bitECC",
                "Cache2InstalledSizeKB": 35840,
                "Cache2Level": "L2",
                "Cache2Location": "Internal",
                "Cache2PrimaryStatus": "OK",
                "Cache2SRAMType": "Unknown",
                "Cache2SizeKB": 35840,
                "Cache2Type": "Unified",
                "Cache2WritePolicy": "WriteBack",
                "Cache3Associativity": "12-WaySet-Associative",
                "Cache3ErrorMethodology": "Single-bitECC",
                "Cache3InstalledSizeKB": 43008,
                "Cache3Level": "L3",
                "Cache3Location": "Internal",
                "Cache3PrimaryStatus": "OK",
                "Cache3SRAMType": "Unknown",
                "Cache3SizeKB": 43008,
                "Cache3Type": "Unified",
                "Cache3WritePolicy": "WriteBack",
                "CurrentClockSpeedMhz": 2000,
                "ExternalBusClockSpeedMhz": 11200,
                "HyperThreadingCapable": "Yes",
                "HyperThreadingEnabled": "Yes",
                "Id": "CPU.Socket.2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellProcessor",
                "TurboModeCapable": "Yes",
                "TurboModeEnabled": "Yes",
                "VirtualizationTechnologyCapable": "Yes",
                "VirtualizationTechnologyEnabled": "Yes",
                "Volts": "1.6"
            },
            "PowerMetrics": null,
            "ThermalMetrics": null
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/SecureBoot
------------------------------------------------
{
    "Actions": {
        "Oem": {}
    },
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellSecureBoot.DellSecureBoot",
            "@odata.type": "#DellSecureBoot.v1_0_0.DellSecureBoot",
            "Certificates": {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/Oem/Dell/Certificates"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1
---------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Oem/Dell/DellControllers/AHCI.Embedded.1-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotPresent",
                "AutoConfigBehavior": "NotApplicable",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 0,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 0,
                "ControllerFirmwareVersion": null,
                "CurrentControllerMode": "NotSupported",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": null,
                "EncryptionCapability": "None",
                "EncryptionMode": "None",
                "Id": "AHCI.Embedded.1-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Unknown",
                "PersistentHotspare": "NotApplicable",
                "RealtimeCapability": "Incapable",
                "RollupStatus": "Unknown",
                "SASAddress": "0",
                "SecurityStatus": "EncryptionNotCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "NotSupported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "NotSupported",
                "SupportRAID10UnevenSpans": "NotSupported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1
---------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Oem/Dell/DellControllers/AHCI.Embedded.2-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotPresent",
                "AutoConfigBehavior": "NotApplicable",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 0,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 0,
                "ControllerFirmwareVersion": null,
                "CurrentControllerMode": "NotSupported",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": null,
                "EncryptionCapability": "None",
                "EncryptionMode": "None",
                "Id": "AHCI.Embedded.2-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Unknown",
                "PersistentHotspare": "NotApplicable",
                "RealtimeCapability": "Incapable",
                "RollupStatus": "Unknown",
                "SASAddress": "0",
                "SecurityStatus": "EncryptionNotCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "NotSupported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "NotSupported",
                "SupportRAID10UnevenSpans": "NotSupported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1
---------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Oem/Dell/DellControllers/AHCI.SL.6-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotSupported",
                "AutoConfigBehavior": "NotApplicable",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 0,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 0,
                "ControllerFirmwareVersion": "2.5.13.4008",
                "CurrentControllerMode": "NotSupported",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": null,
                "EncryptionCapability": "None",
                "EncryptionMode": "None",
                "Id": "AHCI.SL.6-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Unknown",
                "PersistentHotspare": "NotApplicable",
                "RealtimeCapability": "Incapable",
                "RollupStatus": "OK",
                "SASAddress": "0",
                "SecurityStatus": "EncryptionNotCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "NotSupported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "NotSupported",
                "SupportRAID10UnevenSpans": "NotSupported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1
---------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1
---------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Oem/Dell/DellControllers/RAID.SL.3-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotPresent",
                "AutoConfigBehavior": "Off",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 4096,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 4,
                "ControllerFirmwareVersion": "51.14.0-3900",
                "CurrentControllerMode": "RAID",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": "7.713.08.00",
                "EncryptionCapability": "LocalKeyManagementAndSecureEnterpriseKeyManagerCapable",
                "EncryptionMode": "None",
                "Id": "RAID.SL.3-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-30T23:00:48+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Stopped",
                "PersistentHotspare": "Disabled",
                "RealtimeCapability": "Capable",
                "RollupStatus": "OK",
                "SASAddress": "5B07B250D514E600",
                "SecurityStatus": "EncryptionCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "Supported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "Supported",
                "SupportRAID10UnevenSpans": "Supported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            },
            "DellControllerBattery": {
                "@odata.context": "/redfish/v1/$metadata#DellControllerBattery.DellControllerBattery",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Oem/Dell/DellControllerBattery/Battery.Integrated.1:RAID.SL.3-1",
                "@odata.type": "#DellControllerBattery.v1_0_0.DellControllerBattery",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "FQDD": "Battery.Integrated.1:RAID.SL.3-1",
                "Id": "Battery.Integrated.1:RAID.SL.3-1",
                "Name": "Battery on RAID Controller in SL 3",
                "PrimaryStatus": "OK",
                "RAIDState": "Ready"
            }
        }
    }
}

/redfish/v1/UpdateService
-------------------------
{
    "Actions": {
        "Oem": {
            "DellUpdateService.v1_1_0#DellUpdateService.Install": {
                "InstallUpon@Redfish.AllowableValues": [
                    "Now",
                    "NowAndReboot",
                    "NextReboot"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/DellUpdateService.Install"
            }
        }
    }
}
```