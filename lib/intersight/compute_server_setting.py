from lib.intersight.intersight_common import IntersightCommon


class ComputeServerSetting(IntersightCommon):
    """Class for intersight compute server setting objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "AdminLocatorLedState": "None",
        "AdminPowerState": "Policy",
        "Ancestors": [],
        "CertificatesAction": null,
        "ClassId": "compute.ServerSetting",
        "CmosReset": "Ready",
        "ConfigState": "Applied",
        "CreateTime": "2020-12-20T18:50:42.762Z",
        "DeviceMoId": "5fdf9cf26f72612d300aaca0",
        "Dn": "sys/rack-unit-1",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "FrontPanelLockState": "Unlock",
        "KvmReset": "Ready",
        "LocatorLed": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d156176752d35e4b534",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9d156176752d35e4b534"
        },
        "ModTime": "2022-09-30T16:16:23.99Z",
        "Moid": "5fdf9d026573732d30fdb471",
        "Name": "",
        "ObjectType": "compute.ServerSetting",
        "OneTimeBootDevice": "",
        "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdf9cf26f72612d300aaca0"
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
        "PersistentMemoryOperation": {
        "AdminAction": "None",
        "ClassId": "compute.PersistentMemoryOperation",
        "IsSecurePassphraseSet": false,
        "Modules": [],
        "ObjectType": "compute.PersistentMemoryOperation"
        },
        "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9cf26f72612d300aaca0",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9cf26f72612d300aaca0"
        },
        "Rn": "",
        "RunningWorkflow": null,
        "Server": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d026176752d35e4ac4e",
        "ObjectType": "compute.RackUnit",
        "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9d026176752d35e4ac4e"
        },
        "ServerConfig": {
        "AssetTag": "022C2CE",
        "ClassId": "compute.ServerConfig",
        "ObjectType": "compute.ServerConfig",
        "UserLabel": "aio-3-p2b-eu-spdc-WZP23400AKL"
        },
        "ServerOpStatus": [
        {
            "ClassId": "compute.ServerOpStatus",
            "ConfigState": "Applied",
            "ObjectType": "compute.ServerOpStatus",
            "WorkflowType": "compute.ServerPowerOn"
        },
        {
            "ClassId": "compute.ServerOpStatus",
            "ConfigState": "Applied",
            "ObjectType": "compute.ServerOpStatus",
            "WorkflowType": "compute.ServerPowerCycle"
        },
        {
            "ClassId": "compute.ServerOpStatus",
            "ConfigState": "Applied",
            "ObjectType": "compute.ServerOpStatus",
            "WorkflowType": "compute.ServerPowerOff"
        }
        ],
        "SharedScope": "",
        "StorageControllerOperation": {
        "AdminAction": "None",
        "ClassId": "compute.StorageControllerOperation",
        "ControllerId": "",
        "ObjectType": "compute.StorageControllerOperation"
        },
        "StoragePhysicalDriveOperation": {
        "AdminAction": "None",
        "ClassId": "compute.StoragePhysicalDriveOperation",
        "ControllerId": "",
        "ObjectType": "compute.StoragePhysicalDriveOperation",
        "PhysicalDrives": []
        },
        "StorageVirtualDriveOperation": {
        "AdminAction": "None",
        "ClassId": "compute.StorageVirtualDriveOperation",
        "ControllerId": "",
        "ObjectType": "compute.StorageVirtualDriveOperation",
        "VirtualDrives": []
        },
        "Tags": [],
        "TpmReset": "None",
        "TunneledKvmState": "Ready"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'compute serversetting'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def set(self, attributes):
        create_iobject = 'compute updatecomputeserversetting'
        command = 'isctl create %s %s' % (create_iobject, attributes)
        response = self.isctl.create(command)
        return response

    def get_by_device_moid(self, device_moid, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        for item in self.cache:
            if item['DeviceMoId'] == device_moid:
                return item

        return None

    def get_id_by_device_moid(self, device_moid, cache=True):
        item = self.get_by_device_moid(device_moid, cache=cache)
        if item is not None:
            return item['Moid']
        return None
