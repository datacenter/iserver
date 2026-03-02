import os
import json
from lib import file_helper
from lib import ip_helper
from lib import template
from lib.workflow.ocp_task import create as task
from lib.openshift import console


def validate_base(user_settings, my_output, log_id):
    console_handler = console.Console(log_id=log_id)

    mandatory_keys = [
        'name',
        'base_dns_domain',
        'ntp',
        'dns_ip',
        'dns_search',
        'machine_network_gateway'
    ]
    for key in mandatory_keys:
        if key not in user_settings:
            my_output.error('Key %s missing' % (key))
            return None

    ntp_sources = []
    for ntp_value in user_settings['ntp'].split(','):
        ntp_value = ntp_value.strip()
        if ip_helper.get_ip(ntp_value) is None and not ip_helper.is_valid_ipv4_address(ntp_value):
            my_output.error('ntp must be valid ip or resolvable name')
            return None
        
        ntp_sources.append(ntp_value)

    user_settings['ntp'] = ','.join(ntp_sources)
    
    for ip_address in user_settings['dns_ip'].split(','):
        if not ip_helper.is_valid_ipv4_address(ip_address):
            my_output.error('dns ip invalid')
            return None
    
    if not ip_helper.is_valid_ipv4_cidr(user_settings['machine_network_gateway']):
        my_output.error('invalid machine network gateway')
        return None
    
    deprecated_keys = [
        'olm_operators'
    ]
    for key in deprecated_keys:
        if key in user_settings:
            my_output.error('Key %s deprecated' % (key))
            return None

    defaults = {}
    defaults['randomize'] = False
    defaults['connector'] = None
    defaults['domain'] = None
    defaults['openshift_version'] = console_handler.get_assisted_install_versions_latest()
    defaults['cpu_architecture'] = 'x86_64'
    defaults['cluster_network_cidr'] = '10.128.0.0/14'
    defaults['cluster_network_host_prefix'] = 23
    defaults['service_network_cidr'] = '172.30.0.0/16'
    defaults['http_proxy'] = None
    defaults['https_proxy'] = None
    defaults['no_proxy'] = None
    defaults['network_type'] = 'OVNKubernetes'
    defaults['disk_encryption'] = 'none'
    defaults['encryption_mode'] = 'tpmv2'
    defaults['strip_token'] = True
    for key in defaults:
        if key not in user_settings:
            user_settings[key] = defaults[key]

    if user_settings['connector'] is None:
        user_settings['connector'] = user_settings['name']

    disk_encryption_options = ['none', 'masters', 'arbiters', 'workers', 'masters,arbiters', 'masters,workers', 'arbiters,workers', 'masters,arbiters,workers', 'all']
    if user_settings['disk_encryption'] not in disk_encryption_options:
        my_output.error('Invalid disk encryption option value [%s].' % (user_settings['disk_encryption']))
        my_output.default('Allowed values: ')
        for disk_encryption_option in disk_encryption_options:
            my_output.default('- %s' % (disk_encryption_option))
        return None

    if user_settings['encryption_mode'] != 'tpmv2':
        my_output.error('Invalid encryption mode value [%s]. Expected tpmv2.' % (user_settings['encryption_mode']))
        return None

    return user_settings


def validate_web(user_settings, my_output):
    if 'web_server' not in user_settings:
        my_output.error('Web server section missing')
        return None

    mandatory_keys = [
        'ip',
        'image_base_url',
        'image_upload_directory'
    ]
    for key in mandatory_keys:
        if key not in user_settings['web_server']:
            my_output.error('web_server.%s missing' % (key))
            return None

    if user_settings['web_server']['ip'] != 'localhost':
        if not ip_helper.is_valid_ipv4_address(user_settings['web_server']['ip']):
            my_output.error('web_server.ip invalid')
            return None

        if 'username' not in user_settings['web_server']:
            my_output.error('web_server.username required')
            return None

        if 'password' not in user_settings['web_server']:
            user_settings['web_server']['password'] = None

        if 'ssh_public_key' not in user_settings['web_server']:
            user_settings['web_server']['ssh_public_key'] = None

        if user_settings['web_server']['password'] is None and user_settings['web_server']['ssh_public_key'] is None:
            my_output.error('web_server requires either password or ssh_public_key property')
            return None

        if user_settings['web_server']['password'] is not None and user_settings['web_server']['ssh_public_key'] is not None:
            my_output.error('web_server requires either password or ssh_public_key property')
            return None

    if 'verify' not in user_settings['web_server']:
        user_settings['web_server']['verify'] = True
    
    if not isinstance(user_settings['web_server']['verify'], bool):
        my_output.error('web_server verify bool required')
        return None

    if 'base_check' not in user_settings['web_server']:
        user_settings['web_server']['base_check'] = True
    
    if not isinstance(user_settings['web_server']['base_check'], bool):
        my_output.error('web_server base_check bool required')
        return None

    if 'timeout' not in user_settings['web_server']:
        user_settings['web_server']['timeout'] = 5
    
    if not isinstance(user_settings['web_server']['timeout'], int):
        my_output.error('web_server timeout int required')
        return None

    return user_settings


def validate_tasks(user_settings, my_output):
    if 'tasks' in user_settings:
        new_tasks, error = task.validate(
            user_settings['tasks'], 
            user_settings['name'], 
            cluster_settings=user_settings
        )
        if error is not None:
            my_output.error(error)
            return None

    return user_settings


def validate_cilium(user_settings, my_output):
    settings = {}
    settings['verify'] = True
    settings['manage'] = True
    settings['cidr'] = True

    if 'cilium' not in user_settings:
        user_settings['cilium'] = {}

    if not isinstance(user_settings['cilium'], dict):
        my_output.error('cilium must be dict')
        return None

    for key in settings:
        if key not in user_settings['cilium']:
            user_settings['cilium'][key] = settings[key]

        if not isinstance(user_settings['cilium'][key], bool):
            my_output.error('cilium.%s must be true or false' % (key))
            return None

    return user_settings


def validate_server(user_settings, my_output, log_id):
    template_handler = template.Template(log_id=log_id)
    if 'server' not in user_settings:
        my_output.error('Server section missing')
        return None
    
    if len(user_settings['server']) in [0, 2]:
        my_output.error('Invalid server count')
        return None

    if len(user_settings['server']) == 1:
        user_settings['high_availability_mode'] = "None"
    else:
        user_settings['high_availability_mode'] = "Full"

    redfish_credentials = None
    if 'redfish_credentials' in user_settings:
        if 'username' not in user_settings['redfish_credentials'] or 'password' not in user_settings['redfish_credentials']:
            my_output.error('redfish.json username and password required')
            return None

        redfish_credentials = user_settings['redfish_credentials']

    kube_count = 0

    interfaces_macs = []
    for server in user_settings['server']:
        if 'hostname' not in server:
            my_output.error('Define server hostname')
            return None

        if 'kube' not in server:
            server['kube'] = False

        if server['kube']:
            kube_count += 1
            user_settings['management_ip'] = server['ssh']['ip']

        if 'role' not in server:
            server['role'] = 'auto-assign'

        if server['role'] not in ['auto-assign', 'master', 'worker']:
            my_output.error('Unsupported server role')
            return None

        if 'redfish' not in server:
            my_output.error('Define redfish for server')
            return None

        if 'endpoint_type' not in server['redfish']:
            server['redfish']['endpoint_type'] = 'ucsc'

        if server['redfish']['endpoint_type'] not in ['ucsc', 'bmc', 'fi']:
            my_output.error('Unsupported server redfish endpoint type')
            return None

        if server['redfish']['endpoint_type'] == 'fi':
            if 'inventory_type' not in server['redfish']:
                server['redfish']['inventory_type'] = 'Server'

            if server['redfish']['inventory_type'] not in ['Server']:
                my_output.error('Unsupported server redfish fi inventory type')
                return None
            
            if 'inventory_id' not in server['redfish']:
                my_output.error('redfish fi requires inventory_id')
                return None

        if 'endpoint_ip' not in server['redfish']:
            my_output.error('server.redfish.ip required')
            return None

        if not ip_helper.is_valid_ipv4_address(server['redfish']['endpoint_ip']):
            my_output.error('server.redfish.endpoint_ip invalid: %s' % (server['redfish']['endpoint_ip']))
            return None

        if 'endpoint_port' not in server['redfish']:
            server['redfish']['endpoint_port'] = 443

        if 'username' not in server['redfish'] and redfish_credentials is None:
            my_output.error('server.redfish.username required')
            return None

        if 'username' not in server['redfish']:
            server['redfish']['username'] = redfish_credentials['username']

        if 'password' not in server['redfish'] and redfish_credentials is None:
            my_output.error('server.redfish.password required')
            return None

        if 'password' not in server['redfish']:
            server['redfish']['password'] = redfish_credentials['password']

        if 'ssh' not in server:
            my_output.error('server.ssh required')
            return None

        if 'username' not in server['ssh']:
            server['ssh']['username'] = 'core'

        if 'ip' not in server['ssh']:
            my_output.error('server.ssh.ip required')
            return None

        if not ip_helper.is_valid_ipv4_address(server['ssh']['ip']):
            my_output.error('server.ssh.ip invalid: %s' % (server['ssh']['ip']))
            return None

        if not ip_helper.is_ipv4_in_cidr(server['ssh']['ip'], user_settings['machine_network_gateway']):
            my_output.error('server.ssh.ip %s must be in cidr %s: %s' % (server['ssh']['ip'], user_settings['machine_network_gateway']))
            return None

        if 'interface' not in server:
            my_output.error('server.interface required')
            return None

        if not isinstance(server['interface'], list):
            my_output.error('server.interface list required')
            return None

        if len(server['interface']) == 0:
            my_output.error('server.interface list required')
            return None

        server['kube_interface_count'] = 0
        server['interface_macs'] = []
        server['interface_names'] = []
        server['group_interface'] = {}

        if 'group' not in server:
            server['group'] = []

        server['group_ids'] = []
        for group in server['group']:
            if 'id' not in group:
                my_output.error('server.group.id required')
                return None
            
            if not isinstance(group['id'], int):
                my_output.error('server.group.id must be integer')
                return None
            
            if group['id'] <= 0:
                my_output.error('server.group.id must be gt 1')
                return None
            
            if group['id'] in server['group_ids']:
                my_output.error('server.group.id must be unique')
                return None
            
            server['group_ids'].append(
                group['id']
            )

        for interface in server['interface']:
            if 'name' not in interface:
                my_output.error('server.interface.name required')
                return None

            if interface['name'] in server['interface_names']:
                my_output.error('server.interface.name must be unique')
                return None
            
            server['interface_names'].append(interface['name'])

            if 'mac' not in interface:
                my_output.error('server.interface.mac required')
                return None
            
            if not ip_helper.is_mac_address(interface['mac']):
                my_output.error('server.interface.mac required')
                return None
            
            if interface['mac'] in interfaces_macs:
                my_output.error('server.interface.mac must be unique across servers: %s' % (interface['mac']))
                return None

            interfaces_macs.append(interface['mac'])

            if interface['mac'] in server['interface_macs']:
                my_output.error('server.interface.mac must be unique per server: %s' % (interface['mac']))
                return None
            
            server['interface_macs'].append(interface['mac'])

            if 'group' not in interface:
                interface['group'] = None

            if interface['group'] is None:
                server['kube_interface_count'] += 1
            
            if interface['group'] is not None:
                if interface['group'] not in server['group_ids']:
                    my_output.error('server.interface.group must be defined in server.group')
                    return None
                
                if interface['group'] not in server['group_interface']:
                    server['group_interface'][interface['group']] = {}
                    server['group_interface'][interface['group']]['interface'] = []
                    server['group_interface'][interface['group']]['interface_count'] = 0
                
                group_interface = {}
                group_interface['name'] = interface['name']
                group_interface['mac'] = interface['mac']
                server['group_interface'][interface['group']]['interface'].append(
                    group_interface
                )
                server['group_interface'][interface['group']]['interface_count'] += 1

            if 'aci' in interface:
                if not isinstance(interface['aci'], dict):
                    my_output.error('server.interface.aci dict required')
                    return None
                
                if 'apic' not in interface['aci']:
                    my_output.error('server.interface.aci.apic required')
                    return None
                
                if 'node' not in interface['aci']:
                    my_output.error('server.interface.aci.node required')
                    return None

                if 'port' not in interface['aci']:
                    my_output.error('server.interface.aci.port required')
                    return None

        if server['kube_interface_count'] > 1:
            if server['kube_interface_count'] % 2:
                my_output.error('server.interface list required with 1 or even number of elements')
                return None

            if 'bond' not in server:
                server['bond'] = 'bond0'

            if 'bond_mode' not in server:
                server['bond_mode'] = '802.3ad'

            if 'lacp_rate' not in server:
                server['lacp_rate'] = 'slow'

        for group in server['group']:
            if server['group_interface'][group['id']]['interface_count'] == 0:
                my_output.error('No interface defined for group %s' % (group['id']))
                return None
            
            if server['group_interface'][group['id']]['interface_count'] > 1:
                if server['group_interface'][group['id']]['interface_count'] % 2:
                    my_output.error('server.interface list in group %s required with 1 or even number of elements' % (group['id']))                    
                    return None

                group['bond'] = 'bond%s' % (group['id'])

                if 'bond_mode' not in group:
                    group['bond_mode'] = '802.3ad'

                if 'lacp_rate' not in group:
                    group['lacp_rate'] = 'slow'

            if 'ip' in group:
                if not ip_helper.is_valid_ipv4_cidr(group['ip']):
                    my_output.error('Group %s ip %s must be cidr format' % (group['id'], group['ip']))
                    return None
            
            if 'route' not in group:
                group['route'] = []

            if len(group['route']) > 1 and 'ip' not in group:
                my_output.error('Group %s ip required if routes defined' % (group['id']))
                return None
            
            for route in group['route']:
                if 'cidr' not in route:
                    my_output.error('Group %s route must have cidr property' % (group['id']))
                    return None

                if not ip_helper.is_valid_ipv4_cidr(route['cidr']):
                    my_output.error('Group %s route cidr %s invalid' % (group['id'], route['cidr']))
                    return None

                if 'nh' not in route:
                    my_output.error('Group %s route must have nh property' % (group['id']))
                    return None

                if not ip_helper.is_valid_ipv4_address(route['nh']):
                    my_output.error('Group %s route nh %s invalid' % (group['id'], route['nh']))
                    return None

                if not ip_helper.is_ipv4_in_cidr(route['nh'], group['ip']):
                    my_output.error('Group %s route nh %s not in cidr %s' % (group['id'], route['nh'], group['ip']))
                    return None

        if 'nmstate' not in server:
            my_output.error('define nmstate reference')
            return None

        nmstate_filename = os.path.join(
            user_settings['directory'],
            server['nmstate']
        )
        if not os.path.isfile(nmstate_filename):
            my_output.error('nmstate file not found: %s' % (nmstate_filename))
            return None

        content = file_helper.get_file_text(
            nmstate_filename
        )
        if content is None:
            my_output.error('nmstate file read failed: %s' % (nmstate_filename))
            return None

        if 'variables' not in server:
            server['variables'] = {}

        if 'bond' in server:
            server['variables']['BOND'] = server['bond']

        if 'vlan' in server:
            server['variables']['VLAN'] = server['vlan']

        if 'bond_mode' in server:
            server['variables']['BOND_MODE'] = server['bond_mode']

        if 'lacp_rate' in server:
            server['variables']['LACP_RATE'] = server['lacp_rate']

        server['variables']['IP'] = server['ssh']['ip']
        server['variables']['PREFIX'] = user_settings['machine_network_gateway'].split('/')[1]
        server['variables']['GW'] = user_settings['machine_network_gateway'].split('/')[0]

        index = 1
        for item in user_settings['dns_search'].split(','):
            server['variables']['DNS_SEARCH_%s' % (index)] = item
            index += 1

        if len(user_settings['dns_search'].split(',')) == 1:
            server['variables']['DNS_SEARCH'] = user_settings['dns_search']

        index = 1
        for item in user_settings['dns_ip'].split(','):
            server['variables']['DNS_IP_%s' % (index)] = item
            index += 1

        if len(user_settings['dns_ip'].split(',')) == 1:
            server['variables']['DNS_IP'] = user_settings['dns_ip']

        if server['kube_interface_count'] == 1:
            server['variables']['IFNAME'] = server['interface'][0]['name']

        if server['kube_interface_count'] > 1:
            index = 1
            for item in server['interface']:
                if item['group'] is None:
                    server['variables']['BOND_MEMBER_%s' % (index)] = item['name']
                    index += 1

        for group_id in server['group_interface']:
            if server['group_interface'][group_id]['interface_count'] == 1:
                server['variables']['GROUP_%s_IFNAME' % (group_id)] = server['group_interface'][group_id]['interface'][0]['name']

            if server['group_interface'][group_id]['interface_count'] > 1:
                index = 1
                for interface in server['group_interface'][group_id]['interface']:
                    server['variables']['GROUP_%s_BOND_MEMBER_%s' % (group_id, index)] = interface['name']
                    index += 1

        for group in server['group']:
            if 'vlan' in group:
                server['variables']['GROUP_%s_VLAN' % (group['id'])] = group['vlan']

            if 'bond' in group:
                server['variables']['GROUP_%s_BOND' % (group['id'])] = group['bond']

            if 'bond_mode' in group:
                server['variables']['GROUP_%s_BOND_MODE' % (group['id'])] = group['bond_mode']

            if 'lacp_rate' in group:
                server['variables']['GROUP_%s_LACP_RATE' % (group['id'])] = group['lacp_rate']
            
            if 'ip' in group:
                server['variables']['GROUP_%s_IP' % (group['id'])] = group['ip'].split('/')[0]
                server['variables']['GROUP_%s_PREFIX' % (group['id'])] = group['ip'].split('/')[1]

            route_index = 1
            for route in group['route']:
                server['variables']['GROUP_%s_CIDR_%s' % (group['id'], route_index)] = route['cidr']
                server['variables']['GROUP_%s_NH_%s' % (group['id'], route_index)] = route['nh']
                route_index += 1

        content = template_handler.replace_attributes(
            content,
            server['variables']
        )
        if content is None:
            my_output.error('nmstate variables replacemet failed for server %s' % (server['hostname']))
            return None

        if template_handler.is_template_attributes(content):
            my_output.error('nmstate variables replacemet missing for server %s' % (server['hostname']))
            my_output.default(json.dumps(server['variables'], indent=4))
            return None

        my_output.debug('Server: %s' % (server['hostname']))
        my_output.debug(content, wrap='~~~', before_newline=True, after_newline=True)
        server['network_yaml'] = '\r\n'.join(content.split('\n'))

    if kube_count == 0:
        user_settings['server'][0]['kube'] = True
        user_settings['management_ip'] = user_settings['server'][0]['ssh']['ip']

    if kube_count > 1:
        my_output.error('Define one server with kube:true')
        return None

    if len(user_settings['server']) == 1:
        user_settings['api'] = user_settings['server'][0]['ssh']['ip']
        user_settings['ingress'] = user_settings['server'][0]['ssh']['ip']
    else:
        for key in ['api', 'ingress']:
            if key not in user_settings:
                my_output.error('Key %s missing for multinode cluster' % (key))
                return None

    return user_settings


def validate_settings(user_settings, my_output):
    if 'settings' not in user_settings:
        user_settings['settings'] = {}

    defaults = {}
    defaults['server_force_virtual_media_eject'] = True
    defaults['server_list_virtual_media_on_failure'] = True

    for key in defaults:
        if key not in user_settings['settings']:
            user_settings['settings'][key] = defaults[key]

    bool_settings = [
        'server_force_virtual_media_eject',
        'server_list_virtual_media_on_failure'
    ]
    for key in bool_settings:
        if not isinstance(user_settings['settings'][key], bool):
            my_output.error('settings.%s must be true or false', key)
            return None

    return user_settings


def validate_iso(user_settings, my_output):
    if 'iso' in user_settings and isinstance(user_settings['iso'], str):
        mode = user_settings['iso']
        user_settings['iso'] = {}
        user_settings['iso']['mode'] = mode

    if 'iso' not in user_settings:
        user_settings['iso'] = {}

    iso_defaults = {}
    iso_defaults['mode'] = 'minimal'
    iso_defaults['check_ssl'] = True
    iso_defaults['timeout'] = 600
    iso_defaults['core'] = None
    iso_defaults['manual'] = False
    iso_defaults['ip'] = None
    iso_defaults['username'] = None
    iso_defaults['password'] = None
    iso_defaults['ssh_public_key'] = None
    iso_defaults['exec'] = 'detect'
    iso_defaults['image'] = 'quay.io/coreos/coreos-installer:release'
    for key in iso_defaults:
        if key not in user_settings['iso']:
            user_settings['iso'][key] = iso_defaults[key]

    if user_settings['iso']['mode'] not in ['minimal', 'full']:
        my_output.error('Invalid iso.mode value [%s]. Expected minimal or full.' % (user_settings['iso']['mode']))
        return None

    if not isinstance(user_settings['iso']['check_ssl'], bool):
        my_output.error('Invalid iso.check_ssl value [%s]. Expected boolean.' % (user_settings['iso']['check_ssl']))
        return None

    if not isinstance(user_settings['iso']['manual'], bool):
        my_output.error('Invalid iso.manual value [%s]. Expected boolean.' % (user_settings['iso']['manual']))
        return None

    if not isinstance(user_settings['iso']['timeout'], int):
        my_output.error('Invalid iso.timeout value [%s]. Expected boolean.' % (user_settings['iso']['timeout']))
        return None

    if user_settings['iso']['core'] is not None and not isinstance(user_settings['iso']['core'], str):
        my_output.error('Invalid iso.core value [%s]. Expected string if defined.' % (user_settings['iso']['core']))
        return None

    if user_settings['iso']['core'] is not None:
        user_settings['iso']['mode'] = 'full'
    
        if user_settings['iso']['exec'] not in ['docker', 'podman', 'detect']:
            my_output.error('Invalid iso.exec value [%s]. Expected detect, docker or podman if defined.' % (user_settings['iso']['exec']))
            return None

        if user_settings['iso']['ip'] != 'localhost':
            if not ip_helper.is_valid_ipv4_address(user_settings['iso']['ip']):
                my_output.error('iso.ip invalid')
                return None

            if 'username' not in user_settings['iso']:
                my_output.error('iso.username required')
                return None

            if 'password' not in user_settings['iso']:
                user_settings['iso']['password'] = None

            if 'ssh_public_key' not in user_settings['iso']:
                user_settings['web_server']['iso'] = None

            if user_settings['iso']['password'] is None and user_settings['iso']['ssh_public_key'] is None:
                my_output.error('iso requires either password or ssh_public_key property')
                return None

            if user_settings['iso']['password'] is not None and user_settings['iso']['ssh_public_key'] is not None:
                my_output.error('iso requires either password or ssh_public_key property')
                return None

    return user_settings


def run(user_settings, my_output, log_id):   
    my_output.default('- base')
    user_settings = validate_base(user_settings, my_output, log_id)
    if user_settings is None:
        return None
        
    my_output.default('- iso')
    user_settings = validate_iso(user_settings, my_output)
    if user_settings is None:
        return None
    
    my_output.default('- cilium')
    user_settings = validate_cilium(user_settings, my_output)
    if user_settings is None:
        return None

    my_output.default('- server')
    user_settings = validate_server(user_settings, my_output, log_id)
    if user_settings is None:
        return None

    my_output.default('- web server')
    user_settings = validate_web(user_settings, my_output)
    if user_settings is None:
        return None

    my_output.default('- tasks')
    user_settings = validate_tasks(user_settings, my_output)
    if user_settings is None:
        return None

    my_output.default('- settings')
    user_settings = validate_settings(user_settings, my_output)
    if user_settings is None:
        return None

    return user_settings
