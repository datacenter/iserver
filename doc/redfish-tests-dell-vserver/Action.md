# Redfish Action Resources

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
    --action
    --deep
    --max 0

/redfish/v1/CertificateService
------------------------------
{
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR"
        },
        "#CertificateService.ReplaceCertificate": {
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.ReplaceCertificate"
        }
    }
}

/redfish/v1/Chassis/Enclosure.Internal.0-1
------------------------------------------
{
    "Actions": {}
}

/redfish/v1/Chassis/Enclosure.Internal.0-1/Settings
---------------------------------------------------
{
    "Actions": {}
}

/redfish/v1/Chassis/System.Embedded.1
-------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/System.Embedded.1/Actions/Chassis.Reset"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1/Settings
------------------------------------------------------------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2/Settings
------------------------------------------------------------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1/Settings
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1/Settings
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1/Settings
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1/Settings
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/EventService
------------------------
{
    "Actions": {
        "#EventService.SubmitTestEvent": {
            "EventType@Redfish.AllowableValues": [
                "Alert"
            ],
            "target": "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1
-------------------------------------
{
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "GracefulRestart"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Manager.Reset"
        },
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
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings
-----------------------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings
----------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings
---------------------------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService
-------------------------------------------------------------
{
    "Actions": {
        "#DellJobService.CreateRebootJob": {
            "RebootJobType@Redfish.AllowableValues": [
                "GracefulRebootWithForcedShutdown",
                "GracefulRebootWithoutForcedShutdown",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.CreateRebootJob"
        },
        "#DellJobService.DeleteJobQueue": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.DeleteJobQueue"
        },
        "#DellJobService.SetDeleteOnCompletionTimeout": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.SetDeleteOnCompletionTimeout"
        },
        "#DellJobService.SetupJobQueue": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.SetupJobQueue"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService
------------------------------------------------------------
{
    "Actions": {
        "#DellLCService.ClearProvisioningServer": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ClearProvisioningServer"
        },
        "#DellLCService.DeleteAutoDiscoveryClientCerts": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.DeleteAutoDiscoveryClientCerts"
        },
        "#DellLCService.DeleteAutoDiscoveryServerPublicKey": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.DeleteAutoDiscoveryServerPublicKey"
        },
        "#DellLCService.DownloadClientCerts": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.DownloadClientCerts"
        },
        "#DellLCService.ExportCompleteLCLog": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportCompleteLCLog"
        },
        "#DellLCService.ExportFactoryConfiguration": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportFactoryConfiguration"
        },
        "#DellLCService.ExportHWInventory": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "XMLSchema@Redfish.AllowableValues": [
                "CIM-XML",
                "JSON",
                "Simple"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportHWInventory"
        },
        "#DellLCService.ExportLCLog": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportLCLog"
        },
        "#DellLCService.ExportSVGFile": {
            "ShareType@Redfish.AllowableValues": [
                "Local"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportSVGFile"
        },
        "#DellLCService.ExportServerScreenShot": {
            "FileType@Redfish.AllowableValues": [
                "LastCrashScreenShot",
                "Preview",
                "ServerScreenShot"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportServerScreenShot"
        },
        "#DellLCService.ExportTechSupportReport": {
            "DataSelectorArrayIn@Redfish.AllowableValues": [
                "HWData",
                "OSAppData",
                "OSAppDataWithoutPII",
                "TTYLogs"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportTechSupportReport"
        },
        "#DellLCService.ExportVideoLog": {
            "FileType@Redfish.AllowableValues": [
                "BootCaptureVideo",
                "CrashCaptureVideo"
            ],
            "ShareType@Redfish.AllowableValues": [
                "Local"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportVideoLog"
        },
        "#DellLCService.ExportePSADiagnosticsResult": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportePSADiagnosticsResult"
        },
        "#DellLCService.ExposeiSMInstallerToHostOS": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExposeiSMInstallerToHostOS"
        },
        "#DellLCService.GetRSStatus": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.GetRSStatus"
        },
        "#DellLCService.GetRemoteServicesAPIStatus": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.GetRemoteServicesAPIStatus"
        },
        "#DellLCService.InsertCommentInLCLog": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.InsertCommentInLCLog"
        },
        "#DellLCService.LCWipe": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.LCWipe"
        },
        "#DellLCService.ReInitiateAutoDiscovery": {
            "PerformAutoDiscovery@Redfish.AllowableValues": [
                "NextBoot",
                "Now",
                "Off"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ReInitiateAutoDiscovery"
        },
        "#DellLCService.ReInitiateDHS": {
            "PerformAutoDiscovery@Redfish.AllowableValues": [
                "NextBoot",
                "Now",
                "Off"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ReInitiateDHS"
        },
        "#DellLCService.RunePSADiagnostics": {
            "RebootJobType@Redfish.AllowableValues": [
                "GracefulRebootWithForcedShutdown",
                "GracefulRebootWithoutForcedShutdown",
                "PowerCycle"
            ],
            "RunMode@Redfish.AllowableValues": [
                "Express",
                "ExpressAndExtended",
                "Extended"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.RunePSADiagnostics"
        },
        "#DellLCService.SupportAssistAcceptEULA": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistAcceptEULA"
        },
        "#DellLCService.SupportAssistClearAutoCollectSchedule": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistClearAutoCollectSchedule"
        },
        "#DellLCService.SupportAssistCollection": {
            "DataSelectorArrayIn@Redfish.AllowableValues": [
                "DebugLogs",
                "HWData",
                "OSAppData",
                "TTYLogs",
                "TelemetryReports"
            ],
            "Filter@Redfish.AllowableValues": [
                "No",
                "Yes"
            ],
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS",
                "TFTP"
            ],
            "Transmit@Redfish.AllowableValues": [
                "No",
                "Yes"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistCollection"
        },
        "#DellLCService.SupportAssistExportLastCollection": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistExportLastCollection"
        },
        "#DellLCService.SupportAssistGetAutoCollectSchedule": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistGetAutoCollectSchedule"
        },
        "#DellLCService.SupportAssistGetEULAStatus": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistGetEULAStatus"
        },
        "#DellLCService.SupportAssistRegister": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistRegister"
        },
        "#DellLCService.SupportAssistSetAutoCollectSchedule": {
            "Recurrence@Redfish.AllowableValues": [
                "Monthly",
                "Quarterly",
                "Weekly"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistSetAutoCollectSchedule"
        },
        "#DellLCService.SupportAssistUploadLastCollection": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistUploadLastCollection"
        },
        "#DellLCService.SystemErase": {
            "Component@Redfish.AllowableValues": [
                "AllApps",
                "BIOS",
                "CryptographicErasePD",
                "DIAG",
                "DrvPack",
                "IDRAC",
                "LCData",
                "NonVolatileMemory",
                "OverwritePD",
                "PERCNVCache",
                "vFlash"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SystemErase"
        },
        "#DellLCService.TestNetworkShare": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.TestNetworkShare"
        },
        "#DellLCService.UpdateOSAppHealthData": {
            "UpdateType@Redfish.AllowableValues": [
                "Automatic"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.UpdateOSAppHealthData"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService
---------------------------------------------------------------------------
{
    "Actions": {
        "#DellLicenseManagementService.DeleteLicense": {
            "DeleteOptions@Redfish.AllowableValues": [
                "All",
                "Force",
                "NoOption"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.DeleteLicense"
        },
        "#DellLicenseManagementService.ExportLicense": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicense"
        },
        "#DellLicenseManagementService.ExportLicenseByDevice": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicenseByDevice"
        },
        "#DellLicenseManagementService.ExportLicenseByDeviceToNetworkShare": {
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicenseByDeviceToNetworkShare"
        },
        "#DellLicenseManagementService.ExportLicenseToNetworkShare": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicenseToNetworkShare"
        },
        "#DellLicenseManagementService.ImportLicense": {
            "ImportOptions@Redfish.AllowableValues": [
                "All",
                "Force",
                "NoOption"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ImportLicense"
        },
        "#DellLicenseManagementService.ImportLicenseFromNetworkShare": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ImportOptions@Redfish.AllowableValues": [
                "All",
                "Force",
                "NoOption"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ImportLicenseFromNetworkShare"
        },
        "#DellLicenseManagementService.ShowLicenseBits": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ShowLicenseBits"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService
---------------------------------------------------------------------------
{
    "Actions": {
        "#DellPersistentStorageService.AttachPartition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.AttachPartition"
        },
        "#DellPersistentStorageService.CreatePartition": {
            "PartitionType@Redfish.AllowableValues": [
                "Floppy",
                "HardDisk"
            ],
            "SizeUnit@Redfish.AllowableValues": [
                "GB",
                "MB"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.CreatePartition"
        },
        "#DellPersistentStorageService.CreatePartitionUsingImage": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "PartitionType@Redfish.AllowableValues": [
                "CDROM",
                "Floppy",
                "HardDisk"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.CreatePartitionUsingImage"
        },
        "#DellPersistentStorageService.DeletePartition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.DeletePartition"
        },
        "#DellPersistentStorageService.DetachPartition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.DetachPartition"
        },
        "#DellPersistentStorageService.ExportDataFromPartition": {
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.ExportDataFromPartition"
        },
        "#DellPersistentStorageService.FormatPartition": {
            "FormatType@Redfish.AllowableValues": [
                "EXT2",
                "EXT3",
                "FAT16",
                "FAT32"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.FormatPartition"
        },
        "#DellPersistentStorageService.InitializeMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.InitializeMedia"
        },
        "#DellPersistentStorageService.ModifyPartition": {
            "AccessType@Redfish.AllowableValues": [
                "Read-Only",
                "Read-Write"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.ModifyPartition"
        },
        "#DellPersistentStorageService.VFlashStateChange": {
            "RequestedState@Redfish.AllowableValues": [
                "Disable",
                "Enable"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.VFlashStateChange"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService
--------------------------------------------------------------
{
    "Actions": {
        "#DellTimeService.ManageTime": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService/Actions/DellTimeService.ManageTime"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService
-------------------------------------------------------------------
{
    "Actions": {
        "#DelliDRACCardService.DeleteCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "KMS_SERVER_CA",
                "SEKM_SSL_CERT"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DeleteCertificate"
        },
        "#DelliDRACCardService.DeleteGroup": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DeleteGroup"
        },
        "#DelliDRACCardService.DisableSEKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DisableSEKM"
        },
        "#DelliDRACCardService.DisableiLKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DisableiLKM"
        },
        "#DelliDRACCardService.EnableSEKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.EnableSEKM"
        },
        "#DelliDRACCardService.EnableiLKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.EnableiLKM"
        },
        "#DelliDRACCardService.ExportCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "KMS_SERVER_CA",
                "SEKM_SSL_CERT"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ExportCertificate"
        },
        "#DelliDRACCardService.ExportSSLCertificate": {
            "SSLCertType@Redfish.AllowableValues": [
                "CA",
                "CSC",
                "ClientTrustCertificate",
                "Server"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ExportSSLCertificate"
        },
        "#DelliDRACCardService.FactoryIdentityCertificateGenerateCSR": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.FactoryIdentityCertificateGenerateCSR"
        },
        "#DelliDRACCardService.FactoryIdentityExportCertificate": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.FactoryIdentityExportCertificate"
        },
        "#DelliDRACCardService.FactoryIdentityImportCertificate": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.FactoryIdentityImportCertificate"
        },
        "#DelliDRACCardService.GenerateSEKMCSR": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.GenerateSEKMCSR"
        },
        "#DelliDRACCardService.GetKVMSession": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.GetKVMSession"
        },
        "#DelliDRACCardService.ImportCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "KMS_SERVER_CA",
                "RSYSLOG_SERVER_CA",
                "SEKM_SSL_CERT"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ImportCertificate"
        },
        "#DelliDRACCardService.ImportSSLCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "CA",
                "CSC",
                "ClientTrustCertificate",
                "Server"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ImportSSLCertificate"
        },
        "#DelliDRACCardService.JoinGroup": {
            "CloneConfiguration@Redfish.AllowableValues": [
                "Disable",
                "Enable"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.JoinGroup"
        },
        "#DelliDRACCardService.Rekey": {
            "Mode@Redfish.AllowableValues": [
                "SEKM",
                "iLKM"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.Rekey"
        },
        "#DelliDRACCardService.RemoveSelf": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.RemoveSelf"
        },
        "#DelliDRACCardService.SSLResetCfg": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.SSLResetCfg"
        },
        "#DelliDRACCardService.SendTestEmailAlert": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.SendTestEmailAlert"
        },
        "#DelliDRACCardService.SendTestSNMPTrap": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.SendTestSNMPTrap"
        },
        "#DelliDRACCardService.TestRsyslogServerConnection": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.TestRsyslogServerConnection"
        },
        "#DelliDRACCardService.TestSEKMServerConnection": {
            "ServerType@Redfish.AllowableValues": [
                "Primary",
                "Secondary"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.TestSEKMServerConnection"
        },
        "#DelliDRACCardService.VerifyHWProofOfPossession": {
            "Algorithm@Redfish.AllowableValues": [
                "AES128CBC"
            ],
            "KeyDerivationFunction@Redfish.AllowableValues": [
                "DellSHA256"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.VerifyHWProofOfPossession"
        },
        "#DelliDRACCardService.iDRACReset": {
            "Force@Redfish.AllowableValues": [
                "Force",
                "Graceful"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.iDRACReset"
        },
        "#DelliDRACCardService.iDRACResetCfg": {
            "Force@Redfish.AllowableValues": [
                "Force",
                "Graceful"
            ],
            "Preserve@Redfish.AllowableValues": [
                "All",
                "Default",
                "ResetAllWithRootDefaults"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.iDRACResetCfg"
        },
        "#DelliDRACCardService.iLKMToSEKMTransition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.iLKMToSEKMTransition"
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

/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD
-----------------------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia"
        }
    }
}

/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk
----------------------------------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk/Actions/VirtualMedia.InsertMedia"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1
-------------------------------------
{
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "ForceRestart",
                "GracefulRestart",
                "GracefulShutdown",
                "PushPowerButton",
                "Nmi",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Bios
------------------------------------------
{
    "Actions": {
        "#Bios.ChangePassword": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Actions/Bios.ChangePassword"
        },
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Actions/Bios.ResetBios"
        },
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
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService
--------------------------------------------------------------
{
    "Actions": {
        "#DellBIOSService.DeviceRecovery": {
            "Device@Redfish.AllowableValues": [
                "BIOS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService/Actions/DellBIOSService.DeviceRecovery"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings
-----------------------------------------------------------------------
{
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings/Actions/DellManager.ClearPending"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService
----------------------------------------------------------------
{
    "Actions": {
        "#DellMetricService.ControlMetrics": {
            "MetricCollectionEnabled@Redfish.AllowableValues": [
                "Reset"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService/Actions/DellMetricService.ControlMetrics"
        },
        "#DellMetricService.ExportThermalHistory": {
            "FileType@Redfish.AllowableValues": [
                "CSV",
                "XML"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService/Actions/DellMetricService.ExportThermalHistory"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService
----------------------------------------------------------------------
{
    "Actions": {
        "#DellOSDeploymentService.BootToHD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.BootToHD"
        },
        "#DellOSDeploymentService.BootToISOFromVFlash": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.BootToISOFromVFlash"
        },
        "#DellOSDeploymentService.BootToNetworkISO": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.BootToNetworkISO"
        },
        "#DellOSDeploymentService.ConfigurableBootToNetworkISO": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ResetType@Redfish.AllowableValues": [
                "ColdReset",
                "NoReset",
                "WarmReset"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.ConfigurableBootToNetworkISO"
        },
        "#DellOSDeploymentService.ConnectNetworkISOImage": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.ConnectNetworkISOImage"
        },
        "#DellOSDeploymentService.DeleteISOFromVFlash": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DeleteISOFromVFlash"
        },
        "#DellOSDeploymentService.DetachDrivers": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DetachDrivers"
        },
        "#DellOSDeploymentService.DetachISOFromVFlash": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DetachISOFromVFlash"
        },
        "#DellOSDeploymentService.DetachISOImage": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DetachISOImage"
        },
        "#DellOSDeploymentService.DisconnectNetworkISOImage": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DisconnectNetworkISOImage"
        },
        "#DellOSDeploymentService.DownloadISOToVFlash": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DownloadISOToVFlash"
        },
        "#DellOSDeploymentService.GetAttachStatus": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.GetAttachStatus"
        },
        "#DellOSDeploymentService.GetDriverPackInfo": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.GetDriverPackInfo"
        },
        "#DellOSDeploymentService.GetNetworkISOImageConnectionInfo": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.GetNetworkISOImageConnectionInfo"
        },
        "#DellOSDeploymentService.SkipISOImageBoot": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.SkipISOImageBoot"
        },
        "#DellOSDeploymentService.UnpackAndAttach": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.UnpackAndAttach"
        },
        "#DellOSDeploymentService.UnpackAndShare": {
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.UnpackAndShare"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService
--------------------------------------------------------------
{
    "Actions": {
        "#DellRaidService.AssignSpare": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.AssignSpare"
        },
        "#DellRaidService.BlinkTarget": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.BlinkTarget"
        },
        "#DellRaidService.CancelBackgroundInitialization": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CancelBackgroundInitialization"
        },
        "#DellRaidService.CancelCheckConsistency": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CancelCheckConsistency"
        },
        "#DellRaidService.CancelRebuildPhysicalDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CancelRebuildPhysicalDisk"
        },
        "#DellRaidService.ChangePDState": {
            "State@Redfish.AllowableValues": [
                "Offline",
                "Online"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ChangePDState"
        },
        "#DellRaidService.CheckVDValues": {
            "VDPropNameArrayIn@Redfish.AllowableValues": [
                "RAIDLevel",
                "Size",
                "SpanDepth",
                "SpanLength",
                "StartingLBA",
                "T10PIStatus"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CheckVDValues"
        },
        "#DellRaidService.ClearControllerPreservedCache": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ClearControllerPreservedCache"
        },
        "#DellRaidService.ClearForeignConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ClearForeignConfig"
        },
        "#DellRaidService.ConvertToNonRAID": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ConvertToNonRAID"
        },
        "#DellRaidService.ConvertToRAID": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ConvertToRAID"
        },
        "#DellRaidService.CryptographicEraseWithPSID": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CryptographicEraseWithPSID"
        },
        "#DellRaidService.DisableSecurity": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.DisableSecurity"
        },
        "#DellRaidService.EnableControllerEncryption": {
            "Mode@Redfish.AllowableValues": [
                "DKM",
                "LKM",
                "LKM_TO_SEKM",
                "SEKM"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.EnableControllerEncryption"
        },
        "#DellRaidService.EnableSecurity": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.EnableSecurity"
        },
        "#DellRaidService.GetAvailableDisks": {
            "BlockSizeInBytes@Redfish.AllowableValues": [
                "4096",
                "512",
                "All"
            ],
            "DiskEncrypt@Redfish.AllowableValues": [
                "All",
                "FDE",
                "NonFDE"
            ],
            "DiskType@Redfish.AllowableValues": [
                "All",
                "HDD",
                "SSD"
            ],
            "Diskprotocol@Redfish.AllowableValues": [
                "AllProtocols",
                "NVMe",
                "SAS",
                "SATA"
            ],
            "FormFactor@Redfish.AllowableValues": [
                "All",
                "M.2"
            ],
            "RaidLevel@Redfish.AllowableValues": [
                "NoRAID",
                "RAID0",
                "RAID1",
                "RAID10",
                "RAID5",
                "RAID50",
                "RAID6",
                "RAID60"
            ],
            "T10PIStatus@Redfish.AllowableValues": [
                "All",
                "T10PICapable",
                "T10PIIncapable"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.GetAvailableDisks"
        },
        "#DellRaidService.GetDHSDisks": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.GetDHSDisks"
        },
        "#DellRaidService.GetRAIDLevels": {
            "BlockSizeInBytes@Redfish.AllowableValues": [
                "4096",
                "512",
                "All"
            ],
            "DiskEncrypt@Redfish.AllowableValues": [
                "All",
                "FDE",
                "NonFDE"
            ],
            "DiskType@Redfish.AllowableValues": [
                "All",
                "HDD",
                "SSD"
            ],
            "Diskprotocol@Redfish.AllowableValues": [
                "AllProtocols",
                "NVMe",
                "SAS",
                "SATA"
            ],
            "FormFactor@Redfish.AllowableValues": [
                "All",
                "M.2"
            ],
            "T10PIStatus@Redfish.AllowableValues": [
                "All",
                "T10PICapable",
                "T10PIIncapable"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.GetRAIDLevels"
        },
        "#DellRaidService.ImportForeignConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ImportForeignConfig"
        },
        "#DellRaidService.LockVirtualDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.LockVirtualDisk"
        },
        "#DellRaidService.OnlineCapacityExpansion": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.OnlineCapacityExpansion"
        },
        "#DellRaidService.PrepareToRemove": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.PrepareToRemove"
        },
        "#DellRaidService.RAIDLevelMigration": {
            "NewRaidLevel@Redfish.AllowableValues": [
                "NoRAID",
                "RAID0",
                "RAID1",
                "RAID10",
                "RAID5",
                "RAID50",
                "RAID6",
                "RAID60"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RAIDLevelMigration"
        },
        "#DellRaidService.ReKey": {
            "Mode@Redfish.AllowableValues": [
                "LKM",
                "SEKM"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ReKey"
        },
        "#DellRaidService.RebuildPhysicalDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RebuildPhysicalDisk"
        },
        "#DellRaidService.RemoveControllerKey": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RemoveControllerKey"
        },
        "#DellRaidService.RenameVD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RenameVD"
        },
        "#DellRaidService.ReplacePhysicalDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ReplacePhysicalDisk"
        },
        "#DellRaidService.ResetConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ResetConfig"
        },
        "#DellRaidService.SetAssetName": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.SetAssetName"
        },
        "#DellRaidService.SetBootVD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.SetBootVD"
        },
        "#DellRaidService.SetControllerKey": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.SetControllerKey"
        },
        "#DellRaidService.StartPatrolRead": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.StartPatrolRead"
        },
        "#DellRaidService.StopPatrolRead": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.StopPatrolRead"
        },
        "#DellRaidService.UnBlinkTarget": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.UnBlinkTarget"
        },
        "#DellRaidService.UnLockSecureForeignConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.UnLockSecureForeignConfig"
        },
        "#DellRaidService.UnassignSpare": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.UnassignSpare"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService
------------------------------------------------------------------------------
{
    "Actions": {
        "#DellSoftwareInstallationService.ClearUpdateSchedule": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.ClearUpdateSchedule"
        },
        "#DellSoftwareInstallationService.GetRepoBasedUpdateList": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.GetRepoBasedUpdateList"
        },
        "#DellSoftwareInstallationService.GetUpdateSchedule": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.GetUpdateSchedule"
        },
        "#DellSoftwareInstallationService.InstallFromRepository": {
            "ApplyUpdate@Redfish.AllowableValues": [
                "False",
                "True"
            ],
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.InstallFromRepository"
        },
        "#DellSoftwareInstallationService.InstallFromURI": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.InstallFromURI"
        },
        "#DellSoftwareInstallationService.SetUpdateSchedule": {
            "ApplyReboot@Redfish.AllowableValues": [
                "NoReboot",
                "RebootRequired"
            ],
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.SetUpdateSchedule"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService
--------------------------------------------------------------------------
{
    "Actions": {
        "#DellSwitchConnectionService.ServerPortConnectionRefresh": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService/Actions/DellSwitchConnectionService.ServerPortConnectionRefresh"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService
--------------------------------------------------------------------------
{
    "Actions": {
        "#DellSystemManagementService.ShowErrorsOnLCD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService/Actions/DellSystemManagementService.ShowErrorsOnLCD"
        }
    }
}

/redfish/v1/Systems/System.Embedded.1/SecureBoot
------------------------------------------------
{
    "Actions": {
        "#SecureBoot.ResetKeys": {
            "ResetKeysType@Redfish.AllowableValues": [
                "ResetAllKeysToDefault",
                "DeleteAllKeys",
                "DeletePK",
                "ResetPK",
                "ResetKEK",
                "ResetDB",
                "ResetDBX"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/Actions/SecureBoot.ResetKeys"
        },
        "Oem": {}
    }
}

/redfish/v1/UpdateService
-------------------------
{
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "@Redfish.OperationApplyTimeSupport": {
                "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
                "SupportedValues": [
                    "Immediate",
                    "OnReset",
                    "OnStartUpdateRequest"
                ]
            },
            "TransferProtocol@Redfish.AllowableValues": [
                "HTTP",
                "NFS",
                "CIFS",
                "TFTP",
                "HTTPS"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        },
        "#UpdateService.StartUpdate": {
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.StartUpdate"
        },
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