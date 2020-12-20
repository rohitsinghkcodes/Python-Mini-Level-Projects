# importing modules
import pywhatkit
import wikipedia

#searching on wikipedia and returning the result
def wikiSearch(search):
    return wikipedia.summary(search,sentences = 10)

#converting into hand written form
def handWritten(searchElement):
    text = wikiSearch(searchElement)
    pywhatkit.text_to_handwriting(text,rgb=[0,0,0],save_to='converted.png')


if __name__ == "__main__":
    searchElement = input('WHAT DO YOU WANT TO SEARCH AND CONVERT : ')
    handWritten(searchElement)



