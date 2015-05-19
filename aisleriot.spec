Summary:	A collection of card games
Summary(pl.UTF-8):	Kolekcja gier karcianych
Name:		aisleriot
Version:	3.16.2
Release:	1
License:	GPL v3+ and LGPL v3+ and GFDL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/aisleriot/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	00a71ccef4df729178b56353453fbbcd
URL:		https://wiki.gnome.org/Apps/Aisleriot
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	itstool
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig >= 1:0.15
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools >= 3.2.0
Requires(post,preun):	GConf2
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.0
Requires:	guile >= 5:2.0
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
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
bash %configure \
	--disable-silent-rules \
	--with-pysol-card-theme-path=%{_datadir}/pysol \
	--with-guile="2.0"
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/sol
%dir %{_libdir}/aisleriot
%attr(755,root,root) %{_libdir}/aisleriot/ar-cards-renderer
%{_libdir}/aisleriot/guile
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/aisleriot
%{_datadir}/appdata/sol.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_desktopdir}/sol.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-aisleriot.png
%{_iconsdir}/hicolor/*x*/apps/gnome-freecell.png
%{_iconsdir}/hicolor/symbolic/apps/gnome-aisleriot-symbolic.svg
%{_mandir}/man6/sol.6*

%files -n valgrind-aisleriot
%defattr(644,root,root,755)
%{_libdir}/valgrind/aisleriot.supp
