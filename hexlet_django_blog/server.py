import subprocess


def main():
    cmd = ["python", "manage.py", "runserver", "127.0.0.1:8000"]
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
