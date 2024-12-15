#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import signal
import pygame
import sys

def cleanup_on_exit(signal, frame):
    pygame.quit()
    print("pygame has been stopped!")
 
    with open('', 'w') as f:
        # Truncate the file, which effectively clears its contents
        f.truncate(0)
    print("face file has been cleared")
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup_on_exit)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmoSyncWebsite.settings')
    try:
        pygame.init()
        print("pygame initialized!")
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

