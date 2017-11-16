import setuptools

assert setuptools.__version__ >= '30.3', "Requires latest version of setuptools"

setuptools.setup(
    entry_points={
        'paste.app_factory': [
            'main = {{ cookiecutter.repo_name }}:main',
        ]
    },
)
