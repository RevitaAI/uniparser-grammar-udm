from setuptools import setup
from distutils.command import build as build_module

class build(build_module.build):
  def run(self):
    exec(open("./pre_build.py").read())
    build_module.build.run(self)

setup(
    cmdclass = {
      'build': build,
    }
)
