from controller.Base import Base as BaseController
from view.Domain import Domain as DomainView


class Domain(BaseController):
    def __init__(self, model, parent=None):
        super().__init__(model, DomainView, parent)
