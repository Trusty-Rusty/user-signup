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
def generic_form(username, password, verify, email, error1, error2, error3, error4):
    form = """
    <form action='/' method='post'>
        <label>Username: <input type='text' name='username' value='{0}'/></label>
        <p class=error>{4}</p>
        <label>Password: <input type='password' name='password' value='{1}'/></label>
        <p class=error>{5}</p>
        <label>Confrim Password: <input type='password' name='verify' value='{2}'/></label>
        <p class=error>{6}</p>
        <label>Email (optional): <input type='text' name='email' value='{3}'/></label>
        <p class=error>{7}</p>
        <input type="submit" value="Submit"/>
    </form>
    """.format(username, password, verify, email, error1, error2, error3, error4)
    return(form)

#html biolerplate for bottom of page
footer = """
</body>
</html>
"""
#regular expressions for verifying inputs
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE =  re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):   #validate username
    return USER_RE.match(username)

def valid_password(password):   #validate password
    return PASSWORD_RE.match(password)

def valid_email(email):   #validate email
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        """Handles requests to main (/) page"""
        username = ""
        password = ""
        verify = ""
        email = ""
        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        main_content = generic_form(username, password, verify, email, error1, error2, error3, error4)
        content = (header + main_content + footer)
        self.response.write(content) #print the content to the page

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if not valid_username(username):
            error1 = "Please enter a valid username."

        if not valid_password(password):
            error2 = "Please enter a valid password."

        if password != verify:
            error3 = "Passwords do not match."

        if not valid_email(email):
            error4 = "Please enter a valid email address."

        main_content = generic_form(username, password, verify, email, error1, error2, error3, error4)
        content = (header + main_content + footer)
        self.response.write(content) #print filled out form and any errors to the page


class Welcome(webapp2.RequestHandler):
    """Merely prints welcome message"""
    #def post(self):

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
