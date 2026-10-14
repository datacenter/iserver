from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    instance_rules = [
        ['name', False, None, 'str', None, None, None, None],
        ['etc-size', True, '10Gi', 'str', None, None, None, None],
        ['etc-sc', True, None, 'str', None, None, None, None],
        ['var-size', True, '100Gi', 'str', None, None, None, None],
        ['var-sc', True, None, 'str', None, None, None, None],
        ['sa', True, 'default', 'str', None, None, None, None],
        ['route', True, True, 'bool', None, None, None, None]
    ]

    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['instance', False, None, 'list-of-dict', 1, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(
        params, 
        rules, 
        extras=['__type__'], 
        nested=dict(instance=instance_rules)
    )
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_deployment(params['__default__']['namespace'], params['__default__']['deployment']):
        my_output.error('Splunk deployment must be running')
        return False

    for instance in params['instance']:
        sc_default = params['k8s_handler'].get_default_storage_class_name()
        sc_fixup = params['k8s_handler'].get_default_storage_class(
            fallback_to_single=True
        )
        if instance['etc-sc'] is None:
            if sc_default is None:
                if sc_fixup is None:
                    my_output.error('No storage class found')
                    return False

                instance['etc-sc'] = sc_fixup['name']

        if instance['var-sc'] is None:
            if sc_default is None:
                if sc_fixup is None:
                    my_output.error('No storage class found')
                    return False

                instance['var-sc'] = sc_fixup['name']

        if params['k8s_handler'].is_splunk_standalone(params['__default__']['namespace'], instance['name']):
            my_output.default('Splunk standalone instance %s already exists' % (instance['name']))
        else:
            success = params['k8s_handler'].create_or_update_service_account_role_binding(
                params['__default__']['namespace'],
                params['__default__']['role-binding-name'],
                params['__default__']['role-binding-name'], 
                params['__default__']['namespace'],
                instance['sa'],
                my_output=my_output, 
                confirmation=params['confirmation']
            )
            if not success:
                return False
                
            success = params['k8s_handler'].create_splunk_standalone(
                params['__default__']['namespace'], 
                instance['name'], 
                pvc_finalizers=params['__default__']['pvc-finalizers'],
                etc_size=instance['etc-size'],
                etc_sc=instance['etc-sc'],
                var_size=instance['var-size'],
                var_sc=instance['var-sc'],
                sa=instance['sa'],
                confirmation=params['confirmation'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False
        
        if not instance['route']:
            success = params['k8s_handler'].delete_splunk_standalone_route(
                params['__default__']['namespace'], 
                instance['name'], 
                confirmation=params['confirmation'], 
                my_output=my_output
            )
            if not success:
                return False

        if instance['route']:
            success = params['k8s_handler'].create_splunk_standalone_route(
                params['__default__']['namespace'], 
                instance['name'], 
                confirmation=params['confirmation'], 
                my_output=my_output,
                wait=True
            )
            if not success:
                return False

        object_filter=[]
        object_filter.append('namespace:%s' % (params['__default__']['namespace']))
        object_filter.append('name:%s' % (instance['name']))
        standalones = params['k8s_handler'].get_splunk_standalones(
            object_filter=object_filter,
            pod_info=True,
            pvc_info=True,
            service_info=True,
            route_info=True,
            secret_info=True,
            cache_enabled=False
        )
        if standalones is not None:
            k8s_output_handler.print_splunk_standalones_state(standalones)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Standalone instance created')
    my_output.default('- Route configured')
    return True