import sys
import traceback
import click
import yaml

from lib import file_helper

from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("nncp")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--file", "input_filename", default='', callback=validations.empty_string_to_none, help="Input data")
@click.option("--no-create", "no_create", is_flag=True, show_default=True, default=False, help="No creation")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_k8s_nncp_command(
        ctx,
        cluster_name,
        input_filename,
        no_create,
        no_confirm,
        devel
        ):
    """Create k8s nncp"""

    # iserver create k8s nncp

    ctx.developer = devel
    ctx.output = 'default'

    try:
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        if input_filename is None:
            params = k8s_handlers.get_nncp_input_data(ctx.my_output)
            if params is None:
                raise ErrorExit
            
            input_data = [params]

        if input_filename is not None:
            input_data = file_helper.get_file_json(input_filename)
            if input_data is None:
                ctx.my_output.error('File read failed')
                raise ErrorExit
            
        data = k8s_handlers.generate_nncp(
            input_data,
            ctx.my_output
        )
        if data is None:
            raise ErrorExit

        ctx.my_output.default('Generated CRDs', underline=True, before_newline=True)
        for item in data:
            ctx.my_output.default(
                yaml.dump(item['nncp']),
                before_newline=True,
                after_newline=True
            )

        if no_create:
            return
        
        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        ctx.my_output.default('Create NNCP', underline=True, before_newline=True)
        for item in data:
            ctx.my_output.default('- %s' % (item['nncp']['metadata']['name']))
            success = k8s_handlers.create_node_network_configuration_policy(item['nncp'])
            if not success:
                ctx.my_output.error('REST API failed')
                raise ErrorExit
        
            success = k8s_handlers.wait_node_network_configuration_policies_status(
                [item['nncp']['metadata']['name']],
                my_output=ctx.my_output
            )
            if not success:
                raise ErrorExit
        
            nncp = k8s_handlers.get_node_network_configuration_policy(
                item['nncp']['metadata']['name'],
                cache_enabled=False
            )
            if nncp is None:
                ctx.my_output.error(
                    'Failed to get nncp %s' % (item['nncp']['metadata']['name'])
                )
                raise ErrorExit
            
            ctx.my_output.default('Status: %s' % (nncp['status']))
            if not nncp['available']:
                ctx.my_output.error('Unexpected nncp state')
                raise ErrorExit
            
            if item['delete']:
                success = k8s_handlers.delete_node_network_configuration_policy_mo(
                    item['nncp']['metadata']['name']
                )
                if not success:
                    ctx.my_output.error('Delete rest api failed')
                    raise ErrorExit
                
                ctx.my_output.default('NNCP deleted')
                
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
