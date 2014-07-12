from logging import debug

from artifactory.artifactory.config.config import read_config
from artifactory.artifactory.api.artifactory import Artifactory


class TestArtifactory(object):
    def __init__(self):
        (hostname, user, password) = read_config("admin")

        debug("Artifactory config: hostname={}, user={}, password={}"
              .format(hostname, user, password))

        self.artifactory = Artifactory(hostname=hostname, user=user, password=password)

    def test_all_builds(self):
        """
        Successful call to all_builds()
        """
        self.artifactory.all_builds()

    def test_get_users(self):
        """
        Successful call to get_users()
        """
        self.artifactory.get_users()
