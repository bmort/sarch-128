# SDP Subarray Node Device(s) & Device Server

Proof of concept minimal prototype SDP Subarray device. This device provides
an observation configuration interface for SDP for the case where
scheduling SDP resources to an with an active SKA subarray configuration is
required, ie. when the scheduling block contains receive and real-time
processing workflows.

## Testing

While all tests are run automatically
[CI system](https://travis-ci.com/bmort/sarch-128/branches) on each push to
the GitHub repository, tests can also be run on development machines as
described below.

Two option are provided for running tests locally on development machines.
All command described below assume that they are being issued from the
top-level repository directory. Although in principle this should not be
required, the commands described below make use of relative paths and have not
yet been generalised to avoid this.

If running on a machine with Docker installed by without a native Tango
installation, one can use a special Docker image, `skasiid/tango_tests`,
to start a container where the tests can be run.

To do this we, make use of a
[`bind mount`](https://docs.docker.com/storage/bind-mounts/) to link the
current working source tree into the container and run the tests in the
container environment which has all necessary dependencies already installed.

This can be achieved using the following command:

```bash
docker run --rm -t -v "$(pwd)":"$(pwd)":rw -w "$(pwd)" \
    --entrypoint=./tools/run_test.sh \
    skasiid/tango_tests tango_subarray [--tests-only]
```

The optional `--tests-only` flag disables the linter checks.

The results of the test will be displayed in the stdout of the terminal
from which the command is run and the container will exit and be removed
once the tests are complete.

For systems with Tango installed natively (see documentation on the Tango
website), test can also be run directly. A requirements file,
`test_requirements.txt`, is provided in the top-level repository directory
which defines the Python packages needed to run the default set of tests used
in the CI.

To use this issue the command:

```bash
pip install -r test_requirements.txt
```

Once dependencies for tests have been installed. The tests can be run
using the provided testing script as follows:

```bash
./tools/run_tests.sh tango_subarray [--tests-only]
```

This test script runs [pytest](https://docs.pytest.org/en/latest/) with a set
of predefined settings and flags. Therefore, it is also possible to run
tests directly using `pytest`. If this is required people refer to the
`tools/run_tests.sh` script for the set of recommended flags and options.
