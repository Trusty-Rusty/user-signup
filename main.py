import webapp2
import cgi
import re

#html biolerplate for top of page
header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>User Signup</h1>
"""
def generic_form(username, password, verify, email):
    form = """
    <form action='/' method='post'>
        <label>Username: <input type='text' name='username' value='{0}'/></label>
        <br>
        <label>Password: <input type='text' name='password' value='{1}'/></label>
        <br>
        <label>Confrim Password: <input type='text' name='verify' value='{2}'/></label>
        <br>
        <label>Email (optional): <input type='text' name='email' value='{3}'/></label>
        <br>
        <input type="submit" value="Submit"/>
    </form>
    """.format(username, password, verify, email)
    return(form)

#html biolerplate for bottom of page
footer = """
</body>
</html>
"""
#regular expressions for verifying inputs
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = (r"^.{3,20}$")
EMAIL_RE =  (r"^[\S]+@[\S]+.[\S]+$")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        """Handles requests to main (/) page"""
        username = ""
        password = ""
        verify = ""
        email = ""
        main_content = generic_form(username, password, verify, email)
        content = (header + main_content + footer)
        self.response.write(content) #print the content to the page

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')



class Welcome(webapp2.RequestHandler):
    """Merely prints welcome message"""
    #def post(self):

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
