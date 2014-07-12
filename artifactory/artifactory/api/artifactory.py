"""
artifactory.py
"""
from requests import get
from urlparse import urljoin
from logging import debug

from ..util.logger_init import initialize_logger_console

class Artifactory(object):
    """
    The Artifactory class wrapper for the Artifactor API calls
    """

    def __init__(self, hostname, user, password):

        initialize_logger_console()

        self.base_url = "http://{}".format(hostname)
        self.user = user
        self.password = password


    def get_users(self):
        """
        Get the users list in Artifactory

        http://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUsers
        """
        api_call = "api/security/users"

        url = urljoin(self.base_url, api_call)

        request = get(url, auth=(self.user, self.password))

        debug("http response.url: {}".format(request.url))
        debug("http response.status_code: {}".format(request.status_code))
        debug("text response returned: {}".format(request.text))