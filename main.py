import argparse
import os
import socket
from client import Client
from scp import SCPException
from getpass import getpass


def parse():
    parser = argparse.ArgumentParser(description="Connects to remote host for uploading and downloading files",
                                     exit_on_error=False)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--upload", action="store_true", help="[REQUIRED] Sets program to upload files: "
                                                                   "Cannot be set together with -d")
    group.add_argument("-d", "--download", action="store_true", help="[REQUIRED] Sets program to download files: "
                                                                     "Cannot be set together with -u")

    required_args = parser.add_argument_group("Required arguments")
    required_args.add_argument("-un", "--username", help="Username to connect to Host", required=True)
    required_args.add_argument("-lp", "--local-path", help="Local path to upload/download", required=True)
    required_args.add_argument("-rp", "--remote-path", help="Remote path to upload/download", required=True)

    parser.add_argument("host", help="Host to connect to for upload/download")
    parser.add_argument("-r", "--recursive", help="Sets program to recursively download/upload directory",
                        action="store_true")

    try:
        args = parser.parse_args()

        if not args.upload and not args.download:
            parser.print_usage()
    except argparse.ArgumentError:
        print("ERROR: cannot set -u and -d together")
        parser.print_help()
        exit(1)
    else:
        return args


def main():
    args = parse()
    local_path = os.path.abspath(args.local_path)
    if not os.path.exists(local_path):
        print(f"{local_path} does not exist.")
        print("Verify path and try again.")
        exit(1)
    password = getpass("Password: ")

    client = Client(args.host, args.username, password)
    client.set_local_path(local_path)
    client.set_remote_path(args.remote_path)
    if args.recursive:
        client.set_recursive()

    try:
        if args.upload:
            client.upload()
            print(f"Success in uploading '{local_path}' to '{args.host}:{args.remote_path}'")
        elif args.download:
            client.download()
            print(f"Success in downloading '{args.remote_path}' from '{args.host}' to '{local_path}'")
    except TimeoutError:
        print(f"Failed to connect to {args.host}")
        print("Verify destination and try again.")
        exit(1)
    except SCPException:
        print("Failed to process file")
        print("Verify file and try again")
        exit(1)
    except socket.timeout:
        print(f"The connection to {args.host} timed out.")
    finally:
        client.close_client()


if __name__ == '__main__':
    main()
