# coding=utf-8
"""Test basic interactions with the SDP Subrray Device."""
# pylint: disable=redefined-outer-name
import json
import pytest

from tango.test_utils import DeviceTestContext
from tango import DevString, DevFailed

from ..release import __version__
from ..subarray_device import SubarrayDevice
from .utils_sbi_config_generator import generate_sbi


@pytest.fixture(scope="module")
def test_device_context():
    """Create a test device context for the subarray device."""
    device_name = 'siid_sdp/elt/subarray_00'
    context = DeviceTestContext(SubarrayDevice,
                                device_name=device_name,
                                properties=dict(version=__version__))
    context.start()
    yield context
    context.stop()


def test_subarray_has_configure_configure_command(test_device_context):
    """Verify that the configure command exists."""
    device = test_device_context.device
    assert device.name() == 'siid_sdp/elt/subarray_00'

    # Check that the device has a configure command
    assert 'configure' in device.get_command_list()

    # Verify that configure command takes and returns a string.
    command_info = device.get_command_config('configure')
    assert command_info.in_type == DevString
    assert command_info.out_type == DevString


def test_subarray_configure_invalid_sbi(test_device_context):
    """Test behaviour of incorrect SBI configuration.

    Verify that an incorrectly formatted SBI configuration fails to validate
    and returns a JSON response indicating at the SBI has been rejected
    with an appropriate error message.
    """
    device = test_device_context.device

    # Verify that that the string argument must be valid JSON.
    with pytest.raises(DevFailed) as excinfo:
        response = device.configure('')
    assert 'Unable to decode JSON SBI configuration' in repr(excinfo.value)

    # Verify that providing invalid configuration returns a JSON response
    # indicating that the SBI has been rejected with an appropriate
    # error message.
    response = device.configure('{}')
    assert 'id' in json.loads(response)
    assert 'error' in json.loads(response)


def test_subarrary_configure_valid_sbi(test_device_context):
    """Test behaviour with a correctly formatted SBI.

    Verify that a correctly formatted SBI configuration string is validated
    and returns a JSON string as a response confirming that the SBI has
    been accepted by SDP.
    """
    device = test_device_context.device

    # Verify that a correctly formatted SBI
    sbi_config = generate_sbi(index=0)
    response = device.configure(json.dumps(sbi_config))
    response = json.loads(response)
    assert response['id'] == sbi_config['id']
    assert response['message'] == 'accepted'


def test_subarrary_configure_requires_unique_sbi_ids(test_device_context):
    """Verify that each SBI has a unique ID in the system."""
    device = test_device_context.device

    # Configuring the the subarray device with an SBI with a duplicate ID
    # results in an exception with a clear error message.
    sbi_config = generate_sbi(index=0)

    with pytest.raises(DevFailed) as excinfo:
        _ = device.configure(json.dumps(sbi_config))
    assert 'SBIs must have a unique ID.' in repr(excinfo.value)
    assert 'SBI with ID "{}" already exists' \
        .format(sbi_config['id']) in repr(excinfo.value)


def test_subarrary_configure_requires_unique_pb_ids(test_device_context):
    """Verify that each PB in the SBI has a unique ID in the system."""
    device = test_device_context.device

    # Configuring the the subarray device with an SBI with a duplicate ID
    # results in an exception with a clear error message.
    sbi_config = generate_sbi(index=0)

    # Verify that a each PB in the SBI has a unique ID.
    sbi_config['id'] = '{}-a'.format(sbi_config['id'])
    with pytest.raises(DevFailed) as excinfo:
        _ = device.configure(json.dumps(sbi_config))
    assert 'PBs must have a unique ID.' in repr(excinfo.value)
    assert 'PB with ID "{}" already exists in SBI' \
        .format(sbi_config['processing_blocks'][0]['id']) \
        in repr(excinfo.value)
