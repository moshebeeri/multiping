from mock import patch, Mock
import pytest
from pytest_mock import mocker
from message.ping import Message
from datetime import datetime
from freezegun import freeze_time

class TestPingMessage:
  def create_message(self):
    return Message()

  @freeze_time("2020-08-14")
  def test_time_m(self):
    ping_msg = self.create_message()
    ping_msg.start()
    ping_msg.end()
    assert ping_msg.time() == 0


    