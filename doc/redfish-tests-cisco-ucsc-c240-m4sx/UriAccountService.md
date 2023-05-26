# Resource: /redfish/v1/AccountService

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

## /redfish/v1/AccountService

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService",
    "@odata.id": "/redfish/v1/AccountService",
    "@odata.type": "#AccountService.v1_6_0.AccountService",
    "AccountLockoutCounterResetAfter": 0,
    "AccountLockoutCounterResetEnabled": true,
    "AccountLockoutDuration": 0,
    "AccountLockoutThreshold": 0,
    "Accounts": {
        "@odata.id": "/redfish/v1/AccountService/Accounts"
    },
    "AuthFailureLoggingThreshold": 0,
    "Description": "Account Service",
    "Id": "AccountService",
    "LDAP": {
        "AccountProviderType": "LDAPService",
        "Authentication": {
            "AuthenticationType": "UsernameAndPassword"
        },
        "Certificates": {
            "@odata.id": "/redfish/v1/AccountService/LDAP/Certificates"
        },
        "LDAPService": {
            "SearchSettings": {
                "BaseDistinguishedNames": [],
                "GroupsAttribute": "memberOf",
                "UsernameAttribute": "CiscoAvPair"
            }
        },
        "RemoteRoleMapping": [],
        "ServiceAddresses": [],
        "ServiceEnabled": false
    },
    "LocalAccountAuth": "Fallback",
    "MaxPasswordLength": 20,
    "MinPasswordLength": 8,
    "Name": "Account Service",
    "PrivilegeMap": {
        "@odata.id": "/redfish/v1/AccountService/PrivilegeMap"
    },
    "Roles": {
        "@odata.id": "/redfish/v1/AccountService/Roles"
    },
    "ServiceEnabled": true
}
```

## /redfish/v1/AccountService/Accounts

```null
```

## /redfish/v1/AccountService/LDAP/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/LDAP/Certificates",
    "@odata.id": "/redfish/v1/AccountService/LDAP/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "A Collection of Certificate resource instances.",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/LDAP/Certificates/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/AccountService/LDAP/Certificates/1

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/LDAP/Certificates/Members/$entity",
    "@odata.id": "/redfish/v1/AccountService/LDAP/Certificates/1",
    "@odata.type": "#Certificate.v1_0_1.Certificate",
    "CertificateString": "",
    "CertificateType": "PEM",
    "Id": "Certificate",
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate"
}
```

## /redfish/v1/AccountService/PrivilegeMap

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/PrivilegeMap",
    "@odata.id": "/redfish/v1/AccountService/PrivilegeMap",
    "@odata.type": "#PrivilegeRegistry.v1_1_2.PrivilegeRegistry",
    "Description": "This resource represents the operation to privilege mappings",
    "Id": "PrivilegeMap",
    "Mappings": [
        {
            "Entity": "Manager",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ],
                "POST": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "Chassis",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ],
                "PATCH": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ],
                "POST": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "Systems",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ],
                "PATCH": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ],
                "POST": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "JSONSchemas",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "EventService",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ],
                "PATCH": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ],
                "POST": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "UpdateService",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "SessionService",
            "OperationMap": {
                "DELETE": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ],
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ],
                "POST": [
                    {
                        "Privilege": [
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "TaskService",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "AccountService",
            "OperationMap": {
                "GET": [
                    {
                        "Privilege": [
                            "Login",
                            "ConfigureManager",
                            "ConfigureUsers",
                            "ConfigureSelf",
                            "ConfigureComponents",
                            "OemClearLog",
                            "OemPowerControl",
                            "OemAccessVirtualMedia"
                        ]
                    }
                ]
            }
        }
    ],
    "Name": "Privilege Registry",
    "OEMPrivilegesUsed": [
        "OemClearLog",
        "OemPowerControl",
        "OemAccessVirtualMedia"
    ],
    "PrivilegesUsed": [
        "Login",
        "ConfigureManager",
        "ConfigureUsers",
        "ConfigureSelf",
        "ConfigureComponents"
    ]
}
```

## /redfish/v1/AccountService/Roles

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/Roles",
    "@odata.id": "/redfish/v1/AccountService/Roles",
    "@odata.type": "#RoleCollection.RoleCollection",
    "Description": "Collection of Roles",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/admin"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/user"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/readonly"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/SNMPOnly"
        }
    ],
    "Members@odata.count": 4,
    "Name": "Roles Collection"
}
```

## /redfish/v1/AccountService/Roles/SNMPOnly

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/Roles/Members/$entity",
    "@odata.id": "/redfish/v1/AccountService/Roles/SNMPOnly",
    "@odata.type": "#Role.v1_2_4.Role",
    "AssignedPrivileges": [],
    "Description": "SNMPOnly User Role",
    "Id": "SNMPOnly",
    "IsPredefined": false,
    "Name": "User Role",
    "OemPrivileges": [
        "SNMPAccess"
    ],
    "RoleId": "SNMPOnly"
}
```

## /redfish/v1/AccountService/Roles/admin

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/Roles/Members/$entity",
    "@odata.id": "/redfish/v1/AccountService/Roles/admin",
    "@odata.type": "#Role.v1_2_4.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureManager",
        "ConfigureUsers",
        "ConfigureSelf",
        "ConfigureComponents"
    ],
    "Description": "Admin User Role",
    "Id": "admin",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "OemClearLog",
        "OemPowerControl",
        "OemAccessVirtualMedia"
    ],
    "RoleId": "admin"
}
```

## /redfish/v1/AccountService/Roles/readonly

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/Roles/Members/$entity",
    "@odata.id": "/redfish/v1/AccountService/Roles/readonly",
    "@odata.type": "#Role.v1_2_4.Role",
    "AssignedPrivileges": [
        "Login"
    ],
    "Description": "ReadOnly User Role",
    "Id": "readonly",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [],
    "RoleId": "readonly"
}
```

## /redfish/v1/AccountService/Roles/user

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService/Roles/Members/$entity",
    "@odata.id": "/redfish/v1/AccountService/Roles/user",
    "@odata.type": "#Role.v1_2_4.Role",
    "AssignedPrivileges": [
        "Login"
    ],
    "Description": "User Role",
    "Id": "user",
    "IsPredefined": false,
    "Name": "User Role",
    "OemPrivileges": [
        "OemClearLog",
        "OemPowerControl",
        "OemAccessVirtualMedia"
    ],
    "RoleId": "user"
}
```

