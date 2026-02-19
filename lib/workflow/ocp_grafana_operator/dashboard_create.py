import os
import copy
import json
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_grafana_operator import common as local_common


def resolve_scope(params):
    if 'scope' not in params:
        params['scope'] = []

    for item in params['scope']:
        if len(item.split(':')) != 2:
            return None, 'scope key:value required'
        
    return params, None


def resolve_crd(params):
    if 'crd' not in params:
        return None, 'crd required'

    if not isinstance(params['crd'], list):
        return None, 'crd must be list'

    filenames = []
    for file_path in params['crd']:
        if not os.path.isdir(file_path) and not os.path.isfile(file_path):
            return None, 'Path expected: %s' % (file_path)
        
        if not os.path.isabs(file_path) and 'base_directory' in params:
            file_path = os.path.join(
                params['base_directory'],
                file_path
            )

        if os.path.isfile(file_path):
            filenames.append(file_path)
            continue

        for filename in os.listdir(file_path):
            filenames.append(os.path.join(file_path, filename))

    if len(filenames) == 0:
        return None, 'No crd file defined'
    
    params['user_dashboard'] = []
    for filename in filenames:
        content = file_helper.get_file_yaml(filename)
        if content is None:
            continue

        if 'kind' not in content:
            continue

        if content['kind'] == 'GrafanaDashboard':
            params['user_dashboard'].append(filename)
        
    params['dir'] = None
    params['user_template'] = []
    for filename in filenames:
        content = file_helper.get_file_json(filename)
        if content is None:
            continue

        if 'uid' not in content:
            continue

        if 'title' not in content:
            continue

        if 'panels' not in content:
            continue

        params['user_template'].append(filename)
        params['dir'] = os.path.dirname(os.path.dirname(filename))
    
    if len(params['user_template']) > 0 and not os.path.isdir(os.path.join(params['dir'], 'panel')):
        return None, 'panels expected: %s' % (params['dir'])
    
    if len(params['user_dashboard']) == 0 and len(params['user_template']) == 0:
        return None, 'no dashboard or templates found'

    if len(params['user_template']) > 0 and len(params['scope']) == 0:
        return None, 'scope required in case of templates'

    if 'target' not in params:
        params['target'] = None

    if len(params['user_template']) == 0:
        params['target'] = None

    return params, None


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'instance' not in params:
        return None, 'instance name required'

    if not isinstance(params['instance'], str):
        return None, 'instance param must be string'

    params, error = resolve_scope(params)
    if params is None:
        return None, error
    
    params, error = resolve_crd(params)
    if params is None:
        return None, error
    
    if not isinstance(params['instance'], str):
        return None, 'instance param must be string'

    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
        'instance',
        'dir',
        'user_dashboard',
        'user_template',
        'scope',
        'target',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_content_template(directory, template_name, my_output):
    if len(template_name.split(':')) != 2:
        my_output.error('Unsupported template format: %s' % (template_name))
        return None

    (subdirectory, name) = template_name.split(':')
    directory = os.path.join(
        directory,
        subdirectory
    )
    if not os.path.isdir(directory):
        my_output.error('Template directory not found: %s' % (directory))
        return None

    dashboard = os.path.join(
        directory,
        name
    )

    content = file_helper.get_file_text(dashboard)
    if content is None:
        my_output.error('Template read failed: %s' % (dashboard))
        return None
    
    try:
        jcontent = json.loads(content)
    except BaseException:
        my_output.error('Template json read failed: %s' % (dashboard))
        return None
    
    return content

            
# def get_contents_template(directory, template_name, my_output):
#     if len(template_name.split(':')) != 2:
#         my_output.error('Unsupported template format')
#         return None

#     (subdirectory, dashboard_pattern) = template_name.split(':')
#     search_directory = os.path.join(
#         directory,
#         subdirectory
#     )
#     if not os.path.isdir(search_directory):
#         my_output.error('Template directory not found: %s' % (search_directory))
#         return None

#     contents = []

#     for filename in os.listdir(search_directory):
#         if filter_helper.match_string(dashboard_pattern, filename):
#             content = get_content_template(directory, '%s:%s' % (subdirectory, filename), my_output)
#             if content is not None:
#                 my_output.default('- filename: %s' % (filename))
#                 contents.append(
#                     content
#                 )
    
#     if len(contents) == 0:
#         my_output.error('No valid content file found')
#         return None
    
#     return contents


def resolve_dashboard_panels(content, params, my_output):
    if 'panels' not in content:
        my_output.errors('Panels section required')
        return None
    
    new_panels = []
    current_x = 0
    current_y = 0
    max_h = 0
    for panel in content['panels']:
        if 'ipanel' not in panel:
            new_panels.append(panel)
            continue

        new_panel = get_content_template(
            os.path.join(params['dir'], 'panel'), 
            panel['ipanel'],
            my_output
        )
        if new_panel is None:
            return None
        
        try:
            new_jpanel = json.loads(new_panel)
        except BaseException:
            my_output.error('json panel load failed: %s' % (panel['ipanel']))
            return None
        
        # honor user-provided width and hight
        if 'gridPos' in panel:
            for key in ['h', 'w']:
                if key in panel['gridPos']:
                    new_jpanel['gridPos'][key] = panel['gridPos'][key]

        # adjust position

        if current_x + new_jpanel['gridPos']['w'] > 24:
            current_x = 0
            current_y += max_h
            max_h = 0

        new_jpanel['gridPos']['x'] = current_x
        new_jpanel['gridPos']['y'] = current_y

        current_x += new_jpanel['gridPos']['w']
        max_h = max(max_h, new_jpanel['gridPos']['h'])

        new_panels.append(new_jpanel)

    content['panels'] = copy.deepcopy(new_panels)
    return content


def get_content(params, filename, scope, my_output):
    content = file_helper.get_file_json(filename)
    if content is None:
        my_output.error('File read failed: %s' % (filename))
        return None

    content = resolve_dashboard_panels(content, params, my_output)
    if content is None:
        return None

    prometheus_id = None
    for instance in params['grafana']:
        if instance['name'] == params['instance']:
            for datasource in instance['datasource']:
                if datasource['ds_type'] == 'prometheus':
                    prometheus_id = datasource['uid']

    text_content = json.dumps(content, indent=4)

    if prometheus_id is None and '${PROMETHEUS}' in text_content:
        my_output.error('prometheus uid resolution failed')
        return None
    
    if prometheus_id is not None:
        pattern = '${%s}' % ('PROMETHEUS')
        text_content = text_content.replace(pattern, prometheus_id)

    pattern = '${%s}' % ('SCOPE')
    text_content = text_content.replace(pattern, '%s=\\"%s\\"' % (scope.split(':')[0].replace('-', '_'), scope.split(':')[1]))

    folder_name = None
    dashboard_name = None

    if params['target'] is None:
        folder_name = scope.split(':')[1]
        dashboard_name = scope.split(':')[1]
        
    if params['target'] is not None:
        if len(params['target'].split(':')) == 1:
            folder_name = None
            dashboard_name = params['target']

        if len(params['target'].split(':')) == 2:
            (dashboard_name, folder_name) = params['target'].split(':')

    if dashboard_name is not None:
        pattern = '${%s}' % ('NAME')
        text_content = text_content.replace(pattern, dashboard_name)

    if folder_name is not None:
        pattern = '${%s}' % ('FOLDER')
        text_content = text_content.replace(pattern, folder_name)

    jcontent = json.loads(text_content)

    if folder_name is None and 'folder' in jcontent:
        del jcontent['folder']

    return jcontent

    
def set_dashboard_template(params, filename, scope, my_output):
    content = get_content(params, filename, scope, my_output)
    if content is None:
        return False
    
    folder = None
    if 'folder' in content:
        folder = content['folder']
        del content['folder']
    
    label = None
    for instance in params['grafana']:
        if instance['name'] == params['instance']:
            if 'dashboards' not in instance['label']:
                my_output.error('dashboards label expected in grafana instance')
                return None
            
            label = instance['label']['dashboards']

    success = params['k8s_handler'].create_grafana_dashboard(
        params['namespace'], 
        content['uid'], 
        label, 
        json.dumps(content, indent=4), 
        folder=folder,
        confirmation=params['confirmation'],
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Grafana Operator - Create Dashboard', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_grafana_subscription(params['namespace'], params['name']):
        my_output.error('Grafana Operator is not installed')
        return False
    
    instance_namespace = params['namespace']
    instance_name = params['instance']
    if not params['k8s_handler'].is_grafana(instance_namespace, instance_name, cache_enabled=False):
        my_output.error('Grafana instance [%s/%s] not defined' % (instance_namespace, instance_name))
        return False

    my_output.default('Grafana instance: %s/%s' % (instance_namespace, instance_name))

    params = local_common.get_resources(params, my_output)
    if params is None:
        return False
    
    if len(params['user_dashboard']) > 0:
        my_output.default('Grafana dashboard source files', before_newline=True)
        for item in params['user_dashboard']:
            my_output.default('- %s' % (item))

    if len(params['user_template']) > 0:
        my_output.default('Grafana dashboard template source files', before_newline=True)
        for item in params['user_template']:
            my_output.default('- %s' % (item))

        my_output.default('Grafana dashboard template scope', before_newline=True)
        for item in params['scope']:
            my_output.default('- %s' % (item))

        for filename in params['user_template']:
            for scope in params['scope']:
                success = set_dashboard_template(params, filename, scope, my_output)
                if not success:
                    return False

    return True
