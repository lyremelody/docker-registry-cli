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
import json
import urllib2


class DockerRegistryAPIDisc(object):
    """
    https://docs.docker.com/registry/spec/api/
    """

    @staticmethod
    def api_disc_version_check():
        return {
            'http_method': 'GET',
            'uri': '/v2/'
        }

    @staticmethod
    def api_disc_list_repositories():
        """
        :HTTP Response:
                200 OK
                Content-Type: application/json

                {
                  "repositories": [
                    <name>,
                    ...
                  ]
                }
        """
        return {
            'http_method': 'GET',
            'uri': '/v2/_catalog'
        }

    @staticmethod
    def api_disc_list_image_tags():
        """
        :HTTP Response:
            200 OK
            Content-Type: application/json
            
            {
                "name": <name>,
                "tags": [
                    <tag>,
                    ...
                ]
            }
        """
        return {
            'http_method': 'GET',
            'uri': '/v2/{name}/tags/list',
        }


class DockerRegistryContact(object):
    def __init__(self):
        self._host = None
        self._port = None
        self._url_prefix = None

    def connect(self, host, port):
        self._host = host
        self._port = port
        self._url_prefix = 'http://{0}:{1}'.format(self._host, self._port)

    def version_check(self):
        pass

    def list_repositories(self):
        """
            
        :return: [<repo_name>, ...]
        """
        url = self._url_prefix + DockerRegistryAPIDisc.api_disc_list_repositories()['uri']
        req = urllib2.Request(url=url)
        f = urllib2.urlopen(req)
        result = f.read().encode('utf-8')
        result = result.replace('\n', '').replace(' ', '')
        result = dict(json.loads(result))
        return result['repositories']

    def list_image_tags(self, image_name):
        """
        :param image_name: 
        
        :return: [<tag>, ...]
        """
        url = self._url_prefix + DockerRegistryAPIDisc.api_disc_list_image_tags()['uri']
        url = url.format(name=image_name)
        req = urllib2.Request(url=url)
        f = urllib2.urlopen(req)
        result = f.read().encode('utf-8')
        result = result.replace('\n', '').replace(' ', '')
        result = dict(json.loads(result))
        return result['tags']
