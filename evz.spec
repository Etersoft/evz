Name: evz
Version: 0.0.2
Release: alt1

Summary: OpenVZ control tool

License: AGPLv3
Group: System/Configuration/Packaging
Url: https://github.com/Etersoft/evz

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/evz.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

%description
EVZ is implemented as wrapper around vzctl with accent to group operations on containers.

See detailed description in russian here: http://wiki.etersoft.ru/EVZ

%prep
%setup

%install
# install to datadir and so on
%makeinstall version=%version-%release

install -D -m 0644 bash_completion/evz %buildroot%_sysconfdir/bash_completion.d/evz

# shebang.req.files
#chmod a+x %buildroot%_datadir/%name/{erc-}*

%files
#doc README LICENSE TODO
%_sbindir/evz
#_datadir/%name/
%_man8dir/*
%_sysconfdir/bash_completion.d/evz

%changelog
* Wed Nov 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt1
- evz: add list, exec

* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus