# pylint: disable=no-name-in-module
from pyVmomi import vim
# pylint: disable=no-name-in-module
from pyVmomi import vmodl


class VcCommon():
    def __init__(self):
        pass

    def get_filter_spec(self, container_view, obj_type, path):
        traverse_spec = vmodl.query.PropertyCollector.TraversalSpec()
        traverse_spec.name = 'traverse'
        traverse_spec.path = 'view'
        traverse_spec.skip = False
        traverse_spec.type = vim.view.ContainerView

        obj_spec = vmodl.query.PropertyCollector.ObjectSpec()
        obj_spec.obj = container_view
        obj_spec.skip = True
        obj_spec.selectSet.append(traverse_spec)

        prop_spec = vmodl.query.PropertyCollector.PropertySpec()
        prop_spec.type = obj_type
        prop_spec.pathSet = path

        return vmodl.query.PropertyCollector.FilterSpec(propSet=[prop_spec], objectSet=[obj_spec])

    def get_filemanager_handler(self):
        if self.is_vc_connected():
            return self.vc_service_instance.RetrieveServiceContent().fileManager
        return None

    def wait_for_tasks(self, tasks, exception_on_task_failure=True):
        """
        Given the service instance and tasks, it returns after all the
        tasks are complete
        """
        if self.vc_service_instance is None:
            return False

        property_collector = self.vc_service_instance.content.propertyCollector
        task_list = [str(task) for task in tasks]
        # Create filter
        obj_specs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task) for task in tasks]
        property_spec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task, pathSet=[], all=True)
        filter_spec = vmodl.query.PropertyCollector.FilterSpec()
        filter_spec.objectSet = obj_specs
        filter_spec.propSet = [property_spec]
        pcfilter = property_collector.CreateFilter(filter_spec, True)
        try:
            version, state = None, None
            # Loop looking for updates till the state moves to a completed state.
            while task_list:
                update = property_collector.WaitForUpdates(version)
                for filter_set in update.filterSet:
                    for obj_set in filter_set.objectSet:
                        task = obj_set.obj
                        for change in obj_set.changeSet:
                            if change.name == 'info':
                                state = change.val.state
                            elif change.name == 'info.state':
                                state = change.val
                            else:
                                continue

                            if not str(task) in task_list:
                                continue

                            if state == vim.TaskInfo.State.success:
                                # Remove task from taskList
                                task_list.remove(str(task))
                            elif state == vim.TaskInfo.State.error:
                                if exception_on_task_failure:
                                    raise task.info.error
                                task_list.remove(str(task))

                # Move to next version
                version = update.version
        finally:
            if pcfilter:
                pcfilter.Destroy()
