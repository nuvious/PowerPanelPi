import requests
import yaml
from powerpanel.power_panel import DEFAULT_CONFIG_PATH
import time
from urllib.request import pathname2url


class PowerTester:
    """
    Initializes a Power Tester which registers with a power panel server at a defined frequency.

    Parameters
    ----------
    config : str, default '~/.powerpannel/config.yml'
        Path to configuration yaml.


    >>> # Example Configuration Yaml File
    >>> # Human readable name of the device tester.
    >>> name: Upstairs Bathroom Outlets
    >>> # Url of the server.
    >>> endpoint_url: http://192.168.1.100:5000
    >>> # The frequency at which to register the device.
    >>> reg_frequency: 1
    >>> # NOTE: Must be smaller than the device_expiration time of the server.
    """

    def __init__(self, config=None):
        if config is None:
            config = DEFAULT_CONFIG_PATH
        with open(config, 'r') as f:
            data = yaml.load(f)
            self.url = data['endpoint_url']
            self.name = data['name']
            self.reg_frequency = data['reg_frequency']

    def run(self):
        """
        Runs the tester process, registering at the reg_frequency specified in the configuration.\
        """
        while True:
            try:
                time.sleep(self.reg_frequency)
                requests.get(self.url + "/reg/" + pathname2url(self.name))
            except Exception as e:
                pass


if __name__ == '__main__':
    power_tester = PowerTester()
    power_tester.run()
