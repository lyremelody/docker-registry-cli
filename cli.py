#!/usr/bin/env python
#
# Copyright 2017 lyremelody
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import cmd

from docker_registry_contact import DockerRegistryContact

CMD_ENV = {
    'host': '127.0.0.1',
    'port': 5000
}


class DockerRegistryCmd(cmd.Cmd):
    @staticmethod
    def _sp1str(host, port):
        return '[Registry CMD {0}:{1}] '.format(host, port)

    def _refresh_prompt(self):
        global CMD_ENV
        self.prompt = DockerRegistryCmd._sp1str(CMD_ENV['host'], CMD_ENV['port'])

    def preloop(self):
        self._docker_registry_contact = DockerRegistryContact()
        self._docker_registry_contact.connect(CMD_ENV['host'], CMD_ENV['port'])

        self._refresh_prompt()

    def do_connect(self, line):
        host = raw_input('Registry Host: ')
        port = raw_input('Registry Port: ')

        global CMD_ENV
        CMD_ENV['host'] = host
        CMD_ENV['port'] = int(port)

        self._docker_registry_contact.connect(CMD_ENV['host'], CMD_ENV['port'])
        self._refresh_prompt()

    def do_lsall(self, line):
        print 'todo'

    def do_lsrepos(self, line):
        repo_names = self._docker_registry_contact.list_repositories()
        if repo_names is None:
            print self._docker_registry_contact.get_last_error()
        else:
            for repo_name in repo_names:
                print repo_name

    def do_lstags(self, line):
        repository_name = raw_input('Repository Name: ')

        tags = self._docker_registry_contact.list_image_tags(repository_name)
        if tags is None:
            print self._docker_registry_contact.get_last_error()
        else:
            for tag in tags:
                print tag

    def do_exit(self, line):
        return True


if __name__ == '__main__':
    DockerRegistryCmd().cmdloop()
