# Resource: /redfish/v1/AccountService

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/AccountService

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService.AccountService",
    "@odata.etag": "W/\"8F1B1B4B\"",
    "@odata.id": "/redfish/v1/AccountService",
    "@odata.type": "#AccountService.v1_5_0.AccountService",
    "Accounts": {
        "@odata.id": "/redfish/v1/AccountService/Accounts"
    },
    "ActiveDirectory": {
        "AccountProviderType": "ActiveDirectoryService",
        "Authentication": {
            "AuthenticationType": "UsernameAndPassword",
            "Password": null,
            "Username": ""
        },
        "RemoteRoleMapping": [
            {
                "LocalRole": "dirgroupb3d8954f6ebbe735764e9f7c",
                "RemoteGroup": "Administrators"
            },
            {
                "LocalRole": "dirgroup9d4546a03a03bb977c03086a",
                "RemoteGroup": "Authenticated Users:S-1-5-11"
            }
        ],
        "ServiceAddresses": [
            ""
        ],
        "ServiceEnabled": false
    },
    "Description": "iLO User Accounts",
    "Id": "AccountService",
    "LDAP": {
        "AccountProviderType": "ActiveDirectoryService",
        "Authentication": {
            "AuthenticationType": "UsernameAndPassword",
            "Password": null,
            "Username": ""
        },
        "Certificates": {
            "@odata.id": "/redfish/v1/AccountService/ExternalAccountProviders/LDAP/Certificates"
        },
        "LDAPService": {
            "SearchSettings": {}
        },
        "RemoteRoleMapping": [
            {
                "LocalRole": "dirgroupb3d8954f6ebbe735764e9f7c",
                "RemoteGroup": "Administrators"
            },
            {
                "LocalRole": "dirgroup9d4546a03a03bb977c03086a",
                "RemoteGroup": "Authenticated Users:S-1-5-11"
            }
        ],
        "ServiceAddresses": [
            ""
        ],
        "ServiceEnabled": false
    },
    "LocalAccountAuth": "Enabled",
    "MinPasswordLength": 8,
    "Name": "Account Service",
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
    },
    "Roles": {
        "@odata.id": "/redfish/v1/AccountService/Roles"
    }
}
```

## /redfish/v1/AccountService/Accounts

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccountCollection.ManagerAccountCollection",
    "@odata.etag": "W/\"96E00A2C\"",
    "@odata.id": "/redfish/v1/AccountService/Accounts",
    "@odata.type": "#ManagerAccountCollection.ManagerAccountCollection",
    "Description": "iLO User Accounts",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/Accounts/1"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Accounts/4"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Accounts/3"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Accounts/2"
        }
    ],
    "Members@odata.count": 4,
    "Name": "Accounts"
}
```

## /redfish/v1/AccountService/Accounts/1

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccount.ManagerAccount",
    "@odata.etag": "W/\"226E6C7B\"",
    "@odata.id": "/redfish/v1/AccountService/Accounts/1",
    "@odata.type": "#ManagerAccount.v1_3_0.ManagerAccount",
    "Description": "iLO User Account",
    "Id": "1",
    "Links": {
        "Role": {
            "@odata.id": "/redfish/v1/AccountService/Roles/Administrator"
        }
    },
    "Name": "User Account",
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
    },
    "Password": null,
    "PasswordChangeRequired": false,
    "RoleId": "Administrator",
    "UserName": "Administrator"
}
```

## /redfish/v1/AccountService/Accounts/2

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccount.ManagerAccount",
    "@odata.etag": "W/\"6C84CE67\"",
    "@odata.id": "/redfish/v1/AccountService/Accounts/2",
    "@odata.type": "#ManagerAccount.v1_3_0.ManagerAccount",
    "Description": "iLO User Account",
    "Id": "2",
    "Links": {
        "Role": {
            "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnly"
        }
    },
    "Name": "User Account",
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
    },
    "Password": null,
    "PasswordChangeRequired": false,
    "RoleId": "ReadOnly",
    "UserName": "engineer"
}
```

## /redfish/v1/AccountService/Accounts/3

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccount.ManagerAccount",
    "@odata.etag": "W/\"7C3EE72A\"",
    "@odata.id": "/redfish/v1/AccountService/Accounts/3",
    "@odata.type": "#ManagerAccount.v1_3_0.ManagerAccount",
    "Description": "iLO User Account",
    "Id": "3",
    "Links": {
        "Role": {
            "@odata.id": "/redfish/v1/AccountService/Roles/Administrator"
        }
    },
    "Name": "User Account",
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
    },
    "Password": null,
    "PasswordChangeRequired": false,
    "RoleId": "Administrator",
    "UserName": "complab"
}
```

## /redfish/v1/AccountService/Accounts/4

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccount.ManagerAccount",
    "@odata.etag": "W/\"943194D5\"",
    "@odata.id": "/redfish/v1/AccountService/Accounts/4",
    "@odata.type": "#ManagerAccount.v1_3_0.ManagerAccount",
    "Description": "iLO User Account",
    "Id": "4",
    "Links": {
        "Role": {
            "@odata.id": "/redfish/v1/AccountService/Roles/Administrator"
        }
    },
    "Name": "User Account",
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
    },
    "Password": null,
    "PasswordChangeRequired": false,
    "RoleId": "Administrator",
    "UserName": "_HPOneViewAdmin"
}
```

## /redfish/v1/AccountService/DirectoryTest

```{
    "@odata.context": "/redfish/v1/$metadata#HpeDirectoryTest.HpeDirectoryTest",
    "@odata.etag": "W/\"6B3F28F1\"",
    "@odata.id": "/redfish/v1/AccountService/DirectoryTest",
    "@odata.type": "#HpeDirectoryTest.v1_0_0.HpeDirectoryTest",
    "Actions": {
        "#HpeDirectoryTest.StartTest": {
            "target": "/redfish/v1/AccountService/DirectoryTest/Actions/HpeDirectoryTest.StartTest"
        },
        "#HpeDirectoryTest.StopTest": {
            "target": "/redfish/v1/AccountService/DirectoryTest/Actions/HpeDirectoryTest.StopTest"
        }
    },
    "Id": "DirectoryTest",
    "OverallStatus": "NotRun",
    "TestResults": [
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Directory Server DNS Name"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Ping Directory Server"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Connect to Directory Server"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Connect using SSL"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Bind to Directory Server"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Directory Administrator login"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "User Authentication"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "User Authorization"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "Directory User Contexts"
        },
        {
            "Notes": "",
            "Status": "NotRun",
            "TestName": "LOM Object exists"
        }
    ]
}
```

## /redfish/v1/AccountService/ExternalAccountProviders/LDAP/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/AccountService/ExternalAccountProviders/LDAP/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "iLO LDAP Certificate Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/AccountService/Roles

```{
    "@odata.context": "/redfish/v1/$metadata#RoleCollection.RoleCollection",
    "@odata.etag": "W/\"08A22FCA\"",
    "@odata.id": "/redfish/v1/AccountService/Roles",
    "@odata.type": "#RoleCollection.RoleCollection",
    "Description": "iLO Roles Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/Administrator"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/Operator"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnly"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/dirgroupb3d8954f6ebbe735764e9f7c"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/dirgroup9d4546a03a03bb977c03086a"
        }
    ],
    "Members@odata.count": 5,
    "Name": "Roles"
}
```

## /redfish/v1/AccountService/Roles/Administrator

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.etag": "W/\"B60B0A30\"",
    "@odata.id": "/redfish/v1/AccountService/Roles/Administrator",
    "@odata.type": "#Role.v1_2_1.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureManager",
        "ConfigureUsers",
        "ConfigureSelf",
        "ConfigureComponents"
    ],
    "Description": "iLO User Role",
    "Id": "Administrator",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "RemoteConsolePriv",
        "VirtualMediaPriv",
        "VirtualPowerAndResetPriv",
        "HostBIOSConfigPriv",
        "HostNICConfigPriv",
        "HostStorageConfigPriv"
    ],
    "RoleId": "Administrator"
}
```

## /redfish/v1/AccountService/Roles/Operator

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.etag": "W/\"B60B0A30\"",
    "@odata.id": "/redfish/v1/AccountService/Roles/Operator",
    "@odata.type": "#Role.v1_2_1.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureSelf",
        "ConfigureComponents"
    ],
    "Description": "iLO User Role",
    "Id": "Operator",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "RemoteConsolePriv",
        "VirtualMediaPriv",
        "VirtualPowerAndResetPriv",
        "HostBIOSConfigPriv",
        "HostNICConfigPriv",
        "HostStorageConfigPriv"
    ],
    "RoleId": "Operator"
}
```

## /redfish/v1/AccountService/Roles/ReadOnly

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.etag": "W/\"23C5CB60\"",
    "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnly",
    "@odata.type": "#Role.v1_2_1.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureSelf"
    ],
    "Description": "iLO User Role",
    "Id": "ReadOnly",
    "IsPredefined": true,
    "Name": "User Role",
    "RoleId": "ReadOnly"
}
```

## /redfish/v1/AccountService/Roles/dirgroup9d4546a03a03bb977c03086a

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.etag": "W/\"FD9B3B57\"",
    "@odata.id": "/redfish/v1/AccountService/Roles/dirgroup9d4546a03a03bb977c03086a",
    "@odata.type": "#Role.v1_2_1.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureSelf"
    ],
    "Description": "iLO Directory Group Role",
    "Id": "dirgroup9d4546a03a03bb977c03086a",
    "IsPredefined": false,
    "Name": "Group Role",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeDirectoryGroup.HpeDirectoryGroup",
            "@odata.type": "#HpeDirectoryGroup.v1_0_0.HpeDirectoryGroup",
            "GroupDn": "Authenticated Users",
            "GroupSid": "S-1-5-11"
        }
    },
    "RoleId": "dirgroup9d4546a03a03bb977c03086a"
}
```

## /redfish/v1/AccountService/Roles/dirgroupb3d8954f6ebbe735764e9f7c

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.etag": "W/\"0AFBA434\"",
    "@odata.id": "/redfish/v1/AccountService/Roles/dirgroupb3d8954f6ebbe735764e9f7c",
    "@odata.type": "#Role.v1_2_1.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureSelf",
        "ConfigureManager",
        "ConfigureUsers"
    ],
    "Description": "iLO Directory Group Role",
    "Id": "dirgroupb3d8954f6ebbe735764e9f7c",
    "IsPredefined": false,
    "Name": "Group Role",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeDirectoryGroup.HpeDirectoryGroup",
            "@odata.type": "#HpeDirectoryGroup.v1_0_0.HpeDirectoryGroup",
            "GroupDn": "Administrators",
            "GroupSid": ""
        }
    },
    "OemPrivileges": [
        "RemoteConsolePriv",
        "VirtualMediaPriv",
        "VirtualPowerAndResetPriv",
        "HostBIOSConfigPriv",
        "HostNICConfigPriv",
        "HostStorageConfigPriv"
    ],
    "RoleId": "dirgroupb3d8954f6ebbe735764e9f7c"
}
```

## /redfish/v1/AccountService/UserCertificateMapping

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOAccountCertificateMapCollection.HpeiLOAccountCertificateMapCollection",
    "@odata.etag": "W/\"96E00A2C\"",
    "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping",
    "@odata.type": "#HpeiLOAccountCertificateMapCollection.HpeiLOAccountCertificateMapCollection",
    "Description": "iLO User Certificate Mapping",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/1"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/4"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/3"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/2"
        }
    ],
    "Members@odata.count": 4,
    "Name": "UserCertMapping"
}
```

## /redfish/v1/AccountService/UserCertificateMapping/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOAccountCertificateMap.HpeiLOAccountCertificateMap",
    "@odata.etag": "W/\"A643C195\"",
    "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/1",
    "@odata.type": "#HpeiLOAccountCertificateMap.v1_0_1.HpeiLOAccountCertificateMap",
    "Fingerprint": "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00",
    "FingerprintDigestAlgorithm": "SHA256",
    "Id": "1",
    "UserName": "Administrator"
}
```

## /redfish/v1/AccountService/UserCertificateMapping/2

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOAccountCertificateMap.HpeiLOAccountCertificateMap",
    "@odata.etag": "W/\"ACF825D5\"",
    "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/2",
    "@odata.type": "#HpeiLOAccountCertificateMap.v1_0_1.HpeiLOAccountCertificateMap",
    "Fingerprint": "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00",
    "FingerprintDigestAlgorithm": "SHA256",
    "Id": "2",
    "UserName": "engineer"
}
```

## /redfish/v1/AccountService/UserCertificateMapping/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOAccountCertificateMap.HpeiLOAccountCertificateMap",
    "@odata.etag": "W/\"C52D53FA\"",
    "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/3",
    "@odata.type": "#HpeiLOAccountCertificateMap.v1_0_1.HpeiLOAccountCertificateMap",
    "Fingerprint": "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00",
    "FingerprintDigestAlgorithm": "SHA256",
    "Id": "3",
    "UserName": "complab"
}
```

## /redfish/v1/AccountService/UserCertificateMapping/4

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiLOAccountCertificateMap.HpeiLOAccountCertificateMap",
    "@odata.etag": "W/\"B95091A1\"",
    "@odata.id": "/redfish/v1/AccountService/UserCertificateMapping/4",
    "@odata.type": "#HpeiLOAccountCertificateMap.v1_0_1.HpeiLOAccountCertificateMap",
    "Fingerprint": "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00",
    "FingerprintDigestAlgorithm": "SHA256",
    "Id": "4",
    "UserName": "_HPOneViewAdmin"
}
```

