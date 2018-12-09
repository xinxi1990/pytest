

import logging
logging.basicConfig(level=logging.DEBUG)

class TestNew():


    def add(self,a,b):
        return a + b

    def test_add(self):
        log = logging.getLogger('test_1')
        log.debug('test_add')
        assert self.add(2,3) == 6

    def test_add1(self):
        log = logging.getLogger('test_1')
        log.debug('test_add')
        assert self.add(2,3) == 5