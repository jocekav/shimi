import os
import sys
import random
from shimi import *
import time
import datetime
from motion.move import Move
import argparse
import threading

class ShimiDance:
	def __init__(self, bpm):
		self.shimi = Shimi()
		self.time = 60 / bpm

		self.neck_ud = Move(self.shimi, self.shimi.neck_ud, 1, 1)
		self.neck_lr = Move(self.shimi, self.shimi.neck_lr, 0.5, 1)
		self.torso = Move(self.shimi, self.shimi.torso, 1, 1)
		self.foot = Move(self.shimi, self.shimi.foot, 0, 1)

		self.start()

	def start(self):
		self.neck_ud.start()
		self.neck_lr.start()
		self.torso.start()
		self.foot.start()

		self.neck_ud.join()
		self.neck_lr.join()
		self.torso.join()
		self.foot.join()

	def front(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.torso.add_move(1.1,self.time/2,vel_algo="constant")
		#self.foot.add_move(0,self.time,vel_algo="constant")
		self.neck_ud.add_move(1,self.time,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time,vel_algo="constant")

	def front_left(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.torso.add_move(1.1,self.time/2,vel_algo="constant")
		#self.foot.add_move(0,self.time,vel_algo="constant")
		self.neck_ud.add_move(1,self.time,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

	def front_right(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.torso.add_move(1.1,self.time/2,vel_algo="constant")
		#self.foot.add_move(0,self.time,vel_algo="constant")
		self.neck_ud.add_move(1,self.time,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

	def back_left(self):
		self.torso.add_move(1.1,self.time,vel_algo="constant")
		#self.foot.add_move(0,self.time,vel_algo="constant")
		self.neck_ud.add_move(0.2,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

	def back_right(self):
		self.torso.add_move(1.1,self.time,vel_algo="constant")
		#self.foot.add_move(0,self.time,vel_algo="constant")
		self.neck_ud.add_move(0.2,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

	def gesture_1(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant") #1
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant") #2
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant") #3
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant") #4
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #5
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		#self.foot.add_move(1,self.time/4,vel_algo="constant")
		#self.foot.add_move(0,self.time/4,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")

	def gesture_2(self):
		self.front()
		self.front()
		self.front()

	def gesture_3(self):
		self.front_left()
		self.back_right()
		self.front_left()
		self.back_right()

	def gesture_4(self):
		self.front_right()
		self.back_left()
		self.front_right()
		self.back_left()

	def gesture_5(self):
		self.front_left()
		self.back_right()
		self.front_right()
		self.back_left()

	def add_foot_stay(self):
		self.foot.add_move(0,self.time,vel_algo="constant")

	def add_foot(self):
		self.foot.add_move(2,self.time/2,vel_algo="constant")
		self.foot.add_move(0,self.time/2,vel_algo="constant")

	def random_hiphop_dance(self, n):
		for i in range(n):
			r = random.randint(1, 5)
			if r == 1:
				self.hiphop_1()
				self.hiphop_4()
			if r == 2:
				self.hiphop_1()
				self.hiphop_2()
				self.hiphop_1()
			if r == 3:
				self.hiphop_3()
				self.hiphop_2()
			if r == 4:
				self.hiphop_4()
				self.hiphop_1()
			if r == 5:
				self.hiphop_5()

	def random_rock_dance(self, n):
		for i in range(n):
			r = random.randint(1,5)
			if r == 1:
				self.rock_1()
				self.rock_4()
			if r == 2:
				self.rock_2()
				self.rock_1()
			if r == 3:
				self.rock_1()
				self.rock_3()
			if r == 4:
				self.rock_4()
				self.rock_1()
			if r == 5:
				self.rock_5()

	def random_head_dance(self, n):
		for i in range(n):
			r = random.randint(1,4)
			if r == 1:
				self.front_left()
			if r == 2:
				self.front_right()
			if r == 3:
				self.back_left()
			if r == 4:
				self.back_right()

	def hiphop_1(self):
		self.torso.add_move(1.1,self.time,vel_algo="constant")
		self.neck_ud.add_move(0.2,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time,vel_algo="constant")
		self.add_foot()

	def hiphop_2(self):
		self.front_left()
		self.back_right()
		self.add_foot()
		self.add_foot()

	def hiphop_3(self):
		self.front_right()
		self.back_left()
		self.add_foot()
		self.add_foot()

	def hiphop_4(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant") #1
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		self.add_foot()

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

		self.torso.add_move(0.8,self.time/2,vel_algo="constant") #2
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		self.add_foot()

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #3
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		self.add_foot()

	def hiphop_5(self):
		self.back_left()
		self.back_right()
		self.back_left()
		self.back_right()
		self.add_foot()
		self.add_foot()
		self.add_foot()
		self.add_foot()

	def rock_1(self):
		self.front()
		self.add_foot()

	def rock_2(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #1
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		self.add_foot()

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #2
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")
		self.add_foot()

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.2,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #3
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		self.add_foot()

	def rock_3(self):
		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #1
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		self.add_foot()

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #2
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")
		self.add_foot()

		self.torso.add_move(0.8,self.time/2,vel_algo="constant")
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.8,self.time/2,vel_algo="constant")

		self.torso.add_move(1.1,self.time/2,vel_algo="constant") #3
		self.neck_ud.add_move(1,self.time/2,vel_algo="constant")
		self.neck_lr.add_move(0.5,self.time/2,vel_algo="constant")
		self.add_foot()

	def rock_4(self):
		self.front_left()
		self.front()
		self.front_right()
		self.add_foot()
		self.add_foot()
		self.add_foot()

	def rock_5(self):
		self.front()
		self.front()
		self.front()
		self.front()
		self.add_foot()
		self.add_foot()
		self.add_foot()
		self.add_foot()
