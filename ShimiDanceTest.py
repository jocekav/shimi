from shimi import *
from motion.recorder import *
from utils.utils import *
from ShimiMakeDance import *



# Load Shimi
shimi = Shimi(silent=False)

local_gestures = {}

dance = MakeDance(shimi, 1.0, 5.0, [shimi.head, shimi.foot, shimi.phone], "Headbang")
dance.run()
