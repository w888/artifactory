"""
artifactory.py
"""
from requests import get
from urlparse import urljoin
from logging import debug

from ..util.logger_init import initialize_logger_console
from ..util.util import debug_print

class Artifactory(object):
    """
    The Artifactory class wrapper for the Artifactor API calls
    """

    def __init__(self, hostname, user, password):

        initialize_logger_console()

        self.base_url = "http://{}".format(hostname)
        self.user = user
        self.password = password

    def all_builds(self):
        """
        Provides information on all builds

        http://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-AllBuilds
        """
        api_call = "api/build"

        url = urljoin(self.base_url, api_call)

        request = get(url, auth=(self.user, self.password))

        debug_print(request)

    def get_users(self):
        """
        Get the users list in Artifactory

        http://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUsers
        """
        api_call = "api/security/users"

        url = urljoin(self.base_url, api_call)

        request = get(url, auth=(self.user, self.password))

        debug_print(request)