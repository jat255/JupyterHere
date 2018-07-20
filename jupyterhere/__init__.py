from fman import DirectoryPaneCommand
import subprocess
import os


class JupyterHere(DirectoryPaneCommand):
    def __call__(self):
        cd = self.pane.get_path()

        # Clean path if running on Windows
        if os.path == 'nt':
            cd = cd.lstrip('file:/').rstrip('\\')

        subprocess.call(r'jupyter-notebook ' +
        				r'--notebook-dir="{}"'.format(cd))
