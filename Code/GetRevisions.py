import urllib2
import re

def GetRevisions(pageTitle):
    url = "https://en.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvlimit=500&titles=" + pageTitle
    revisions = []                                        #list of all accumulated revisions
    next = ''                                             #information for the next request
    while True:
        response = urllib2.urlopen(url + next).read()     #web request
        revisions += re.findall('<rev [^>]*>', response)  #adds all revisions from the current request to the list

        cont = re.search('<continue rvcontinue="([^"]+)"', response)
        if not cont:                                      #break the loop if 'continue' element missing
            break

        next = "&rvcontinue=" + cont.group(1)             #gets the revision Id from which to start the next request

    return revisions;