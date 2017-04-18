__author__ = 'Tobias.Obermayer'
from cPickle import dump

class Klasse1(object):
    def __init__(self):
        self.x = 5
        self.y = 1

class Klasse2(object):
    def __init__(self):
        self.x = 5
        self.y = 1



def main():
    test1 = Klasse1()
    test2 = Klasse2()
    with open('pickleSource', 'wb') as datei:
        dump(Klasse1, datei)
        dump(test1, datei)



    print type(test1)
    print type(test2)
    print test1.__class__
    print test2.__class__
    print test2.__class__ == Klasse2





if __name__ == '__main__':
    main()