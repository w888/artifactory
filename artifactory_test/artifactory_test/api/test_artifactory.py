from logging import debug

from artifactory.artifactory.config.config import read_config
from artifactory.artifactory.api.artifactory import Artifactory


class TestArtifactory(object):
    def __init__(self):
        (hostname, user, password) = read_config("admin")

        debug("Artifactory config: hostname={}, user={}, password={}"
              .format(hostname, user, password))

        self.artifactory = Artifactory(hostname=hostname, user=user, password=password)

    def test_config(self):
        """
        test reading config file for user= admin
        """
        conf = read_config("admin")
        debug("config= {}".format(conf))

    def test_get_users(self):
        """

        """
        self.artifactory.get_users()
