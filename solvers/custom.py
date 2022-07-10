from .claspy import *
from . import utils
from .utils.borders import *
from .utils.loops import *
from .utils.numbers import *
from .utils.regions import *
from .utils.shading import *
from .utils.solutions import *

def encode(string):
    return utils.encode(string, has_borders = True, clue_encoder = lambda x : x)

def solve(E):
    set_max_val(100)
    return []

def decode(solutions):
    return utils.decode(solutions)
