



class Manifest:
    """ The flatpak manifest """
    def __init__(self, manifest):
        self.manifest = manifest

    def id(self):
        """ Return the id. It can be from "id" or "app-id" """
        if "id" in self.manifest:
            return self.manifest["id"]
        if "app-id" in self.manifest:
            return self.manifest["app-id"]

    def is_extension(self):
        """ True if the manifest is for an extension  """
        try:
            return self.manifest["build-extension"]
        except:
            return False

    def branch(self):
        """ the branch string """
        try:
            return self.manifest["branch"]
        except:
            return None

    def command(self):
        """ command string """
        try:
            return self.manifest["command"]
        except:
            return None

    def finish_args(self):
        try:
            return self.manifest["finish-args"]
        except:
            return []

    def modules(self):
        try:
            return self.manifest["modules"]
        except:
            return None
