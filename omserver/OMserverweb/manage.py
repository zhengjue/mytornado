#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    #  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OMserverweb.settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OMserverweb.settings")
    #  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
>>>>>>> 94a4bbcaa2a9b06f28fe9deea9e23b30711c484d

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
