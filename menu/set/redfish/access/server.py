import sys
import threading
import traceback
import click

from progress.bar import Bar

from lib.intersight import compute
from lib.redfish import endpoint
from lib.redfish import endpoint_settings

from menu import defaults
from menu import common
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial strict match filter")
@click.option("--model", "model_filter", default='', help="Model loose match filter")
@click.option("--type", "endpoint_type", type=click.Choice(['ucsc', 'dell', 'hpe'], case_sensitive=False), default='ucsc', help="Redfish endpoint type")
@click.option("--redfish-ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Redfish endpoint IP address")
@click.option("--port", "endpoint_port", default=443, help="Redfish management TCP port")
@click.option("--username", default='', help="Redfish username")
@click.option("--password", default='', help="Redfish password")
@click.option("--ssl_verify", is_flag=True, default=False, help="SSL verify")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_redfish_access_server_command(
        ctx,
        iaccount,
        ip_filter,
        group,
        name_filter,
        serial_filter,
        model_filter,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        username,
        password,
        ssl_verify,
        devel
        ):
    """Set redfish access for standalone servers"""

    # iserver set redfish servers

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if username == '':
            ctx.my_output.error('Define Redfish access username')
            raise ErrorExit

        if password == '':
            ctx.my_output.error('Define Redfish access password')
            raise ErrorExit

        if len(endpoint_ip) > 0:
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
                log_id=ctx.run_id
            )

            if not redfish_handler.is_connected():
                ctx.busy = False
                ctx.my_output.error('Redfish authentication failed')
                raise ErrorExit

            identity = redfish_handler.endpoint_handler.get_template_identity_properties()
            if identity is None:
                ctx.busy = False
                ctx.my_output.error('Failed to get server identity information')
                raise ErrorExit

            endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
                log_id=ctx.run_id
            )
            success = endpoint_settings_handler.set_redfish_endpoint_settings(
                redfish_handler.endpoint_handler.get_endpoint_configuration(),
                identity
            )
            if not success:
                ctx.busy = False
                ctx.my_output.error('Failed to save server information locally')
                raise ErrorExit

            ctx.busy = False
            ctx.my_output.default('Redfish endpoints settings verified and saved')

        if len(endpoint_ip) == 0:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

            compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
            match_rules = compute_handler.get_mo_match_rules(
                ip_filter=ip_filter,
                name_filter=name_filter,
                serial_filter=serial_filter + group
            )
            all_servers_mo = compute_handler.get_mo(
                match_rules=match_rules,
                include_rack=True,
                include_blade=False
            )

            servers_mo = []
            for server_mo in all_servers_mo:
                if server_mo['ManagementMode'] == 'IntersightStandalone':
                    servers_mo.append(
                        server_mo
                    )

            ctx.busy = False
            if servers_mo is None or len(servers_mo) == 0:
                ctx.my_output.error('No servers found')
                raise ErrorExit

            bar_handler = Bar('Rack servers in Intersight Standalone Management Mode', max=len(servers_mo))
            failed = []
            bar_handler.goto(0)
            for item in servers_mo:
                if item['ManagementIp'] is None:
                    failed.append(
                        dict(
                            name=item['Name'],
                            reason='No management IP'
                        )
                    )
                    bar_handler.next()
                    continue

                redfish_handler = endpoint.RedfishEndpoint(
                    endpoint_type,
                    item['ManagementIp'],
                    endpoint_port,
                    username,
                    password,
                    get_timeout=30,
                    ssl_verify=ssl_verify,
                    log_id=ctx.run_id
                )

                if not redfish_handler.is_connected():
                    failed.append(
                        dict(
                            name=item['Name'],
                            reason='Redfish authentication failed'
                        )
                    )
                    bar_handler.next()
                    continue

                identity = redfish_handler.endpoint_handler.get_template_identity_properties()
                if identity is None:
                    failed.append(
                        dict(
                            name=item['Name'],
                            reason='Failed to get redfish server identity'
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
                            name=item['Name'],
                            reason='Failed to save endpoint configuration'
                        )
                    )
                    bar_handler.next()
                    continue

                bar_handler.next()

            bar_handler.finish()

            if len(failed) == 0:
                ctx.my_output.default('All redfish endpoints settings saved and access verified')
                return

            ctx.my_output.error('Not all redfish endpoints settings saved')
            for failure in failed:
                ctx.my_output.default('- %s: %s' % (failure['name'], failure['reason']))

            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
