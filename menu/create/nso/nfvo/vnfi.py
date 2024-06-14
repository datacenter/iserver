import sys
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vnfi")
@click.pass_obj
@click.option("--ncs", "ncs_name", default='', callback=validations.validate_ncs_name, help="NSO name")
@click.option("--protocol", "ncs_protocol", type=click.Choice(['http', 'https'], case_sensitive=False), default='http', show_default=True, help="Protocol")
@click.option("--ip", "ncs_ip", default='', callback=validations.validate_ip, help="NSO IP")
@click.option("--port", "ncs_port", default=8080, help="NSO Port")
@click.option("--username", "ncs_username", default='', help="NSO Username")
@click.option("--password", "ncs_password", default='', help="NSO Password")
@click.option("--password", "ncs_password", default='', help="NSO Password")
@click.option("--nfvo", "nfvo_version", type=click.Choice(['3.x', '4.x'], case_sensitive=False), default='4.x', show_default=True, help="NFVO Version")
@click.option("--etsi", "nfvo_etsi", is_flag=True, show_default=True, default=False, help="NFVO ETSI")
@click.option("--restconf_disabled", is_flag=True, show_default=True, default=False, help="Restconf")
@click.option("--xml", "vnfi_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VNF-INFO XML")
@click.option("--wait", is_flag=True, show_default=True, default=False, help="Wait for active")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def create_nso_nfvo_vnfi_command(
        ctx,
        ncs_name,
        ncs_protocol,
        ncs_ip,
        ncs_port,
        ncs_username,
        ncs_password,
        nfvo_version,
        nfvo_etsi,
        restconf_disabled,
        vnfi_filename,
        wait,
        verbose,
        debug
        ):
    """Create nso nfvo vnfi"""

    # iocp create nso nfvo vnfi

    try:
        if debug:
            verbose = True
        ctx.my_output.set_flags(False, verbose, debug)

        if len(vnfi_filename) == 0:
            ctx.my_output.error('Define vnfi xml location')
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        user_input = validations.validate_xml_file(ctx, vnfi_filename)
        if user_input is None:
            raise ErrorExit

        nso_handler = validations.validate_nso_ncs(
            ctx,
            ncs_name,
            ncs_protocol,
            ncs_ip,
            ncs_port,
            ncs_username,
            ncs_password,
            not restconf_disabled,
            nfvo_version,
            nfvo_etsi
        )
        if nso_handler is None:
            raise ErrorExit

        vnfi_name = nso_handler.get_vnfi_name(user_input)
        if nso_handler.is_vnfi(vnfi_name):
            ctx.busy = False
            ctx.my_output.error(
                'VNF-INFO already created'
            )
            return

        success = nso_handler.create_vnfi(
            user_input
        )
        if not success:
            ctx.busy = False
            ctx.my_output.error(
                'VNF-INFO %s create failed' % (vnfi_name)
            )
            raise ErrorExit

        ctx.busy = False
        ctx.my_output.default(
            'VNF-INFO %s created' % (vnfi_name)
        )

        if wait:
            ctx.my_output.default(
                'Wait until VNF-INFO reaches ready state'
            )
            success = nso_handler.wait_for_vnfi_ready(vnfi_name)
            if not success:
                raise ErrorExit

            if not nso_handler.is_vnfi_ready(vnfi_name, cache=False):
                ctx.my_output.error(
                    'VNF-INFO %s activation failed' % (vnfi_name)
                )
                raise ErrorExit

            ctx.my_output.error(
                'VNF-INFO %s ready' % (vnfi_name)
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
