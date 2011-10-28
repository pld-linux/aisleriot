Summary:	A collection of card games
Name:		aisleriot
Version:	3.2.1
Release:	1
License:	GPL v3+ and LGPL v3+ and GFDL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/aisleriot/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	e25a6df872ed1593b1d590561e3e91fb
URL:		http://live.gnome.org/Aisleriot
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools >= 3.2.0
Requires(post,preun):	GConf2
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	guile >= 5:2.0
Requires:	hicolor-icon-theme
Provides:	gnome-games-sol = %{version}
Obsoletes:	gnome-games-sol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aisleriot (also known as Solitaire or sol) is a collection of card
games which are easy to play with the aid of a mouse. The rules for
the games have been coded for your pleasure in the GNOME scripting
language (Scheme).

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
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
%update_icon_cache hicolor
%gconf_schema_install aisleriot.schemas
%glib_compile_schemas

%preun
%gconf_schema_uninstall aisleriot.schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/sol
%dir %{_libdir}/aisleriot
%attr(755,root,root) %{_libdir}/aisleriot/ar-cards-renderer
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/aisleriot
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_desktopdir}/freecell.desktop
%{_desktopdir}/sol.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man6/sol.6*
