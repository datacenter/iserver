import json
import platform

from lib import ssh
from lib import ip_helper


class OcpVsphereIpiValidate():
    def __init__(self):
        self.local_system_type = platform.system()

    def validate_vsphere_ipi_create_user_input(self):
        mandatory_sections = ['vcenter', 'ocp', 'sources', 'installer', 'dns', 'dhcp', 'cni', 'post', 'pre', 'addons', 'calico', 'cilium']
        if self.local_system_type != 'Linux':
            mandatory_sections.append('jump')

        optional_sections = ['ssh', 'proxy', 'bgp']
        if self.local_system_type == 'Linux':
            optional_sections.append('jump')

        ocp_parameters = self.validate_sections(
            mandatory_sections,
            optional_sections
        )
        if ocp_parameters is None:
            return None

        # vcenter

        vcenter_definition = ocp_parameters['vcenter']
        vcenter_definition['username'] = self.vcenter_credentials['username']
        vcenter_definition['password'] = self.vcenter_credentials['password']

        vcenter_definition = self.validate_vcenter(
            vcenter_definition
        )
        if vcenter_definition is None:
            return None

        # jump

        if 'jump' in ocp_parameters:
            self.my_output.info('Validate jump section', underline=True, before_newline=True)

            ssh_handler = ssh.Ssh(
                ocp_parameters['jump']['ip'],
                ocp_parameters['jump']['username'],
                password=ocp_parameters['jump']['password'],
                log_id=self.log_id
            )
            if not ssh_handler.is_ssh():
                self.my_output.error('Jump ssh access fails')
                return None

            self.my_output.info('SSH access works')
            self.my_output.info('Completed')

        # installer

        self.my_output.info('Validate installer section', underline=True, before_newline=True)

        self.my_output.info('Check IP and gateway')
        if not ip_helper.is_ipv4_in_cidr(ocp_parameters['installer']['vm']['ip'], ocp_parameters['dhcp']['subnet']):
            self.my_output.error('Installer IP must be in DHCP subnet')
            return None
        self.my_output.info('Completed')

        # dhcp

        self.my_output.info('Validate dhcp section', underline=True, before_newline=True)

        self.my_output.info('Check subnet and gateway')
        if not ip_helper.is_ipv4_in_cidr(ocp_parameters['dhcp']['gateway'], ocp_parameters['dhcp']['subnet']):
            self.my_output.error('DHCP gateway must be in ip subnet')
            return None

        self.my_output.info('Completed')

        # ocp

        self.my_output.info('Validate ocp section', underline=True, before_newline=True)

        self.my_output.info('Cross-check API VIP and DHCP subnet')
        if not ip_helper.is_ipv4_in_cidr(ocp_parameters['ocp']['cluster']['api_vip'], ocp_parameters['dhcp']['subnet']):
            self.my_output.error('API VIP must be part of DHCP subnet')
            return None

        self.my_output.info('Cross-check ingress VIP and DHCP subnet')
        if not ip_helper.is_ipv4_in_cidr(ocp_parameters['ocp']['cluster']['ingress_vip'], ocp_parameters['dhcp']['subnet']):
            self.my_output.error('API VIP must be part of DHCP subnet')
            return None

        self.my_output.info('Check API VIP and Ingress VIP uniqueness')
        if ocp_parameters['ocp']['cluster']['ingress_vip'] == ocp_parameters['ocp']['cluster']['api_vip']:
            self.my_output.error('API and Ingress VIP must be different')
            return None

        # sources and version

        self.my_output.info('Validate ocp source', underline=True, before_newline=True)

        if ocp_parameters['ocp']['source'] == 'local':
            self.my_output.info('Local source files expected')
            if ocp_parameters['sources']['ocp'] is None:
                self.my_output.error('ocp installation tarball not defined')
                return None

            if ocp_parameters['sources']['ocp'] is None:
                self.my_output.error('oc binary tarball not defined')
                return None

        if ocp_parameters['ocp']['source'] == 'web':
            self.my_output.info('Installation binaries will be downloaded')
            if ocp_parameters['ocp']['release'] is None:
                self.my_output.error('Define ocp.release value for installation binaries download')
                return None

            ocp_parameters['sources']['ocp'] = '%s/%s/openshift-install-linux.tar.gz' % (
                ocp_parameters['sources']['ocp_base_url'],
                ocp_parameters['ocp']['release']
            )
            if not ip_helper.is_url_accessible(ocp_parameters['sources']['ocp']):
                self.my_output.error('Openshift installation binary not found: %s' % (ocp_parameters['sources']['ocp']))
                return None

            ocp_parameters['sources']['oc'] = '%s/%s/openshift-client-linux.tar.gz' % (
                ocp_parameters['sources']['ocp_base_url'],
                ocp_parameters['ocp']['release']
            )
            if not ip_helper.is_url_accessible(ocp_parameters['sources']['oc']):
                self.my_output.error('Openshift client binary not found: %s' % (ocp_parameters['sources']['oc']))
                return None

        ocp_parameters['sources']['secret'] = self.ocp_token_filename

        self.my_output.info('Completed')

        # all good !

        self.my_output.info('User input validated and augmented with generated data')

        return ocp_parameters

    def validate_vsphere_ipi_delete_user_input(self):
        mandatory_sections = ['vcenter', 'ocp', 'sources', 'installer', 'dns', 'dhcp', 'cni', 'post', 'pre', 'addons', 'calico', 'cilium']
        if self.local_system_type != 'Linux':
            mandatory_sections.append('jump')

        optional_sections = ['ssh', 'proxy', 'bgp']
        if self.local_system_type == 'Linux':
            optional_sections.append('jump')

        ocp_parameters = self.validate_sections(
            mandatory_sections,
            optional_sections
        )
        if ocp_parameters is None:
            return None

        # vcenter

        vcenter_definition = ocp_parameters['vcenter']
        vcenter_definition['username'] = self.vcenter_credentials['username']
        vcenter_definition['password'] = self.vcenter_credentials['password']

        vcenter_definition = self.validate_vcenter(
            vcenter_definition
        )
        if vcenter_definition is None:
            return None

        self.my_output.info('Validated user input: %s' % (json.dumps(ocp_parameters, indent=4)))

        return ocp_parameters
