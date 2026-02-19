import os
import copy
import yaml
import traceback
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'crd' not in params or len(params['crd']) == 0:
        return None, 'CRDs expected'

    if isinstance(params['crd'][0], str):
        crd = []
        locations = []
        for policy_item in params['crd']:
            try:
                if not os.path.isabs(policy_item):
                    policy_item = os.path.join(
                        params['base_directory'],
                        policy_item
                    )
            except BaseException:
                print(traceback.format_exc())
                return None, 'Policy file path detection failed'
            
            locations.append(policy_item)

        for item in locations:
            policies = file_helper.get_files_text(item, yaml_only=True)
            if policies is not None:
                for key in policies:
                    crd.append(
                        yaml.safe_load(policies[key])
                    )

        params['crd'] = copy.deepcopy(crd)

    if len(params['crd']) == 0:
        return None, 'CRDs expected'
    
    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    allowed_keys = [
        'cluster',
        'crd',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Tetragon Operator - Create Policy', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_tetragon_subscription(params['namespace'], params['name']):
        my_output.default('Tetragon Operator not installed')
        return True

    for body in params['crd']:
        if not local_common.is_tetragon_crd(body['kind']):
            my_output.default('Non-tetragon kind: %s' % (body['kind']))
            my_output.error('Fixup input files')
            return False

        if body['kind'] == 'AlertRule':
            success = params['k8s_handler'].create_alert_rule(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False
            
        if body['kind'] == 'SandboxPolicy':
            success = params['k8s_handler'].create_sandbox_policy(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if body['kind'] == 'SandboxPolicyNamespaced':
            success = params['k8s_handler'].create_sandbox_policy_namespaced(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if body['kind'] == 'TetragonNetworkPolicy':
            success = params['k8s_handler'].create_tetragon_network_policy(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if body['kind'] == 'TetragonNetworkPolicyNamespaced':
            success = params['k8s_handler'].create_tetragon_network_policy_namespaced(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if body['kind'] == 'TracingPolicy':
            success = params['k8s_handler'].create_tracing_policy(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if body['kind'] == 'TracingPolicyNamespaced':
            success = params['k8s_handler'].create_tracing_policy_namespaced(
                body,
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- CRDs applied')

    return True
