import os
import logging
from dotenv import load_dotenv
import slack


def send_message(client):
  client.chat_postMessage(
    channel="youversion-votd-test",
    text="Hello from your app! :tada:"
  )

if __name__ == "__main__":
  load_dotenv()
  logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
  log = logging.getLogger("votd-logger")
  # ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
  slack_token = os.environ["SLACK_BOT_TOKEN"]
  # log.info(YOUVERSION_TOKEN)
  log.info(slack_token)
  client = slack.WebClient(token=slack_token)
  # rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
  # rtm_client.start()

  send_message(client)