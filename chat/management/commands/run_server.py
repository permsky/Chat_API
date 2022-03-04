import environs
from django.contrib.staticfiles.management.commands import runserver


env = environs.Env()
env.read_env()


class Command(runserver.Command):
    default_port = env.str('RUNSERVER_PORT')
