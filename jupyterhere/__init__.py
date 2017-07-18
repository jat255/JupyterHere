from fman import DirectoryPaneCommand
import subprocess

class JupyterHere(DirectoryPaneCommand):
    def __call__(self):
        subprocess.call(r'jupyter-notebook ' + 
        				r'--notebook-dir="{cd}"'.format(cd=self.pane.get_path()))
