import json
import threading
from lib.k8s import output as k8s_output
from menu import validations
from menu import progress


def get(ctx, cluster_name, object_name, output, view, views, cluster_type='ocp', filter_params={}, get_params={}):
    ctx.developer = False
    ctx.output = output

    vvv = []
    defv = None

    input_views = views.split(', ')
    for input_view in input_views:
        if len(input_view.split(' (def)')) == 2:
            defv = input_view.split(' (def)')[0]
            vvv.append(defv)
        else:
            vvv.append(input_view)

    view = validations.validate_view(
        ctx,
        view,
        '|'.join(vvv),
        defv,
        []
    )
    if view is None:
        return False

    k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
    k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type=cluster_type, log_id=ctx.run_id)
    if k8s_handlers is None:
        return False

    object_filter = []

    if 'namespace' in filter_params and filter_params['namespace'] is not None:
        object_filter.append(
            'namespace:%s' % (filter_params['namespace'])
        )

    if 'name' in filter_params and filter_params['name'] is not None:
        object_filter.append(
            'name:%s' % (filter_params['name'])
        )

    for item in filter_params:
        if item not in ['namespace', 'name']:
            if filter_params[item] is not None:
                object_filter.append(
                    '%s:%s' % (item, filter_params[item])
                )

    if output not in ['json', 'mo']:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

    if k8s_handlers.get_api() is None:
        ctx.busy = False
        ctx.my_output.error(
            'Connection to kubernetes cluster failed'
        )
        return False

    if output == 'mo':
        managed_objects = getattr(k8s_handlers, 'get_%ss' % (object_name))(
            object_filter=object_filter,
            return_mo=True
        )
        ctx.my_output.default(
            json.dumps(
                managed_objects,
                indent=4
            )
        )
        return True

    managed_objects = getattr(k8s_handlers, 'get_%ss' % (object_name))(
        object_filter=object_filter,
        **get_params
    )
    
    ctx.busy = False

    if output == 'json':
        ctx.my_output.default(
            json.dumps(
                managed_objects,
                indent=4
            )
        )
        return True

    for item in view:
        getattr(k8s_output_handler, 'print_%ss_%s' % (object_name, item))(managed_objects)

    if len(filter_params) > 0:
        ctx.my_output.default('Filter: %s' % (', '.join(filter_params.keys())), before_newline=True)
    ctx.my_output.default('View:   %s' % (views))
    
    return True
