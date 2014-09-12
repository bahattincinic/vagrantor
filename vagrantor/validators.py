import subprocess
import os
from clint.textui.validators import ValidationError, RegexValidator


class BoxNameValidator(object):
    message = 'Enter a valid box name'

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        """
        Validates that the input is a box names.
        """
        query = subprocess.Popen(['vagrant', 'box', 'list'],
                                 stdout=subprocess.PIPE)
        response, error = query.communicate()
        box_list = [r.split(' ')[0] for r in response.split('\n')]
        if value not in box_list:
            raise ValidationError(self.message)
        return value


class VagrantFileValidator(object):
    message = 'VagrantFile already exists'

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        """
        Validates that the input is a valid file.
        """
        if not os.path.isdir(value):
            raise ValidationError('Enter a valid file.')
        file_path = os.path.join(value, 'VagrantFile')
        if os.path.isfile(file_path):
            raise ValidationError(self.message)
        return value


class IpAddressValidator(RegexValidator):
    message = 'Enter a valid ip address.'

    def __init__(self):
        regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
        super(IpAddressValidator, self).__init__(regex=regex)