from config import Config
from web.web import start_server
from web.simple_routes import simple_routes


def main():
    config = Config()
    start_server(simple_routes, config.get_server_port())

if __name__ == '__main__':
    # TODO: Added handle exceptions SystemExit and KeyboardInterrupt
    main()
