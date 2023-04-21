from shimi import *
from motion.recorder import *
from utils.utils import *
from ShimiMakeDance import *



# Load Shimi
shimi = Shimi(silent=False)

local_gestures = {}


load_prev = load_recorder(shimi, "Headbang_gesture", path="saved_gestures")
load_prev.play()
shimi.initial_position
