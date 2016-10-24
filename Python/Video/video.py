#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os
import codecs


class VideosManager(object):
    """docstring for VideosManager"""
    def __init__(self):
        super(VideosManager, self).__init__()
        self.db_file = "video.sqlite3"
        self.table_name = "video"
        self.video_folder = u'D:\Downloads'
        self.movie_extensions = ['.avi', '.mkv']
        self.default_language = u"GER"

        self.connection = sqlite3.connect(self.db_file, isolation_level='DEFERRED')
        self.cursor = self.connection.cursor()

    def connect(self):
        conn = sqlite3.connect(self.db_file, isolation_level='DEFERRED')
        return conn.cursor()
    
    def aktualisieren(self):
        self.cursor.execute('''DROP TABLE IF EXISTS {0}_tmp'''.format(self.table_name))
        self.cursor.execute('''ALTER TABLE {0} RENAME TO {0}_tmp'''.format(self.table_name))
        self.create_database()
        self.connection.close()

    def create_database(self):
        self.cursor.execute('''CREATE TABLE {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT,
        Year INTEGER,
        Filepath TEXT,
        ReleaseName TEXT,
        Language TEXT,
        Cover BLOB
        );'''.format(self.table_name))

    def find_new_db_entries(self):

        os.chdir(self.video_folder)
        for root_folder in os.listdir(u'.'):
            if not os.path.isdir(root_folder):
                continue
            for afile in os.listdir(root_folder):
                name, extension = os.path.splitext(afile)
                if extension in self.movie_extensions:
                    infos = self.extract_infos_from_filename(name)
                    if infos is None:
                        continue
                    title, year = infos
                    print title
                    release = self.get_release(root_folder)
                    language = self.get_language(root_folder)
                    blob = self.get_cover_blob(root_folder)
                    # print title, year, file, release, language
                    self.cursor.execute('''INSERT INTO {0} VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(self.table_name),
                                        (None, title, year, root_folder, release, language, blob))
                    self.connection.commit()

    @staticmethod
    def extract_infos_from_filename(name):
        # name, extension = os.path.splitext(filename)
        if not (name[-1] == ')' and name[-6] == '('):
            return None
        year_string = name[-5:-1]
        if not year_string.isdigit():
            return None
        year = int(year_string)
        title = name[0:-7]
        return title, year

    def get_release(self, folder):
        filepath = os.path.join(self.video_folder, folder, 'Infos.nfo')
        with codecs.open(filepath, 'r', 'utf-8') as f:
            first_line = f.readline()
            return first_line

    def get_language(self, folder):
        try:
            start_index = folder.index('[')
            end_index = folder.index(']')
        except ValueError:
            return self.default_language
        language = folder[start_index+1:end_index]
        return language

    def get_cover_blob(self, folder):
        path = os.path.join(self.video_folder, folder, 'folder.jpg')
        with open(path, 'rb') as afile:
            fileblob = afile.read()
            return sqlite3.Binary(fileblob)

    def auslesen(self):
        self.connection.execute('''SELECT * from {0}'''.format(self.table_name))
        result = self.cursor.fetchone()
        while result is not None:
            print result
            result = self.cursor.fetchone()
        self.connection.close()


def main():
    manager = VideosManager()
    manager.aktualisieren()


if __name__ == "__main__":
    main()
