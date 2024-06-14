import os
import socket
import traceback

import click

from lib import context
from lib import file_helper
from lib import iaccount_helper
from lib import ip_helper
from lib import my_servers_helper
from lib import settings_helper

from lib.intersight import organization
from lib.intersight import scu
from lib.intersight import os_image
from lib.intersight import hcl_operating_system
from lib.intersight import hcl_operating_system_vendor

from lib.aci import apic
from lib.aci import settings as aci_settings
from lib.k8s import settings as k8s_settings
from lib.k8s import main as k8s
from lib.kubevirt import main as kubevirt
from lib.osp import settings as osp_settings
from lib.osp import main as osp

from lib.nexus import settings as nexus_settings
from lib.nexus import nxapi
from lib.nso import settings as nso_settings
from lib.nso import main as nso
from lib.ocp import settings as ocp_settings
from lib.ocp import main as ocp
from lib.ocp.vm import validate as ocp_deployment_validate
from lib.ucsm import settings as ucsm_settings
from lib.vc import vcenter
from lib.vc import settings as vc_settings
from lib.linux import main as linux
from lib.linux import settings as linux_settings


def validate_iaccount(ctx, param, value):
    iaccount_handler = iaccount_helper.IntersightAccount()
    if not iaccount_handler.is_isctl():
        raise click.BadParameter('isctl not found')

    if value is None:
        raise click.BadParameter('Define iaccount value')


    if not iaccount_handler.is_iaccount_valid(value):
        iaccounts = iaccount_handler.get_iaccounts()
        print('Defined iaccounts:')
        for iaccount in iaccounts:
            print(iaccount['name'])

        raise click.BadParameter('Invalid iaccount value')

    iaccount_handler.set_default_iaccount(value)

    return value


def validate_organization(ctx, iaccount, organization_name):
    organization_handler = organization.Organization(iaccount, log_id=ctx.run_id)

    if len(organization_name) == 0:
        organizations = organization_handler.get_moids_dict()
        if len(organizations) == 0:
            ctx.busy = False
            ctx.my_output.error('No organizations found')
            return None

        if len(organizations) > 0:
            ctx.busy = False
            ctx.my_output.error('Multiple organizations found. Select single one')
            for key in organizations:
                ctx.my_output.default('- %s' % (organizations[key]))
            return None

        return list(organizations.keys())[0]

    organization_details = organization_handler.get_by_name(organization_name)
    if organization_details is None:
        ctx.busy = False
        ctx.my_output.error('Organization not found: %s' % (organization_name))
        return None

    return organization_details['Moid']


def validate_fqdn(value):
    try:
        address = socket.gethostbyname(value)
        if ip_helper.is_valid_ipv4_address(address):
            return True

    except BaseException:
        pass

    return False


def validate_ip(ctx, param, value):
    if value is not None and len(value) > 0:
        if not ip_helper.is_valid_ipv4_address(value):
            if not validate_fqdn(value):
                raise click.BadParameter('Invalid IPv4 address: %s' % (value))

    return value


def validate_ips(ctx, param, values):
    context_handler = context.Context()
    ips = []

    for value in values:
        if value is not None and len(value) > 0:

            if len(value.split('ctx:')) == 2:
                context_ips = context_handler.get(
                   value.split('ctx:')[1]
                )
                if context_ips is None:
                    raise click.BadParameter('Unknown context: %s' % (value.split('ctx:')[1]))

                for item in context_ips:
                    if not ip_helper.is_valid_ipv4_address(item):
                        if not validate_fqdn(item):
                            raise click.BadParameter('Invalid IPv4 address: %s' % (item))

                    ips.append(item)
            else:
                if not ip_helper.is_valid_ipv4_address(value):
                    if not validate_fqdn(value):
                        raise click.BadParameter('Invalid IPv4 address: %s' % (value))

                ips.append(value)

    return ips


def validate_ip_subnet(ctx, param, value):
    if len(value) > 0:
        if ip_helper.is_valid_ipv4_address(value):
            return value

        if ip_helper.is_valid_ipv4_cidr(value):
            return value

        raise click.BadParameter('Invalid IPv4 address or subnet: %s' % (value))

    return value


def validate_subnet(ctx, param, value):
    if len(value) > 0:
        if ip_helper.is_valid_ipv4_cidr(value):
            return value

        raise click.BadParameter('Invalid subnet: %s' % (value))

    return value


def validate_prefix_length(ctx, param, value):
    if value <= 0 or value >= 30:
        raise click.BadParameter('Invalid prefix length')
    return value


def validate_file_content(ctx, filename):
    if not os.path.isfile(filename):
        ctx.my_output.error('File %s not found' % (filename))
        return None

    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        return None

    return content


def validate_file(ctx, param, filename):
    if len(filename) == 0:
        raise click.BadParameter('Define filename')

    if not os.path.isfile(filename):
        raise click.BadParameter('File %s not found' % (filename))

    return filename


def validate_optional_file(ctx, param, filename):
    if len(filename) == 0:
        return None

    if not os.path.isfile(filename):
        raise click.BadParameter('File %s not found' % (filename))

    return filename


def validate_int_oper(ctx, param, value):
    if len(value) == 0:
        return value

    for prefix in ['ge', '>=', 'le', '<=', 'gt', '>', 'lt', '<', 'ne', '!=']:
        if value.startswith(prefix):
            try:
                int_value = int(value.lstrip(prefix))
                return value
            except BaseException:
                pass
            raise click.BadParameter('Wrong value: %s' % (value))

    try:
        int_value = int(value)
        return value
    except BaseException:
        pass

    raise click.BadParameter('Wrong value: %s' % (value))


def validate_group(ctx, param, value):
    my_servers_handler = my_servers_helper.MyServers()
    if not my_servers_handler.is_group(value):
        raise click.BadParameter('Group not found: %s' % (value))
    return value


def validate_group_serials(ctx, param, value):
    if len(value) == 0:
        return []

    my_servers_handler = my_servers_helper.MyServers()
    if not my_servers_handler.is_group(value):
        raise click.BadParameter('Group not found: %s' % (value))

    serials = my_servers_handler.get_group_serials(value)
    if serials is None or len(serials) == 0:
        raise click.BadParameter('No group members found: %s' % (value))

    return serials


def validate_group_oper(ctx, param, value):
    my_servers_handler = my_servers_helper.MyServers()
    if len(value) == 0:
        return None

    group_oper = {}
    if value.startswith('+'):
        group_oper['oper'] = 'add'
        group_oper['group'] = value.lstrip('+')

    if value.startswith('-'):
        group_oper['oper'] = 'del'
        group_oper['group'] = value.lstrip('-')

    if not value.startswith('-') and not value.startswith('+'):
        group_oper['oper'] = 'set'
        group_oper['group'] = value
        return group_oper

    if not my_servers_handler.is_group(group_oper['group']):
        raise click.BadParameter('Group not found: %s' % (value))

    return group_oper


def validate_filter_serials(ctx, param, value):
    if len(value) == 0:
        return []
    return value.split(',')


def validate_filter_ip(ctx, param, value):
    if len(value) == 0:
        return []

    ip_filter = []
    for item in value.split(','):
        if ip_helper.is_valid_ipv4_address(item):
            ip_filter.append(
                dict(
                    type='address',
                    value=item
                )
            )
            continue

        if ip_helper.is_valid_ipv4_cidr(item):
            ip_filter.append(
                dict(
                    type='subnet',
                    value=item
                )
            )
            continue

        raise click.BadParameter('Invalid IP address or subnet value: %s' % (item))

    return ip_filter


def validate_scu(ctx, iaccount, scu_name, required=True):
    if len(scu_name) == 0:
        if required:
            ctx.my_output.error('SCU value required')
            return None
        return scu_name

    scu_handler = scu.SoftwareConfigurationUtility(iaccount, log_id=ctx.run_id)
    scu_item = scu_handler.get_by_name(scu_name)
    if scu_item is None:
        ctx.my_output.error('SCU not found: %s' % (scu_name))
        return None

    return scu_item


def validate_os_image(ctx, iaccount, image_name, required=True):
    if len(image_name) == 0:
        if required:
            ctx.my_output.error('OS image value required')
            return None
        return image_name

    image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
    image_item = image_handler.get_by_name(image_name)
    if image_item is None:
        ctx.my_output.error('Image not found: %s' % (image_name))
        return None

    vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
    vendor_item = vendor_handler.get_by_name(image_item['Vendor'])
    if vendor_item is None:
        ctx.my_output.error('Image vendor not found: %s' % (image_item['Vendor']))
        return None
    image_item['VendorId'] = vendor_item['Moid']

    version_handler = hcl_operating_system.HclOperatingSystem(iaccount, log_id=ctx.run_id)
    version_item = version_handler.get_vendor_version(vendor_item['Moid'], image_item['Version'])
    if version_item is None:
        ctx.my_output.error('Image version not found: %s' % (image_item['Version']))
        return None

    image_item['VersionId'] = version_item['Moid']

    return image_item


def validate_chassis_ifm_filter(ctx, param, value):
    if value is None:
        ifm_filter = {}
        ifm_filter['enabled'] = False
        return ifm_filter

    if value.lower() in ['all', '.', '*']:
        ifm_filter = {}
        ifm_filter['enabled'] = True
        ifm_filter['path'] = None
        ifm_filter['id'] = None
        return ifm_filter

    if len(value.split(',')) > 1:
        raise click.BadParameter('Select module by ID or Path')

    if value.lower() == 'a':
        ifm_filter = {}
        ifm_filter['enabled'] = True
        ifm_filter['path'] = 'A'
        ifm_filter['id'] = None
        return ifm_filter

    if value.lower() == 'b':
        ifm_filter = {}
        ifm_filter['enabled'] = True
        ifm_filter['path'] = 'B'
        ifm_filter['id'] = None
        return ifm_filter

    try:
        ifm_module_id = int(value)
    except BaseException:
        ifm_module_id = None

    if ifm_module_id is None:
        raise click.BadParameter('Select path A or B')

    if ifm_module_id not in [1, 2]:
        raise click.BadParameter('Select module id 1 or 2')

    ifm_filter = {}
    ifm_filter['enabled'] = True
    ifm_filter['path'] = None
    ifm_filter['id'] = ifm_module_id

    return ifm_filter


def validate_chassis_fan_filter(ctx, param, value):
    fan_filter = {}
    fan_filter['enabled'] = value
    return fan_filter


def validate_chassis_power_filter(ctx, param, value):
    power_filter = {}
    power_filter['enabled'] = value
    return power_filter


def validate_chassis_node_filter(ctx, param, value):
    node_filter = {}
    node_filter['enabled'] = value
    return node_filter


def validate_chassis_port_filter(ctx, param, value):
    if len(value) == 0:
        port_filter = {}
        port_filter['enabled'] = False
        return port_filter

    port_filter = {}
    port_filter['enabled'] = True
    port_filter['type'] = None
    port_filter['state'] = None
    port_filter['module'] = None
    port_filter['node'] = None

    for parameter in value:
        if parameter.lower() in ['all', '.', '*']:
            return port_filter

        if len(parameter.split(':')) != 2:
            continue

        (param_type, param_value) = parameter.split(':')

        if param_type.lower() in ['t', 'type']:
            if param_value.lower() not in ['host', 'net']:
                raise click.BadParameter('Port type host or net')
            port_filter['type'] = param_value.lower()

        if param_type.lower() in ['s', 'state']:
            if param_value.lower() not in ['up', 'down']:
                raise click.BadParameter('Port state up or down')
            port_filter['state'] = param_value.lower()

        if param_type.lower() in ['m', 'module']:
            if param_value.lower() not in ['a', 'b', '1', '2']:
                raise click.BadParameter('Port path a/b or 1/2')
            port_filter['module'] = param_value.lower()

        if param_type.lower() in ['n', 'node']:
            if param_value.lower() in ['.', '*', 'all']:
                port_filter['node'] = -1
            else:
                node_id = None
                try:
                    node_id = int(param_value)
                except BaseException:
                    pass

                if node_id is None:
                    raise click.BadParameter('Node all or index')

                port_filter['node'] = node_id

    return port_filter


def validate_redfish_path(ctx, param, value):
    if value == '':
        return value

    if value.startswith('/redfish/v1/'):
        value = value.lstrip('/redfish/v1/')

    if value.startswith('/api-explorer/resources/redfish/v1/'):
        value = value.lstrip('/api-explorer/resources/redfish/v1/')

    return value


def validate_apic_name(ctx, param, value):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)
    if len(value) == 0:
        default_controller_name = aci_settings_handler.get_default_controller()
        if default_controller_name is None:
            return None

        return aci_settings_handler.get_apic_controller(default_controller_name)

    controller = aci_settings_handler.get_apic_controller(value)
    if controller is None:
        controllers = aci_settings_handler.get_apic_controller_names()
        if controllers is None:
            raise click.BadParameter('Invalid apic name')
        raise click.BadParameter('Invalid apic name. Define one of %s' % (','.join(controllers)))

    return controller


def validate_apic_any_name(ctx, param, value):
    if len(value) == 0:
        return []

    aci_settings_handler = aci_settings.ApicSettings(log_id=None)
    selected_controllers = []
    names = []

    for parameter in value.split(','):
        if parameter.lower() in ['any', 'all']:
            all_controllers = aci_settings_handler.get_apic_controllers()
            if all_controllers is not None:
                for controller in all_controllers:
                    if controller['name'] not in names:
                        names.append(
                            controller['name']
                        )
                        selected_controllers.append(
                            controller
                        )

            continue

        if parameter.startswith('dom:'):
            domain_controllers = aci_settings_handler.get_apic_domain_controllers(
                parameter[4:]
            )
            if domain_controllers is not None:
                for domain_controller in domain_controllers:
                    if domain_controller['name'] not in names:
                        names.append(
                            domain_controller['name']
                        )
                        selected_controllers.append(
                            domain_controller
                        )

            continue

        controller = aci_settings_handler.get_apic_controller(parameter)
        if controller is not None:
            aci_settings_handler.set_default_controller(
                controller['name']
            )

        if controller is None:
            controllers = aci_settings_handler.get_apic_controller_names()
            if controllers is None:
                raise click.BadParameter('Invalid apic name')
            controllers.append('any')
            raise click.BadParameter('Invalid apic name. Define one of %s' % (','.join(controllers)))

        if controller['name'] not in names:
            names.append(
                controller['name']
            )
            selected_controllers.append(
                controller
            )

    return selected_controllers


def validate_apic_controller(ctx, controller_obj, controller_ip, controller_port, controller_username, controller_password, show_selected=True, auto_connect=False, no_cache=False, debug=False):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)

    if controller_obj is None and len(controller_ip) == 0 and len(controller_username) == 0 and len(controller_password) == 0:
        controller_name = aci_settings_handler.get_default_controller()
        if controller_name is not None:
            controller_obj = aci_settings_handler.get_apic_controller(controller_name)

    if len(controller_ip) > 0 or len(controller_username) > 0 or len(controller_password) > 0:
        if len(controller_ip) == 0 or len(controller_username) == 0 or len(controller_password) == 0:
            ctx.my_output.error('Define controller name or ip/username/password')
            return None
    else:
        controller_ip = controller_obj['ip']
        controller_port = controller_obj['port']
        controller_username = controller_obj['username']
        controller_password = controller_obj['password']
        aci_settings_handler.set_default_controller(
            controller_obj['name']
        )

        if show_selected and ctx.output == 'default':
            ctx.my_output.default(
                aci_settings_handler.get_apic_controller_label(
                    controller_obj['name']
                )
            )

    apic_handler = apic.Apic(
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        apic_name=controller_obj['name'],
        log_id=ctx.run_id,
        no_cache=no_cache,
        debug=debug
    )

    if auto_connect:
        if not apic_handler.is_connected():
            ctx.my_output.error('Failed to connect to APIC')
            return None

    return apic_handler


def validate_apic_controllers(ctx, controller_objs, controller_ip, controller_port, controller_username, controller_password, show_selected=True, auto_connect=False, no_cache=False):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)

    if len(controller_objs) == 0 and len(controller_ip) == 0 and len(controller_username) == 0 and len(controller_password) == 0:
        controller_name = aci_settings_handler.get_default_controller()
        if controller_name is not None:
            controller_objs.append(
                aci_settings_handler.get_apic_controller(controller_name)
            )

    if len(controller_ip) > 0 and len(controller_username) > 0 and len(controller_password) > 0:
        controller_objs.append(
            dict(
                name=controller_ip,
                ip=controller_ip,
                port=controller_port,
                username=controller_username,
                password=controller_password
            )
        )

    if len(controller_objs) == 0:
        ctx.my_output.error('Select at least on APIC')
        return None

    apic_handlers = []
    names = []
    for controller_obj in controller_objs:
        controller_ip = controller_obj['ip']
        controller_port = controller_obj['port']
        controller_username = controller_obj['username']
        controller_password = controller_obj['password']

        apic_handler = apic.Apic(
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            apic_name=controller_obj['name'],
            log_id=ctx.run_id,
            no_cache=no_cache
        )

        if auto_connect:
            if not apic_handler.is_connected():
                ctx.my_output.error('Failed to connect to APIC')
                return None

        names.append(controller_obj['name'])
        apic_handlers.append(
            dict(
                name=controller_obj['name'],
                handler=apic_handler
            )
        )

    if show_selected and ctx.output == 'default':
        if len(names) > 0:
            for name in names:
                ctx.my_output.default(
                    aci_settings_handler.get_apic_controller_label(
                        name
                    )
                )

    return apic_handlers


def validate_apic_controllers_with_context_interfaces(ctx, context_interfaces):
    controller_names = []
    for context_interface in context_interfaces:
        apic_name = context_interface.split(':')[1]
        if apic_name not in controller_names:
            controller_names.append(apic_name)

    controller_objs = validate_apic_any_name(ctx, 'apic', ','.join(controller_names))
    apic_handlers = validate_apic_controllers(
        ctx,
        controller_objs,
        '',
        '',
        '',
        '',
        show_selected=False
    )
    if apic_handlers is None:
        return None

    for apic_handler in apic_handlers:
        node_names = []
        for context_interface in context_interfaces:
            if apic_handler['name'] == context_interface.split(':')[1]:
                node_name = apic_handler['handler'].get_node_name(
                    context_interface.split(':')[3].split('-')[1],
                    pod_id=context_interface.split(':')[2].split('-')[1]
                )
                if node_name not in node_names:
                    node_names.append(
                        node_name
                    )

        apic_handler['nodes'] = validate_apic_node_names(
            ctx,
            apic_handler['handler'],
            node_names,
            node_role='any'
        )
        if apic_handler['nodes'] is None:
            return None

    return apic_handlers


def validate_apic_controllers_with_nodes(ctx, controller_objs, controller_ip, controller_port, controller_username, controller_password, node_names, node_role, pod_id=None, no_cache=False):
    apic_handlers = validate_apic_controllers(
        ctx,
        controller_objs,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        show_selected=False,
        no_cache=no_cache
    )
    if apic_handlers is None:
        return None

    if len(apic_handlers) > 1:
        if len(node_names) == 0:
            node_names = ['any']

    if len(apic_handlers) == 1:
        if len(node_names) == 0 and node_role == 'any':
            aci_settings_handler = aci_settings.ApicSettings(log_id=None)
            node_name = aci_settings_handler.get_default_node(
                apic_handlers[0]['handler'].get_apic_ip()
            )
            if node_name is None:
                ctx.my_output.error('Define node name')
                return None
            node_names = [node_name]

    for apic_handler in apic_handlers:
        apic_handler['nodes'] = validate_apic_node_names(
            ctx,
            apic_handler['handler'],
            node_names,
            node_role,
            pod_id=pod_id
        )
        if apic_handler['nodes'] is None:
            return None

    return apic_handlers


def validate_apic_node_name(ctx, apic_handler, node_name, pod_id=None):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)

    if node_name is None:
        node_name = aci_settings_handler.get_default_node(
            apic_handler.get_apic_ip()
        )
        if node_name is None:
            ctx.my_output.error('Define node name')
            return None

    node_filter = []
    if pod_id is not None:
        node_filter.append(
            'pod:%s' % (pod_id)
        )

    node_filter.append(
        'name:*%s*' % (node_name.replace('*', ''))
    )

    nodes_info = apic_handler.get_nodes(
        node_filter=node_filter
    )

    if nodes_info is None or len(nodes_info) != 1:
        ctx.my_output.error(
            'Unique node name match failed: %s' % (node_name)
        )

        node_names = apic_handler.get_node_names(pod_id=pod_id)
        if node_names is not None:
            ctx.my_output.default('\nNode names:')
            for name in node_names:
                ctx.my_output.default('- %s' % (name))

        return None

    aci_settings_handler.set_default_node(
        apic_handler.get_apic_ip(),
        nodes_info[0]['name']
    )
    if ctx.output == 'default':
        ctx.my_output.default('Pod: %s' % (nodes_info[0]['podId']))
        ctx.my_output.default('Node: %s' % (nodes_info[0]['name']))

    return nodes_info[0]


def validate_apic_node_names(ctx, apic_handler, node_names, node_role, pod_id=None, silent=False):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)

    # Check default node name
    if len(node_names) == 0 and node_role == 'any':
        node_name = aci_settings_handler.get_default_node(
            apic_handler.get_apic_ip()
        )
        if node_name is None:
            ctx.my_output.error('Define node name')
            return None

        node_names = [node_name]

    node_filter = []
    role_filter = True

    if pod_id is not None:
        role_filter = False
        node_filter.append(
            'pod:%s' % (pod_id)
        )

    if node_role != 'any':
        node_filter.append(
            'role:%s' % (node_role)
        )
    else:
        role_filter = False
        node_filter.append(
            'role:!controller'
        )

    if 'any' not in node_names and len(node_names) > 0:
        role_filter = False
        new_node_names = []
        for node_name in node_names:
            new_node_names.append(
                '*%s*' % (node_name.replace('*', ''))
            )

        node_filter.append(
            'names:%s' % (','.join(new_node_names))
        )

    nodes_info = apic_handler.get_nodes(
        node_filter=node_filter
    )

    if nodes_info is None:
        ctx.my_output.error(
            'Failed to get nodes'
        )
        return None

    if len(nodes_info) == 0:
        ctx.my_output.error(
            'No node name match'
        )

        node_names = apic_handler.get_node_names(pod_id=pod_id)
        if node_names is not None and not silent:
            ctx.my_output.default('\nNode names:')
            for name in node_names:
                ctx.my_output.default('- %s' % (name))

        return None

    if len(nodes_info) == 1:
        aci_settings_handler.set_default_node(
            apic_handler.get_apic_ip(),
            nodes_info[0]['name']
        )
        if ctx.output == 'default' and not silent:
            ctx.my_output.default(
                aci_settings_handler.get_apic_controller_label(
                    apic_handler.get_apic_name()
                )
            )
            ctx.my_output.default('Pod: %s' % (nodes_info[0]['podId']))
            ctx.my_output.default('Node: %s' % (nodes_info[0]['name']))

    if len(nodes_info) > 1:
        if ctx.output == 'default' and not silent:
            nodes_count = apic_handler.get_node_count()
            ctx.my_output.default(
                aci_settings_handler.get_apic_controller_label(
                    apic_handler.get_apic_name()
                )
            )
            ctx.my_output.default('Pod: %s' % (nodes_info[0]['podId']))
            if len(nodes_info) == nodes_count:
                ctx.my_output.default('Node: all (#%s)' % (nodes_count))
                return nodes_info

            if role_filter:
                if node_role == 'spine':
                    ctx.my_output.default('Node: all spines (#%s)' % (len(nodes_info)))
                    return nodes_info

                if node_role == 'leaf':
                    ctx.my_output.default('Node: all leaves (#%s)' % (len(nodes_info)))
                    return nodes_info

            for node_info in nodes_info:
                ctx.my_output.default('- node: %s' % (node_info['name']))

    return nodes_info


def validate_apic_tenant_name(ctx, param, value):
    if len(value) == 0:
        return None

    tenant_name = {}
    if len(value.split('/')) == 1:
        tenant_name['tenant'] = None
        tenant_name['name'] = value
        return tenant_name

    if len(value.split('/')) == 2:
        tenant_name['tenant'] = value.split('/')[0]
        tenant_name['name'] = value.split('/')[1]
        return tenant_name

    raise click.BadParameter('Invalid name syntax')


def validate_apic_tenant_ap_name(ctx, param, value):
    if len(value) == 0:
        return None

    tenant_name = {}
    if len(value.split('/')) == 1:
        tenant_name['tenant'] = None
        tenant_name['ap'] = None
        tenant_name['name'] = value
        return tenant_name

    if len(value.split('/')) == 2:
        tenant_name['tenant'] = None
        tenant_name['ap'] = value.split('/')[0]
        tenant_name['name'] = value.split('/')[1]
        return tenant_name

    if len(value.split('/')) == 3:
        tenant_name['tenant'] = value.split('/')[0]
        tenant_name['ap'] = value.split('/')[1]
        tenant_name['name'] = value.split('/')[2]
        return tenant_name

    raise click.BadParameter('Invalid name syntax')


def validate_context(ctx, param, value):
    if len(value) == 0:
        return None

    context_handler = context.Context()
    user_context = {}
    user_context['key'] = value
    user_context['value'] = context_handler.get(value)
    if user_context['value'] is None:
        return None

    return user_context


def validate_nexus_name(ctx, param, value):
    if len(value) == 0:
        return None

    nexus_settings_handler = nexus_settings.NexusSettings(log_id=None)
    nexus_device = nexus_settings_handler.get_nexus_device(value)
    if nexus_device is None:
        devices = nexus_settings_handler.get_nexus_device_names()
        if devices is None:
            raise click.BadParameter('Invalid device name')
        raise click.BadParameter('Invalid device name. Define one of %s' % (','.join(devices)))

    return nexus_device


def validate_nexus_any_name(ctx, param, value):
    nexus_settings_handler = nexus_settings.NexusSettings(log_id=None)
    selected_devices = []
    names = []

    if len(value) == 0:
        default_nexus = nexus_settings_handler.get_default_nexus_device()
        if default_nexus is not None:
            value = default_nexus

    for parameter in value.split(','):
        if parameter.lower() in ['any', 'all']:
            all_devices = nexus_settings_handler.get_nexus_devices()
            if all_devices is not None:
                for device in all_devices:
                    if device['name'] not in names:
                        names.append(
                            device['name']
                        )
                        selected_devices.append(
                            device
                        )

            continue

        if parameter.startswith('dom:'):
            domain_devices = nexus_settings_handler.get_nexus_domain_devices(
                parameter[4:]
            )
            if domain_devices is not None:
                for domain_device in domain_devices:
                    if domain_device['name'] not in names:
                        names.append(
                            domain_device['name']
                        )
                        selected_devices.append(
                            domain_device
                        )

            continue

        device = nexus_settings_handler.get_nexus_device(parameter)
        if device is not None:
            nexus_settings_handler.set_default_nexus_device(
                device['name']
            )

        if device is None:
            devices = nexus_settings_handler.get_nexus_device_names()
            if devices is None:
                raise click.BadParameter('Invalid nexus name')
            devices.append('any')
            raise click.BadParameter('Invalid nexus name. Define one of %s' % (','.join(devices)))

        if device['name'] not in names:
            names.append(
                device['name']
            )
            selected_devices.append(
                device
            )

    return selected_devices


def validate_nexus_device(ctx, device_obj, device_ip, device_username, device_password, debug=False):
    nexus_settings_handler = nexus_settings.NexusSettings(log_id=None)

    if device_obj is None and len(device_ip) == 0 and len(device_username) == 0 and len(device_password) == 0:
        device_name = nexus_settings_handler.get_default_nexus_device()
        if device_name is not None:
            device_obj = nexus_settings_handler.get_nexus_device(device_name)

    device_name = None
    if device_obj is not None:
        device_ip = device_obj['ip']
        device_username = device_obj['username']
        device_password = device_obj['password']
        device_name = device_obj['name']
        nexus_settings_handler.set_default_nexus_device(
            device_obj['name']
        )

        if ctx.output == 'default':
            ctx.my_output.default('Switch: %s' % (device_obj['name']))

    if device_obj is None:
        if len(device_ip) == 0 or len(device_username) == 0 or len(device_password) == 0:
            ctx.my_output.error('Define device name or ip/username/password')
            return None

    nexus_handler = nxapi.NxApi(
        device_ip,
        device_username,
        device_password,
        name=device_name,
        log_id=ctx.run_id,
        debug=debug
    )

    if not nexus_handler.is_connected(autoconnect=True):
        ctx.my_output.error('Failed to connect to device')
        return None

    return nexus_handler


def validate_nexus_devices(ctx, device_objs, device_ip, device_username, device_password, show_selected=True, debug=False, cache_enabled=False):
    nexus_settings_handler = nexus_settings.NexusSettings(log_id=None)

    if len(device_objs) == 0 and len(device_ip) == 0 and len(device_username) == 0 and len(device_password) == 0:
        device_name = nexus_settings_handler.get_default_nexus_device()
        if device_name is not None:
            device_objs.append(
                nexus_settings_handler.get_nexus_device(device_name)
            )

    if len(device_ip) > 0 and len(device_username) > 0 and len(device_password) > 0:
        device_objs.append(
            dict(
                name=device_ip,
                ip=device_ip,
                username=device_username,
                password=device_password
            )
        )

    if len(device_objs) == 0:
        ctx.my_output.error('Select at least one device')
        return None

    device_handlers = []
    names = []
    for device_obj in device_objs:
        device_name = device_obj['name']
        device_ip = device_obj['ip']
        device_username = device_obj['username']
        device_password = device_obj['password']

        nexus_handler = nxapi.NxApi(
            device_ip,
            device_username,
            device_password,
            name=device_name,
            log_id=ctx.run_id,
            debug=debug,
            cache_enabled=cache_enabled
        )

        names.append(device_obj['name'])
        device_handlers.append(
            dict(
                name=device_obj['name'],
                handler=nexus_handler
            )
        )

    if show_selected and ctx.output == 'default':
        if len(names) > 0:
            ctx.my_output.default('Device: %s' % (','.join(names)))

    return device_handlers


def validate_ucsm_name(ctx, param, value):
    if len(value) == 0:
        raise click.BadParameter('Define ucsm name')

    ucsm_settings_handler = ucsm_settings.UcsmSettings(log_id=None)
    ucsm_manager = ucsm_settings_handler.get_ucsm_manager(value)
    if ucsm_manager is None:
        raise click.BadParameter('Invalid ucsm name')

    return ucsm_manager


def validate_vc_name(ctx, param, value):
    if len(value) == 0:
        return None

    vc_settings_handler = vc_settings.VcSettings(log_id=None)
    instance = vc_settings_handler.get_vc_instance(value)
    if instance is None:
        raise click.BadParameter('Invalid vcenter name')

    return instance


def validate_vc_any_name(ctx, param, value):
    if len(value) == 0:
        return None

    vc_settings_handler = vc_settings.VcSettings(log_id=None)

    if value.lower() in ['any', 'all']:
        return vc_settings_handler.get_vc_instances()

    instance = vc_settings_handler.get_vc_instance(value)
    if instance is None:
        raise click.BadParameter('Invalid vcenter name')

    return instance


def validate_vcenter(ctx, vcenter_obj, vcenter_ip, vcenter_username, vcenter_password, vcenter_port=443):
    vc_settings_handler = vc_settings.VcSettings(log_id=ctx.run_id)

    if vcenter_obj is None and len(vcenter_ip) == 0 and len(vcenter_username) == 0 and len(vcenter_password) == 0:
        instance_name = vc_settings_handler.get_default_instance()
        if instance_name is not None:
            vcenter_obj = vc_settings_handler.get_vc_instance(instance_name)

    if vcenter_obj is not None:
        vcenter_ip = vcenter_obj['ip']
        vcenter_port = vcenter_obj['port']
        vcenter_username = vcenter_obj['username']
        vcenter_password = vcenter_obj['password']
        vc_settings_handler.set_default_instance(
            vcenter_obj['name']
        )

        if ctx.output == 'default':
            ctx.my_output.default('vcenter: %s' % (vcenter_obj['name']))

    if vcenter_obj is None:
        if len(vcenter_ip) == 0 or len(vcenter_username) == 0 or len(vcenter_password) == 0:
            ctx.my_output.error('Define vcenter name or ip/username/password')
            return None

    vc_handler = vcenter.Vcenter(
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        port=vcenter_port,
        log_id=ctx.run_id
    )

    if not vc_handler.is_vc_connected():
        ctx.my_output.error('Failed to connect to vcenter')
        return None

    return vc_handler


def validate_vcenters(ctx, vcenter_objs):
    vc_settings_handler = vc_settings.VcSettings(log_id=None)

    vc_handlers = []
    for vcenter_obj in vcenter_objs:
        vcenter_ip = vcenter_obj['ip']
        vcenter_port = vcenter_obj['port']
        vcenter_username = vcenter_obj['username']
        vcenter_password = vcenter_obj['password']

        vcenter_handler = vcenter.Vcenter(
            vcenter_ip,
            vcenter_username,
            vcenter_password,
            port=vcenter_port,
            log_id=ctx.run_id
        )

        if not vcenter_handler.is_vc_connected():
            ctx.my_output.error('Failed to connect to vcenter')
            return None

        vc_handlers.append(
            dict(
                name=vcenter_obj['name'],
                handler=vcenter_handler
            )
        )

    return vc_handlers


def empty_string_to_none(ctx, param, value):
    if len(value) == 0:
        return None

    return value


def validate_ocp_cluster(ctx, cluster_name, verbose=False, debug=False, silent=False):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=ctx.run_id)

    if cluster_name is None or cluster_name == '':
        cluster_name = ocp_settings_handler.get_default_cluster()
        if cluster_name is None:
            ctx.my_output.error('Define ocp cluster name')
            return None

        if ctx.output == 'default' and not silent:
            ctx.my_output.default('Cluster: %s' % (cluster_name))

    cluster_obj = ocp_settings_handler.get_ocp_cluster(cluster_name, strict_match=False)
    if cluster_obj is None:
        ctx.my_output.error('Define valid ocp cluster name')
        names = ocp_settings_handler.get_ocp_cluster_names()
        if names is not None:
            for name in names:
                ctx.my_output.default('- %s' % (name))

        return None

    ocp_settings_handler.set_default_cluster(
        cluster_obj['name']
    )

    ocp_handler = ocp.Ocp(
        cluster_obj['name'],
        verbose=verbose,
        debug=debug,
        log_id=ctx.run_id
    )

    return ocp_handler


def get_ocp_cluster_settings(ctx, cluster_name, silent=False):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=ctx.run_id)

    if cluster_name is None or cluster_name == '':
        cluster_name = ocp_settings_handler.get_default_cluster()
        if cluster_name is None:
            ctx.my_output.error('Define ocp cluster name')
            names = ocp_settings_handler.get_ocp_cluster_names()
            if names is not None:
                for name in names:
                    ctx.my_output.default('- %s' % (name))
            return None

        if ctx.output == 'default' and not silent:
            ctx.my_output.default('Cluster: %s' % (cluster_name))

        settings = ocp_settings_handler.get_ocp_cluster(cluster_name)
        return settings

    settings = ocp_settings_handler.get_ocp_cluster(cluster_name, strict_match=False)
    if settings is None:
        ctx.my_output.error('Define valid ocp cluster name')
        names = ocp_settings_handler.get_ocp_cluster_names()
        if names is not None:
            for name in names:
                ctx.my_output.default('- %s' % (name))
        return None

    ocp_settings_handler.set_default_cluster(
        settings['name']
    )

    return settings


def validate_ocp_cluster_settings(ctx, cluster_name, silent=False, mandatory=[]):
    settings = get_ocp_cluster_settings(
        ctx,
        cluster_name,
        silent=silent
    )
    if settings is None:
        return None

    for item in mandatory:
        if item not in settings:
            ctx.my_output.error('%s not defined for cluster %s' % (item, settings['name']))
            return None

    return settings


def validate_ocp_node(ctx, ocp_handler, node_name):
    if node_name == '':
        ctx.my_output.error('Define ocp cluster node name')
        return False

    if not ocp_handler.is_node(node_name):
        ctx.my_output.error('Define valid ocp cluster node name')
        names = ocp_handler.get_nodes_name()
        if names is not None:
            for name in names:
                ctx.my_output.default('- %s' % (name))

        return False

    return True


def validate_ocp_cluster_name(ctx, param, cluster_name):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=None)
    if cluster_name == '':
        cluster_name = ocp_settings_handler.get_default_cluster()
        if cluster_name is None:
            raise click.BadParameter('Define OCP cluster name')

    cluster_obj = ocp_settings_handler.get_ocp_cluster(cluster_name, strict_match=False)
    if cluster_obj is None:
        raise click.BadParameter('Define valid OCP cluster name')

    return cluster_obj['name']


def select_ocp_name(ctx):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=None)
    names = ocp_settings_handler.get_ocp_cluster_names()
    if len(names) == 0:
        ctx.my_output.error('No OpenShift cluster defined')
        return None

    ctx.my_output.default('Select OpenShift Cluster', underline=True)
    for name in names:
        ctx.my_output.default('- %s' % (name))

    selected = input('Value: ')
    if len(selected) == 0:
        return None

    if selected not in names:
        return None

    return selected


def validate_ocp_namespace_name(ctx, param, value):
    if len(value) == 0:
        return None

    namespace_name = {}
    if len(value.split('/')) == 1:
        namespace_name['namespace'] = None
        namespace_name['name'] = value
        return namespace_name

    if len(value.split('/')) == 2:
        namespace_name['namespace'] = value.split('/')[0]
        namespace_name['name'] = value.split('/')[1]
        return namespace_name

    raise click.BadParameter('Invalid name syntax')


def validate_ocp_vm_namespace(ctx, ocp_handler, namespace, vm_name):
    if namespace == '':
        vm_filter = ['name:%s' % (vm_name)]
        vms_mo = ocp_handler.k8s_handler.get_virtual_machines(
            object_filter=vm_filter,
            return_mo=True,
            cache_enabled=False
        )
        if vms_mo is None or len(vms_mo) == 0:
            ctx.busy = False
            ctx.my_output.error(
                'Virtual machine %s not found in any namespace' % (vm_name)
            )
            return None

        if len(vms_mo) > 1:
            ctx.busy = False
            ctx.my_output.error(
                'Multiple virtual machines found - define namespace'
            )
            for vm_mo in vms_mo:
                ctx.my_output.default(
                    '- %s' % (vm_mo['metadata']['namespace'])
                )
            return None

        namespace = vms_mo[0]['metadata']['namespace']
    else:
        if not ocp_handler.k8s_handler.is_virtual_machine(namespace, vm_name, cache_enabled=False):
            ctx.busy = False
            ctx.my_output.error(
                'Virtual machine %s/%s not found' % (
                    namespace,
                    vm_name
                )
            )
            return None

    ctx.busy = False

    ctx.my_output.default(
        'Virtual machine %s/%s found' % (
            namespace,
            vm_name
        )
    )

    return namespace


def validate_ocp_vm_yaml_file(ctx, filename):
    if filename == '':
        ctx.my_output.error('Define virtual machine deployment yaml filename')
        return None

    content = file_helper.get_file_yaml(
        filename
    )
    if content is None:
        ctx.my_output.error(
            'File read failed: %s' % (filename)
        )
        return None

    if 'kind' not in content:
        ctx.my_output.error('Invalid yaml file content')
        return None

    if content['kind'] not in ['VirtualMachineDeployment', 'VirtualMachine']:
        ctx.my_output.error('Unsupported kind property')
        return None

    ocp_deployment_validate_handler = ocp_deployment_validate.OcpDeploymentValidate(log_id=ctx.run_id)

    if content['kind'] == 'VirtualMachineDeployment':
        return ocp_deployment_validate_handler.validate(filename)

    if content['kind'] == 'VirtualMachine':
        deployment = 'kind: VirtualMachineDeployment'
        deployment = '%s\ndeployment:' % (deployment)
        deployment = '%s\n  name: %s' % (deployment, content['metadata']['name'])
        deployment = '%s\n  namespace: %s' % (deployment, content['metadata']['namespace'])
        deployment = '%s\n  vm: %s' % (deployment, os.path.basename(filename))
        new_filename = file_helper.set_tmp_file(deployment)
        if new_filename is None:
            ctx.my_output.error('Failed to prepare deployment file')
            return None

        return ocp_deployment_validate_handler.validate(
            new_filename,
            chdir=os.path.dirname(filename)
        )

    return None


def validate_ncs_name(ctx, param, value):
    if len(value) == 0:
        return None

    nso_settings_handler = nso_settings.NsoSettings(log_id=None)
    controller = nso_settings_handler.get_nso_ncs(value)
    if controller is None:
        raise click.BadParameter('Invalid ncs name')

    return controller


def validate_nso_nfvo(ctx, ncs_obj, ncs_protocol, ncs_ip, ncs_port, ncs_username, ncs_password, restconf_enabled, nfvo):
    nso_settings_handler = nso_settings.NsoSettings(log_id=ctx.run_id)

    if ncs_obj is None and len(ncs_ip) == 0 and len(ncs_username) == 0 and len(ncs_password) == 0:
        ncs_name = nso_settings_handler.get_default_ncs()
        if ncs_name is not None:
            ncs_obj = nso_settings_handler.get_nso_ncs(ncs_name)

    if ncs_obj is not None:
        ncs_protocol = ncs_obj['protocol']
        ncs_ip = ncs_obj['ip']
        ncs_port = ncs_obj['port']
        ncs_username = ncs_obj['username']
        ncs_password = ncs_obj['password']
        restconf_enabled = ncs_obj['restconf_enabled']
        nfvo = ncs_obj['nfvo']
        nso_settings_handler.set_default_ncs(
            ncs_obj['name']
        )

        if ctx.output == 'default':
            ctx.my_output.default('NCS: %s' % (ncs_obj['name']))

    if ncs_obj is None:
        if len(ncs_ip) == 0 or len(ncs_username) == 0 or len(ncs_password) == 0:
            ctx.my_output.error('Define ncs name or ip/username/password')
            return None

    nso_handler = nso.Nso(
        ncs_protocol,
        ncs_ip,
        ncs_port,
        username=ncs_username,
        password=ncs_password,
        restconf_enabled=restconf_enabled,
        nfvo=nfvo,
        log_id=ctx.run_id
    )

    if not nso_handler.is_connected():
        ctx.my_output.error('Failed to connect to NCS')
        return None

    return nso_handler


def validate_nso(ctx, ncs_obj, ncs_protocol, ncs_ip, ncs_port, ncs_username, ncs_password, restconf_enabled):
    nso_settings_handler = nso_settings.NsoSettings(log_id=ctx.run_id)

    if ncs_obj is None and len(ncs_ip) == 0 and len(ncs_username) == 0 and len(ncs_password) == 0:
        ncs_name = nso_settings_handler.get_default_ncs()
        if ncs_name is not None:
            ncs_obj = nso_settings_handler.get_nso_ncs(ncs_name)

    if ncs_obj is not None:
        ncs_protocol = ncs_obj['protocol']
        ncs_ip = ncs_obj['ip']
        ncs_port = ncs_obj['port']
        ncs_username = ncs_obj['username']
        ncs_password = ncs_obj['password']
        restconf_enabled = ncs_obj['restconf_enabled']
        nso_settings_handler.set_default_ncs(
            ncs_obj['name']
        )

        if ctx.output == 'default':
            ctx.my_output.default('NCS: %s' % (ncs_obj['name']))

    if ncs_obj is None:
        if len(ncs_ip) == 0 or len(ncs_username) == 0 or len(ncs_password) == 0:
            ctx.my_output.error('Define ncs name or ip/username/password')
            return None

    nso_handler = nso.Nso(
        ncs_protocol,
        ncs_ip,
        ncs_port,
        username=ncs_username,
        password=ncs_password,
        restconf_enabled=restconf_enabled,
        log_id=ctx.run_id
    )

    if not nso_handler.is_connected():
        ctx.my_output.error('Failed to connect to NCS')
        return None

    return nso_handler


def validate_xml_file(ctx, filename):
    if not os.path.isfile(filename):
        ctx.my_output.error('File %s not found' % (filename))
        return None

    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        return None

    return content


def validate_fabric(ctx, param, value):
    if len(value) == 0:
        return None

    aci_settings_handler = aci_settings.ApicSettings(log_id=None)
    fabrics = []
    for item in value:
        if len(item.split(':')) != 2:
            raise click.BadParameter('Expected fabric syntax is <type>:<name>')

        fabric_hint = {}
        fabric_hint['type'] = item.split(':')[0]
        if fabric_hint['type'] not in ['aci']:
            raise click.BadParameter('Unsupported fabric type')

        if fabric_hint['type'] == 'aci':
            fabric_hint['controller'] = item.split(':')[1]

        if aci_settings_handler.get_apic_controller(fabric_hint['controller']) is None:
            raise click.BadParameter('Undefined apic: %s' % (fabric_hint['controller']))

        fabrics.append(
            fabric_hint
        )

    return fabrics


def validate_timestamp_filter(ctx, param, value):
    if len(value) == 0:
        return None

    if value in ['any', 'all', '*']:
        return '10y'

    if value.endswith('m'):
        try:
            reference = int(value[:-1])
        except BaseException:
            click.BadParameter('Unsupported time filter. Use <n>[m|h|d|y] syntax.')
        return value

    if value.endswith('h'):
        try:
            reference = int(value[:-1])
        except BaseException:
            click.BadParameter('Unsupported time filter. Use <n>[m|h|d|y] syntax.')
        return value

    if value.endswith('d'):
        try:
            reference = int(value[:-1])
        except BaseException:
            click.BadParameter('Unsupported time filter. Use <n>[m|h|d|y] syntax.')
        return value

    if value.endswith('y'):
        try:
            reference = int(value[:-1])
        except BaseException:
            click.BadParameter('Unsupported time filter. Use <n>[m|h|d|y] syntax.')
        return value

    click.BadParameter('Unsupported time filter. Use <n>[m|h|d|y] syntax.')
    return None


def validate_view(ctx, user_input, all_views, default, resolve):
    views = []

    if len(user_input) == 0:
        view = [default]
        return view

    user_views = []
    for item in user_input:
        user_views = user_views + item.split(',')

    defined_views = all_views.split('|')
    resolve_views = {}
    for item in resolve:
        (resolve_name, resolve_view) = item.split(':')
        resolve_views[resolve_name] = resolve_view

    for user_view in user_views:
        if user_view not in defined_views:
            ctx.my_output.error('Supported views: %s' % ','.join(defined_views))
            return None

        if user_view == 'all':
            for defined_view in defined_views:
                if defined_view not in ['all', 'verbose'] and defined_view not in views and defined_view not in resolve_views:
                    views.append(
                        defined_view
                    )
            continue

        if user_view in resolve_views:
            for resolve_view in resolve_views[user_view].split(','):
                if resolve_view not in views:
                    views.append(
                        resolve_view
                    )

            continue

        if user_view not in views:
            views.append(
                user_view
            )

    return views


def validate_kubernetes_name(ctx, value, cluster_type=None, silent=False):
    k8s_settings_handler = k8s_settings.K8sSettings(log_id=None)
    if value is None or len(value) == 0:
        default_cluster_name = k8s_settings_handler.get_default_cluster()
        if default_cluster_name is not None:
            if not silent:
                ctx.my_output.default(
                    'Cluster: %s (type: %s)' % (
                        default_cluster_name,
                        k8s_settings_handler.get_k8s_cluster(default_cluster_name)['type']
                    )
                )
            kubeconfig = k8s_settings_handler.get_k8s_cluster(default_cluster_name)['kubeconfig']

            cluster = k8s_settings_handler.get_k8s_cluster(default_cluster_name)
            if cluster_type is not None:
                if cluster['type'] != cluster_type:
                    ctx.my_output.error(
                        'Required cluster type: %s' % (cluster_type)
                    )
                    return None

            return k8s.K8s(kubeconfig_filename=kubeconfig, cluster_type=cluster['type'], log_id=ctx.run_id)

    if len(value) > 0:
        cluster = k8s_settings_handler.get_k8s_cluster(value, strict_match=False)
        if cluster is not None:
            if cluster_type is not None:
                if cluster['type'] != cluster_type:
                    ctx.my_output.error(
                        'Required cluster type: %s' % (cluster_type)
                    )
                    return None

            if not silent:
                ctx.my_output.default(
                    'Cluster: %s (type: %s)' % (cluster['name'], cluster['type'])
                )
            success = k8s_settings_handler.set_default_cluster(cluster['name'])
            if not success:
                ctx.my_output.default(
                    '[Warning] Default k8s cluster name set failed'
                )

            return k8s.K8s(kubeconfig_filename=cluster['kubeconfig'], cluster_type=cluster['type'], log_id=ctx.run_id)

    clusters = k8s_settings_handler.get_k8s_clusters()
    if len(clusters) == 0:
        ctx.my_output.error('No cluster defined')
    else:
        ctx.my_output.error('Define cluster name')
        for cluster in clusters:
            ctx.my_output.default('- %s (type: %s)' % (cluster['name'], cluster['type']))

    return None


def validate_kubevirt_name(ctx, value):
    k8s_settings_handler = k8s_settings.K8sSettings(log_id=None)
    if len(value) == 0:
        default_cluster_name = k8s_settings_handler.get_default_cluster()
        if default_cluster_name is not None:
            ctx.my_output.default(
                'Cluster: %s' % (default_cluster_name)
            )
            kubeconfig = k8s_settings_handler.get_k8s_cluster(default_cluster_name)['kubeconfig']
            return kubevirt.Kubevirt(kubeconfig_filename=kubeconfig)

    if len(value) > 0:
        cluster = k8s_settings_handler.get_k8s_cluster(value)
        if cluster is not None:
            ctx.my_output.default(
                'Cluster: %s' % (cluster['name'])
            )
            k8s_settings_handler.set_default_cluster(cluster['name'])
            return kubevirt.Kubevirt(kubeconfig_filename=cluster['kubeconfig'])

    cluster_names = k8s_settings_handler.get_k8s_cluster_names()
    if len(cluster_names) == 0:
        ctx.my_output.error('No cluster defined')
    else:
        ctx.my_output.error('Define cluster name')
        for cluster_name in cluster_names:
            ctx.my_output.default('- %s' % (cluster_name))

    return None


def validate_linux_name(ctx, server_name, no_cache=False):
    linux_settings_handler = linux_settings.LinuxSettings(log_id=None)
    if server_name is None:
        default_server_name = linux_settings_handler.get_default_server()
        if default_server_name is not None:
            ctx.my_output.default(
                'Server: %s' % (
                    default_server_name
                )
            )
            server = linux_settings_handler.get_linux_server(default_server_name)
            if server is None:
                ctx.my_output.error('Default server not found')
                return None

            return linux.Linux(
                server['address'],
                server['username'],
                password=server['password'],
                key_filename=server['key'],
                server_name=server['name'],
                no_cache=no_cache
            )

    if server_name is not None and len(server_name) > 0:
        server = linux_settings_handler.get_linux_server(server_name, strict_match=False)
        if server is not None:
            ctx.my_output.default(
                'Server: %s' % (server['name'])
            )
            success = linux_settings_handler.set_default_server(server['name'])
            if not success:
                ctx.my_output.default(
                    '[Warning] Default server name set failed'
                )

            return linux.Linux(
                server['address'],
                server['username'],
                password=server['password'],
                key_filename=server['key'],
                server_name=server['name'],
                no_cache=no_cache
            )

    servers = linux_settings_handler.get_linux_servers()
    if len(servers) == 0:
        ctx.my_output.error('No linux server defined')
        return None

    ctx.my_output.error('Define linux server')
    for server in servers:
        ctx.my_output.default('- %s' % (server['name']))

    return None


def validate_linux_names(ctx, server_names, no_cache=False):
    linux_settings_handler = linux_settings.LinuxSettings(log_id=None)
    if len(server_names) == 0:
        default_server_name = linux_settings_handler.get_default_server()
        if default_server_name is not None:
            ctx.my_output.default(
                'Server: %s' % (
                    default_server_name
                )
            )
            default_server = linux_settings_handler.get_linux_server(default_server_name)
            if default_server is None:
                ctx.my_output.error('Default server not found')
                return None

            server_handler = linux.Linux(
                default_server['address'],
                default_server['username'],
                password=default_server['password'],
                key_filename=default_server['key'],
                server_name=default_server['name'],
                no_cache=no_cache,
                log_id=ctx.run_id
            )
            return [server_handler]

    all_servers = linux_settings_handler.get_linux_servers()
    if len(all_servers) == 0:
        ctx.my_output.error('No linux server defined')
        return None

    selected_server_names = []
    for server_name in server_names:
        for server in all_servers:
            if server_name in server['name']:
                if server['name'] not in selected_server_names:
                    selected_server_names.append(server['name'])

    if len(selected_server_names) == 0:
        ctx.my_output.error('Define linux server')
        for server in all_servers:
            ctx.my_output.default('- %s' % (server['name']))
        return None

    server_handlers = []
    server_handler_names = []
    for server_name in selected_server_names:
        server = linux_settings_handler.get_linux_server(server_name, strict_match=False)
        if server is not None:
            server_handler_names.append(server_name)
            server_handler = linux.Linux(
                server['address'],
                server['username'],
                password=server['password'],
                key_filename=server['key'],
                server_name=server['name'],
                no_cache=no_cache,
                log_id=ctx.run_id
            )
            server_handlers.append(server_handler)

    if len(selected_server_names) == 0:
        ctx.my_output.error('Define linux server')
        for server in all_servers:
            ctx.my_output.default('- %s' % (server['name']))
        return None

    if len(selected_server_names) == 1:
        success = linux_settings_handler.set_default_server(server['name'])
        if not success:
            ctx.my_output.default(
                '[Warning] Default server name set failed'
            )

    ctx.my_output.default(
        'Server: %s' % (
            ','.join(selected_server_names)
        )
    )
    return server_handlers


def validate_helm_chart(ctx, values_filename):
    chart_info = {}
    chart_info['directory'] = os.path.dirname(values_filename)
    chart_info['values'] = values_filename

    if not os.path.isfile(chart_info['values']):
        ctx.my_output.error('Values file not found: %s' % (chart_info['values']))
        return None

    if file_helper.get_file_yaml(chart_info['values']) is None:
        ctx.my_output.error('File should be YAML: %s' % (chart_info['values']))
        return None

    chart_filename = os.path.join(
        chart_info['directory'],
        'Chart.yaml'
    )

    if not os.path.isfile(chart_filename):
        ctx.my_output.error('Chart file not found: %s' % (chart_filename))
        return None

    chart_definition = file_helper.get_file_yaml(chart_filename)
    if chart_definition is None:
        ctx.my_output.error('File should be YAML: %s' % (chart_filename))
        return None

    chart_info['chart'] = chart_definition['name']
    chart_info['version'] = chart_definition['version']
    chart_info['appVersion'] = chart_definition['appVersion']

    templates_directory = os.path.join(chart_info['directory'], 'templates')
    if not os.path.isdir(templates_directory):
        ctx.my_output.error('Templates directory not found: %s' % (templates_directory))
        return None

    charts_directory = os.path.join(chart_info['directory'], 'charts')
    if not os.path.isdir(charts_directory):
        ctx.my_output.error('Charts directory not found: %s' % (charts_directory))
        return None

    return chart_info


def select_osp_name(ctx):
    osp_settings_handler = osp_settings.OspSettings(log_id=None)
    names = osp_settings_handler.get_openstack_cluster_names()
    if len(names) == 0:
        ctx.my_output.error('No openstack cluster defined')
        return None

    ctx.my_output.default('Select OpenStack Cluster', underline=True)
    for name in names:
        ctx.my_output.default('- %s' % (name))

    selected = input('Value: ')
    if len(selected) == 0:
        return None

    if selected not in names:
        return None

    return selected


def validate_osp_name(ctx, value, silent=False):
    osp_settings_handler = osp_settings.OspSettings(log_id=None)
    if value is None or len(value) == 0:
        default_cluster_name = osp_settings_handler.get_default_cluster()
        if default_cluster_name is not None:
            if not silent:
                ctx.my_output.default(
                    'Cluster: %s (type: %s)' % (
                        default_cluster_name,
                        osp_settings_handler.get_openstack_cluster(default_cluster_name)['type']
                    )
                )
            openrc = osp_settings_handler.get_openstack_cluster(default_cluster_name)['openrc']
            cert = osp_settings_handler.get_openstack_cluster(default_cluster_name)['cert']
            return osp.Osp(openrc_filename=openrc, cert_filename=cert, log_id=ctx.run_id)

    if len(value) > 0:
        cluster = osp_settings_handler.get_openstack_cluster(value, strict_match=False)
        if cluster is not None:
            if not silent:
                ctx.my_output.default(
                    'Cluster: %s' % (cluster['name'])
                )
            success = osp_settings_handler.set_default_cluster(cluster['name'])
            if not success:
                ctx.my_output.default(
                    '[Warning] Default osp cluster name set failed'
                )

            return osp.Osp(openrc_filename=cluster['openrc'], cert_filename=cluster['cert'], log_id=ctx.run_id)

    clusters = osp_settings_handler.get_openstack_clusters()
    if len(clusters) == 0:
        ctx.my_output.error('No cluster defined')
    else:
        ctx.my_output.error('Define cluster name')
        for cluster in clusters:
            ctx.my_output.default('- %s' % (cluster['name']))

    return None

def validate_bot(ctx, param, value):
    if len(value) == 0:
        return None

    settings_handler = settings_helper.Settings()
    bot_main_directory = os.path.join(
        settings_handler.get_settings_dir(),
        'bot'
    )
    bot_directory = os.path.join(
        bot_main_directory,
        value
    )

    if not os.path.isfile(bot_directory):
        raise click.BadParameter('bot not found: %s' % (value))

    return file_helper.get_file_json(bot_directory)


def validate_bot_group(users, group_name):
    group_users = []
    for user in users:
        if 'group' in user and 'title' in user:
            for user_group in user['group']:
                if user_group == group_name:
                    group_users.append(user)
    return group_users
