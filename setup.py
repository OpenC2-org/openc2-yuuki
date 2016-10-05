from distutils.core import setup

setup(name='yuuki',
      version='0.1a3',
      description='OpenC2 proxy',
      author='Joshua Brule',
      author_email='jtcbrule@gmail.com',
      packages=['yuuki'],
      install_requires=[
          "requests >= 2.11.1",
          "PyYAML >= 3.11",
          "Flask == 0.11.1"])


