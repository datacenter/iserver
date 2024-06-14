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


@click.command("release")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_helm_release_command(
        ctx,
        cluster_name,
        namespace,
        name,
        no_confirm,
        devel
        ):
    """Delete helm release"""

    # iserver delete helm release

    ctx.developer = devel
    ctx.output = 'default'

    try:
        if name is not None:
            if len(name.split('/')) == 2:
                (namespace, name) = name.split('/')

        output_handler = helm_output.HelmOutput(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )

        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name, mandatory=['helm'])
        if settings is None:
            raise ErrorExit

        if settings['helm'] is None:
            ctx.my_output.error('Helm not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        helm_handler = helm.Helm(
            settings['helm']['ip'],
            settings['helm']['username'],
            password=settings['helm']['password'],
            key_filename=settings['helm']['key_filename'],
            log_id=ctx.run_id
        )

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name,
            silent=True
        )
        if ocp_handler is None:
            raise ErrorExit

        object_filter = []

        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        releases = helm_handler.get_releases(
            release_filter=object_filter,
            chart_info=True,
            values_info=True,
            day0_info=True
        )
        if releases is None:
            ctx.my_output.error('No helm releases matching search criteria')
            return

        if len(releases) == 0:
            ctx.my_output.default('No helm releases matching search criteria')
            return

        output_handler.print_releases(
            releases,
            title=True
        )

        output_handler.print_releases_day0(
            releases,
            title=False
        )

        if not no_confirm:
            if not common.get_confirmation():
                return

        for release in releases:
            if release['day0'] is not None:
                for item in release['day0']:
                    if ocp_handler.k8s_handler.is_pvc(item['dv']['metadata']['namespace'], item['dv']['metadata']['name'], cache_enabled=False):
                        success = ocp_handler.k8s_handler.delete_namespaced_pvc(
                            item['dv']['metadata']['namespace'],
                            item['dv']['metadata']['name']
                        )
                        if not success:
                            ctx.my_output.error(
                                'Failed to delete release day0 information: %s/%s' % (
                                    item['dv']['metadata']['namespace'],
                                    item['dv']['metadata']['name']
                                )
                            )
                            raise ErrorExit

                        ctx.my_output.default(
                            'Day0 pvc deleted: %s/%s' % (
                                item['dv']['metadata']['namespace'],
                                item['dv']['metadata']['name']
                            )
                        )

            if not helm_handler.delete_release(release['namespace'], release['name']):
                raise ErrorExit

            ctx.my_output.default(
                'Release deleted: %s/%s' % (
                    release['namespace'],
                    release['name']
                )
            )

        ctx.my_output.default('Helm releases deleted')

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
