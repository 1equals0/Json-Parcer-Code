Program Overview

This python code will take three json files as inputs an one message as an output. Two provided json files provide guesta and company information and the third json file provides message template data, a
staff member will select the company and the guest/s with id numbers. The staff memeber is also able to create custom messgae template using provided information.
The final result will be a messaaage customized by the user.

Instructions

To run the program (Hotel Greeting Code), the a python shell is needed as well as the following json files: Message2.json, Companies.json, and Guests.json. Once the json files are in the same folder as the program, the python script can be run. The user will be asked for the ID of the company, guest, and the message template (if they choose a generic one). This program assumes that the user will navigate the program using ID's of the company and the guest in question. The steps are described below:
1. User is asked for the company ID
2. User is assked for the guest ID
3. User is asked if they want to use a standard message template
4.a) If standard is chosen, an automated message is printed
4.b) If the user chooses to make a custom message, all relevant information will be provided and the user will be able to input a custom message

Design Overview

1. I tried to keep naming the same as i was given i.e. firstSeconnd  (second word is capatalized, no underscores or dashes)
2. I tried to account for all cases in which someone might enter in some incorrect data when asked (only integers are acceoted where they are required, other inputs will result in another input prompt)
3.I assumed that if other json files were used, they would have the same format
4. I tried to keep variable naming consistent with the subject matter (coi, toi, poi (company/template/person of interest))
5. The program is split into 3 parts:  1rst = Company info    2nd = Guest info    3rd = template info
6. Many of the functions/commands used were found online as I am just learnig Python by  myslef, therefore there may be some cases that would break the program

Language

The langauge used is Python 3.7, I picked it so that i could learn more about it and for the "simplicity". I already have some experience with matlab and C but from what i could see it would be harder to parse json files using those languages. I knew very little Python coming in but I feel as if i obtained a good grasp on it i a short period of time.

Verification

As I wrote the program, I would use print statements and I would comment out sections to find program errors. To validate my code, I tried to make it fail at every section (except for assumptions) whcihch includes all user inputs. I tried puttin non-integer characters in inputs that required integer values. For the final validation test, I tried many different possible inputs and sought variables that produced undesired results.

"Future Work"

With more time, I would try the following things:
1. Incorporate time zones when deciding whether to gret with good morning/evening/etc.
2. When the custom template option is selected, the user could write a message and then input variable wherever they choose (GUI) as they would have to currently type the entire message out, including known variables. 
3. I would try to clean up and simplify the code further
4. I would try to make my program work for all type of json files used by the company

Authors
Aleksey Garbaly
