Summary:	A professional CAD system
Summary(pl.UTF-8):	Profesjonalny program CAD
Summary(pt_BR.UTF-8):	Um sistema de CAD 2D livre (Open Source)
Name:		qcad
Version:	3.26.0.1
Release:	2
License:	GPL v3
Group:		X11/Applications/Graphics
#Source0Download: http://www.ribbonsoft.com/qcad_downloads.html
Source0:	https://github.com/qcad/qcad/archive/v%{version}/%{name}-%{version}-community.tar.gz
# Source0-md5:	e34bae0b84e3a0d4a9ffab45a802e15b
Source1:	%{name}.appdata.xml
URL:		http://www.ribbonsoft.com/qcad.html
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5ScriptTools-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	appstream-glib-devel
BuildRequires:	dbus-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	openssl-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	Qt5Concurrent
Requires:	Qt5Core
Requires:	Qt5Designer-plugin-qwebview
Requires:	Qt5Gui
Requires:	Qt5Gui
Requires:	Qt5Gui-imageformats
Requires:	Qt5Multimedia
Requires:	Qt5Network
Requires:	Qt5OpenGL
Requires:	Qt5PrintSupport
Requires:	Qt5PrintSupport
Requires:	qt5-qttools
Requires:	Qt5Script
Requires:	Qt5ScriptTools
Requires:	Qt5Sql
Requires:	Qt5Sql
Requires:	Qt5Sql-sqldriver-sqlite3
Requires:	Qt5Svg
Requires:	Qt5WebKit
Requires:	Qt5Widgets
Requires:	Qt5Xml
Requires:	Qt5XmlPatterns
Requires:	fonts-TTF-DejaVu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QCad is a professional CAD System. With QCad you can easily construct
and change drawings with ISO-text and many other features and save
them as DXF-files. These DXF-files are the interface to many
CAD-systems such as AutoCAD(c) and many others.

%description -l pl.UTF-8
QCad jest profesjonalnym programem CAD. QCadem można prosto
konstruować i zmieniać rysunki i zapisywać je w formacie DXF, który
jest akceptowany przez wiele programów CAD w tym program AutoCAD(c).

%description -l pt_BR.UTF-8
O QCad é um sistema profissional de CAD. Com ele você pode facilmente
construir e mudar desenhos com textos ISO e muitas outras
características e salvá-los como arquivos DXF. Estes arquivos DXF são
a interface para muitos outros sistemas de CAD, como o AutoCAD(c).

%prep
%setup -q

%build
qmake-qt5 -makefile \
	CONFIG+=release %{name}.pro \
	QMAKE_CFLAGS_RELEASE+="%{rpmcflags}" \
	QMAKE_CXXFLAGS_RELEASE+="%{rpmcxxflags}" \
	QMAKE_LFLAGS+="%{rpmldflags} -Wl,-rpath -Wl,%{_libdir}/%{name}" \
	LFLAGS+="%{rpmldflags} -Wl,-rpath -Wl,%{_libdir}/%{name}"

%{__make} release

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_mandir}/man1,%{_iconsdir}/hicolor/scalable/apps} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{plugins/{designer,imageformats,sqldrivers,script,printsupport},ts} \
	$RPM_BUILD_ROOT%{_datadir}/metainfo

## Install fonts
cp -a fonts $RPM_BUILD_ROOT%{_libdir}/%{name}

# Unbundle dejavu fonts
for i in $RPM_BUILD_ROOT%{_libdir}/%{name}/fonts/qt/DejaVuS*; do
	ln -sf "%{_datadir}/fonts/TTF/$(basename $i)" "$i"
done

cp -a patterns themes libraries scripts plugins linetypes $RPM_BUILD_ROOT%{_libdir}/%{name}

# This file is required for Help's "Show Readme" menu choice
cp -p readme.txt $RPM_BUILD_ROOT%{_libdir}/%{name}

cp -p ts/qcad*.qm $RPM_BUILD_ROOT%{_libdir}/%{name}/ts
ln -sf %{_libdir}/qt5/plugins/designer/libqwebview.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/designer/libqwebview.so

ln -sf %{_libdir}/qt5/plugins/imageformats/libqgif.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats/libqgif.so
ln -sf %{_libdir}/qt5/plugins/imageformats/libqico.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats/libqico.so
ln -sf %{_libdir}/qt5/plugins/imageformats/libqjpeg.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats/libqjpeg.so
ln -sf %{_libdir}/qt5/plugins/imageformats/libqsvg.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats/libqsvg.so
ln -sf %{_libdir}/qt5/plugins/imageformats/libqtga.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats/libqtga.so
ln -sf %{_libdir}/qt5/plugins/imageformats/libqtiff.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats/libqtiff.so

ln -sf %{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/sqldrivers/libqsqlite.so
ln -sf %{_libdir}/qt5/plugins/printsupport/libcupsprintersupport.so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/printsupport/libcupsprintersupport.so

cp -p scripts/qcad_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp -p release/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -p release/%{name}-bin $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -p readme.txt $RPM_BUILD_ROOT%{_libdir}/%{name}

cp -p qcad.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p scripts/%{name}_icon.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

find $RPM_BUILD_ROOT%{_libdir}/%{name} -name ".gitignore" -delete
find $RPM_BUILD_ROOT%{_libdir}/%{name} -name "readme.txt" -delete
find $RPM_BUILD_ROOT%{_libdir}/%{name} -name "Makefile" -delete

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
export LD_LIBRARY_PATH=%{_libdir}/%{name}:%{_libdir}/%{name}/plugins/script
export QTLIB=%{_libdir}
export QTDIR=%{_libdir}
export QTINC=%{_includedir}/qt5
export PATH=%{_libdir}:%{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-bin "\$@"
EOF

cp -p qcad.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/metainfo

cd $RPM_BUILD_ROOT%{_libdir}/%{name}
for i in $(find . -type f \( -name "*.so*" -o -name "qcad-bin" \)); do
  chmod -c 755 $i
  chrpath -r %{_libdir}/%{name} $i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qcad
%dir %{_libdir}/qcad
%attr(755,root,root) %{_libdir}/qcad/lib*.so
%attr(755,root,root) %{_libdir}/qcad/qcad-bin
%{_libdir}/qcad/fonts
%{_libdir}/qcad/libraries
%{_libdir}/qcad/linetypes
%{_libdir}/qcad/patterns
%dir %{_libdir}/qcad/plugins
%attr(755,root,root) %{_libdir}/qcad/plugins/lib*.so
%dir %{_libdir}/qcad/plugins/designer
%attr(755,root,root) %{_libdir}/qcad/plugins/designer/lib*.so
%dir %{_libdir}/qcad/plugins/imageformats
%attr(755,root,root) %{_libdir}/qcad/plugins/imageformats/lib*.so
%dir %{_libdir}/qcad/plugins/printsupport
%attr(755,root,root) %{_libdir}/qcad/plugins/printsupport/lib*.so
%dir %{_libdir}/qcad/plugins/script
%attr(755,root,root) %{_libdir}/qcad/plugins/script/libqtscript_*.so*
%dir %{_libdir}/qcad/plugins/sqldrivers
%attr(755,root,root) %{_libdir}/qcad/plugins/sqldrivers/lib*.so
%{_libdir}/qcad/scripts
%{_libdir}/qcad/themes
%dir %{_libdir}/qcad/ts
%{_libdir}/qcad/ts/*_en.qm
%lang(cs) %{_libdir}/qcad/ts/*_cs.qm
%lang(da) %{_libdir}/qcad/ts/*_da.qm
%lang(de) %{_libdir}/qcad/ts/*_de.qm
%lang(es) %{_libdir}/qcad/ts/*_es.qm
%lang(fi) %{_libdir}/qcad/ts/*_fi.qm
%lang(fr) %{_libdir}/qcad/ts/*_fr.qm
%lang(hr) %{_libdir}/qcad/ts/*_hr.qm
%lang(hu) %{_libdir}/qcad/ts/*_hu.qm
%lang(it) %{_libdir}/qcad/ts/*_it.qm
%lang(ja) %{_libdir}/qcad/ts/*_ja.qm
%lang(lt) %{_libdir}/qcad/ts/*_lt.qm
%lang(nl) %{_libdir}/qcad/ts/*_nl.qm
%lang(pl) %{_libdir}/qcad/ts/*_pl.qm
%lang(pt) %{_libdir}/qcad/ts/*_pt.qm
%lang(ru) %{_libdir}/qcad/ts/*_ru.qm
%lang(sk) %{_libdir}/qcad/ts/*_sk.qm
%lang(sl) %{_libdir}/qcad/ts/*_sl.qm
%lang(sv) %{_libdir}/qcad/ts/*_sv.qm
%lang(th) %{_libdir}/qcad/ts/*_th.qm
%lang(tr) %{_libdir}/qcad/ts/*_tr.qm
%lang(zh_CN) %{_libdir}/qcad/ts/*_zh_CN.qm
%lang(zh_TW) %{_libdir}/qcad/ts/*_zh_TW.qm
%{_desktopdir}/qcad.desktop
%{_pixmapsdir}/qcad.png
%{_iconsdir}/hicolor/scalable/apps/qcad.svg
%{_mandir}/man1/qcad.1*
%{_datadir}/metainfo/qcad.appdata.xml
