[![Build Status](https://travis-ci.com/bmort/sarch-128.svg?branch=master)](https://travis-ci.com/bmort/sarch-128)
[![codecov](https://codecov.io/gh/bmort/sarch-128/branch/master/graph/badge.svg)](https://codecov.io/gh/bmort/sarch-128)

# SKA Solution Intent Interface Demo

This repository has been set up for use with a proof-of-concept demo
analysing how one might update ICDs in the context of a SAFe approach to
Solution Intent. This should be viewed in conjunction with the a page on
SDP Confluence describing this process
(<https://confluence.ska-sdp.org/pages/viewpage.action?pageId=293699597>)
and an proof-of-concept JIRA project
(<https://jira.ska-sdp.org/issues/?filter=28704>).

This work was carried out for the SKA SARCH agile team in sprint #1.5 under
story [SARCH-128](https://jira.skatelescope.org/browse/SARCH-128).

## Quick-start

Deploy services:

```bash
docker stack deploy -c docker-compose.yml siid
```

Clean up:

```bash
docker stack rm siid
docker volume rm siid_tc_tango_mysql
```
