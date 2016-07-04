from distutils.core import setup
import py2exe

setup(
    name='Calculator',
    version='0.0.1',
    windows=['calculate.py'],
    options={"py2exe": {"includes": ["sip", "PyQt4.QtGui"]}},
    url='',
    license='',
    author='Tobias Obermayer',
    author_email='Obermayer@live.de',
    description=''
)
