import sys

from builder import env_builder
from builder import server


def main():
    mode_or_url = sys.argv[1]
    if mode_or_url == 'server_mode':
        server.run()
    else:
        env_builder.check_push_thread(mode_or_url)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stop")
