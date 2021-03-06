import unittest

from lsst.sims.ocs.configuration.instrument import Slew

from lsst.sims.opsim4.model import SlewModel

class SlewModelTest(unittest.TestCase):

    def setUp(self):
        self.model = SlewModel()

    def test_basic_information_after_creation(self):
        self.assertIsInstance(self.model.config_obj, Slew)
        self.assertEqual(len(self.model.params), 16)
