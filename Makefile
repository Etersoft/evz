
pkgdatadir=$(datadir)/evz
# due using %makeinstallstd in spec
instpkgdatadir=/usr/share/evz

install:
	mkdir -p $(DESTDIR)$(bindir)/
	# breaks link
	#install -m 755 `ls -1 bin/* | grep -v "-"` $(DESTDIR)$(bindir)/
	cp -a `ls -1 bin/* | grep -v "-"` $(DESTDIR)$(bindir)/
	chmod 0755 $(DESTDIR)$(bindir)/*

	# hack to replace path
	sed -e "s|SHAREDIR=.*|SHAREDIR=$(instpkgdatadir)|g" -e "s|@VERSION@|$(version)|g" <bin/evz >$(DESTDIR)$(bindir)/evz

	mkdir -p $(DESTDIR)$(pkgdatadir)/
	install -m 644 `ls -1 bin/* | grep "-"` $(DESTDIR)$(pkgdatadir)/

	mkdir -p $(DESTDIR)$(mandir)/man8
	cp -a `ls -1 man/*` $(DESTDIR)$(mandir)/man8/
