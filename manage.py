#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv

load_dotenv()

print('*'*50)
print('Loading Environment')
print('*'*50)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wifi_lma.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
