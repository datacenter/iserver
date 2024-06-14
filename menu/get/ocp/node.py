import sys
import json
import traceback
import threading
import click

from lib.ocp import settings
from lib.ocp import output as ocp_output
from lib.ocp import main as ocp

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("node")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster node name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--label", default='', callback=validations.empty_string_to_none, help="Filter by node label")
@click.option("--view", "-v", type=click.Choice(['default', 'version', 'label', 'sriov', 'sriov-phy', 'sriov-policy', 'sriov-network', 'sriov-vf', 'all'], case_sensitive=False), multiple=False, default='default')
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_node_command(
        ctx,
        cluster_name,
        node_name,
        node_role,
        label,
        view,
        output,
        devel
        ):
    """Get ocp node"""

    # iserver get ocp node

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_output_handler = ocp_output.OcpOutput(log_id=ctx.run_id)
        settings_handler = settings.OcpSettings(log_id=ctx.run_id)

        if cluster_name is None:
            cluster_name = settings_handler.get_default_cluster()
            if cluster_name is not None and output == 'default':
                ctx.my_output.default('Cluster: %s' % (cluster_name))

        cluster_filter = []

        if cluster_name is not None:
            cluster_filter.append(
                'name:%s' % (cluster_name)
            )

        clusters = settings_handler.get_ocp_clusters(
            cluster_filter=cluster_filter
        )

        if clusters is None or len(clusters) == 0:
            ctx.busy = False
            raise ErrorExit

        nodes = []

        node_filter = []

        if node_name is not None:
            node_filter.append(
                'name:%s' % (node_name)
            )

        if node_role != 'any':
            if node_role == 'master':
                node_filter.append(
                    'master:true'
                )
            if node_role == 'worker':
                node_filter.append(
                    'worker:true'
                )

        if label is not None:
            node_filter.append(
                'label:%s' % (label)
            )

        sriov_phy_info = False
        sriov_policy_info = False
        sriov_network_info = False
        sriov_vf_info = False

        if view in ['sriov', 'all']:
            sriov_phy_info = True
            sriov_policy_info = True
            sriov_network_info = True
            sriov_vf_info = True

        if view == 'sriov-phy':
            sriov_phy_info = True

        if view == 'sriov-policy':
            sriov_policy_info = True

        if view == 'sriov-network':
            sriov_network_info = True

        if view == 'sriov-vf':
            sriov_vf_info = True

        for cluster_settings in clusters:
            cluster_handler = ocp.Ocp(
                cluster_settings['name'],
                log_id=ctx.run_id
            )
            cluster_nodes_info = cluster_handler.get_ocp_nodes(
                node_filter=node_filter,
                sriov_phy_info=sriov_phy_info,
                sriov_policy_info=sriov_policy_info,
                sriov_network_info=sriov_network_info,
                sriov_vf_info=sriov_vf_info
            )
            if cluster_nodes_info is not None:
                nodes = nodes + cluster_nodes_info

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    nodes,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(nodes)

        if view in ['default', 'all']:
            pass

        if view in ['version', 'all']:
            pass

        if view in ['label', 'all']:
            pass

        if view in ['sriov-phy', 'sriov', 'all']:
            ocp_output_handler.print_ocp_nodes_sriov_phy(nodes, title=True)

        if view in ['sriov-policy', 'sriov', 'all']:
            ocp_output_handler.print_ocp_nodes_sriov_policy(nodes, title=True)

        if view in ['sriov-network', 'sriov', 'all']:
            ocp_output_handler.print_ocp_nodes_sriov_network(nodes, title=True)

        if view in ['sriov-vf', 'sriov', 'all']:
            ocp_output_handler.print_ocp_nodes_sriov_vf(nodes, title=True)

        ctx.busy = False

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
