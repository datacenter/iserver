import sys
import traceback
import click
from lib.k8s import output as k8s_output
from menu import user_inputs
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("pvc")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--mode", type=click.Choice(['f', 'b', ''], case_sensitive=False), default='', help="Fileystem or block mode")
@click.option("--sc", "storage_class", default='', callback=validations.empty_string_to_none, help="Storage class")
@click.option("--size", "pvc_size", default='', callback=validations.empty_string_to_none, help="Requested size")
@click.option("--limit", "pvc_limit", default='', callback=validations.empty_string_to_none, help="Requested limit")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def create_k8s_pvc_command(
        ctx,
        cluster_name,
        namespace,
        name,
        mode,
        storage_class,
        pvc_size,
        pvc_limit,
        no_confirm
        ):
    """Create k8s pvc"""

    # iserver create k8s pvc

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        sc_names = None
        if storage_class is None:
            sc_names = k8s_handlers.get_storage_class_names(cache_enabled=False)
            if sc_names is None:
                ctx.my_output.error('failed to get storage class')
                raise ErrorExit
            
            if len(sc_names) == 0:
                ctx.my_output.error('no storage class defined')
                raise ErrorExit
            
        if namespace is None:
            namespace = user_inputs.get_value(ctx, 'PVC Namespace')

        if name is None:
            name = user_inputs.get_value(ctx, 'PVC Name')

        if len(mode) == 0:
            mode = user_inputs.get_selection(ctx, 'Volume mode (filesystem, block)', ['f', 'b'])

        if storage_class is None:
            if len(sc_names) == 1:
                storage_class = sc_names[0]
            else:
                storage_class = k8s_handlers.get_default_storage_class_name(cache_enabled=True)
                if storage_class is None:
                    storage_class = user_inputs.get_selection(ctx, 'Storage class', sc_names)

        if pvc_size is None:
            pvc_size = user_inputs.get_value(ctx, 'Requests size (e.g. 1Gi)')

        if pvc_limit is None:
            pvc_limit = user_inputs.get_value(ctx, 'Limits size (e.g. 1Gi)')

        if mode == 'f':
            mode = 'Filesystem'

        if mode == 'b':
            mode = 'Block'

        success = k8s_handlers.create_pvc(
            namespace, 
            name, 
            mode,
            storage_class, 
            pvc_size, 
            pvc_limit,
            confirmation=not no_confirm, 
            my_output=ctx.my_output, 
            wait=True
        )
        if not success:
            raise ErrorExit
        
        pvc = k8s_handlers.get_pvc(namespace, name, cache_enabled=False)
        k8s_output_handler.print_pvcs([pvc])
        
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
