from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.RuleWindow import UIRuleWindow

from model.Fact import Fact as FactModel
from controller.Fact import Fact as FactnController

from utils.Mixins import *


class Rule(IShowError):
    pass
