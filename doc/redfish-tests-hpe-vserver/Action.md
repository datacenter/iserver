# Redfish Action Resources

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
    --action
    --deep
    --max 0

/redfish/v1/AccountService
--------------------------
{
    "Oem": {
        "Hpe": {
            "Actions": {
                "#HpeiLOAccountService.ImportKerberosKeytab": {
                    "target": "/redfish/v1/AccountService/Actions/Oem/Hpe/HpeiLOAccountService.ImportKerberosKeytab"
                }
            }
        }
    }
}

/redfish/v1/AccountService/DirectoryTest
----------------------------------------
{
    "Actions": {
        "#HpeDirectoryTest.StartTest": {
            "target": "/redfish/v1/AccountService/DirectoryTest/Actions/HpeDirectoryTest.StartTest"
        },
        "#HpeDirectoryTest.StopTest": {
            "target": "/redfish/v1/AccountService/DirectoryTest/Actions/HpeDirectoryTest.StopTest"
        }
    }
}

/redfish/v1/CertificateService
------------------------------
{
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "KeyUsage@Redfish.AllowableValues": [
                "DigitalSignature",
                "NonRepudiation",
                "KeyEncipherment",
                "DataEncipherment",
                "KeyAgreement",
                "KeyCertSign",
                "CRLSigning",
                "EncipherOnly",
                "DecipherOnly",
                "ServerAuthentication",
                "ClientAuthentication",
                "CodeSigning",
                "EmailProtection",
                "Timestamping",
                "OCSPSigning"
            ],
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR"
        }
    }
}

/redfish/v1/Chassis/1
---------------------
{
    "Oem": {
        "Hpe": {
            "Actions": {
                "#HpeServerChassis.DisableMCTPOnServer": {
                    "target": "/redfish/v1/Chassis/1/Actions/Oem/Hpe/HpeServerChassis.DisableMCTPOnServer"
                },
                "#HpeServerChassis.FactoryResetMCTP": {
                    "target": "/redfish/v1/Chassis/1/Actions/Oem/Hpe/HpeServerChassis.FactoryResetMCTP"
                }
            }
        }
    }
}

/redfish/v1/EventService
------------------------
{
    "Actions": {
        "#EventService.SubmitTestEvent": {
            "EventType@Redfish.AllowableValues": [
                "StatusChange",
                "ResourceUpdated",
                "ResourceAdded",
                "ResourceRemoved",
                "Alert"
            ],
            "target": "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
        }
    },
    "Oem": {
        "Hpe": {
            "Actions": {
                "#HpeEventService.ImportCACertificate": {
                    "target": "/redfish/v1/EventService/Actions/Oem/Hpe/HpeEventService.ImportCACertificate"
                }
            }
        }
    }
}

/redfish/v1/Managers/1
----------------------
{
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart",
                "GracefulRestart"
            ],
            "target": "/redfish/v1/Managers/1/Actions/Manager.Reset"
        }
    },
    "Oem": {
        "Hpe": {
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
            }
        }
    }
}

/redfish/v1/Managers/1/ActiveHealthSystem
-----------------------------------------
{
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
    }
}

/redfish/v1/Managers/1/NetworkProtocol
--------------------------------------
{
    "Oem": {
        "Hpe": {
            "Actions": {
                "#HpeiLOManagerNetworkService.SendTestAlertMail": {
                    "target": "/redfish/v1/Managers/1/NetworkProtocol/Actions/Oem/Hpe/HpeiLOManagerNetworkService.SendTestAlertMail"
                },
                "#HpeiLOManagerNetworkService.SendTestSyslog": {
                    "target": "/redfish/v1/Managers/1/NetworkProtocol/Actions/Oem/Hpe/HpeiLOManagerNetworkService.SendTestSyslog"
                }
            }
        }
    }
}

/redfish/v1/Managers/1/RemoteSupportService
-------------------------------------------
{
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
    }
}

/redfish/v1/Managers/1/SecurityService/CertificateAuthentication
----------------------------------------------------------------
{
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
    }
}

/redfish/v1/Managers/1/SecurityService/ESKM
-------------------------------------------
{
    "Actions": {
        "#HpeESKM.ClearESKMLog": {
            "target": "/redfish/v1/Managers/1/SecurityService/ESKM/Actions/HpeESKM.ClearESKMLog"
        },
        "#HpeESKM.TestESKMConnections": {
            "target": "/redfish/v1/Managers/1/SecurityService/ESKM/Actions/HpeESKM.TestESKMConnections"
        }
    }
}

/redfish/v1/Managers/1/SecurityService/HttpsCert
------------------------------------------------
{
    "Actions": {
        "#HpeHttpsCert.GenerateCSR": {
            "target": "/redfish/v1/Managers/1/SecurityService/HttpsCert/Actions/HpeHttpsCert.GenerateCSR"
        },
        "#HpeHttpsCert.ImportCertificate": {
            "target": "/redfish/v1/Managers/1/SecurityService/HttpsCert/Actions/HpeHttpsCert.ImportCertificate"
        }
    }
}

/redfish/v1/Managers/1/SecurityService/SSO
------------------------------------------
{
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
    }
}

/redfish/v1/Managers/1/SecurityService/SSO/
-------------------------------------------
{
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
    }
}

/redfish/v1/Managers/1/SnmpService
----------------------------------
{
    "Actions": {
        "#HpeiLOSnmpService.SendSNMPTestAlert": {
            "target": "/redfish/v1/Managers/1/SnmpService/Actions/HpeiLOSnmpService.SendSNMPTestAlert"
        }
    }
}

/redfish/v1/Managers/1/VirtualMedia/1
-------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/1/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/1/Actions/VirtualMedia.InsertMedia"
        }
    },
    "Oem": {
        "Hpe": {
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
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/VirtualMedia.InsertMedia"
        }
    },
    "Oem": {
        "Hpe": {
            "Actions": {
                "#HpeiLOVirtualMedia.EjectVirtualMedia": {
                    "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.EjectVirtualMedia"
                },
                "#HpeiLOVirtualMedia.InsertVirtualMedia": {
                    "target": "/redfish/v1/Managers/1/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.InsertVirtualMedia"
                }
            }
        }
    }
}

/redfish/v1/Systems/1
---------------------
{
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "ForceRestart",
                "Nmi",
                "PushPowerButton",
                "GracefulRestart"
            ],
            "target": "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset"
        }
    },
    "Oem": {
        "Hpe": {
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
            }
        }
    }
}

/redfish/v1/Systems/1/SecureBoot
--------------------------------
{
    "Actions": {
        "#SecureBoot.ResetKeys": {
            "target": "/redfish/v1/Systems/1/SecureBoot/Actions/SecureBoot.ResetKeys"
        }
    }
}

/redfish/v1/Systems/1/SecureEraseReportService
----------------------------------------------
{
    "Actions": {
        "#HpeSecureEraseReportService.DeleteSecureEraseReport": {
            "target": "/redfish/v1/Systems/1/SecureEraseReportService/Actions/HpeSecureEraseReportService.DeleteSecureEraseReport"
        }
    }
}

/redfish/v1/Systems/1/bios
--------------------------
{
    "Actions": {
        "#Bios.ChangePassword": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ChangePasswords/"
        },
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ResetBios/"
        }
    }
}

/redfish/v1/Systems/1/bios/
---------------------------
{
    "Actions": {
        "#Bios.ChangePassword": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ChangePasswords/"
        },
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ResetBios/"
        }
    }
}

/redfish/v1/UpdateService
-------------------------
{
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "TransferProtocol@Redfish.AllowableValues": [
                "HTTP",
                "HTTPS"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        }
    },
    "Oem": {
        "Hpe": {
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
            }
        }
    }
}

/redfish/v1/UpdateService/InstallSets/a74b22b6
----------------------------------------------
{
    "Actions": {
        "#HpeComponentInstallSet.Invoke": {
            "target": "/redfish/v1/UpdateService/InstallSets/a74b22b6/Actions/HpeComponentInstallSet.Invoke"
        }
    }
}
```