# -*- coding: utf-8 -*-
"""Proof of concept SDP Tango Master Device."""
# pylint: disable=no-self-use
import json
import time
import logging

from tango import DebugIt, DevState
from tango.server import Device, attribute

from .release import __subsystem__, __version__

LOG = logging.getLogger('sdp.tc.master')


class SDPMaster(Device):
    """SDP Master device class."""

    _start_time = time.time()

    def init_device(self):
        """Device constructor."""
        Device.init_device(self)
        self._set_master_state('init')
        # Add anything here that has to be done before the device is set to
        # its ON state.
        self._set_master_state('on')

    def always_executed_hook(self):
        """Run for each command."""

    def delete_device(self):
        """Device destructor."""

    @attribute(dtype=str)
    def version(self):
        """Return the version of the Master Controller Device."""
        return __version__

    @attribute(dtype=str)
    @DebugIt()
    def health(self):
        """Health check method, returns the up-time of the device."""
        return json.dumps(dict(uptime='{:.3f}s'
                               .format((time.time() - self._start_time))))

    def _set_master_state(self, state):
        """Set the state of the device."""
        if state == 'init':
            self.set_state(DevState.INIT)
        elif state == 'on':
            self.set_state(DevState.ON)
