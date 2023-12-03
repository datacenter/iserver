from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.asset_device_contract_information.info import AssetDeviceContractInformationInfo

class AssetDeviceContractInformation(IntersightCommon, AssetDeviceContractInformationInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'asset devicecontractinformation'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        AssetDeviceContractInformationInfo.__init__(self)
