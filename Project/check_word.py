import urllib

def read_text_files():
    #get the list of files
    file_path = "/Users/Slimn/Desktop/Work/Project/Python/Programming Foundations with Python/movie_quotes.txt"
    quote = open(file_path)
    file_content = quote.read()
    #print(file_content)
    quote.close()
    check_profanity(file_content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)

    output = connection.read()
    connection.close()

    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text_files()
