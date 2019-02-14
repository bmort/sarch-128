#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SDP Tango Master Device server.

Run with:

```bash
python3 sdp_master_ds.py 1 -v4
```
"""
import sys
import logging

from tango import Database, DbDevInfo
from tango.server import run

from sip_logging import init_logger
from sdp_master_device import SDPMaster
from .release import __service_id__


LOG = logging.getLogger('sdp.tc.master')


def register_master():
    """Register the SDP Master device."""
    # pylint: disable=protected-access
    tango_db = Database()
    device = "siid_sdp/elt/master"
    device_info = DbDevInfo()
    device_info._class = "SDPMaster"
    device_info.server = "sdp_master_ds/1"
    device_info.name = device
    devices = tango_db.get_device_name(device_info.server, device_info._class)
    if device not in devices:
        LOG.info('Registering device "%s" with device server "%s"',
                 device_info.name, device_info.server)
        tango_db.add_device(device_info)


def main(args=None, **kwargs):
    """Run the Tango SDP Master device server."""
    LOG.info('Starting %s', __service_id__)
    return run([SDPMaster], verbose=True, msg_stream=sys.stdout,
               args=args, **kwargs)


if __name__ == '__main__':
    init_logger(logger_name='', show_log_origin=True)
    init_logger(show_log_origin=True)
    if not any(['-nodb' in arg for arg in sys.argv]):
        register_master()
    main()
