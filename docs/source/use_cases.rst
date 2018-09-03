Use Case Examples
=================

Business Use Case Example
-------------------------
You're a property investor that routinely buys up business fronts and rental properties in a historic district that
often has power panels with out of date or inaccurate labels. You have in your inventory several raspbery pi's
preconfigured with generic names. When you go to a site to update/verify the power panel labels, you move from room to
room plugging in the raspberry pi's into the outlets and keeping track of the generic label to room mapping in a
spreadsheet program. After you've plugged in all the devices, you go to the breaker panel and begin cycling breakers,
noting which rooms are tied to which breakers in the excel sheet in a new column. After you've cycled all the breakers
you simply remove the column with the generic names of the test devices and sort by the breaker number and you have a
printable mapping of breaker numbers to rooms.

Home Use Case Example
---------------------
You have just purchased a house or a condo and after living there for a while you decide to change out the old outlets
for newer ones but find that the breaker panel is mostly unlabeled and the few that are there are inaccurate (like I did
when I bought my first condo). You have a lot of raspberry pi's handy so you flash them all with rasbian images and
deploy the testing utility to them, giving them names of the different rooms in the house. You then plug the respective
raspberry pi's into the outlets in the respective rooms. Finally, you launch the server and navigate to it using your
phone and go to the breaker panel. One by one you flip the breaker off, watch for a device to disappear off the list,
then flip it back on to see it come back and label the panel.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
