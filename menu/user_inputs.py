from lib import ip_helper

from lib.intersight import scu
from lib.intersight import os_image
from lib.intersight import organization
from lib.intersight import hcl_operating_system_vendor
from lib.intersight import hcl_operating_system


def string_fixup(value):
    value = value.strip()
    return value


def get_scu_name(ctx, iaccount):
    scu_handler = scu.SoftwareConfigurationUtility(iaccount, log_id=ctx.run_id)
    items = scu_handler.get_all()
    scu_handler.print(items)

    value = ''
    while len(value) == 0:
        value = input('SCU name: ')

    return string_fixup(value)


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


def get_os_image_name(ctx, iaccount):
    image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
    items = image_handler.get_all()
    image_handler.print(items)

    value = ''
    while len(value) == 0:
        value = input('OS Image name: ')

    return string_fixup(value)


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


def get_value(ctx, prompt, empty=False):
    value = ''
    while len(value) == 0:
        value = input('%s: ' % (prompt))
        if empty:
            break

    return string_fixup(value)


def get_ip_address(ctx, prompt, empty=False):
    value = ''
    while len(value) == 0:
        value = input('%s: ' % (prompt))

        if len(value) == 0 and empty:
            break

        if not ip_helper.is_valid_ipv4_address(value):
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
