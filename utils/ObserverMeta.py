from PyQt5.QtCore import QObject
from abc import ABCMeta


class ObserverMeta(type(QObject), type(ABCMeta)):
    pass
