#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Credentials(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.get_credentials()
    
    def get_credentials(self):
        with open(self.file_path, 'r') as cred_file:
            lines = cred_file.read().splitlines()
            for line in lines:
                words = line.split(": ")
                setattr(self, words[0], words[1])

if __name__ == "__main__":
    creds = Credentials('test_credentials')
    print(creds.PASSWORD)
    print(creds.TOKEN)
    print(creds.USERID)
