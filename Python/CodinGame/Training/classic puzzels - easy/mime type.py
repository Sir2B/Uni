import sys
import math
import os

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.

mime_dic = dict()
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    print >> sys.stderr, ext, mt
    mime_dic[ext.lower()] = mt

print >> sys.stderr, mime_dic
for i in xrange(q):
    fname = raw_input()  # One file name per line.
    
    last_dot = fname.rfind('.')
    if last_dot != -1:
    	f_ext = fname[last_dot+1:]
    else:
    	f_ext = ""
    # splitted_name = os.path.splitext(fname)
    # if splitted_name[1] is "":
    # 	f_ext = splitted_name[0]
    # else:
    # 	f_ext = splitted_name[1]
    # f_ext = f_ext.replace('.', '')
    m_type = "UNKNOWN"
    if f_ext.lower() in mime_dic:
    	m_type = mime_dic[f_ext.lower()]

    print >> sys.stderr, "{0} = {1} (ext: {2})".format(fname, m_type, f_ext)
    print m_type

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

