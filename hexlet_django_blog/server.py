import subprocess
import signal
import sys


def signal_handler(sig, frame):
    print(' You pressed Ctrl+C!')
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    cmd = ["python", "manage.py", "runserver", "127.0.0.1:8000"]
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
