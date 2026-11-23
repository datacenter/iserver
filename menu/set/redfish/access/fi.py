import sys
import threading
import traceback
import click

from progress.bar import Bar

from lib.redfish import endpoint
from lib.redfish import endpoint_settings

from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("fi")
@click.pass_obj
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Fabric Interconnect IP")
@click.option("--port", "endpoint_port", default=443, help="Redfish port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--ssl_verify", is_flag=True, default=False, help="SSL verify")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_redfish_access_fi_command(
        ctx,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        ssl_verify,
        devel
        ):
    """Set redfish access for FI-Attached systems"""

    # iserver set redfish endpoint

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)
    endpoint_type = 'fi'
    try:
        if endpoint_ip == '':
            ctx.my_output.error('Define endpoint IP address')
            raise ErrorExit

        if username == '':
            ctx.my_output.error('Define Redfish access username')
            raise ErrorExit

        if password == '':
            ctx.my_output.error('Define Redfish access password')
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        redfish_handler = endpoint.RedfishEndpoint(
            endpoint_type,
            endpoint_ip,
            endpoint_port,
            username,
            password,
            get_timeout=30,
            ssl_verify=ssl_verify,
            log_id=ctx.run_id,
            verbose=False,
            debug=False
        )

        if not redfish_handler.is_connected():
            ctx.busy = False
            ctx.my_output.error(
                'Redfish access failed'
            )
            raise ErrorExit

        ctx.busy = False

        ctx.my_output.default('\nRedfish authentication successful')

        redfish_handler.endpoint_handler.set_inventory(
            '',
            ''
        )
        inventory = redfish_handler.endpoint_handler.get_inventory()
        if inventory is None:
            ctx.my_output.error('Failed to get fabric interconnect inventory')
            raise ErrorExit

        redfish_handler.endpoint_handler.print_inventory(inventory)
        ctx.my_output.default('')
        if not common.get_confirmation():
            return

        failed = []

        bar_handler = Bar('Chassis', max=len(inventory['chassis']))
        bar_handler.goto(0)
        for item in inventory['chassis']:
            redfish_handler.endpoint_handler.set_inventory(
                'Chassis',
                item['Iom1']
            )

            identity = redfish_handler.endpoint_handler.get_template_identity_chassis_properties()
            if identity is None:
                failed.append(
                    dict(
                        type='Chassis',
                        serial=item['Serial']
                    )
                )
                bar_handler.next()
                continue

            endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
                log_id=ctx.run_id
            )
            success = endpoint_settings_handler.set_redfish_endpoint_settings(
                redfish_handler.endpoint_handler.get_endpoint_configuration(),
                identity
            )
            if not success:
                failed.append(
                    dict(
                        type='Chassis',
                        serial=item['Serial']
                    )
                )

            bar_handler.next()

        bar_handler.finish()

        bar_handler = Bar('Server', max=len(inventory['servers']))
        bar_handler.goto(0)
        for item in inventory['servers']:
            redfish_handler.endpoint_handler.set_inventory(
                'Server',
                item['Name']
            )

            identity = redfish_handler.endpoint_handler.get_template_identity_server_properties()
            if identity is None:
                failed.append(
                    dict(
                        type='Server',
                        serial=item['Serial']
                    )
                )
                bar_handler.next()
                continue

            endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
                log_id=ctx.run_id
            )
            success = endpoint_settings_handler.set_redfish_endpoint_settings(
                redfish_handler.endpoint_handler.get_endpoint_configuration(),
                identity
            )
            if not success:
                failed.append(
                    dict(
                        type='Server',
                        serial=item['Serial']
                    )
                )

            bar_handler.next()

        bar_handler.finish()

        if len(failed) == 0:
            ctx.my_output.default('All FI-attached redfish endpoints settings saved')
            return

        ctx.my_output.default('')
        ctx.my_output.error('Not all FI-attached redfish endpoints settings saved')
        for item in failed:
            ctx.my_output.default('- Inventory Type [%s] Serial [%s]' % (item['type'], item['serial']))
        raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
