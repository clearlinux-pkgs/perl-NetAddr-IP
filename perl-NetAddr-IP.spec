#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-NetAddr-IP
Version  : 4.079
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnetaddr-ip-perl/libnetaddr-ip-perl_4.079+dfsg-1.debian.tar.xz
Summary  : Manages IPv4 and IPv6 addresses and subnets
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: perl-NetAddr-IP-license = %{version}-%{release}
Requires: perl-NetAddr-IP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
NetAddr::IP::Lite - Manages IPv4 and IPv6 addresses and subnets
SYNOPSIS
use NetAddr::IP::Lite qw(
Zeros
Ones
V4mask
V4net
:aton           DEPRECATED !
:old_nth
:upper
:lower
:nofqdn
);

%package dev
Summary: dev components for the perl-NetAddr-IP package.
Group: Development
Provides: perl-NetAddr-IP-devel = %{version}-%{release}
Requires: perl-NetAddr-IP = %{version}-%{release}

%description dev
dev components for the perl-NetAddr-IP package.


%package license
Summary: license components for the perl-NetAddr-IP package.
Group: Default

%description license
license components for the perl-NetAddr-IP package.


%package perl
Summary: perl components for the perl-NetAddr-IP package.
Group: Default
Requires: perl-NetAddr-IP = %{version}-%{release}

%description perl
perl components for the perl-NetAddr-IP package.


%prep
%setup -q -n NetAddr-IP-4.079
cd %{_builddir}
tar xf %{_sourcedir}/libnetaddr-ip-perl_4.079+dfsg-1.debian.tar.xz
cd %{_builddir}/NetAddr-IP-4.079
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/NetAddr-IP-4.079/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-NetAddr-IP
cp %{_builddir}/NetAddr-IP-4.079/Copying %{buildroot}/usr/share/package-licenses/perl-NetAddr-IP/d77a17ea0c8a78f0ad38dd3770fe2c5c833f6b79
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-NetAddr-IP/e4f5b7bd72bdc522a363aa269d88db2ebb0187c6
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/NetAddr::IP.3
/usr/share/man/man3/NetAddr::IP::InetBase.3
/usr/share/man/man3/NetAddr::IP::Lite.3
/usr/share/man/man3/NetAddr::IP::Util.3
/usr/share/man/man3/NetAddr::IP::UtilPP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-NetAddr-IP/d77a17ea0c8a78f0ad38dd3770fe2c5c833f6b79
/usr/share/package-licenses/perl-NetAddr-IP/e4f5b7bd72bdc522a363aa269d88db2ebb0187c6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
