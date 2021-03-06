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
        <label>Username: <input type='text' name='username' value='{0}'/></label><span class=error>{4}</span>
        <br>
        <label>Password: <input type='password' name='password' value='{1}'/></label><span class=error>{5}</span>
        <br>
        <label>Confrim Password: <input type='password' name='verify' value='{2}'/></label><span class=error>{6}</span>
        <br>
        <label>Email (optional): <input type='text' name='email' value='{3}'/></label><span class=error>{7}</span>
        <br>
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
        error_count = 0

        if not valid_username(username):
            error1 = "Please enter a valid username."
            error_count += 1

        if not valid_password(password):
            error2 = "Please enter a valid password."
            error_count += 1

        if password != verify:
            error3 = "Passwords do not match."
            error_count += 1

        if not valid_email(email):
            error4 = "Please enter a valid email address."
            error_count += 1

        main_content = generic_form(username, password, verify, email, error1, error2, error3, error4)
        content = (header + main_content + footer)
        if error_count == 0:
            self.redirect("/welcome?username=" + username)     #If no errors, then redirect to welcome page

        else:
            self.response.write(content) #print filled out form and any errors to the page


class Welcome(webapp2.RequestHandler):
    """Merely prints welcome message"""

    def get(self):
        username = self.request.get('username')
        welcome_message = """
        <h1>Success!</h1>
        <h2>Welcome, {0}</h2>
        """.format(username)
        self.response.write(welcome_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
