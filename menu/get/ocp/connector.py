import sys
import traceback
import click
from progress.bar import Bar

from lib.workflow.ocp_access import check
from lib.ocp import settings
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("connector")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--view", "-v", default=['list'], help="[list|access|cli]", show_default=True, multiple=True)
def get_ocp_connector(
        ctx,
        cluster_name,
        domain_name,
        view
        ):
    """Get ocp connector"""

    ctx.developer = False

    ctx.developer = False
    ctx.output = 'default'
    view = validations.validate_view(
        ctx,
        view,
        'list|access|cli',
        'list',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        settings_handler = settings.OcpSettings(log_id=ctx.run_id)
        cluster_filter = []
        if cluster_name is not None:
            cluster_filter.append('name:%s' % (cluster_name))
        if domain_name is not None:
            cluster_filter.append('domain:%s' % (domain_name))

        clusters = settings_handler.get_ocp_clusters(
            cluster_filter=cluster_filter,
            files_info=True
        )

        if clusters is None:
            ctx.my_output.error('Failed to get connectors')
            raise ErrorExit
        
        order = [
            'name',
            'domain',
            'isKubeTick',
            'isSshTick',
            'management_ip'
        ]

        headers = [
            'Cluster',
            'Domain',
            'Kubeconfig',
            'SSH Public Key',
            'Management IP'
        ]

        ctx.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            cast_none=True,
            table=True
        )

        if len(clusters) == 0 or 'list' in view:
            ctx.my_output.default('Filter: cluster, domain', before_newline=True)
            ctx.my_output.default('View:   list (def), access, cli')
            return
        
        ctx.my_output.default('')
        bar_handler = Bar('Collect cluster access', max=len(clusters))

        cli = False
        if 'cli' in view:
            cli = True

        access = []
        for cluster in clusters:
            params = {}
            params['cluster'] = cluster['name']
            params['kc-check'] = True
            params['kc-required'] = False
            params['kube-api-check'] = True
            params['kube-api-required'] = False
            params['fqdn-required'] = False
            params['ssh-check'] = True
            params['ssh-required'] = False
            params['ssh-fixup'] = False
            params['mgmt-check'] = True
            params['mgmt-required'] = False
            params['mgmt-fixup'] = False
            params['cli-check'] = cli
            params['verbose'] = False
            params['break-on-error'] = False
            params['none-on-error'] = False

            params, errors = check.run(
                params,
                log_id=ctx.run_id
            )

            result = params['result']
            result['__Output'] = {}
            for key in params['__Output']:
                result['__Output'][key.split('.')[1]] = params['__Output'][key]
            result['cluster'] = cluster['name']
            result['errors'] = errors
            access.append(result)

            bar_handler.next()

        bar_handler.finish()

        order = [
            'cluster',
            'api_hostname',
            'domain',
            'fqdnTick',
            'kubeTick',
            'sshTick'
        ]

        headers = [
            'Cluster',
            'API',
            'Ingress',
            'DNS',
            'Kube',
            'SSH'
        ]

        if cli:
            order = order + [
                'mgmtTick',
                'ciliumTick',
                'hubbleTick',
                'helmTick',
                'virtctlTick'
            ]

            headers = headers + [
                'Mgmt SSH',
                'cilium',
                'hubble',
                'helm',
                'virtctl'
            ]

        ctx.my_output.my_table(
            access,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            cast_none=True,
            table=True
        )

        ctx.my_output.default('Filter: cluster, domain', before_newline=True)
        ctx.my_output.default('View:   list (def), access, cli')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
