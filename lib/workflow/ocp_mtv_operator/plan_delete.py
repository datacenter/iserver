from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'plan_namespace' not in params:
        params['plan_namespace'] = None

    if 'plan_name' not in params:
        params['plan_name'] = None

    if 'wipe' not in params:
        params['wipe'] = False

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'wait' not in params:
        params['wait'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'plan_namespace',
        'plan_name',
        'wipe',
        'wait',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Migraton Plan', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True
    
    migrations = params['k8s_handler'].get_migrations(
        vm_info=True, 
        vmi_info=True, 
        pvc_info=True, 
        dv_info=True, 
        pod_info=True,
        cache_enabled=False
    )

    ret, migration_plans = local_common.select_migration_plans(
        params,
        my_output,
        k8s_output_handler
    )
    if migration_plans is None:
        return ret
    
    success = True
    for migration_plan in migration_plans:
        if migration_plan['running']:
            my_output.default('Skipping running migration plan: %s/%s' % (migration_plan['namespace'], migration_plan['name']))
            continue
        
        plan_success = params['k8s_handler'].delete_plan(
            migration_plan['namespace'],
            migration_plan['name'],
            confirmation=False,
            wait=params['wait'],
            my_output=my_output
        )
        success = success and plan_success

        if not params['wipe']:
            continue

        my_output.default(
            'Migration resources for plan %s/%s' % (
                migration_plan['namespace'],
                migration_plan['name']
            ),
            before_newline=True
        )

        for migration in migrations:
            if migration['plan'] != migration_plan['name']:
                continue

            for vmi in migration['vmis']:
                my_output.default(
                    '- Virtual Machine Instance [%s/%s]' % (
                        vmi['namespace'],
                        vmi['name']
                    )
                )

            for vm in migration['vms']:
                my_output.default(
                    '- Virtual Machine [%s/%s]' % (
                        vm['namespace'],
                        vm['name']
                    )
                )

            for dv in migration['dvs']:
                my_output.default(
                    '- Data Volume [%s/%s]' % (
                        dv['namespace'],
                        dv['name']
                    )
                )

            for pvc in migration['pvcs']:
                my_output.default(
                    '- PVC [%s/%s]' % (
                        pvc['namespace'],
                        pvc['name']
                    )
                )

            for pod in migration['pods']:
                my_output.default(
                    '- Pod [%s/%s]' % (
                        pod['namespace'],
                        pod['name']
                    )
                )

        if params['confirmation']:
            if not get_confirmation():
                continue
            
        for migration in migrations:
            if migration['plan'] != migration_plan['name']:
                continue

            for vmi in migration['vmis']:
                wipe_success = params['k8s_handler'].stop_virtual_machine(
                    vmi['namespace'], 
                    vmi['name'], 
                    confirmation=False, 
                    my_output=my_output, 
                    wait=True
                )
                success = success and wipe_success

            for vm in migration['vms']:
                wipe_success = params['k8s_handler'].delete_virtual_machine(
                    vm['namespace'], 
                    vm['name'], 
                    confirmation=False, 
                    my_output=my_output, 
                    wait=True
                )
                success = success and wipe_success

            for dv in migration['dvs']:
                wipe_success = params['k8s_handler'].delete_data_volume(
                    dv['namespace'], 
                    dv['name'], 
                    my_output=my_output, 
                    wait=True
                )
                success = success and wipe_success

            for pvc in migration['pvcs']:
                wipe_success = params['k8s_handler'].delete_pvc(
                    pvc['namespace'], 
                    pvc['name'], 
                    my_output=my_output, 
                    wait=True
                )
                success = success and wipe_success

            for pod in migration['pods']:
                wipe_success = params['k8s_handler'].delete_pod(
                    pod['namespace'], 
                    pod['name'], 
                    my_output=my_output, 
                    wait=True
                )
                success = success and wipe_success

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- selected migration plans archived and deleted')
    if params['wipe']:
        my_output.default('- migration related resources deleted')

    return True
