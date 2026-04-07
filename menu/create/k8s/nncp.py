import sys
import traceback
import click
import yaml

from lib.workflow.k8s import nncp_input
from lib.workflow.k8s import nncp_generate
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nncp")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--no-create", "no_create", is_flag=True, show_default=True, default=False, help="No creation")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation")
def create_k8s_nncp_command(
        ctx,
        cluster_name,
        no_create,
        no_confirm
        ):
    """Create k8s nncp"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        params = nncp_input.run(k8s_handlers, ctx.my_output)
        if params is None:
            raise ErrorExit
        
        params['k8s_handler'] = k8s_handlers
        data = nncp_generate.run(
            params,
            ctx.my_output
        )
        if data is None:
            raise ErrorExit

        ctx.my_output.default('Generated CRDs', underline=True, before_newline=True)
        ctx.my_output.default(
            yaml.dump(data['nncp']),
            before_newline=True,
            after_newline=True
        )

        if no_create:
            return
        
        success = params['k8s_handler'].create_node_network_configuration_policy(
            data['nncp'],
            confirmation=not no_confirm, 
            my_output=ctx.my_output, 
            wait=True
        )
        if not success:
            raise ErrorExit
        
        if data['delete']:
            success = k8s_handlers.delete_node_network_configuration_policy_mo(
                data['nncp']['metadata']['name']
            )
            if not success:
                ctx.my_output.error('Delete rest api failed')
                raise ErrorExit
            
            ctx.my_output.default('NNCP deleted')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
