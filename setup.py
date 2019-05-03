from setuptools import setup, find_packages
setup(
    name = 'helloflask',
    version = '0.01',
    packages = find_packages(exclude = ['tests']),
    install_requires = [
    'Flask>=0.12.3',
    'gunicorn>=19.5.0',
    'httplib2==0.9.2',
    'itsdangerous==0.24',
    'Jinja2>=2.10.1',
    'MarkupSafe==0.23',
    'PySocks==1.5.6',
    'pytz==2015.6',
    'six==1.10.0',
    'twilio==4.6.0',
    'Werkzeug==0.10.4',
    'wheel==0.24.0'
    ],
    test_suite = 'tests'
    )