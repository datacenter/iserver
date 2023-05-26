# Resource: /redfish/v1/CertificateService

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/CertificateService

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
    "Description": "Certificate Service",
    "Id": "CertificateService",
    "Name": "Certificate Service"
}
```

## /redfish/v1/CertificateService/CertificateLocations

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateLocations.CertificateLocations",
    "@odata.id": "/redfish/v1/CertificateService/CertificateLocations",
    "@odata.type": "#CertificateLocations.v1_0_2.CertificateLocations",
    "Description": "The CertificateLocations schema defines a resource that an administrator can use in order to locate all certificates installed on a given service.",
    "Id": "CertificateLocations",
    "Links": {
        "Certificates": [
            {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates/SecurityCertificate.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/PK/Certificates/StdSecbootpolicy.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/KEK/Certificates/StdSecbootpolicy.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.6"
            }
        ],
        "Certificates@odata.count": 7,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "HWCertificates": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/HWCertificates/SecurityCertificate.2"
                }
            }
        }
    },
    "Name": "Certificate Locations"
}
```

