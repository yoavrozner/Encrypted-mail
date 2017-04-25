"""
Name: Yoav Rozner
Version: 1.0.1
Description: Build a chat between two computers that combines high-level encryption.
"""
import pygame
import scapy
import datetime
from cryptography.fernet import Fernet


def sender():
    """
    Takes a string and send it to the
    wanted client with the wanted encryption.
    Returns: nothing
    """
    pass


def getter():
    """
    Receives a message decodes it by the used encryption.
    Returns: the decoded message.
    """
    pass


def database():
    """
    Will create and update a database for each message.
    Returns: nothing
    """
    pass


def chat_build():
    """
    By using pygame, this function will
    show the messages of both clients.
    """
    pass


class EncodeMessage():
    """
    The class will have encode functions for each wanted encoding.
    *The functions will be built while the progress writing*.
    """
    def __init__(self, msg, encrypt):
        self.msg = msg
        self.encrypt = encrypt
        self.new_msg = []

    def caesar_cipher(self, num):
        self.new_msg = []
        for letter in self.msg:
            if 97 < ord(letter) < 122:
                if ord(letter) + num > 122:
                    letter_help = ord(letter) + num - 122
                    self.new_msg.append(ord('a') + letter_help)
                else:
                    self.new_msg.append(ord(letter) + num)
            elif 65 < ord(letter) < 90:
                if ord(letter) + num > 90:
                    letter_help = ord(letter) + num - 90
                    self.new_msg.append(ord('A') + letter_help)
                else:
                    self.new_msg.append(ord(letter) + num)
        return self.new_msg

    def symmetric_encryption(self, *args):
        self.new_msg = []

        if args:
            key = args

        else:
            key = Fernet.generate_key()

        f = Fernet(key)
        self.new_msg.append(f.encrypt(self.msg))
        return self.new_msg

class DecodeMessage():
    """
    The class will have decode functions for each of the encodes.
    *The functions will be built while the progress writing*.
    """
    def __init__(self, msg, encrypt):
        self.msg = msg
        self.encrypt = encrypt
        self.new_msg = ""

    def caesar_cipher(self, num):
        new_msg = []
        new_string = []
        for letter in self.msg:
            if 97 < letter < 122:
                if letter - num < 97:
                    letter_help = 97 - letter - num
                    new_msg.append(ord('z') - letter_help)
                else:
                    new_msg.append(letter - num)
            elif 65 < letter < 90:
                if letter - num < 65:
                    letter_help = 65 - letter - num
                    new_msg.append(ord('Z') - letter_help)
                else:
                    new_msg.append(letter - num)
        for letter in new_msg:
            new_string.append(chr(letter))

        self.new_msg = "".join(new_string)
        return self.new_msg

    def symmetric_encryption(self, key):
        f = Fernet(key)
        self.new_msg = f.decrypt(self.msg[0])
        return self.new_msg


def main():
    """
    Add Documentation here
    """
    pass


if __name__ == '__main__':
    main()