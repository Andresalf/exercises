import sys
import os

these_modules_path = os.path.abspath(os.path.dirname(__file__))
if these_modules_path not in sys.path:
    sys.path.append(these_modules_path)