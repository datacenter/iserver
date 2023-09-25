from lib.intersight.intersight_common import IntersightCommon


class EquipmentPsu(IntersightCommon):
    """Class for intersight equipment led objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5efdfb9d6176752d3559bb60",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60"
            }
        ],
        "ClassId": "equipment.Psu",
        "ComputeRackUnit": null,
        "CreateTime": "2020-07-02T15:22:12.078Z",
        "Description": "",
        "DeviceMoId": "5efdfb7e6f72612d30e4501e",
        "Dn": "sys/chassis-1/psu-4",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EquipmentChassis": {
            "ClassId": "mo.MoRef",
            "Moid": "5efdfb9d6176752d3559bb60",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60"
        },
        "EquipmentFex": null,
        "EquipmentRackEnclosure": null,
        "InventoryDeviceInfo": null,
        "ModTime": "2021-06-11T06:52:19.353Z",
        "Model": "PS-2112-9S-LF",
        "Moid": "5efdfba46176752d3559be1a",
        "Name": "",
        "NetworkElement": null,
        "ObjectType": "equipment.Psu",
        "OperReason": [],
            "ClassId": "mo.MoRef",
            "Moid": "62614bdd6f72612d3331038b",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/62614bdd6f72612d3331038b"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "LIT21182DMM",
        "SharedScope": "",
        "Sku": "",
        "Tags": [],
        "Vendor": "Cisco Systems Inc",
        "Vid": "",
        "Voltage": ""
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'equipment psu'
        self.cache_key = 'psu'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id, cache_key=self.cache_key)

    def is_psu_on(self, managed_object):
        if managed_object is None:
            return False

        if managed_object['Voltage'] == 'ok':
            return True

        try:
            if int(managed_object['Voltage']) > 0:
                return True
        except BaseException:
            pass

        return False

    def get_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}
        for key in ['Moid', 'Name', 'Model', 'Serial', 'Vendor', 'Dn', 'Model', 'Vendor', 'Voltage']:
            info[key] = managed_object[key]

        info['On'] = self.is_psu_on(
            managed_object
        )

        if info['On']:
            info['__Output']['On'] = 'Green'
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['__Output']['On'] = 'Red'
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        if info['Voltage'].lower() == 'ok':
            info['__Output']['Voltage'] = 'Green'
        else:
            info['__Output']['Voltage'] = 'Red'

        return info
