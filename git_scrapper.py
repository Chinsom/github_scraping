import requests
from bs4 import BeautifulSoup as bs


user_name=input("\nType in your github username: ")
url=("https://github.com/"+ user_name)
r= requests.get(url,timeout=10)

soup = bs(r.content,"html.parser")

profile_user = soup.find("img", {"class": "avatar avatar-user width-full border color-bg-default"})

if profile_user:
    profile_user = profile_user["src"]
    print("\nProfile picture URL:", profile_user)
else:
    print("\nProfile picture not found.")

bio = soup.find('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'})

if bio:
    print("\nBio:")
    print(bio.text.strip())
else:
    print("\nNo bio found.")
