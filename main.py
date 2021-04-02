import sys
import os
from client import Client
from scp import SCPException
from getpass import getpass

"""TODO:
Make class for client
"""

USAGE = "script.py [--upload | --download] [--username <username>] <host> " \
        "[<localpath> | <remotepath>] [<remotepath> | <localpath>]"


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
        if not os.path.exists(local_path):
            print(f"{local_path} does not exist.")
            print("Verify path and try again.")
            sys.exit(1)
        remote_path = sys.argv[6]
    elif sys.argv[1] == '--download':
        up_down = 'down'
        remote_path = sys.argv[5]
        local_path = os.path.abspath(sys.argv[6])
        if not os.path.exists(local_path):
            print(f"{local_path} does not exist")
            print("Verify path and try again.")
            sys.exit(1)

    host = sys.argv[4]
    username = sys.argv[3]
    password = getpass("Password: ")

    client = Client(host, username, password, local_path, remote_path)

    try:
        if up_down == 'up':
            client.upload()
            print(f"Success in uploading '{local_path}' to '{host}:{remote_path}'")
        elif up_down == 'down':
            client.download()
            print(f"Success in downloading '{remote_path}' from '{host}' to '{local_path}'")
    except TimeoutError:
        print(f"Couldn't connect to {host}")
        print("Verify destination and try again.")
        sys.exit(1)
    except SCPException:
        print("Couldn't process file")
        print("Verify file and try again")
        sys.exit(1)
    finally:
        client.close_client()


if __name__ == '__main__':
    main()
