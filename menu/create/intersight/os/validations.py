import os

from progress.bar import IncrementalBar

from lib.intersight.os_configuration_file import main as os_configuration_file
from lib.intersight.hcl_operating_system_vendor import main as hcl_operating_system_vendor
from lib.intersight.hcl_operating_system import main as hcl_operating_system

from lib.intersight import compute
from lib import ip_helper
from lib import file_helper

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
        attributes['organization']
    )
    return attributes[0]


def validate_static_attributes(ctx, iaccount, filename, attributes):
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
    servers_mo = common.get_servers_mo(
        ctx,
        iaccount,
        ip_filter=[ip_filter],
        name_filter=name_filter,
        serial_filter=[serial_filter],
        show_progress=True,
        include_rack=True,
        include_blade=False
    )
    common.print_servers_mo_info(
        ctx,
        iaccount,
        servers_mo,
        show_progress=True
    )

    if len(servers_mo) > 1:
        ctx.my_output.error('Select single server...')
        return None

    return servers_mo[0]


def get_server(ctx, iaccount, name_filter, ip_filter, serial_filter):
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

    ctx.my_output.default('Validate server selection...')
    server_mo = validate_server(ctx, iaccount, name_filter, ip_filter, serial_filter)
    if server_mo is None:
        return None, None

    ctx.my_output.default('Getting server details...')
    compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
    settings = {}
    settings['storage'] = True
    settings['workflow'] = 3600

    servers_info = compute_handler.get_info(
        [server_mo],
        settings,
        None,
        1
    )
    if servers_info is None or len(servers_info) == 0:
        return None, None

    if servers_info[0]['VirtualDiskCount'] == 0:
        ctx.my_output.error('No virtual disk detected on the server')
        return None, None

    return servers_info[0], server_mo


def get_scu_info(ctx, iaccount, scu_name):
    if len(scu_name) > 0:
        ctx.my_output.default('Validate SCU...')
        scu_info = validations.validate_scu(ctx, iaccount, scu_name)
        if scu_info is not None:
            return scu_info

    return user_inputs.get_scu_info(ctx, iaccount)


def get_os_image_info(ctx, iaccount, image_name):
    if len(image_name) > 0:
        ctx.my_output.default('Validate OS Image...')
        os_info = validations.validate_os_image(ctx, iaccount, image_name)
        if os_info is None:
            return None
    else:
        os_info = user_inputs.get_os_image_info(ctx, iaccount)
        if os_info is None:
            return None

    hcl_os_vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
    image_vendor_mo = hcl_os_vendor_handler.get_by_name(
        os_info['Vendor']
    )
    if image_vendor_mo is None:
        ctx.my_output.error('Vendor not found for image')
        return None

    hcl_os_version_handler = hcl_operating_system.HclOperatingSystem(iaccount, log_id=ctx.run_id)
    image_version_id = hcl_os_version_handler.get_vendor_version_id(
        image_vendor_mo['Moid'],
        os_info['Version']
    )
    if image_version_id is None:
        ctx.my_output.error('Version %s not found for image vendor %s' % (
            os_info['Version'],
            image_vendor_mo['Name']
        ))
        return None

    os_info['VendorId'] = image_vendor_mo['Moid']
    os_info['VersionId'] = image_version_id

    os_configuration_file_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
    os_configuration_files = os_configuration_file_handler.get_file_for_os(
        image_version_id
    )
    if len(os_configuration_files) == 0:
        ctx.my_output.error(
            'No autoconfiguration file found for image: %s [%s]' % (
                os_info['Name'],
                os_info['VersionId']
            )
        )
        return None

    if len(os_configuration_files) > 1:
        ctx.my_output.error('Multiple autoconfiguration files found for image: %s' % (os_info['Name']))
        for item in os_configuration_files:
            ctx.my_output.default('- Moid [%s] Name [%s]' % (item['Moid'], item['Name']))
        return None

    os_info['ConfigurationId'] = os_configuration_files[0]['Moid']
    return os_info


def get_os_config_info(ctx, iaccount, config_name):
    if len(config_name) > 0:
        ctx.my_output.default('Validate OS configuration...')
        os_info = validations.validate_os_config(ctx, iaccount, config_name)
        if os_info is not None:
            return os_info

    return user_inputs.get_os_config_info(ctx, iaccount)


def get_organization_id(ctx, iaccount, organization_name):
    if len(organization_name) > 0:
        ctx.my_output.default('Validate organization...')
        organization_id = validations.validate_organization(ctx, iaccount, organization_name)
        if organization_id is not None:
            return organization_id

    return user_inputs.get_organization_id(ctx, iaccount)


def get_values_yaml(ctx, filename):
    if len(filename) > 0:
        content = file_helper.get_file_yaml(
            filename
        )
        if content is not None:
            return content

        ctx.my_output.error('Values yaml read failed: %s' % (filename))

    return user_inputs.get_yaml_file(ctx, 'Values yaml filename')


def get_embedded_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, organization_name):
    server_info, server_mo = get_server(
        ctx,
        iaccount,
        name_filter,
        ip_filter,
        serial_filter
    )
    if server_info is None:
        return None

    scu_info = get_scu_info(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = get_os_image_info(ctx, iaccount, image_name)
    if image_info is None:
        return None

    organization_id = get_organization_id(ctx, iaccount, organization_name)
    if organization_id is None:
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

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server_mo
    attributes['server_info'] = server_info

    return [attributes]


def get_dhcp_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, interface_name, interface_mac, hostname, password, organization_name):
    server_info, server_mo = get_server(
        ctx,
        iaccount,
        name_filter,
        ip_filter,
        serial_filter
    )
    if server_info is None:
        return None

    scu_info = get_scu_info(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = get_os_image_info(ctx, iaccount, image_name)
    if image_info is None:
        return None

    if len(hostname) == 0:
        hostname = user_inputs.get_value(ctx, 'Hostname', empty=True)
        if len(hostname) == 0:
            return None

    if len(password) == 0:
        password = user_inputs.get_value(ctx, 'Password', empty=True)
        if len(password) == 0:
            return None

    if interface_name == '' and interface_mac == '':
        ctx.my_output.default('Define either interface name or interface mac for sending dhcp request')
        interface_name = user_inputs.get_value(ctx, '- interface name', empty=True)
        interface_mac = user_inputs.get_value(ctx, '- interface mac', empty=True)
        if interface_name == '' and interface_mac == '':
            return None

    organization_id = get_organization_id(ctx, iaccount, organization_name)
    if organization_id is None:
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
    attributes['configuration_file_id'] = image_info['ConfigurationId']
    attributes['ip_config'] = 'dhcp'
    attributes['interface_name'] = interface_name
    attributes['interface_mac'] = interface_mac
    attributes['hostname'] = hostname
    attributes['password'] = password

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server_mo
    attributes['server_info'] = server_info

    return [attributes]


def get_static_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, interface_name, interface_mac, address, netmask, gateway, nameserver, hostname, password, organization_name):
    server_info, server_mo = get_server(
        ctx,
        iaccount,
        name_filter,
        ip_filter,
        serial_filter
    )
    if server_info is None:
        return None

    scu_info = get_scu_info(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = get_os_image_info(ctx, iaccount, image_name)
    if image_info is None:
        return None

    if len(hostname) == 0:
        hostname = user_inputs.get_value(ctx, 'Hostname', empty=True)
        if len(hostname) == 0:
            return None

    if len(password) == 0:
        password = user_inputs.get_value(ctx, 'Password', empty=True)
        if len(password) == 0:
            return None

    if interface_name == '' and interface_mac == '':
        ctx.my_output.default('Define either interface name or interface mac for sending dhcp request')
        interface_name = user_inputs.get_value(ctx, '- interface name', empty=True)
        interface_mac = user_inputs.get_value(ctx, '- interface mac', empty=True)
        if interface_name == '' and interface_mac == '':
            return None

    if len(address) == 0:
        address = user_inputs.get_ip_address(ctx, 'Interface IPv4 address', empty=True)
        if len(address) == 0:
            return None

    if len(netmask) == 0:
        netmask = user_inputs.get_ip_address(ctx, 'Interface IPv4 netmask', empty=True)
        if len(netmask) == 0:
            return None

    prefix = ip_helper.netmask_to_prefix(netmask)
    cidr = '%s/%s' % (
        address,
        str(prefix)
    )

    if len(gateway) == 0:
        gateway = user_inputs.get_ip_address(ctx, 'Gateway IP address', empty=True)
        if len(gateway) == 0:
            return None

    if not ip_helper.is_ipv4_in_cidr(gateway, cidr):
        ctx.my_output.error('Gateway must be part of the interface subnet')
        return None

    if len(nameserver) == 0:
        nameserver = user_inputs.get_ip_address(ctx, 'Nameserver IP address', empty=True)
        if len(nameserver) == 0:
            return None

    organization_id = get_organization_id(ctx, iaccount, organization_name)
    if organization_id is None:
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
    attributes['configuration_file_id'] = image_info['ConfigurationId']
    attributes['ip_config'] = 'static'
    attributes['interface_name'] = interface_name
    attributes['interface_mac'] = interface_mac
    attributes['ipv4_address'] = address
    attributes['ipv4_mask'] = netmask
    attributes['ipv4_gateway'] = gateway
    attributes['nameserver'] = nameserver
    attributes['hostname'] = hostname
    attributes['password'] = password

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server_mo
    attributes['server_info'] = server_info

    return [attributes]


def get_custom_attributes(ctx, iaccount, name_filter, ip_filter, serial_filter, scu_name, image_name, config_name, values_filename, organization_name):
    server_info, server_mo = get_server(
        ctx,
        iaccount,
        name_filter,
        ip_filter,
        serial_filter
    )
    if server_info is None:
        return None

    scu_info = get_scu_info(ctx, iaccount, scu_name)
    if scu_info is None:
        return None

    image_info = get_os_image_info(ctx, iaccount, image_name)
    if image_info is None:
        return None

    config_info = get_os_config_info(ctx, iaccount, config_name)
    if config_info is None:
        return None

    organization_id = get_organization_id(ctx, iaccount, organization_name)
    if organization_id is None:
        return None

    attributes = {}
    attributes['type'] = 'custom'
    attributes['server_id'] = server_info['Moid']
    attributes['server_name'] = server_info['Name']
    attributes['scu_id'] = scu_info['Moid']
    attributes['image'] = {}
    attributes['image']['id'] = image_info['Moid']
    attributes['image']['name'] = image_info['Name']
    attributes['image']['vendor_id'] = image_info['VendorId']
    attributes['image']['version_id'] = image_info['VersionId']
    attributes['configuration_file_id'] = config_info['Moid']

    virtual_disk = server_info['VirtualDisks'][0]
    attributes['storage_controller_slot'] = virtual_disk['StorageControllerId']
    attributes['virtual_drive_id'] = virtual_disk['VirtualDriveId']
    attributes['virtual_drive_name'] = virtual_disk['Name']

    attributes['organization_id'] = organization_id
    attributes['server'] = server_mo
    attributes['server_info'] = server_info

    attributes['values'] = get_values_yaml(ctx, values_filename)
    if attributes['values'] is None:
        return None

    return [attributes]
