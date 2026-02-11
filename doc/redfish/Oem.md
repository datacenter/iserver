# Get Oem properties

[[Next]](./Action.md) [[Back]](./README.md)

Resources in Redfish can have optional Oem extensions with vendor specific extensions
- add --oem flag to get Oem properties in resource specified with --uri
- add --deep flag to search for Oem properties recursively starting from --uri resource

## Example: get system oem properties

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --oem

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933,
            "PostCompletionStatus": true,
            "FrontPanelButtonsLocked": false
        }
    },
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "target": "/redfish/v1/Systems/FA11122233/Actions/Oem/ComputerSystem.ResetBIOSCMOS",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS"
            }
        }
    }
}
```

## Example: get all oem properties (deep)

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --oem \
    --deep

/redfish/v1/AccountService
--------------------------
{
    "LDAP": {
        "LDAPService": {
            "Oem": {
                "Cisco": {
                    "LDAPGroupAuthorizationEnabled": false
                }
            }
        }
    },
    "Oem": {
        "Cisco": {
            "PasswordExpiry": {
                "Enabled": false,
                "ExpiryDuration": 0,
                "GracePeriod": 0,
                "NotificationPeriod": 15
            },
            "PasswordHistory": 0,
            "StrongPasswordPolicyEnabled": false
        }
    }
}

...
```

[[Back]](./README.md)