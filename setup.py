from setuptools import setup, find_packages

setup(
    version='1.0',
    name='django_push',
    description='',
    author='Carel Burger',
    author_email='carelburger@gmail.com',
    install_requires=[
        'Django ~=1.11.1',
        'djangorestframework ~=3.6.3',
        'django_push_notifications ~=1.5.0',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
