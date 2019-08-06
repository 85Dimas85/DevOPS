#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# the lib use python logging can get it if the following is set in your
# Ansible config.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_log_eventfilter
short_description: Configure log event filters in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify log feature and eventfilter category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.8"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
       description:
            - FortiOS or FortiGate ip address.
       required: true
    username:
        description:
            - FortiOS or FortiGate username.
        required: true
    password:
        description:
            - FortiOS or FortiGate password.
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: true
    log_eventfilter:
        description:
            - Configure log event filters.
        default: null
        suboptions:
            compliance-check:
                description:
                    - Enable/disable PCI DSS compliance check logging.
                choices:
                    - enable
                    - disable
            endpoint:
                description:
                    - Enable/disable endpoint event logging.
                choices:
                    - enable
                    - disable
            event:
                description:
                    - Enable/disable event logging.
                choices:
                    - enable
                    - disable
            ha:
                description:
                    - Enable/disable ha event logging.
                choices:
                    - enable
                    - disable
            router:
                description:
                    - Enable/disable router event logging.
                choices:
                    - enable
                    - disable
            security-rating:
                description:
                    - Enable/disable Security Rating result logging.
                choices:
                    - enable
                    - disable
            system:
                description:
                    - Enable/disable system event logging.
                choices:
                    - enable
                    - disable
            user:
                description:
                    - Enable/disable user authentication event logging.
                choices:
                    - enable
                    - disable
            vpn:
                description:
                    - Enable/disable VPN event logging.
                choices:
                    - enable
                    - disable
            wan-opt:
                description:
                    - Enable/disable WAN optimization event logging.
                choices:
                    - enable
                    - disable
            wireless-activity:
                description:
                    - Enable/disable wireless event logging.
                choices:
                    - enable
                    - disable
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure log event filters.
    fortios_log_eventfilter:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      log_eventfilter:
        compliance-check: "enable"
        endpoint: "enable"
        event: "enable"
        ha: "enable"
        router: "enable"
        security-rating: "enable"
        system: "enable"
        user: "enable"
        vpn: "enable"
        wan-opt: "enable"
        wireless-activity: "enable"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule

fos = None


def login(data):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_log_eventfilter_data(json):
    option_list = ['compliance-check', 'endpoint', 'event',
                   'ha', 'router', 'security-rating',
                   'system', 'user', 'vpn',
                   'wan-opt', 'wireless-activity']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def log_eventfilter(data, fos):
    vdom = data['vdom']
    log_eventfilter_data = data['log_eventfilter']
    filtered_data = filter_log_eventfilter_data(log_eventfilter_data)
    return fos.set('log',
                   'eventfilter',
                   data=filtered_data,
                   vdom=vdom)


def fortios_log(data, fos):
    login(data)

    methodlist = ['log_eventfilter']
    for method in methodlist:
        if data[method]:
            resp = eval(method)(data, fos)
            break

    fos.logout()
    return not resp['status'] == "success", resp['status'] == "success", resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "log_eventfilter": {
            "required": False, "type": "dict",
            "options": {
                "compliance-check": {"required": False, "type": "str",
                                     "choices": ["enable", "disable"]},
                "endpoint": {"required": False, "type": "str",
                             "choices": ["enable", "disable"]},
                "event": {"required": False, "type": "str",
                          "choices": ["enable", "disable"]},
                "ha": {"required": False, "type": "str",
                       "choices": ["enable", "disable"]},
                "router": {"required": False, "type": "str",
                           "choices": ["enable", "disable"]},
                "security-rating": {"required": False, "type": "str",
                                    "choices": ["enable", "disable"]},
                "system": {"required": False, "type": "str",
                           "choices": ["enable", "disable"]},
                "user": {"required": False, "type": "str",
                         "choices": ["enable", "disable"]},
                "vpn": {"required": False, "type": "str",
                        "choices": ["enable", "disable"]},
                "wan-opt": {"required": False, "type": "str",
                            "choices": ["enable", "disable"]},
                "wireless-activity": {"required": False, "type": "str",
                                      "choices": ["enable", "disable"]}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    global fos
    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_log(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
