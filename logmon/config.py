'''
    logmon.config
    -------------

    Flask configuration.
'''


class Config(object):
    SITE_NAME = 'Logmon'
    SITE_DOMAIN = 'localhost'
    
    # indicates the file to watch
    #LOG_FILE = '/var/log/nginx/access.log'
    # For your Rails app, feel free change it to your production.log or development.log
    #LOG_FILE = '/www/fosun/log/development.log'
    LOG_FILE = '/var/rails/fosun/current/log/production.log'