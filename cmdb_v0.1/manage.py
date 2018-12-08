#!/usr/bin/env python

#为了区分线上和测试等不同的配置文件，修改mange.py
# 制定配置文件：
# python manage.py runserver --settings=admin.settings.local_cj

import os
import sys

if __name__ == "__main__":
    print(111111, sys.argv)
    if len(sys.argv) > 3:
        print(222222)
        run_arg = sys.argv[2]
        if not run_arg.startswith('--settings'):
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings.settings")
    else:
        print(3333)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings.settings")

    from django.core.management import execute_from_command_line
    print(4444, os.environ['DJANGO_SETTINGS_MODULE'])
    print('-'*20)
    execute_from_command_line(sys.argv)
    print(5555, os.environ['DJANGO_SETTINGS_MODULE'])

    # print(11111, sys.argv)
    # if len(sys.argv) > 2 and sys.argv[2].startswith('--settings'):
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings.local_cj")
    # else:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings.settings")
    # try:
    #     from django.core.management import execute_from_command_line
    # except ImportError:
    #     # The above import may fail for some other reason. Ensure that the
    #     # issue is really that Django is missing to avoid masking other
    #     # exceptions on Python 2.
    #     try:
    #         import django
    #     except ImportError:
    #         raise ImportError(
    #             "Couldn't import Django. Are you sure it's installed and "
    #             "available on your PYTHONPATH environment variable? Did you "
    #             "forget to activate a virtual environment?"
    #         )
    #     raise
    # execute_from_command_line(sys.argv)