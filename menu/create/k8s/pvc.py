import os
import sys
import traceback
import threading
import click

from lib.k8s import output as k8s_output
from lib.linux import main as linux

from menu import progress
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("pvc")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--namespace", default='default', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--type", "file_type", type=click.Choice(['file', 'day0'], case_sensitive=False), default='file', help="PVC source file type")
@click.option("--size", default='', callback=validations.empty_string_to_none, help="Target PVC size")
@click.option("--file", "source_filename", default='', callback=validations.empty_string_to_none, help="Source filename")
@click.option("--rfile", "remote_filename", default='', callback=validations.empty_string_to_none, help="Remote source filename")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_k8s_pvc_command(
        ctx,
        cluster_name,
        namespace,
        name,
        file_type,
        size,
        source_filename,
        remote_filename,
        devel
        ):
    """Create k8s pvc"""

    # iserver create k8s pvc

    ctx.developer = devel
    ctx.output = 'default'

    try:
        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name, silent=True)
        if settings is None:
            raise ErrorExit

        if 'tools' not in settings:
            ctx.my_output.error('Tools not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        if 'virtctl' not in settings:
            ctx.my_output.error('Virtctl not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        if namespace is None:
            ctx.my_output.error('Define target pvc namespace')
            raise ErrorExit

        if name is None:
            ctx.my_output.error('Define target pvc name')
            raise ErrorExit

        if source_filename is None and remote_filename is None:
            ctx.my_output.error('Define local or remote filename')
            raise ErrorExit

        if source_filename is not None and remote_filename is not None:
            ctx.my_output.error('Define local or remote filename')
            raise ErrorExit

        if size is None:
            ctx.my_output.error('Define target pvc size e.g. 1Gi')
            raise ErrorExit

        if source_filename is not None:
            if not os.path.isfile(source_filename):
                ctx.my_output.error('Local filename not found: %s' % (source_filename))
                raise ErrorExit

        if remote_filename is not None:
            virtctl_handler = linux.Linux(
                settings['virtctl']['ip'],
                settings['virtctl']['username'],
                password=settings['virtctl']['password'],
                key_filename=settings['virtctl']['key_filename'],
                log_id=ctx.run_id
            )
            if not virtctl_handler.ssh_handler.is_file(remote_filename):
                ctx.my_output.error(
                    'Remote filename not found at %s@%s:%s' % (
                        settings['virtctl']['username'],
                        settings['virtctl']['ip'],
                        remote_filename
                    )
                )
                raise ErrorExit

        if k8s_handlers.is_data_volume(namespace, name):
            ctx.my_output.error(
                'Data volume already exists: %s/%s' % (namespace, name)
            )
            raise ErrorExit

        if k8s_handlers.is_pvc(namespace, name, cache_enabled=False):
            if k8s_handlers.is_pvc_used(namespace, name):
                ctx.my_output.default('PVC %s/%s already exists and is used. It cannot be overwritten.' % (namespace, name))
                raise ErrorExit

            ctx.my_output.default('PVC %s/%s already exists. Remove it?' % (namespace, name))
            if not common.get_confirmation():
                return

            if not k8s_handlers.delete_namespaced_pvc(namespace, name):
                ctx.my_output.error('PVC delete failed')
                raise ErrorExit

            ctx.my_output.default('PVC deleted')

        if source_filename is not None:
            ctx.my_output.default(
                'Creating PVC %s/%s type %s from local file %s' % (
                    namespace,
                    name,
                    file_type,
                    source_filename
                )
            )
        else:
            ctx.my_output.default(
                'Creating PVC %s/%s type %s from remote file %s@%s:%s' % (
                    namespace,
                    name,
                    file_type,
                    settings['virtctl']['username'],
                    settings['virtctl']['ip'],
                    remote_filename
                )
            )

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        success = k8s_handlers.create_pvc_via_data_volume_upload(
            namespace,
            name,
            settings['tools'],
            settings['virtctl'],
            file_type=file_type,
            source_filename=source_filename,
            remote_filename=remote_filename,
            size=size,
            must_bound=False
        )
        if not success:
            ctx.busy = False
            ctx.my_output.error('PVC creation failed')
            raise ErrorExit

        ctx.busy = False
        ctx.my_output.default('PVC created')

        pvcs = k8s_handlers.get_pvcs(
            object_filter=['namespace:%s' % (namespace), 'name:%s' % (name)],
            usage_info=False,
            pv_info=True,
            cache_enabled=False
        )
        k8s_output_handler.print_pvcs(
            pvcs,
            title=True
        )
        k8s_output_handler.print_pvcs_metadata(
            pvcs,
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
