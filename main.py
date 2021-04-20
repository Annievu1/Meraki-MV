import requests
import json
from twilio.rest import Client
import time
import config
from webexteamssdk import WebexTeamsAPI
# Live API
print('MV Sense Live API')

mv_live_url = "https://api.meraki.com/api/v1/devices/Q2HV-8G6Q-5QYC/camera/analytics/live?="

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config.meraki_api_key
}
#detects number of people 
mv_live_response = requests.request(
    'GET', url=mv_live_url, headers=headers, data=payload)
mv_live_response_json = json.loads(mv_live_response.text)
num_of_person_detected = mv_live_response_json['zones']['0']['person']
print('number of people detected: ' + str(num_of_person_detected))


print('Snapshot API')

snapshot_url = "https://api.meraki.com/api/v1/devices/"+config.camera_serial+"/camera/generateSnapshot"

payload = '''{}'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config.meraki_api_key
}

snapshot_response = requests.request(
    'POST', url=snapshot_url, headers=headers, data=payload)

snapshot_response_json = json.loads(snapshot_response.text)
snapshot_url = snapshot_response_json['url']
# twilio waits max 15seconds for a response
time.sleep(15)
print('snapshot url: ' + snapshot_url)


# sends snapshot as mms via twilio api
print('Sending Message via Twilio API')
account_sid = config.twilio_account_ssid
auth_token = config.twilio_auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(body='snapshot of current zone',
                                 from_=config.twilio_from_number,
                                 media_url=[snapshot_url],
                                 to=twilio_to_phone_num)
print('message.sid: ' + message.sid)

# sends snapshot to webex teams room via webexapi
webex_space_url = 'https://webexapis.com/v1/messages'

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": 'Bearer' + config.webex_auth_token
}

body = {
    "text": "Click this link to get to meraki snapshot ",
    "roomId": config.webex_room_id,
    "files": snapshot_url
}
api = WebexTeamsAPI(access_token=config.webex_auth_token)
api.messages.create(config.webex_room_id,
                    text="Meraki snapshot: ", files=[snapshot_url])

print("Successfully posted snapshot to Webex")
