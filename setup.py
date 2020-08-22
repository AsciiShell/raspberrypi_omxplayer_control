from pkg_resources import parse_requirements
from setuptools import find_packages, setup


def load_requirements(filename: str) -> list:
    requirements = []
    with open(filename, 'r') as f:
        for requirement in parse_requirements(f.read()):
            extras = '[{}]'.format(','.join(requirement.extras)) if requirement.extras else ''
            requirements.append(
                '{}{}{}'.format(requirement.name, extras, requirement.specifier)
            )
    return requirements


module_name = 'raspberrypi_omxplayer_control'

with open('README.md', 'rt') as f:
    long_description = f.read()

setup(
    name=module_name,
    version='0.1.15',
    description='Web remote control for raspberrypi omxplayer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AsciiShell/raspberrypi_omxplayer_control',
    author='asciishell (Aleksey Podchezertsev)',
    author_email='dev@asciishell.ru',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
    ],
    keywords=['raspberry-pi', 'omxplayer', 'remote-control', 'python3'],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            '{0} = {0}.__main__:main'.format(module_name),
        ]
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=load_requirements('requirements.txt'),
)
