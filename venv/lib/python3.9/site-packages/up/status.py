"""

.. autoclass:: StatusMonitor
   :members:
   :undoc-members:


"""

from up import annotation
from up.moods import moods
from argparse import ArgumentParser
import sys
import os.path


class StatusMonitor(object):
    """
    A status monitor. Inherit from this class to create your own.
    """
    source = None
    sink = None

    def main(self, note, mood, verbosity):

        self.sink.set_verbosity(verbosity)
        self.sink.set_mood(mood)

        if note:
            self.sink.add_annotation(note)

        self.source.timed_prepare()

        self.sink.set_status(self.source)


def load_config():
    sys.path.insert(0, os.getcwd())
    __import__('upfile')
    sys.path.pop(0)

    return StatusMonitor.__subclasses__()


def main():
    parser = ArgumentParser(description='Is it up yet?')
    parser.add_argument('--note', type=str, help='Record a note with this status.')
    parser.add_argument('--verbose', '-v', default=0, action='count', help='Control the amount of information written to the terminal. Use more v\'s to specify how much.')
    parser.add_argument('--realist', dest='mood', action='store_const', const=moods.REALIST, help='Adujust messaging for ordinary people. The default.')
    parser.add_argument('--optimist', dest='mood', action='store_const', const=moods.OPTIMIST, help='Adujust messaging for happy people.')
    parser.add_argument('--pessimist', dest='mood', action='store_const', const=moods.PESSIMIST, help='Adujust messaging for unhappy people.')

    args = parser.parse_args()
    note = None

    config = load_config()

    status_monitor = config[0]()

    if args.note:
        note = annotation.Annotation(args.note)

    exit(status_monitor.main(note, args.mood or moods.REALIST, args.verbose))
