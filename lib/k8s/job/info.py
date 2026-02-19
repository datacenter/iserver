import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sJobInfo():
    def __init__(self):
        self.job = None

    def get_job_info(self, job_mo):
        if job_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            job_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(job_mo, 'spec')
        info['status'] = self.get(job_mo, 'status')

        info['completed'] = False
        conditions_mo = self.get(job_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                type_mo = self.get(condition_mo, 'type')
                status_mo = self.get(condition_mo, 'status')
                if type_mo == 'Complete':
                    if status_mo == 'True':
                        info['completed'] = True
                        info['completedTick'] = '\u2713'
                        info['__Output']['completedTick'] = 'Green'
                    else:
                        info['completed'] = False
                        info['completedTick'] = '\u2717'
                        info['__Output']['completedTick'] = 'Red'

        return info

    def get_jobs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.job is not None:
                return self.job

        managed_objects = self.get_job_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.job = []
        for managed_object in managed_objects:
            job_info = {}
            job_info['info'] = self.get_job_info(
                managed_object
            )
            job_info['mo'] = managed_object
            self.job.append(
                job_info
            )

        return self.job

    def match_job(self, job_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, job_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, job_info['name']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_job',
                    'Unsupported key: %s' % (key)
                )
        return True

    def get_jobs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_jobs = self.get_jobs_info(cache_enabled=cache_enabled)
        if all_jobs is None:
            return None

        jobs = []

        for job_info in all_jobs:
            if not self.match_job(job_info['info'], object_filter):
                continue

            if return_mo:
                jobs.append(
                    job_info['mo']
                )
                continue

            jobs.append(
                job_info['info']
            )

        self.log.k8s_mo(
            'job.info',
            jobs
        )

        return jobs
    
    def is_job(self, namespace, name, cache_enabled=True):
        if self.get_job(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_job(self, namespace, name, pv_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        jobs = self.get_jobs(
            object_filter=object_filter,
            pv_info=pv_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if jobs is None:
            return None

        if len(jobs) == 1:
            return jobs[0]

        return None

    def delete_namespaced_jobs(self, namespace, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete namespaced jobs', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))

        jobs = self.get_jobs(
            object_filter=['namespace:%s' % (namespace)]
        )
        if jobs is None:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        for job in jobs:
            my_output.default('- %s' % (job['name']))
            success = self.delete_job_mo(job['namespace'], job['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')

                if wait:
                    if my_output is not None:
                        my_output.default('- wait for no job...')

                    if not self.wait_no_job(job['namespace'], job['name']):
                        if my_output is not None:
                            my_output.error('Timed out')
                        return False
                    
        return True

    def wait_no_job(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_job(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_job',
                    'Max time reached'
                )
                return False

            time.sleep(5)
