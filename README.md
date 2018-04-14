# Whatsapp-via-terminal
A simple script that allows user to send text messages(for now) to anyone in their contact list via Whatsapp Web.
The script uses selenium to automate the browser.
The name of the reciever need to be same as in the contact book.
The element is found by searching for an xpath with title attribute of span as the name of person or group.
The rest is trivial. Fill the message bar by sendKey() and elem.click() the send button.
