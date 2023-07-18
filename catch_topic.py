import websocket
import json
import kernel_classification

def on_message(ws, message):
    print("Received:")

    json_message = json.loads(message)

    if "Persistent" in json_message:
        json_message = json_message["Persistent"]

        print('JSON-MESSAGE')
        print(json_message['topic_name'])

        # Handle messages
        topic_name = json_message['topic_name']
        if topic_name == 'SIFIS:Privacy_Aware_Device_KERNEL_monitor':
            if "value" in json_message:
                topic_value = json_message["value"]
                if "Dictionary" in topic_value:
                    dictionary = topic_value['Dictionary']
                    kernel_classification.receive_data(dictionary)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")

def on_open(ws):
    print("### Connection established ###")

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:3000/ws",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
