import sys
import json
import traceback
import threading
import click

from lib.ocp import settings
from lib.iwo.lcm import main as iwo
from lib.ocp import output as ocp_output
from lib.ocp import main as ocp

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify access")
@click.option("--view", "-v", type=click.Choice(['default', 'state', 'vcenter', 'kc', 'manager', 'iwo', 'console', 'cnv', 'all'], case_sensitive=False), multiple=False, default='default')
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_cluster_command(
        ctx,
        cluster_name,
        verify,
        view,
        output,
        devel
        ):
    """Get ocp cluster"""

    # iserver get ocp cluster

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_output_handler = ocp_output.OcpOutput(log_id=ctx.run_id)
        settings_handler = settings.OcpSettings(log_id=ctx.run_id)

        cluster_filter = []
        if cluster_name is not None:
            if '*' not in cluster_name:
                cluster_name = '*%s*' % (cluster_name)
            cluster_filter.append(
                'name:%s' % (cluster_name)
            )

        clusters = settings_handler.get_ocp_clusters(
            cluster_filter=cluster_filter
        )

        if clusters is None:
            ctx.busy = False
            raise ErrorExit

        if len(clusters) == 0:
            ctx.my_output.error('No cluster matching filtering critera')
            raise ErrorExit

        if view == 'default':
            if output == 'json':
                ctx.busy = False
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        clusters,
                        indent=4
                    )
                )
                return

            ctx.busy = False
            ctx.my_output.json_output(clusters)
            ocp_output_handler.print_ocp_clusters(
                clusters
            )

        if view == 'state':
            states_info = []

            for cluster_settings in clusters:
                cluster_handler = ocp.Ocp(
                    cluster_settings['name'],
                    log_id=ctx.run_id
                )

                state_info = {}
                state_info['name'] = cluster_settings['name']
                state_info['online'] = False
                ocp_version = cluster_handler.k8s_handler.get_version()
                if ocp_version is not None:
                    state_info['online'] = True
                    for key in ocp_version:
                        state_info[key] = ocp_version[key]

                ocp_cni = cluster_handler.k8s_handler.get_cni()
                if ocp_cni is not None:
                    for key in ocp_cni:
                        state_info[key] = ocp_cni[key]

                states_info.append(
                    state_info
                )

            ctx.busy = False
            ctx.my_output.json_output(states_info)

            ocp_output_handler.print_ocp_clusters_state(
                states_info
            )

        if view == 'manager':
            managers_info = []

            for cluster_settings in clusters:
                cluster_handler = ocp.Ocp(
                    cluster_settings['name'],
                    log_id=ctx.run_id
                )
                manager_info = cluster_handler.get_ocp_cluster_manager_info(
                    validate=verify
                )
                if manager_info is not None:
                    managers_info.append(
                        manager_info
                    )

            if output == 'json':
                ctx.busy = False
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        managers_info,
                        indent=4
                    )
                )
                return

            ctx.busy = False
            ctx.my_output.json_output(managers_info)
            ocp_output_handler.print_ocp_clusters_manager(
                managers_info
            )

        if view == 'kc':
            kubeconfigs_info = []

            for cluster_settings in clusters:
                cluster_handler = ocp.Ocp(
                    cluster_settings['name'],
                    log_id=ctx.run_id
                )
                kubeconfig_info = cluster_handler.get_ocp_cluster_kubeconfig_info(
                    validate=verify
                )
                if kubeconfig_info is not None:
                    kubeconfigs_info.append(
                        kubeconfig_info
                    )

            ctx.busy = False
            ctx.my_output.json_output(kubeconfigs_info)

            ocp_output_handler.print_ocp_clusters_kubeconfig(
                kubeconfigs_info,
                title=True
            )

        if view == 'vcenter':
            clusters_info = []

            for cluster_settings in clusters:
                cluster_handler = ocp.Ocp(
                    cluster_settings['name'],
                    log_id=ctx.run_id
                )
                cluster_info = cluster_handler.get_ocp_cluster_vcenter_info()
                if cluster_info is not None:
                    clusters_info.append(
                        cluster_info
                    )

            if output == 'json':
                ctx.busy = False
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        clusters_info,
                        indent=4
                    )
                )
                return

            ctx.busy = False
            ctx.my_output.json_output(clusters_info)
            ocp_output_handler.print_ocp_clusters_vcenter(
                clusters_info
            )

        if view == 'iwo':
            settings_handler = settings.OcpSettings(log_id=ctx.run_id)

            clusters = settings_handler.get_ocp_clusters_iwo()
            if clusters is None:
                ctx.busy = False
                ctx.my_output.error('Failed to get OCP clusters')
                raise ErrorExit

            iwo_handler = iwo.IwoLcm(
                verbose=False,
                debug=False,
                log_id=ctx.run_id
            )
            for cluster in clusters:
                state = iwo_handler.get_lcm_state(cluster['iwo'])
                for key in state:
                    cluster[key] = state[key]

            if output == 'json':
                ctx.busy = False
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        clusters,
                        indent=4
                    )
                )
                return

            ctx.busy = False
            ctx.my_output.json_output(clusters)

            ocp_output_handler.print_ocp_clusters_iwo(clusters)

        if view == 'console':
            consoles_info = []

            for cluster_settings in clusters:
                cluster_handler = ocp.Ocp(
                    cluster_settings['name'],
                    log_id=ctx.run_id
                )
                console_info = cluster_handler.get_ocp_cluster_console_info()
                if console_info is not None:
                    consoles_info.append(
                        console_info
                    )

            ctx.busy = False
            ctx.my_output.json_output(consoles_info)

            ocp_output_handler.print_ocp_clusters_console(
                consoles_info
            )

        if view == 'cnv':
            ocp_handler = validations.validate_ocp_cluster(
                ctx,
                cluster_name
            )
            if ocp_handler is None:
                raise ErrorExit

            if not ocp_handler.is_connected():
                ctx.busy = False
                ctx.my_output.error(
                    'OCP connection failed'
                )
                raise ErrorExit

            cnv = ocp_handler.get_ocp_cnv_state()
            nodes = ocp_handler.get_ocp_nodes_info()

            info = {}
            info['cnv'] = cnv
            info['nodes'] = nodes

            ctx.busy = False

            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        info,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(info)
            ocp_handler.print_ocp_cnv_state(cnv)
            ocp_handler.print_ocp_nodes_list(nodes)

        ctx.busy = False

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
