from lib import ip_helper
from lib import file_helper

from lib.intersight.scu import main as scu
from lib.intersight.os_image import main as os_image
from lib.intersight.os_configuration_file import main as os_configuration_file
from lib.intersight.organization import main as organization
from lib.intersight.hcl_operating_system_vendor import main as hcl_operating_system_vendor
from lib.intersight.hcl_operating_system import main as hcl_operating_system


def string_fixup(value):
    value = value.strip()
    return value


def get_scu_info(ctx, iaccount):
    scu_handler = scu.SoftwareConfigurationUtility(iaccount, log_id=ctx.run_id)
    items = scu_handler.get_all()
    if items is None or len(items) == 0:
        ctx.my_output.error('No SCU found')
        return None

    scu_handler.print(items)
    while True:
        value = input('SCU name: ')
        if len(value) == 0:
            return None

        for item in items:
            if item['Name'] == string_fixup(value):
                return item


def get_os_image_vendor(ctx, iaccount, empty=False):
    handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
    vendors = handler.get_all()

    ctx.my_output.default('OS Vendors:')
    for vendor in vendors:
        ctx.my_output.default('- %s' % (vendor['Name']))

    value = ''
    while len(value) == 0:
        value = input('OS Vendor name: ')
        if empty:
            break

    return string_fixup(value)


def get_os_image_version(ctx, iaccount, vendor_name, empty=False):
    vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
    vendor_attributes = vendor_handler.get_by_name(vendor_name)
    if vendor_attributes is None:
        ctx.my_output.error('Vendor not found: %s' % (vendor_name))
        return None

    version_handler = hcl_operating_system.HclOperatingSystem(iaccount, log_id=ctx.run_id)
    versions = version_handler.get_vendor_versions(vendor_attributes['Moid'])

    ctx.my_output.default('OS Versions:')
    for version in versions:
        ctx.my_output.default('- %s' % (version['Version']))

    value = ''
    while len(value) == 0:
        value = input('OS Version name: ')
        if empty:
            break

    return string_fixup(value)


def get_os_image_name(ctx, iaccount, new=False):
    image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
    items = image_handler.get_all()
    image_handler.print(items)

    value = ''
    while len(value) == 0:
        if new:
            value = input('New OS Image name: ')
        else:
            value = input('Existing OS Image name: ')

    return string_fixup(value)


def get_os_image_info(ctx, iaccount):
    image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
    items = image_handler.get_all()
    if items is None or len(items) == 0:
        ctx.my_output.error('No OS image found')
        return None

    image_handler.print(items)

    while True:
        value = input('OS image name: ')
        if len(value) == 0:
            return None

        for item in items:
            if item['Name'] == string_fixup(value):
                return item


def get_os_config_file(ctx, iaccount, new=False):
    vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
    vendors = vendor_handler.get_all()

    config_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
    config_files = config_handler.get_infos(
        vendors
    )

    names = []
    for config_file in config_files:
        names.append(
            config_file['Name']
        )

    names = sorted(names)

    ctx.my_output.default(
        'OS configuration files'
    )
    for name in names:
        ctx.my_output.default('- %s' % (name))

    value = ''
    while len(value) == 0:
        if new:
            value = input('New OS configuration filename: ')
        else:
            value = input('Existing OS configuration filename: ')

    return string_fixup(value)


def get_os_config_info(ctx, iaccount):
    vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
    vendors = vendor_handler.get_all()

    config_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
    config_files = config_handler.get_infos(
        vendors
    )

    if config_files is None or len(config_files) == 0:
        ctx.my_output.error('No OS configuration found')
        return None

    ctx.my_output.default(
        'OS configuration files'
    )
    for config_file in config_files:
        ctx.my_output.default('- %s' % (config_file['Name']))

    while True:
        value = input('OS configuration file name: ')
        if len(value) == 0:
            return None

        for config_file in config_files:
            if config_file['Name'] == string_fixup(value):
                return config_file


def get_organization_name(ctx, iaccount):
    organization_handler = organization.Organization(iaccount, log_id=ctx.run_id)

    organizations = organization_handler.get_moids_dict()
    if len(organizations) == 0:
        ctx.my_output.error('No organizations found')
        return None

    if len(organizations) == 1:
        for key in organizations:
            return organizations[key]

    ctx.my_output.default('Intersight Organizations')
    for key in organizations:
        ctx.my_output.default('- %s' % (organizations[key]))

    value = ''
    while len(value) == 0:
        value = input('Organization name: ')

    return string_fixup(value)


def get_organization_id(ctx, iaccount):
    organization_handler = organization.Organization(iaccount, log_id=ctx.run_id)

    organizations = organization_handler.get_moids_dict()
    if len(organizations) == 0:
        ctx.my_output.error('No organizations found')
        return None

    if len(organizations) == 1:
        for key in organizations:
            return key

    ctx.my_output.default('Intersight Organizations')
    for key in organizations:
        ctx.my_output.default('- %s' % (organizations[key]))

    while True:
        value = input('Organization name: ')
        if len(value) == 0:
            return None

        for key in organizations:
            if organizations[key] == string_fixup(value):
                return key


def get_value(ctx, prompt, empty=False):
    value = ''
    while len(value) == 0:
        value = input('%s: ' % (prompt))
        if empty:
            break

    return string_fixup(value)


def get_integer(ctx, prompt, min_value=None, max_value=None):
    value = None
    while value is None:
        input_value = input('%s: ' % (prompt))
        try:
            int_value = int(input_value)
        except BaseException:
            int_value = None

        if int_value is None:
            continue

        if min_value is not None and int_value < min_value:
            continue

        if max_value is not None and int_value > max_value:
            continue

        value = int_value
        break

    return value


def get_ip_address(ctx, prompt, empty=False):
    value = ''
    while len(value) == 0:
        value = input('%s: ' % (prompt))

        if len(value) == 0 and empty:
            break

        if not ip_helper.is_valid_ipv4_address(value):
            value = ''

    return string_fixup(value)


def get_cidr(ctx, prompt, empty=False):
    value = ''
    while len(value) == 0:
        value = input('%s: ' % (prompt))

        if len(value) == 0 and empty:
            break

        if not ip_helper.is_valid_ipv4_cidr(value):
            value = ''

    return string_fixup(value)


def get_prefix_length(ctx, prompt, empty=False):
    value = ''
    while len(value) == 0:
        value = input('%s: ' % (prompt))

        if len(value) == 0 and empty:
            break

        try:
            if int(value) < 8 or int(value) > 30:
                value = ''
        except BaseException:
            value = ''

    return int(value)


def get_selection(ctx, prompt, options):
    ctx.my_output.default('%s:' % (prompt))
    for allowed_value in options:
        ctx.my_output.default('- %s' % (allowed_value))

    value = ''
    while len(value) == 0 or value not in options:
        value = input('Value: ')

    return string_fixup(value)


def get_bool(ctx, prompt):
    selection = get_selection(ctx, prompt, ['T', 'F'])
    if selection == 'T':
        return True
    return False


def get_yaml_file(ctx, prompt, empty=False):
    while True:
        value = input('%s: ' % (prompt))

        if len(value) == 0 and empty:
            return None

        content = file_helper.get_file_yaml(value)
        if content is not None:
            return content
