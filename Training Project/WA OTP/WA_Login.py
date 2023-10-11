import requests

jatis_url = 'https://interactive.jatismobile.com/wa/users/login'
jatis_username = 'puprpusat'
jatis_password = 'Puprkemen83@'
login = False

class Whatsapp_Login():
    def post(self):

        # if not current_user.ikh_user_id:
            # user_auth = default
        if login == False:
            r = requests.post(
                jatis_url,
                jatis_username,
                jatis_password
            )
            return r(), 200
        else:
            pass