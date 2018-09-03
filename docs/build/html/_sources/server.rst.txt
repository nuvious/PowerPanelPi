Running the Server
==================

It is best practice to deploy this server onto a network that is either connected to a separate power panel as the one
being tested on, a network that is on a UPS, or to a mobile hotspot that allows inner device communication.

First a configuration file must be created. Create a directory called .powerpannel in your home directory then create a
config.yml file in that with the following format:

.. code-block:: yaml

   # Delay between a devices last registration (sec) allowed before the device is removed from the active testers
   # list.
   device_expiration: 3
   # The time after which the homepage should refresh to display the active devices.
   refresh_delay: 1
   # The server port.
   port: 5000
   # NOTE: device_expiration should be at least 2x the refresh_delay.

Then run the following command in a python shell.

.. code-block:: python

   from powerpanel.power_panel import PowerPanelServer
   server = PowerPanelServer()
   server.run()

The server can then be reached at \http://[Server IP]:[Server Port]

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
