# -*- coding: utf-8 -*-
"""The register user Handler."""

from user import User, UserHandler


class RegisterUserHandler(UserHandler):
    """Register page."""

    def get(self):
        """Display register form."""
        self.view('register.html')

    def post(self):
        """Try to save the new user."""
        valid = True
        username = self.request.get('username').strip()
        email = self.request.get('email').strip()
        password = self.request.get('password').strip()
        re_password = self.request.get('password-validate').strip()
        params = dict(username=username, email=email)
        if not self.valid_username(username):
            params['error_username'] = "That's not a valid username."
            valid = None
        if not self.valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            valid = None
        elif password != re_password:
            params['error_password_verify'] = "Your passwords didn't match."
            valid = None

        if not self.valid_email(email):
            params['error_email'] = "That's not a valid email."
            valid = None

        if valid:
            uniques = ['email_address']
            success, info = User.create_user(username, uniques,
                                             email_address=email,
                                             name=username,
                                             password_raw=password,
                                             verified=False)
            if not success:
                if 'auth_id' in info:
                    params['error_username'] = "Username already taken."
                    valid = None
                if 'email_address' in info:
                    params['error_email'] = "That E-mail address is in use."
                    valid = None
        if not valid:
            self.view('register.html', **params)
        else:
            user_id = info.get_id()
            token = User.create_signup_token(user_id)
            verification_url = self.uri_for('auth.verification', operation='v',
                                            user_id=user_id, token=token,
                                            _full=True)
            self.view('verification.html', username=username,
                      verification_url=verification_url)
