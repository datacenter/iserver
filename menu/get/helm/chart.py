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


@click.command("chart")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by chart name")
@click.option("--view", "-v", default=['state'], help="[state|values|files]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_helm_chart_command(
        ctx,
        cluster_name,
        name,
        view,
        output,
        devel
        ):
    """Get helm chart"""

    # iserver get helm chart

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|values|files',
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
        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        release_info = False
        files_info = False
        values_info = False

        if 'state' in view:
            release_info = True

        if 'values' in view:
            values_info = True

        if 'files' in view:
            files_info = True

        charts = helm_handler.get_charts(
            chart_filter=object_filter,
            release_info=release_info,
            values_info=values_info,
            files_info=files_info
        )
        if charts is None:
            ctx.my_output.error('Helm chart get failed')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    charts,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(charts)

        output_handler = helm_output.HelmOutput(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )

        if 'state' in view:
            output_handler.print_charts(
                charts,
                title=True
            )

        if 'values' in view:
            output_handler.print_chart_values(
                charts
            )

        if 'files' in view:
            output_handler.print_chart_files(
                charts,
                title=True
            )

        ctx.my_output.default('\nViews: state (def), values, files, all')

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
