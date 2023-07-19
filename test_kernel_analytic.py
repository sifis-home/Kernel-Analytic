from unittest.mock import patch

import pytest

import catch_topic


@pytest.fixture
def mock_predict_instance():
    with patch("catch_topic.predict_instance") as mock_predict_instance:
        yield mock_predict_instance


"""
def test_on_message(mock_predict_instance):
    ws = MagicMock()
    message = '{"Persistent": {"topic_name": "SIFIS:Privacy_Aware_Device_KERNEL_monitor", "value": {"dictionary": {"key": "value"}}}}'

    with patch('catch_topic.transform_json_to_instance', return_value=[]):
        import catch_topic
        catch_topic.on_message(ws, message)

    mock_predict_instance.assert_called_once()

"""


def test_on_error():
    error = "WebSocket error occurred"

    with patch("builtins.print") as mock_print:
        catch_topic.on_error(None, error)

    mock_print.assert_called_once_with(error)


def test_on_close():
    close_status_code = 1000
    close_msg = "Connection closed"

    with patch("builtins.print") as mock_print:
        catch_topic.on_close(None, close_status_code, close_msg)

    mock_print.assert_called_once_with("### Connection closed ###")


def test_on_open():
    with patch("builtins.print") as mock_print:
        catch_topic.on_open(None)

    mock_print.assert_called_once_with("### Connection established ###")
