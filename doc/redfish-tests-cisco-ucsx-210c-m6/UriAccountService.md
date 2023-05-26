# Resource: /api-explorer/resources/redfish/v1/AccountService

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/AccountService

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService.AccountService",
    "@odata.id": "/redfish/v1/AccountService",
    "@odata.type": "#AccountService.v1_7_2.AccountService",
    "AccountLockoutCounterResetAfter": 0,
    "AccountLockoutDuration": 0,
    "AccountLockoutThreshold": 0,
    "Accounts": {
        "@odata.id": "/redfish/v1/AccountService/Accounts"
    },
    "Description": "Account Service",
    "Id": "AccountService",
    "LDAP": {
        "LDAPService": {
            "Oem": {
                "Cisco": {
                    "LDAPGroupAuthorizationEnabled": false
                }
            },
            "SearchSettings": {
                "BaseDistinguishedNames": [],
                "GroupsAttribute": null,
                "UsernameAttribute": null
            }
        },
        "RemoteRoleMapping": [],
        "ServiceAddresses": [],
        "ServiceEnabled": null
    },
    "MaxPasswordLength": 127,
    "MinPasswordLength": 8,
    "Name": "Account Service",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "AccountsCapabilities": [
                {
                    "AccountType": "Redfish",
                    "PasswordObfuscationCapabilities": [
                        "OriginalClear"
                    ]
                },
                {
                    "AccountType": "IPMI",
                    "PasswordObfuscationCapabilities": [
                        "OriginalClear"
                    ]
                },
                {
                    "AccountType": "SNMP",
                    "PasswordObfuscationCapabilities": [
                        "OriginalClear"
                    ]
                }
            ]
        }
    },
    "PrivilegeMap": {
        "@odata.id": "/redfish/v1/AccountService/PrivilegeMap"
    },
    "Roles": {
        "@odata.id": "/redfish/v1/AccountService/Roles"
    },
    "ServiceEnabled": true
}
```

## /api-explorer/resources/redfish/v1/AccountService/Accounts

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccountCollection.ManagerAccountCollection",
    "@odata.id": "/redfish/v1/AccountService/Accounts",
    "@odata.type": "#ManagerAccountCollection.ManagerAccountCollection",
    "Description": "Collection of Accounts",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/Accounts/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Account Collection"
}
```

## /api-explorer/resources/redfish/v1/AccountService/Accounts/1

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccount.ManagerAccount",
    "@odata.id": "/redfish/v1/AccountService/Accounts/1",
    "@odata.type": "#ManagerAccount.v1_7_0.ManagerAccount",
    "AccountTypes": [
        "Redfish",
        null,
        "OEM"
    ],
    "Description": "User Account",
    "Enabled": true,
    "Id": "1",
    "Locked": false,
    "Name": "User Account",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "IPMI": {
                "Password": null,
                "UID": 1
            }
        }
    },
    "Password": null,
    "RoleId": "Admin",
    "SNMP": null,
    "UserName": "admin"
}
```

## /api-explorer/resources/redfish/v1/AccountService/PrivilegeMap

```{
    "@odata.context": "/redfish/v1/$metadata#PrivilegeRegistry.PrivilegeRegistry",
    "@odata.id": "/redfish/v1/AccountService/PrivilegeMap",
    "@odata.type": "#PrivilegeRegistry.v1_1_4.PrivilegeRegistry",
    "Description": "This resource represents the operation to privilege mappings",
    "Id": "PrivilegeMap",
    "Mappings": [
        {
            "Entity": "Chassis",
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
                            "ConfigureComponents"
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
                            "ConfigureComponents"
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
            "Entity": "Managers",
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
                            "ConfigureComponents"
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
            "Entity": "AccountService",
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
                            "ConfigureComponents"
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
            "Entity": "*",
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
                            "ConfigureComponents"
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
                            "ConfigureComponents"
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
            "Entity": "TaskService",
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
                            "ConfigureComponents"
                        ]
                    }
                ]
            }
        },
        {
            "Entity": "UpdateService",
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
                            "ConfigureComponents"
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
        }
    ],
    "Name": "Privilege Registry"
}
```

## /api-explorer/resources/redfish/v1/AccountService/Roles

```{
    "@odata.context": "/redfish/v1/$metadata#RoleCollection.RoleCollection",
    "@odata.id": "/redfish/v1/AccountService/Roles",
    "@odata.type": "#RoleCollection.RoleCollection",
    "Description": "Collection of Roles",
    "Members": [
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnly"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/Admin"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/IPMIAdmin"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/IPMIReadOnly"
        },
        {
            "@odata.id": "/redfish/v1/AccountService/Roles/SNMPOnly"
        }
    ],
    "Members@odata.count": 5,
    "Name": "Roles Collection"
}
```

## /api-explorer/resources/redfish/v1/AccountService/Roles/Admin

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/AccountService/Roles/Admin",
    "@odata.type": "#Role.v1_2_5.Role",
    "AssignedPrivileges": [
        "Login",
        "ConfigureManager",
        "ConfigureUsers",
        "ConfigureSelf",
        "ConfigureComponents"
    ],
    "Description": "User Role",
    "Id": "Admin",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "IPMIAdministratorAccess",
        "SNMPAccess"
    ]
}
```

## /api-explorer/resources/redfish/v1/AccountService/Roles/IPMIAdmin

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/AccountService/Roles/IPMIAdmin",
    "@odata.type": "#Role.v1_2_5.Role",
    "Description": "User Role",
    "Id": "IPMIAdmin",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "IPMIAdministratorAccess",
        "SNMPAccess"
    ]
}
```

## /api-explorer/resources/redfish/v1/AccountService/Roles/IPMIReadOnly

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/AccountService/Roles/IPMIReadOnly",
    "@odata.type": "#Role.v1_2_5.Role",
    "Description": "User Role",
    "Id": "IPMIReadOnly",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "IPMIReadonlyAccess",
        "SNMPAccess"
    ]
}
```

## /api-explorer/resources/redfish/v1/AccountService/Roles/ReadOnly

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnly",
    "@odata.type": "#Role.v1_2_5.Role",
    "AssignedPrivileges": [
        "Login"
    ],
    "Description": "User Role",
    "Id": "ReadOnly",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "IPMIReadonlyAccess",
        "SNMPAccess"
    ]
}
```

## /api-explorer/resources/redfish/v1/AccountService/Roles/SNMPOnly

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/AccountService/Roles/SNMPOnly",
    "@odata.type": "#Role.v1_2_5.Role",
    "Description": "User Role",
    "Id": "SNMPOnly",
    "IsPredefined": true,
    "Name": "User Role",
    "OemPrivileges": [
        "SNMPAccess"
    ]
}
```

