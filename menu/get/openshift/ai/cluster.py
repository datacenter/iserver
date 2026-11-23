import sys
import traceback
import json
import threading
import click

from lib.openshift import console
from lib.openshift import output as openshift_output

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--view", "-v", default=['state'], help="[state|config|cred|host|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--insecure", is_flag=True, show_default=True, default=False, help="No SSL verification")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_openshift_ai_cluster_command(
        ctx,
        name,
        view,
        output,
        insecure,
        devel
        ):
    """Get openshift assisted installer clusters"""

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|config|cred|host|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        openshift_output_handler = openshift_output.OpenshiftOutput(log_id=ctx.run_id)
        console_handler = console.Console(log_id=ctx.run_id, check_ssl=not insecure)

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        subscriptions = console_handler.get_accounts_mgmt_subscription_mo()
        if subscriptions is None:
            ctx.my_output.error('Failed to get subscriptions')
            raise ErrorExit

        cluster_ids = []
        for subscription in subscriptions:
            cluster_ids.append(
                subscription['cluster_id']
            )

        config_info = False
        if 'config' in view:
            config_info = True
        
        credentials_info = False
        if 'cred' in view:
            credentials_info = True
        
        infra_info = False
        if 'state' in view:
            infra_info = True
        
        manifest_info = False
        if 'state' in view:
            manifest_info = True
        
        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if len(cluster_ids) > 0:
            object_filter.append(
                'ids:%s' % (','.join(cluster_ids))
            )

        clusters = console_handler.get_assisted_install_clusters(
            assisted_install_cluster_filter=object_filter,
            config_info=config_info,
            credentials_info=credentials_info,
            infra_info=infra_info,
            manifest_info=manifest_info,
            kubeconfig_info=credentials_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    clusters,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(clusters)

        openshift_output_handler.print_assisted_install_clusters_state(clusters, title=True)
        for cluster in clusters:
            openshift_output_handler.print_assisted_install_cluster(cluster, view)

        ctx.my_output.default('Filter: name', before_newline=True)
        ctx.my_output.default('View:   state (def), config, cred, host, all')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
