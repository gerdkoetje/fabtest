from fabric.api import run, env
from fabtools import require
import fabtools
from fabtools.system import distrib_id, distrib_release

def initial_setup():
    env.host_string = ''
    env.user  = 'root'
    env.password = ''

    require.deb.packages([
        'sudo',
        'python-setuptools',
        'python-simplejson',
    ])

    with fabtools.python.virtualenv('/home/myuser/env'):
        require.python.package('pyramid')

    require.postgres.server()
    require.postgres.user('myuser', 's3cr3tp4ssw0rd')
    require.postgres.database('myappsdb', 'myuser')