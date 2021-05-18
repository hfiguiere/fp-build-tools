


all:
	install -Dm755 fp-build ${HOME}/bin/fp-build
	install -Dm755 fp-list ${HOME}/bin/fp-list
	install -Dm755 fp-ccache ${HOME}/bin/fp-ccache
	install -Dm755 fp-distclean ${HOME}/bin/fp-distclean

