



all: build

link:
	install -d ~/bin
	ln -sf ${PWD}/fp-build ~/bin/
	ln -sf ${PWD}/fp-ccache ~/bin/
	ln -sf ${PWD}/fp-close-branch ~/bin/
	ln -sf ${PWD}/fp-deprecate ~/bin/
	ln -sf ${PWD}/fp-distclean ~/bin/
	ln -sf ${PWD}/fp-list ~/bin/
	ln -sf ${PWD}/fp-2008 ~/bin/
	ln -sf ${PWD}/fp-2108 ~/bin/
	ln -sf ${PWD}/fp-2208 ~/bin/

build:
	test -f flatpak-manifest-generator/Cargo.toml
	cd flatpak-manifest-generator && cargo build --release

install: link build
	install -Dm755 flatpak-manifest-generator/target/release/flatpak-manifest-generator -t ${HOME}/bin/
