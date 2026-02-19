import yaml
from lib.k8s import output as k8s_output
from lib.linux import output as linux_output
from lib import output_helper
from lib.workflow.ocp_lvm_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'ssh-required' not in params:
        params['ssh-required'] = True

    if not isinstance(params['ssh-required'], bool):
        return None, 'ssh-required params must be true or false'
    
    if 'test-namespace' not in params:
        params['test-namespace'] = 'test-lvm'

    if 'cleanup' not in params:
        params['cleanup'] = True

    if not isinstance(params['cleanup'], bool):
        return None, 'cleanup params must be true or false'

    if 'cleanup-on-error' not in params:
        params['cleanup-on-error'] = False

    if not isinstance(params['cleanup-on-error'], bool):
        return None, 'cleanup-on-error params must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    return params, None


def prepare_namespace(name, k8s_handler, my_output):
    my_output.default('- namespace: %s' % (name))

    if k8s_handler.is_namespace(name, cache_enabled=False):
        my_output.error('Namespace already exists')
        return False
    
    my_output.default('- namespace does not exist')

    success = k8s_handler.create_namespace(
        name,
        my_output=my_output, 
        wait=True
    )
    if not success:
        my_output.error('Namespace create failed')
        return False
    
    my_output.default('- namespace created')
    return True


def prepare_pvc(namespace, k8s_handler, my_output):
    node_names = k8s_handler.get_worker_nodes_name()
    if node_names is None:
        my_output.error('Failed to get node names')
        return False
    
    storage_class = k8s_handler.get_storage_class_lvm()
    if storage_class is None:
        my_output.error('Failed to get lvm storage class name')
        return False

    for node_name in node_names:
        success = k8s_handler.create_pvc(
            namespace,
            node_name,
            'Block',
            storage_class['name'],
            '1Gi',
            '2Gi',
            confirmation=False,
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
    return True


def prepare_pod(namespace, k8s_handler, my_output):
    node_names = k8s_handler.get_worker_nodes_name()
    if node_names is None:
        my_output.error('Failed to get node names')
        return False
    
    for node_name in node_names:
        body = k8s_handler.get_pod_block_volume_definition(namespace, node_name, node_name, node_name=node_name)
        my_output.default(yaml.dump(body), wrap='~~~')
        
        if not k8s_handler.create_resource(body):
            my_output.error('Pod create failed')
            return False
        
        my_output.default('- pod [%s/%s] created' % (namespace, node_name))
        my_output.default('- wait for pod running [timeout:600s]...')
        if not k8s_handler.wait_pod_phase(namespace, node_name, ['Running'], max_time=600):
            my_output.error('Pod has not reached desired state')
            return False

        my_output.default('- wait for pvc [%s/%s] bound [timeout:60s]...'  % (namespace, node_name))
        if not k8s_handler.wait_pvc_phase(namespace, node_name, ['Bound'], max_time=60):
            my_output.error('PVC has not reached desired state')
            return False
                
    return True


def prepare_snapshot(namespace, k8s_handler, my_output):
    node_names = k8s_handler.get_worker_nodes_name()
    if node_names is None:
        my_output.error('Failed to get node names')
        return False
    
    storage_class = k8s_handler.get_storage_class_lvm()
    if storage_class is None:
        my_output.error('Failed to get lvm storage class name')
        return False

    for node_name in node_names:
        pvc_name = node_name
        snapshot_name = '%s-snap' % (pvc_name)
        body = k8s_handler.get_volume_snapshot_definition(namespace, snapshot_name, storage_class['name'], pvc_name=pvc_name)
        my_output.default(yaml.dump(body), wrap='~~~')
        if not k8s_handler.create_volume_snapshot(body):
            my_output.error('Volume snapshot create failed')
            return False
        
        my_output.default('- volume snapshot [%s/%s] created' % (namespace, snapshot_name))
        
    return True


def check_consistency(cluster_name, namespace, k8s_handler, k8s_output_handler, linux_output_handler, my_output, log_id):
    pods = k8s_handler.get_pods(
        object_filter=['namespace:%s' % (namespace)],
        cache_enabled=False
    )
    if pods is None or len(pods) == 0:
        my_output.error('Unexpected no pods found in namespace: %s' % (namespace))
        return False

    my_output.default('PODs', underline=True, before_newline=True)
    k8s_output_handler.print_pods_state(pods)

    pvcs = k8s_handler.get_pvcs(
        object_filter=['namespace:%s' % (namespace)],
        usage_info=True,
        cache_enabled=False
    )

    if pvcs is None or len(pvcs) == 0:
        my_output.error('Unexpected no pvcs found in namespace: %s' % (namespace))
        return False
    
    my_output.default('Persistent Volume Claims', underline=True, before_newline=True)
    k8s_output_handler.print_pvcs(pvcs)

    pvcs_list = []
    for pvc in pvcs:
        pvcs_list.append(pvc['namespace_name'])
    
    pvs = k8s_handler.get_pvs(
        object_filter=['pvcs:%s' % (','.join(pvcs_list))],
        cache_enabled=False
    )

    if pvs is None:
        my_output.error('Unexpected failure in pv get')
        return False
    
    k8s_output_handler.print_pvs(pvs)

    if len(pvs) != len(pvcs):
        my_output.error('Unexpected pvs and pv count not equal')
        return False

    snapshots = k8s_handler.get_volume_snapshots(
        object_filter=['pvcs:%s' % (','.join(pvcs_list))],
        cache_enabled=False
    )

    if snapshots is None:
        my_output.error('Unexpected failure in volume snapshots get')
        return False
    
    my_output.default('Volume Snapshots', underline=True, before_newline=True)
    k8s_output_handler.print_volume_snapshots(snapshots, title=False)

    if len(snapshots) != len(pvcs):
        my_output.error('Unexpected pvs and snapshots count not equal')
        return False
        
    pv_list = []
    for pv in pvs:
        pv_list.append(pv['name'])

    topo_lvs = k8s_handler.get_logical_volumes(
        object_filter=['names:%s' % (','.join(pv_list))],
        cache_enabled=False
    )

    if topo_lvs is None:
        my_output.error('Unexpected failure in logical volume get')
        return False
    
    my_output.default('Logical Volumes (TopoLVM)', underline=True, before_newline=True)
    k8s_output_handler.print_logical_volumes(topo_lvs, title=False)

    if len(pvs) != len(topo_lvs):
        my_output.error('Unexpected pv and topolvm logical volume count not equal')
        return False
        
    lv_names = []
    for item in pvs:
        lv_names.append(item['csi_handle'])

    lvs = local_common.get_linux_lv(cluster_name, k8s_handler, my_output, log_id=log_id, lv_names=lv_names, include_snap=True)
    if lvs is None:
        my_output.error('Unexpected failure in linux logical volume state collection')
        return False
    
    for node_name in lvs:
        linux_output_handler.print_linux_lv(
            lvs[node_name],
            title=True,
            server=node_name
        )

    my_output.default('Consistency Checks', underline=True, before_newline=True)
    for pvc in pvcs:
        my_output.default('- pvc: %s [node:%s]' % (pvc['namespace_name'], pvc['selected_node']))
        csi_handle = None
        pv_name = None
        for pv in pvs:
            if pv['pvc_namespace'] == pvc['namespace'] and pv['pvc_name'] == pvc['name']:
                csi_handle = pv['csi_handle']
                pv_name = pv['name']
                my_output.default('- pv found: [name:%s] [csi handle:%s]' % (pv_name, csi_handle))

        if csi_handle is None:
            my_output.error('PV not found')
            return False

        for topo_lv in topo_lvs:
            if topo_lv['name'] == pv_name:
                my_output.default('- topolvm logical volume found: [name:%s] [volume:%s] with csi handle match' % (pv_name, topo_lv['info']['volume_id']))
                if topo_lv['info']['volume_id'] != csi_handle:
                    my_output.error('Unexpected mismatch in volume ids: [pv csi handle:%s] vs [topolvm volume: %s]' % (csi_handle, topo_lv['info']['volume_id']))
                    return False

        if pvc['selected_node'] not in lvs:
            my_output.error('Unexpected pvc node: %s' % (pvc['selected_node']))
            return False
        
        lv_uuid = None
        if csi_handle is not None:
            for lv in lvs[pvc['selected_node']]:
                if lv['lv_name'] == csi_handle:
                    lv_uuid = lv['lv_uuid']

        if lv_uuid is None:
            my_output.error('Logical Volume not found')
            return False
        
        my_output.default('- lv found: [node:%s] [name:%s] [uuid:%s]' % (pvc['selected_node'], csi_handle, lv_uuid))

    return True


def prepare(cluster_name, namespace, k8s_handler, k8s_output_handler, linux_output_handler, my_output, log_id):
    my_output.default('Prepare test resources')

    if not prepare_namespace(namespace, k8s_handler, my_output):
        return False
    
    if not prepare_pvc(namespace, k8s_handler, my_output):
        return False
    
    if not prepare_pod(namespace, k8s_handler, my_output):
        return False

    if not prepare_snapshot(namespace, k8s_handler, my_output):
        return False

    if not check_consistency(cluster_name, namespace, k8s_handler, k8s_output_handler, linux_output_handler, my_output, log_id):
        return False
    
    return True


def cleanup_namespace(name, k8s_handler, my_output):
    if not k8s_handler.is_namespace(name, cache_enabled=False):
        my_output.default('- namespace does not exist: %s' % (name))
        return True
    
    success = k8s_handler.delete_namespace_mo(name)
    if not success:
        my_output.error('Namespace delete failed: %s' % (name))
        return False
    
    my_output.default('- namespace deleted: %s' % (name))
    return True


def cleanup_snapshot(namespace, k8s_handler, my_output):
    snapshots = k8s_handler.get_volume_snapshots(
        object_filter=['namespace:%s' % (namespace)]
    )
    if snapshots is None:
        my_output.error('Failed to get volume snapshots information')
        return False
    
    if len(snapshots) == 0:
        my_output.default('- no snapshots found in namespace: %s' % (namespace))
        return True
    
    for snapshot in snapshots:
        my_output.default('- delete snapshot %s' % (snapshot['namespace_name']))
        if not k8s_handler.delete_volume_snapshot(snapshot['namespace'], snapshot['name']):
            my_output.error('Volume snapshot delete failed')
            return False
        
        my_output.default('- volume snapshot delete request successful')
        my_output.default('- wait for no snapshot...')
        if not k8s_handler.wait_no_volume_snapshot(snapshot['namespace'], snapshot['name']):
            my_output.error('Volume snapshot still there')
            return False
            
        
    my_output.default('- all snapshots deleted')
    return True


def cleanup_pvc(namespace, k8s_handler, my_output):
    pvcs = k8s_handler.get_pvcs(
        object_filter=['namespace:%s' % (namespace)]
    )
    if pvcs is None:
        my_output.error('Failed to get pvc information')
        return False
    
    if len(pvcs) == 0:
        my_output.default('- no pvcs found in namespace: %s' % (namespace))
        return True
    
    for pvc in pvcs:
        my_output.default('- delete pvc %s' % (pvc['namespace_name']))
        if not k8s_handler.delete_pvc_mo(pvc['namespace'], pvc['name']):
            my_output.error('PVC delete failed')
            return False
        
        my_output.default('- pvc delete request successful')
        my_output.default('- wait for no pvc...')
        if not k8s_handler.wait_no_pvc(pvc['namespace'], pvc['name']):
            my_output.error('PVC still there')
            return False
        
    my_output.default('- all pvcs deleted')
    return True


def cleanup_pod(namespace, k8s_handler, my_output):
    pods = k8s_handler.get_pods(
        object_filter=['namespace:%s' % (namespace)]
    )
    if pods is None:
        my_output.error('Failed to get pod information')
        return False
    
    if len(pods) == 0:
        my_output.default('- no pods found in namespace: %s' % (namespace))
        return True
    
    for pod in pods:
        my_output.default('- delete pod %s' % (pod['namespace_name']))
        if not k8s_handler.delete_pod_mo(pod['namespace'], pod['name']):
            my_output.error('PVC delete failed')
            return False
        
        my_output.default('- pod delete request successful')
        my_output.default('- wait for no pod...')
        if not k8s_handler.wait_no_pod(pod['namespace'], pod['name']):
            my_output.error('PVC still there')
            return False
        
    my_output.default('- all pods deleted')
    return True


def cleanup(name, k8s_handler, my_output):
    my_output.default('Delete test resources', before_newline=True)

    if not cleanup_pod(name, k8s_handler, my_output):
        my_output.error('Pod cleanup failed')
        return False
    
    if not cleanup_snapshot(name, k8s_handler, my_output):
        my_output.error('Volume snapshot cleanup failed')
        return False
    
    if not cleanup_pvc(name, k8s_handler, my_output):
        my_output.error('PVC cleanup failed')
        return False
    
    if not cleanup_namespace(name, k8s_handler, my_output):
        my_output.error('Namespace cleanup failed')
        return False
    
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LVM Operator - Functional Test', before_newline=True, after_newline=True, double_underline=True) 

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False

    if not local_common.is_lvm_ready(params, my_output):
        return False

    success = prepare(
        params['cluster'], 
        params['test-namespace'], 
        params['k8s_handler'], 
        k8s_output_handler, 
        linux_output_handler, 
        my_output, 
        log_id
    )
    if not success:
        my_output.error('Test failed')

    if params['cleanup']:
        if not success and not params['cleanup-on-error']:
            if params['confirmation']:
                if not get_confirmation(title='Delete resources?'):
                    return False
            
        if not cleanup(params['test-namespace'], params['k8s_handler'], my_output):
            my_output.error('Test cleanup failed')
            success = False

    return success
