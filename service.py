import json
import logging
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    response = True
    slack_channel = os.environ["slackChannel"]
    hook_url = f"https://{os.environ['hookUrl']}"
    logger.info(f"Event: {event}")
    message = json.loads(event["Records"][0]["Sns"]["Message"])
    logger.info(f"Message: {message}")

    alarm_name = message["AlarmName"]
    new_state = message["NewStateValue"]
    reason = message["NewStateReason"]
    msg = f"{alarm_name} state is now {new_state}: {reason}."
    slack_message = {"channel": slack_channel, "text": msg}
    encoded_message = json.dumps(slack_message).encode("utf-8")
    req = Request(hook_url, encoded_message)
    try:
        http_response = urlopen(req)
        logger.info(
            "Message posted to %s with response %s",
            slack_message["channel"],
            http_response.read(),
        )
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
        response = False
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
        response = False
    return response
