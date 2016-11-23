try:
    from unittest import mock
except ImportError:
    import mock
import unittest
import sys

from PyQt5 import QtWidgets

from lsst.sims.opsim4.controller import EnvironmentController

class EnvironmentControllerTest(unittest.TestCase):

    app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def setupClass(cls):
        patcher1 = mock.patch("opsim4.widgets.EnvironmentWidget", spec=True)
        cls.addCleanup(patcher1.stop)
        cls.mock_widget = patcher1.start()

    def setUp(self):
        self.controller = EnvironmentController("environment")

    def test_basic_information_after_creation(self):
        self.assertIsNotNone(self.controller.model)
