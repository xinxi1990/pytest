#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def test_1th():
    logger.info('====test_1th=====')

@pytest.mark.flaky(reruns=5)
def test_2th():
    logger.info('====test_2th=====')
    assert 1 == 2