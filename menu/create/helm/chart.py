import sys
import traceback
import click

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
@click.option("--file", "chart_values_filename", default='', callback=validations.empty_string_to_none, help="Chart values filename")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_helm_chart_command(
        ctx,
        cluster_name,
        chart_values_filename,
        devel
        ):
    """Create helm chart"""

    # iserver create helm chart

    ctx.developer = devel
    ctx.output = 'default'

    try:
        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name, mandatory=['helm'])
        if settings is None:
            raise ErrorExit

        chart_info = validations.validate_helm_chart(ctx, chart_values_filename)
        if chart_info is None:
            raise ErrorExit

        ctx.my_output.default('Chart directory : %s' % (chart_info['directory']))
        ctx.my_output.default('Chart name      : %s' % (chart_info['chart']))
        ctx.my_output.default('Version         : %s' % (chart_info['version']))
        ctx.my_output.default('AppVersion      : %s' % (chart_info['appVersion']))
        ctx.my_output.default('Values          : %s\n' % (chart_values_filename))

        helm_handler = helm.Helm(
            settings['helm']['ip'],
            settings['helm']['username'],
            password=settings['helm']['password'],
            key_filename=settings['helm']['key_filename'],
            log_id=ctx.run_id
        )

        if helm_handler.is_chart(chart_info['chart']):
            if helm_handler.is_chart_release(chart_info['chart']):
                ctx.my_output.default('Chart already defined and release exists')
                if not common.get_confirmation():
                    raise ErrorExit
            else:
                ctx.my_output.default('Chart already defined')
                if not common.get_confirmation():
                    raise ErrorExit

            if not helm_handler.delete_chart(chart_info['chart']):
                ctx.my_output.error('Chart delete failed')
                raise ErrorExit

            ctx.my_output.default('Chart deleted')

        ctx.my_output.default(
            'Chart %s will be uploaded from %s to helm repository at %s@%s' % (
                chart_info['chart'],
                chart_info['directory'],
                settings['helm']['username'],
                settings['helm']['ip']
            )
        )

        success = helm_handler.create_chart(
            chart_info['chart'],
            chart_info['directory'],
            chart_info['values'],
            verbose=True
        )
        if not success:
            ctx.my_output.error('Chart upload failed')
            raise ErrorExit

        ctx.my_output.default('Upload completed', before_newline=True)

        output_handler = helm_output.HelmOutput(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )

        charts = helm_handler.get_charts(
            chart_filter=['name:%s' % (chart_info['chart'])],
            release_info=True,
            values_info=True,
            files_info=True,
            cache_enabled=False
        )

        output_handler.print_charts(
            charts,
            title=True
        )

        output_handler.print_chart_files(
            charts,
            title=True
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
