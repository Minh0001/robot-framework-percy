from setuptools import setup, find_packages

requirements = [
    'percy',
    'robotframework',
    'robotframework-selenium2library',
]

setup(
    name='robot-framework-percy',
    version='0.1',
    description='Robot framework Percy client',
    url='https://github.com/Minh0001/robot-framework-percy',
    author='Minh Le',
    author_email='quangminh0001@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
