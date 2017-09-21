from subprocess import Popen
from fman import DirectoryPaneCommand

class UnmountVolume(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			Popen('diskutil unmount "%s"' % file_under_cursor, shell=True)
