from lib.intersight.intersight_common import IntersightCommon


class AssetDeviceContractInformation(IntersightCommon):
    """Class for intersight asset device contract information objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [],
        "ClassId": "asset.DeviceContractInformation",
        "Contract": {
            "BillTo": {
                "Address1": "",
                "Address2": "",
                "Address3": "",
                "City": "",
                "ClassId": "asset.AddressInformation",
                "Country": "",
                "County": "",
                "Location": "",
                "Name": "",
                "ObjectType": "asset.AddressInformation",
                "PostalCode": "",
                "Province": "",
                "State": ""
            },
            "BillToGlobalUltimate": {
                "ClassId": "asset.GlobalUltimate",
                "Id": "",
                "Name": "",
                "ObjectType": "asset.GlobalUltimate"
            },
            "ClassId": "asset.ContractInformation",
            "ContractNumber": "",
            "LineStatus": "NEVER COVERED",
            "ObjectType": "asset.ContractInformation"
        },
        "ContractStatus": "Not Covered",
        "ContractStatusReason": "",
        "ContractUnavailableRetryCount": 0,
        "ContractUpdatedTime": "2022-11-15T22:03:14.439Z",
        "CoveredProductLineEndDate": "",
        "CreateTime": "2022-02-04T07:29:30.967Z",
        "DeviceId": "FDO25500ZVK",
        "DeviceType": "CiscoNexusSwitch",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EndCustomer": {
            "Address": {
                "Address1": "VIA SANTA MARIA MOLGORA 48 C",
                "Address2": "",
                "Address3": "",
                "City": "VIMERCATE",
                "ClassId": "asset.AddressInformation",
                "Country": "IT",
                "County": "",
                "Location": "",
                "Name": "",
                "ObjectType": "asset.AddressInformation",
                "PostalCode": "20871",
                "Province": "",
                "State": "LOMBARDIA"
            },
            "ClassId": "asset.CustomerInformation",
            "Id": "1001745576",
            "Name": "CISCO PHOTONICS ITALY  SRL",
            "ObjectType": "asset.CustomerInformation"
        },
        "EndUserGlobalUltimate": {
            "ClassId": "asset.GlobalUltimate",
            "Id": "52428",
            "Name": "CISCO SYSTEMS INC",
            "ObjectType": "asset.GlobalUltimate"
        },
        "IsValid": true,
        "managed_objectType": "CHASSIS",
        "MaintenancePurchaseOrderNumber": "",
        "MaintenanceSalesOrderNumber": "",
        "ModTime": "2022-11-15T22:03:15.018Z",
        "Moid": "61fcd5da6265722d3016f18a",
        "ObjectType": "asset.DeviceContractInformation",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5fe1ddc96f72612d304f7531"
        ],
        "PermissionResources": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5dee1d736972652d321d26b5",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "625706a06972652d3202a8f9",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6242d1016972652d32eda017",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
            }
        ],
        "PlatformType": "APIC",
        "Product": {
            "BillTo": {
                "Address1": "PALAZZO ACERO",
                "Address2": "VIA TORRI BIANCHE 8",
                "Address3": "",
                "City": "VIMERCATE",
                "ClassId": "asset.AddressInformation",
                "Country": "IT",
                "County": "",
                "Location": "405085",
                "Name": "CISCO SYSTEMS ITALY SRL",
                "ObjectType": "asset.AddressInformation",
                "PostalCode": "20871",
                "Province": "",
                "State": ""
            },
            "ClassId": "asset.ProductInformation",
            "Description": "Nexus 9300 Series, 32p 400G QSFP-DD",
            "Family": "N9300",
            "Group": "SWITCH",
            "Number": "N9K-C9332D-GX2B",
            "ObjectType": "asset.ProductInformation",
            "ShipTo": {
                "Address1": "VIA SANTA MARIA MOLGORA 48 C",
                "Address2": "",
                "Address3": "",
                "City": "VIMERCATE",
                "ClassId": "asset.AddressInformation",
                "Country": "IT",
                "County": "",
                "Location": "1001745576",
                "Name": "CISCO PHOTONICS ITALY  SRL",
                "ObjectType": "asset.AddressInformation",
                "PostalCode": "20871",
                "Province": "",
                "State": "LOMBARDIA"
            },
            "SubType": "N9300 SERIES"
        },
        "PurchaseOrderNumber": "PR555627",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5fe1ddc96f72612d304f7531",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fe1ddc96f72612d304f7531"
        },
        "ResellerGlobalUltimate": {
            "ClassId": "asset.GlobalUltimate",
            "Id": "",
            "Name": "",
            "ObjectType": "asset.GlobalUltimate"
        },
        "SalesOrderNumber": "113581639",
        "ServiceDescription": "Nexus 9300 Series, 32p 400G QSFP-DD",
        "ServiceEndDate": "0001-01-01T00:00:00Z",
        "ServiceLevel": "",
        "ServiceSku": "",
        "ServiceStartDate": "0001-01-01T00:00:00Z",
        "SharedScope": "",
        "Source": {
            "ClassId": "mo.MoRef",
            "Moid": "61fcd5da77616e2d31925d37",
            "ObjectType": "niatelemetry.NiaInventory",
            "link": "https://www.intersight.com/api/v1/niatelemetry/NiaInventories/61fcd5da77616e2d31925d37"
        },
        "StateContract": "OK",
        "Tags": [],
        "WarrantyEndDate": "2023-04-14T00:00:00Z",
        "WarrantyType": "WARR-1YR-LTD-HW"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'asset devicecontractinformation'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['Moid'] = managed_object['Moid']
        info['PurchaseOrderNumber'] = managed_object['PurchaseOrderNumber']
        info['SalesOrderNumber'] = managed_object['SalesOrderNumber']
        info['ContractStatus'] = managed_object['ContractStatus']
        info['ContractNumber'] = managed_object['Contract']['ContractNumber']
        info['ContractUpdatedTime'] = managed_object['ContractUpdatedTime']
        info['ServiceDescription'] = managed_object['ServiceDescription']
        info['ServiceLevel'] = managed_object['ServiceLevel']
        info['ServiceSku'] = managed_object['ServiceSku']
        info['ServiceStartDate'] = managed_object['ServiceStartDate']
        info['ServiceEndDate'] = managed_object['ServiceEndDate']
        info['IsValid'] = managed_object['IsValid']

        if info['ContractStatus'] == 'Active':
            info['__Output']['ContractStatus'] = 'Green'
        else:
            info['__Output']['ContractStatus'] = 'Red'

        return info
