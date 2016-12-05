# -*- coding: utf-8 -*-
"""The verification user Handler."""

from user import User, UserHandler


class VerificateUserHandler(UserHandler):
    """Email Verification page."""

    def get(self, *args, **kwargs):
        """Validate user email address."""
        user = None
        user_id = kwargs['user_id']
        signup_token = kwargs['token']
        verification_type = kwargs['operation']
        # it should be something more concise like
        # self.auth.get_user_by_token(user_id, signup_token)
        # unfortunately the auth interface does not (yet) allow to manipulate
        # signup tokens concisely
        user, ts = User.get_by_auth_token(int(user_id), signup_token, 'signup')
        if not user:
            self.abort(404)

        # store user data in the session
        self.auth.set_session(
            self.auth.store.user_to_dict(user), remember=True)

        if verification_type == 'v':
            # remove signup token, we don't want users to come back with an old
            # link
            User.delete_signup_token(user.get_id(), signup_token)
        if not user.verified:
            user.verified = True
            user.put()
            self.flash('Great %s you can now enjoy the blog.' %
                       user.name, 'success')
            self.redirect(self.uri_for('blog'))
            return
        elif verification_type == 'p':
            # supply user to the page
            params = {
                'user': user,
                'token': signup_token
            }
            self.render_template('resetpassword.html', params)
        else:
            self.abort(404)
