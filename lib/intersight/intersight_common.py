import traceback
import time
from datetime import datetime

from lib import isctl_helper
from lib import log_helper
from lib import info_helper
from lib import iaccount_helper


class IntersightCommon():
    def __init__(self, iaccount, iobject, get_filter=None, silent=False, verbose=False, debug=False, log_id=None, cache_key=None):
        self.log = log_helper.Log(log_id=log_id)
        self.iaccount = iaccount
        self.isctl = isctl_helper.Isctl(iaccount, log_id=log_id)
        self.iobject = iobject
        self.info_helper = info_helper.InfoHelper(log_id=log_id)
        self.ia_helper = iaccount_helper.IntersightAccount()
        self.cache = None
        self.cache_key = cache_key
        if get_filter is None:
            self.get_filter = ''
        else:
            self.get_filter = '--filter %s' % (get_filter)
        self.get_expand = ''
        self.get_order = ''

        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug

    def prepare_cache(self, force=False):
        if self.cache_key is not None:
            if self.log.is_cache(self.cache_key):
                self.cache = self.log.get_cache(self.cache_key)

        if self.cache is None or force:
            self.cache = self.get_all()

    def get_cache_moid(self, moid):
        self.prepare_cache()
        if self.cache is not None:
            for item in self.cache:
                if item['Moid'] == moid:
                    return item
        return None

    def set_get_expand(self, get_expand):
        self.get_expand = '--expand "%s"' % (get_expand)

    def set_get_filter(self, get_filter):
        self.get_filter = '--filter "%s"' % (get_filter)

    def set_get_order(self, get_order):
        self.get_filter = '--orderby "%s"' % (get_order)

    def get_top(self, top):
        api_debug = True
        if len(self.get_filter) == 0:
            api_debug = False

        command = 'isctl get %s %s %s %s -o json --top %s' % (
            self.iobject,
            self.get_filter,
            self.get_expand,
            self.get_order,
            top
        )

        response = self.isctl.get(command, api_debug=api_debug)
        return response

    def get_all(self, max_errors=3, error_timeout=1):
        all_results = []
        top = 100
        skip = 0
        errors = 0

        api_debug = True
        if len(self.get_filter) == 0:
            api_debug = False

        while True:
            if skip == 0:
                command = 'isctl get %s %s %s %s -o json --top %s' % (
                    self.iobject,
                    self.get_filter,
                    self.get_expand,
                    self.get_order,
                    top
                )
            else:
                command = 'isctl get %s %s %s %s -o json --top %s --skip %s' % (
                    self.iobject,
                    self.get_filter,
                    self.get_expand,
                    self.get_order,
                    top,
                    skip
                )

            response = self.isctl.get(command, api_debug=api_debug)

            if response is None:
                self.log.error('iwe_common.get_all', 'Command failed: %s' % (command))
                if errors >= max_errors:
                    self.log.error('iwe_common.get_all', 'Max command failures: %s' % (command))
                    break

                errors = errors + 1
                time.sleep(error_timeout)
                continue

            all_results = all_results + response
            if len(response) < top:
                break

            skip = skip + top

        self.cache = all_results
        return all_results

    def get(self, moid):
        command = 'isctl get %s %s moid %s -o json' % (
            self.iobject,
            self.get_expand,
            moid
        )
        response = self.isctl.get(command, api_debug=True)
        return response

    def get_filtered(self, get_filter):
        current_filter = self.get_filter
        self.get_filter = get_filter
        response = self.get_all()
        self.get_filter = current_filter
        return response

    def get_moid(self, name):
        command = 'isctl get %s name "%s" -o json' % (self.iobject, name)
        response = self.isctl.get(command, api_debug=True)
        if response is None:
            return None
        if isinstance(response, list):
            return None
        return response['Moid']

    def get_name(self, moid):
        return self.get_object_attribute(moid, 'Name')

    def is_moid(self, moid):
        return bool(self.get(moid) is not None)

    def is_name(self, name):
        return bool(self.get_moid(name) is not None)

    def get_by_name(self, name):
        command = 'isctl get %s name "%s" -o json' % (self.iobject, name)
        response = self.isctl.get(command, api_debug=True)
        if response is None:
            return None
        if isinstance(response, list):
            return None
        return response

    def get_moids_list(self):
        return self.get_objects_attribute('Moid')

    def get_moids_dict(self):
        moids = {}
        attributes_list = self.get_objects_attributes(['Moid', 'Name'])
        if attributes_list is not None:
            for attributes in attributes_list:
                moids[attributes['Moid']] = attributes['Name']
        return moids

    def get_object_attribute(self, moid, attribute_name):
        attribute_value = None
        item = self.get(moid)
        if item is not None:
            if attribute_name in item:
                attribute_value = item[attribute_name]
        return attribute_value

    def get_object_attributes(self, moid, attribute_names):
        attribute_values = None
        item = self.get(moid)
        if item is not None:
            attribute_values = {}
            for attribute_name in attribute_names:
                if attribute_name in item:
                    attribute_values[attribute_name] = item[attribute_name]
        return attribute_values

    def get_objects_attribute(self, attribute_name, unique_only=False, sort=False):
        attributes = []
        items = self.get_all()
        if items is not None:
            for i in items:
                if attribute_name in i:
                    if not unique_only or i[attribute_name] not in attributes:
                        attributes.append(i[attribute_name])

        if sort:
            try:
                attributes = sorted(attributes)
            except BaseException:
                self.log.error('iwe_common.get_objects_attribute', 'Sort failed: %s' % (traceback.format_exc()))
                return None

        return attributes

    def get_objects_attributes(self, attribute_names, order_by=None):
        objects_attributes = None
        items = self.get_all()
        if items is not None:
            objects_attributes = []
            for item in items:
                attributes = {}
                for attribute_name in attribute_names:
                    if attribute_name in item:
                        attributes[attribute_name] = item[attribute_name]

                objects_attributes.append(attributes)

            if order_by is not None:
                try:
                    objects_attributes = sorted(objects_attributes, key=lambda i: i[order_by])
                except BaseException:
                    self.log.error('iwe_common.get_objects_attributes', 'Sort failed: %s' % (traceback.format_exc()))

        return objects_attributes

    def create(self, attributes, get_response=False, json_conversion=True):
        command = 'isctl create %s %s' % (self.iobject, attributes)
        response = self.isctl.create(command, get_response=get_response, json_conversion=json_conversion)
        return response

    def update(self, moid, attributes):
        command = 'isctl update %s moid %s %s' % (self.iobject, moid, attributes)
        response = self.isctl.update(command)
        return response

    def delete(self, moid):
        command = 'isctl delete %s moid %s' % (self.iobject, moid)
        response = self.isctl.delete(command)
        return response

    def convert_time_epoch(self, time_string):
        """Return epoch ms time from string in workflow info object

        Args:
            time_string (string): time string

        Returns:
            int: epoch ms
        """
        try:
            time_string = time_string.replace('T', ' ').replace('Z', '000')
            return int(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000)
        except BaseException:
            return None

    def get_iaccount_json_file(self, filename):
        return self.ia_helper.get_iaccount_json_file(self.iaccount, filename)

    def set_iaccount_json_file(self, filename, content):
        return self.ia_helper.set_iaccount_json_file(self.iaccount, filename, content)
