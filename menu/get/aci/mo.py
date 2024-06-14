import sys
import json
import threading
import traceback
import click

from lib import log_helper
from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("mo")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--dn", "-d", "mo_dn", default='', help="Managed object distinguished name")
@click.option("--class", "-c", "class_name", default='', help="Class name")
@click.option("--option", "-x", "extra_options", help="Extra options", multiple=True)
@click.option("--node", is_flag=True, show_default=True, default=False, help="Node specific")
@click.option("--limit", "imdata_limit", default=1, help="Limit objects")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_aci_mo_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        mo_dn,
        class_name,
        extra_options,
        node,
        imdata_limit,
        output
        ):
    """Get aci managed object"""

    # iserver get aci managed object

    ctx.developer = False
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=True
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()
        else:
            ctx.my_output.error(
                'Define single APIC'
            )
            raise ErrorExit

        apic_handler = apic_handlers[0]['handler']

        if len(mo_dn) == 0 and len(class_name) == 0:
            ctx.my_output.error(
                'Define DN or Class'
            )
            raise ErrorExit

        if len(mo_dn) > 0 and len(class_name) > 0:
            ctx.my_output.error(
                'Define DN or Class'
            )
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if len(class_name) > 0:
            query = None
            if len(extra_options) > 0:
                query = '&'.join(extra_options)
            managed_objects = apic_handler.get_class(
                class_name,
                query=query,
                node_class=node
            )
            request_info = apic_handler.get_request_info()

        if len(mo_dn) > 0:
            query = None
            if len(extra_options) > 0:
                query = '&'.join(extra_options)
            managed_objects = apic_handler.get_managed_object(
                mo_dn,
                query=query,
                node_mo=node
            )
            request_info = apic_handler.get_request_info()

        ctx.busy = False

        if request_info['connected']:
            if output not in ['json']:
                ctx.my_output.default('URL: %s' % (request_info['url']))
                ctx.my_output.default('Response code: %s' % (request_info['status_code']))
                ctx.my_output.default('Duration [ms]: %s' % (request_info['duration']))
                if request_info['error'] is not None:
                    ctx.my_output.default('Error: %s' % (request_info['error']))

            if managed_objects is not None:
                if output not in ['json']:
                    ctx.my_output.default('Total count: %s' % (managed_objects['totalCount']))

                if imdata_limit == 0:
                    ctx.my_output.default(
                        json.dumps(
                            managed_objects['imdata'],
                            indent=4
                        )
                    )

                if imdata_limit > 0:
                    ctx.my_output.default(
                        json.dumps(
                            managed_objects['imdata'][:imdata_limit],
                            indent=4
                        )
                    )

        log_handler = log_helper.Log(log_id=ctx.run_id)
        log_handler.apic_mo(
            'result',
            managed_objects
        )

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
