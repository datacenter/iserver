import sys
import json
import traceback
import click

from lib.helm import output as helm_output
from lib.helm import main as helm

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("release")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--view", "-v", default=['state'], help="[state|values|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_helm_release_command(
        ctx,
        cluster_name,
        namespace,
        name,
        view,
        output,
        devel
        ):
    """Get helm release"""

    # iserver get helm release

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|values|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name)
        if settings is None:
            raise ErrorExit

        if 'helm' not in settings:
            ctx.my_output.error('Helm not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        helm_handler = helm.Helm(
            settings['helm']['ip'],
            settings['helm']['username'],
            password=settings['helm']['password'],
            key_filename=settings['helm']['key_filename'],
            log_id=ctx.run_id
        )

        object_filter = []

        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        values_info = False
        chart_info = False
        day0_info = False

        if 'state' in view:
            chart_info = True

        if 'day0' in view:
            day0_info = True

        if 'values' in view:
            values_info = True

        releases = helm_handler.get_releases(
            release_filter=object_filter,
            values_info=values_info,
            chart_info=chart_info,
            day0_info=day0_info
        )
        if releases is None:
            ctx.my_output.error('Helm release get failed')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    releases,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(releases)

        output_handler = helm_output.HelmOutput(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )

        if 'state' in view:
            output_handler.print_releases(
                releases,
                title=True
            )

        if 'day0' in view:
            output_handler.print_releases_day0(
                releases,
                title=True
            )

        if 'values' in view:
            output_handler.print_release_values(
                releases,
                title=True
            )

        ctx.my_output.default('\nViews: state (def), values, all')

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
