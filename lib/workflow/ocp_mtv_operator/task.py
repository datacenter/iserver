from lib.workflow.ocp_mtv_operator import operator_create
from lib.workflow.ocp_mtv_operator import instance_create
from lib.workflow.ocp_mtv_operator import vcenter_provider_create
from lib.workflow.ocp_mtv_operator import network_map_create
from lib.workflow.ocp_mtv_operator import storage_map_create
from lib.workflow.ocp_mtv_operator import plan_create
from lib.workflow.ocp_mtv_operator import migration_run
from lib.workflow.ocp_mtv_operator import operator_delete
from lib.workflow.ocp_mtv_operator import instance_delete
from lib.workflow.ocp_mtv_operator import provider_delete
from lib.workflow.ocp_mtv_operator import network_map_delete
from lib.workflow.ocp_mtv_operator import storage_map_delete
from lib.workflow.ocp_mtv_operator import plan_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'mtv task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'mtv.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'mtv.instance dict required'
        
        task['instance']['cluster'] = cluster_name
        task['instance']['confirmation'] = confirmation
        task['instance']['base_directory'] = cluster_settings['directory']
        task['instance'], error = instance_create.validate(task['instance'])
        if task['instance'] is None:
            return None, error

    if 'provider' in task:
        if not isinstance(task['provider'], list):
            return None, 'mtv.provider list required'

        for item in task['provider']:
            if not isinstance(item, dict):
                return None, 'mtv.provider list of dict required'

            if 'type' not in item:
                return None, 'mtv.provider.type required'

            if item['type'] not in ['vcenter']:
                return None, 'unsupported mtv.provider.type'
            
    
            if item['type'] == 'vcenter':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = vcenter_provider_create.validate(item)
                if error is not None:
                    return None, error

    if 'map' in task:
        if not isinstance(task['map'], list):
            return None, 'mtv.map list required'

        for item in task['map']:
            if not isinstance(item, dict):
                return None, 'mtv.map list of dict required'

            if 'type' not in item:
                return None, 'mtv.map.type required'

            if item['type'] not in ['network', 'storage']:
                return None, 'unsupported mtv.map.type'
            
            if item['type'] == 'network':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = network_map_create.validate(item)
                if error is not None:
                    return None, error
                    
            if item['type'] == 'storage':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = storage_map_create.validate(item)
                if error is not None:
                    return None, error

    if 'plan' in task:
        if not isinstance(task['plan'], list):
            return None, 'mtv.plan list required'

        for item in task['plan']:
            if not isinstance(item, dict):
                return None, 'mtv.plan list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item, error = plan_create.validate(item)
            if error is not None:
                return None, error

    if 'migration' in task:
        if not isinstance(task['migration'], list):
            return None, 'mtv.migration list required'

        for item in task['migration']:
            if not isinstance(item, dict):
                return None, 'mtv.migration list of dict required'

            if 'action' not in item:
                return None, 'mtv.migration.action required'

            if item['action'] not in ['run']:
                return None, 'unsupported mtv.migration.action'
            
            if item['action'] == 'run':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = migration_run.validate(item)
                if error is not None:
                    return None, error
                                            
    new_task = {}
    allowed_keys = [
        'operator',
        'instance',
        'provider',
        'map',
        'plan',
        'migration'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for mtv task'
    
    return new_task, None


def run(task, log_id=None):
    if 'operator' in task:
        success = operator_create.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False
        
    if 'instance' in task:
        success = instance_create.run(
            task['instance'],
            log_id=log_id
        )
        if not success:
            return False

    if 'provider' in task:
        for item in task['provider']:
            if item['type'] == 'vcenter':
                success = vcenter_provider_create.run(item, log_id=log_id)
                if not success:
                    return False

    if 'map' in task:
        for item in task['map']:
            if item['type'] == 'network':
                success = network_map_create.run(item, log_id=log_id)
                if not success:
                    return False
            
            if item['type'] == 'storage':
                success = storage_map_create.run(item, log_id=log_id)
                if not success:
                    return False
                
    if 'plan' in task:
        for item in task['plan']:
            success = plan_create.run(item, log_id=log_id)
            if not success:
                return False
                            
    if 'migration' in task:
        for item in task['migration']:
            if item['action'] == 'run':
                success = migration_run.run(item, log_id=log_id)
                if not success:
                    return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if not isinstance(task, dict):
        return None, 'mtv task definition in dict format required'
    
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'mtv.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if task['operator'] is None:
            return None, error
        
    if 'instance' in task:
        if not isinstance(task['instance'], dict):
            return None, 'mtv.instance dict required'
        
        task['instance']['cluster'] = cluster_name
        task['instance'], error = instance_delete.validate(task['instance'])
        if task['instance'] is None:
            return None, error

    if 'provider' in task:
        if not isinstance(task['provider'], list):
            return None, 'mtv.provider list required'

        for item in task['provider']:
            if not isinstance(item, dict):
                return None, 'mtv.provider list of dict required'

            if 'type' not in item:
                return None, 'mtv.provider.type required'

            if item['type'] not in ['vcenter']:
                return None, 'unsupported mtv.provider.type'
            
            if item['type'] == 'vcenter':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = provider_delete.validate(item)
                if error is not None:
                    return None, error

    if 'map' in task:
        if not isinstance(task['map'], list):
            return None, 'mtv.map list required'

        for item in task['map']:
            if not isinstance(item, dict):
                return None, 'mtv.map list of dict required'

            if 'type' not in item:
                return None, 'mtv.map.type required'

            if item['type'] not in ['network', 'storage']:
                return None, 'unsupported mtv.map.type'
            
            if item['type'] == 'network':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = network_map_delete.validate(item)
                if error is not None:
                    return None, error
                    
            if item['type'] == 'storage':
                item['cluster'] = cluster_name
                item['confirmation'] = confirmation
                item, error = storage_map_delete.validate(item)
                if error is not None:
                    return None, error

    if 'plan' in task:
        if not isinstance(task['plan'], list):
            return None, 'mtv.plan list required'

        for item in task['plan']:
            if not isinstance(item, dict):
                return None, 'mtv.plan list of dict required'

            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item, error = plan_delete.validate(item)
            if error is not None:
                return None, error

    new_task = {}
    allowed_keys = [
        'operator',
        'instance',
        'provider',
        'map',
        'plan'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for mtv task'
    
    return new_task, None


def delete(task, log_id=None):
    if 'plan' in task:
        for item in task['plan']:
            success = plan_delete.run(item, log_id=log_id)
            if not success:
                return False
                            
    if 'map' in task:
        for item in task['map']:
            if item['type'] == 'network':
                success = network_map_delete.run(item, log_id=log_id)
                if not success:
                    return False
            
            if item['type'] == 'storage':
                success = storage_map_delete.run(item, log_id=log_id)
                if not success:
                    return False

    if 'provider' in task:
        for item in task['provider']:
            if item['type'] == 'vcenter':
                success = provider_delete.run(item, log_id=log_id)
                if not success:
                    return False
                                
    if 'instance' in task:
        success = instance_delete.run(
            task['instance'],
            log_id=log_id
        )
        if not success:
            return False

    if 'operator' in task:
        success = operator_delete.run(
            task['operator'],
            log_id=log_id
        )
        if not success:
            return False        

    return True
