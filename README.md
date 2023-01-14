A set of tools for flatpak building. Just some wrappers.

These commands assume that:

1. the package directory is the same as the package ID.
2. the package manifest in that directory is the package ID with the right extension.
3. that you are in that package directory.



- fp-build: simply build the package and install it locally. You can
  pass more options to flatpak-builder.
  It will also validate the AppStream file and the flatpak-external-data-checker

- fp-list: `flatpak list` with some different display options

- fp-ccache: Use ccache on the flatpak builder cache for the
  package. Pass the usual ccache options

- fp-distclean: Clear the repo and the cache for the package.


To install:

Type `make`. The commands will be installed in `~/bin`.
