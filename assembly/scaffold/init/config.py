# -*- coding: utf-8 -*-
"""
Assembly: config.py

Class based config file, where each class is an environment:
ie: Dev = Development, Production=Production, ...

Assembly: Global Configuration

Global config shared by all applications

The method allow multiple configuration

By default, it is expecting the Dev and Prod, but you can add your class
which extends from BaseConfig

- Access in templates
You have the ability to access these config in your template
just use the global variable `config`
ie:
    {{ config.APPLICATION_NAME }}

"""

import os

# The root dir
ROOT_DIR = os.path.dirname(__file__)

# Data directory
DATA_DIR = os.path.join(ROOT_DIR, "_data")


class BaseConfig(object):
    """
    Base configuration

    """

    #: Site's name or Name of the application
    APPLICATION_NAME = "Assembly"

    #: The application url
    APPLICATION_URL = ""

    #: Version of application
    APPLICATION_VERSION = "0.0.1"

    #: Google Analytics ID
    GOOGLE_ANALYTICS_ID = ""

    #: Required to setup. This email will have SUPER USER role
    ADMIN_EMAIL = None

    #: The address to receive email when using the contact page
    CONTACT_EMAIL = None

    #: PAGINATION_PER_PAGE : Total entries to display per page
    PAGINATION_PER_PAGE = 20

    # MAX_CONTENT_LENGTH
    # If set to a value in bytes, Flask will reject incoming requests with a
    # content length greater than this by returning a 413 status code
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024

    # To remove whitespace off the HTML result
    COMPRESS_HTML = False

    # Data directory
    DATA_DIR = DATA_DIR

    #------------------- DATE FORMAT and TIMEZONE -------------
    # Arrow is used as date parser
    # from assembly import date
    # http://crsmithdev.com/arrow
    # To view tokens: http://crsmithdev.com/arrow/#tokens

    # Timezone to use when dealing with date. 
    # Example
    # date.now().to(config.get("TIMEZONE"))
    # Timezone
    TIMEZONE = "US/Eastern"

    # Date format
    # Dict of dates format
    # Example
    # date.now().format(config.get("DATE_FORMAT.default"))
    DATE_FORMAT = {
        "default": "MM/DD/YYYY",
        "date": "MM/DD/YYYY",
        "datetime": "MM/DD/YYYY hh:mm a",
        "time": "hh:mm a",
        "long_datetime": "dddd, MMMM D, YYYY hh:mm a",
    }

    #--------- AWS Credentials ----------
    #: AWS Credentials
    # AWS is used by lots of extensions
    # For: S3, SES Mailer, flask S3.

    # The AWS Access KEY
    AWS_ACCESS_KEY_ID = ""

    # Secret Key
    AWS_SECRET_ACCESS_KEY = ""

    # The bucket name for S3
    AWS_S3_BUCKET_NAME = ""

    # The default region name
    AWS_REGION_NAME = "us-east-1"


    #--------- DATABASES URL ----------

    #: DB_URL
    #: Assembly uses Active-Alchemy to work with DB 
    #: format: engine://USERNAME:PASSWORD@HOST:PORT/DB_NAME
    #: format: dialect+driver://USERNAME:PASSWORD@HOST:PORT/DB_NAME
    #: SQLite: sqlite:////foo.db
    #: SQLite in memory: sqlite://
    #: Postgresql: postgresql+pg8000://user:password@host:port/dbname
    #: MySQL: mysql+pymysql://user:password@host:port/dbname
    DB_URL = "sqlite:////%s/db.db" % DATA_DIR

    #: DB_REDIS_URL
    #: format: USERNAME:PASSWORD@HOST:PORT
    DB_REDIS_URL = None


    #--------- ASSETS DELIVERY ----------
    # ASSETS DELIVERY allows to serve static files from S3, Cloudfront or other CDN
    # The delivery method:
    #   - None: will use the local static files
    #   - S3: Will use AWS S3. By default it will use the bucket name set in AWS_S3_BUCKET_NAME
    #       When S3, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are required to upload files
    #   - CDN: To use a CDN. ASSETS_DELIVERY_DOMAIN need to have the CDN domain
    ASSETS_DELIVERY_METHOD = None

    # Set the base domain of the CDN
    ASSETS_DELIVERY_DOMAIN = None

    #--------- SESSION ----------
    #: SESSION
    #: Flask-KVSession is used to save the user's session
    #: Set the SESSION_URL by using these examples below to set KVSession
    #: To use local session, just set SESSION_URL to None
    #:
    #: Redis: redis://username:password@host:6379/db
    #: S3: s3://username:password@s3.aws.amazon.com/bucket
    #: Google Storage: google_storage://username:password@cloud.google.com/bucket
    #: SQL: postgresql://username:password@host:3306/db
    #:      mysql+pysql://username:password@host:3306/db
    #:      sqlite://
    #: Memcached: memcache://host:port
    #:
    SESSION_URL = None


    #--------- STORAGE ----------
    #: STORAGE
    #: Flask-Cloudy is used to save upload on S3, Google Storage,
    #: Cloudfiles, Azure Blobs, and Local storage
    #: When using local storage, they can be accessed via http://yoursite/files
    #:

    #: STORAGE_PROVIDER:
    # The provider to use. By default it's 'LOCAL'.
    # You can use:
    # LOCAL, S3, GOOGLE_STORAGE, AZURE_BLOBS, CLOUDFILES
    STORAGE_PROVIDER = "LOCAL"

    #: STORAGE_KEY
    # The storage key. Leave it blank if PROVIDER is LOCAL
    STORAGE_KEY = AWS_ACCESS_KEY_ID

    #: STORAGE_SECRET
    #: The storage secret key. Leave it blank if PROVIDER is LOCAL
    STORAGE_SECRET = AWS_SECRET_ACCESS_KEY

    #: STORAGE_REGION_NAME
    #: The region for the storage. Leave it blank if PROVIDER is LOCAL
    STORAGE_REGION_NAME = AWS_REGION_NAME

    #: STORAGE_CONTAINER
    #: The Bucket name (for S3, Google storage, Azure, cloudfile)
    #: or the directory name (LOCAL) to access
    STORAGE_CONTAINER = os.path.join(DATA_DIR, "uploads")

    #: STORAGE_SERVER
    #: Bool, to serve local file
    STORAGE_SERVER = True

    #: STORAGE_SERVER_URL
    #: The url suffix for local storage
    STORAGE_SERVER_URL = "files"

    #:STORAGE_UPLOAD_FILE_PROPS
    #: A convenient K/V properties for storage.upload to use when using `upload_file()`
    #: It contains common properties that can passed into the upload function
    #: ie: upload_file("profile-image", file)
    STORAGE_UPLOAD_FILE_PROPS = {
        # To upload regular images
        "image": {
            "extensions": ["jpg", "png", "gif", "jpeg"],
            "public": True
        },

        # To upload profile image
        "profile-image": {
            "prefix": "profile-image/",
            "extensions": ["jpg", "png", "gif", "jpeg"],
            "public": True
        }
    }

    #--------- MAIL ----------
    # To send emails
    #
    # from assembly import asm
    # asm.send_mail(to="user@email.com", subject="Hi", body="How are you?")
    #
    # OPTIONS
    #
    # AWS SES
    # To use AWS SES to send email
    #:
    #: - To use the default AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    #: set MAIL_URL = "ses://"
    #: * To use a different credential:
    #: set MAIL_URL = "ses://{access_key}:{secret_key}@{region}"
    #:
    #: *** uncomment if you are using SMTP instead
    # MAIL_URL = "ses://"

    # SMTP
    #: If you are using SMTP, it will use Flask-Mail
    #: The uri for the smtp connection. It will use Flask-Mail
    #: format: smtp://USERNAME:PASSWORD@HOST:PORT
    #: with sll -> smtp+ssl://USERNAME:PASSWORD@HOST:PORT
    #: with ssl and tls -> smtp+ssl+tls://USERNAME:PASSWORD@HOST:PORT
    #:
    #: *** comment out if you are using SMTP instead
    # MAIL_URL = "smtp+ssl://{username}:{password}@{host}:{port}"\
    #    .format(username="", password="", host="smtp.gmail.com", port=465)

    #: MAIL_SENDER - The sender of the email by default
    #: For SES, this email must be authorized
    MAIL_SENDER = ADMIN_EMAIL

    #: MAIL_REPLY_TO
    #: The email to reply to by default
    MAIL_REPLY_TO = ADMIN_EMAIL

    #: MAIL_TEMPLATES_DIR
    #: files based templates
    MAIL_TEMPLATES_DIR = os.path.join(DATA_DIR, 'mail-templates')

    #: MAIL_TEMPLATES_DICT
    #: dict based templates 
    # MAIL_TEMPLATES_DICT = {
    #     "welcome.txt": """
    #     {% block subject %}Welcome{% endblock %}
    #     {% block body %}Welcome to the site {{name}}?{% endblock %}        
    #     """
    # }

    #: MAIL_TEMPLATE_CONTEXT
    #: a dict of all context to pass to the email by default
    MAIL_TEMPLATE_CONTEXT = {
        "params": {
            "site_name": APPLICATION_NAME,
            "site_url": APPLICATION_URL
        }
    }


    #--------- CACHING ----------
    #: Flask-Cache is used to caching

    #: CACHE_TYPE
    #: The type of cache to use
    #: null, simple, redis, filesystem,
    CACHE_TYPE = "simple"

    #: CACHE_REDIS_URL
    #: If CHACHE_TYPE is 'redis', set the redis uri
    #: redis://username:password@host:port/db
    CACHE_REDIS_URL = ""

    #: CACHE_DIR
    #: Directory to store cache if CACHE_TYPE is filesystem, it will
    CACHE_DIR = ""

    #--------- SWAGGER ----------
    #: Flassger is used to render Swagger Docs
    
    #: SWAGGER_TITLE
    #: Name of the Application
    SWAGGER_TITLE = "Assembly"

    #: SWAGGER_UI_VERSION
    #: The type of Swagger UI to render
    #: 2 or 3 default: 3
    SWAGGER_UI_VERSION = "3"


# -------------------------- ENVIRONMENT BASED CONFIG ---------------------------
"""
The environment based config is what will be loaded.
By default it will load the development

## 1. Set environment variables
export ASSEMBLY_ENV=Development # for development
export ASSEMBLY_APP=default  

## 2. Run the wsgi
wsgi:app


### **for development server
asm-admin serve

"""

class Development(BaseConfig):
    """ Config for development environment """
    SERVER_NAME = None
    DEBUG = True
    SECRET_KEY = "PLEASE CHANGE ME"


class Production(BaseConfig):
    """ Config for Production environment """
    SERVER_NAME = None
    DEBUG = False
    SECRET_KEY = None
    COMPRESS_HTML = True
