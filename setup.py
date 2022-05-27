# usr/bin/python3.8.10

from setuptools import setup
import platform
from shutil import move

setup(
   name='hsaban',
   version='v0.6',
   description=' Computational Math Calculus',
   download_url='https://github.com/AhSiber/Hsaban_math/archive/refs/tags/v0.6.zip',
   url='https://github.com/AhSiber/Hsaban_math/',
   scripts='/hsaban/match.py',
   script_name='hsaban',
   fullname='hsaban math'
)

try:
   unameed = platform.node().split("-")[0]
   if platform.system() == "Linux":
      move(src=f"hsaban" , dst=f'/home/{unameed}/Desktop')
except:
   pass
