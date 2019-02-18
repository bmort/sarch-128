# coding=utf-8
"""Test basic interactions with the SDP Master."""
import socket

# import tango
from tango.test_utils import DeviceTestContext

from ..release import __version__
from ..sdp_master_device import SDPMaster


def get_open_port():
    """Select an open port to test with."""
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.bind(("", 0))
    _socket.listen(1)
    port = _socket.getsockname()[1]
    _socket.close()
    return port


def test_tango_master_device():
    """Check that we can successfully connect to the SDP Master device."""
    port = get_open_port()
    # context = DeviceTestContext(SDPMaster, port=port, process=False)
    context = DeviceTestContext(SDPMaster, port=port, process=True)
    with context as proxy:
        # assert proxy.state() == DevState.ON
        assert proxy.version == __version__


# def test_tango_master_attributes():
#     """Test the Tango Master attributes."""
#     master = tango.DeviceProxy(
#         'localhost:10000/siid_sdp/elt/master#dbase=no')
#     assert master.version == __version__
#     assert master.ping()
