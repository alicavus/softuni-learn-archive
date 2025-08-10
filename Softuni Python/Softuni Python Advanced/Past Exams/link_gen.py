from requests import get

with open(__file__.replace("_gen.py", "s.txt")) as links_data:
    for url in links_data:
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            continue
        url = url.replace('svn.softuni.org/admin', 'softuni.bg/downloads')
        file = url.split("/")[-1]

        req = get(url)


        if req.status_code == 200:
            try:
                with open(file, "wb") as f:
                    f.write(req.content)
                    print(f"Downloaded: {file}")
            except Exception as e:
                print(f"Failed to download: {file}", *e.args)
        else:
            print(f"Downloading failed: {req.status_code}")
