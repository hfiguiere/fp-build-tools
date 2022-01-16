

class Linter:

    def __init__(self, m):
        self.m = m

    def lint(self):
        """ Lint the manifest m """
        print("Linting app: {}".format(self.m.id()))

        lints = self.rules()
        return lints

    def source_rules(self, source):
        """ Rules for sources """
        pass

    def module_rules(self, module):
        """ Rules for modules """
        name = module["name"]
        lints = []
        if "buildsystem" not in module:
            buildsystem = "autotools"
        else:
            buildsystem = module["buildsystem"]

        # We prefer cmake-ninja
        # TODO figure out how to make this explicit. (ie ignorable)
        if buildsystem == "cmake":
            lints.append("module '{}': cmake-ninja is preferred".format(name))
        if buildsystem == "cmake" or buildsystem == "cmake-ninja":
            if "config-opts" in module:
                for opt in module["config-opts"]:
                    if opt.startswith("-DCMAKE_INSTALL_PREFIX="):
                        lints.append("module '{}': redundant config option {}".format(name, opt))
        elif buildsystem == "autotools":
            if "config-opts" in module:
                for opt in module["config-opts"]:
                    if opt.startswith("--prefix="):
                        lints.append("module '{}': redundant config option {}".format(name, opt))
        # XXX missing meson, qmake and simple

        return lints

    def rules(self):
        lints = []

        # Branch
        branch = self.m.branch()
        if branch == "master" or branch == "stable":
            lints.append("manifest: Shouldn't have a 'branch' set. Remove it.");

        # Command
        if self.m.is_extension() and self.m.command() is not None:
            lints.append("manifest: command shouldn't be set for an extension")
        elif not self.m.is_extension():
            if self.m.command() is None:
                lints.append("manifest: no command set")
            elif self.m.command().startswith("/"):
                lints.append("manifest: command should not be a path")

        # Check finish args.
        finish_args = self.m.finish_args()
        if self.m.is_extension():
            # No finish args on extensions
            pass
        elif len(finish_args) == 0:
            lints.append("manifest: No finish args")
        else:
            # Check sockets
            has_x11 = "--socket=x11" in finish_args
            has_fallback_x11 = "--socket=fallback-x11" in finish_args
            has_wayland = "--socket=wayland" in finish_args
            has_ipc = "--share=ipc" in finish_args

            if has_x11 and has_fallback_x11:
                lints.append("socket: x11 and fallback-x11 shouldn't be use simultaneously")
            if has_x11 and has_wayland:
                lints.append("socket: fallback-x11 is preferred when using wayland")
            if has_x11 and not(has_x11 or has_fallback_x11):
                lints.append("socket: no X11 fallback")
            if (has_x11 or has_fallback_x11) and not has_ipc:
                lints.append("socket: IPC ar needed for X11 (and fallback)")

        # modules
        modules = self.m.modules()
        if modules is None or len(modules) == 0:
            lints.append("manifest: No modules")
        else:
            for module in modules:
                if type(module) is str:
                    # XXX Recursively check the modules manifest
                    # XXX Currently skip it
                    continue
                lints.extend(self.module_rules(module))

        return lints
