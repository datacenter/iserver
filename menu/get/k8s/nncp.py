import sys
import json
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from lib import file_helper
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("nncp")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--file", "input_filename", default='', callback=validations.empty_string_to_none, help="Load managed objects from file")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--wait", is_flag=True, show_default=True, default=False, help="Wait until all nncp complete")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_nncp_command(
        ctx,
        cluster,
        name,
        input_filename,
        view,
        output,
        wait,
        devel
        ):
    """Get k8s node network configuration policy"""

    # iserver get k8s nncp

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if output not in ['json', 'mo']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        if input_filename is not None:
            content = file_helper.get_file_json(input_filename)
            if content is None:
                ctx.my_output.error(
                    'File read failed'
                )
                raise ErrorExit
            
            k8s_handlers.set_node_network_configuration_policy_mo(content)
            
        if output == 'mo':
            policies = k8s_handlers.get_node_network_configuration_policies(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    policies,
                    indent=4
                )
            )
            return

        policies = k8s_handlers.get_node_network_configuration_policies(
            object_filter=object_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    policies,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(policies)

        if 'state' in view:
            k8s_output_handler.print_node_network_configuration_policy(
                policies,
                title=True
            )

        ctx.my_output.default('Filter: name', before_newline=True)
        ctx.my_output.default('View:   state (def)')

        if wait:
            k8s_handlers.wait_node_network_configuration_policy(my_output=ctx.my_output)

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
