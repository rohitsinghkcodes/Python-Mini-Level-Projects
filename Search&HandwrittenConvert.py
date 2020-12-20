# importing modules
import pywhatkit
import wikipedia

#searching on wikipedia and returning the result
def wikiSearch(search):
    return wikipedia.summary(search,sentences = 3)

#converting into hand written form
def handWritten(searchElement):
    text = wikiSearch(searchElement)
    pywhatkit.text_to_handwriting(text,rgb=[0,0,0])


if __name__ == "__main__":
    handWritten('India')



