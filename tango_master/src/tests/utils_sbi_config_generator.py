# coding: utf-8
"""Script to generate a test SBI configuration."""
import datetime
from random import randint, choice


def generate_sbi(index: int = None, num_scans: int = 2):
    """Generate a SBI config JSON string."""
    date = datetime.datetime.utcnow().strftime('%Y%m%d')
    if index is None:
        index = randint(0, 999)
    sbi_id = 'SBI-{}-siid-test-{:03d}'.format(date, index)
    sb_id = 'SBI-{}-siid-test-{:03d}'.format(date, index)
    pb_id = 'PB-{}-siid-test-{:03d}'.format(date, index)
    scans = [dict(id='SCAN-{}-{:04d}.{:02d}'
                  .format(date, randint(0, 9999), i))
             for i in range(num_scans)]
    sbi = dict(
        id=sbi_id,
        version='0.1.0',
        observation_config=dict(),
        scheduling_block=dict(
            id=sb_id,
            project='ska-demo',
            programme_block='sarch-128'
        ),
        scans=scans,
        processing_blocks=[
            dict(
                id=pb_id,
                version='1.0.0',
                type=choice(['OFFLINE', 'REAL_TIME']),
                priority=1,
                dependencies=[],
                workflow=dict(
                    id='test_workflow',
                    version='1.0.0',
                    parameters=dict(
                        stage1=dict(duration=30),
                        stage2=dict(duration=30)
                    )
                )
            )
        ]
    )
    return sbi
