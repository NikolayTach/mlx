# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.29-filter-categories
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.dataset_service_api import DatasetServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDatasetServiceApi(unittest.TestCase):
    """DatasetServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.dataset_service_api.DatasetServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_approve_datasets_for_publishing(self):
        """Test case for approve_datasets_for_publishing

        """
        pass

    def test_create_dataset(self):
        """Test case for create_dataset

        """
        pass

    def test_delete_dataset(self):
        """Test case for delete_dataset

        """
        pass

    def test_download_dataset_files(self):
        """Test case for download_dataset_files

        Returns the dataset artifacts compressed into a .tgz (.tar.gz) file.  # noqa: E501
        """
        pass

    def test_generate_dataset_code(self):
        """Test case for generate_dataset_code

        """
        pass

    def test_get_dataset(self):
        """Test case for get_dataset

        """
        pass

    def test_get_dataset_template(self):
        """Test case for get_dataset_template

        """
        pass

    def test_list_datasets(self):
        """Test case for list_datasets

        """
        pass

    def test_set_featured_datasets(self):
        """Test case for set_featured_datasets

        """
        pass

    def test_upload_dataset(self):
        """Test case for upload_dataset

        """
        pass

    def test_upload_dataset_file(self):
        """Test case for upload_dataset_file

        """
        pass


if __name__ == '__main__':
    unittest.main()
