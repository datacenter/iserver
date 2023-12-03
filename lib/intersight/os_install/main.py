import json
from lib import output_helper
from lib.intersight.intersight_common import IntersightCommon


class OsInstall(IntersightCommon):
    def __init__(self, iaccount, dry_run=False, silent=False, verbose=False, debug=False, log_id=None):
        self.iobject = 'os install'
        self.dry_run = dry_run
        IntersightCommon.__init__(self, iaccount, self.iobject, silent=silent, verbose=verbose, debug=debug, log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def create_embedded(self, attributes):
        """Create os install object in Intersight to trigger bare metal OS installation

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        create_attributes = '%s --InstallMethod vMedia' % (create_attributes)
        create_attributes = '%s --Server="MoRef:ComputeRackUnitRelationship[Moid:%s]"' % (create_attributes, attributes['server_id'])
        create_attributes = '%s --Image=MoRef[Moid:%s]' % (create_attributes, attributes['image']['id'])
        create_attributes = '%s --OsduImage=MoRef[Moid:%s]' % (create_attributes, attributes['scu_id'])
        create_attributes = '%s --Organization=MoRef[Moid:%s]' % (create_attributes, attributes['organization_id'])

        install_target = {}
        install_target['ObjectType'] = 'os.VirtualDrive'
        install_target['StorageControllerSlotId'] = attributes['storage_controller_slot']
        install_target['Id'] = attributes['virtual_drive_id']
        install_target['Name'] = attributes['virtual_drive_name']
        create_attributes = '%s --InstallTarget=\'%s\'' % (create_attributes, json.dumps(install_target))

        answers = {}
        answers['Source'] = 'Embedded'
        create_attributes = '%s --Answers=\'%s\'' % (create_attributes, json.dumps(answers))

        command = 'isctl create os install %s' % (create_attributes.replace(' --', '\n\t--'))
        self.my_output.info(command)
        if self.dry_run:
            self.my_output.default(command)
            return dict(success=True)

        response = IntersightCommon.create(
            self,
            create_attributes,
            get_response=True,
            json_conversion=True
        )
        return response

    def create_template_dhcp(self, attributes):
        """Create os install object in Intersight to trigger bare metal OS installation

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        create_attributes = '%s --InstallMethod vMedia' % (create_attributes)
        create_attributes = '%s --Server="MoRef:ComputeRackUnitRelationship[Moid:%s]"' % (create_attributes, attributes['server_id'])
        create_attributes = '%s --Image=MoRef[Moid:%s]' % (create_attributes, attributes['image']['id'])
        create_attributes = '%s --ConfigurationFile=MoRef[Moid:%s]' % (create_attributes, attributes['configuration_file_id'])
        create_attributes = '%s --OsduImage=MoRef[Moid:%s]' % (create_attributes, attributes['scu_id'])
        create_attributes = '%s --Organization=MoRef[Moid:%s]' % (create_attributes, attributes['organization_id'])

        install_target = {}
        install_target['ObjectType'] = 'os.VirtualDrive'
        install_target['StorageControllerSlotId'] = attributes['storage_controller_slot']
        install_target['Id'] = attributes['virtual_drive_id']
        install_target['Name'] = attributes['virtual_drive_name']
        create_attributes = '%s --InstallTarget=\'%s\'' % (create_attributes, json.dumps(install_target))

        answers = {}
        answers['Source'] = 'Template'
        answers['IpConfigType'] = 'DHCP'
        answers['IpConfiguration'] = {}
        answers['IpConfiguration']['ObjectType'] = 'os.Ipv4Configuration'
        if attributes['interface_mac'] == '':
            answers['NetworkDevice'] = attributes['interface_name']
        else:
            answers['NetworkDevice'] = attributes['interface_mac']
        answers['Hostname'] = attributes['hostname']
        answers['IsRootPasswordCrypted'] = False
        answers['RootPassword'] = attributes['password']
        create_attributes = '%s --Answers=\'%s\'' % (create_attributes, json.dumps(answers))

        command = 'isctl create os install %s' % (create_attributes.replace(' --', '\n\t--'))
        self.my_output.info(command)
        if self.dry_run:
            self.my_output.default(command)
            return dict(success=True)

        response = IntersightCommon.create(
            self,
            create_attributes,
            get_response=True,
            json_conversion=True
        )
        return response

    def create_template_static(self, attributes):
        """Create os install object in Intersight to trigger bare metal OS installation

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        create_attributes = '%s --InstallMethod vMedia' % (create_attributes)
        create_attributes = '%s --Server="MoRef:ComputeRackUnitRelationship[Moid:%s]"' % (create_attributes, attributes['server_id'])
        create_attributes = '%s --Image=MoRef[Moid:%s]' % (create_attributes, attributes['image']['id'])
        create_attributes = '%s --ConfigurationFile=MoRef[Moid:%s]' % (create_attributes, attributes['configuration_file_id'])
        create_attributes = '%s --OsduImage=MoRef[Moid:%s]' % (create_attributes, attributes['scu_id'])
        create_attributes = '%s --Organization=MoRef[Moid:%s]' % (create_attributes, attributes['organization_id'])

        install_target = {}
        install_target['ObjectType'] = 'os.VirtualDrive'
        install_target['StorageControllerSlotId'] = attributes['storage_controller_slot']
        install_target['Id'] = attributes['virtual_drive_id']
        install_target['Name'] = attributes['virtual_drive_name']
        create_attributes = '%s --InstallTarget=\'%s\'' % (create_attributes, json.dumps(install_target))

        answers = {}
        answers['Source'] = 'Template'
        answers['IpConfigType'] = 'static'
        answers['IpConfiguration'] = {}
        answers['IpConfiguration']['ObjectType'] = 'os.Ipv4Configuration'
        answers['IpConfiguration']['IpV4Config'] = {}
        answers['IpConfiguration']['IpV4Config']['IpAddress'] = attributes['ipv4_address']
        answers['IpConfiguration']['IpV4Config']['Netmask'] = attributes['ipv4_mask']
        answers['IpConfiguration']['IpV4Config']['Gateway'] = attributes['ipv4_gateway']
        if attributes['interface_mac'] == '':
            answers['NetworkDevice'] = attributes['interface_name']
        else:
            answers['NetworkDevice'] = attributes['interface_mac']
        answers['Nameserver'] = attributes['nameserver']
        answers['Hostname'] = attributes['hostname']
        answers['IsRootPasswordCrypted'] = False
        answers['RootPassword'] = attributes['password']
        create_attributes = '%s --Answers=\'%s\'' % (create_attributes, json.dumps(answers))

        command = 'isctl create os install %s' % (create_attributes.replace(' --', '\n\t--'))
        self.my_output.info(command)
        if self.dry_run:
            self.my_output.default(command)
            return dict(success=True)

        response = IntersightCommon.create(
            self,
            create_attributes,
            get_response=True,
            json_conversion=True
        )
        return response

    def create_os_install(self, attributes):
        """Create os install object in Intersight to trigger bare metal OS installation

        Returns:
            bool: success or failure
        """
        if attributes['type'] == 'embedded':
            return self.create_embedded(attributes)

        if attributes['type'] == 'template':
            if attributes['ip_config'] == 'dhcp':
                return self.create_template_dhcp(attributes)
            if attributes['ip_config'] == 'static':
                return self.create_template_static(attributes)

        return dict(success=False, response=None)
