import sys
import traceback
import click

from menu import validations
from lib.k8s import output as k8s_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("test")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
def set_k8s_test(
        ctx,
        cluster_name
        ):
    """Test"""

    ctx.developer = False

    k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
    k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp', log_id=ctx.run_id)
                                                        
    # print(k8s_handlers.create_namespace('aaaa'))

    print(k8s_handlers.get_namespace('aaaa'))

    print(k8s_handlers.delete_namespace_mo('aaaa'))