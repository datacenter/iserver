from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_iotel import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'suffix' not in params or params['cluster'] is None:
        return None, 'Suffix name required'
    
    if 'metric' not in params:
        params['metric'] = []

    if not isinstance(params['metric'], list):
        return None, 'metric param must be list'
    
    if 'attribute' not in params:
        params['attribute'] = []

    if not isinstance(params['attribute'], list):
        return None, 'attribute param must be list'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = False

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
        
    allowed_keys = [
        'cluster',
        'suffix',
        'metric',
        'attribute',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def match_section(params, poller):
    if len(params['metric']) == 0 and len(params['attribute']) == 0:
        return True
    
    match = False
    for metric in params['metric']:
        if filter_helper.match_string(metric, poller['name']):
            match = True

    if len(params['metric']) > 0 and not match:
        return False

    match = False    
    for attribute in params['attribute']:
        if len(attribute.split('=')) != 2:
            continue

        (key, value) = attribute.split('=')
        if key in poller['attribute'] and filter_helper.match_string(value, poller['attribute'][key]):
            match = True

    if len(params['attribute']) > 0 and not match:
        return False
        
    return True


def modify_poller(params, content, my_output):
    endpoint = None
    for line in content.split('\n'):
        if len(line.split('otel_collector_endpoint = ')) == 2:
            endpoint = line

    if endpoint is None:
        my_output.error('No otel_collector_endpoint found')
        return False, None
    
    modified = False
    new_poller = endpoint
    section = None
    for line in content.split('\n'):
        if '[[pollers]]' in line:
            if section is not None:
                if match_section(params, section):
                    my_output.default(section['content'], after_newline=True)
                    modified = True
                else:
                    new_poller = '%s\n\n%s' % (new_poller, section['content'])
            
            section = {}
            section['name'] = None
            section['attribute'] = {}
            section['content'] = '[[pollers]]'
            continue

        if '[[tspollers]]' in line:
            if section is not None:
                if match_section(params, section):
                    my_output.default(section['content'], after_newline=True)
                    modified = True
                else:
                    new_poller = '%s\n\n%s' % (new_poller, section['content'])
            
            section = {}
            section['name'] = None
            section['attribute'] = {}
            section['content'] = '[[tspollers]]'
            continue

        if section is not None:
            if len(line.strip()) > 0:
                if len(line.split('name = ')) == 2:
                    section['name'] = line.split('name = ')[1].replace('"', '')
                if len(line.split('otel_attributes = ')) == 2:
                    attributes = line.split('otel_attributes = ')[1].split('{ ')[1].split(' }')[0]
                    for item in attributes.split(', '):
                        section['attribute'][item.split(' = ')[0]] = item.split(' = ')[1].replace('"', '')

                section['content'] = '%s\n%s' % (
                    section['content'],
                    line
                )
        
    if section is not None:
        if match_section(params, section):
            my_output.default(section['content'], after_newline=True)
            modified = True
        else:
            new_poller = '%s\n\n%s' % (new_poller, section['content'])

    return modified, new_poller

    
def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Open Telemetry (iotel) - Delete Poller', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    params = local_common.get_instances(params, my_output)
    if params is None: 
        return False
    
    if len(params['instance']) == 0:
        my_output.default('No instance found', before_newline=True)
        return True
    
    my_output.default('Poller selection', underline=True)
    my_output.default('- suffix: %s' % (params['suffix']))
    if len(params['metric']) > 0:
        my_output.default('- metric: %s' % (', '.join(params['metric'])))
    if len(params['attribute']) > 0:
        my_output.default('- attribute: %s' % (', '.join(params['attribute'])))
    
    for instance in params['instance']:
        my_output.default('Instance', before_newline=True, underline=True)
        my_output.default('- deployment %s/%s' % (instance['namespace'], instance['name']))
        my_output.default('- config map %s/%s' % (instance['intersight_config_namespace'], instance['intersight_config_name']))

        my_output.default('Removed pollers', before_newline=True, after_newline=True, underline=True)
        modified, new_poller = modify_poller(params, instance['poller'], my_output)
        if new_poller is None:
            continue

        if not modified:
            my_output.default('No changes')
            continue

        my_output.default('New pollers', before_newline=True, after_newline=True, underline=True)
        my_output.default(new_poller)

        if params['confirmation']:
            if not get_confirmation():
                return False

        success = params['k8s_handler'].set_deployment_replicas(
            instance['namespace'], 
            instance['name'],
            0,
            confirmation=False, 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        data = {}
        data['intersight-otel.toml'] = new_poller

        success = params['k8s_handler'].update_config_map(
            instance['intersight_config_namespace'], 
            instance['intersight_config_name'],
            data,
            confirmation=False,
            my_output=my_output
        )
        if not success:
            return False

        success = params['k8s_handler'].set_deployment_replicas(
            instance['namespace'], 
            instance['name'],
            1,
            confirmation=False, 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
                
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Config map changed')
    my_output.default('- Deployment restarted')

    return True
