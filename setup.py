try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.0"


setup(
    name="pyserial-jaculus",
    description="Serial Lib for jaculus in Python",
    version=version,
    author="C2Coder",
    author_email="jansky.stepan08@gmail.com",
    url="https://github.com/c2coder/pyserial-jaculus",
    packages=['jacserial', 'jacserial.tools', 'jacserial.urlhandler', 'jacserial.threaded'],
    license="BSD",
    long_description="""\
Pyserial port for jaculus
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