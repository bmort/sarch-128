# -*- coding: utf-8 -*-
"""SKA SDP Tango Processing Block Device."""
# pylint: disable=no-self-use,attribute-defined-outside-init
import json
import time

from tango import DevState
from tango.server import Device, attribute

from release import LOG, __version__ as tango_pb_device_version


class ProcessingBlockDevice(Device):
    """Tango Processing Block Device."""

    _start_time = time.time()

    def init_device(self):
        """Device constructor."""
        start_time = time.time()
        Device.init_device(self)
        self._pb_id = ''
        LOG.debug('Init PB device %s, time taken %.6f s (total: %.2f s)',
                  self.get_name(), (time.time() - start_time),
                  (time.time() - self._start_time))
        self.set_state(DevState.STANDBY)

    @attribute(dtype=str)
    def version(self):
        """Return the version of the Processing Block Device."""
        return tango_pb_device_version

    @attribute(dtype=str)
    def pb_id(self):
        """Return the Processing block ID for this device."""
        return self._pb_id
