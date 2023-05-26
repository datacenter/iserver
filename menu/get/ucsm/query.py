import sys
import json
import traceback
import click

from lib.ucsm import manager

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("query")
@click.pass_obj
@click.option("--manager", "ucsm", default='', callback=validations.validate_ucsm_name, help="UCSM manager name")
@click.option("--class-id", "class_id", default='', help="Class Id")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ucsm_query_command(
        ctx,
        ucsm,
        class_id,
        devel
        ):
    """Get ucsm api query"""

    # iserver get ucsm query

    ctx.developer = devel

    try:
        if len(class_id) == 0:
            ctx.my_output.error('Define class id')
            raise ErrorExit

        ucsm_handler = manager.UcsManager(
            ucsm['ip'],
            ucsm['username'],
            ucsm['password'],
            log_id=ctx.run_id
        )

        if not ucsm_handler.is_connected():
            ctx.my_output.error('Failed to connect to UCSM')
            raise ErrorExit

        response = ucsm_handler.query_classid(
            class_id
        )
        if response is None:
            ctx.my_output.error('Failed to get class id: %s' % (class_id))
            raise ErrorExit

        if isinstance(response, list):
            for item in response:
                ctx.my_output.default(str(item))
        else:
            ctx.my_output.default(str(item))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
