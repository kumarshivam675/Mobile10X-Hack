
## Requirements

 - Requires python2.6+, or python3.0 +
 - Required python packages: python-dateutil,
 - Required python packages for end-to-end encryption: protobuf, pycrypto, python-axolotl-curve25519
 - Required python packages for yowsup-cli: argparse, readline (or pyreadline for windows), pillow (for sending images)

## Installation
 - clone the project from https://github.com/kumarshivam675/Mobile10X-Hack
 - Install using setup.py to pull all python dependencies:

## Setup
 - Move into the Travel Assistance directory
 - To receive registration sms run the following command "yowsup-cli registration --requestcode sms --phone 91XXXXXXXXXX -C 91"
 - You will receive an registration code XXX-XXX
 - To register run the following "yowsup-cli registration -register XXX-XXX --phone 91XXXXXXXXXX -C 91

## Working
 - Move into the Travel Assistance directory
 - Execute "python run.py"
 - Open your whatsapp and create a group with the registered number as a participant.

## About API keys
 - All the API keys are blank for the user to enable it. The application will not run without API keys

## for knowing about the Assistance system ( how to start )
 - To start send a message by "#zense"
 - this will reply back to you with the available Assistance in your application

## About Cab
 - If cab services is to be used the the details have to be entered in the "Book1.xlsx" file in the present format
 - For demo purpose two names have been added
 - The user is searched by his phone number, hence he/she will not get any output if the number is not present in the excel file
 - for your cab

## PNR Status
  - return you the pnr status of your ticket.
  - send a message with "#pnr pnr_number"
  - this will return you the status of each passenger with his/her birth number.

## Live Train Status
  - return you the current status of the train, with the delay till the last station.
  - for using this send a message as "#status train_number yyyymmdd"

## Nearby hospitals
  - this list out the five hospitals near your locality for this it will also ask about the location.
  - send a message with "#hospitals" this will further ask you about the current location and use location of whatsapp then it will return you the desired result.

## Passport
  - send a message with "#passpost" to get your passport status.

## Complaint
  - Using this citizens of a city can post complaints with the image of the problem such as piled up garbage lying on the road, electric poles not functioning and numerous other. Once the image is sent the user will be asked to send his location which will then be recorded and can be viewed on Google maps.
  - send a message with "#complaint" this will ask you for the image upload the image with the caption and on the server side we can visualize this on the google maps.
