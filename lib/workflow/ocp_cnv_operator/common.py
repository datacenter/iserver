import json
import copy
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    return params

def get_default_params():
    params = {}
    params['namespace'] = 'openshift-cnv'
    params['name'] = 'kubevirt-hyperconverged'
    params['operator-group-name'] = 'cnv-operator-group'
    params['delete-namespace'] = True
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params

def is_cnv_used(k8s_handler, k8s_output_handler, my_output, cache_enabled=False):
    data_volumes = k8s_handler.get_data_volumes(
        cache_enabled=cache_enabled
    )
    if data_volumes is None:
        my_output.error('Failed to get data volumes, not sure if storage is used')
        return True
        
    is_ready = False
    for data_volume in data_volumes:
        if data_volume['ready']:
            is_ready = True
            break

    if is_ready:
        k8s_output_handler.print_data_volumes(
            data_volumes
        )
        my_output.default('Delete data volumes first')
        return True
    
    my_output.default('No ready data volumes found <=> virtualization subsystem is not using storage')
    return False

def get_cnv_crd(k8s_handler, my_output=None, cache_enabled=False, message_on_error=True, crd=['__all__']):
    if my_output is not None:
        my_output.default('Get OpenShift Virtualization CRD', before_newline=True, underline=True)

    response = {}

    response['aaq'] = None   
    if 'AAQ' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- AAQ')

        response['aaq'] = k8s_handler.get_aaqs(
            cache_enabled=cache_enabled
        )
        if response['aaq'] is None and message_on_error:
            my_output.error('AAQ crd failed')

    response['cdi_config'] = None   
    if 'CDIConfig' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CDIConfig')

        response['cdi_config'] = k8s_handler.get_cdi_configs(
            cache_enabled=cache_enabled
        )
        if response['cdi_config'] is None and message_on_error:
            my_output.error('CDIConfig crd failed')

    response['cdi'] = None   
    if 'CDI' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CDI')

        response['cdi'] = k8s_handler.get_cdis(
            cache_enabled=cache_enabled
        )
        if response['cdi'] is None and message_on_error:
            my_output.error('CDI crd failed')

    response['data_import_cron'] = None   
    if 'DataImportCron' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- DataImportCron')

        response['data_import_cron'] = k8s_handler.get_data_import_crons(
            cache_enabled=cache_enabled
        )
        if response['data_import_cron'] is None and message_on_error:
            my_output.error('DataImportCron crd failed')

    response['data_source'] = None   
    if 'DataSource' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- DataSource')

        response['data_source'] = k8s_handler.get_data_sources(
            dv_info=True,
            pvc_info=True,
            cron_info=True,
            cache_enabled=cache_enabled
        )
        if response['data_source'] is None and message_on_error:
            my_output.error('DataSource crd failed')

    response['data_volume'] = None   
    if 'DataVolume' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- DataVolume')

        response['data_volume'] = k8s_handler.get_data_volumes(
            cache_enabled=cache_enabled
        )
        if response['data_volume'] is None and message_on_error:
            my_output.error('DataVolume crd failed')

    response['object_transfer'] = None   
    if 'ObjectTransfer' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- ObjectTransfer')

        response['object_transfer'] = k8s_handler.get_object_transfers(
            cache_enabled=cache_enabled
        )
        if response['object_transfer'] is None and message_on_error:
            my_output.error('ObjectTransfer crd failed')

    response['storage_profile'] = None   
    if 'StorageProfile' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageProfile')

        response['storage_profile'] = k8s_handler.get_storage_profiles(
            cache_enabled=cache_enabled
        )
        if response['storage_profile'] is None and message_on_error:
            my_output.error('StorageProfile crd failed')

    response['volume_clone_source'] = None   
    if 'VolumeCloneSource' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VolumeCloneSource')

        response['volume_clone_source'] = k8s_handler.get_volume_clone_sources(
            cache_enabled=cache_enabled
        )
        if response['volume_clone_source'] is None and message_on_error:
            my_output.error('VolumeCloneSource crd failed')

    response['volume_import_source'] = None   
    if 'VolumeImportSource' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VolumeImportSource')

        response['volume_import_source'] = k8s_handler.get_volume_import_sources(
            cache_enabled=cache_enabled
        )
        if response['volume_import_source'] is None and message_on_error:
            my_output.error('VolumeImportSource crd failed')

    response['volume_upload_source'] = None   
    if 'VolumeUploadSource' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VolumeUploadSource')

        response['volume_upload_source'] = k8s_handler.get_volume_upload_sources(
            cache_enabled=cache_enabled
        )
        if response['volume_upload_source'] is None and message_on_error:
            my_output.error('VolumeUploadSource crd failed')

    response['virtual_machine_clone'] = None   
    if 'VirtualMachineClone' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachineClone')

        response['virtual_machine_clone'] = k8s_handler.get_virtual_machine_clones(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_clone'] is None and message_on_error:
            my_output.error('VirtualMachineClone crd failed')

    response['virtual_machine_export'] = None   
    if 'VirtualMachineExport' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachineExport')

        response['virtual_machine_export'] = k8s_handler.get_virtual_machine_exports(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_export'] is None and message_on_error:
            my_output.error('VirtualMachineExport crd failed')

    response['openstack_volume_populator'] = None   
    if 'OpenstackVolumePopulator' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- OpenstackVolumePopulator')

        response['openstack_volume_populator'] = k8s_handler.get_openstack_volume_populators(
            cache_enabled=cache_enabled
        )
        if response['openstack_volume_populator'] is None and message_on_error:
            my_output.error('OpenstackVolumePopulator crd failed')

    response['ovirt_volume_populator'] = None   
    if 'OvirtVolumePopulator' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- OvirtVolumePopulator')

        response['ovirt_volume_populator'] = k8s_handler.get_ovirt_volume_populators(
            cache_enabled=cache_enabled
        )
        if response['ovirt_volume_populator'] is None and message_on_error:
            my_output.error('OvirtVolumePopulator crd failed')

    response['hyperconverged'] = None   
    if 'HyperConverged' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- HyperConverged')

        response['hyperconverged'] = k8s_handler.get_hyperconvergeds(
            cache_enabled=cache_enabled
        )
        if response['hyperconverged'] is None and message_on_error:
            my_output.error('HyperConverged crd failed')

    response['host_path_provisioner'] = None   
    if 'HostPathProvisioner' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- HostPathProvisioner')

        response['host_path_provisioner'] = k8s_handler.get_host_path_provisioners(
            cache_enabled=cache_enabled
        )
        if response['host_path_provisioner'] is None and message_on_error:
            my_output.error('HostPathProvisioner crd failed')

    response['migration_policy'] = None   
    if 'MigrationPolicy' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- MigrationPolicy')

        response['migration_policy'] = k8s_handler.get_migration_policies(
            cache_enabled=cache_enabled
        )
        if response['migration_policy'] is None and message_on_error:
            my_output.error('MigrationPolicy crd failed')

    response['network_addons_config'] = None   
    if 'NetworkAddonsConfig' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- NetworkAddonsConfig')

        response['network_addons_config'] = k8s_handler.get_network_addons_configs(
            cache_enabled=cache_enabled
        )
        if response['network_addons_config'] is None and message_on_error:
            my_output.error('NetworkAddonsConfig crd failed')

    response['virtual_machine_cluster_instance_type'] = None   
    if 'VirtualMachineClusterInstancetype' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachineClusterInstancetype')

        response['virtual_machine_cluster_instance_type'] = k8s_handler.get_virtual_machine_cluster_instance_types(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_cluster_instance_type'] is None and message_on_error:
            my_output.error('VirtualMachineClusterInstancetype crd failed')

    response['virtual_machine_pool'] = None   
    if 'VirtualMachinePool' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachinePool')

        response['virtual_machine_pool'] = k8s_handler.get_virtual_machine_pools(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_pool'] is None and message_on_error:
            my_output.error('VirtualMachinePool crd failed')

    response['virtual_machine_restore'] = None   
    if 'VirtualMachineRestore' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachineRestore')

        response['virtual_machine_restore'] = k8s_handler.get_virtual_machine_restores(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_restore'] is None and message_on_error:
            my_output.error('VirtualMachineRestore crd failed')

    response['virtual_machine_snapshot_content'] = None   
    if 'VirtualMachineSnapshotContent' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachineSnapshotContent')

        response['virtual_machine_snapshot_content'] = k8s_handler.get_virtual_machine_snapshot_contents(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_snapshot_content'] is None and message_on_error:
            my_output.error('VirtualMachineSnapshotContent crd failed')

    response['virtual_machine_snapshot'] = None   
    if 'VirtualMachineSnapshot' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- VirtualMachineSnapshot')

        response['virtual_machine_snapshot'] = k8s_handler.get_virtual_machine_snapshots(
            cache_enabled=cache_enabled
        )
        if response['virtual_machine_snapshot'] is None and message_on_error:
            my_output.error('VirtualMachineSnapshot crd failed')

    response['ssp'] = None   
    if 'SSP' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- SSP')

        response['ssp'] = k8s_handler.get_ssps(
            cache_enabled=cache_enabled
        )
        if response['ssp'] is None and message_on_error:
            my_output.error('SSP crd failed')

    return response

def print_cnv_crd(crds, k8s_output_handler, only_non_zero=True, crd=['__all__']):
    if 'AAQ' in crd or '__all__' in crd:
        if crds['aaq'] is not None:
            if not only_non_zero or len(crds['aaq']) > 0:
                k8s_output_handler.print_aaqs(
                    crds['aaq']
                )

    if 'CDIConfig' in crd or '__all__' in crd:
        if crds['cdi_config'] is not None:
            if not only_non_zero or len(crds['cdi_config']) > 0:
                k8s_output_handler.print_cdi_configs(
                    crds['cdi_config']
                )
    
    if 'CDI' in crd or '__all__' in crd:
        if crds['cdi'] is not None:
            if not only_non_zero or len(crds['cdi']) > 0:
                k8s_output_handler.print_cdis(
                    crds['cdi']
                )

    if 'DataImportCron' in crd or '__all__' in crd:
        if crds['data_import_cron'] is not None:
            if not only_non_zero or len(crds['data_import_cron']) > 0:
                k8s_output_handler.print_data_import_crons(
                    crds['data_import_cron']
                )

    if 'DataSource' in crd or '__all__' in crd:
        if crds['data_source'] is not None:
            if not only_non_zero or len(crds['data_source']) > 0:
                k8s_output_handler.print_data_sources(
                    crds['data_source']
                )

    if 'DataVolume' in crd or '__all__' in crd:
        if crds['data_volume'] is not None:
            if not only_non_zero or len(crds['data_volume']) > 0:
                k8s_output_handler.print_data_volumes(
                    crds['data_volume']
                )

    if 'ObjectTransfer' in crd or '__all__' in crd:
        if crds['object_transfer'] is not None:
            if not only_non_zero or len(crds['object_transfer']) > 0:
                k8s_output_handler.print_object_transfers(
                    crds['object_transfer']
                )

    if 'StorageProfile' in crd or '__all__' in crd:
        if crds['storage_profile'] is not None:
            if not only_non_zero or len(crds['storage_profile']) > 0:
                k8s_output_handler.print_storage_profiles(
                    crds['storage_profile']
                )

    if 'VolumeCloneSource' in crd or '__all__' in crd:
        if crds['volume_clone_source'] is not None:
            if not only_non_zero or len(crds['volume_clone_source']) > 0:
                k8s_output_handler.print_volume_clone_sources(
                    crds['volume_clone_source']
                )

    if 'VolumeImportSource' in crd or '__all__' in crd:
        if crds['volume_import_source'] is not None:
            if not only_non_zero or len(crds['volume_import_source']) > 0:
                k8s_output_handler.print_volume_import_sources(
                    crds['volume_import_source']
                )

    if 'VolumeUploadSource' in crd or '__all__' in crd:
        if crds['volume_upload_source'] is not None:
            if not only_non_zero or len(crds['volume_upload_source']) > 0:
                k8s_output_handler.print_volume_upload_sources(
                    crds['volume_upload_source']
                )
            
    if 'VirtualMachineClone' in crd or '__all__' in crd:
        if crds['virtual_machine_clone'] is not None:
            if not only_non_zero or len(crds['virtual_machine_clone']) > 0:
                k8s_output_handler.print_virtual_machine_clones(
                    crds['virtual_machine_clone']
                )

    if 'VirtualMachineExport' in crd or '__all__' in crd:
        if crds['virtual_machine_export'] is not None:
            if not only_non_zero or len(crds['virtual_machine_export']) > 0:
                k8s_output_handler.print_virtual_machine_exports(
                    crds['virtual_machine_export']
                )

    if 'OpenstackVolumePopulator' in crd or '__all__' in crd:
        if crds['openstack_volume_populator'] is not None:
            if not only_non_zero or len(crds['openstack_volume_populator']) > 0:
                k8s_output_handler.print_openstack_volume_populators(
                    crds['openstack_volume_populator']
                )

    if 'OvirtVolumePopulator' in crd or '__all__' in crd:
        if crds['ovirt_volume_populator'] is not None:
            if not only_non_zero or len(crds['ovirt_volume_populator']) > 0:
                k8s_output_handler.print_ovirt_volume_populators(
                    crds['ovirt_volume_populator']
                )

    if 'HyperConverged' in crd or '__all__' in crd:
        if crds['hyperconverged'] is not None:
            if not only_non_zero or len(crds['hyperconverged']) > 0:
                k8s_output_handler.print_hyperconvergeds(
                    crds['hyperconverged']
                )

    if 'HostPathProvisioner' in crd or '__all__' in crd:
        if crds['host_path_provisioner'] is not None:
            if not only_non_zero or len(crds['host_path_provisioner']) > 0:
                k8s_output_handler.print_host_path_provisioners(
                    crds['host_path_provisioner']
                )

    if 'MigrationPolicy' in crd or '__all__' in crd:
        if crds['migration_policy'] is not None:
            if not only_non_zero or len(crds['migration_policy']) > 0:
                k8s_output_handler.print_migration_policies(
                    crds['migration_policy']
                )

    if 'NetworkAddonsConfig' in crd or '__all__' in crd:
        if crds['network_addons_config'] is not None:
            if not only_non_zero or len(crds['network_addons_config']) > 0:
                k8s_output_handler.print_network_addons_configs(
                    crds['network_addons_config']
                )

    if 'VirtualMachineClusterInstancetype' in crd or '__all__' in crd:
        if crds['virtual_machine_cluster_instance_type'] is not None:
            if not only_non_zero or len(crds['virtual_machine_cluster_instance_type']) > 0:
                k8s_output_handler.print_virtual_machine_cluster_instance_types(
                    crds['virtual_machine_cluster_instance_type']
                )

    if 'VirtualMachinePool' in crd or '__all__' in crd:
        if crds['virtual_machine_pool'] is not None:
            if not only_non_zero or len(crds['virtual_machine_pool']) > 0:
                k8s_output_handler.print_virtual_machine_pools(
                    crds['virtual_machine_pool']
                )

    if 'VirtualMachineRestore' in crd or '__all__' in crd:
        if crds['virtual_machine_restore'] is not None:
            if not only_non_zero or len(crds['virtual_machine_restore']) > 0:
                k8s_output_handler.print_virtual_machine_restores(
                    crds['virtual_machine_restore']
                )

    if 'VirtualMachineSnapshotContent' in crd or '__all__' in crd:
        if crds['virtual_machine_snapshot_content'] is not None:
            if not only_non_zero or len(crds['virtual_machine_snapshot_content']) > 0:
                k8s_output_handler.print_virtual_machine_snapshot_contents(
                    crds['virtual_machine_snapshot_content']
                )

    if 'VirtualMachineSnapshot' in crd or '__all__' in crd:
        if crds['virtual_machine_snapshot'] is not None:
            if not only_non_zero or len(crds['virtual_machine_snapshot']) > 0:
                k8s_output_handler.print_virtual_machine_snapshots(
                    crds['virtual_machine_snapshot']
                )
    