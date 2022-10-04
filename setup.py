import atexit
from setuptools                 import setup
from setuptools.command.install import install

def _post_install():
    import goosempl
    cf_template.copy_style()

class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)

__version__ = '0.1.0'

setup(
    name              = 'cf_template',
    version           = __version__,
    ...
    install_requires  = ['matplotlib>=2.0.0'],
    packages          = ['cf_template'],
    cmdclass          = {'install': new_install},
    package_data      = {'cf_template/styles':[
        'cf_template/styles/example.mplstyle',
    ]},
)
