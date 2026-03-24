import copy
import importlib
from lib import filter_helper


def get_function_map():
    fmap = {}
    fmap['config-map'] = 'cm'
    fmap['data-volume'] = 'dv'
    fmap['lb-ip-pool'] = 'lb_ip_pool'
    fmap['namespace'] = 'namespace'
    fmap['nad'] = 'nad'
    fmap['pod'] = 'pod'
    fmap['service'] = 'service'
    fmap['ovn-udn'] = 'ovn_udn'
    fmap['virtual-machine'] = 'vm'
    return fmap


def get_task_ids(task):
    tasks_mo = filter_helper.get(task, '__id__')
    if tasks_mo is None:
        return [None]
    
    if isinstance(tasks_mo, int):
        return [tasks_mo]
    
    if len(tasks_mo.split('-')) != 2:
        return None
    
    try:
        (min_value, max_value) = tasks_mo.split('-')
        min_value = int(min_value)
        max_value = int(max_value)

        tasks = []
        for index in range(min_value, max_value+1):
            tasks.append(index)
    except:
        return None
    
    return tasks


def validate(operation, task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    fmap = get_function_map()
    tasks_id = get_task_ids(task)
    if tasks_id is None:
        return None, 'k8s.__id__ invalid'
    namespace = filter_helper.get(task, 'namespace')

    if 'items' in task:
        if not isinstance(task['items'], list):
            return None, 'k8s.items list required'

        items = []
        for item in task['items']:
            item_type = filter_helper.get(item, '__type__')
            if item_type not in fmap:
                return None, 'Unsupported type: %s' % (item_type)

            done_once = False
            for task_id in tasks_id:
                if not filter_helper.get(item, '__enabled__', on_error=True, on_none=True):
                    continue

                if operation == 'create' and filter_helper.get(item, '__no_create__', on_error=False, on_none=False):
                    continue
                
                if operation == 'delete' and filter_helper.get(item, '__no_delete__', on_error=False, on_none=False):
                    continue

                new_item = copy.deepcopy(item)
                if task_id is not None and '${__id__}' not in item['name']:
                    new_item['__id__'] = None
                    if done_once:
                        continue
                else:
                    new_item['__id__'] = task_id

                new_item['cluster'] = cluster_name
                new_item['confirmation'] = confirmation
                new_item['base_directory'] = cluster_settings['directory']
                
                if namespace is not None and 'namespace' not in new_item:
                    new_item['namespace'] = namespace

                fmodule = importlib.import_module('lib.workflow.k8s.%s_%s' % (fmap[item_type], operation))
                new_item, error = getattr(fmodule, 'validate')(new_item)                            
                if error is not None:
                    return None, error
            
                items.append(new_item)
                done_once = True

        task['items'] = copy.deepcopy(items)

    new_task = {}
    allowed_keys = [
        '__id__',
        'items'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for k8s task'
    
    return new_task, None


def execute(operation, params, log_id=None):
    fmap = get_function_map()
    if 'items' in params:
        if operation == 'delete':
            items = reversed(params['items'])
        else:
            items = params['items']

        for item in items:
            item_type = filter_helper.get(item, '__type__')

            if not filter_helper.get(item, '__enabled__', on_error=True, on_none=True):
                continue

            if operation == 'create' and filter_helper.get(item, '__no_create__', on_error=False, on_none=False):
                continue
            
            if operation == 'delete' and filter_helper.get(item, '__no_delete__', on_error=False, on_none=False):
                continue

            fmodule = importlib.import_module('lib.workflow.k8s.%s_%s' % (fmap[item_type], operation))
            success = getattr(fmodule, 'run')(item, log_id=log_id)
            if not success:
                return False
            
    return True


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    return validate(
        'create', 
        task, 
        cluster_name, 
        confirmation, 
        cluster_settings=cluster_settings, 
        k8s_handler=k8s_handler
    )


def run(params, log_id=None):
    return execute('create', params, log_id=log_id)


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    return validate(
        'delete', 
        task, 
        cluster_name, 
        confirmation, 
        cluster_settings=cluster_settings, 
        k8s_handler=k8s_handler
    )


def delete(params, log_id=None):
    return execute('delete', params, log_id=log_id)
