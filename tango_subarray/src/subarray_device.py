# -*- coding: utf-8 -*-
"""Tango subarray device class."""
import json
import time

from tango import DebugIt, DevState
from tango.server import Device, attribute, class_property, command, pipe


class SubarrayDevice(Device):
    """SDP Subarray device class."""

    def init_device(self):
        """Initialise the device."""
        Device.init_device(self)
        time.sleep(0.1)
        self.set_state(DevState.STANDBY)

    version = class_property(dtype=str, default_value='test')
