Summary:	LV2 port of the MCP, VCO, FIL, and WAH plugins
Summary(pl.UTF-8):	Port LV2 wtyczek MCP, VCO, FIL i WAH
Name:		fomp
Version:	1.2.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	15d51621e0811bab8cdad0f811e8fcf3
URL:		http://drobilla.net/software/fomp/
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	lv2-devel >= 1.16.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	lv2 >= 1.16.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%dir %{_libdir}/lv2/fomp.lv2
%attr(755,root,root) %{_libdir}/lv2/fomp.lv2/*.so
%{_libdir}/lv2/fomp.lv2/*.ttl
