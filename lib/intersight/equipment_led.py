from lib.intersight.intersight_common import IntersightCommon


class EquipmentLed(IntersightCommon):
    """Class for intersight equipment led objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6026b0086176752d350dec89",
                "ObjectType": "compute.RackUnit",
                "link": "https://www.intersight.com/api/v1/compute/RackUnits/6026b0086176752d350dec89"
            }
        ],
        "ClassId": "equipment.LocatorLed",
        "Color": "unknown",
        "ComputeBlade": null,
        "ComputeRackUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "6026b0086176752d350dec89",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6026b0086176752d350dec89"
        },
        "CreateTime": "2021-02-12T16:43:03.88Z",
        "DeviceMoId": "6026afe76f72612d305f5af6",
        "Dn": "sys/rack-unit-1/locator-led",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EquipmentChassis": null,
        "EquipmentFex": null,
        "InventoryDeviceInfo": null,
        "ModTime": "2022-05-09T13:35:48.286Z",
        "Moid": "6026b0176176752d350df2ad",
        "ObjectType": "equipment.LocatorLed",
        "OperState": "off",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "6026afe76f72612d305f5af6"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6026b0086176752d350dec89",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6026b0086176752d350dec89"
        },
        "PermissionResources": [
            {
                "ClassId": "mo.MoRef",
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
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Rn": "",
        "SharedScope": "",
        "StoragePhysicalDisk": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2de",
            "ObjectType": "storage.PhysicalDisk",
            "link": "https://www.intersight.com/api/v1/storage/PhysicalDisks/6311b01a76752d31398ef2de"
        },
        "Tags": []
    }
    """
    def __init__(self, iaccount, get_filter='"OperState eq \'on\'"', log_id=None):
        self.iobject = 'equipment locatorled'
        self.cache_key = 'locator_led'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id, cache_key=self.cache_key)

    def is_locator_led_on(self, item):
        if item is None:
            return False

        if item['OperState'] == 'off':
            return False

        return True

    def get_all(self, max_errors=3, error_timeout=1):
        items = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if items is not None:
            for item in items:
                item['On'] = self.is_locator_led_on(item)

        return items

    def get_locator_led(self, moid, cache=True):
        if not cache:
            return self.is_locator_led_on(self.get(moid))
        return self.is_locator_led_on(self.get_cache_moid(moid))
