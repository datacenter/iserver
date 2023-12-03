import sys
import traceback
import click

from progress.bar import Bar

from lib.helm import output as helm_output
from lib.helm import main as helm

from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("chart")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_helm_chart_command(
        ctx,
        cluster_name,
        name,
        no_confirm,
        devel
        ):
    """Delete helm chart"""

    # iserver delete helm chart

    ctx.developer = devel
    ctx.output = 'default'

    try:
        output_handler = helm_output.HelmOutput(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )

        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name, mandatory=['helm'])
        if settings is None:
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

        charts = helm_handler.get_charts(
            chart_filter=object_filter,
            release_info=True
        )
        if charts is None:
            ctx.my_output.error('No chart matching search criteria')
            return

        output_handler.print_charts(
            charts,
            title=True
        )

        if not no_confirm:
            if not common.get_confirmation():
                return

        bar_handler = Bar('Verify', max=len(charts))
        bar_handler.goto(0)
        for chart in charts:
            if helm_handler.is_chart_release(chart['chart']):
                ctx.my_output.error(
                    'Chart %s has active release' % (chart['chart'])
                )
                bar_handler.finish()
                raise ErrorExit

            bar_handler.next()

        bar_handler.finish()

        bar_handler = Bar('Progress', max=len(charts))
        bar_handler.goto(0)
        failed = []
        for chart in charts:
            if not helm_handler.delete_chart(chart['chart']):
                failed.append(chart)
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Not all helm charts deleted')
            for chart in failed:
                ctx.my_output.default('- %s' % (chart['chart']))
            raise ErrorExit

        ctx.my_output.default('Helm charts deleted')

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
