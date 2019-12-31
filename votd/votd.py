import os
import logging
from dotenv import load_dotenv
import slack
import os
import requests
import json


def construct_message(content):
  data = json.loads(content)
  blocks = []

  image_url = f'https:{data["image"]["url"]}'
  reference = f'<{data["verse"]["url"]}|{data["verse"]["human_reference"]}>'

  section_mrkdwn = f'{data["verse"]["text"]}\n{reference}'

  blocks.append({
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*VERSE OF THE DAY*"
			}
		})

  blocks.append({
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": section_mrkdwn
    },
    "accessory": {
				"type": "image",
				"image_url": image_url,
				"alt_text": "VOTD Image"
			}
  })

  return blocks

def send_message(client, blocks):
  client.chat_postMessage(
    channel="youversion-votd-test",
    blocks=blocks
  )

def get_votd():
  # Assuming you keep your tokens in environment variables:
  YOUVERSION_DEVELOPER_TOKEN = os.environ["YOUVERSION_DEVELOPER_TOKEN"]

  headers = {
      "accept": "application/json",
      "x-youversion-developer-token": YOUVERSION_DEVELOPER_TOKEN,
      "accept-language": "en",
  }

  response = requests.get(
      "https://developers.youversionapi.com/1.0/verse_of_the_day/1?version_id=12",
      headers=headers
  )

  log.info(response.content)
  return response.content

if __name__ == "__main__":
  load_dotenv()
  logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
  log = logging.getLogger("votd-logger")
  # ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
  slack_token = os.environ["SLACK_BOT_TOKEN"]
  log.info(slack_token)
  client = slack.WebClient(token=slack_token)
  # rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
  # rtm_client.start()

  votd = get_votd()
  votd_slack_message = construct_message(votd)
  send_message(client, votd_slack_message)
