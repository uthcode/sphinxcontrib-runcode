import httplib
import urllib
import urllib2
from docutils import nodes
from docutils.parsers.rst import Directive

from ideone import Ideone

IDEONE_AUTHENTICATED = False

try:
    ideone_auth = Ideone('APIUSER', 'APIPASSWORD')
except Exception as e:
    IDEONE_AUTHENTICATED = False
else:
    IDEONE_AUTHENTICATED = True

class run_code_block(nodes.General, nodes.FixedTextElement):
    pass

class RunCode(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    option_spec = dict(codesite=str,
                       language=str,
                       run=True)

    def run(self):
        document = self.state.document
        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])
        try:
            with open(filename) as fd:
                contents = fd.read()
        except IOError:
            contents = ""
        retnode = run_code_block(contents, contents, source=filename)

        retnode["contents"] = contents

        if self.options.get("language", ""):
            if self.options["language"] in ("Python", "python", "py"):
                retnode["language"] = "Python"
            if self.options["language"] in ("C", "c"):
                retnode["language"] = "C"
        if self.options.get("codesite", ""):
            if self.options['codesite'] == "codepad":
                retnode["codesite"] = "http://codepad.org"
            elif self.options["codesite"] == "ideone":
                retnode["codesite"] = "http://ideone.com"
        if self.options.get("run", ''):
            if self.options["run"] in ("True", "true"):
                retnode["run"] = True

        return [retnode]

def visit_block(self, node):
    """Visit hidden code block"""
    try:
        self.visit_literal_block(node)
    except nodes.SkipNode:
        pass

    url = node.get('codesite')
    code = node.get('contents')
    language = node.get('language')

    if url == 'http://codepad.org':
        values = {'lang' : language,
                  'code' : code,
                  'submit':'Submit'}

        data = urllib.urlencode(values)
        runcode_url = url
        try:
            response = urllib2.urlopen(url, data)
        except (urllib2.URLError, httplib.HTTPException) as e:
            print(str(e))
        else:
            codepage = response.geturl()
            runcode_url = codepage + '/fork'
    elif url == 'http://ideone.com':
        if IDEONE_AUTHENTICATED and ideone_auth.test()["error"] == "OK":
            response = ideone_auth.create_submission(code,language,run=False)
            runcode_url = "http://ideone.com/fork/%s" % (response['link'])
        else:
            runcode_url = "http://ideone.com"

    fill_header = {'runcode_url': runcode_url}

    divblock = ("""<a href="{runcode_url}" class='button' target="_blank">Run this</a><br/>""").format(**fill_header)
    self.body[-1] = divblock
    raise nodes.SkipNode


def depart_block(self, node):
    """Depart hidden code block"""
    # Stub because of SkipNode in visit

def setup(app):
    app.add_directive('runcode', RunCode)
    app.add_node(run_code_block, html=(visit_block, depart_block))
