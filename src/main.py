from config import Config
from web.web import start_server

# TODO: Added handle exceptions SystemExit and KeyboardInterrupt
def main():
    config = Config()
    start_server(config.get_server_port())

if __name__ == '__main__':
    main()
