from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    windows = ['dota2_ehp_idea_rc2.pyw'],
    options = {'py2exe': {
        'bundle_files': 1,
        }
    },
    zipfile = None
)
