def method_name(url):
    modified_string = url.replace("https://learn.foundry.com/zh-hans/nuke/content/", "")
    print()
    cc = modified_string.split("/")[:-1]
    kk = ""
    for c in cc:
        kk += c + "/"
    return kk
a = 'https://learn.foundry.com/zh-hans/nuke/content/getting_started/installation/windows.html'


print(method_name(a))