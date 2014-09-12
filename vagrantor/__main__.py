# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from clint.textui import colored, puts, prompt
from jinja2 import Template
from clint.textui.validators import RegexValidator, IntegerValidator
from vagrantor.validators import (BoxNameValidator, IpAddressValidator,
                                  VagrantFileValidator)


class VagrantFileGenerator(object):
    # template default content
    content = {'box_name': '', 'forwarded_ports': [], 'private_ip': '',
               'public_network': '', 'memory': '', 'cpu': ''}
    # VagrantFile path
    path = ''

    def __init__(self):
        puts(colored.green('Vagrant configuration file generator', bold=True))
        self.exists('vagrant')

    @staticmethod
    def exists(cmd):
        devnull = open(os.devnull, 'w')
        params = {'stdout': devnull, 'stderr': devnull, }
        query = 'which %s' % cmd
        code = subprocess.call(query.split(), **params)
        if code != 0:
            puts(colored.red('%(command)s not installed' % {'command': cmd}))
            sys.exit(1)

    def get_path(self):
        """
        VagrantFile Path
        """
        self.path = prompt.query('VagrantFile Path: ',
                                 validators=[VagrantFileValidator()])

    def forwarded_port(self, another_ports=None):
        """
        Forwarded ports allow you to access a port on your host
        machine and have all data forwarded to a port on the guest
        machine, over either TCP or UDP.

        https://docs.vagrantup.com/v2/networking/forwarded_ports.html
        """
        ports = another_ports if another_ports else []
        if prompt.yn('Create a forwarded port ?', default='y'):
            guest = prompt.query("Guest Port: ",
                                 validators=[IntegerValidator()])
            host = prompt.query("Host Port: ",
                                validators=[IntegerValidator()])
            data = {'quest': guest, 'host': host}
            ports.append(data)
            self.forwarded_port(another_ports=ports)
        self.content['forwarded_ports'] = ports

    def get_box_name(self):
        """
        This configures what box the machine will be brought up against.
        The value here should be the name of an installed box or a
        shorthand name of a box in Vagrant Cloud.

        https://docs.vagrantup.com/v2/vagrantfile/machine_settings.html
        """
        self.content['box_name'] = prompt.query(
            "Your Box name: ",
            validators=[RegexValidator(r'.+'), BoxNameValidator()])

    def get_private_ip(self):
        """
        You can also specify a static IP address for the machine.
        This lets you access the Vagrant managed machine using a static
         known IP. The Vagrantfile for a static IP looks like this:

        https://docs.vagrantup.com/v2/networking/private_network.html
        """
        if prompt.yn('Create a private network ?', default='y'):
            self.content['private_ip'] = prompt.query(
                'Private Ip Address: ',
                validators=[IpAddressValidator()])

    def get_public_network(self):
        """
        Public networks are less private than private networks,
        and the exact meaning actually varies from provider to provider,
        hence the ambiguous definition. The idea is that while private
        networks should never allow the general public access to your
        machine, public networks can.

        https://docs.vagrantup.com/v2/networking/public_network.html
        """
        if prompt.yn('Create a Public network(Static ip) ?', default='y'):
            self.content['public_network'] = prompt.query(
                'Public Ip Address: ',
                validators=[IpAddressValidator()])

    def get_memory(self):
        """
        Customize default Memory

        https://docs.vagrantup.com/v2/virtualbox/configuration.html
        """
        if prompt.yn('Customize your box memory', default='y'):
            self.content['memory'] = prompt.query(
                "New Memory: ", validators=[IntegerValidator()])

    def get_cpu(self):
        """
        Customize Default CPU

        https://docs.vagrantup.com/v2/virtualbox/configuration.html
        """
        if prompt.yn('Customize your box cpu', default='y'):
            self.content['cpu'] = prompt.query(
                "New Cpu: ", validators=[IntegerValidator()])

    def save_file(self):
        """
        Save VagrantFile
        """
        base_dir = os.path.dirname(__file__)
        config_file = os.path.join(base_dir,
                                   'templates/configuration_template.html')
        # config template
        with open(config_file, 'r') as f:
            config_data = f.read()
        template = Template(config_data)
        content = template.render(**self.content)
        file_path = os.path.join(self.path, 'VagrantFile')
        with open(file_path, 'w') as f:
            f.write(content)
        puts(colored.green('%s created' % file_path))


def main():
    vagrant = VagrantFileGenerator()
    vagrant.get_path()
    vagrant.get_box_name()
    vagrant.forwarded_port()
    vagrant.get_private_ip()
    vagrant.get_public_network()
    vagrant.get_cpu()
    vagrant.get_memory()
    vagrant.save_file()

if __name__ == '__main__':
    main()