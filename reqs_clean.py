with open("requirements.txt") as f, open("requirements_clean.txt", "w") as out:
    out.writelines(f"{line.split('=')[0].split('<')[0].split('>')[0].strip()}\n" for line in f if line.strip() and not line.startswith("#"))
