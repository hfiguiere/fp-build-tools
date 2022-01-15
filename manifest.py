



class Manifest:
    """ The flatpak manifest """
    def __init__(self, manifest):
        self.manifest = manifest

    def id(self):
        return self.manifest["id"]
