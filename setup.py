from setuptools import setup

setup(name='stuffleQuestBot',
      version='0.1',
      description='Discord bot with a part of the stuffle\'s life',
      url='https://github.com/CheshireCat12/PythonBotDiscord',
      author='Anthony Gillioz',
      author_email='anthony.gillioz@he-arc.ch',
      license='MIT',
      packages=['stuffleQuest'],
      install_requires=['Discord.py', 'graphql-core'],
      entry_points={'console_scripts': [
          'stuffleQuest = bookbot:main'
      ]},
zip_safe=False)
