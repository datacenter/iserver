from lib import filter_helper


class K8sAdminJobInfo():
    def __init__(self):
        self.admin_job = None

    def get_admin_job_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')
        return info

    def get_admin_jobs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.admin_job is not None:
                return self.admin_job

        managed_objects = self.get_admin_job_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.admin_job = []
        for managed_object in managed_objects:
            admin_job_info = {}
            admin_job_info['info'] = self.get_admin_job_info(
                managed_object
            )
            admin_job_info['mo'] = managed_object
            self.admin_job.append(
                admin_job_info
            )

        return self.admin_job

    def match_admin_job(self, admin_job_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, admin_job_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, admin_job_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_admin_job',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_admin_jobs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_admin_jobs = self.get_admin_jobs_info(cache_enabled=cache_enabled)
        if all_admin_jobs is None:
            return None

        admin_jobs = []

        for admin_job_info in all_admin_jobs:
            if not self.match_admin_job(admin_job_info['info'], object_filter):
                continue

            if return_mo:
                admin_jobs.append(
                    admin_job_info['mo']
                )
                continue

            admin_jobs.append(
                admin_job_info['info']
            )

        return admin_jobs

    def is_admin_job(self, namespace, name, cache_enabled=True):
        if self.get_admin_job(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_admin_job(self, cache_enabled=True):
        policies = self.get_admin_jobs(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_admin_job(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        admin_jobs = self.get_admin_jobs(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if admin_jobs is None:
            return None

        if len(admin_jobs) == 1:
            return admin_jobs[0]

        return None
