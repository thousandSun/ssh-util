import sys
import os
import paramiko
from scp import SCPClient
from getpass import getpass

"""TODO:
implement downloading from remote
implement command line argument functionality for upload/download
implement password getting from user in python book
functionify the program
if possible classify it
handle TimeoutError for ssh"""

USAGE = "script.py [--upload | --download] [--username <username>] <host> [<localpath> | <remotepath>] [<remotepath> | <localpath>]"


def upload(client, host, local_path, remote_path, username, password):
    client.connect(host, username=username, password=password)

    with SCPClient(client.get_transport()) as scp:
        scp.put(local_path, remote_path)
    client.close()


def download(client, host, remote_path, local_path, username, password):
    client.connect(host, username=username, password=password)
    with SCPClient(client.get_transport()) as scp:
        scp.get(remote_path, local_path)
    client.close()


def main():
    if len(sys.argv[1:]) < 6:
        print("Invalid Usage")
        print(USAGE)
        sys.exit(1)

    up_down = ''
    local_path = ''
    remote_path = ''
    if sys.argv[1] == '--upload':
        up_down = 'up'
        local_path = os.path.abspath(sys.argv[5])
        remote_path = sys.argv[6]
    elif sys.argv[1] == '--download':
        up_down = 'down'
        remote_path = sys.argv[5]
        local_path = os.path.abspath(sys.argv[6])

    host = sys.argv[4]
    user = sys.argv[3]
    password = getpass("Password: ")

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if up_down == 'up':
        upload(client, host, local_path, remote_path, user, password)
    elif up_down == 'down':
        download(client, host, remote_path, local_path, user, password)


if __name__ == '__main__':
    main()
