from PyQt4 import QtGui

import lsst.pex.config.listField

from utilities import load_class

class ConfigurationTab(QtGui.QWidget):
    def __init__(self, tab_name, config_obj, parent=None):
        super(QtGui.QWidget, self).__init__(parent)

        self.tab_name = tab_name
        self.config_obj = config_obj
        self.config_cls = load_class(self.config_obj)

        self.layout = QtGui.QGridLayout()
        self.create_form()
        self.setLayout(self.layout)

    @property
    def title(self):
        values = self.tab_name.split('_')
        for i, value in enumerate(values):
            if value == "lsst":
                values[i] = value.upper()
            else:
                values[i] = value.capitalize()
        return " ".join(values)

    def create_form(self):
        for i, (k, v) in enumerate(self.config_cls.__dict__["_fields"].items()):
            tcls = None
            name_label = QtGui.QLabel(k)

            if v.dtype == float:
                tcls = "Float"
            if v.dtype == bool:
                tcls = "Bool"
            if v.dtype == str:
                tcls = "Str"
            if isinstance(v, lsst.pex.config.listField.ListField):
                tcls = "List"
            if tcls is None:
                print("Cannot handle {}".format(k))

            if tcls is not None:
                self.layout.addWidget(name_label, i, 0)
                pwidget = self.make_property_widget(tcls, v)
                name_label.setBuddy(pwidget)
                self.layout.addWidget(pwidget, i, 1)
                unit_label = QtGui.QLabel("")
                self.layout.addWidget(unit_label, i, 2)

    def make_property_widget(self, tcls, v):
        widget = QtGui.QWidget()
        if tcls == "Str":
            widget = QtGui.QLineEdit(self.config_obj.toDict()[v.name])
        if tcls == "Float":
            widget = QtGui.QLineEdit(str(self.config_obj.toDict()[v.name]))
            widget.setValidator(QtGui.QDoubleValidator())

        widget.setToolTip(v.doc)
        return widget
