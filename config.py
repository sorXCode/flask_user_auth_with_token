import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    SECRET_KEY = "HGTO6rmUxIC_4maze8TIj54BPJ7IRb--Awsz_1oSELs"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class Test(Config):
    # Add a secret key for testing
    SECRET_KEY = "fca409881de74c0900c06066b946bd6dc324f193f0f9fbcd508316fd73db3d6b"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test_db.sqlite')



config = {
    'development': Development,
    'test': Test,
    'default': Development
}