Summary:	A library for creating and verifying cancel locks
Summary(pl.UTF-8):	Biblioteka do tworzenia i weryfikowania cancel-locków
Name:		libcanlock
Version:	3.3.0
Release:	1
License:	MIT-like, BSD-like
Group:		Libraries
Source0:	https://micha.freeshell.org/libcanlock/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e1de8ff736867d24c5e1ba2fc02f0ad7
URL:		https://micha.freeshell.org/libcanlock/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for creating and verifying cancel locks (special news
articles headers that prevent cancelling articles by unauthorized
persons).

%description -l pl.UTF-8
Biblioteka do tworzenia i weryfikowania cancel-locków (specjalnych
nagłówków artykułów newsowych zapobiegających usuwaniu artykułów przez
osoby nieuprawnione).

%package devel
Summary:	Header files for canlock library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki canlock
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	canlock-devel < 3

%description devel
Header files for canlock library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki canlock.

%package static
Summary:	Static canlock library
Summary(pl.UTF-8):	Statyczna biblioteka canlock
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	canlock-static < 3

%description static
Static canlock library.

%description static -l pl.UTF-8
Statyczna biblioteka canlock.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcanlock*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog ChangeLog_V[012] README
%attr(755,root,root) %{_bindir}/canlock
%attr(755,root,root) %{_bindir}/canlock-hfp
%attr(755,root,root) %{_bindir}/canlock-mhp
%attr(755,root,root) %{_libdir}/libcanlock.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanlock.so.3
%attr(755,root,root) %{_libdir}/libcanlock-hp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanlock-hp.so.3
%{_mandir}/man1/canlock.1*
%{_mandir}/man1/canlock-hfp.1*
%{_mandir}/man1/canlock-mhp.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanlock.so
%attr(755,root,root) %{_libdir}/libcanlock-hp.so
%{_includedir}/libcanlock-3
%{_mandir}/man3/cl_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcanlock.a
%{_libdir}/libcanlock-hp.a
