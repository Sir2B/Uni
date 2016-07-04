#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

class BytePrinter( threading.Thread ) :
    """
    A sample thread class
    """
    def __init__(self, name="TestThread"):
        """
        Constructor, setting initial variables
        """
        threading.Thread.__init__(self, name=name)

    def run(self):
        """
        overload of threading.thread.run()
        main control loop
        """
        print "%s starts" % (self.getName(),)
        for i in range(-128, 1280):
            print self.getName(), i
            time.sleep(0.0001) # sleep 0.1 ms

# main
bp1 = BytePrinter("Helmut")
bp2 = BytePrinter("Edi")
bp3 = BytePrinter("Angie")

bp1.start()
bp2.start()
bp3.start()
# bp3.stop()