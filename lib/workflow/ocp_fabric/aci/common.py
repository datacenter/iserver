from lib.aci import apic
from lib.aci import settings as aci_settings


def get_controller_ip(controller_name, my_output, log_id):
    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    controller = aci_settings_handler.get_apic_controller(controller_name)
    if controller is None:
        my_output.error('APIC controller not defined: %s' % (controller_name))
        return None

    return controller['ip']


def get_handler(controller_name, my_output, log_id):
    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    controller = aci_settings_handler.get_apic_controller(controller_name)
    if controller is None:
        my_output.error('APIC controller not defined: %s' % (controller_name))
        return None

    apic_handler = apic.Apic(
        controller['ip'],
        controller['port'],
        controller['username'],
        controller['password'],
        apic_name=controller_name,
        log_id=log_id,
        requested_ttl=-1,
        debug=True
    )

    if not apic_handler.is_connected():
        my_output.error('Failed to connect to APIC: %s' % (controller_name))
        return None

    return apic_handler