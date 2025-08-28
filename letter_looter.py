import string, time
target = "liyonoro_10@"
attempt = ""
chars = string.ascii_letters + string.digits + string.punctuation + " "
for i in range(len(target)):
    for c in chars:
        temp = attempt + c
        print(temp)
        time.sleep(0.01)
        if target[i] == c:
            attempt += c
            break
