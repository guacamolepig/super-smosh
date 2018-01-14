from data import main

import os

# this get our current location in the file system
import inspect
root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

if __name__ == '__main__':
    main.run(root)
