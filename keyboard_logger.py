import time
from pynput import keyboard

EVENT_TYPES = ['keyup', 'keypress', 'keydown']

class KeyboardLogger:
    def __init__(self):
        self.setup_listeners()

    def setup_listeners(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def parse_event(self, event_type, key):
        return {
            'timeSeconds': int(time.time()),
            'key': key,
            'type': event_type
        }

    def on_press(self, key):
        try:
            event = self.parse_event('keypress', key.char)
            self.emit(event)
        except AttributeError:
            event = self.parse_event('keypress', key.name)
            self.emit(event)

    def on_release(self, key):
        event = self.parse_event('keyup', key)
        self.emit(event)

    def emit(self, event):
        print(event)

if __name__ == '__main__':
    logger = KeyboardLogger()
