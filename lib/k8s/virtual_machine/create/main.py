from lib.k8s.virtual_machine.create.c8kv import K8sVirtualMachineCreateC8kv


class K8sVirtualMachineCreate(K8sVirtualMachineCreateC8kv):
    def __init__(self):
        K8sVirtualMachineCreateC8kv.__init__(self)

    def increase_virtual_machine_disk_size(self, size, factor):
        if not isinstance(size, str):
            return size
        
        if not size.endswith('Gi'):
            return size
        
        try:
            new_size = '%sGi' % (str(float(size.split('Gi')[0]) * factor))
        except BaseException:
            return size
        
        return new_size
    
    def get_virtual_machine_body_main(self, namespace, name, labels=None):
        body = {}
        body['apiVersion'] = 'kubevirt.io/v1'
        body['kind'] = 'VirtualMachine'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if labels is not None:
            body['metadata']['labels'] = {}
            for key in labels:
                body['metadata']['labels'][key] = labels[key]

        body['spec'] = {}
        return body

    def get_virtual_machine_data_volume_url_template_body(self, namespace, name, size, url, storage_class=None):
        body = {}
        body['apiVersion'] = 'cdi.kubevirt.io/v1beta1'
        body['kind'] = 'DataVolume'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['pvc'] = {}
        if storage_class is not None:
            body['spec']['pvc']['storageClassName'] = storage_class
        body['spec']['pvc']['accessModes'] = ['ReadWriteOnce']
        body['spec']['pvc']['resources'] = dict(requests=dict(storage=size))
        body['spec']['pvc']['volumeMode'] = 'Block'
        body['spec']['source'] = dict(http=dict(url=url))
        return body

    def get_virtual_machine_data_volume_pvc_template_body(self, namespace, name, size, pvc, storage_class=None):
        body = {}
        body['apiVersion'] = 'cdi.kubevirt.io/v1beta1'
        body['kind'] = 'DataVolume'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['pvc'] = {}
        if storage_class is not None:
            body['spec']['pvc']['storageClassName'] = storage_class
        body['spec']['pvc']['accessModes'] = ['ReadWriteOnce']
        body['spec']['pvc']['resources'] = dict(requests=dict(storage=size))
        body['spec']['pvc']['volumeMode'] = 'Block'

        if len(pvc.split('/')) == 1:
            pvc_name = pvc
            pvc_namespace = namespace
        else:
            (pvc_namespace, pvc_name) = pvc.split('/')

        body['spec']['source'] = dict(pvc=dict(name=pvc_name, namespace=pvc_namespace))
        return body
    
    def get_virtual_machine_template_body(
            self, 
            namespace, 
            name, 
            cores, 
            sockets, 
            threads, 
            memory, 
            interface=None, 
            day0=None,
            node=None
        ):
        body = {}
        body['metadata'] = {}
        body['metadata']['labels'] = {}
        body['metadata']['labels']['kubevirt.io/domain'] = name
        body['metadata']['labels']['app'] = name

        body['spec'] = {}

        if node is not None:
            body['spec']['nodeSelector'] = {}
            body['spec']['nodeSelector']['kubernetes.io/hostname'] = node

        body['spec']['hostname'] = name
        body['spec']['evictionStrategy'] = 'LiveMigrate'

        body['spec']['domain'] = {}
        body['spec']['domain']['cpu'] = dict(cores=cores, sockets=sockets, threads=threads)
        body['spec']['domain']['resources'] = dict(requests=dict(memory=memory))

        body['spec']['domain']['devices'] = {}
        body['spec']['domain']['devices']['rng'] = {}

        body['spec']['domain']['devices']['disks'] = []
        body['spec']['volumes'] = []

        disk_mo = {}
        disk_mo['name'] = 'rootdisk'
        disk_mo['disk'] = dict(bus='virtio')
        body['spec']['domain']['devices']['disks'].append(disk_mo)

        volume_mo = {}
        volume_mo['name'] = 'rootdisk'
        volume_mo['dataVolume'] = dict(namespace=namespace, name=name)
        body['spec']['volumes'].append(volume_mo)

        if day0 is not None:
            disk_mo = {}
            disk_mo['name'] = 'day0'
            disk_mo['cdrom'] = dict(readyOnly=True, bus='sata')
            body['spec']['domain']['devices']['disks'].append(disk_mo)

            volume_mo = {}
            volume_mo['name'] = 'day0'
            volume_mo['configMap'] = dict(namespace=namespace, name=day0)
            body['spec']['volumes'].append(volume_mo)

        body['spec']['domain']['devices']['interfaces'] = []
        body['spec']['networks'] = []

        if interface is None:
            interface_mo = {}
            interface_mo['name'] = 'default'
            interface_mo['masquerade'] = {}
            body['spec']['domain']['devices']['interfaces'].append(interface_mo)

            network_mo = {}
            network_mo['name'] = 'default'
            network_mo['pod'] = {}
            body['spec']['networks'].append(network_mo)

        if interface is not None:
            for item in interface:
                interface_mo = {}
                interface_mo['name'] = item['name']
                if item['type'] not in ['udn-l2-primary', 'udn-l3-primary']:
                    interface_mo[item['type']] = {}
                if item['type'] == 'udn-l2-primary':
                    interface_mo['binding'] = dict(name='l2bridge')
                if item['type'] == 'udn-l3-primary':
                    interface_mo['binding'] = dict(name='l2bridge')

                body['spec']['domain']['devices']['interfaces'].append(interface_mo)

                network_mo = {}
                network_mo['name'] = item['name']
                if item['type'] in ['masquerade', 'udn-l2-primary', 'udn-l3-primary']:
                    network_mo['pod'] = {}

                if 'nad' in item:
                    network_mo['multus'] = {}
                    network_mo['multus']['networkName'] = '%s/%s' % (namespace, item['nad'])

                body['spec']['networks'].append(network_mo)

        return body
    
    def create_virtual_machine_template(
            self, 
            namespace,
            name,
            template, 
            variables,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = None
        if template == 'c8kv':
            body, error = self.get_virtual_machine_c8kv_body(
                namespace,
                name,
                variables
            )
            if body is None:
                if my_output is not None:
                    my_output.error(error)
                return False

        if body is None:
            if my_output is not None:
                my_output.error('virtual machine cr body generated failed')
            return False
        
        if not self.create_resource(body, object_name='virtual_machine', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_virtual_machine(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if not info['running_expected']:
            return True

        success = self.wait_virtual_machine_up(
            namespace,
            name,
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False
        
        return True