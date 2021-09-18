from PyQt5.QtCore import QObject
from abc import ABCMeta


class ObserverMeta(QObject, ABCMeta):
    pass
