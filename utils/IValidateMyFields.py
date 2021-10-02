from model.exceptions.InvalidFieldValidator import InvalidFieldValidator


class IValidateMyFields:
    def validate(self):
        if not self.fields_validators:
            return True
        for field, validator in self.fields_validators.items():
            if not validator(self.__getattribute__(field)):
                raise InvalidFieldValidator('Не все поля заполнены верно')

        return True

    def accept_changes(self):
        if not hasattr(self, 'change_signal'):
            return False
        if not hasattr(self, 'show_error') or not callable(self.show_error):
            return False
        try:
            self.validate()
            self.change_signal.emit()
        except InvalidFieldValidator as inv_field:
            self.show_error(str(inv_field))

    @staticmethod
    def empty_string_validator(string):
        return len(string.strip()) > 0

    @staticmethod
    def empty_array_validator(array):
        return len(array) > 0
