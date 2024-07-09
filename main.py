# import keyboard
# import mouse
# import time

# isClicking = False

# def set_clikcer():
#     global isClicking
#     if isClicking:
#         isClicking = False
#         print("Кликер отключен")
#     else:
#         isClicking = True
#         print("Кликер включен")
    
# keyboard.add_hotkey("Alt + Z", set_clikcer)

# while True:
#     if self.isClicking:
#         mouse.double_click(button = "left")
#         time.sleep(0.01)

from GUI import GUI

if __name__ == "__main__":
    GUI()

