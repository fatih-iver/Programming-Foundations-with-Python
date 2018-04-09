import urllib.request

def read_text():
    quotes = open("C:\\Users\\fatih\\Desktop\\dummy.txt")
    content = quotes.read()
    check_profanity(content)
    quotes.close()
    
    
def check_profanity(text_to_check):
    print(text_to_check)
    text_to_check = "-".join(text_to_check.split())    
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()
