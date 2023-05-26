# Resource: /api-explorer/resources/redfish/v1/CertificateService

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/CertificateService

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateService.CertificateService",
    "@odata.id": "/redfish/v1/CertificateService",
    "@odata.type": "#CertificateService.v1_0_3.CertificateService",
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR"
        },
        "#CertificateService.ReplaceCertificate": {
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.ReplaceCertificate"
        }
    },
    "CertificateLocations": {
        "@odata.id": "/redfish/v1/CertificateService/CertificateLocations"
    },
    "Description": "Service to manage system certificates",
    "Id": "CertificateService",
    "Name": "Certificate Service"
}
```

## /api-explorer/resources/redfish/v1/CertificateService/CertificateLocations

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateLocations.CertificateLocations",
    "@odata.id": "/redfish/v1/CertificateService/CertificateLocations",
    "@odata.type": "#CertificateLocations.v1_0_2.CertificateLocations",
    "Description": "Service to manage system certificates",
    "Id": "CertificateLocations",
    "Links": {
        "Certificates": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPClient"
            },
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPServer"
            },
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
            },
            {
                "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/SPDMTrustStore/Certificates/1"
            }
        ],
        "Certificates@odata.count": 4
    },
    "Name": "Certificate Locations"
}
```

