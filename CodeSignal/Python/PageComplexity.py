# You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the complexity of the main page of your site. In order to measure the complexity of the page, you need to find a set of all tags located on the deepest level of a tree correponsing to HTML document. Given a valid HTML document, find all distinct tags located on the deepest level.

# Example

# For
# document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"
# the output should be
# solution(document) = ["h1", "p"].

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.max_depth = 0
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth
            self.tags = [tag]
        elif self.depth == self.max_depth and tag not in self.tags:
            self.tags.append(tag)

    def handle_endtag(self, tag):
        self.depth -= 1

def solution(document):
    parser = MyHTMLParser()
    parser.feed(document)
    return sorted(parser.tags)
