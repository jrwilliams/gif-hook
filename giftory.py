#!/usr/bin/python

# 
# Module to keep a GIF-based history of image files. It's main purpose is to be used
# with gif-hook (github.com/jrwilliams/gif-hook) but the core functionality can be 
# useful elsewhere.
# 
# It is actually more general purpose than this and can be used to simply make GIFs.
# 
# Author: James R Williams (jrwilliams)
# Date: 15th September, 2014
# Licence: MIT

from images2gif import writeGif
from PIL import Image, ImageSequence
import os
import string

class Giftory:
	def __init__(self):
		# Default configuration
		self.props = {}
		self.props["frame_duration"] = 0.5
		self.props["filetypes"] = ['*.png', '*.jpg', '*.jpeg']

	def set_prop(self, name, value):
		"""Set a configuration property."""
		self.props[name] = value

	def get_prop(self, name):
		"""Retrieve a configuration property."""
		return self.props[name]

	def make_historic_gif(self, img_path, dir_path):
		"""Create a historic gif. A gif with the same name as the image will be
		created in the specified folder. If the image exists, the image will be 
		appended to the end as the last frame."""
		
		if not os.path.exists(dir_path):
			os.makedirs(dir_path)

		# Gif image
		gif = dir_path + "/" + os.path.splitext(os.path.basename(img_path))[0] + ".gif"

		# Our latest version of the image
		im = Image.open(img_path)
		
		if os.path.exists(gif):
			im_gif = Image.open(gif)

			frames = [frame.copy() for frame in ImageSequence.Iterator(im_gif)] 		
			frames.append(im)

			writeGif(gif, frames, duration=self.props["frame_duration"])
		else:
			frames = [ im ]
			writeGif(gif, frames, duration=self.props["frame_duration"])	

	def make_gif(self, image_paths, gif_path):
		"""Simple utility method to combine a set of images into a gif."""
		frames = []
		for im in image_paths:
			frames.append(Image.open(im))

		writeGif(gif_path, frames, duration=self.props["frame_duration"])
