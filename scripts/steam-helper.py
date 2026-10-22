from pathlib import Path

acf_file = Path("$HOME/.steam/steamapps/appmanifest_222480.acf") # RESIDENT EVIL REVELATIONS

content = acf_file.read_text()

for line in content.splitlines():
    if '"appid"' in line:
        print(line)
        