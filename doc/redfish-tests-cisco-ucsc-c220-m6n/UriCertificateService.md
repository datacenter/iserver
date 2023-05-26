# Resource: /redfish/v1/CertificateService

Vendor | Model
--- | ---
Cisco | UCSC-C220-M6N

## /redfish/v1/CertificateService

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateService.CertificateService",
    "@odata.id": "/redfish/v1/CertificateService",
    "@odata.type": "#CertificateService.v1_0_1.CertificateService",
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "CertificateCollection@Redfish.AllowableValues": [
                "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
            ],
            "KeyCurveId@Redfish.AllowableValues": [
                "TPM_ECC_NIST_P256",
                "TPM_ECC_NIST_P384"
            ],
            "KeyPairAlgorithm@Redfish.AllowableValues": [
                "TPM_ALG_SHA512",
                "TPM_ALG_SHA384",
                "TPM_ALG_SHA1",
                "TPM_ALG_SHA256",
                "TPM_ALG_ECDSA"
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
    },
    "CertificateLocations": {
        "@odata.id": "/redfish/v1/CertificateService/CertificateLocations"
    },
    "Description": "Certificate Service",
    "Id": "CertificateService",
    "Name": "Certificate Service"
}
```

## /redfish/v1/CertificateService/CertificateLocations

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateLocations.CertificateLocations",
    "@odata.id": "/redfish/v1/CertificateService/CertificateLocations",
    "@odata.type": "#CertificateLocations.v1_0_1.CertificateLocations",
    "Description": "Certificate Locations",
    "Id": "CertificateLocation",
    "Links": {
        "Certificates": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
            },
            {
                "@odata.id": "/redfish/v1/AccountService/LDAP/Certificates/1"
            },
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPClient"
            },
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPServer"
            }
        ]
    },
    "Name": "Certificate Location"
}
```

