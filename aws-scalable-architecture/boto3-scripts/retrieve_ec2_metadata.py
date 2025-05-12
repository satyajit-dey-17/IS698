import urllib.request

def fetch(path):
    url = f'http://169.254.169.254/latest/meta-data/{path}'
    with urllib.request.urlopen(url) as r:
        return r.read().decode()

def main():
    print("Available metadata categories:")
    print(fetch(''))          # lists categories
    print("Instance ID:", fetch('instance-id'))

if __name__ == '__main__':
    main()

