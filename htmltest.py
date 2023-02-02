from html.parser import HTMLParser
import urllib.request


#############################################
def cleandata(d):
    cd = d.strip()
    cd1=cd.replace('\\n','')
    cd2=cd1.replace('\\t','')    
    return cd2

##############################################    
class MyHTMLParser(HTMLParser):
    TableTag=False
    TableData=False
    TableRow=False
    TableA=False
    ptext=False
    Path="http://www.overthedesk.com/spanking_stories/"
    Parsed=""
    
    def handle_starttag(self, tag, attrs):
        if tag=="table": self.TableTag=True
        if tag=="td": self.TableData=True
        if tag=="tr": self.TableRow=True
        if tag=="a":
            self.TableA=True
            if attrs[0][0]=='href':
                s=attrs[0][1]
                if self.Path in s and 'tag' not in s and 'category' not in s and 'http' in s:
                    self.Parsed=self.Parsed + s + '\n'
        if tag=="p": self.ptext = True

    def handle_endtag(self, tag):
        if tag=="table": self.TableTag=False
        if tag=="td": self.TableData=False
        if tag=="tr": self.TableRow=False
        if tag=="a": self.TableA=False
        if tag=="p": self.ptext=False
        #        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.ptext:
            self.Parsed=self.Parsed + data + "\n"

    def print_parsed(self):
        print(self.Parsed)

    def return_parsed(self):
        return(self.Parsed)

def read_story(story):
    parser= MyHTMLParser()
    with urllib.request.urlopen('http://www.overthedesk.com/spanking_stories/story-index/') as response:
        html = cleandata(str(response.read()))
        parser.feed(html)
        return(parser.return_parsed())
    

parser= MyHTMLParser()
with urllib.request.urlopen('http://www.overthedesk.com/spanking_stories/story-index/') as response:
    html = cleandata(str(response.read()))
    parser.feed(html)
    stories=parser.return_parsed()
    print (stories)
##    for story in stories:
##        read_story(story)
##    print(read_story(stories[10]))
        
    
