from django import forms
from django_recaptcha.fields import ReCaptchaField,ReCaptchaV2Checkbox
from allauth.account.forms import LoginForm
class AllAuthSignupForm(forms.Form):

    captcha = ReCaptchaV2Checkbox()
    captcha = ReCaptchaField(
    public_key='6LciX1YqAAAAAEabHig-jxTlRgbEweRaqKim0acy',
    private_key='6LciX1YqAAAAAIyBa5iwPgcN3V_B9IQ1L19-khCw',
)
    def signup(self, request, user):
        pass
class AllAuthLoginForm(LoginForm):

    captcha = ReCaptchaV2Checkbox()
    captcha = ReCaptchaField(
    public_key='6LciX1YqAAAAAEabHig-jxTlRgbEweRaqKim0acy',
    private_key='6LciX1YqAAAAAIyBa5iwPgcN3V_B9IQ1L19-khCw',
)
    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(AllAuthLoginForm, self).login(*args, **kwargs)