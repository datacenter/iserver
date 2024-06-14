import os
import time
import json
import sys
import traceback
import threading
import click

from lib import ip_helper
from lib.osp import output as osp_output

from menu import progress
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("flv")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--name", "flavor_name", default='', callback=validations.empty_string_to_none, help="Flavor name")
@click.option("--cpu", default=1, type=click.INT, help="CPU")
@click.option("--mem", default=2048, type=click.INT, help="Memory")
@click.option("--disk", default=20, type=click.INT, help="Disk")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_flv_command(
        ctx,
        cluster_name,
        flavor_name,
        cpu,
        mem,
        disk,
        devel
        ):
    """Create osp flv"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
        if osp_handlers is None:
            raise ErrorExit

        if flavor_name is None:
            flavor_name = input('New flavor name: ')
            if flavor_name is None or len(flavor_name) == 0:
                raise ErrorExit

            cpu = common.get_integer('CPU: ')
            if cpu <= 0:
                raise ErrorExit

            mem = common.get_integer('Memory [MB]: ')
            if mem <= 0:
                raise ErrorExit

            disk = common.get_integer('Disk [GB]: ')
            if disk < 0:
                raise ErrorExit

        if osp_handlers.is_flavor(flavor_name=flavor_name):
            ctx.my_output.error('Flavor already exists: %s' % (flavor_name))
            raise ErrorExit

        ctx.my_output.default('Creating new flavor...')
        new_flavor_id = osp_handlers.create_flavor_mo(
            flavor_name,
            mem,
            cpu,
            disk
        )

        if new_flavor_id is None:
            ctx.my_output.error('Flavor create failed')
            raise ErrorExit

        ctx.my_output.default('Flavor created: %s' % (new_flavor_id))

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
