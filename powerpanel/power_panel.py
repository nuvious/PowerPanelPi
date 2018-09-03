import calendar
import time
import yaml
from os.path import expanduser
from flask import (
    Flask, render_template
)

DEFAULT_CONFIG_PATH = expanduser("~") + "/.powerpannel/config.yml"


class PowerPanelServer:
    """
    Initializes a Power Tester Server with the following endpoints:

    GET / - Home page. Lists all active devices.
    GET /reg/<name> - Registration endpoint for devices.

    Parameters
    ----------
    config : str, default '~/.powerpannel/config.yml'
        Path to configuration yaml.


    >>> # Example Configuration Yaml File
    >>> # Delay between a devices last registration (sec) allowed before the device is removed from the active testers
    >>> # list.
    >>> device_expiration: 3
    >>> # The time after which the homepage should refresh to display the active devices.
    >>> refresh_delay: 1
    >>> # The server port.
    >>> port: 5000
    >>> # NOTE: device_expiration should be at least 2x the refresh_delay.
    """

    def __init__(self, config=None):
        if config is None:
            config = DEFAULT_CONFIG_PATH
        with open(config, "r") as f:
            data = yaml.load(f)
            self.refresh_delay = data['refresh_delay']
            self.device_expiration = data['device_expiration']
            self.port = data['port']

        self.app = Flask(__name__, template_folder='templates', host_matching=False)
        self.devices = {}
        self.cleanup = False
        self.app.add_url_rule('/', methods=['GET'], view_func=self.home)
        self.app.add_url_rule('/reg/<name>', methods=['GET'], view_func=self.reg)

    def run(self):
        """
        Runs the server.
        """
        self.app.run(host="0.0.0.0", port=self.port)

    def reg(self, name):
        """
        Endpoint which registers an active device.

        Parameters
        ----------
        name : str
            Device name passed as a path parameter

        Returns
        -------
        str
            An empty string.
        """
        if not self.cleanup:
            self.devices[name] = calendar.timegm(time.gmtime())
        return ""

    def home(self):
        """
        The homepage of the server.

        Returns
        -------
        str
            The template page built by templates/main.html template.
        """
        return render_template('main.html', active_testers=self.active_testers)

    def active_testers(self):
        """
        Processes the list of devices, removing any device that has not registered itself in the last 3 seconds.

        Returns
        -------
        list
            A list of device names that are currently active.
        """
        self.cleanup = True
        time_now = calendar.timegm(time.gmtime())
        for device in list(self.devices):
            if time_now - self.devices[device] > self.device_expiration:
                del self.devices[device]
        self.cleanup = False
        return list(self.devices)


if __name__ == '__main__':
    power_panel = PowerPanelServer()
    power_panel.run()
