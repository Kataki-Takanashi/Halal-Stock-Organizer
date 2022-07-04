"""

.. autoclass:: StatusSource
   :members:
   :undoc-members:

.. autoclass:: StatusTreeSource
   :members:
   :undoc-members:

.. autoclass:: ThreadedTreeSource
   :members:
   :undoc-members:

.. autoclass:: ThreadedTreeSource
   :members:
   :undoc-members:

.. autoclass:: HTTPStatusSource
   :members:
   :undoc-members:

.. autoclass:: GitHubStatusSource
   :members:
   :undoc-members:

"""

from up.util import NAME_SEPARATOR
from urllib.request import build_opener, Request
from urllib.error import HTTPError, URLError
from http.client import BadStatusLine, IncompleteRead
from pysnmp.entity.rfc3413.oneliner import cmdgen
import io
import gzip
import json
import time
import threading

UP = 1
DOWN = 0


class InvalidNameError(Exception):
    pass


class StatusSource(object):
    """
    A base class for a status. All statuses should extend from this class.
    """
    def __init__(self, name):
        super(StatusSource, self).__init__()

        if name is not None and NAME_SEPARATOR in name:
            raise InvalidNameError('name contains invalid character "' + NAME_SEPARATOR + '"')

        self.name = name
        self.status = UP
        self.date = None
        self.duration = 0

    def timed_prepare(self):
        """
        Call prepare and record the amount of time it takes to finish.
        """
        self.date = time.time()
        self.prepare()
        self.duration = time.time() - self.date

    def prepare(self):
        """
        Abstract method, implementing classes should use this hook to poll the
        status and update `self.status`.
        """
        raise NotImplemented


class StatusTreeSource(StatusSource):
    """
    A tree source allows you to organize your statuses. It will allow you to see
    the combined status of all of the statuses underneath it.
    """
    def __init__(self, name, children=None):
        super(StatusTreeSource, self).__init__(name)

        # default arguments are evaulated a compile time and are references
        if not children:
            children = list()

        self.children = children

    def calculate(self):
        """
        Calculates the percentage of the children that are up.
        """
        total = 0

        for child in self.children:
            total += child.status

        if len(self.children) > 0:
            return total / len(self.children)

        return 0

    def prepare(self):
        """
        Calls `timed_prepare` on all of its children and sets its status to the
        percentage of children that are up.
        """

        for child in self.children:
            child.timed_prepare()

        self.status = self.calculate()


class ThreadedTreeSource(StatusTreeSource):
    """
    Similar to `StatusTreeSource`, `ThreadedTreeSource` runs all of the
    `timed_prepare` calls in parallel. This is useful for statuses that require
    network access.
    """

    def __threaded_prepare(self, source):
        source.timed_prepare()

    def prepare(self):
        threads = []

        for child in self.children:
            status_thread = threading.Thread(target=self.__threaded_prepare, args=(child,))
            status_thread.start()
            threads.append(status_thread)

        for thread in threads:
            thread.join()

        self.status = self.calculate()


class HTTPStatusSource(StatusSource):
    """
    Makes a request to a url and uses the HTTP status code to determine of the
    server is up.

    Redirects are followed before determining the status.If the status code is
    2xx the server is considered to be up. Status codes 4xx, 5xx, truncated
    connections, or otherwise mangled responses are considered down.

    You can also use this as a basis for parsed statuses.
    """
    def __init__(self, name, url):
        super(HTTPStatusSource, self).__init__(name)

        self.url = url
        self.request = Request(self.url)
        self.result = None

        self.request.add_header('Accept-encoding', 'gzip')

    def _get_result(self):
        # for thread safety
        opener = build_opener()
        status_connection = opener.open(self.request)
        data = status_connection.read()

        if status_connection.info().get('Content-Encoding') == 'gzip':
            buf = io.BytesIO(data)
            file_obj = gzip.GzipFile(fileobj=buf)
            data = file_obj.read()

        return data.decode('utf-8')

    def prepare(self):
        if not self.result:
            self.status = UP

            try:
                self.result = self._get_result()
            except (HTTPError, ConnectionError, URLError, BadStatusLine, IncompleteRead):
                self.status = DOWN


class GitHubStatusSource(HTTPStatusSource):
    """
    Using the `GitHub status api <https://status.github.com/>`_ you can retrieve
    the current status of GitHub.

    GitHub Statuses:
    Good maps to UP
    Minor maps to HALF UP
    Major maps to DOWN
    """
    def __init__(self, name='GitHub', url='https://status.github.com/api/status.json'):
        super(GitHubStatusSource, self).__init__(name, url)

    def prepare(self):
        super(GitHubStatusSource, self).prepare()

        self.status = DOWN

        self.result = json.loads(self.result)
        # TODO: Find something to do with 'last_updated' date.
        if self.result['status'] == 'good':
            self.status = UP
        elif self.result['status'] == 'minor':
            self.status = 0.5


class SNMPStatusSource(StatusSource):
    def __init__(self, name=None, domain=None, port=161):
        super(SNMPStatusSource, self).__init__(name)

        if domain is None:
            raise ValueError("domain must be specified.")

        self.domain = domain
        self.port = port
        self.commands = [
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((self.domain, self.port)),
            cmdgen.MibVariable('SNMPv2-MIB', 'sysName', 0)
        ]

    def prepare(self):
        cmdGen = cmdgen.CommandGenerator()

        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(*self.commands)

        # Check for errors and print out results
        if errorIndication:
            self.status = DOWN
            #print(errorIndication)
        else:
            if errorStatus:
                self.status = DOWN
                #print('%s at %s' % (
                #    errorStatus.prettyPrint(),
                #    errorIndex and varBinds[int(errorIndex)-1] or '?'
                #))
            else:
                if self.name is None:
                    # the first variable requested is the name
                    self.name = str(varBinds[0][1])

                #for name, val in varBinds:
                #    print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
