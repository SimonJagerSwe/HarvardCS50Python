########## TWITTER PROFILE URL ##########
import re
url = input("URL: ").strip()

# Example 1, no regex
'''print(f"URL: {url}")
username = url.replace("https://twitter.com/", "")
# Alternative is username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")'''


# Example 2, using regex with re.sub
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"User name: {username}")


# Example 3, using regex with re.search, walrus, capturing & non-capturing
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    # if matches.group(1) == "com":
    print(f"Username:", matches.group(1))