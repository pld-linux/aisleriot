#
# Conditional build:
%bcond_with	qt	# Support for QtSvg based formats (kde,native)
#
Summary:	A collection of card games
Summary(pl.UTF-8):	Kolekcja gier karcianych
Name:		aisleriot
Version:	3.22.26
Release:	1
License:	GPL v3+ and LGPL v3+ and GFDL
Group:		X11/Applications/Games
Source0:	https://gitlab.gnome.org/GNOME/aisleriot/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	77f03df941fe9236652e68a9d79490d7
URL:		https://wiki.gnome.org/Apps/Aisleriot
%{?with_qt:BuildRequires:	Qt5Svg-devel >= 5.0.0}
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	guile-devel >= 5:2.2
BuildRequires:	itstool
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-progs
BuildRequires:	lsb-release
BuildRequires:	pkgconfig >= 1:0.15
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	tar >= 1:1.22
BuildRequires:	yelp-tools >= 3.2.0
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.18.0
Requires:	guile >= 5:2.2
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-sol = %{version}
Obsoletes:	gnome-games-sol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aisleriot (also known as Solitaire or sol) is a collection of card
games which are easy to play with the aid of a mouse. The rules for
the games have been coded for your pleasure in the GNOME scripting
language (Scheme).

%description -l pl.UTF-8
Aisleriot (znany także jako Pasjans, Solitaire lub sol) to kolekcja
gier karcianych, łatwych do rozgrywania przy pomocy myszy. Zasady gier
zostały zakodowane w języku skryptowym GNOME (Scheme).

%package -n valgrind-aisleriot
Summary:	Aisleriot support for Valgrind
Summary(pl.UTF-8):	Obsługa Aisleriota dla Valgrinda
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	valgrind

%description -n valgrind-aisleriot
Aisleriot support for Valgrind.

%description -n valgrind-aisleriot -l pl.UTF-8
Obsługa Aisleriota dla Valgrinda.

%prep
%setup -q

%build
%{__meson} build \
	-Dtheme_kde=false \
	%{?with_qt:-Dtheme_svg_qtsvg=true -Dtheme_kde=true -Dtheme_kde_path=%{_datadir}/apps/carddecks} \
	-Dtheme_pysol=true \
	-Dtheme_pysol_path=%{_datadir}/pysol \
	-Dprefix=/usr \
	-Dlibdir=%{_libdir} \
	-Dbuildtype=debugoptimized

cd build
%{ninja_build}

%install
rm -rf $RPM_BUILD_ROOT
cd  build
%{ninja_install}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache HighContrast
%update_icon_cache hicolor
%gconf_schema_install aisleriot.schemas
%glib_compile_schemas

%preun
%gconf_schema_uninstall aisleriot.schemas

%postun
%update_icon_cache HighContrast
%update_icon_cache hicolor
%glib_compile_schemas

%files -f build/%{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/sol
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/aisleriot
%endif
%attr(755,root,root) %{_libexecdir}/aisleriot/ar-cards-renderer
%dir %{_libdir}/aisleriot
%{_libdir}/aisleriot/guile
%{_datadir}/aisleriot
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_datadir}/metainfo/sol.metainfo.xml
%{_desktopdir}/sol.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-aisleriot.png
%{_iconsdir}/hicolor/*x*/apps/gnome-freecell.png
%{_iconsdir}/hicolor/symbolic/apps/gnome-aisleriot-symbolic.svg
%{_mandir}/man6/sol.6*

%files -n valgrind-aisleriot
%defattr(644,root,root,755)
%{_libdir}/valgrind/aisleriot.supp
