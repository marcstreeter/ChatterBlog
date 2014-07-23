


class BaseConfig(object):
    # ~~~~~~~~~~FLASK SETTINGS~~~~~~~~~~FLASK SETTINGS~~~~~~~~~~FLASK SETTINGS~~~~~~~~~~FLASK SETTINGS
    SRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{psw}@{host}/{name}'.format(user='collegecat',
                                                                          host='localhost',
                                                                          psw='UrNotAG04t',
                                                                          name='collegecat')
    root_logger = "chatter."
    api_prefix = "/api/v1/"



