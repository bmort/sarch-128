# coding: utf-8
"""Unit tests for the SBI configuration schema.

`SIID-3 <https://jira.ska-sdp.org/browse/SIID-3>`.
"""
import json
from os.path import dirname, join

import pytest
import jsonschema

from .utils_sbi_config_generator import generate_sbi


def _sbi_schema():
    """Load the SBI configuration schema."""
    schema_path = join(dirname(__file__), '..', 'schema',
                       'sbi_configuration_0.1.0.json')
    with open(schema_path, 'r') as file:
        schema_str = file.read()
        schema = json.loads(schema_str)
    return schema


def test_sbi_config_passes_validation():
    """Test valid SBI configuration.

    Verify that a correctly formatted example SBI configuration
    schema passes validation with no errors.
    """
    sbi_config = generate_sbi()
    try:
        jsonschema.validate(sbi_config, _sbi_schema())
    except jsonschema.ValidationError:
        pytest.fail("Unexpected validation error!")


def test_sbi_config_fails_validation():
    """Test invalid / incorrect configuration.

    Verify that an incorrectly foramtted SBI configuration
    fails schema validation with an error identifying the issue.
    This includes:
        - Missing required fields.
        - Additional undefined fields.
        - Invalid value type.
    """
    # Expect failure with missing field (scan[0] 'id' field)
    with pytest.raises(jsonschema.ValidationError):
        sbi_config = generate_sbi(num_scans=2)
        del sbi_config['scans'][0]['id']
        jsonschema.validate(sbi_config, _sbi_schema())

    # Expect failure with addition field 'foo'
    with pytest.raises(jsonschema.ValidationError):
        sbi_config = generate_sbi(num_scans=2)
        sbi_config['foo'] = 2
        jsonschema.validate(sbi_config, _sbi_schema())

    # Verify type of value field
    with pytest.raises(jsonschema.ValidationError):
        sbi_config = generate_sbi(num_scans=2)
        sbi_config['processing_blocks'][0]['type'] = 2
        jsonschema.validate(sbi_config, _sbi_schema())
