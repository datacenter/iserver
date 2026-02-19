from lib.aci import apic
from lib.aci import settings as aci_settings


def get_apic_handler(connector, my_output, log_id):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)

    controller_obj = aci_settings_handler.get_apic_controller(connector)
    if controller_obj is None:
        my_output.error('Invalid apic connector: %s' % (connector))
        return None

    apic_handler = apic.Apic(
        controller_obj['ip'],
        controller_obj['port'],
        controller_obj['username'],
        controller_obj['password'],
        apic_name=controller_obj['name'],
        log_id=log_id,
        requested_ttl=-1
    )

    if not apic_handler.is_connected():
        my_output.error('Failed to connect to APIC')
        return None

    return apic_handler