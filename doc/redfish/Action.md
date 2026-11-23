# Get Action properties

[[Next]](./GetBootOverride.md) [[Back]](./README.md)

Resources in Redfish can have optional actions property for POST requests description
- add --action flag to get Action properties in resource specified with --uri
- add --deep flag to search for Action properties recursively starting from --uri resource

## Example: get system action properties

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --action

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Actions": {
        "#ComputerSystem.Reset": {
            "target": "/redfish/v1/Systems/FA11122233/Actions/ComputerSystem.Reset",
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "GracefulRestart",
                "ForceRestart",
                "Nmi",
                "PowerCycle"
            ]
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "target": "/redfish/v1/Systems/FA11122233/Actions/Oem/ComputerSystem.ResetBIOSCMOS",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS"
            }
        }
    }
}
```

## Example: get all action properties (deep)

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --action \
    --deep

/redfish/v1/CertificateService
------------------------------
{
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "CertificateCollection@Redfish.AllowableValues": [
                "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
            ],
            "KeyPairAlgorithm@Redfish.AllowableValues": [
                "TPM_ALG_SHA512",
                "TPM_ALG_SHA384",
                "TPM_ALG_SHA1",
                "TPM_ALG_SHA256"
            ],
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR"
        },
        "#CertificateService.ReplaceCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "PEM"
            ],
            "CertificateUri@Redfish.AllowableValues": [
                "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1",
                "/redfish/v1/AccountService/LDAP/Certificates/1",
                "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPServer",
                "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPClient"
            ],
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.ReplaceCertificate"
        }
    }
}

...
```

[[Back]](./README.md)