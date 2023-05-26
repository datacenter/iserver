# Resource: /redfish/v1/CertificateService

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/CertificateService

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateService.CertificateService",
    "@odata.etag": "W/\"90FBE318\"",
    "@odata.id": "/redfish/v1/CertificateService",
    "@odata.type": "#CertificateService.v1_0_3.CertificateService",
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
    },
    "CertificateLocations": {
        "@odata.id": "/redfish/v1/CertificateService/CertificateLocations"
    },
    "Description": "Certificate service",
    "Id": "CertificateService",
    "Name": "Certificate Service"
}
```

## /redfish/v1/CertificateService/CertificateLocations

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateLocations.CertificateLocations",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/CertificateService/CertificateLocations",
    "@odata.type": "#CertificateLocations.v1_0_2.CertificateLocations",
    "Description": "Certificate Locations",
    "Id": "CertificateLocations",
    "Name": "Certificate Locations"
}
```

