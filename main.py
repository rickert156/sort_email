import re

with open('Inbox.mbox', 'r') as file:
    text = file.readlines()
    for t in text:
        if "Your message wasn't delivered to" in t:
            match = re.search(r'[\w\.-]+@[\w\.-]+', t)
            if match:
                email = match.group(0)
                with open('result.txt', 'a+') as file2:
                    file2.write(f'{email}\n')