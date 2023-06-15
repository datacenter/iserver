# https://kubevirt.io/user-guide/virtual_machines/disks_and_volumes/


class OcpVmGetDisk():
    def __init__(self):
        self.lvm = {}

    def get_ocp_vm_disk_type(self, disk_mo):
        if disk_mo is None:
            return 'n/a'

        if 'cdrom' in disk_mo and disk_mo['cdrom'] is not None:
            return 'cdrom'

        if 'disk' in disk_mo and disk_mo['disk'] is not None:
            return 'disk'

        if 'lun' in disk_mo and disk_mo['lun'] is not None:
            return 'lun'

        return 'unknown'

    def get_ocp_vm_disk_bus(self, disk_mo):
        if 'cdrom' in disk_mo and disk_mo['cdrom'] is not None:
            return disk_mo['cdrom']['bus']

        if 'disk' in disk_mo and disk_mo['disk'] is not None:
            return disk_mo['disk']['bus']

        return 'unknown'

    def get_ocp_vm_disk_volume_spec_info(self, volume_spec_mo):
        info = {}
        info['name'] = volume_spec_mo['name']
        info['type'] = 'unknown'
        info['info'] = {}

        if 'cloud_init_config_drive' in volume_spec_mo and volume_spec_mo['cloud_init_config_drive'] is not None:
            info['type'] = 'cloudInitConfigDrive'
            for key in volume_spec_mo['cloud_init_config_drive']:
                info['info'][key] = volume_spec_mo['cloud_init_config_drive'][key]

        if 'cloud_init_no_cloud' in volume_spec_mo and volume_spec_mo['cloud_init_no_cloud'] is not None:
            info['type'] = 'cloudInitNoCloud'
            for key in volume_spec_mo['cloud_init_no_cloud']:
                info['info'][key] = volume_spec_mo['cloud_init_no_cloud'][key]

        if 'config_map' in volume_spec_mo and volume_spec_mo['config_map'] is not None:
            info['type'] = 'configMap'
            for key in volume_spec_mo['config_map']:
                info['info'][key] = volume_spec_mo['config_map'][key]

        if 'container_disk' in volume_spec_mo and volume_spec_mo['container_disk'] is not None:
            info['type'] = 'containerDisk'
            for key in volume_spec_mo['container_disk']:
                info['info'][key] = volume_spec_mo['container_disk'][key]

        if 'data_volume' in volume_spec_mo and volume_spec_mo['data_volume'] is not None:
            info['type'] = 'dataVolume'
            for key in volume_spec_mo['data_volume']:
                info['info'][key] = volume_spec_mo['data_volume'][key]

        if 'empty_disk' in volume_spec_mo and volume_spec_mo['empty_disk'] is not None:
            info['type'] = 'emptyDisk'
            for key in volume_spec_mo['empty_disk']:
                info['info'][key] = volume_spec_mo['empty_disk'][key]

        if 'host_disk' in volume_spec_mo and volume_spec_mo['host_disk'] is not None:
            info['type'] = 'hostDisk'
            for key in volume_spec_mo['host_disk']:
                info['info'][key] = volume_spec_mo['host_disk'][key]

        if 'ephemeral' in volume_spec_mo and volume_spec_mo['ephemeral'] is not None:
            info['type'] = 'ephemeral'
            for key in volume_spec_mo['ephemeral']:
                info['info'][key] = volume_spec_mo['ephemeral'][key]

        if 'persistent_volume_claim' in volume_spec_mo and volume_spec_mo['persistent_volume_claim'] is not None:
            info['type'] = 'persistentVolumeClaim'
            for key in volume_spec_mo['persistent_volume_claim']:
                info['info'][key] = volume_spec_mo['persistent_volume_claim'][key]

        if 'secret' in volume_spec_mo and volume_spec_mo['secret'] is not None:
            info['type'] = 'secret'
            for key in volume_spec_mo['secret']:
                info['info'][key] = volume_spec_mo['secret'][key]

        return info

    def get_ocp_vm_disks_info(self, vm_mo, vmi_mo):
        disks = vm_mo['spec']['template']['spec']['domain']['devices']['disks']
        for disk in disks:
            disk['type'] = self.get_ocp_vm_disk_type(disk)
            for volume in vm_mo['spec']['template']['spec']['volumes']:
                if volume['name'] == disk['name']:
                    disk['volume'] = self.get_ocp_vm_disk_volume_spec_info(volume)

        if vmi_mo is None:
            for disk in disks:
                disk['info'] = '%s' % (
                    disk['name']
                )

        if vmi_mo is not None:
            if 'volume_status' in vmi_mo['status'] and vmi_mo['status']['volume_status'] is not None:
                for volume_status in vmi_mo['status']['volume_status']:
                    for disk in disks:
                        if volume_status['name'] == disk['name']:
                            keys = ['persistent_volume_claim_info', 'target']
                            for key in keys:
                                if key in volume_status:
                                    disk[key] = volume_status[key]

                        try:
                            disk['info'] = '%s/%s - %s' % (
                                disk['name'],
                                disk['target'],
                                disk['persistent_volume_claim_info']['capacity']['storage']
                            )
                        except BaseException:
                            disk['info'] = ''

        for disk in disks:
            disk['__Output'] = {}
            disk['bus'] = ''
            if disk['cdrom'] is not None:
                disk['bus'] = disk['cdrom']['bus']

            if disk['disk'] is not None:
                disk['bus'] = disk['disk']['bus']

            disk['pvc_name'] = ''
            disk['storage_class_name'] = ''
            disk['pod_name'] = ''

            if disk['volume']['type'] == 'dataVolume':
                pvc_name = disk['volume']['info']['name']
                pvc_namespace = vm_mo['metadata']['namespace']

                pvc_info = self.k8s_handler.get_pvc_info(
                    self.k8s_handler.get_pvc(
                        pvc_namespace,
                        pvc_name
                    )
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

            if disk['volume']['type'] == 'persistentVolumeClaim':
                pvc_name = disk['volume']['info']['claim_name']
                pvc_namespace = vm_mo['metadata']['namespace']

                pvc_info = self.k8s_handler.get_pvc_info(
                    self.k8s_handler.get_pvc(
                        pvc_namespace,
                        pvc_name
                    )
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

            disk['pv'] = self.k8s_handler.get_pv_info(
                self.k8s_handler.get_pv(
                    disk['pvc_name']
                )
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
        lvms = self.get_ocp_node_lvms(vm_info['nodeName'])
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
                    if lvm['name'] == disk['pv']['csi_handle']:
                        disk['lvm'] = lvm

        return vm_info
