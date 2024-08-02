from fabric.api import *

env.user = 'root'
env.hosts = ["172.17.0.2"]

def upload():
	run("ls ~")
def host_name():
    sudo("ls ~")
