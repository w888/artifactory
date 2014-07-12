from os.path import dirname, join
import ConfigParser

from logging import debug


def read_config(filename):
    """
    Read artifactory config file
    """
    tmpconfig = ConfigParser.ConfigParser()

    filepath = join(dirname(__file__), "{}.cfg".format(filename))
    debug("filename= {}".format(filepath))

    with open(filepath) as file:
        tmpconfig.readfp(file)

    hostname = tmpconfig.get("artifactory", "hostname")
    debug("hostname= {}".format(hostname))

    user = tmpconfig.get("artifactory", "user")
    debug("user= {}".format(user))

    password = tmpconfig.get("artifactory", "password")
    debug("password= {}".format(password))

    config = {}

    for section in tmpconfig.sections():
        config[section] = {}
        for option in tmpconfig.options(section):
            config[section][option] = tmpconfig.get(section, option)

    debug("config= {}".format(config))

    return (hostname, user, password)