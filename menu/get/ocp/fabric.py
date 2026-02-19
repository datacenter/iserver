import sys
import traceback
import click

from lib.workflow.ocp_bm_install import input as ocp_installer
from lib.workflow.ocp_fabric import main as ocp_fabric
from lib.workflow.ocp_fabric import validations as fabric_validations

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("fabric")
@click.pass_obj
@click.option("--dir", "location", is_flag=False, show_default=False, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Cluster definition directory")
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Select cluster by name")
def get_ocp_cluster_fabric_command(ctx, cluster_name, location):
    """Get OCP cluster fabric state"""

    try:
        if cluster_name is None and location is None:
            ctx.my_output.error(
                'Define cluster name or installation settings location'
            )
            raise ErrorExit

        if location is not None:
            user_settings = ocp_installer.get_input(
                location,
                ctx.my_output
            )
            if user_settings is None:
                raise ErrorExit

            if 'fabric' not in user_settings:
                ctx.my_output.error('fabric not defined')
                raise ErrorExit
            
            fabric = user_settings['fabric']

        if cluster_name is not None:
            fabric = ocp_fabric.get_fabric_configuration(
                cluster_name,
                log_id=ctx.run_id
            )
            if fabric is None:
                ctx.my_output.error(
                    'Fabric info not cached locally'
                )
                raise ErrorExit

        # fabric = fabric_validations.run(
        #     fabric, 
        #     'check', 
        #     ctx.my_output, 
        #     ctx.run_id
        # )

        success = ocp_fabric.run_check(
            fabric, 
            ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
