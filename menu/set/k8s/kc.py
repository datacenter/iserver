import os
import sys
import traceback
import click

from lib.k8s import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("kc")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="K8s cluster name")
@click.option("--file", "kubeconfig_filename", default='', help="Kubeconfig filename")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_k8s_kc(
        ctx,
        cluster_name,
        kubeconfig_filename,
        devel
        ):
    """Set k8s kc settings"""

    # iserver set k8s kc

    ctx.developer = devel

    try:
        if len(cluster_name) == 0:
            ctx.my_output.error('Define k8s cluster name')
            raise ErrorExit

        if len(kubeconfig_filename) == 0:
            ctx.my_output.error('Define kubeconfig filename')
            raise ErrorExit

        if not os.path.isfile(kubeconfig_filename):
            ctx.my_output.error('Kubeconfig file not found')
            raise ErrorExit

        settings_handler = settings.K8sSettings(log_id=ctx.run_id)

        cluster = settings_handler.get_k8s_cluster(
            cluster_name
        )

        if cluster is not None:
            if cluster['source'] != 'user':
                ctx.my_output.error(
                    'Cluster %s cannot be modified' % (cluster_name)
                )
                raise ErrorExit

        success = settings_handler.set_k8s_cluster(
            cluster_name,
            kubeconfig_filename,
            cluster_type='standard'
        )
        if not success:
            ctx.my_output.error('Failed to set cluster')
            raise ErrorExit

        ctx.my_output.default('Kubernetes cluster set: %s' % (cluster_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
