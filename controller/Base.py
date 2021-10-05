from PyQt5.QtWidgets import QDialog

from abc import ABCMeta


class Base(metaclass=ABCMeta):
    def __init__(self, model, view_class, parent=None, **kwargs):
        self._model = model
        self._view = view_class(model, parent, **kwargs)

        self._view.change_signal.connect(self.change_model)

    def change_model(self):
        try:
            for prop in self._model.__dict__.keys():
                _, view_prop = prop.split("__")
                if hasattr(self._view, f'ui_{view_prop}'):
                    val = self._view.__getattribute__(f'ui_{view_prop}')
                    val = val.strip().upper() if isinstance(val, str) else val
                    self._model.__setattr__(prop, val)
            self._view.setResult(QDialog.Accepted)
            self._view.accept()
        except ValueError as v_e:
            self._view.show_error(v_e)
        except BaseException as b_e:
            self._view.show_error(b_e)

    @property
    def model(self):
        return self._model

    def exec_view(self):
        return self._view.exec()
