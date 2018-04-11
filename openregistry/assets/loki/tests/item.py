# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from openprocurement.api.tests.base import snitch

from openregistry.assets.loki.tests.base import (
    AssetContentWebTest
)
from openprocurement.api.tests.blanks.json_data import test_loki_item_data
from openregistry.assets.loki.tests.blanks.item import (
    create_item_resource,
    patch_item,
    create_loki_with_item_schemas,
    bad_item_schemas_code,
    delete_item_schema
)

class AssetItemResourceTest(AssetContentWebTest):
    initial_item_data = deepcopy(test_loki_item_data)
    test_create_item_resource = snitch(create_item_resource)
    test_patch_item_resource = snitch(patch_item)
    test_create_loki_with_item_schemas = snitch(create_loki_with_item_schemas)
    test_bad_item_schemas_code = snitch(bad_item_schemas_code)
    test_delete_item_schema = snitch(delete_item_schema)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AssetItemResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
