from setuptools import setup, find_packages
import io

def read_all(f):
    with io.open(f, encoding="utf-8") as I:
        return I.read()

requirements = list(map(str.strip, open("requirements.txt").readlines()))

setup(
    name='test-release-rts-py',
    version="1.4.7",
    description='Test Release for RedisTimeSeries Python Client',
    long_description=read_all("README.md"),
    long_description_content_type='text/markdown',
    url='https://github.com/filipecosta90/test-release-rts-py',
    packages=['test-release-rts-py'],
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database',
        'Topic :: Software Development :: Testing'
    ],
    keywords='Redis TimeSeries Extension',
    author='RedisLabs',
    author_email='oss@redislabs.com'
)
