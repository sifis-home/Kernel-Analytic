from unittest.mock import MagicMock, patch

import pytest

import catch_topic


@pytest.fixture
def mock_predict_instance():
    with patch("catch_topic.predict_instance") as mock_predict_instance:
        yield mock_predict_instance


@pytest.fixture
def mock_kernel_classification():
    with patch(
        "catch_topic.kernel_classification.receive_data"
    ) as mock_kernel_classification:
        yield mock_kernel_classification


def test_on_message(mock_kernel_classification):
    ws = MagicMock()
    message = '{"Persistent": {"topic_name": "SIFIS:Privacy_Aware_Device_KERNEL_monitor", "value": {"Dictionary": {"key": "value"}}}}'

    # Call the on_message function with the mock WebSocket and message
    catch_topic.on_message(ws, message)

    # Assert that kernel_classification.receive_data() is called with the correct dictionary
    mock_kernel_classification.assert_called_once_with({"key": "value"})


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
