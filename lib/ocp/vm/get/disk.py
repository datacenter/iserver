# https://kubevirt.io/user-guide/virtual_machines/disks_and_volumes/


class OcpVmGetDisk():
    def __init__(self):
        self.lvm = {}

    def get_ocp_vm_disks_info(self, vm_info, vmi_info):
        disks = vm_info['disks']

        if vmi_info is not None and vmi_info['volume_status'] is not None:
            for volume_status in vmi_info['volume_status']:
                for disk in disks:
                    if volume_status['name'] == disk['name']:
                        for key in ['persistent_volume_claim_info', 'target', 'storage']:
                            disk[key] = volume_status[key]

                        disk['info'] = '%s/%s - %s' % (
                            disk['name'],
                            disk['target'],
                            disk['storage']
                        )

        for disk in disks:
            disk['__Output'] = {}
            disk['pvc_name'] = ''
            disk['storage_class_name'] = ''
            disk['pod_name'] = ''

            if disk['volume']['type'] == 'dataVolume':
                pvc_name = disk['volume']['attributes']['name']
                pvc_namespace = vm_info['namespace']

                pvc_info = self.k8s_handler.get_pvc(
                    pvc_namespace,
                    pvc_name
                )

                if pvc_info is not None:
                    disk['pvc_name'] = pvc_info['volume_name']
                    if pvc_info['phase'] == 'Bound':
                        disk['__Output']['pvc_name'] = 'Green'
                    else:
                        disk['__Output']['pvc_name'] = 'Red'

                    disk['storage_class_name'] = pvc_info['storage_class_name']

                    if pvc_info['pod'] is not None:
                        disk['pod_name'] = pvc_info['pod']['name']
                        if 'phase' in pvc_info['pod'] and pvc_info['pod']['phase'] == 'Succeeded':
                            disk['__Output']['pod_name'] = 'Green'
                        else:
                            disk['__Output']['pod_name'] = 'Red'

            if disk['volume']['type'] == 'persistentVolumeClaim':
                pvc_name = disk['volume']['attributes']['claim_name']
                pvc_namespace = vm_info['namespace']

                pvc_info = self.k8s_handler.get_pvc(
                    pvc_namespace,
                    pvc_name
                )

                if pvc_info is not None:
                    disk['pvc_name'] = pvc_info['volume_name']
                    if pvc_info['phase'] == 'Bound':
                        disk['__Output']['pvc_name'] = 'Green'
                    else:
                        disk['__Output']['pvc_name'] = 'Red'

                    disk['storage_class_name'] = pvc_info['storage_class_name']

                    if pvc_info['pod'] is not None:
                        disk['pod_name'] = pvc_info['pod']['name']
                        if pvc_info['pod']['phase'] == 'Succeeded':
                            disk['__Output']['pod_name'] = 'Green'
                        else:
                            disk['__Output']['pod_name'] = 'Red'

            disk['pv'] = self.k8s_handler.get_pv(
                disk['pvc_name']
            )

        return disks

    def get_ocp_node_lvms(self, node_name):
        if node_name in self.lvm:
            return self.lvm[node_name]

        linux_handler = self.get_ocp_node_linux_handler(
            node_name=node_name
        )
        if linux_handler is None:
            return None

        self.lvm[node_name] = linux_handler.get_lvms()
        return self.lvm[node_name]

    def get_ocp_vm_disks_csi_info(self, vm_info):
        lvms = self.get_ocp_node_lvms(vm_info['node_name'])
        if lvms is None:
            self.log.error(
                'get_ocp_vm_disks_csi_info',
                'No lvms info'
            )
            return vm_info

        for disk in vm_info['disks']:
            disk['lvm'] = None
            for lvm in lvms:
                if lvm['name'] is not None:
                    if disk['pv'] is not None:
                        if lvm['name'] == disk['pv']['csi_handle']:
                            disk['lvm'] = lvm

        return vm_info
