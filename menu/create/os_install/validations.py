import os

from progress.bar import IncrementalBar

from lib.intersight import compute_info
from lib.intersight import os_configuration_file
from lib import ip_helper

from menu import user_inputs
from menu import common
from menu import validations


def validate_embedded_attributes(ctx, iaccount, filename, attributes):
    '''
        type: embedded
        server:
            ip: 10.58.50.46
        image: dummy
        scu: dummmy
        organization: EMEAR-SPDC-Specialists
    '''
    for attribute in ['server', 'image', 'scu', 'organization']:
        if attribute not in attributes:
            ctx.my_output.error('[%s] Attribute %s required' % (filename, attribute))
            return None

    found = False
    for attribute in ['ip', 'name', 'serial']:
        if attribute in attributes['server']:
            found = True
        else:
            attributes['server'][attribute] = ''

    if not found:
        ctx.my_output.error('[%s] Attribute server.[ip|name|serial] required' % (filename))
        return None

    if len(attributes['server']['ip']) > 0:
        if not ip_helper.is_valid_ipv4_address(attributes['server']['ip']):
            ctx.my_output.error('[%s] Invalid IPv4 address: %s' % (filename, attributes['server']['ip']))
            return None

    attributes = get_embedded_attributes(
        ctx,
        iaccount,
        attributes['server']['name'],
        attributes['server']['ip'],
        attributes['server']['serial'],
        attributes['scu'],
        attributes['image'],
        attributes['organization']
    )

    return attributes[0]


def validate_dhcp_attributes(ctx, iaccount, filename, attributes):
    '''
        type: dhcp
        server:
            ip: 10.58.50.46
        image: dummy
        scu: dummmy
        interface:
            name: eno5
        hostname: kvm
        password: cisco
        organization: EMEAR-SPDC-Specialists
    '''
    for attribute in ['server', 'image', 'scu', 'interface', 'organization', 'hostname', 'password']:
        if attribute not in attributes:
            ctx.my_output.error('[%s] Attribute %s required' % (filename, attribute))
            return None

    found = False
    for attribute in ['ip', 'name', 'serial']:
        if attribute in attributes['server']:
            found = True
        else:
            attributes['server'][attribute] = ''

    if not found:
        ctx.my_output.error('[%s] Attribute server.[ip|name|serial] required' % (filename))
        return None

    if len(attributes['server']['ip']) > 0:
        if not ip_helper.is_valid_ipv4_address(attributes['server']['ip']):
            ctx.my_output.error('[%s] Invalid IPv4 address: %s' % (filename, attributes['server']['ip']))
            return None

    found = False
    for attribute in ['name', 'mac']:
        if attribute in attributes['interface']:
            found = True
        else:
            attributes['interface'][attribute] = ''

    if not found:
        ctx.my_output.error('[%s] Attribute interface.[name|mac] required' % (filename))
        return None

    attributes = get_dhcp_attributes(
        ctx,
        iaccount,
        attributes['server']['name'],
        attributes['server']['ip'],
        attributes['server']['serial'],
        attributes['scu'],
        attributes['image'],
        attributes['interface']['name'],
        attributes['interface']['mac'],
        attributes['hostname'],
        attributes['password'],
        attributes['organization'],
        interactive=False
    )
    return attributes[0]


def validate_static_attributes(ctx, iaccount, filename, attributes):
    '''
    type: static
    server:
        ip: 10.58.50.46
    image: Ubuntu 22.04LTS
    scu: SCU 6.2.2a
    interface:
        name: eno5
        ip: 10.58.25.163
        netmask: 255.255.255.240
        gateway: 10.58.25.174
    hostname: iserver-test
    password: cisco
    nameserver: 144.254.71.184
    organization: EMEAR-SPDC-Specialists
    '''
    for attribute in ['server', 'image', 'scu', 'interface', 'organization', 'hostname', 'password', 'nameserver']:
        if attribute not in attributes:
            ctx.my_output.error('[%s] Attribute %s required' % (filename, attribute))
            return None

    found = False
    for attribute in ['ip', 'name', 'serial']:
        if attribute in attributes['server']:
            found = True
        else:
            attributes['server'][attribute] = ''

    if not found:
        ctx.my_output.error('[%s] Attribute server.[ip|name|serial] required' % (filename))
        return None

    if len(attributes['server']['ip']) > 0:
        if not ip_helper.is_valid_ipv4_address(attributes['server']['ip']):
            ctx.my_output.error('[%s] Invalid IPv4 address: %s' % (filename, attributes['server']['ip']))
            return None

    found = False
    for attribute in ['name', 'mac']:
        if attribute in attributes['interface']:
            found = True
        else:
            attributes['interface'][attribute] = ''

    if not found:
        ctx.my_output.error('[%s] Attribute interface.[name|mac] required' % (filename))
        return None

    for attribute in ['ip', 'netmask', 'gateway']:
        if attribute not in attributes['interface']:
            ctx.my_output.error('[%s] Attribute interface.%s required' % (filename, attribute))
            return None

    if len(attributes['interface']['ip']) > 0:
        if not ip_helper.is_valid_ipv4_address(attributes['interface']['ip']):
            ctx.my_output.error('[%s] Invalid IPv4 address: %s' % (filename, attributes['interface']['ip']))
            return None

    if len(attributes['interface']['gateway']) > 0:
        if not ip_helper.is_valid_ipv4_address(attributes['interface']['gateway']):
            ctx.my_output.error('[%s] Invalid IPv4 address: %s' % (filename, attributes['interface']['gateway']))
            return None

    if len(attributes['interface']['netmask']) == 0:
        ctx.my_output.error('[%s] netmask value required' % (filename))
        return None

    prefix = ip_helper.netmask_to_prefix(attributes['interface']['netmask'])
    if prefix is None:
        ctx.my_output.error('[%s] invalud netmask value: %s' % (filename, attributes['interface']['netmask']))
        return None

    if len(attributes['nameserver']) > 0:
        if not ip_helper.is_valid_ipv4_address(attributes['nameserver']):
            ctx.my_output.error('[%s] Invalid IPv4 address: %s' % (filename, attributes['nameserver']))
            return None

    attributes = get_static_attributes(
        ctx,
        iaccount,
        attributes['server']['name'],
        attributes['server']['ip'],
        attributes['server']['serial'],
        attributes['scu'],
        attributes['image'],
        attributes['interface']['name'],
        attributes['interface']['mac'],
        attributes['interface']['ip'],
        prefix,
        attributes['interface']['gateway'],
        attributes['nameserver'],
        attributes['hostname'],
        attributes['password'],
        attributes['organization']
    )

    return attributes[0]


def validate_attributes(ctx, iaccount, filename, attributes):
    if attributes is None:
        return None

    if 'type' not in attributes:
        ctx.my_output.error('type attribute required')
        return None

    if attributes['type'] not in ['embedded', 'dhcp', 'static']:
        ctx.my_output.error('type attribute allowed values: embedded, dhcp, static')
        return None

    if attributes['type'] == 'embedded':
        return validate_embedded_attributes(ctx, iaccount, filename, attributes)

    if attributes['type'] == 'dhcp':
        return validate_dhcp_attributes(ctx, iaccount, filename, attributes)

    return validate_static_attributes(ctx, iaccount, filename, attributes)


def get_batch_attributes(ctx, iaccount, location):
    filenames = []
    if os.path.isdir(location):
        for file_in_dir in os.listdir(location):
            filenames.append(
                os.path.join(location, file_in_dir)
            )

    if os.path.isfile(location):
        filenames.append(location)

    if len(filenames) == 0:
        ctx.my_output.error('No input files found')
        return None

    attributes = []
    bar_handler = IncrementalBar('Input file', max=len(filenames))
    bar_handler.goto(0)
    for filename in filenames:
        file_attributes = validate_attributes(
            ctx,
            iaccount,
            filename,
            validations.validate_yaml_file(ctx, filename)
        )
        if file_attributes is None:
            bar_handler.finish()
            ctx.my_output.error('\nInvalid file content: %s' % (filename))
            return None

        attributes.append(file_attributes)
        bar_handler.next()

    bar_handler.finish()

    return attributes


def validate_server(ctx, iaccount, name_filter, ip_filter, serial_filter, workflow=86400):
    server = common.get_selected_servers(
        ctx,
        iaccount,
        None,
        serial_filter,
        name_filter,
        ip_filter,

        workflow=workflow,
        include_object=True,
        show_servers=True,
        confirm=True
    )
    if server is None:
        return None

    if server['Workflow']['Running'] is not None:
        ctx.my_output.error('Active workflow on server %s. Cannot continue' % (server['Name']))
        return None

    return server


def get_embedded_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, organization_name, interactive=False):
    if name_filter == '' and ip_filter == '' and serial_filter == '':
        server_selection_mode = user_inputs.get_selection(
            ctx,
            'Select server selection type',
            ['name', 'serial', 'ip']
        )

        if server_selection_mode == 'name':
            name_filter = user_inputs.get_value(ctx, 'Server name')

        if server_selection_mode == 'serial':
            serial_filter = user_inputs.get_value(ctx, 'Server serial number')

        if server_selection_mode == 'ip':
            ip_filter = user_inputs.get_value(ctx, 'Server management IP address')

    if not interactive:
        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is None:
            return None

    server = validate_server(ctx, iaccount, name_filter, ip_filter, serial_filter)
    if server is None:
        return None

    if interactive:
        scu_name = user_inputs.get_scu_name(ctx, iaccount)
        image_name = user_inputs.get_os_image_name(ctx, iaccount)

        organization_name = user_inputs.get_organization_name(ctx, iaccount)
        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is None:
            return None

    settings = common.get_server_selection_settings(
        iaccount,
        workflow=None,
        action=True,
        registration=False,
        enabled=['storage']
    )

    compute_handler = compute_info.ComputeInfo(iaccount, settings=settings, log_id=ctx.run_id)
    server_info = compute_handler.get_server_info(server['IntersightObject'])

    scu_info = validations.validate_scu(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = validations.validate_os_image(ctx, iaccount, image_name)
    if image_info is None:
        return None

    attributes = {}
    attributes['type'] = 'embedded'
    attributes['server_id'] = server_info['Moid']
    attributes['server_name'] = server_info['Name']
    attributes['scu_id'] = scu_info['Moid']
    attributes['image'] = {}
    attributes['image']['id'] = image_info['Moid']
    attributes['image']['name'] = image_info['Name']
    attributes['image']['vendor_id'] = image_info['VendorId']
    attributes['image']['version_id'] = image_info['VersionId']

    if server_info['VirtualDiskCount'] == 0:
        ctx.my_output.error('No virtual disk detected on the server')
        return None

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server

    return [attributes]


def get_dhcp_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, interface_name, interface_mac, hostname, password, organization_name, interactive=False):
    if name_filter == '' and ip_filter == '' and serial_filter == '':
        server_selection_mode = user_inputs.get_selection(
            ctx,
            'Select server selection type',
            ['name', 'serial', 'ip']
        )

        if server_selection_mode == 'name':
            name_filter = user_inputs.get_value(ctx, 'Server name')

        if server_selection_mode == 'serial':
            serial_filter = user_inputs.get_value(ctx, 'Server serial number')

        if server_selection_mode == 'ip':
            ip_filter = user_inputs.get_value(ctx, 'Server management IP address')

    if not interactive:
        if interface_name == '' and interface_mac == '':
            ctx.my_output.error('Define either interface name or interface mac for sending dhcp request')
            return None

        if hostname == '':
            ctx.my_output.error('Define hostname')
            return None

        if password == '':
            ctx.my_output.error('Define password')
            return None

        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is None:
            return None

    server = validate_server(ctx, iaccount, name_filter, ip_filter, serial_filter)
    if server is None:
        return None

    if interactive:
        scu_name = user_inputs.get_scu_name(ctx, iaccount)
        image_name = user_inputs.get_os_image_name(ctx, iaccount)
        ctx.my_output.default('Define interface by name or mac address')
        interface_name = user_inputs.get_value(ctx, '- interface name', empty=True)
        interface_mac = user_inputs.get_value(ctx, '- interface mac', empty=True)
        hostname = user_inputs.get_value(ctx, 'Hostname')
        password = user_inputs.get_value(ctx, 'Password')
        organization_name = user_inputs.get_organization_name(ctx, iaccount)

        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is None:
            return None

    settings = common.get_server_selection_settings(
        iaccount,
        workflow=86400,
        action=True,
        registration=False,
        enabled=['storage']
    )

    compute_handler = compute_info.ComputeInfo(iaccount, settings=settings, log_id=ctx.run_id)
    server_info = compute_handler.get_server_info(server['IntersightObject'])

    scu_info = validations.validate_scu(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = validations.validate_os_image(ctx, iaccount, image_name)
    if image_info is None:
        return None

    attributes = {}
    attributes['type'] = 'template'
    attributes['server_id'] = server_info['Moid']
    attributes['server_name'] = server_info['Name']
    attributes['scu_id'] = scu_info['Moid']
    attributes['image'] = {}
    attributes['image']['id'] = image_info['Moid']
    attributes['image']['name'] = image_info['Name']
    attributes['image']['vendor_id'] = image_info['VendorId']
    attributes['image']['version_id'] = image_info['VersionId']
    attributes['ip_config'] = 'dhcp'
    attributes['interface_name'] = interface_name
    attributes['interface_mac'] = interface_mac
    attributes['hostname'] = hostname
    attributes['password'] = password

    if server_info['VirtualDiskCount'] == 0:
        ctx.my_output.error('No virtual disk detected on the server')
        return None

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server_info

    os_configuration_file_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
    os_configuration_files = os_configuration_file_handler.get_file_for_os(
        attributes['image']['version_id']
    )
    if len(os_configuration_files) == 0:
        ctx.my_output.error('No autoconfiguration file found for image: %s' % (attributes['image']['name']))
        return None

    if len(os_configuration_files) > 1:
        ctx.my_output.error('Multiple autoconfiguration files found for image: %s' % (attributes['image']['name']))
        for item in os_configuration_files:
            ctx.my_output.default('- Moid [%s] Name [%s]' % (item['Moid'], item['Name']))
        return None

    attributes['configuration_file_id'] = os_configuration_files[0]['Moid']

    return [attributes]


def get_static_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, interface_name, interface_mac, address, prefix, gateway, nameserver, hostname, password, organization_name, interactive=False):
    if name_filter == '' and ip_filter == '' and serial_filter == '':
        server_selection_mode = user_inputs.get_selection(
            ctx,
            'Select server selection type',
            ['name', 'serial', 'ip']
        )

        if server_selection_mode == 'name':
            name_filter = user_inputs.get_value(ctx, 'Server name')

        if server_selection_mode == 'serial':
            serial_filter = user_inputs.get_value(ctx, 'Server serial number')

        if server_selection_mode == 'ip':
            ip_filter = user_inputs.get_value(ctx, 'Server management IP address')

    if not interactive:
        if interface_name == '' and interface_mac == '':
            ctx.my_output.error('Define either interface name or interface mac for sending dhcp request')
            return None

        if hostname == '':
            ctx.my_output.error('Define hostname')
            return None

        if password == '':
            ctx.my_output.error('Define password')
            return None

        if address == '':
            ctx.my_output.error('Define IP address')
            return None

        netmask = ip_helper.prefix_to_netmask(prefix)
        cidr = '%s/%s' % (
            address,
            str(prefix)
        )

        if gateway == '':
            ctx.my_output.error('Define gateway address')
            return None

        if not ip_helper.is_ipv4_in_cidr(gateway, cidr):
            ctx.my_output.error('Gateway must be part of the subnet')
            return None

        if nameserver == '':
            ctx.my_output.error('Define nameserver address')
            return None

        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is None:
            return None

    server = validate_server(ctx, iaccount, name_filter, ip_filter, serial_filter)
    if server is None:
        return None

    if interactive:
        scu_name = user_inputs.get_scu_name(ctx, iaccount)
        image_name = user_inputs.get_os_image_name(ctx, iaccount)
        ctx.my_output.default('Define interface by name or mac address')
        interface_name = user_inputs.get_value(ctx, '- interface name', empty=True)
        interface_mac = user_inputs.get_value(ctx, '- interface mac', empty=True)
        address = user_inputs.get_ip_address(ctx, 'Interface IP address')
        prefix = user_inputs.get_prefix_length(ctx, 'Prefix length')
        gateway = user_inputs.get_ip_address(ctx, 'Gateway IP address')

        netmask = ip_helper.prefix_to_netmask(prefix)
        cidr = '%s/%s' % (
            address,
            str(prefix)
        )

        if not ip_helper.is_ipv4_in_cidr(gateway, cidr):
            ctx.my_output.error('Gateway must be part of the subnet')
            return None

        nameserver = user_inputs.get_value(ctx, 'Nameserver IP address')
        hostname = user_inputs.get_value(ctx, 'Hostname')
        password = user_inputs.get_value(ctx, 'Password')

        organization_name = user_inputs.get_organization_name(ctx, iaccount)
        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is None:
            return None

    settings = common.get_server_selection_settings(
        iaccount,
        workflow=None,
        action=True,
        registration=False
    )
    settings['storage'] = True

    compute_handler = compute_info.ComputeInfo(iaccount, settings=settings, log_id=ctx.run_id)
    server_info = compute_handler.get_server_info(server['IntersightObject'])

    scu_info = validations.validate_scu(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = validations.validate_os_image(ctx, iaccount, image_name)
    if image_info is None:
        return None

    attributes = {}
    attributes['type'] = 'template'
    attributes['server_id'] = server_info['Moid']
    attributes['server_name'] = server_info['Name']
    attributes['scu_id'] = scu_info['Moid']
    attributes['image'] = {}
    attributes['image']['id'] = image_info['Moid']
    attributes['image']['name'] = image_info['Name']
    attributes['image']['vendor_id'] = image_info['VendorId']
    attributes['image']['version_id'] = image_info['VersionId']
    attributes['ip_config'] = 'static'
    attributes['interface_name'] = interface_name
    attributes['interface_mac'] = interface_mac
    attributes['ipv4_address'] = address
    attributes['ipv4_mask'] = netmask
    attributes['ipv4_gateway'] = gateway
    attributes['nameserver'] = nameserver
    attributes['hostname'] = hostname
    attributes['password'] = password

    if server_info['VirtualDiskCount'] == 0:
        ctx.my_output.error('No virtual disk detected on the server')
        return None

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server

    os_configuration_file_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
    os_configuration_files = os_configuration_file_handler.get_file_for_os(
        attributes['image']['version_id']
    )
    if len(os_configuration_files) == 0:
        ctx.my_output.error('No autoconfiguration file found for image: %s' % (attributes['image']['name']))
        return None

    if len(os_configuration_files) > 1:
        ctx.my_output.error('Multiple autoconfiguration files found for image: %s' % (attributes['image']['name']))
        for item in os_configuration_files:
            ctx.my_output.default('- Moid [%s] Name [%s]' % (item['Moid'], item['Name']))
        return None

    attributes['configuration_file_id'] = os_configuration_files[0]['Moid']

    return [attributes]
