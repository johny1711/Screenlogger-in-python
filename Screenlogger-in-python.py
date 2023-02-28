import time

import mouse
import pyscreenshot as ImageGrab

count = 1  # contador para numerar as imagens capturadas

while True:
    if mouse.is_pressed(button='left'):
        screenshot = ImageGrab.grab()
        screenshot.save(f"screenshot_{count}.png")
        count += 1
        # screenshot.show() <== Essa função faz aparecer na tela o print tirado
        # screenshot.hide()
    time.sleep(0.1)
