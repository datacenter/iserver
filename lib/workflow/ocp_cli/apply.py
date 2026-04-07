from lib import file_helper
from lib import ip_helper
from lib import output_helper
from menu import common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, None, 'str', None, None, None, None],
        ['location', False, [], 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Apply CRDs from file', before_newline=True, after_newline=True, double_underline=True)
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    destination = '/tmp/%s.yaml' % (ip_helper.get_short_uuid())
    for location in params['location']:
        my_output.default('Checking location [%s]...' % (location), before_newline=True)
        contents = file_helper.get_files_text(location, yaml_only=True)
        if len(contents) == 0:
            my_output.default('No valid yaml content found')

        for filename in contents:
            my_output.default('File: %s' % (filename), before_newline=True)
            my_output.default(contents[filename], wrap='~~~')

            if params['confirmation']:
                if not common.get_confirmation():
                    return False
            
            my_output.default('Upload yaml file to %s...' % (destination), before_newline=True)
            success = params['ssh_handler'].scp_file(
                filename,
                destination
            )
            if not success:
                my_output.error('Upload failed')
                return False
            
            if params['namespace'] is None:
                command = 'oc apply -f %s' % (destination)
            else:
                command = 'oc apply -n %s -f %s' % (params['namespace'], destination)
                
            my_output.default(command)
            success, output, error = params['ssh_handler'].run_cmd(command)
            if not success:
                my_output.error('Failed')
                my_output.default(error, wrap='~~~')
                return False
            else:
                my_output.default(output, wrap='~~~', before_newline=True)

    return True
