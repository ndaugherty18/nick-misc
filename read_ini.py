import ConfigParser

ini_file = '/home/nick/projects/tldr-mediabuyer/uwsgi.ini'
config = ConfigParser.RawConfigParser()
config.read(ini_file)
version = config.get('uwsgi', 'version')
version = version.split('.')
last_digit = int(version[len(version)-1]) + 1
version[len(version)-1] = str(last_digit)
version = '.'.join(version)
config.set('uwsgi', 'version', version)
config.write(open(ini_file, 'wb'))
