
## Use Case 
This allows you to configure a zone for your MV camera to monitor, take a manual snapshot, detect the number of people in the defined zone and send the snapshot and information on number of people detected to your phone and webex room. 

# Meraki 
1. Enable API access and retrieve API key https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API#:~:text=For%20access%20to%20the%20API,to%20generate%20an%20API%20key.
2. Configure zone you want MV to monitor. https://developer.cisco.com/meraki/mv-sense/#!zones Note, the ability to configure zones is a feature only avaliable for second generation MV cameras (camera models ending in the number 2). 

## Twilio
1. Register for an account on twilio to register desired phone number to receive text messages.

## Webex Teams 
1. Create a webex teams account at https://cart.webex.com/sign-up and go to https://developer.webex.com/docs/api/getting-started to retrieve your access token. Note, this token has a 12 hour lifetime and will require a new token after expiration. 

## Installation 
1. Create a virtual environment 
2. Run the command 'pip install -r requirements.txt' to install all dependencies 
