import json
import uuid
import datetime

from lib import ip_helper


class OcpVsphereIpiInstaller():
    def __init__(self):
        pass

    def get_vshpere_ipi_installer_iso(self):
        '''
        "iso": {
            "enabled": true,
            "destination": "/linux-iso/Fedora-Server-dvd-x86_64-36-1.5.iso",
            "delete_source": false,
            "source": null,
            "overwrite": false,
            "delete_destination": false,
            "folder_name": "/linux-iso/",
            "file_name": "Fedora-Server-dvd-x86_64-36-1.5.iso",
            "is_folder": true,
            "is_file": true
        },
        '''

        iso = {}
        iso['enabled'] = True
        iso['source'] = self.ocp_parameters['installer']['iso']['source']
        iso['destination'] = self.ocp_parameters['installer']['iso']['destination']
        iso['delete_source'] = False
        iso['overwrite'] = False
        iso['delete_destination'] = False

        iso_destination = iso['destination'].rstrip('/')
        iso['folder_name'] = self.vcenter_handler.get_parent_folder_name(iso_destination)
        iso['file_name'] = iso_destination.split('/')[-1]
        iso['destination'] = '%s%s' % (iso['folder_name'], iso['file_name'])
        self.my_output.info('iso destination verified: %s' % (iso['destination']))

        if not self.vcenter_handler.is_datastore_folder(self.ocp_parameters['vcenter']['datacenter'], self.ocp_parameters['vcenter']['datastore'], iso['folder_name']):
            self.my_output.info('datastore folder not found: %s' % (iso['folder_name']))
            iso['is_folder'] = False
        else:
            self.my_output.info('datastore folder found: %s' % (iso['folder_name']))
            iso['is_folder'] = True

        iso['is_file'] = False
        if iso['is_folder']:
            files = self.vcenter_handler.get_datastore_files(self.ocp_parameters['vcenter']['datacenter'], self.ocp_parameters['vcenter']['datastore'], iso['folder_name'])
            if files is not None:
                for file_info in files:
                    if file_info['filename'] == iso['file_name']:
                        iso['is_file'] = True
                        break

        if iso['is_file']:
            self.my_output.info('datastore file found: %s' % (iso['file_name']))
        else:
            self.my_output.info('datastore file not found: %s' % (iso['file_name']))

        return iso

    def get_vsphere_ipi_installer_variables(self, attributes={}):
        '''
        Files e.g. kickstart or task related, can have ${VARIABLE} that will be replaced with parameters from user input (yaml)

        System generated variables

        User-defined variables - globally in 'variables' section

        Indirectly defined variables based on vm section:

        HOSTNAME - vm.settings.hostname
        PASSWORD - vm.settings.password
        DNS_NAMESERVER - the first item in the list vm.settings.dns.nameservers
        DNS_DOMAIN - vm.settings.dns.domain
        NTP_SERVER - the first item in the list vm.settings.ntp.servers
        TIMEZONE - vm.settings.ntp.timezone
        INTERFACE_n_IP - vm.network[n].ip
        INTERFACE_n_NETMASK - vm.network[n].netmask
        INTERFACE_n_GATEWAY - vm.network[n].gateway
        INTERFACE_n_NETWORK - network of vm.network[n].ip
        INTERFACE_n_PREFIX - prefix length based on netmask
        INTERFACE_n_CIDR - IP/Prefix
        INTERFACE_n_NAME - vm.network[n].interface - Linux OS specific name of interface
        INTERFACE_n_REVDNS - reverse DNS style representatin of the INTERFACE_n_NETWORK

        Every variable associated with IPv4 address value will trigger generated variables
        <var_name>_OCTET_<n>

        vcenter section based parameters

        VCENTER_NAME - vcenter.name
        VCENTER_IP - vcenter.ip
        VCENTER_PORT - vcenter.port
        VCENTER_USERNAME - vcenter.username
        VCENTER_PASSWORD - vcenter.password
        VCENTER_DATACENTER - vcenter.datacenter
        VCENTER_DATASTORE - vcenter.datastore
        VCENTER_CLUSTER - vcenter.cluster
        VCENTER_FOLDER - vcenter.folder
        VCENTER_NETWORK - vcenter.network
        '''
        self.my_output.info('Variables generation', underline=True, before_newline=True)

        # User input related

        vcenter_section = self.ocp_parameters['vcenter']
        installer_section = self.ocp_parameters['installer']
        installer_vm_section = self.ocp_parameters['installer']['vm']
        dhcp_section = self.ocp_parameters['dhcp']

        attributes = {}
        attributes['VCENTER_NAME'] = vcenter_section['name']
        attributes['VCENTER_IP'] = vcenter_section['ip']
        attributes['VCENTER_PORT'] = vcenter_section['port']
        attributes['VCENTER_USERNAME'] = vcenter_section['username']
        attributes['VCENTER_PASSWORD'] = vcenter_section['password']
        attributes['VCENTER_DATACENTER'] = vcenter_section['datacenter']
        attributes['VCENTER_DATASTORE'] = vcenter_section['datastore']
        attributes['VCENTER_CLUSTER'] = vcenter_section['cluster']
        attributes['VCENTER_FOLDER'] = vcenter_section['folder']
        attributes['VCENTER_CLUSTER_HOST_IPS'] = ','.join(vcenter_section['host_ips'])
        attributes['VCENTER_NETWORK'] = vcenter_section['network']

        attributes['HOSTNAME'] = installer_vm_section['name']
        attributes['PASSWORD'] = installer_vm_section['password']

        attributes['DNS_NAMESERVER'] = dhcp_section['dns']['servers'].split(',')[0]
        attributes['DNS_DOMAIN'] = dhcp_section['dns']['domain']
        attributes['NTP_SERVER'] = dhcp_section['ntp']['servers'].split(',')[0]
        attributes['TIMEZONE'] = dhcp_section['ntp']['timezone']

        network_id = 0
        attributes['INTERFACE_%s_VC_NETWORK_NAME' % (network_id)] = vcenter_section['network']
        attributes['INTERFACE_%s_IP' % (network_id)] = installer_vm_section['ip']
        attributes['INTERFACE_%s_NETMASK' % (network_id)] = ip_helper.prefix_to_netmask(
            int(dhcp_section['subnet'].split('/')[1])
        )
        attributes['INTERFACE_%s_PREFIX' % (network_id)] = dhcp_section['subnet'].split('/')[1]
        attributes['INTERFACE_%s_CIDR' % (network_id)] = '%s/%s' % (
            installer_vm_section['ip'],
            dhcp_section['subnet'].split('/')[1]
        )
        attributes['INTERFACE_%s_NETWORK' % (network_id)] = ip_helper.get_network_ipv4_in_cidr(
            attributes['INTERFACE_%s_CIDR' % (network_id)]
        )
        attributes['INTERFACE_%s_GATEWAY' % (network_id)] = dhcp_section['gateway']
        attributes['INTERFACE_%s_NAME' % (network_id)] = installer_vm_section['interface']['name']
        attributes['INTERFACE_%s_REVDNS' % (network_id)] = '%s.%s.%s' % (
            attributes['INTERFACE_%s_NETWORK' % (network_id)].split('.')[2],
            attributes['INTERFACE_%s_NETWORK' % (network_id)].split('.')[1],
            attributes['INTERFACE_%s_NETWORK' % (network_id)].split('.')[0]
        )

        # Proxy

        attributes['HTTP_PROXY_ENABLED'] = 'False'
        attributes['HTTP_PROXY'] = 'undefined'
        attributes['HTTPS_PROXY'] = 'undefined'
        attributes['USER_NO_PROXY'] = 'undefined'

        if 'proxy' in self.ocp_parameters:
            if self.ocp_parameters['proxy']['enabled']:
                attributes['HTTP_PROXY_ENABLED'] = "True"
                attributes['HTTP_PROXY'] = self.ocp_parameters['proxy']['http']
                attributes['HTTPS_PROXY'] = self.ocp_parameters['proxy']['https']
                if self.ocp_parameters['proxy']['no_proxy'] is None:
                    attributes['USER_NO_PROXY'] = ''
                else:
                    attributes['USER_NO_PROXY'] = '%s,' % (self.ocp_parameters['proxy']['no_proxy'])

        # DHCP

        attributes['MANAGED_DHCP_ENABLED'] = "False"
        if 'dhcp' in self.ocp_parameters:
            if self.ocp_parameters['dhcp']['managed']:
                attributes['MANAGED_DHCP_ENABLED'] = "True"

        # Named

        attributes['MANAGED_DNS_ENABLED'] = "False"
        if 'dns' in self.ocp_parameters:
            if self.ocp_parameters['dns']['managed']:
                attributes['MANAGED_DNS_ENABLED'] = "True"

        # OCP

        attributes['OCP_BASE_DOMAIN'] = self.ocp_parameters['ocp']['cluster']['domain']
        attributes['OCP_NAME'] = self.ocp_parameters['ocp']['cluster']['name']
        attributes['OCP_API_VIP'] = self.ocp_parameters['ocp']['cluster']['api_vip']
        attributes['OCP_INGRESS_VIP'] = self.ocp_parameters['ocp']['cluster']['ingress_vip']
        attributes['OCP_NODES_DHCP_START'] = self.ocp_parameters['dhcp']['range'].split('-')[0]
        attributes['OCP_NODES_DHCP_END'] = self.ocp_parameters['dhcp']['range'].split('-')[1]
        attributes['OCP_NODES_IPS'] = ','.join(
            ip_helper.get_ipv4_addresses_in_range(
                attributes['OCP_NODES_DHCP_START'],
                attributes['OCP_NODES_DHCP_END']
            )
        )
        attributes['OCP_MASTER_COUNT'] = str(self.ocp_parameters['ocp']['cluster']['master']['replicas'])
        attributes['OCP_WORKER_COUNT'] = str(self.ocp_parameters['ocp']['cluster']['worker']['replicas'])

        if vcenter_section['folder'] is None:
            attributes['OCP_CONFIG_FOLDER'] = ''
        else:
            attributes['OCP_CONFIG_FOLDER'] = '/%s/vm/%s' % (
                vcenter_section['datacenter'],
                vcenter_section['folder']
            )

        # CNI

        attributes['CNI_TYPE'] = self.ocp_parameters['cni']['type']
        if attributes['CNI_TYPE'] == 'Calico':
            attributes['CALICO_VERSION'] = self.ocp_parameters['calico']['version']

        if attributes['CNI_TYPE'] == 'Cilium':
            attributes['CILIUM_VERSION'] = self.ocp_parameters['cilium']['version']

        attributes['CNI_SERVICE_V4'] = self.ocp_parameters['cni']['v4serviceNetwork']
        attributes['CNI_POD_V4'] = self.ocp_parameters['cni']['v4cidr']
        attributes['CNI_HOST_PREFIX'] = str(self.ocp_parameters['cni']['v4hostPrefix'])

        # Calico BGP

        if 'bgp' in self.ocp_parameters:
            attributes['BGP_LOCAL_AS'] = str(self.ocp_parameters['bgp']['local_as'])
            if self.ocp_parameters['bgp']['mesh']:
                attributes['BGP_MESH'] = 'true'
            else:
                attributes['BGP_MESH'] = 'false'

            attributes['BGP_ADVERTISEMENTS'] = ''
            if 'external_ips' in self.ocp_parameters['bgp'] and self.ocp_parameters['bgp']['external_ips'] is not None and len(self.ocp_parameters['bgp']['external_ips']) > 0:
                attributes['BGP_ADVERTISEMENTS'] = '  serviceExternalIPs:\n'
                is_community = False
                for external_ip in self.ocp_parameters['bgp']['external_ips']:
                    if len(external_ip.split(',')) > 1:
                        is_community = True
                        attributes['BGP_ADVERTISEMENTS'] = '%s  - cidr: %s\n' % (
                            attributes['BGP_ADVERTISEMENTS'],
                            external_ip.split(',')[0]
                        )
                    else:
                        attributes['BGP_ADVERTISEMENTS'] = '%s  - cidr: %s\n' % (
                            attributes['BGP_ADVERTISEMENTS'],
                            external_ip
                        )

                if is_community:
                    attributes['BGP_ADVERTISEMENTS'] = '%s  prefixAdvertisements:\n' % (
                        attributes['BGP_ADVERTISEMENTS']
                    )
                    for external_ip in self.ocp_parameters['bgp']['external_ips']:
                        if len(external_ip.split(',')) > 1:
                            attributes['BGP_ADVERTISEMENTS'] = '%s  - cidr: %s\n' % (
                                attributes['BGP_ADVERTISEMENTS'],
                                external_ip.split(',')[0]
                            )
                            attributes['BGP_ADVERTISEMENTS'] = '%s    communities:\n' % (
                                attributes['BGP_ADVERTISEMENTS']
                            )
                            for community in external_ip.split(',')[1:]:
                                attributes['BGP_ADVERTISEMENTS'] = '%s    - %s\n' % (
                                    attributes['BGP_ADVERTISEMENTS'],
                                    community
                                )
                attributes['BGP_ADVERTISEMENTS'] = attributes['BGP_ADVERTISEMENTS'].rstrip('\n')

            attributes['BGP_PEERS'] = ''
            for peer in self.ocp_parameters['bgp']['peer']:
                attributes['BGP_PEERS'] = '%s---\n' % (attributes['BGP_PEERS'])
                attributes['BGP_PEERS'] = '%sapiVersion: projectcalico.org/v3\n' % (attributes['BGP_PEERS'])
                attributes['BGP_PEERS'] = '%skind: BGPPeer\n' % (attributes['BGP_PEERS'])
                attributes['BGP_PEERS'] = '%smetadata:\n' % (attributes['BGP_PEERS'])
                attributes['BGP_PEERS'] = '%s  name: %s\n' % (attributes['BGP_PEERS'], peer)
                attributes['BGP_PEERS'] = '%sspec:\n' % (attributes['BGP_PEERS'])
                attributes['BGP_PEERS'] = '%s  asNumber: %s\n' % (attributes['BGP_PEERS'], str(self.ocp_parameters['bgp']['remote_as']))
                attributes['BGP_PEERS'] = '%s  peerIP: %s\n' % (attributes['BGP_PEERS'], peer)

        # Non-user input related variables

        attributes['DNS_SERIAL'] = '%s01' % (datetime.date.today().strftime("%Y%m%d"))

        # IP address octets variables

        new_attributes = {}
        for key in attributes:
            if ip_helper.is_valid_ipv4_address(attributes[key]):
                index = 1
                for octet in attributes[key].split('.'):
                    new_attributes['%s_OCTET_%s' % (key, index)] = octet
                    index = index + 1

        for key in new_attributes:
            if key not in attributes:
                attributes[key] = new_attributes[key]

        self.my_output.info('Completed')
        self.my_output.debug(json.dumps(attributes, indent=4))

        return attributes

    def get_vsphere_ipi_installer_ks(self, variables):
        if not self.is_template_valid('ip-static.ks', variables):
            return None

        kickstart = {}
        kickstart['enabled'] = True
        kickstart['template'] = self.get_template_filename('ip-static.ks')
        kickstart['delete_source'] = True
        kickstart['overwrite'] = self.ocp_parameters['installer']['ks']['overwrite']
        kickstart['delete_destination'] = True
        kickstart['generate'] = True

        self.my_output.info('Kickstart template verified: %s' % (kickstart['template']))

        kickstart['source'] = '/tmp/%s.iso' % (str(uuid.uuid4()))
        self.my_output.debug('Generated kickstart iso target location: %s' % (kickstart['source']))

        if self.ocp_parameters['installer']['ks']['folder'] is None:
            kickstart['folder_name'] = '/'
        else:
            kickstart['folder_name'] = '/%s/' % (self.ocp_parameters['installer']['ks']['folder'].rstrip('/').lstrip('/'))
        kickstart['file_name'] = '%s-ks.iso' % (self.ocp_parameters['installer']['vm']['name'])
        kickstart['destination'] = '%s%s' % (kickstart['folder_name'], kickstart['file_name'])
        self.my_output.info('kickstart destination value verified: %s' % (kickstart['destination']))

        success = self.vcenter_handler.is_datastore_folder(
            self.ocp_parameters['vcenter']['datacenter'],
            self.ocp_parameters['vcenter']['datastore'],
            kickstart['folder_name']
        )
        if success:
            self.my_output.debug('datastore folder found: %s' % (kickstart['folder_name']))
            kickstart['is_folder'] = True
        else:
            self.my_output.debug('datastore folder not found: %s' % (kickstart['folder_name']))
            kickstart['is_folder'] = False

        success = self.vcenter_handler.is_datastore_file(
            self.ocp_parameters['vcenter']['datacenter'],
            self.ocp_parameters['vcenter']['datastore'],
            kickstart['folder_name'],
            kickstart['file_name']
        )
        if success:
            kickstart['is_file'] = True
            self.my_output.debug('datastore file found: %s' % (kickstart['file_name']))
        else:
            kickstart['is_file'] = False
            self.my_output.debug('datastore file not found: %s' % (kickstart['file_name']))

        self.my_output.info('Completed')
        return kickstart

    def get_vsphere_ipi_installer_vm_parameters(self, iso, kickstart):
        vm_parameters = {}
        vm_parameters['datacenter_name'] = self.ocp_parameters['vcenter']['datacenter']
        vm_parameters['datastore_name'] = self.ocp_parameters['vcenter']['datastore']
        vm_parameters['host_ip'] = None
        if 'host_ip' in self.ocp_parameters['vcenter']:
            vm_parameters['host_ip'] = self.ocp_parameters['vcenter']['host_ip']
        vm_parameters['distribution'] = self.ocp_parameters['installer']['vm']['template']
        vm_parameters['name'] = self.ocp_parameters['installer']['vm']['name']
        vm_parameters['cpu'] = self.ocp_parameters['installer']['vm']['cpu']
        vm_parameters['memory'] = self.ocp_parameters['installer']['vm']['memory']
        vm_parameters['disk'] = []
        disk_info = {}
        disk_info['size'] = self.ocp_parameters['installer']['vm']['disk']['size']
        disk_info['thin'] = False
        if self.ocp_parameters['installer']['vm']['disk']['type'] == 'thin':
            disk_info['thin'] = True
        vm_parameters['disk'].append(disk_info)
        vm_parameters['network'] = []
        network_info = {}
        network_info['name'] = self.ocp_parameters['vcenter']['network']
        network_info['type'] = self.ocp_parameters['installer']['vm']['interface']['type']
        vm_parameters['network'].append(network_info)
        vm_parameters['cdrom'] = []
        cdrom_info = {}
        cdrom_info['datastore_name'] = self.ocp_parameters['vcenter']['datastore']
        cdrom_info['iso'] = iso['destination']
        vm_parameters['cdrom'].append(cdrom_info)
        cdrom_info = {}
        cdrom_info['datastore_name'] = self.ocp_parameters['vcenter']['datastore']
        cdrom_info['iso'] = kickstart['destination']
        vm_parameters['cdrom'].append(cdrom_info)
        vm_parameters['ssh'] = {}
        vm_parameters['ssh']['enabled'] = True
        vm_parameters['ssh']['username'] = self.ocp_parameters['installer']['vm']['username']
        vm_parameters['ssh']['password'] = self.ocp_parameters['installer']['vm']['password']
        vm_parameters['ssh']['ip'] = self.ocp_parameters['installer']['vm']['ip']

        return vm_parameters

    def get_vsphere_ipi_installer_parameters(self):
        installer = {}
        installer['vcenter'] = self.ocp_parameters['vcenter']

        if 'jump' in self.ocp_parameters:
            installer['jump'] = self.ocp_parameters['jump']
            installer['jump']['enabled'] = True

        installer['iso'] = self.get_vshpere_ipi_installer_iso()
        if installer['iso'] is None:
            return None

        installer['variables'] = self.get_vsphere_ipi_installer_variables()
        if installer['variables'] is None:
            return None

        installer['ks'] = self.get_vsphere_ipi_installer_ks(
            installer['variables']
        )
        if installer['ks'] is None:
            return None

        installer['vm'] = self.get_vsphere_ipi_installer_vm_parameters(
            installer['iso'],
            installer['ks']
        )
        if installer['vm'] is None:
            return None

        return installer
