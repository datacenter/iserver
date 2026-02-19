from lib.workflow.ocp_nmstate_operator import operator_create
from lib.workflow.ocp_nmstate_operator import enable_lldp
from lib.workflow.ocp_nmstate_operator import operator_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        task['operator'] = dict(enabled=False)    
        if not isinstance(task['operator'], dict):
            return None, 'nmstate.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error
    
    if 'lldp' in task:
        if not isinstance(task['lldp'], dict):
            return None, 'nmstate.lldp dict required'

        task['lldp']['cluster'] = cluster_name
        task['lldp']['confirmation'] = confirmation
        task['lldp']['settings'] = dict(enable=True)
        if 'fw' in task['lldp']:
            task['lldp']['settings']['nic-fw-disable'] = task['lldp']['fw']
        if 'keep-nncp' in task['lldp']:
            task['lldp']['settings']['delete-nncp'] = not task['lldp']['keep-nncp']
        if 'skip-down' in task['lldp']:
            task['lldp']['settings']['include-down'] = not task['lldp']['skip-down']

        task['lldp'], error = enable_lldp.validate(task['lldp'])
        if error is not None:
            return None, error
        
    new_task = {}
    allowed_keys = [
        'operator',
        'lldp'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for nmstate task'
    
    return new_task, None


def run(params, log_id=None):
    if 'operator' in params:
        success = operator_create.run(params['operator'], log_id=log_id)
        if not success:
            return False
        
    if 'lldp' in params:
        success = enable_lldp.run(params['lldp'], log_id=log_id)
        if not success:
            return False
    
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        task['operator'] = dict(enabled=False)    
        if not isinstance(task['operator'], dict):
            return None, 'nmstate.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error
    
    new_task = {}
    allowed_keys = [
        'operator'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for nmstate task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'operator' in params:
        success = operator_delete.run(params['operator'], log_id=log_id)
        if not success:
            return False
        
    return True
