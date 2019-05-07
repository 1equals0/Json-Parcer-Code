This python code will take two json files as inputs an one message as an output. The two json files provide guesta and company information, a
staff member will select the company and the guest/s with id numbers. The staff memeber is also able to create custom messgae template using defined variables.
The final result will be a messaaage customized by the user.

Program Overview

In the beginging, two json files are imported and individual variables are defined (firstName, lastName, etc.).
An input template asks for the company and guest ID, assuming that they are known and used to define the company and the guest.
Standard message parts are defined in a custom made json ("enjoy your stay",any questions",etc.).
A standard message structure is defined ("time of day greeting","greeting to company","state guest name",etc.)
Various inputs let the user use the standard message template or make a custom one (within bounds), variables mentioned above can be changed ass well.
The message is displayed to the user.


Built With
IDLE (Python 3.7 32-bit)

Authors
Aleksey Garbaly
