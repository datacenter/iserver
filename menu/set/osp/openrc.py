import os
import sys
import traceback
import click

from lib.osp import settings

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("openrc")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="K8s cluster name")
@click.option("--file", "openrc_filename", default='', callback=validations.empty_string_to_none, help="Kubeconfig filename")
@click.option("--cert", "cert_filename", default='', callback=validations.empty_string_to_none, help="Certificate filename")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_osp_openrc(
        ctx,
        cluster_name,
        openrc_filename,
        cert_filename,
        devel
        ):
    """Set openstack cluster openrc"""

    # iserver set osp openrc

    ctx.developer = devel

    try:
        if cluster_name is None:
            ctx.my_output.error('Define openstack cluster name')
            raise ErrorExit

        if openrc_filename is None:
            ctx.my_output.error('Define openrc filename')
            raise ErrorExit

        if not os.path.isfile(openrc_filename):
            ctx.my_output.error('Openrc file not found')
            raise ErrorExit

        if cert_filename is not None:
            if not os.path.isfile(cert_filename):
                ctx.my_output.error('Certificate file not found')
                raise ErrorExit

        settings_handler = settings.OspSettings(log_id=ctx.run_id)

        cluster = settings_handler.get_openstack_cluster(
            cluster_name
        )

        if cluster is not None:
            if cluster['source'] != 'user':
                ctx.my_output.error(
                    'Cluster %s cannot be modified' % (cluster_name)
                )
                raise ErrorExit

        success = settings_handler.set_openstack_cluster(
            cluster_name,
            openrc_filename,
            cluster_type='standard',
            cert_filename=cert_filename
        )
        if not success:
            ctx.my_output.error('Failed to set openstack cluster')
            raise ErrorExit

        ctx.my_output.default('Openstack cluster set: %s' % (cluster_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
