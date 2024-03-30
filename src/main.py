from config import Config
from web.server import start_server
from web.routes import simple_routes, regexp_routes


def main():
    config = Config()
    start_server(simple_routes, regexp_routes, config.get_server_port())

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('long KeyboardInterrupt exception message.')
