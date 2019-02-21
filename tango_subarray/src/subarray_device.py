# -*- coding: utf-8 -*-
"""Tango subarray device class."""
import json
import time
from os.path import join, dirname
import inspect

import jsonschema

from tango import DevState
from tango.server import Device, command, device_property
from tango import Except

from .release import __subsystem__, __version__


class SubarrayDevice(Device):
    """SDP Subarray device class."""

    _start_time = time.time()

    def init_device(self):
        """Initialise the device."""
        Device.init_device(self)
        self._sbi_list = dict()
        self._pb_list = dict()
        self.set_state(DevState.STANDBY)

    version = device_property(dtype=str, default_value=__version__)

    def always_executed_hook(self):
        """Run for each command."""

    def delete_device(self):
        """Device destructor."""

    @command(dtype_in=str, dtype_out=str)
    def configure(self, sbi_config_str):
        """Issue an SBI configuration request."""
        # Load the SBI configuration as a dictionary
        try:
            sbi_config = json.loads(sbi_config_str)
        except json.JSONDecodeError as error:
            Except.throw_exception(
                'Unable to decode JSON SBI configuration',
                '{} (position {}, line {}, column {})'.
                format(error.msg, error.pos, error.lineno, error.colno),
                'File "{}", line {}'.
                format(__file__, inspect.currentframe().f_back.f_lineno))

        # Validate the provided SBI configuration using JSON schema
        try:
            self._validate_sbi_schema(sbi_config)
        except jsonschema.ValidationError as error:
            return self._invalid_sbi_config_response(sbi_config)

        # Check that the SBI (and PBs) are not already registered.
        if sbi_config['id'] in self._sbi_list:
            Except.throw_exception(
                'SBIs must have a unique ID.',
                'SBI with ID "{}" already exists.'.format(sbi_config['id']),
                'File "{}", line {}'.
                format(__file__, inspect.currentframe().f_back.f_lineno))
        for pb in sbi_config['processing_blocks']:
            if pb['id'] in self._pb_list:
                Except.throw_exception(
                    'PBs must have a unique ID.',
                    'PB with ID "{}" already exists in SBI {}.'.
                    format(pb['id'], self._pb_list[pb['id']]),
                    'File "{}", line {}'.
                    format(__file__, inspect.currentframe().f_back.f_lineno))

        # Check that the PB workflows are registered.
        # ***

        # Check that there are enough resources
        # ***

        # Check that there are enough PB devices
        # ***

        # Save the data structure in the Configuration database.
        # *** make sure to associate it with the subarray
        self._sbi_list[sbi_config['id']] = sbi_config
        for pb in sbi_config['processing_blocks']:
            self._pb_list[pb['id']] = sbi_config['id']

        # Allocate PB devices
        # ***

        return self._accepted_response(sbi_config['id'])

    @staticmethod
    def _validate_sbi_schema(sbi_config):
        """Validate the SBI configuration schema."""
        schema_path = join(dirname(__file__), 'schema',
                           'sbi_configuration_0.1.0.json')
        with open(schema_path, 'r') as file:
            schema_str = file.read()
            schema = json.loads(schema_str)
        jsonschema.validate(sbi_config, schema)

    @staticmethod
    def _accepted_response(sbi_id: str):
        """Response when an SBI is accepted."""
        _accepted = dict(id=sbi_id, message="accepted")
        return json.dumps(_accepted)

    @staticmethod
    def _invalid_sbi_config_response(sbi_config: str):
        """Response when an SBI configuration is invalid."""
        return json.dumps(dict(
            id=sbi_config['id'] if 'id' in sbi_config else 'Unknown',
            error='Unable to configure SBI, Invalid configuration.'
        ))
