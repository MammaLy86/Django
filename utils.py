from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin
def SendOtpCode(phone_number, code):
    try:
        api = KavenegarAPI('70345A344F365953614C33307577626F5639472F6174796A444B34482F4330615676456F514737745438773D')
        params = {
            'sender': '2000660110', # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'{code} کد تایید',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


class InAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.user.is_admin