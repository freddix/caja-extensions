Summary:	Caja extensions
Name:		caja-extensions
Version:	1.8.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	bc56df2c6b0445b574040222b40813bd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	caja-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mate-desktop-devel
BuildRequires:	pkg-config
Requires:	caja
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of extensions for Caja.

%package -n caja-extension-sendto
Summary:	Caja "sendto" extension
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,postun):	glib-gio-gsettings

%description -n caja-extension-sendto
Caja "sendto" extension.

%package -n caja-extension-image-converter
Summary:	Caja "image converter" extension
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick-coders

%description -n caja-extension-image-converter
Caja "image converter" extension.

%package -n caja-extension-open-terminal
Summary:	Caja "open terminal" extension
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,postun):	glib-gio-gsettings

%description -n caja-extension-open-terminal
Caja "open terminal" extension.

%package -n caja-extension-gksu
Summary:	Caja "gksu" extension
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description -n caja-extension-gksu
Caja "gksu" extension.

%package -n caja-extension-share
Summary:	Caja "share" extension
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description -n caja-extension-share
Caja "share" extension.

%prep
%setup -q

# kill mate common deps
%{__sed} -i -e '/MATE_COMPILE_WARNINGS.*/d'	\
    -i -e '/MATE_MAINTAINER_MODE_DEFINES/d'	\
    -i -e '/MATE_COMMON_INIT/d'			\
    -i -e '/MATE_CXX_WARNINGS.*/d'		\
    -i -e '/MATE_DEBUG_CHECK/d' configure.ac

%build
%{__libtoolize}
%{__intltoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*/*/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/MateConf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n caja-extension-sendto
%update_gsettings_cache

%postun -n caja-extension-sendto
%update_gsettings_cache

%post -n caja-extension-open-terminal
%update_gsettings_cache

%postun -n caja-extension-open-terminal
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog

%files -n caja-extension-sendto
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstburn.so
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstemailclient.so
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstgajim.so
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstpidgin.so
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstupnp.so
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-extensions/caja-sendto.ui
%{_mandir}/man1/caja-sendto.1*

%files -n caja-extension-image-converter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui

%files -n caja-extension-open-terminal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

%files -n caja-extension-gksu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-gksu.so

%files -n caja-extension-share
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui

