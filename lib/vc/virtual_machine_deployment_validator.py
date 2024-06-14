import os
import json
import uuid
import datetime
import bcrypt

from lib.input_validator import InputValidator

from lib import file_helper
from lib import ip_helper
from lib import log_helper
from lib import output_helper

from lib.vc import helper
from lib.vc import vcenter
from lib import ssh
from lib import template


class VcVirtualMachineDeploymentValidator(InputValidator):
    def __init__(self, log_id=None, verbose=False, debug=False):
        InputValidator.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log_handler = log_helper.Log(log_id=log_id)

        self.my_output = output_helper.OutputHelper(log_id=log_id, verbose=verbose, debug=debug)
        self.template_handler = template.Template(debug=debug, log_id=log_id)
        self.template_category = 'vc'
        self.vc_helper_handler = helper.VcHelper()
        self.vcenter_handler = None
        self.user_input = None
        self.vm_parameters = {}

    def validate_settings(self):
        self.my_output.debug('Validate settings section', underline=True, before_newline=True)

        self.vm_parameters['settings'] = {}
        for key in self.user_input['settings']:
            self.vm_parameters['settings'][key] = self.user_input['settings'][key]

        self.my_output.debug('Completed')
        return True

    def validate_datacenter_name(self):
        datacenters = self.vcenter_handler.get_datacenters()
        if datacenters is None:
            self.my_output.error('No datacenters found')
            return False

        datacenter_name = self.vm_parameters['vcenter']['datacenter']
        for datacenter in datacenters:
            if datacenter['name'] == datacenter_name:
                self.my_output.debug('Datacenter found: %s' % (datacenter_name))
                return True

        self.my_output.error('Datacenter not found: %s' % (datacenter_name))
        return False

    def validate_datastore_name(self):
        datacenter_name = self.vm_parameters['vcenter']['datacenter']
        datastores = self.vcenter_handler.get_datastores(datacenter_name=datacenter_name)

        if datastores is None:
            self.my_output.error('No datastores found')
            return False

        datastore_name = self.vm_parameters['vcenter']['datastore']
        for datastore in datastores:
            if datastore['name'] == datastore_name:
                self.my_output.debug('Datastore found: %s' % (datastore_name))
                return datastore_name

        self.my_output.error('Datastore not found: %s' % (datastore_name))
        return True

    def validate_vm_folder_name(self):
        if self.vm_parameters['vcenter']['vm_folder'] is not None:
            folder_name = self.vm_parameters['vcenter']['vm_folder']
            if not self.vcenter_handler.is_vm_folder(folder_name):
                self.my_output.error('Folder not found: %s' % (folder_name))
                return False

            self.my_output.debug('Folder found: %s' % (folder_name))

        return True

    def validate_vcenter_parameters(self, location):
        self.my_output.debug('Validate vcenter section', underline=True, before_newline=True)

        self.vm_parameters['vcenter'] = {}
        for key in self.user_input['vcenter']:
            self.vm_parameters['vcenter'][key] = self.user_input['vcenter'][key]

        vcenter_filename = os.path.join(location, 'secret')
        vcenter_filename = os.path.join(vcenter_filename, 'vcenter.yaml')
        if not os.path.isfile(vcenter_filename):
            self.my_output.error('Specify valid vcenter credentials file: %s' % (vcenter_filename))
            return False

        vcenter_credentials = file_helper.get_file_yaml(vcenter_filename)
        if vcenter_credentials is None:
            self.my_output.error('Specify valid vcenter credentials file: %s' % (vcenter_filename))
            return False

        if 'username' not in vcenter_credentials or 'password' not in vcenter_credentials:
            self.my_output.error('Specify valid vcenter credentials file: %s' % (vcenter_filename))
            return False

        self.vm_parameters['vcenter']['username'] = vcenter_credentials['username']
        self.vm_parameters['vcenter']['password'] = vcenter_credentials['password']

        self.vcenter_handler = vcenter.Vcenter(
            self.vm_parameters['vcenter']['ip'],
            self.vm_parameters['vcenter']['username'],
            self.vm_parameters['vcenter']['password'],
            port=self.vm_parameters['vcenter']['port'],
            log_id=self.log_id
        )
        if not self.validate_datacenter_name():
            return False

        if not self.validate_datastore_name():
            return False

        if not self.validate_vm_folder_name():
            return False

        host_ips = self.vcenter_handler.get_host_ips()
        if host_ips is None:
            self.my_output.error('No host IP found in datacenter')
            return False

        self.my_output.debug('vcenter hosts: %s' % (','.join(host_ips)))
        self.vm_parameters['vcenter']['host_ips'] = host_ips
        self.my_output.debug('Completed')

        return True

    def validate_jump_parameters(self):
        '''
        Optional section in user input. Required if machine is Windows and KS template is used
        Then ISO needs to be generated and this code works on Linux only
        Jump is the optional definition of Linux-based machine

        jump:
            ip: <ip>
            username: ****
            password: ****

        if used, then all attributes required.

        SSH access check included unless syntax_only
        '''
        self.my_output.debug('Validate jump section', underline=True, before_newline=True)
        self.vm_parameters['jump'] = {}

        if 'jump' not in self.user_input:
            self.vm_parameters['jump']['enabled'] = False
            self.my_output.debug('Jump disabled')
            return True

        self.vm_parameters['jump']['enabled'] = True
        for key in ['ip', 'username', 'password']:
            self.vm_parameters['jump'][key] = self.user_input['jump'][key]

        ssh_handler = ssh.Ssh(
            self.vm_parameters['jump']['ip'],
            self.vm_parameters['jump']['username'],
            port=22,
            password=self.vm_parameters['jump']['password']
        )
        success = ssh_handler.is_ssh()
        if not success:
            self.my_output.error(
                'Jump access fails: %s@%s with %s' % (
                    self.vm_parameters['jump']['username'],
                    self.vm_parameters['jump']['ip'],
                    self.vm_parameters['jump']['password']
                )
            )
            return False

        self.my_output.debug('jump ssh access verified')
        self.my_output.debug('Completed')
        return True

    def validate_iso_parameters(self, check_source=True):
        self.my_output.debug('Validate linux.iso section', underline=True, before_newline=True)

        iso_section = self.user_input['linux']['iso']

        self.vm_parameters['iso'] = {}
        self.vm_parameters['iso']['enabled'] = True
        self.vm_parameters['iso']['source'] = iso_section['source']
        self.vm_parameters['iso']['delete_source'] = False
        self.vm_parameters['iso']['overwrite'] = False
        self.vm_parameters['iso']['delete_destination'] = False

        # destination syntax
        # - if linux.iso.filename contains '/' then it is considerd as full path name
        # - otherwise destination is based on vcenter.iso_folder and linux.iso.filename

        if '/' in iso_section['filename']:
            self.vm_parameters['iso']['folder_name'] = self.vc_helper_handler.get_parent_folder_name(
                iso_section['filename']
            )
            self.vm_parameters['iso']['file_name'] = iso_section['filename'].split('/')[-1]
            self.vm_parameters['iso']['destination'] = '%s%s' % (self.vm_parameters['iso']['folder_name'], self.vm_parameters['iso']['file_name'])
            self.my_output.debug('iso destination verified: %s' % (self.vm_parameters['iso']['destination']))
        else:
            self.vm_parameters['iso']['folder_name'] = self.vc_helper_handler.fixup_datastore_folder_name(
                self.vm_parameters['vcenter']['iso_folder']
            )
            self.vm_parameters['iso']['file_name'] = iso_section['filename']
            self.vm_parameters['iso']['destination'] = '%s%s' % (self.vm_parameters['iso']['folder_name'], self.vm_parameters['iso']['file_name'])
            self.my_output.debug('iso destination verified: %s' % (self.vm_parameters['iso']['destination']))

        # verify destination folder

        self.vm_parameters['iso']['is_folder'] = self.vcenter_handler.is_datastore_folder(
            self.user_input['vcenter']['datacenter'],
            self.user_input['vcenter']['datastore'],
            self.vm_parameters['iso']['folder_name']
        )
        if self.vm_parameters['iso']['is_folder']:
            self.my_output.debug('datastore folder found: %s' % (self.vm_parameters['iso']['folder_name']))
        else:
            self.my_output.debug('datastore folder not found: %s' % (self.vm_parameters['iso']['folder_name']))

        # verify destination file

        self.vm_parameters['iso']['is_file'] = False
        if self.vm_parameters['iso']['is_folder']:
            files = self.vcenter_handler.get_datastore_files(
                self.user_input['vcenter']['datacenter'],
                self.user_input['vcenter']['datastore'],
                self.vm_parameters['iso']['folder_name']
            )
            if files is not None:
                for file_info in files:
                    if file_info['filename'] == self.vm_parameters['iso']['file_name']:
                        self.vm_parameters['iso']['is_file'] = True
                        break

        if self.vm_parameters['iso']['is_file']:
            self.my_output.debug('datastore file found: %s' % (self.vm_parameters['iso']['file_name']))
        else:
            self.my_output.debug('datastore file not found: %s' % (self.vm_parameters['iso']['file_name']))

        if check_source:
            # Source verification
            # - source is optional if destination exists (is_file) and overwrite is False
            # - must be local filesystem name
            # - must be present
            if self.vm_parameters['iso']['is_file'] and not self.vm_parameters['iso']['overwrite']:
                if self.vm_parameters['iso']['source'] is not None:
                    self.my_output.debug('linux.iso.source attribute value is not checked as linux.iso.filename exists')
            else:
                if self.vm_parameters['iso']['source'] is None:
                    self.my_output.error('linux.iso.source attribute value required since linux.iso.destination does not exist')
                    return False

                if self.vm_parameters['iso']['source'].startswith('http'):
                    self.my_output.error('linux.iso.source attribute value must be local filename')
                    return False

                if not os.path.isfile(self.vm_parameters['iso']['source']):
                    self.my_output.error('linux.iso.source file not found: %s' % (self.vm_parameters['iso']['source']))
                    return False

                self.my_output.debug('iso source verified: %s' % (self.vm_parameters['iso']['source']))

        self.my_output.debug('Completed')

        return True

    def generate_variables(self):
        self.my_output.debug('Variables generation', underline=True, before_newline=True)

        self.vm_parameters['variables'] = {}

        # User defined variables

        if 'variables' in self.user_input:
            for name in self.user_input['variables']:
                self.vm_parameters['variables'][name] = self.user_input['variables'][name]

        # Proxy based variables

        if 'proxy' in self.user_input:
            self.vm_parameters['variables']['HTTP_PROXY_ENABLED'] = str(self.user_input['proxy']['enabled'])
            self.vm_parameters['variables']['HTTP_PROXY'] = self.user_input['proxy']['http']
            self.vm_parameters['variables']['HTTPS_PROXY'] = self.user_input['proxy']['https']
        else:
            self.vm_parameters['variables']['HTTP_PROXY_ENABLED'] = str(False)
            self.vm_parameters['variables']['HTTP_PROXY'] = 'undefined'
            self.vm_parameters['variables']['HTTPS_PROXY'] = 'undefined'

        # vcenter based variables

        vcenter_section = self.vm_parameters['vcenter']
        self.vm_parameters['variables']['VCENTER_NAME'] = vcenter_section['name']
        self.vm_parameters['variables']['VCENTER_IP'] = vcenter_section['ip']
        self.vm_parameters['variables']['VCENTER_PORT'] = vcenter_section['port']
        self.vm_parameters['variables']['VCENTER_USERNAME'] = vcenter_section['username']
        self.vm_parameters['variables']['VCENTER_PASSWORD'] = vcenter_section['password']
        self.vm_parameters['variables']['VCENTER_DATACENTER'] = vcenter_section['datacenter']
        self.vm_parameters['variables']['VCENTER_DATASTORE'] = vcenter_section['datastore']
        self.vm_parameters['variables']['VCENTER_CLUSTER'] = vcenter_section['cluster']
        self.vm_parameters['variables']['VCENTER_VM_FOLDER'] = vcenter_section['vm_folder']
        self.vm_parameters['variables']['VCENTER_ISO_FOLDER'] = vcenter_section['iso_folder']
        self.vm_parameters['variables']['VCENTER_KS_FOLDER'] = vcenter_section['ks_folder']
        self.vm_parameters['variables']['VCENTER_CLUSTER_HOST_IPS'] = ','.join(self.vm_parameters['vcenter']['host_ips'])
        self.vm_parameters['variables']['ISO_FILENAME'] = self.vm_parameters['iso']['destination']

        # Linux VM based variables

        linux_section = self.user_input['linux']
        self.vm_parameters['variables']['LINUX_DISTRIBUTION'] = linux_section['distribution']
        self.vm_parameters['variables']['LINUX_VERSION'] = linux_section['version']
        self.vm_parameters['variables']['VM_NAME'] = linux_section['vm']['name']
        self.vm_parameters['variables']['HOSTNAME'] = linux_section['vm']['name']
        self.vm_parameters['variables']['PASSWORD'] = linux_section['vm']['password']
        if self.vm_parameters['variables']['PASSWORD'] is not None:
            self.vm_parameters['variables']['ENCRYPTED_PASSWORD'] = bcrypt.hashpw(
                linux_section['vm']['password'].encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

        if linux_section['vm']['dns']['servers'] is not None:
            self.vm_parameters['variables']['DNS_NAMESERVER'] = linux_section['vm']['dns']['servers'].split(',')[0]
        if linux_section['vm']['dns']['domain'] is not None:
            self.vm_parameters['variables']['DNS_DOMAIN'] = linux_section['vm']['dns']['domain']

        if linux_section['vm']['ntp']['servers'] is not None:
            self.vm_parameters['variables']['NTP_SERVER'] = linux_section['vm']['ntp']['servers'].split(',')[0]

        if linux_section['vm']['ntp']['timezone'] is not None:
            self.vm_parameters['variables']['TIMEZONE'] = linux_section['vm']['ntp']['timezone']

        network_id = 0
        self.vm_parameters['variables']['INTERFACE_%s_VC_NETWORK_NAME' % (network_id)] = linux_section['vm']['interface']['network']
        self.vm_parameters['variables']['INTERFACE_%s_NAME' % (network_id)] = linux_section['vm']['interface']['device']
        if linux_section['vm']['ip'] is not None:
            self.vm_parameters['variables']['INTERFACE_%s_IP' % (network_id)] = linux_section['vm']['ip'].split('/')[0]
            self.vm_parameters['variables']['INTERFACE_%s_NETMASK' % (network_id)] = ip_helper.prefix_to_netmask(
                int(linux_section['vm']['ip'].split('/')[1])
            )
            self.vm_parameters['variables']['INTERFACE_%s_PREFIX' % (network_id)] = linux_section['vm']['ip'].split('/')[1]
            self.vm_parameters['variables']['INTERFACE_%s_CIDR' % (network_id)] = linux_section['vm']['ip']
            self.vm_parameters['variables']['INTERFACE_%s_NETWORK' % (network_id)] = ip_helper.get_network_ipv4_in_cidr(
                linux_section['vm']['ip']
            )
            self.vm_parameters['variables']['INTERFACE_%s_GATEWAY' % (network_id)] = linux_section['vm']['gateway']
            self.vm_parameters['variables']['INTERFACE_%s_REVDNS' % (network_id)] = '%s.%s.%s' % (
                self.vm_parameters['variables']['INTERFACE_%s_NETWORK' % (network_id)].split('.')[2],
                self.vm_parameters['variables']['INTERFACE_%s_NETWORK' % (network_id)].split('.')[1],
                self.vm_parameters['variables']['INTERFACE_%s_NETWORK' % (network_id)].split('.')[0]
            )

        # Non-user input related variables

        self.vm_parameters['variables']['DNS_SERIAL'] = '%s01' % (datetime.date.today().strftime("%Y%m%d"))

        # IP address octets variables

        new_attributes = {}
        for key in self.vm_parameters['variables']:
            if ip_helper.is_valid_ipv4_address(self.vm_parameters['variables'][key]):
                index = 1
                for octet in self.vm_parameters['variables'][key].split('.'):
                    new_attributes['%s_OCTET_%s' % (key, index)] = octet
                    index = index + 1

        for key in new_attributes:
            if key not in self.vm_parameters['variables']:
                self.vm_parameters['variables'][key] = new_attributes[key]

        for key in self.vm_parameters['variables']:
            self.my_output.debug(
                '%s => %s' % (
                    key,
                    self.vm_parameters['variables'][key]
                )
            )

        self.my_output.debug('Completed')
        return True

    def get_kickstart_default_filename(self):
        kickstart_filename = None

        if self.vm_parameters['variables']['LINUX_DISTRIBUTION'] in ['centos', 'fedora', 'rhel']:
            kickstart_filename = self.get_template_definition_key_value(
                self.vm_parameters['template_name'],
                'default_kickstart',
                template_category=self.template_category
            )

        if self.vm_parameters['variables']['LINUX_DISTRIBUTION'] in ['ubuntu']:
            if self.vm_parameters['variables']['HTTP_PROXY_ENABLED'] == 'True':
                kickstart_filename = self.get_template_definition_key_value(
                    self.vm_parameters['template_name'],
                    'default_user_data_proxy',
                    template_category=self.template_category
                )
            else:
                kickstart_filename = self.get_template_definition_key_value(
                    self.vm_parameters['template_name'],
                    'default_user_data_no_proxy',
                    template_category=self.template_category
                )

        if kickstart_filename is None:
            self.my_output.error('No default kickstart defined for template: %s' % (self.vm_parameters['template_name']))
            return None

        kickstart_path = self.get_template_filename(
            self.vm_parameters['template_name'],
            kickstart_filename,
            template_category=self.template_category
        )

        return kickstart_path

    def validate_ks_parameters(self, check_source=True):
        self.my_output.debug('Validate linux.ks section', underline=True, before_newline=True)
        ks_section = self.user_input['linux']['ks']

        self.vm_parameters['ks'] = {}
        self.vm_parameters['ks']['enabled'] = ks_section['enabled']

        # Auto-fix ks.enabled in case ks.template or ks.iso is defined
        if ks_section['template'] is not None or ks_section['iso'] is not None:
            self.vm_parameters['ks']['enabled'] = True

        # ks.template and ks.iso cannot be used at the same time
        if ks_section['template'] is not None and ks_section['iso'] is not None:
            self.my_output.error('Define linux.ks.template or linux.ks.source')
            return False

        # if ks is disabled, exit early
        if not self.vm_parameters['ks']['enabled']:
            self.my_output.debug('Kickstart disabled')
            return True

        # Kickstart destination related parameters

        self.vm_parameters['ks']['folder_name'] = self.vc_helper_handler.fixup_datastore_folder_name(
            self.vm_parameters['vcenter']['ks_folder']
        )
        self.vm_parameters['ks']['file_name'] = '%s-ks.iso' % (
            self.vm_parameters['variables']['VM_NAME']
        )
        self.vm_parameters['ks']['destination'] = '%s%s' % (
            self.vm_parameters['ks']['folder_name'],
            self.vm_parameters['ks']['file_name']
        )
        self.vm_parameters['ks']['overwrite'] = True
        self.vm_parameters['ks']['delete_destination'] = True

        self.vm_parameters['variables']['KS_FILENAME'] = self.vm_parameters['ks']['destination']

        # Check destination folder

        success = self.vcenter_handler.is_datastore_folder(
            self.vm_parameters['vcenter']['datacenter'],
            self.vm_parameters['vcenter']['datastore'],
            self.vm_parameters['ks']['folder_name']
        )
        if success:
            self.my_output.debug('datastore folder found: %s' % (self.vm_parameters['ks']['folder_name']))
            self.vm_parameters['ks']['is_folder'] = True
        else:
            self.my_output.debug('datastore folder not found: %s' % (self.vm_parameters['ks']['folder_name']))
            self.vm_parameters['ks']['is_folder'] = False

        # Check destination file

        success = self.vcenter_handler.is_datastore_file(
            self.vm_parameters['vcenter']['datacenter'],
            self.vm_parameters['vcenter']['datastore'],
            self.vm_parameters['ks']['folder_name'],
            self.vm_parameters['ks']['file_name']
        )
        if success:
            self.vm_parameters['ks']['is_file'] = True
            self.my_output.debug('kickstart iso file already defined: %s' % (self.vm_parameters['ks']['destination']))
        else:
            self.vm_parameters['ks']['is_file'] = False
            self.my_output.debug('datastore file not found: %s' % (self.vm_parameters['ks']['destination']))

        # check_source code runs for create operation
        # delete operation only cares about kickstart location that is based on vcenter.ks_folder and linux.vm.name
        if check_source:

            # Option: ks.iso defined (only for centos/fedora/rhel)
            if ks_section['iso'] is not None:
                self.vm_parameters['ks']['generate'] = False
                self.vm_parameters['ks']['template'] = None
                self.vm_parameters['ks']['delete_source'] = False

                # ks.iso can be relative or absolute path
                self.vm_parameters['ks']['source'] = ks_section['iso']
                if not os.path.isabs(ks_section['iso']):
                    self.vm_parameters['ks']['source'] = os.path.join(
                        self.user_input['base_directory'],
                        ks_section['iso']
                    )

                # ks.iso must exist
                if not os.path.isfile(self.vm_parameters['ks']['source']):
                    self.my_output.error(
                        'linux.ks.iso must be valid kickstart iso file location: %s' %
                        (self.vm_parameters['ks']['source'])
                    )
                    return False

            if ks_section['iso'] is None:
                # Option: ks.template is not defined and default template should be used
                if ks_section['template'] is None:
                    self.vm_parameters['ks']['generate'] = True

                    self.vm_parameters['ks']['template'] = self.get_kickstart_default_filename()
                    if self.vm_parameters['ks']['template'] is None:
                        return False

                # Option: ks.template is defined
                if ks_section['template'] is not None:
                    self.vm_parameters['ks']['generate'] = True
                    self.vm_parameters['ks']['source'] = '/tmp/%s.iso' % (str(uuid.uuid4()))
                    self.vm_parameters['ks']['delete_source'] = True

                    # ks.template can be relative or absolute path
                    self.vm_parameters['ks']['template'] = ks_section['template']
                    if not os.path.isabs(ks_section['template']):
                        self.vm_parameters['ks']['template'] = os.path.join(
                            self.user_input['base_directory'],
                            ks_section['template']
                        )

                # ks.template must exist
                if not os.path.isfile(self.vm_parameters['ks']['template']):
                    self.my_output.error('linux.ks.template file not found: %s' % (self.vm_parameters['ks']['template']))
                    return False

                # check template content with conditional variable replacement
                content = self.template_handler.get_template(
                    self.vm_parameters['ks']['template'],
                    self.vm_parameters['variables'],
                    replace_variables_enabled=self.vm_parameters['settings']['kickstart_template_variable_replacement_enabled']
                )
                if content is None:
                    return False

                self.vm_parameters['ks']['delete_source'] = True
                self.vm_parameters['ks']['source'] = '/tmp/%s.iso' % (str(uuid.uuid4()))

                self.my_output.debug('Kickstart template verified: %s' % (self.vm_parameters['ks']['template']))
                self.my_output.debug('Generated kickstart iso target location: %s' % (self.vm_parameters['ks']['source']))

        self.my_output.debug('Completed')
        return True

    def validate_vm_get_parameters(self):
        self.my_output.debug('Validate linux vm section', underline=True, before_newline=True)

        linux_section = self.user_input['linux']

        self.vm_parameters['vm'] = {}
        self.vm_parameters['vm']['distribution'] = linux_section['distribution']
        self.vm_parameters['vm']['datacenter_name'] = self.vm_parameters['vcenter']['datacenter']
        self.vm_parameters['vm']['datastore_name'] = self.vm_parameters['vcenter']['datastore']
        self.vm_parameters['vm']['host_ip'] = self.vm_parameters['vcenter']['host_ip']
        self.vm_parameters['vm']['name'] = linux_section['vm']['name']

        self.vm_parameters['vm']['management_ip'] = None
        self.vm_parameters['vm']['ssh'] = {}
        self.vm_parameters['vm']['ssh']['enabled'] = False
        self.vm_parameters['vm']['ssh']['username'] = None
        self.vm_parameters['vm']['ssh']['password'] = None
        self.vm_parameters['vm']['ssh']['ip'] = None

        if linux_section['vm']['username'] is not None:
            self.vm_parameters['vm']['ssh']['username'] = linux_section['vm']['username']
        if linux_section['vm']['password'] is not None:
            self.vm_parameters['vm']['ssh']['password'] = linux_section['vm']['password']
        if linux_section['vm']['ip'] is not None:
            self.vm_parameters['vm']['ssh']['ip'] = linux_section['vm']['ip'].split('/')[0]
            self.vm_parameters['vm']['management_ip'] = linux_section['vm']['ip'].split('/')[0]

        if self.vm_parameters['vm']['ssh']['username'] is not None:
            if self.vm_parameters['vm']['ssh']['password'] is not None:
                if self.vm_parameters['vm']['ssh']['ip'] is not None:
                    self.vm_parameters['vm']['ssh']['enabled'] = True

        self.my_output.debug('Completed')
        return True

    def validate_vm_create_parameters(self):
        self.my_output.debug('Validate linux vm section', underline=True, before_newline=True)

        kickstart = self.vm_parameters['ks']
        linux_section = self.user_input['linux']

        self.vm_parameters['vm'] = {}
        self.vm_parameters['vm']['distribution'] = linux_section['distribution']
        self.vm_parameters['vm']['datacenter_name'] = self.vm_parameters['vcenter']['datacenter']
        self.vm_parameters['vm']['datastore_name'] = self.vm_parameters['vcenter']['datastore']
        self.vm_parameters['vm']['host_ip'] = self.vm_parameters['vcenter']['host_ip']

        for key in ['name', 'cpu', 'memory']:
            self.vm_parameters['vm'][key] = linux_section['vm'][key]

        self.vm_parameters['vm']['disk'] = []
        new_disk = {}
        new_disk['size'] = linux_section['vm']['disk']['size']
        new_disk['thin'] = False
        if linux_section['vm']['disk']['type'] == 'thin':
            new_disk['thin'] = True
        self.vm_parameters['vm']['disk'].append(new_disk)

        self.vm_parameters['vm']['network'] = []
        new_network = {}
        new_network['device'] = linux_section['vm']['interface']['device']
        new_network['name'] = linux_section['vm']['interface']['network']
        new_network['type'] = linux_section['vm']['interface']['type']
        self.vm_parameters['vm']['network'].append(new_network)

        self.vm_parameters['vm']['cdrom'] = []

        if self.vm_parameters['iso']['enabled']:
            if linux_section['distribution'] in ['centos', 'fedora', 'rhel']:
                new_cdrom = {}
                new_cdrom['datastore_name'] = self.vm_parameters['vcenter']['datastore']
                new_cdrom['iso'] = self.vm_parameters['iso']['destination']
                self.vm_parameters['vm']['cdrom'].append(new_cdrom)

            if linux_section['distribution'] in ['ubuntu'] and not kickstart['enabled']:
                new_cdrom = {}
                new_cdrom['datastore_name'] = self.vm_parameters['vcenter']['datastore']
                new_cdrom['iso'] = self.vm_parameters['iso']['destination']
                self.vm_parameters['vm']['cdrom'].append(new_cdrom)

        if kickstart['enabled']:
            new_cdrom = {}
            new_cdrom['datastore_name'] = self.vm_parameters['vcenter']['datastore']
            new_cdrom['iso'] = kickstart['destination']
            self.vm_parameters['vm']['cdrom'].append(new_cdrom)

        self.vm_parameters['vm']['created'] = self.vcenter_handler.is_vm(linux_section['vm']['name'])
        if not self.vm_parameters['vm']['created']:
            if kickstart['enabled'] and kickstart['is_file']:
                self.my_output.error('Kickstart file already defined: %s' % (kickstart['destination']))
                return None

        net_obj = self.vcenter_handler.get_network_object(linux_section['vm']['interface']['network'])
        if net_obj is None:
            self.my_output.error('Network %s not found' % (linux_section['vm']['interface']['network']))
            return None

        self.vm_parameters['vm']['management_ip'] = None
        self.vm_parameters['vm']['ssh'] = {}
        self.vm_parameters['vm']['ssh']['enabled'] = False
        self.vm_parameters['vm']['ssh']['username'] = None
        self.vm_parameters['vm']['ssh']['password'] = None
        self.vm_parameters['vm']['ssh']['ip'] = None

        if linux_section['vm']['username'] is not None:
            self.vm_parameters['vm']['ssh']['username'] = linux_section['vm']['username']
        if linux_section['vm']['password'] is not None:
            self.vm_parameters['vm']['ssh']['password'] = linux_section['vm']['password']
        if linux_section['vm']['ip'] is not None:
            self.vm_parameters['vm']['ssh']['ip'] = linux_section['vm']['ip'].split('/')[0]
            self.vm_parameters['vm']['management_ip'] = linux_section['vm']['ip'].split('/')[0]

        if self.vm_parameters['vm']['ssh']['username'] is not None:
            if self.vm_parameters['vm']['ssh']['password'] is not None:
                if self.vm_parameters['vm']['ssh']['ip'] is not None:
                    self.vm_parameters['vm']['ssh']['enabled'] = True

        self.my_output.debug('Completed')
        return True

    def validate_vm_delete_parameters(self):
        self.my_output.debug('Validate linux vm section', underline=True, before_newline=True)

        linux_section = self.user_input['linux']

        self.vm_parameters['vm'] = {}
        self.vm_parameters['vm']['distribution'] = linux_section['distribution']
        self.vm_parameters['vm']['datacenter_name'] = self.vm_parameters['vcenter']['datacenter']
        self.vm_parameters['vm']['datastore_name'] = self.vm_parameters['vcenter']['datastore']
        self.vm_parameters['vm']['host_ip'] = self.vm_parameters['vcenter']['host_ip']
        self.vm_parameters['vm']['name'] = linux_section['vm']['name']

        self.vm_parameters['vm']['management_ip'] = None
        self.vm_parameters['vm']['ssh'] = {}
        self.vm_parameters['vm']['ssh']['enabled'] = False
        self.vm_parameters['vm']['ssh']['username'] = None
        self.vm_parameters['vm']['ssh']['password'] = None
        self.vm_parameters['vm']['ssh']['ip'] = None

        if linux_section['vm']['username'] is not None:
            self.vm_parameters['vm']['ssh']['username'] = linux_section['vm']['username']
        if linux_section['vm']['password'] is not None:
            self.vm_parameters['vm']['ssh']['password'] = linux_section['vm']['password']
        if linux_section['vm']['ip'] is not None:
            self.vm_parameters['vm']['ssh']['ip'] = linux_section['vm']['ip'].split('/')[0]
            self.vm_parameters['vm']['management_ip'] = linux_section['vm']['ip'].split('/')[0]

        if self.vm_parameters['vm']['ssh']['username'] is not None:
            if self.vm_parameters['vm']['ssh']['password'] is not None:
                if self.vm_parameters['vm']['ssh']['ip'] is not None:
                    self.vm_parameters['vm']['ssh']['enabled'] = True

        self.my_output.debug('Completed')
        return True

    def load_task(self, filename):
        content = self.template_handler.get_template(
            filename,
            self.vm_parameters['variables'],
            yaml_conversion=True
        )

        if content is None:
            return None

        return content

    def validate_task(self, task_filename):
        task_definition = self.load_task(task_filename)
        if task_definition is None:
            return False

        if 'tasks' not in task_definition:
            self.my_output.error('tasks list required')
            return False

        task_directory = os.path.dirname(task_filename)
        for task in task_definition['tasks']:
            for key in task:
                if key not in ['scripts', 'files', 'commands']:
                    self.my_output.error('Unsupported task key: %s' % (key))
                    return False

                if key == 'scripts':
                    for item in task[key]:
                        filename = os.path.join(task_directory, item)
                        self.my_output.debug('\nScript: %s' % (filename))

                        content = self.template_handler.get_template(filename, self.vm_parameters['variables'])
                        if content is None:
                            return False

                        self.my_output.debug('Verified')
                        self.my_output.debug(content)

                if key == 'files':
                    for item in task[key]:
                        for attribute in ['source', 'template', 'destination', 'chmod']:
                            if attribute not in item:
                                self.my_output.error('File requires attribute %s' % (attribute))
                                return False

                        if '/' in item['source'] or '\\' in item['source']:
                            filename = item['source']
                        else:
                            filename = os.path.join(task_directory, item['source'])
                        self.my_output.debug('\nFile: %s' % (filename))

                        if item['template']:
                            content = self.template_handler.get_template(filename, self.vm_parameters['variables'])
                            if content is None:
                                return False
                            self.my_output.debug(content)

                        self.my_output.debug('Verifed')

        return True

    def validate_tasks(self, task_type):
        self.vm_parameters['tasks'] = []
        if task_type in self.user_input:
            for task_filename in self.user_input[task_type]:
                self.my_output.debug('Validate task: %s' % (task_filename), underline=True, before_newline=True)
                if not self.validate_task(task_filename):
                    return False
                self.vm_parameters['tasks'].append(task_filename)

        return True

    def validate_get(self, location):
        if not self.validate_syntax(location, 'get'):
            return None

        if not self.validate_vcenter_parameters(location):
            return None

        if not self.validate_vm_get_parameters():
            return None

        self.vm_parameters['state'] = {}
        for key in self.user_input['state']:
            self.vm_parameters['state'][key] = self.user_input['state'][key]

        self.my_output.debug('\nValidated vm get parameters: %s' % (json.dumps(self.vm_parameters, indent=4)))
        return self.vm_parameters

    def validate_syntax(self, location, operation):
        self.log_handler.debug('validate_syntax', 'Operation: %s, Location: %s' % (operation, location))
        self.user_input = self.validate(
            location,
            operation,
            template_reference='linux.template',
            template_category=self.template_category
        )
        if self.user_input is None:
            self.log_handler.error('validate_syntax', 'Validation failed')
            return False

        self.log_handler.debug('validate_syntax', 'self.user_input: %s' % (json.dumps(self.user_input, indent=4)))

        self.vm_parameters['template_name'] = self.user_input['template_name']
        self.log_handler.debug('validate_syntax', 'self.vm_parameters: %s' % (json.dumps(self.vm_parameters, indent=4)))

        return True

    def validate_create(self, location):
        self.log_handler.debug('validate_create', location)
        if not self.validate_syntax(location, 'create'):
            return None

        if not self.validate_settings():
            return None

        if not self.validate_vcenter_parameters(location):
            return None

        if not self.validate_jump_parameters():
            return None

        if not self.validate_iso_parameters(check_source=True):
            return None

        if not self.generate_variables():
            return None

        if not self.validate_ks_parameters(check_source=True):
            return None

        if not self.validate_vm_create_parameters():
            return None

        if not self.validate_tasks('create_tasks'):
            return None

        self.vm_parameters['state'] = {}
        for key in self.user_input['state']:
            self.vm_parameters['state'][key] = self.user_input['state'][key]

        self.my_output.debug('\nValidated vm create parameters: %s' % (json.dumps(self.vm_parameters, indent=4)))
        return self.vm_parameters

    def validate_delete(self, location):
        if not self.validate_syntax(location, 'delete'):
            return None

        if not self.validate_vcenter_parameters(location):
            return None

        if not self.validate_iso_parameters(check_source=False):
            return None

        if not self.generate_variables():
            return None

        if not self.validate_ks_parameters(check_source=False):
            return None

        if not self.validate_vm_delete_parameters():
            return None

        if not self.validate_tasks('delete_tasks'):
            return None

        self.my_output.debug('\nValidated vm delete parameters: %s' % (json.dumps(self.vm_parameters, indent=4)))
        return self.vm_parameters
