from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, 'openshift-mtv', 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['wipe', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
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

    ocp_common.print_title(params, my_output, 'Delete Migration Plan')
    params = ocp_common.workflow_init(params, my_output, log_id)
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
