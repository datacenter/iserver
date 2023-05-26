# Resource: /api-explorer/resources/redfish/v1/AccountService

Vendor | Model
--- | ---
Cisco | UCSX-9508

## /api-explorer/resources/redfish/v1/AccountService

```{
    "@odata.context": "/redfish/v1/$metadata#AccountService.AccountService",
    "@odata.id": "/redfish/v1/AccountService",
    "@odata.type": "#AccountService.v1_7_0.AccountService",
    "AccountLockoutCounterResetAfter": 0,
    "AccountLockoutDuration": 0,
    "AccountLockoutThreshold": 0,
    "Accounts": {
        "@odata.id": "/redfish/v1/AccountService/Accounts"
    },
    "AuthFailureLoggingThreshold": 0,
    "Description": "Account Service",
    "Id": "AccountService",
    "MaxPasswordLength": 127,
    "MinPasswordLength": 1,
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
    "ServiceEnabled": true
}
```

## /api-explorer/resources/redfish/v1/AccountService/Accounts

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerAccountCollection.ManagerAccountCollection",
    "@odata.id": "/redfish/v1/AccountService/Accounts",
    "@odata.type": "#ManagerAccountCollection.ManagerAccountCollection",
    "Description": "Collection of Accounts",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Account Collection"
}
```

