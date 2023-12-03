import sys
import traceback
import click
import yaml

from lib.k8s import output as k8s_output

from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("srnnp")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--namespace", default='openshift-sriov-network-operator', callback=validations.empty_string_to_none, help="Policy namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Policy name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_k8s_srnnp_command(
        ctx,
        cluster_name,
        namespace,
        name,
        devel
        ):
    """Delete k8s srnnp"""

    # iserver delete k8s srnnp

    ctx.developer = devel
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        if namespace is None:
            ctx.my_output.error('Define policy namespace')
            raise ErrorExit

        if namespace not in ['openshift-sriov-network-operator']:
            ctx.my_output.error('Unsupported policy namespace')
            raise ErrorExit

        if name is None:
            ctx.my_output.error('Define policy name')
            raise ErrorExit

        sriov_network_node_policy_info = k8s_handlers.get_sriov_network_node_policy(
            name,
            sriov_network_info=True
        )
        if sriov_network_node_policy_info is None:
            ctx.my_output.error('SR-IOV network node policy not found: %s' % (name))
            raise ErrorExit

        k8s_output_handler.print_sriov_network_node_policies(
            [sriov_network_node_policy_info],
            title=False
        )

        if sriov_network_node_policy_info['sriov_network_count'] > 0:
            ctx.my_output.error(
                'SR-IOV network node policy is used and cannot be deleted'
            )
            raise ErrorExit

        if not common.get_confirmation():
            raise ErrorExit

        if not k8s_handlers.delete_sriov_network_node_policy(sriov_network_node_policy_info['namespace'], sriov_network_node_policy_info['name']):
            ctx.my_output.error(
                'SR-IOV network node policy delete failed'
            )
            raise ErrorExit

        ctx.my_output.default(
            'SR-IOV network node policy deleted'
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
