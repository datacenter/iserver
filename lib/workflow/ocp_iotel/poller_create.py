import os 
import base64
from lib import output_helper
from lib import iaccount_helper
from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib.ocp import main as ocp
from lib.ocp import settings
from lib.intersight import helper as intersight_helper
from lib.workflow.ocp_iotel import common as local_common
from menu.common import get_confirmation


def validate(params, log_id):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'suffix' not in params or params['suffix'] is None:
        return None, 'Suffix name required'

    if 'iaccount' not in params or params['iaccount'] is None:
        params['iaccount'] = params['suffix']

    if 'dir' not in params:
        params['dir'] = None

    if 'template' not in params or params['template'] is None:
        params['template'] = []

    if len(params['template']) > 0 and params['dir'] is None:
        return None, 'Template directory required'
    
    if 'mode' not in params or params['mode'] is None:
        params['mode'] = 'replace'

    if 'attribute' not in params or params['attribute'] is None:
        params['attribute'] = []

    for item in params['attribute']:
        if len(item.split(':')) != 2:
            return None, 'Attributes in key:value format required'
        
    if 'target' not in params or params['target'] is None:
        params['target'] = []

    settings_handler = settings.OcpSettings(log_id=log_id)
    for target in params['target']:
        if len(target.split(':')) == 1:
            return None, 'invalid target format'
        
        if target.split(':')[0] not in ['ocp', 'server-name', 'server-ip']:
            return None, 'invalid target format'
        
        if target.split(':')[0] == 'ocp':
            if settings_handler.get_ocp_cluster(target.split(':')[1], strict_match=False) is None:
                return None, 'Cluster not found: %s' % (target.split(':')[1])

    if 'pollers' not in params or params['pollers'] is None:
        params['pollers'] = None
        if len(params['template']) == 0:
            return None, 'Pollers filename or templates required'

    if params['pollers'] is not None:
        pollers_filename = params['pollers']
        if 'base_directory' in params:
            try:
                pollers_filename = os.path.join(
                    params['base_directory'],
                    params['pollers']
                )
            except BaseException:
                return None, 'Pem file path detection failed'
            
        params['poller'] = file_helper.get_file_text(
            pollers_filename
        )
        if params['poller'] is None:
            return None, 'Pollers file read failed'
    else:
        params['poller'] = ''

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'suffix',
        'iaccount',
        'poller',
        'pollers',
        'dir',
        'target',
        'template',
        'attribute',
        'mode',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def create_temporary_iaccount(instance, my_output):
    iaccount_handler = iaccount_helper.IntersightAccount()

    iaccount_name = 'iotel-%s' % (ip_helper.get_short_uuid())
    configuration = {}
    configuration['keyfile'] = file_helper.set_tmp_file(base64.b64decode(instance['intersight_pem']).decode('utf-8'))
    configuration['keyid'] = base64.b64decode(instance['intersight_key']).decode('utf-8')
    configuration['output'] = 'default'
    configuration['server'] = 'intersight.com'

    if not iaccount_handler.create_iaccount(iaccount_name, configuration):
        my_output.error('Failed to create temporary iaccount')
        return None

    return iaccount_name


def delete_temporary_iaccount(iaccount_name):
    iaccount_handler = iaccount_helper.IntersightAccount()
    iaccount_handler.delete_iaccount(iaccount_name)


def resolve_moids(params, servers, my_output, log_id):
    my_output.default('Resolving intersight ids', before_newline=True, underline=True)

    cluster_ids = {}
    params['server_ids'] = []

    for target in params['target']:
        if target.split(':')[0] == 'server-name':
            my_output.default('Server name: %s' % (target.split(':')[1]))
            found = False
            for server in servers:
                if server['Name'] == target.split(':')[1]:
                    found = True
                    server_ids = {}
                    server_ids['moid'] = server['Moid']
                    server_ids['name'] = server['Name']
                    server_ids['ip'] = server['ManagementIp']
                    server_ids['device_id'] = server['DeviceMoId']
                    params['server_ids'].append(
                        server_ids
                    )
                    break
            
            if not found:
                my_output.error('not found')
                return None

        if target.split(':')[0] == 'server-ip':
            addresses = []
            cidrs = []

            if ip_helper.is_valid_ipv4_address(target.split(':')[1]):
                addresses.append(
                    target.split(':')[1]
                )

            if ip_helper.is_valid_ipv4_cidr(target.split(':')[1]):
                cidrs.append(
                    target.split(':')[1]
                )

            if len(target.split(':')[1].split('-')) == 2:
                (start_adress, end_address) = target.split(':')[1].split('-')
                if len(end_address.split('.')) == 1:
                    end_address = '%s.%s' % (
                        '.'.join(start_adress.split('.')[:3]),
                        end_address
                    )

                addresses = addresses + ip_helper.get_ipv4_addresses_in_range(
                    start_adress,
                    end_address
                )

            my_output.default('Server IP: %s' % (target.split(':')[1]))
            found = False
            for server in servers:
                match = False
                if server['ManagementIp'] in addresses:
                    match = True

                if not match:
                    for cidr in cidrs:
                        if ip_helper.is_ipv4_in_cidr(server['ManagementIp'], cidr):
                            match = True

                if match:
                    found = True
                    server_ids = {}
                    server_ids['moid'] = server['Moid']
                    server_ids['name'] = server['Name']
                    server_ids['ip'] = server['ManagementIp']
                    server_ids['device_id'] = server['DeviceMoId']
                    params['server_ids'].append(
                        server_ids
                    )
            
            if not found:
                my_output.error('not found')
                return None
            
        if target.split(':')[0] == 'ocp':
            cluster_name = target.split(':')[1]
            cluster_handler = ocp.Ocp(
                cluster_name,
                verbose=False,
                debug=False,
                log_id=log_id
            )

            my_output.default('Cluster: %s' % (cluster_name), before_newline=True)
            if not cluster_handler.k8s_handler.check_api():
                my_output.error('k8s api fails')
    
            cluster_ids[cluster_name] = {}
            nodes = cluster_handler.k8s_handler.get_nodes()
            if nodes is None:
                my_output.error('Failed to get cluster nodes')
                return None
            
            for node in nodes:
                my_output.default('- node: %s' % (node['name']))

                cluster_ids[cluster_name][node['name']] = {}
                cluster_ids[cluster_name][node['name']]['id'] = None
                cluster_ids[cluster_name][node['name']]['device_id'] = None
                for annotation in node['annotations']:
                    if len(annotation.split('intersight-')) > 1:
                        if len(annotation.split('intersight-dev-')) > 1:
                            cluster_ids[cluster_name][node['name']]['device_id'] = node['annotations'][annotation]
                        else:
                            cluster_ids[cluster_name][node['name']]['id'] = node['annotations'][annotation]

                if cluster_ids[cluster_name][node['name']]['id'] is None:
                    my_output.error('node %s has no intersight id annotation' % (node['name']))
                    return None
                
                my_output.default('\tid: %s' % (cluster_ids[cluster_name][node['name']]['id']))

                if cluster_ids[cluster_name][node['name']]['device_id'] is None:
                    my_output.error('node %s has no intersight device id annotation' % (node['name']))
                    return None
                
                my_output.default('\tdevice id: %s' % (cluster_ids[cluster_name][node['name']]['device_id']))

                found = False
                for server in servers:
                    if server['Moid'] == cluster_ids[cluster_name][node['name']]['id']:
                        if server['RegisteredDeviceMoid'] == cluster_ids[cluster_name][node['name']]['device_id']:
                            server_ids = {}
                            server_ids['moid'] = server['Moid']
                            server_ids['name'] = server['Name']
                            server_ids['ip'] = server['ManagementIp']
                            server_ids['device_id'] = server['DeviceMoId']
                            params['server_ids'].append(
                                server_ids
                            )
                            found = True

                if not found:
                    my_output.error('Server not found in intersight')
                    return None
                
                my_output.default('\tserver found')

    return params


def get_template_names(params, template_search):
    all_template_names = file_helper.get_subdirs(
        params['dir'], 
        return_full_name=False, 
        must_include=['pollers.txt']
    )
    template_names = []
    for template_name in all_template_names:
        if filter_helper.match_string(template_search, template_name):
            template_names.append(
                template_name
            )

    return template_names


def generate_poller(params, template_name, my_output):
    poller_template_filename = os.path.join(os.path.join(params['dir'], template_name), 'pollers.txt')
    poller_template = file_helper.get_file_text(poller_template_filename)
    if poller_template is None:
        my_output.error('Failed to read file: %s' % (poller_template))
        return None

    poller = None
    for server_ids in params['server_ids']:
        content = poller_template

        pattern = '${%s}' % ('DEVICE_ID')
        content = content.replace(pattern, server_ids['device_id'])

        pattern = '${%s}' % ('SCOPE')
        scope = 'server-name = "%s", server-ip = "%s"' % (server_ids['name'], server_ids['ip'])
        for attribute in params['attribute']:
            scope = '%s, %s = "%s"' % (
                scope,
                attribute.split(':')[0],
                attribute.split(':')[1]
            )
        content = content.replace(pattern, scope)

        if poller is None:
            poller = content
        else:
            poller = '%s\n%s' % (poller, content)

    return poller


def generate_pollers(params, template_search, my_output):
    template_names = get_template_names(params, template_search)
    if len(template_names) == 0:
        my_output.error('No template found')
        return None
    
    pollers = None
    for template_name in template_names:
        poller = generate_poller(params, template_name, my_output)
        if poller is None:
            my_output.error('Poller generation from template failed: %s' % (template_name))
            return None
        
        if pollers is None:
            pollers = poller
        else:
            pollers = '%s\n%s' % (pollers, poller)
    
    return pollers


def modify_poller(params, instance, my_output, log_id):
    if len(params['template']) == 0:
        if params['mode'] == 'add':
            if len(params['poller']) == 0: 
                my_output.default('- no templates and no user-provided poller and add mode => nothing to add')
                return None

        if params['mode'] == 'replace':
            my_output.default(params['poller'], wrap='~~~', before_newline=True, after_newline=True)
            my_output.default('- no templates and replace mode => nothing to add')
            return None
    
    if params['mode'] == 'add':
        new_poller = 'otel_collector_endpoint = "http://127.0.0.1:4317"\n'
        for line in instance['poller'].split('\n'):
            if len(line.split('otel_collector_endpoint = ')) == 1:
                new_poller = '%s\n%s' % (new_poller, line)

        for line in params['poller'].split('\n'):
            if len(line.split('otel_collector_endpoint = ')) == 1:
                new_poller = '%s\n%s' % (new_poller, line)

        params['poller'] = new_poller

    if len(params['template']) == 0:
        my_output.default(params['poller'], wrap='~~~', before_newline=True, after_newline=True)
        if params['confirmation']:
            if not get_confirmation('Confirm pollers definition?'):
                return None
                
        return params

    iaccount_name = create_temporary_iaccount(instance, my_output)
    if iaccount_name is None:
        return None

    servers = intersight_helper.get_all_servers(
        iaccount_name,
        1,
        log_id=log_id
    )
    if servers is None:
        my_output.error(
            'Failed to collect servers info'
        )
        return None
    
    params = resolve_moids(params, servers, my_output, log_id)
    if params is None:
        delete_temporary_iaccount(iaccount_name)
        return None
    
    delete_temporary_iaccount(iaccount_name)

    if 'otel_collector_endpoint = "http://127.0.0.1:4317"' not in params['poller']:
        params['poller'] = 'otel_collector_endpoint = "http://127.0.0.1:4317"\n\n%s' % (params['poller'])
    
    for ptemplate in params['template']:
        tpoller = generate_pollers(params, ptemplate, my_output)
        if tpoller is None:
            return None
        
        params['poller'] = '%s\n%s' % (
            params['poller'],
            tpoller
        )

    my_output.default(params['poller'], wrap='~~~', before_newline=True, after_newline=True)

    if params['confirmation']:
        if not get_confirmation('Confirm pollers definition?'):
            return None
        
    return params


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Open Telemetry (iotel) - Set Poller', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params, log_id)
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
    
    for instance in params['instance']:
        my_output.default('Instance', before_newline=True, underline=True)
        my_output.default('- deployment %s/%s' % (instance['namespace'], instance['name']))
        my_output.default('- config map %s/%s' % (instance['intersight_config_namespace'], instance['intersight_config_name']))
        my_output.default('- mode: %s' % (params['mode']))
        if len(params['template']) == 0:
            my_output.default('- no template')
        if len(params['template']) > 0:
            my_output.default('- template: %s' % (','.join(params['template'])))
            my_output.default('- target: %s' % (','.join(params['target'])))
            if len(params['attribute']) > 0:
                my_output.default('- extra metric attributes: %s' % (','.join(params['attribute'])))

        if len(params['poller']) == 0:
            my_output.default('- empty user-provided poller')
        else:
            my_output.default('- user-provided poller')

        my_output.default('')

        new_poller = modify_poller(params, instance, my_output, log_id)
        if new_poller is None:
            continue

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
        data['intersight-otel.toml'] = params['poller']

        success = params['k8s_handler'].set_config_map_data(
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
