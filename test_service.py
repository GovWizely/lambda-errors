import json
from urllib.error import HTTPError, URLError

import pytest
import vcr

from service import handler


@pytest.fixture
def event(monkeypatch):
    monkeypatch.setenv("slackChannel", "external-monitors")
    monkeypatch.setenv("hookUrl", "hooks.slack.com/services/abc")
    with open("event.json") as f:
        event = json.load(f)
    return event


@vcr.use_cassette()
def test_handler(event):
    """Reads from the `test_handler` cassette and processes the request
    """
    assert handler(event, None) is True


def test_handler_handles_http_error(mocker, event):
    """Ensures any HTTP client errors get handled"""
    mocker.patch(
        "service.urlopen",
        side_effect=HTTPError("http://example.com", 500, "Internal Error", {}, None),
    )
    assert handler(event, None) is False


def test_handler_handles_url_error(mocker, event):
    """Ensures any URL errors get handled"""
    mocker.patch("service.urlopen", side_effect=URLError("unknown host"))
    assert handler(event, None) is False
