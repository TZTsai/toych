import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import toych.model
import toych.optim
import toych.utils
from toych.func import *
from toych.model import Model, Compose
from toych.utils.graph import show_compgraph
from toych.utils.dev import setloglevel

setloglevel('INFO')