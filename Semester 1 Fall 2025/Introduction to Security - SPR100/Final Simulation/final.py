import urllib.request


def fetch_google():
    url = "https://www.google.com"
    with urllib.request.urlopen(url) as response:
        content = response.read()  # bytes in memory, not written to disk
    return content


if __name__ == "__main__":
    data = fetch_google()
    # Show basic info without saving to a file
    print(f"Downloaded {len(data)} bytes from https://www.google.com")
    print("First 200 bytes:")
    print(data[:200])
