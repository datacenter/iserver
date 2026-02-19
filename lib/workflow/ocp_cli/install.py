import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check

from lib.workflow import ocp_common
from lib.workflow.ocp_bashrc_proxy import task as task_bashrc
from lib.workflow.ocp_cilium_cli import task as task_cilium_cli
from lib.workflow.ocp_helm_cli import task as task_helm_cli
from lib.workflow.ocp_hubble_cli import task as task_hubble_cli
from lib.workflow.ocp_tridentctl_cli import task as task_tridentctl_cli
from lib.workflow.ocp_virtctl_cli import task as task_virtctl_cli
from lib.workflow.ocp_web_terminal_operator import task as task_web_cli
from lib.workflow.ocp_cli import apply as task_file


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    return params, None

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - CLI Tools Installation', before_newline=True, after_newline=True, double_underline=True)
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    my_output.default('Workflow Parameters', underline=True)
    my_output.default(json.dumps(params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id=log_id)

    if 'exec' in params:
        for command in params['exec']:
            my_output.default('Run command: %s' % command, before_newline=True, underline=True)
            success, output, error = params['ssh_handler'].run_cmd(command)
            if not success:
                my_output.error('Failed')
                my_output.error(error)
            else:
                my_output.default(output)

    if 'bashrc' in params:
        task_bashrc.run(params['bashrc'], log_id=log_id)

    if 'cilium' in params:
        task_cilium_cli.run(params['cilium'], log_id=log_id)

    if 'hubble' in params:
        task_hubble_cli.run(params['hubble'], log_id=log_id)

    if 'helm' in params:
        task_helm_cli.run(params['helm'], log_id=log_id)

    if 'tridentctl' in params:
        task_tridentctl_cli.run(params['tridentctl'], log_id=log_id)

    if 'virtctl' in params:
        task_virtctl_cli.run(params['virtctl'], log_id=log_id)

    if 'web' in params:
        task_web_cli.run(params['web'], log_id=log_id)

    if 'file' in params:
        task_file.run(params['file'], log_id=log_id)

    return True
