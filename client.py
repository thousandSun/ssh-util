import paramiko
from scp import SCPClient


class Client:

    def __init__(self, host: str, username: str, password: str):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__local_path = None
        self.__remote_path = None
        self.__recursive = False
        self.__set_client()

    def __set_client(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.connect(self.__host, username=self.__username, password=self.__password, timeout=10)
        self.__client = client

    def set_local_path(self, local_path: str):
        self.__local_path = local_path

    def set_remote_path(self, remote_path: str):
        self.__remote_path = remote_path

    def set_recursive(self, recursive: bool):
        self.__recursive = recursive

    def upload(self):
        self.__client.connect(self.__host, username=self.__username, password=self.__password, timeout=10)
        with SCPClient(self.__client.get_transport()) as scp:
            scp.put(self.__local_path, self.__remote_path, recursive=self.__recursive)
        self.__client.close()

    def download(self):
        self.__client.connect(self.__host, username=self.__username, password=self.__password, timeout=10)
        with SCPClient(self.__client.get_transport()) as scp:
            scp.get(self.__remote_path, self.__local_path, recursive=self.__recursive)
        self.__client.close()

    def close_client(self):
        self.__client.close()
