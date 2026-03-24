import os
from lib import ip_helper
from lib import output_helper
from lib import ssh
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from lib.workflow.k8s import common as local_common
from lib.linux import settings
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['storage_class', True, None, 'str', None, None, None, None],
        ['source', True, None, 'str', None, None, None, None],
        ['size', False, None, 'str', None, None, None, None],
        ['secret', True, None, 'str', None, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Data Volume - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['storage_class'] is None:
        sc_names = params['k8s_handler'].get_storage_class_names(cache_enabled=False)
        if len(sc_names) == 0:
            my_output.error('No storage class found')
            return False
        
        if len(sc_names) == 1:
            params['storage_class'] = sc_names[0]

        if len(sc_names) > 1:
            default_storage_class = params['k8s_handler'].get_default_storage_class_name(cache_enabled=True)
            if default_storage_class is None:
                my_output.error('Define storage class name')
                return False

            params['storage_class'] = default_storage_class

    if params['source'] is None:
        success = params['k8s_handler'].create_data_volume(
            params['namespace'], 
            params['name'], 
            params['storage_class'],
            params['size'],
            None,
            bind=True,
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    if params['source'] is not None:
        if ip_helper.is_url_valid(params['source']):
            success = params['k8s_handler'].create_data_volume(
                params['namespace'], 
                params['name'], 
                params['storage_class'],
                params['source'],
                params['size'],
                bind=True,
                secret=params['secret'],
                confirmation=params['confirmation'], 
                my_output=my_output, 
                my_k8s_output=k8s_output_handler,
                wait=True
            )
            if not success:
                return False
        else:
            if len(params['source'].split('@')) == 2:
                source_linux, source_filename = params['source'].split('@')

                linux_settings_handler = settings.LinuxSettings(log_id=log_id)
                server = linux_settings_handler.get_linux_server(source_linux)
                if server is None:
                    my_output.error('Linux connector not found: %s' % (source_linux))
                    return False
                
                destination = '/tmp/%s' % (ip_helper.get_short_uuid())
                my_output.default('Download file: %s => %s' % (source_filename, destination))
                server_ssh = ssh.Ssh(
                    server['address'], 
                    server['username'], 
                    password=server['password'],
                    key_filename=server['key'], 
                    log_id=log_id
                )
                success = server_ssh.scp_file(
                    source_filename,
                    destination,
                    put=False
                )
                if not success:
                    my_output.error('Download failed')
                    return False
                
                source_filename = destination
            else:
                source_filename = params['source']
                if not os.path.isfile(source_filename):
                    my_output.error('File not found: %s' % (source_filename))
                    return False

            ssh_handler = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id=log_id)
            if ssh_handler is None:
                my_output.error('Cluster management node ssh access required for virtctl file upload')
                return False
            
            success, output, error = ssh_handler.run_cmd(
                'virtctl version'
            )
            if not success:
                my_output.error('virtctl required on cluster management node')
                return False

            success = params['k8s_handler'].create_data_volume(
                params['namespace'], 
                params['name'], 
                params['storage_class'],
                None,
                params['size'],
                bind=True,
                confirmation=params['confirmation'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False

            destination = '/tmp/%s' % (ip_helper.get_short_uuid())
            my_output.default('scp file upload: %s => %s' % (source_filename, destination))
            success = ssh_handler.scp_file(
                source_filename,
                destination
            )
            if not success:
                my_output.error('Upload failed')
                return False

            command = 'virtctl -n %s image-upload dv %s --no-create --image-path=%s --insecure' % (
                params['namespace'],
                params['name'],
                destination
            )
            my_output.default('Run: %s' % (command))
            success, output, error = ssh_handler.run_cmd(
                command
            )
            if not success:
                my_output.default(str(output))
                my_output.default(str(error))
                return False
            
    info = params['k8s_handler'].get_data_volume(
        params['namespace'], 
        params['name'],
        cache_enabled=False
    )
    if info is None:
        my_output.error('New data volume not found')
        return False
    
    k8s_output_handler.print_data_volumes([info])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- data volume created')
    return True
