#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-NetAddr-IP
Version  : 4.079
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnetaddr-ip-perl/libnetaddr-ip-perl_4.079+dfsg-1.debian.tar.xz
Summary  : Manages IPv4 and IPv6 addresses and subnets
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: perl-NetAddr-IP-data = %{version}-%{release}
Requires: perl-NetAddr-IP-lib = %{version}-%{release}
Requires: perl-NetAddr-IP-license = %{version}-%{release}
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

%package data
Summary: data components for the perl-NetAddr-IP package.
Group: Data

%description data
data components for the perl-NetAddr-IP package.


%package dev
Summary: dev components for the perl-NetAddr-IP package.
Group: Development
Requires: perl-NetAddr-IP-lib = %{version}-%{release}
Requires: perl-NetAddr-IP-data = %{version}-%{release}
Provides: perl-NetAddr-IP-devel = %{version}-%{release}

%description dev
dev components for the perl-NetAddr-IP package.


%package lib
Summary: lib components for the perl-NetAddr-IP package.
Group: Libraries
Requires: perl-NetAddr-IP-data = %{version}-%{release}
Requires: perl-NetAddr-IP-license = %{version}-%{release}

%description lib
lib components for the perl-NetAddr-IP package.


%package license
Summary: license components for the perl-NetAddr-IP package.
Group: Default

%description license
license components for the perl-NetAddr-IP package.


%prep
%setup -q -n NetAddr-IP-4.079
cd ..
%setup -q -T -D -n NetAddr-IP-4.079 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/NetAddr-IP-4.079/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-NetAddr-IP
cp Copying %{buildroot}/usr/share/package-licenses/perl-NetAddr-IP/Copying
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-NetAddr-IP/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/NetAddr/IP.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/NetAddr/IP/InetBase.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/NetAddr/IP/Lite.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/NetAddr/IP/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/NetAddr/IP/UtilPP.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/NetAddr/IP/Util_IS.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/_inet_ntop.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/_inet_pton.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/_packzeros.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/inet_any2n.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/inet_n2ad.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/inet_n2dx.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/inet_ntoa.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/ipv6_aton.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/InetBase/ipv6_ntoa.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/Util/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_128x10.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_128x2.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_bcd2bin.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_bcdcheck.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_bin2bcdn.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_deadlen.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/_sa128.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/add128.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/addconst.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/bcd2bin.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/bcdn2bin.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/bcdn2txt.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/bin2bcd.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/bin2bcdn.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/comp128.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/hasbits.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/ipanyto6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/ipv4to6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/ipv6to4.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/mask4to6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/maskanyto6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/notcontiguous.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/shiftleft.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/simple_pack.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/slowadd128.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/UtilPP/sub128.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/_compV6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/_compact_v6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/_splitplan.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/_splitref.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/canon.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/coalesce.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/compactref.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/do_prefix.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/hostenum.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/mod_version.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/nprefix.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/prefix.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/re.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/re6.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/short.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/wildcard.al

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-NetAddr-IP/Copying

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/NetAddr::IP.3
/usr/share/man/man3/NetAddr::IP::InetBase.3
/usr/share/man/man3/NetAddr::IP::Lite.3
/usr/share/man/man3/NetAddr::IP::Util.3
/usr/share/man/man3/NetAddr::IP::UtilPP.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/NetAddr/IP/Util/Util.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-NetAddr-IP/deblicense_copyright
