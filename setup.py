try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.0"


setup(
    name="jacprotocol",
    description="Protocol lib Jaculus",
    version="1.0",
    author="C2Coder",
    author_email="",
    url="https://github.com/c2coder/JacProtocol",
    packages=['jacprotocol'],
    license="BSD",
    long_description="""\
Protocol lib for Jaculus devices (https://jaculus.org)
""",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals :: Serial',
    ],
    platforms='any',
)