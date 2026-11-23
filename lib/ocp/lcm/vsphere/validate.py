class OcpVsphereValidate():
    def __init__(self):
        pass

    def validate_vcenter_datacenter_name(self, datacenter_name):
        self.my_output.debug('Getting datacenters...')
        datacenters = self.vcenter_handler.get_datacenters()
        if datacenters is None:
            self.my_output.error('No datacenters found')
            return False

        for datacenter in datacenters:
            if datacenter['name'] == datacenter_name:
                self.my_output.info('Datacenter found: %s' % (datacenter_name))
                return True

        self.my_output.error('Datacenter not found: %s' % (datacenter_name))
        return False

    def validate_vcenter_datastore_name(self, datacenter_name, datastore_name):
        self.my_output.debug('Getting datastores available in datacenter...')
        datastores = self.vcenter_handler.get_datastores(datacenter_name=datacenter_name)

        if datastores is None:
            self.my_output.error('No datastores found')
            return False

        for datastore in datastores:
            if datastore['name'] == datastore_name:
                self.my_output.info('Datastore found: %s' % (datastore_name))
                return True

        self.my_output.error('Datastore not found: %s' % (datastore_name))
        return True

    def validate_vcenter_cluster_name(self, cluster_name):
        self.my_output.debug('Getting vcenter clusters...')
        if not self.vcenter_handler.is_vm_cluster(cluster_name):
            self.my_output.error('Cluster not found: %s' % (cluster_name))
            return False

        self.my_output.info('Cluster found: %s' % (cluster_name))
        return True

    def validate_vcenter_folder_name(self, folder_name):
        self.my_output.debug('Getting vcenter folders...')
        if not self.vcenter_handler.is_vm_folder(folder_name):
            self.my_output.error('Folder not found: %s' % (folder_name))
            return False

        self.my_output.info('Folder found: %s' % (folder_name))
        return True

    def validate_vcenter_host_ip(self, vcenter_hosts, host_ip):
        for vcenter_host in vcenter_hosts:
            if vcenter_host == host_ip:
                self.my_output.info('Target host found: %s' % (host_ip))
                return True

        self.my_output.error('Target host not found: %s' % (host_ip))
        return False

    def validate_vcenter_network(self, vcenter_network):
        if not self.vcenter_handler.is_network(vcenter_network):
            self.my_output.error('vcenter network not found: %s' % (vcenter_network))
            self.vcenter_handler.print_network_names(
                title='Available networks'
            )
            return False

        self.my_output.info('Network found: %s' % (vcenter_network))
        return True

    def validate_vcenter(self, vcenter_parameters):
        self.my_output.info('Validate vcenter section', underline=True, before_newline=True)

        if not self.vcenter_connect(vcenter_parameters):
            self.my_output.error('Failed to connect to vcenter')
            return None

        if not self.validate_vcenter_datacenter_name(vcenter_parameters['datacenter']):
            return None

        if not self.validate_vcenter_datastore_name(vcenter_parameters['datacenter'], vcenter_parameters['datastore']):
            return None

        if not self.validate_vcenter_cluster_name(vcenter_parameters['cluster']):
            return None

        host_ips = self.vcenter_handler.get_vm_cluster_hosts(
            vcenter_parameters['cluster']
        )

        self.my_output.debug('vcenter cluster hosts: %s' % (','.join(host_ips)))
        vcenter_parameters['host_ips'] = host_ips

        if vcenter_parameters['host_ip'] is not None:
            if not self.validate_vcenter_host_ip(vcenter_parameters['host_ips'], vcenter_parameters['host_ip']):
                return None

        if vcenter_parameters['folder'] is not None:
            if not self.validate_vcenter_folder_name(vcenter_parameters['folder']):
                return None

        if not self.validate_vcenter_network(vcenter_parameters['network']):
            return None

        self.my_output.info('Completed')

        return vcenter_parameters
