



all: build

link:
	install -d ~/bin
	ln -sf ${PWD}/scripts/fp-build ~/bin/
	ln -sf ${PWD}/scripts/fp-nobackup ~/bin/
	ln -sf ${PWD}/scripts/fp-ccache ~/bin/
	ln -sf ${PWD}/scripts/fp-close-branch ~/bin/
	ln -sf ${PWD}/scripts/fp-deprecate ~/bin/
	ln -sf ${PWD}/scripts/fp-distclean ~/bin/
	ln -sf ${PWD}/scripts/fp-download ~/bin/
	ln -sf ${PWD}/scripts/fp-list ~/bin/
	ln -sf ${PWD}/scripts/fp-2308 ~/bin/

build:
	test -f flatpak-manifest-generator/Cargo.toml
	cd flatpak-manifest-generator && cargo build --release

install: link build
	install -Dm755 flatpak-manifest-generator/target/release/flatpak-manifest-generator -t ${HOME}/bin/
