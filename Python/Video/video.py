#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os

class VideosManager(object):
    """docstring for VideosManager"""
    def __init__(self):
        super(VideosManager, self).__init__()
        self.db_file = "video.sqlite3"
        self.table_name = "video"
        self.video_folder = u'D:\Downloads'
        self.movie_extensions = ['.avi', '.mkv']
        self.default_language = "GER"

        self.connection = sqlite3.connect(self.db_file, isolation_level='DEFERRED')
        self.cursor = self.connection.cursor()

    def connect(self):
        conn = sqlite3.connect(self.db_file, isolation_level='DEFERRED')
        return conn.cursor()
    
    def aktualisieren(self):
        self.cursor.execute('''DROP TABLE IF EXISTS {0}_tmp'''.format(self.table_name))
        self.cursor.execute('''ALTER TABLE {0} RENAME TO {0}_tmp'''.format(self.table_name))
        self.createDatabase()
        self.connection.close()


    def createDatabase(self):
        self.cursor.execute('''CREATE TABLE {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT,
        Year INTEGER,
        Filepath TEXT,
        Release TEXT,
        Language TEXT,
        Cover BLOB
        );'''.format(self.table_name))

        os.chdir(self.video_folder)
        for root, dirs, files in os.walk('.'):
            if len(files) is not 0:
                # print root
                # print dirs
                # print files
                # ordner=root.split('/')[1]
                # nummer=root.split('/')[2].split('. ')[0]
                # stueck=root.split('/')[2].split('. ')[1]
                #name=files[0].split('.jpg')[0]
                for file in files:
                    name, extension = os.path.splitext(file)
                    if (extension in self.movie_extensions):
                        title, year = self.extractInformationsFromFilename(name)
                        print title
                        release = self.getRelease(root)
                        language = self.getLanguage(root)
                        blob = self.getCoverBlob(root)
                        # print title, year, file, release, language
                        self.cursor.execute('''INSERT INTO {0} VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(self.table_name), 
                            (None, title, year, file, release, language, None))
                        self.connection.commit()
        
        #try:
        # self.database.execute('''DROP TABLE {0}_tmp'''.format(self.table_name))
        # conn.commit()
        # conn.close()

    @staticmethod
    def extractInformationsFromFilename(name):
        # name, extension = os.path.splitext(filename)
        if not (name[-1] is ')' and name[-6] is '('):
            return None
        year_string = name[-5:-1]
        if not year_string.isdigit():
            return None
        year = int(year_string)
        title = name[0:-7]
        return title, year

    def getRelease(self, folder):
        filepath = os.path.join(self.video_folder, folder, 'Infos.nfo')
        with open(filepath, 'r') as f:
            first_line = f.readline()
            return first_line

    def getLanguage(self, folder):
        try:
            start_index = folder.index('[')
            end_index = folder.index(']')
        except ValueError:
            return self.default_language
        language = folder[start_index+1:end_index]
        return language

    def getCoverBlob(self, folder):
        path = os.path.join(self.video_folder, folder, 'folder.jpg')
        with open(path, 'rb') as file:
            fileblob = file.read()
            return sqlite3.Binary(fileblob)


    def auslesen(self):
        self.database.execute('''SELECT * from {0}'''.format(self.table_name))
        result = curs.fetchone()
        while result is not None:
            print result
            result = curs.fetchone()
        conn.close()

def main():
    manager = VideosManager()
    manager.aktualisieren()


if __name__ == "__main__":
    main()