class AssetDeviceContractInformationInfo():
    def __init__(self):
        pass

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
