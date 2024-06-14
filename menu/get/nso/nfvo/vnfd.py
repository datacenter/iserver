import sys
import json
import threading
import traceback
import click

from lib.nso import output as nso_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vnfd")
@click.pass_obj
@click.option("--ncs", "ncs_name", default='', callback=validations.validate_ncs_name, help="NSO name")
@click.option("--protocol", "ncs_protocol", type=click.Choice(['http', 'https'], case_sensitive=False), default='http', show_default=True, help="Protocol")
@click.option("--ip", "ncs_ip", default='', callback=validations.validate_ip, help="NSO IP")
@click.option("--port", "ncs_port", default=8080, help="NSO Port")
@click.option("--username", "ncs_username", default='', help="NSO Username")
@click.option("--password", "ncs_password", default='', help="NSO Password")
@click.option("--nfvo", type=click.Choice(['3.x', 'etsi:4.x'], case_sensitive=False), default='etsi:4.x', show_default=True, help="NFVO Version")
@click.option("--restconf_disabled", is_flag=True, show_default=True, default=False, help="Restconf")
@click.option("--id", "vnfd_id", default='', callback=validations.empty_string_to_none, help="VNFD name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nso_nfvo_vnfd_command(
        ctx,
        ncs_name,
        ncs_protocol,
        ncs_ip,
        ncs_port,
        ncs_username,
        ncs_password,
        nfvo,
        restconf_disabled,
        vnfd_id,
        output,
        devel
        ):
    """Get nso nfvo vnfd"""

    # iserver get nso nfvo vnfd

    ctx.developer = devel
    ctx.output = output

    try:
        nso_output_handler = nso_output.NsoOutput(
            verbose=False,
            debug=devel,
            log_id=ctx.run_id
        )
        nso_handler = validations.validate_nso_nfvo(
            ctx,
            ncs_name,
            ncs_protocol,
            ncs_ip,
            ncs_port,
            ncs_username,
            ncs_password,
            not restconf_disabled,
            nfvo
        )
        if nso_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if vnfd_id is None:
            vnfds = nso_handler.nfvo_handler.get_vnfds()

            ctx.busy = False

            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        vnfds,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(vnfds)

            nso_output_handler.print_vnfds(
                vnfds
            )

        else:
            vnfd = nso_handler.nfvo_handler.get_vnfd(
                vnfd_id=vnfd_id
            )

            ctx.busy = False

            if vnfd is None:
                ctx.my_output.error(
                    'VNFD %s not found' % (vnfd_id)
                )
                raise ErrorExit

            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        vnfd,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(vnfd)

            ctx.my_output.default(
                vnfd
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
