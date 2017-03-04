from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cricketlivescore',
      version='1.1.2',
      description='Get live cricket scores',
      url='http://github.com/appi147/cricketlivescore',
      author='Arpit Choudhary',
      author_email='arpitkumar147@gmail.com',
      keywords='cricket live score',
      license='MIT',
      scripts=['bin/cricls'],
      packages=['cricketlivescore'],
      install_requires=[
          'feedparser',
      ],
      zip_safe=False)
