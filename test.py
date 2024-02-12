from keyboard_logger import KeyboardLogger

def on_keypress(event):
    print('Key pressed:', event['key'])

def on_keyup(event):
    print('Key released:', event['key'])

def on_keydown(event):
    print('Key down:', event['key'])

def on_error(err):
    print('Error:', err)

if __name__ == '__main__':
    keyboard_logger = KeyboardLogger()

    keyboard_logger.on('keypress', on_keypress)
    keyboard_logger.on('keyup', on_keyup)
    keyboard_logger.on('keydown', on_keydown)
    keyboard_logger.on('error', on_error)
