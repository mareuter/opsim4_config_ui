from opsim4.controller import BaseController
from opsim4.model import ScienceModel
from opsim4.widgets import ScienceWidget

__all__ = ["ScienceController"]

class ScienceController(BaseController):

    def __init__(self, name):
        """Initialize the class.

        Parameters
        ----------
        name : str
            Tab name for the configuration view.
        """
        BaseController.__init__(self, name)
        self.model = ScienceModel()
        self.widget = ScienceWidget(name)

        self.widget.create_tabs(self.model.ad_params)
        self.widget.set_information(self.model.ad_params)

        for i in xrange(self.widget.count()):
            tab = self.widget.widget(i)
            tab.checkProperty.connect(self.check_property)
            tab.getProperty.connect(self.get_property)
            tab.saveConfiguration.connect(self.save_configuration)
            print("A:", tab.signal_mapper.mapping(0))