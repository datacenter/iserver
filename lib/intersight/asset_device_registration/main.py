from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.asset_device_registration.info import AssetDeviceRegistrationInfo


class AssetDeviceRegistration(IntersightCommon, AssetDeviceRegistrationInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'asset deviceregistration'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        AssetDeviceRegistrationInfo.__init__(self)

    def create_target(self, serial_number, security_token):
        self.iobject = 'asset deviceclaim'
        create_attributes = ''
        create_attributes = '%s --SerialNumber %s' % (create_attributes, serial_number)
        create_attributes = '%s --SecurityToken %s' % (create_attributes, security_token)

        response = self.create(
            create_attributes,
            get_response=True,
            json_conversion=True
        )
        return response

    def delete_target(self, moid):
        self.iobject = 'asset deviceclaim'
        return self.delete(moid)
