import keyboard
import time
import random
def generate_random_int():
  return random.randint(6, 12)
def generate_random_string(length):
  letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  result = ""
  for i in range(length): result += random.choice(letters)
  return result

count = int(input("Enter the number of times you want to search: "))
time.sleep(5)
for i in range(count):
  keyboard.write(generate_random_string(generate_random_int()))
  keyboard.press_and_release("enter")
  time.sleep(7)