Summary:	LV2 port of the MCP, VCO, FIL, and WAH plugins
Summary(pl.UTF-8):	Port LV2 wtyczek MCP, VCO, FIL i WAH
Name:		fomp
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	5f9c52c5b954ddf37c7af7f31adcc0ff
URL:		http://drobilla.net/software/fomp/
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	python
Requires:	lv2 >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FOMP is an LV2 port of the MCP, VCO, FIL, and WAH plugins by Fons
Adriaensen.

There are 13 plugins in total: 1 auto-wah, 1 EQ, 3 chorus, 5 filters,
and 3 oscillators.

%description -l pl.UTF-8
FOMP to port LV2 wtyczek MCP, VCO, FIL oraz WAH, napisanych przez
Fonsa Adriaensena.

W sumie jest 13 wtyczek: 1 auto-wah, 1 EQ, 3 chóry, 5 filtrów, 3
generatory.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%dir %{_libdir}/lv2/fomp.lv2
%attr(755,root,root) %{_libdir}/lv2/fomp.lv2/*.so
%{_libdir}/lv2/fomp.lv2/*.ttl
