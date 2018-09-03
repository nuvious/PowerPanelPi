Deploying Test Device
=====================

Create a raspbian sd card and add a wpa_supplicant.conf for your wifi network and an empty ssh file to initialize ssh so
ssh is enabled on the first boot. Boot up the raspberry pi, find it on your network and ssh into it.

Install Python 3.

.. code-block:: bash

   sudo apt install python3 python3-pip

Clone the Power Panel project to a directory of your choosing. Then install the package using the following command:

.. code-block:: bash

   pip3 install -e [git repository directory]

Create a configuration file.

.. code-block:: bash

   mkdir ~/.powerpanel
   cat >~/.powerpanel/config.yml <<EOL
   # Human readable name of the device tester.
   name: [Name of Tester Device; ex Kitchen Outlet Tester]
   # Url of the server.
   endpoint_url: \http://[IP of Server]:[Server Port]
   # The frequency at which to register the device.
   reg_frequency: 1
   # NOTE: Must be smaller than the device_expiration time of the server.
   EOL

Next create a script to run the tester

.. code-block:: bash

   cat >~/.powerpanel/tester.py <<EOL
   from powerpanel.power_tester import PowerTester
   power_tester = PowerTester()
   power_tester.run()
   EOL

Add the following line to /etc/rc.local just before exit 0:

.. code-block:: bash

   su - pi -c 'python3 ~/.powerpanel/tester.py'

Finally reboot the raspberry pi. After it boots you should see the testers name as specified in the yaml in the list of
devices. You can then deploy to multiple devices and plug them around the house or business you want to map the outlets
to and begin opening breakers and monitoring the list for devices which have disappeared off the server page, then
shutting the breaker to verify the device you expect returns.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
