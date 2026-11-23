from lib.workflow import ocp_common
from lib import output_helper
from lib.linux import output as linux_output
from lib.workflow.ocp_lvm_operator import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Orphan Logical Volumes')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    if not local_common.is_lvm_ready(params, my_output, check_lvm_cluster=True, instance_required=True, ready_required=False):
        return False

    lvs = local_common.get_linux_lv(
        params['cluster'], 
        params['k8s_handler'], 
        my_output, 
        log_id=log_id, 
        include_snap=True
    )
    
    is_orphan = False
    for node_name in lvs:
        if lvs[node_name] is None:
            my_output.error('Unexpected no logical volume for node [%s]' % (node_name))
            return False
        
        linux_output_handler.print_linux_lv(
            lvs[node_name],
            title=True,
            server=node_name
        )
    
        for item in lvs[node_name]:
            if item['orphan']:
                is_orphan = True
        
    if not is_orphan:
        my_output.default('No orphan logical volumes found')
        return True

    my_output.default('Orphans to be deleted', before_newline=True)
    for node_name in lvs:
        for item in lvs[node_name]:
            if item['orphan']:
                my_output.default('- node [%s] lv [%s]' % (node_name, item['lv_path']))

    if params['confirmation']:
        if not get_confirmation():
            return True

    my_output.default('Delete orphans', before_newline=True)
    linux_handlers = ocp_common.get_nodes_linux_handler(
        params['cluster'],
        params['k8s_handler'],
        log_id=log_id
    )
    for node_name in lvs:
        for item in lvs[node_name]:
            if item['orphan']:
                my_output.default('- node [%s] lv [%s]' % (node_name, item['lv_path']))
                success, output = linux_handlers[node_name].delete_lv_cmd(item['lv_path'])
                if not success:
                    my_output.error(output)
                else:
                    my_output.default(output)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Linux logical volumes not backed by PVC/PV or Volume Snapshot (aka orphans) deleted')

    return True