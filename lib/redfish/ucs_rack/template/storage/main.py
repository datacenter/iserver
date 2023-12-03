import json


class RedfishEndpointUcsRackTemplateStorage():
    def __init__(self):
        self.defult_storage_uri = '/redfish/v1/Systems/SYSTEM_ID/Storage'

    def get_storage_uri(self):
        return self.path_fixup(self.defult_storage_uri)

    def get_storage_controllers_uri(self):
        uri = self.get_storage_uri()
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_storage_controller_info(self, uri):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        info['Id'] = data['Id']
        info['Drive'] = []
        for drive_mo in data['Drives']:
            drive_info = {}
            drive_info['uri'] = drive_mo['@odata.id']
            info['Drive'].append(
                drive_info
            )

        info['PhysicalDiskCount'] = len(info['Drive'])

        info['Volume'] = []
        if 'Volumes' in data:
            if data['Volumes'] is not None:
                if isinstance(data['Volumes'], dict):
                    volume_data = self.get_properties(data['Volumes']['@odata.id'])
                    if volume_data is not None:
                        for item in volume_data['Members']:
                            volume_info = {}
                            volume_info['uri'] = item['@odata.id']
                            info['Volume'].append(
                                volume_info
                            )

        info['VirtualDriveCount'] = len(info['Volume'])

        if len(data['StorageControllers']) != 1:
            self.log.error(
                'get_storage_controller_info',
                'Unexpected storage controller count: %s' % (uri)
            )
            return None

        storage_controller_mo = data['StorageControllers'][0]
        info['FirmwareVersion'] = self.get_property_value(
            storage_controller_mo,
            'FirmwareVersion'
        )
        info['Vendor'] = self.get_property_value(
            storage_controller_mo,
            'Manufacturer'
        )
        info['Pid'] = self.get_property_value(
            storage_controller_mo,
            'Model'
        )
        info['Model'] = self.get_property_value(
            storage_controller_mo,
            'Name'
        )
        info['Oem'] = None
        if info['Vendor'] == 'Cisco Systems Inc' or 'Cisco' in storage_controller_mo['Oem']:
            info['Oem'] = self.get_property_value(
                storage_controller_mo,
                'Oem:Cisco'
            )
        else:
            self.log.error(
                'get_storage_controller_info',
                'Unrecognized storage controller vendor: %s' % (uri)
            )

        info['PciSlot'] = self.get_property_value(
            storage_controller_mo,
            'Oem:Cisco:PCIeSlot'
        )
        info['SerialNumber'] = self.get_property_value(
            storage_controller_mo,
            'SerialNumber'
        )
        info['Health'] = self.get_property_value(
            storage_controller_mo,
            'Status:Health'
        )
        info['State'] = self.get_property_value(
            storage_controller_mo,
            'Status:State'
        )
        info['SupportedControllerProtocols'] = self.get_property_value(
            storage_controller_mo,
            'SupportedControllerProtocols'
        )
        info['SupportedDeviceProtocols'] = self.get_property_value(
            storage_controller_mo,
            'SupportedDeviceProtocols'
        )
        info['SupportedRAIDTypes'] = self.get_property_value(
            storage_controller_mo,
            'SupportedRAIDTypes'
        )

        info['LocationType'] = self.get_property_value(
            storage_controller_mo,
            'Location:PartLocation:LocationType'
        )

        info['Slot'] = None
        if info['LocationType'] == 'Slot':
            info['Slot'] = self.get_property_value(
                storage_controller_mo,
                'Location:PartLocation:ServiceLabel'
            )

        return info

    def get_storage_controllers_info(self):
        info = []
        controllers_uri = self.get_storage_controllers_uri()
        for controller_uri in controllers_uri:
            controller_info = self.get_storage_controller_info(
                controller_uri
            )
            if controller_info is not None:
                info.append(
                    controller_info
                )
        return info

    def get_storage_drive_info(self, uri, controller_id):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        info['DiskId'] = self.get_property_value(
            data,
            'Id'
        )
        info['StorageControllerId'] = controller_id
        info['Model'] = self.get_property_value(
            data,
            'Name'
        )
        info['Type'] = self.get_property_value(
            data,
            'MediaType'
        )
        info['Pid'] = self.get_property_value(
            data,
            'Model'
        )
        info['Vendor'] = self.get_property_value(
            data,
            'Manufacturer'
        )
        info['Revision'] = self.get_property_value(
            data,
            'Revision'
        )
        info['SerialNumber'] = self.get_property_value(
            data,
            'SerialNumber'
        )
        info['Protocol'] = self.get_property_value(
            data,
            'Protocol'
        )
        info['Health'] = self.get_property_value(
            data,
            'Status:Health'
        )
        info['State'] = self.get_property_value(
            data,
            'Status:State'
        )
        if info['State'] == 'Absent':
            return None

        if info['Health'] in [None, 'OK'] and info['State'] == 'Enabled':
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            print(json.dumps(data, indent=4))
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        info['LocationType'] = self.get_property_value(
            data,
            'PhysicalLocation:PartLocation:LocationType'
        )
        info['Slot'] = None
        if info['LocationType'] == 'Slot':
            info['Slot'] = self.get_property_value(
                data,
                'PhysicalLocation:PartLocation:ServiceLabel'
            )

        info['Oem'] = self.get_property_value(
            data,
            'Oem:Cisco'
        )

        info['Bootable'] = self.get_property_value(
            data,
            'Oem:Cisco:Bootable'
        )
        info['BootableTick'] = '\u2717'
        info['__Output']['BootableTick'] = 'Red'

        if info['Bootable'] is not None:
            if info['Bootable']:
                info['BootableTick'] = '\u2713'
                info['__Output']['BootableTick'] = 'Green'

        info['BlockSizeBytes'] = self.get_property_value(
            data,
            'BlockSizeBytes'
        )

        info['CapableSpeedGbs'] = self.get_property_value(
            data,
            'CapableSpeedGbs'
        )
        info['LinkSpeed'] = ''
        if info['CapableSpeedGbs'] is not None:
            info['LinkSpeed'] = '%s gb/s' % (
                info['CapableSpeedGbs']
            )

        info['EncryptionAbility'] = self.get_property_value(
            data,
            'EncryptionAbility'
        )

        info['FailurePredicted'] = self.get_property_value(
            data,
            'FailurePredicted'
        )

        info['CapacityBytes'] = self.get_property_value(
            data,
            'CapacityBytes'
        )
        info['SizeUnit'] = self.info_handler.convert_storage(
            info['CapacityBytes']
        )

        info['HotspareType'] = self.get_property_value(
            data,
            'HotspareType'
        )

        info['IndicatorLED'] = self.get_property_value(
            data,
            'IndicatorLED'
        )

        info['PredictedMediaLifeLeftPercent'] = self.get_property_value(
            data,
            'PredictedMediaLifeLeftPercent'
        )

        return info

    def get_storage_volume_info(self, uri, controller_id):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        info['VirtualDriveId'] = self.get_property_value(
            data,
            'Id'
        )

        info['StorageControllerId'] = controller_id

        info['PhysicalDiskUri'] = []
        drives = self.get_property_value(
            data,
            'Links:Drives'
        )
        if drives is not None:
            for drive in drives:
                info['PhysicalDiskUri'].append(
                    drive['@odata.id']
                )

        info['PhysicalDiskCount'] = len(info['PhysicalDiskUri'])

        info['CapacityBytes'] = self.get_property_value(
            data,
            'CapacityBytes'
        )
        info['SizeUnit'] = self.info_handler.convert_storage(
            info['CapacityBytes']
        )

        info['Name'] = self.get_property_value(
            data,
            'Name'
        )

        info['Type'] = self.get_property_value(
            data,
            'RAIDType'
        )

        info['Oem'] = self.get_property_value(
            data,
            'Oem:Cisco'
        )

        info['Bootable'] = self.get_property_value(
            data,
            'Oem:Cisco:Bootable'
        )
        info['BootableTick'] = '\u2717'
        info['__Output']['BootableTick'] = 'Red'

        if info['Bootable'] is not None:
            if info['Bootable']:
                info['BootableTick'] = '\u2713'
                info['__Output']['BootableTick'] = 'Green'

        info['Health'] = self.get_property_value(
            data,
            'Status:Health'
        )
        info['State'] = self.get_property_value(
            data,
            'Status:State'
        )

        info['DriveState'] = self.get_property_value(
            data,
            'Oem:Cisco:VolumeState'
        )

        if info['DriveState'] == 'Optimal':
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        info['ActualWriteCachePolicy'] = self.get_property_value(
            data,
            'Oem:Cisco:ConfiguredWriteCachePolicy'
        )

        return info

    def get_template_storage_properties(self):
        properties = {}
        properties['Controller'] = self.get_storage_controllers_info()

        properties['Drive'] = []
        for controller_info in properties['Controller']:
            drive_count = 0
            for drive_mo in controller_info['Drive']:
                drive_info = self.get_storage_drive_info(
                    drive_mo['uri'],
                    controller_info['Id']
                )
                if drive_info is not None:
                    properties['Drive'].append(
                        drive_info
                    )
                    drive_count = drive_count + 1

            controller_info['PhysicalDiskCount'] = drive_count

        properties['Volume'] = []
        for controller_info in properties['Controller']:
            volume_count = 0
            for volume_mo in controller_info['Volume']:
                volume_info = self.get_storage_volume_info(
                    volume_mo['uri'],
                    controller_info['Id']
                )
                if volume_info is not None:
                    properties['Volume'].append(
                        volume_info
                    )
                    volume_count = volume_count + 1

            controller_info['VirtualDriveCount'] = volume_count

        for volume_info in properties['Volume']:
            for disk_uri in volume_info['PhysicalDiskUri']:
                for drive_info in properties['Drive']:
                    if drive_info['Uri'] == disk_uri:
                        drive_info['VirtualDriveId'] = volume_info['VirtualDriveId']

        return properties
