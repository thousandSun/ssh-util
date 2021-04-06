import sys
import os
import socket
from client import Client
from scp import SCPException
from getpass import getpass

USAGE = "main.py [--upload | --download] [--username <username>] <host> " \
        "[<localpath> | <remotepath>] [<remotepath> | <localpath>] [--recursive | -r]"


def main():
    if len(sys.argv[1:]) < 6:
        print("Invalid Usage")
        print(USAGE)
        sys.exit(1)

    up_down = ''
    local_path = ''
    remote_path = ''
    recurse = False
    if len(sys.argv[1:]) == 7 and (sys.argv[7] == '--recursive' or sys.argv[7] == '-r'):
        recurse = True
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

    client = Client(host, username, password)
    client.set_local_path(local_path)
    client.set_remote_path(remote_path)
    client.set_recursive(recurse)

    try:
        if up_down == 'up':
            client.upload()
            print(f"Success in uploading '{local_path}' to '{host}:{remote_path}'")
        elif up_down == 'down':
            client.download()
            print(f"Success in downloading '{remote_path}' from '{host}' to '{local_path}'")
    except TimeoutError:
        print(f"Failed to connect to {host}")
        print("Verify destination and try again.")
        sys.exit(1)
    except SCPException:
        print("Failed to process file")
        print("Verify file and try again")
        sys.exit(1)
    except socket.timeout:
        print(f"The connection to {host} timed out.")
    finally:
        client.close_client()


if __name__ == '__main__':
    main()
