import copy
import json
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id, ssh_required=False):
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
    ocp_check_params['ssh-required'] = ssh_required
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    params['ssh-ready'] = False
    if 'ssh_public_key' in ocp_check_params['data']:
        params['ssh-ready'] = True

    return params


def get_default_params():
    params = {}
    params['namespace'] = 'openshift-storage'
    params['name'] = 'odf-operator'
    params['cluster-name'] = 'odf-cluster'
    params['operator-group-name'] = 'openshift-storage-operator-group'
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


def check_state(params, my_output, check_ready=True):
    state = {}

    state['installed'] = params['k8s_handler'].check_odf_subscription(
        params['name'], 
        my_output=my_output,
        check_ready=False
    )

    if not check_ready or not state['installed']:
        return state

    state['ready'] = params['k8s_handler'].is_subscription_odf_ready(my_output=my_output)
    return state


def get_odf_crd(k8s_handler, my_output=None, cache_enabled=False, message_on_error=True, crd=['__all__']):
    if my_output is not None:
        my_output.default('Get OpenShift Data Foundation (ODF) CRD', before_newline=True, underline=True)

    response = {}

    response['ceph_block_pool'] = None   
    if 'CephBlockPool' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephBlockPool')

        response['ceph_block_pool'] = k8s_handler.get_ceph_block_pools(
            cache_enabled=cache_enabled
        )
        if response['ceph_block_pool'] is None and message_on_error:
            my_output.error('CephBlockPool crd failed')

    response['ceph_block_pool_rados_namespace'] = None
    if 'CephBlockPoolRadosNamespace' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephBlockPoolRadosNamespace')

        response['ceph_block_pool_rados_namespace'] = k8s_handler.get_ceph_block_pool_rados_namespaces(
            cache_enabled=cache_enabled
        )
        if response['ceph_block_pool_rados_namespace'] is None and message_on_error:
            my_output.error('CephBlockPoolRadosNamespace crd failed')

    response['ceph_bucket_notification'] = None
    if 'CephBucketNotification' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephBucketNotification')

        response['ceph_bucket_notification'] = k8s_handler.get_ceph_bucket_notifications(
            cache_enabled=cache_enabled
        )
        if response['ceph_bucket_notification'] is None and message_on_error:
            my_output.error('CephBucketNotification crd failed')

    response['ceph_bucket_topic'] = None
    if 'CephBucketTopic' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephBucketTopic')
        
        response['ceph_bucket_topic'] = k8s_handler.get_ceph_bucket_topics(
            cache_enabled=cache_enabled
        )
        if response['ceph_bucket_topic'] is None and message_on_error:
            my_output.error('CephBucketTopic crd failed')

    response['ceph_client'] = None
    if 'CephClient' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephClient')
        
        response['ceph_client'] = k8s_handler.get_ceph_clients(
            cache_enabled=cache_enabled
        )
        if response['ceph_client'] is None and message_on_error:
            my_output.error('CephClient crd failed')

    response['ceph_client_profile'] = None
    if 'ClientProfile' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- ClientProfile')
        
        response['ceph_client_profile'] = k8s_handler.get_ceph_client_profiles(
            cache_enabled=cache_enabled
        )
        if response['ceph_client_profile'] is None and message_on_error:
            my_output.error('ClientProfile crd failed')

    response['ceph_client_profile_mapping'] = None
    if 'ClientProfileMapping' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- ClientProfileMapping')

        response['ceph_client_profile_mapping'] = k8s_handler.get_ceph_client_profile_mappings(
            cache_enabled=cache_enabled
        )
        if response['ceph_client_profile_mapping'] is None and message_on_error:
            my_output.error('ClientProfileMapping crd failed')

    response['ceph_cluster'] = None
    if 'CephCluster' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephCluster')
        
        response['ceph_cluster'] = k8s_handler.get_ceph_clusters(
            cache_enabled=cache_enabled
        )
        if response['ceph_cluster'] is None and message_on_error:
            my_output.error('CephCluster crd failed')

    response['ceph_connection'] = None
    if 'CephConnection' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephConnection')
        
        response['ceph_connection'] = k8s_handler.get_ceph_connections(
            cache_enabled=cache_enabled
        )
        if response['ceph_connection'] is None and message_on_error:
            my_output.error('CephConnection crd failed')

    response['ceph_cosi_driver'] = None
    if 'CephCOSIDriver' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephCOSIDriver')
        
        response['ceph_cosi_driver'] = k8s_handler.get_ceph_cosi_drivers(cache_enabled=cache_enabled)
        if response['ceph_cosi_driver'] is None and message_on_error:
            my_output.error('CephCOSIDriver crd failed')

    response['ceph_driver'] = None
    if 'Driver' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- Driver')
        
        response['ceph_driver'] = k8s_handler.get_ceph_drivers(
            cache_enabled=cache_enabled
        )
        if response['ceph_driver'] is None and message_on_error:
            my_output.error('Driver crd failed')

    response['ceph_filesystem'] = None
    if 'CephFilesystem' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephFilesystem')

        response['ceph_filesystem'] = k8s_handler.get_ceph_filesystems(
            cache_enabled=cache_enabled
        )
        if response['ceph_filesystem'] is None and message_on_error:
            my_output.error('CephFilesystem crd failed')

    response['ceph_filesystem_mirror'] = None
    if 'CephFilesystemMirror' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephFilesystemMirror')

        response['ceph_filesystem_mirror'] = k8s_handler.get_ceph_filesystem_mirrors(
            cache_enabled=cache_enabled
        )
        if response['ceph_filesystem_mirror'] is None and message_on_error:
            my_output.error('CephFilesystemMirror crd failed')

    response['ceph_filesystem_subvolume_group'] = None
    if 'CephFilesystemSubVolumeGroup' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephFilesystemSubVolumeGroup')

        response['ceph_filesystem_subvolume_group'] = k8s_handler.get_ceph_filesystem_subvolume_groups(
            cache_enabled=cache_enabled
        )
        if response['ceph_filesystem_subvolume_group'] is None and message_on_error:
            my_output.error('CephFilesystemSubVolumeGroup crd failed')

    response['ceph_nfs'] = None
    if 'CephNFS' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephNFS')

        response['ceph_nfs'] = k8s_handler.get_ceph_nfses(
            cache_enabled=cache_enabled
        )
        if response['ceph_nfs'] is None and message_on_error:
            my_output.error('CephNFS crd failed')

    response['ceph_object_realm'] = None
    if 'CephObjectRealm' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephObjectRealm')

        response['ceph_object_realm'] = k8s_handler.get_ceph_object_realms(
            cache_enabled=cache_enabled
        )
        if response['ceph_object_realm'] is None and message_on_error:
            my_output.error('CephObjectRealm crd failed')

    response['ceph_object_store'] = None
    if 'CephObjectStore' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephObjectStore')
        
        response['ceph_object_store'] = k8s_handler.get_ceph_object_stores(
            cache_enabled=cache_enabled
        )
        if response['ceph_object_store'] is None and message_on_error:
            my_output.error('CephObjectStore crd failed')

    response['ceph_object_store_user'] = None
    if 'CephObjectStoreUser' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephObjectStoreUser')
        
        response['ceph_object_store_user'] = k8s_handler.get_ceph_object_store_users(
            cache_enabled=cache_enabled
        )
        if response['ceph_object_store_user'] is None and message_on_error:
            my_output.error('CephObjectStoreUser crd failed')

    response['ceph_object_zone'] = None
    if 'CephObjectZone' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephObjectZone')
        
        response['ceph_object_zone'] = k8s_handler.get_ceph_object_zones(
            cache_enabled=cache_enabled
        )
        if response['ceph_object_zone'] is None and message_on_error:
            my_output.error('CephObjectZone crd failed')

    response['ceph_object_zone_group'] = None
    if 'CephObjectZoneGroup' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephObjectZoneGroup')
        
        response['ceph_object_zone_group'] = k8s_handler.get_ceph_object_zone_groups(
            cache_enabled=cache_enabled
        )
        if response['ceph_object_zone_group'] is None and message_on_error:
            my_output.error('CephObjectZoneGroup crd failed')

    response['ceph_operator_config'] = None
    if 'OperatorConfig' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- OperatorConfig')
        
        response['ceph_operator_config'] = k8s_handler.get_ceph_operator_configs(
            cache_enabled=cache_enabled
        )
        if response['ceph_operator_config'] is None and message_on_error:
            my_output.error('OperatorConfig crd failed')

    response['ceph_rdb_mirror'] = None
    if 'CephRBDMirror' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- CephRBDMirror')
        
        response['ceph_rdb_mirror'] = k8s_handler.get_ceph_rdb_mirrors(
            cache_enabled=cache_enabled
        )
        if response['ceph_rdb_mirror'] is None and message_on_error:
            my_output.error('CephRBDMirror crd failed')

    response['storage_system'] = None
    if 'StorageSystem' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageSystem')
        
        response['storage_system'] = k8s_handler.get_storage_systems(
            cache_enabled=cache_enabled
        )
        if response['storage_system'] is None and message_on_error:
            my_output.error('StorageSystem crd failed')

    response['ocs_initialization'] = None
    if 'OCSInitialization' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- OCSInitialization')

        response['ocs_initialization'] = k8s_handler.get_ocs_initializations(
            cache_enabled=cache_enabled
        )

        if response['ocs_initialization'] is None and message_on_error:
            my_output.error('OCSInitialization crd failed')

    response['storage_claim'] = None
    if 'StorageClaim' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageClaim')

        response['storage_claim'] = k8s_handler.get_storage_claims(
            cache_enabled=cache_enabled
        )
        if response['storage_claim'] is None and message_on_error:
            my_output.error('StorageClaim crd failed')

    response['storage_client'] = None
    if 'StorageClient' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageClient')

        response['storage_client'] = k8s_handler.get_storage_clients(
            cache_enabled=cache_enabled
        )
        if response['storage_client'] is None and message_on_error:
            my_output.error('StorageClient crd failed')

    response['storage_cluster'] = None
    if 'StorageCluster' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageCluster')

        response['storage_cluster'] = k8s_handler.get_storage_clusters(
            cache_enabled=cache_enabled
        )
        if response['storage_cluster'] is None and message_on_error:
            my_output.error('StorageCluster crd failed')

    response['storage_cluster_peer'] = None
    if 'StorageClusterPeer' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageClusterPeer')
        
        response['storage_cluster_peer'] = k8s_handler.get_storage_cluster_peers(
            cache_enabled=cache_enabled
        )
        if response['storage_cluster_peer'] is None and message_on_error:
            my_output.error('StorageClusterPeer crd failed')

    response['storage_consumer'] = None
    if 'StorageConsumer' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageConsumer')
        
        response['storage_consumer'] = k8s_handler.get_storage_consumers(
            cache_enabled=cache_enabled
        )
        if response['storage_consumer'] is None and message_on_error:
            my_output.error('StorageConsumer crd failed')

    response['storage_request'] = None
    if 'StorageRequest' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- StorageRequest')
        
        response['storage_request'] = k8s_handler.get_storage_requests(
            cache_enabled=cache_enabled
        )
        if response['storage_request'] is None and message_on_error:
            my_output.error('StorageRequest crd failed')

    response['pv'] = None
    if 'PersistentVolume' in crd or '__all__' in crd:
        try:
            local_storage_sc = response['storage_cluster'][0]['local_storage_sc']
        except BaseException:
            local_storage_sc = None

        if local_storage_sc is not None:
            if my_output is not None:
                my_output.default('- PV')

            response['pv'] = k8s_handler.get_pvs(
                object_filter=['sc:%s' % (local_storage_sc)],
                cache_enabled=cache_enabled
            )

    response['pvc'] = None
    if 'PersistentVolumeClaim' in crd or '__all__' in crd:
        try:
            local_storage_sc = response['storage_cluster'][0]['local_storage_sc']
        except BaseException:
            local_storage_sc = None

        if local_storage_sc is not None:
            if my_output is not None:
                my_output.default('- PVC')

            response['pvc'] = k8s_handler.get_pvcs(
                object_filter=['sc:%s' % (local_storage_sc)],
                usage_info=True, 
                cache_enabled=cache_enabled
            )

    response['job'] = None
    if 'Job' in crd or '__all__' in crd:
        if my_output is not None:
            my_output.default('- Job')
        
        response['job'] = k8s_handler.get_jobs(
            object_filter=['namespace:openshift-storage']
        )

    return response


def print_odf_crd(crds, k8s_output_handler, only_non_zero=True, crd=['__all__']):
    if 'StorageSystem' in crd or '__all__' in crd:
        if crds['storage_system'] is not None:
            if not only_non_zero or len(crds['storage_system']) > 0:
                k8s_output_handler.print_storage_systems(
                    crds['storage_system']
                )

    if 'StorageCluster' in crd or '__all__' in crd:
        if crds['storage_cluster'] is not None:
            if not only_non_zero or len(crds['storage_cluster']) > 0:
                k8s_output_handler.print_storage_clusters(
                    crds['storage_cluster']
                )

    if 'OCSInitialization' in crd or '__all__' in crd:
        if crds['ocs_initialization'] is not None:
            if not only_non_zero or len(crds['ocs_initialization']) > 0:
                k8s_output_handler.print_ocs_initializations(
                    crds['ocs_initialization']
                )

    if 'StorageClaim' in crd or '__all__' in crd:
        if crds['storage_claim'] is not None:
            if not only_non_zero or len(crds['storage_claim']) > 0:
                k8s_output_handler.print_storage_claims(
                    crds['storage_claim']
                )

    if 'StorageClient' in crd or '__all__' in crd:
        if crds['storage_client'] is not None:
            if not only_non_zero or len(crds['storage_client']) > 0:
                k8s_output_handler.print_storage_clients(
                    crds['storage_client']
                )

    if 'StorageClusterPeer' in crd or '__all__' in crd:
        if crds['storage_cluster_peer'] is not None:
            if not only_non_zero or len(crds['storage_cluster_peer']) > 0:
                k8s_output_handler.print_storage_cluster_peers(
                    crds['storage_cluster_peer']
                )

    if 'StorageConsumer' in crd or '__all__' in crd:
        if crds['storage_consumer'] is not None:
            if not only_non_zero or len(crds['storage_consumer']) > 0:
                k8s_output_handler.print_storage_consumers(
                    crds['storage_consumer']
                )

    if 'StorageRequest' in crd or '__all__' in crd:
        if crds['storage_request'] is not None:
            if not only_non_zero or len(crds['storage_request']) > 0:
                k8s_output_handler.print_storage_requests(
                    crds['storage_request']
                )

    if 'CephCluster' in crd or '__all__' in crd:
        if crds['ceph_cluster'] is not None:
            if not only_non_zero or len(crds['ceph_cluster']) > 0:
                k8s_output_handler.print_ceph_clusters(
                    crds['ceph_cluster']
                )

    if 'CephBlockPool' in crd or '__all__' in crd:
        if crds['ceph_block_pool'] is not None:
            if not only_non_zero or len(crds['ceph_block_pool']) > 0:
                k8s_output_handler.print_ceph_block_pools(
                    crds['ceph_block_pool']
                )

    if 'CephBlockPoolRadosNamespace' in crd or '__all__' in crd:
        if crds['ceph_block_pool_rados_namespace'] is not None:
            if not only_non_zero or len(crds['ceph_block_pool_rados_namespace']) > 0:
                k8s_output_handler.print_ceph_block_pool_rados_namespaces(
                    crds['ceph_block_pool_rados_namespace']
                )

    if 'CephBucketNotification' in crd or '__all__' in crd:
        if crds['ceph_bucket_notification'] is not None:
            if not only_non_zero or len(crds['ceph_bucket_notification']) > 0:
                k8s_output_handler.print_ceph_bucket_notifications(
                    crds['ceph_bucket_notification']
                )

    if 'CephBucketTopic' in crd or '__all__' in crd:
        if crds['ceph_bucket_topic'] is not None:
            if not only_non_zero or len(crds['ceph_bucket_topic']) > 0:
                k8s_output_handler.print_ceph_bucket_topics(
                    crds['ceph_bucket_topic']
                )

    if 'CephClient' in crd or '__all__' in crd:
        if crds['ceph_client'] is not None:
            if not only_non_zero or len(crds['ceph_client']) > 0:
                k8s_output_handler.print_ceph_clients(
                    crds['ceph_client']
                )

    if 'ClientProfile' in crd or '__all__' in crd:
        if crds['ceph_client_profile'] is not None:
            if not only_non_zero or len(crds['ceph_client_profile']) > 0:
                k8s_output_handler.print_ceph_client_profiles(
                    crds['ceph_client_profile']
                )

    if 'ClientProfileMapping' in crd or '__all__' in crd:
        if crds['ceph_client_profile_mapping'] is not None:
            if not only_non_zero or len(crds['ceph_client_profile_mapping']) > 0:
                k8s_output_handler.print_ceph_client_profile_mappings(
                    crds['ceph_client_profile_mapping']
                )

    if 'CephConnection' in crd or '__all__' in crd:
        if crds['ceph_connection'] is not None:
            if not only_non_zero or len(crds['ceph_connection']) > 0:
                k8s_output_handler.print_ceph_connections(
                    crds['ceph_connection']
                )

    if 'CephCOSIDriver' in crd or '__all__' in crd:
        if crds['ceph_cosi_driver'] is not None:
            if not only_non_zero or len(crds['ceph_cosi_driver']) > 0:
                k8s_output_handler.print_ceph_cosi_drivers(
                    crds['ceph_cosi_driver']
                )

    if 'Driver' in crd or '__all__' in crd:
        if crds['ceph_driver'] is not None:
            if not only_non_zero or len(crds['ceph_driver']) > 0:
                k8s_output_handler.print_ceph_drivers(
                    crds['ceph_driver']
                )

    if 'CephFilesystem' in crd or '__all__' in crd:
        if crds['ceph_filesystem'] is not None:
            if not only_non_zero or len(crds['ceph_filesystem']) > 0:
                k8s_output_handler.print_ceph_filesystems(
                    crds['ceph_filesystem']
                )

    if 'CephFilesystemMirror' in crd or '__all__' in crd:
        if crds['ceph_filesystem_mirror'] is not None:
            if not only_non_zero or len(crds['ceph_filesystem_mirror']) > 0:
                k8s_output_handler.print_ceph_filesystem_mirrors(
                    crds['ceph_filesystem_mirror']
                )

    if 'CephFilesystemSubVolumeGroup' in crd or '__all__' in crd:
        if crds['ceph_filesystem_subvolume_group'] is not None:
            if not only_non_zero or len(crds['ceph_filesystem_subvolume_group']) > 0:
                k8s_output_handler.print_ceph_filesystem_subvolume_groups(
                    crds['ceph_filesystem_subvolume_group']
                )

    if 'CephNFS' in crd or '__all__' in crd:
        if crds['ceph_nfs'] is not None:
            if not only_non_zero or len(crds['ceph_nfs']) > 0:
                k8s_output_handler.print_ceph_nfses(
                    crds['ceph_nfs']
                )

    if 'CephObjectRealm' in crd or '__all__' in crd:
        if crds['ceph_object_realm'] is not None:
            if not only_non_zero or len(crds['ceph_object_realm']) > 0:
                k8s_output_handler.print_ceph_object_realms(
                    crds['ceph_object_realm']
                )

    if 'CephObjectStore' in crd or '__all__' in crd:
        if crds['ceph_object_store'] is not None:
            if not only_non_zero or len(crds['ceph_object_store']) > 0:
                k8s_output_handler.print_ceph_object_stores(
                    crds['ceph_object_store']
                )

    if 'CephObjectStoreUser' in crd or '__all__' in crd:
        if crds['ceph_object_store_user'] is not None:
            if not only_non_zero or len(crds['ceph_object_store_user']) > 0:
                k8s_output_handler.print_ceph_object_store_users(
                    crds['ceph_object_store_user']
                )

    if 'CephObjectZone' in crd or '__all__' in crd:
        if crds['ceph_object_zone'] is not None:
            if not only_non_zero or len(crds['ceph_object_zone']) > 0:
                k8s_output_handler.print_ceph_object_zones(
                    crds['ceph_object_zone']
                )

    if 'CephObjectZoneGroup' in crd or '__all__' in crd:
        if crds['ceph_object_zone_group'] is not None:
            if not only_non_zero or len(crds['ceph_object_zone_group']) > 0:
                k8s_output_handler.print_ceph_object_zone_groups(
                    crds['ceph_object_zone_group']
                )

    if 'OperatorConfig' in crd or '__all__' in crd:
        if crds['ceph_operator_config'] is not None:
            if not only_non_zero or len(crds['ceph_operator_config']) > 0:
                k8s_output_handler.print_ceph_operator_configs(
                    crds['ceph_operator_config']
                )

    if 'CephRBDMirror' in crd or '__all__' in crd:
        if crds['ceph_rdb_mirror'] is not None:
            if not only_non_zero or len(crds['ceph_rdb_mirror']) > 0:
                k8s_output_handler.print_ceph_rdb_mirrors(
                    crds['ceph_rdb_mirror']
                )

    if 'Job' in crd or '__all__' in crd:
        if crds['job'] is not None:
            if not only_non_zero or len(crds['job']) > 0:
                k8s_output_handler.print_jobs(
                    crds['job']
                )

    if 'PersistentVolume' in crd or '__all__' in crd:
        if crds['pv'] is not None:
            if not only_non_zero or len(crds['pv']) > 0:
                k8s_output_handler.print_pvs(
                    crds['pv']
                )

    if 'PersistentVolumeClaim' in crd or '__all__' in crd:
        if crds['pvc'] is not None:
            if not only_non_zero or len(crds['pvc']) > 0:
                k8s_output_handler.print_pvcs(crds['pvc'])
