from setuptools import setup, find_namespace_packages

setup(
    name='personal-assistant-bot',
    version='1.0.0',
    description='Personal Assistant Console Bot for contacts and notes',
    author='Vic Lymar',
    author_email='victorlymar@gmail.com',
    packages=find_namespace_packages(),
    install_requires=[
        'colorama==0.4.6'
    ],
    entry_points={
        'console_scripts': [
            'assistant-bot = modules.console_bot.console_bot:main'
        ]
    }
)