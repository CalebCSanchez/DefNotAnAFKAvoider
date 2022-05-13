import unittest
import src.notanafkavoider as nafka
from pynput.keyboard import Key, Controller



# class testNotAnAFKAvoider(unittest.TestCase):
#     def test_esc_is_pressed_returns_new_key(self):
#         keyboard = Controller()
#         keyboard.press('y')
#         keyboard.release('y')
#         keyboard.press('9')
#         keyboard.release('9')
#         quit_key, afk_key = nafka.esc_is_pressed()
        

#         self.assertIsEqual(quit_key, 'esc')
#         self.assertIsEqual(afk_key, 9)