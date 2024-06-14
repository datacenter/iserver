import sys
import traceback
import click

from lib.helm import output as helm_output
from lib.helm import main as helm

from lib import file_helper

from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("release")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--chart", "chart_name", default='', callback=validations.empty_string_to_none, help="Chart name")
@click.option("--file", "chart_values_filename", default='', callback=validations.empty_string_to_none, help="Chart values filename")
@click.option("--namespace", default='default', help="Release namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Release name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_helm_release_command(
        ctx,
        cluster_name,
        chart_name,
        chart_values_filename,
        namespace,
        name,
        devel
        ):
    """Create helm release"""

    # iserver create helm release

    ctx.developer = devel
    ctx.output = 'default'

    try:
        if chart_name is None:
            ctx.my_output.error('Define chart name')
            raise ErrorExit

        if name is None:
            ctx.my_output.error('Define release name')
            raise ErrorExit

        if len(name.split('/')) == 2:
            (namespace, name) = name.split('/')

        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name, mandatory=['helm', 'tools', 'virtctl'])
        if settings is None:
            raise ErrorExit

        output_handler = helm_output.HelmOutput(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name,
            silent=True
        )
        if ocp_handler is None:
            raise ErrorExit

        helm_handler = helm.Helm(
            settings['helm']['ip'],
            settings['helm']['username'],
            password=settings['helm']['password'],
            key_filename=settings['helm']['key_filename'],
            log_id=ctx.run_id
        )

        if not helm_handler.is_chart(chart_name):
            ctx.my_output.error(
                'Chart does not exist: %s' % (chart_name)
            )
            raise ErrorExit

        if helm_handler.is_release(namespace, name):
            ctx.my_output.error(
                'Release exists: %s/%s' % (namespace, name)
            )
            raise ErrorExit

        if chart_values_filename is None:
            ctx.my_output.default('Using default chart value')
            values = helm_handler.get_chart_file(chart_name, 'values.yaml', convert_yaml=True)
            if values is None:
                ctx.my_output.error('Failed to read release values')
                raise ErrorExit

        if chart_values_filename is not None:
            ctx.my_output.default('Using custom chart value')
            values = file_helper.get_file_yaml(chart_values_filename)
            if values is None:
                ctx.my_output.error('Failed to read release values')
                raise ErrorExit

        day0 = helm_handler.get_release_day0(chart_name, namespace, name, values)
        if day0 is None:
            ctx.my_output.error('Failed to get release day0 information')
            raise ErrorExit

        if len(day0) > 0:
            for item in day0:
                create_dv = True
                pvc_namespace = item['dv']['metadata']['namespace']
                pvc_name = item['dv']['metadata']['name']
                if ocp_handler.k8s_handler.is_pvc(pvc_namespace, pvc_name, cache_enabled=True):
                    if ocp_handler.k8s_handler.is_pvc_used(namespace, name):
                        ctx.my_output.default('Day0 PVC %s/%s already exists and is used. It cannot be overwritten.' % (pvc_namespace, pvc_name))
                        raise ErrorExit

                    ctx.my_output.default('Day0 PVC %s/%s already exists. Reuse it?' % (pvc_namespace, pvc_name))
                    if not common.get_confirmation():
                        if not ocp_handler.k8s_handler.delete_namespaced_pvc(pvc_namespace, pvc_name):
                            ctx.my_output.error('PVC delete failed')
                            raise ErrorExit
                        ctx.my_output.default('PVC deleted')

                if create_dv:
                    success = ocp_handler.create_ocp_vm_day0(
                        item['filename'],
                        item['content'],
                        'config.iso',
                        item['dv']
                    )
                    if not success:
                        ctx.my_output.error('Release day0 preparation not supported')
                        raise ErrorExit

        success, reason = helm_handler.create_release(chart_name, namespace, name, values)
        if not success:
            ctx.my_output.error('Release create failed: %s' % (reason))

            ctx.my_output.default('Delete release?')
            if common.get_confirmation():
                releases = helm_handler.get_releases(
                    release_filter=['namespace:%s' % (namespace), 'name:%s' % (name)],
                    chart_info=True,
                    values_info=True,
                    day0_info=True
                )
                if releases is None:
                    ctx.my_output.error('Failed to get release information')
                    raise ErrorExit

                if len(releases) == 0:
                    ctx.my_output.error('Release not found')
                    raise ErrorExit

                if len(releases) > 1:
                    ctx.my_output.error('Multiple releases found')
                    raise ErrorExit

                if helm_handler.delete_release(namespace, name):
                    ctx.my_output.default('Release deleted')
                else:
                    ctx.my_output.error('Release delete failed')
                    raise ErrorExit

                for release in releases:
                    if release['day0'] is not None:
                        for item in release['day0']:
                            if ocp_handler.k8s_handler.is_pvc(item['dv']['metadata']['namespace'], item['dv']['metadata']['name'], cache_enabled=False):
                                success = ocp_handler.k8s_handler.delete_namespaced_pvc(
                                    item['dv']['metadata']['namespace'],
                                    item['dv']['metadata']['name']
                                )
                                if not success:
                                    ctx.my_output.error('Failed to delete release day0 pvc')
                                    raise ErrorExit

                                ctx.my_output.default(
                                    'Release day0 deleted: %s/%s' % (
                                        item['dv']['metadata']['namespace'],
                                        item['dv']['metadata']['name']
                                    )
                                )

            raise ErrorExit

        ctx.my_output.default('Helm release created')

        release = helm_handler.get_release(
            namespace,
            name,
            day0_info=True,
            cache_enabled=False
        )
        output_handler.print_releases(
            [release],
            title=False
        )

        if len(release['day0']) > 0:
            output_handler.print_releases_day0(
                [release],
                title=False
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
