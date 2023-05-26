# https://kubevirt.io/user-guide/virtual_machines/disks_and_volumes/


class OcpVmDisk():
    def __init__(self):
        pass

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

    def get_ocp_vm_disks_info(self, namespace, name):
        info = self.get_ocp_vms_info(
            name=name,
            namespace=namespace
        )
        if info is None:
            return None

        for disk in info['disks']:
            disk['__Output'] = {}
            disk['bus'] = self.get_ocp_vm_disk_bus(
                disk
            )

            if disk['volume']['type'] == 'dataVolume':
                pvc_name = disk['volume']['info']['name']
                pvc_namespace = info['namespace']

                pvc_info = self.k8s_handler.get_pvc_info(
                    self.k8s_handler.get_pvc(
                        pvc_namespace,
                        pvc_name
                    )
                )

                disk['persistent_volume_claim_info'] = pvc_info
                for key in disk['persistent_volume_claim_info']['__Output']:
                    disk['__Output']['persistent_volume_claim_info.%s' % (key)] = disk['persistent_volume_claim_info']['__Output'][key]

            if disk['volume']['type'] == 'persistentVolumeClaim':
                pvc_name = disk['volume']['info']['claim_name']
                pvc_namespace = info['namespace']

                pvc_info = self.k8s_handler.get_pvc_info(
                    self.k8s_handler.get_pvc(
                        pvc_namespace,
                        pvc_name
                    )
                )

                disk['persistent_volume_claim_info'] = pvc_info
                for key in disk['persistent_volume_claim_info']['__Output']:
                    disk['__Output']['persistent_volume_claim_info.%s' % (key)] = disk['persistent_volume_claim_info']['__Output'][key]

        return info

    def print_ocp_vm_disks_info(self, info, show_vm_info=True, stream='default'):
        if show_vm_info:
            self.print_ocp_vm_base_info(info, stream=stream)

        order = [
            'name',
            'type',
            'bus',
            'target',
            'volume.type',
            'persistent_volume_claim_info.name',
            'persistent_volume_claim_info.phase',
            'persistent_volume_claim_info.storage_class_name',
            'persistent_volume_claim_info.access_modes_string',
            'persistent_volume_claim_info.capacity.storage',
            'persistent_volume_claim_info.volume_mode'
        ]

        headers = [
            'Name',
            'Type',
            'Bus',
            'Target',
            'Volume Type',
            'Volume Name',
            'Volume State',
            'SC',
            'Access Modes',
            'Storage',
            'Volume Mode'
        ]

        self.my_output.my_table(
            info['disks'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream=stream
        )
