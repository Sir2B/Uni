__author__ = 'Tobias.Obermayer'
import numpy

def main():
    with open('rohr.dat','r') as datei:
        a = numpy.array(datei)
        print a


if __name__ == '__main__':
    main()


QLabel.setText()