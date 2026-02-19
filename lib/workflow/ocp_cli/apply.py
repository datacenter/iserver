from lib import file_helper
from lib import ip_helper
from lib import output_helper
from menu import common
from lib.workflow.ocp_cli import common as local_common

def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'namespace' not in params:
        params['namespace'] = None

    if 'location' not in params or params['location'] is None or len(params['location']) == 0:
        return None, 'File locations with kube crds required'
        
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    allowed_keys = [
        'cluster',
        'namespace',
        'location',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Apply CRDs from file', before_newline=True, after_newline=True, double_underline=True)
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    destination = '/tmp/%s.yaml' % (ip_helper.get_short_uuid())
    for location in params['location']:
        contents = file_helper.get_files_text(location, yaml_only=True)
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
