%define		oname	wxWidgets
%define		api	%(echo %{version} |cut -d. -f1-2)
%define		major	%(echo %{version} |cut -d. -f3)

Summary:	Qt port of the wxWidgets library
Name:		wxqt%{api}
Version:	3.1.4
Release:	1
License:	wxWidgets Library Licence
Group:		System/Libraries
Url:		http://www.wxwidgets.org/
Source0:	https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/%{oname}-%{version}.tar.bz2
Patch0:		wxWidgets-3.0.0-locales.patch
Patch1:		wxQt-3.1.0-wxconfig-includes.patch
# abi check is useless as it reports different abi used between clang and gcc
# however clang just hard codes a def to an old abi version, its not actually
# a different abi
Patch2:		wxWidgets-3.0.2-disable_abi_check.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(cppunit)
# For wxGraphicsContext
BuildRequires:	pkgconfig(cairo)

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%files -f wxstd-%{api}.lang
%doc *.txt

#----------------------------------------------------------------------------

%define libwx_baseu %mklibname wx_baseu %{api} %{major}

%package -n	%{libwx_baseu}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu}
%{_libdir}/libwx_baseu-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_baseu_net %mklibname wx_baseu_net %{api} %{major}

%package -n	%{libwx_baseu_net}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu_net}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu_net}
%{_libdir}/libwx_baseu_net-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_baseu_xml %mklibname wx_baseu_xml %{api} %{major}

%package -n	%{libwx_baseu_xml}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu_xml}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu_xml}
%{_libdir}/libwx_baseu_xml-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_adv %mklibname wx_qtu_adv %{api} %{major}

%package -n	%{libwx_qtu_adv}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_adv}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_adv}
%{_libdir}/libwx_qtu_adv-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_aui %mklibname wx_qtu_aui %{api} %{major}

%package -n	%{libwx_qtu_aui}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_aui}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_aui}
%{_libdir}/libwx_qtu_aui-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_core %mklibname wx_qtu_core %{api} %{major}

%package -n	%{libwx_qtu_core}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_core}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_core}
%{_libdir}/libwx_qtu_core-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_gl %mklibname wx_qtu_gl %{api} %{major}

%package -n	%{libwx_qtu_gl}
Summary:	OpenGL shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_gl}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_gl}
%{_libdir}/libwx_qtu_gl-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_html %mklibname wx_qtu_html %{api} %{major}

%package -n	%{libwx_qtu_html}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_html}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_html}
%{_libdir}/libwx_qtu_html-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_media %mklibname wx_qtu_media %{api} %{major}

%package -n	%{libwx_qtu_media}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_media}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_media}
%{_libdir}/libwx_qtu_media-%{api}.so.%{major}*
%dir %{_libdir}/wx
%dir %{_libdir}/wx/%{version}
%{_libdir}/wx/%{version}/sound_sdlu-%{version}.so

#----------------------------------------------------------------------------

%define libwx_qtu_propgrid %mklibname wx_qtu_propgrid %{api} %{major}

%package -n	%{libwx_qtu_propgrid}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_propgrid}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_propgrid}
%{_libdir}/libwx_qtu_propgrid-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_qa %mklibname wx_qtu_qa %{api} %{major}

%package -n	%{libwx_qtu_qa}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_qa}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_qa}
%{_libdir}/libwx_qtu_qa-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_ribbon %mklibname wx_qtu_ribbon %{api} %{major}

%package -n	%{libwx_qtu_ribbon}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_ribbon}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_ribbon}
%{_libdir}/libwx_qtu_ribbon-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_richtext %mklibname wx_qtu_richtext %{api} %{major}

%package -n	%{libwx_qtu_richtext}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_richtext}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_richtext}
%{_libdir}/libwx_qtu_richtext-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_qtu_stc %mklibname wx_qtu_stc %{api} %{major}

%package -n	%{libwx_qtu_stc}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_stc}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_stc}
%{_libdir}/libwx_qtu_stc-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%if 0
%define libwx_qtu_webview %mklibname wx_qtu_webview %{api} %{major}

%package -n	%{libwx_qtu_webview}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_webview}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_webview}
%{_libdir}/libwx_qtu_webview-%{api}.so.%{major}*
%endif

#----------------------------------------------------------------------------

%define libwx_qtu_xrc %mklibname wx_qtu_xrc %{api} %{major}

%package -n	%{libwx_qtu_xrc}
Summary:	Shared library of wxQt - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_qtu_xrc}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (Qt, GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_qtu_xrc}
%{_libdir}/libwx_qtu_xrc-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libnameudev %mklibname -d wxqtu %{api}

%package -n	%{libnameudev}
Summary:	Header files and development documentation for wxQt - unicode
Group:		Development/C++
Requires:	%{libwx_baseu} = %{EVRD}
Requires:	%{libwx_baseu_net} = %{EVRD}
Requires:	%{libwx_baseu_xml} = %{EVRD}
Requires:	%{libwx_qtu_adv} = %{EVRD}
Requires:	%{libwx_qtu_aui} = %{EVRD}
Requires:	%{libwx_qtu_core} = %{EVRD}
Requires:	%{libwx_qtu_gl} = %{EVRD}
Requires:	%{libwx_qtu_html} = %{EVRD}
Requires:	%{libwx_qtu_media} = %{EVRD}
Requires:	%{libwx_qtu_propgrid} = %{EVRD}
Requires:	%{libwx_qtu_qa} = %{EVRD}
Requires:	%{libwx_qtu_ribbon} = %{EVRD}
Requires:	%{libwx_qtu_richtext} = %{EVRD}
Requires:	%{libwx_qtu_stc} = %{EVRD}
%if 0
Requires:	%{libwx_qtu_webview} = %{EVRD}
%endif
Requires:	%{libwx_qtu_xrc} = %{EVRD}
Provides:	wxqtu%{api}-devel = %{EVRD}
Requires:	pkgconfig(Qt5Core)
Requires:	pkgconfig(Qt5Gui)
Requires:	pkgconfig(Qt5Widgets)
Requires:	pkgconfig(Qt5OpenGL)
Requires:	pkgconfig(Qt5Test)

%description -n %{libnameudev}
Header files for the unicode enabled version of wxQt, the Qt port of
the wxWidgets library.

%files -n %{libnameudev}
%doc samples/
%doc docs/
%doc demos/
%{_bindir}/wx-config
%{_bindir}/wxrc
%{_bindir}/wxrc-%{api}
%{_includedir}/wx-%{api}/
%{_datadir}/aclocal/*
%{_datadir}/bakefile/
%{_libdir}/wx/config/qt-unicode-%{api}
%{_libdir}/wx/include/qt-unicode-%{api}/wx/setup.h
%{_libdir}/libwx_baseu-%{api}.so
%{_libdir}/libwx_baseu_net-%{api}.so
%{_libdir}/libwx_baseu_xml-%{api}.so
%{_libdir}/libwx_qtu_adv-%{api}.so
%{_libdir}/libwx_qtu_aui-%{api}.so
%{_libdir}/libwx_qtu_core-%{api}.so
%{_libdir}/libwx_qtu_gl-%{api}.so
%{_libdir}/libwx_qtu_html-%{api}.so
%{_libdir}/libwx_qtu_media-%{api}.so
%{_libdir}/libwx_qtu_propgrid-%{api}.so
%{_libdir}/libwx_qtu_qa-%{api}.so
%{_libdir}/libwx_qtu_ribbon-%{api}.so
%{_libdir}/libwx_qtu_richtext-%{api}.so
%{_libdir}/libwx_qtu_stc-%{api}.so
%if 0
%{_libdir}/libwx_qtu_webview-%{api}.so
%endif
%{_libdir}/libwx_qtu_xrc-%{api}.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%autopatch -p1

sh autogen.sh
#autoreconf -fiv -I `pwd`/build/aclocal
# fix plugin dir for 64-bit
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp

%build
#gw 2.8.11 doesn't build otherwise:
%define _disable_ld_no_undefined 1
%define Werror_cflags %nil
# --disable-optimise prevents our $RPM_OPT_FLAGS being overridden
# (see OPTIMISE in configure).
# this code dereferences type-punned pointers like there's no tomorrow.
CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="%{optflags} -fno-strict-aliasing"

%configure --disable-option-checking --enable-unicode \
	--enable-compat28 \
	--without-odbc \
	--with-opengl \
	--with-qt \
	--without-debug_flag \
	--without-debug_info \
	--with-sdl \
	--with-libpng=sys \
	--with-libjpeg=sys \
	--with-libtiff=sys \
	--with-zlib=sys \
	--with-regex=sys \
	--with-liblzma=sys \
	--with-expat=sys \
	--with-cxx=17 \
	--enable-plugins \
	--enable-cxx11 \
	--enable-utf8 \
	--enable-repro-build \
	--enable-pch \
	--enable-intl \
	--enable-xlocale \
	--enable-config \
	--enable-protocols \
	--enable-ftp \
	--enable-http \
	--enable-fileproto \
	--enable-sockets \
	--enable-ipv6 \
	--enable-dataobj \
	--enable-ipc \
	--enable-baseevtloop \
	--enable-epollloop \
	--enable-selectloop \
	--enable-any \
	--enable-arcstream \
	--enable-base64 \
	--enable-backtrace \
	--enable-cmdline \
	--enable-datetime \
	--enable-debugreport \
	--enable-dialupman \
	--enable-dynlib \
	--enable-dynamicloader \
	--enable-exceptions \
	--enable-ffile \
	--enable-file \
	--enable-filehistory \
	--enable-filesystem \
	--enable-fontenum \
	--enable-fontmap \
	--enable-fs_archive \
	--enable-fs_inet \
	--enable-fs_zip \
	--enable-fsvolume \
	--enable-fswatcher \
	--enable-geometry \
	--enable-log \
	--enable-longlong \
	--enable-mimetype \
	--enable-printfposparam \
	--enable-secretstore \
	--enable-snglinst \
	--enable-sound \
	--enable-stdpaths \
	--enable-stopwatch \
	--enable-streams \
	--enable-sysoptions \
	--enable-tarstream \
	--enable-textbuf \
	--enable-textfile \
	--enable-timer \
	--enable-variant \
	--enable-zipstream \
	--enable-url \
	--enable-protocol \
	--enable-protocol-http \
	--enable-protocol-ftp \
	--enable-protocol-file \
	--enable-threads \
	--enable-docview \
	--enable-help \
	--enable-html \
	--enable-htmlhelp \
	--enable-xrc \
	--enable-aui \
	--enable-propgrid \
	--enable-ribbon \
	--enable-stc \
	--enable-constraints \
	--enable-loggui \
	--enable-logwin \
	--enable-logdialog \
	--enable-mdi \
	--enable-mdidoc \
	--enable-mediactrl \
	--enable-richtext \
	--enable-postscript \
	--enable-printarch \
	--enable-svg \
	--enable-webview \
	--enable-graphics_ctx \
	--enable-clipboard \
	--enable-dnd \
	--disable-controls \
	--enable-markup \
	--enable-accel \
	--enable-actindicator \
	--enable-addremovectrl \
	--enable-animatectrl \
	--enable-bannerwindow \
	--enable-artstd \
	--enable-bmpbutton \
	--enable-bmpcombobox \
	--enable-button \
	--enable-calendar \
	--enable-caret \
	--enable-checkbox \
	--enable-checklst \
	--enable-choice \
	--enable-choicebook \
	--enable-collpane \
	--enable-colourpicker \
	--enable-combobox \
	--enable-comboctrl \
	--enable-commandlinkbutton \
	--enable-dataviewctrl \
	--enable-datepick \
	--enable-detect_sm \
	--enable-dirpicker \
	--enable-display \
	--enable-editablebox \
	--enable-filectrl \
	--enable-filepicker \
	--enable-fontpicker \
	--enable-gauge \
	--enable-grid \
	--enable-headerctrl \
	--enable-hyperlink \
	--enable-imaglist \
	--enable-infobar \
	--enable-listbook \
	--enable-listbox \
	--enable-listctrl \
	--enable-notebook \
	--enable-notifmsg \
	--enable-odcombobox \
	--enable-popupwin \
	--enable-prefseditor \
	--enable-privatefonts \
	--enable-radiobox \
	--enable-radiobtn \
	--enable-richmsgdlg \
	--enable-richtooltip \
	--enable-rearrangectrl \
	--enable-sash \
	--enable-scrollbar \
	--enable-searchctrl \
	--enable-slider \
	--enable-spinbtn \
	--enable-spinctrl \
	--enable-splitter \
	--enable-statbmp \
	--enable-statbox \
	--enable-statline \
	--enable-stattext \
	--enable-statusbar \
	--enable-taskbaricon \
	--enable-tbarnative \
	--enable-textctrl \
	--enable-timepick \
	--enable-tipwindow \
	--enable-togglebtn \
	--enable-toolbar \
	--enable-toolbook \
	--enable-treebook \
	--enable-treectrl \
	--enable-treelist \
	--enable-commondlg \
	--enable-aboutdlg \
	--enable-choicedlg \
	--enable-coldlg \
	--enable-filedlg \
	--enable-finddlg \
	--enable-fontdlg \
	--enable-dirdlg \
	--enable-msgdlg \
	--enable-numberdlg \
	--enable-splash \
	--enable-textdlg \
	--enable-tipdlg \
	--enable-progressdlg \
	--enable-wizarddlg \
	--enable-menus \
	--enable-miniframe \
	--enable-tooltips \
	--enable-splines \
	--enable-mousewheel \
	--enable-validators \
	--enable-busyinfo \
	--enable-hotkey \
	--enable-joystick \
	--enable-metafiles \
	--enable-dragimage \
	--enable-uiactionsim \
	--enable-dctransform \
	--enable-webviewwebkit \
	--enable-palette \
	--enable-image \
	--enable-gif \
	--enable-pcx \
	--enable-tga \
	--enable-iff \
	--enable-pnm \
	--enable-xpm \
	--enable-ico_cur \
	--enable-autoidman


%make

# make -C locale

%install
%makeinstall_std
%find_lang wxstd-%{api}
%find_lang wxmsw-%{api}
cat wxmsw-%{api}.lang >> wxstd-%{api}.lang
