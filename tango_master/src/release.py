# -*- coding: utf-8 -*-
"""SDP Tango Master Release info."""
__subsystem__ = 'TangoControl'
__service_name__ = 'SDPMaster'
__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))
__service_id__ = ':'.join(map(str, (__subsystem__,
                                    __service_name__,
                                    __version__)))
__all__ = [
    '__subsystem__',
    '__service_name__',
    '__version__',
    '__service_id__',
]
