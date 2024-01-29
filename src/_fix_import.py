import os
import sys

current_path = os.path.join(os.path.dirname(sys.path[0]), "")
parent_path  = os.path.abspath(os.path.join(current_path, os.pardir))

sys.path.append(current_path)
sys.path.append(parent_path)