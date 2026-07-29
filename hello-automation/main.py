from datetime import datetime

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, the time is: {now}")


if __name__ == "__main__":
    main()