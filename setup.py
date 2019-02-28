from setuptools import setup

setup(
    name = 'firebase-function-python-skeleton',
    version = '0.1.0',
    description = 'Skeleton project of firebase function with python',
    author = 'Udom Tarathummarat',
    author_email = 'paopaojr@gmail.com',
    install_requires = [
        'Flask==1.0.2',
        'Flask-Cors==3.0.7',
        'flask-restplus==0.12.1',
        'mypy==0.670'
    ],
    scripts=[
        'scripts/start-dev',
        'scripts/run-test',
        'scripts/deploy-prod',
        'scripts/clean'
    ],
)
