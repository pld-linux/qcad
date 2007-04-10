# TODO:
# - separate language packages
# - manual supbackage (languaged?)
%define		_csver		2.0.4.0-1
%define		_dever		2.0.4.0-1
%define		_enver		2.0.4.0-1
%define		_huver		2.0.4.0-1
Summary:	A professional CAD system
Summary(pl.UTF-8):	Profesjonalny program CAD
Summary(pt_BR.UTF-8):	Um sistema de CAD 2D livre (Open Source)
Name:		qcad
Version:	2.0.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
#Source0Download: http://www.ribbonsoft.com/qcad_downloads.html
Source0:	http://www.ribbonsoft.com/archives/qcad/%{name}-%{version}-1-community.src.tar.gz
# Source0-md5:	96b6a56027782aec953c9c4e64c5998c
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-cs-%{_csver}.html.zip
# Source3-md5:	45b444d58761b7a4074ca231f46d04fa
Source4:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-de-%{_dever}.html.zip
# Source4-md5:	71aba8cfd5dc521bd96454c46dafcb2c
Source5:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-en-%{_enver}.html.zip
# Source5-md5:	20d8fddbe0da978f996bdfaf9ae6bec1
Source6:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-hu-%{_huver}.html.zip
# Source6-md5:	56c94d907761d4affa00c029f52fe96d
Patch0:		%{name}-gcc4.patch
URL:		http://www.ribbonsoft.com/qcad.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3:3.0.5
BuildRequires:	qt-linguist
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXext-devel
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
%setup -q -n %{name}-%{version}-1-community.src -a3 -a4 -a5 -a6
%patch0 -p1

sed -i -e 's/-pedantic//' mkspecs/defs.pro

%build
QTDIR=%{_prefix}; export QTDIR
QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++; export QMAKESPEC
CXXFLAGS="%{rpmcflags} -fno-exceptions"
for i in fparser dxflib; do
	cd $i
	cp -f /usr/share/automake/config.* .
	%{__autoconf}
	%configure
	%{__make}
	cd ..
done
cd qcadcmd
%{__make} prepare
cd ..
for i in qcadlib qcadcmd qcadactions qcadguiqt qcad; do
	cd $i/src
	echo 'CONFIG += thread' >> `echo *.pro`
	qmake *.pro \
		QMAKE_CXXFLAGS_RELEASE="$CXXFLAGS"
	cd ..
	%{__make}
	cd ..
done;

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/qcad} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cwd=`pwd`
for dir in qcadcmd qcadactions qcadguiqt qcad; do
	cd $dir/src
	lrelease *.pro
	cd ts
	for tf in *.qm; do
		ln -sf $cwd/$dir/src/ts/$tf $cwd/qcad/qm/$tf
	done
	cd ../../..
done

cp -LR scripts $RPM_BUILD_ROOT%{_datadir}/qcad
cd qcad
install qcad $RPM_BUILD_ROOT%{_bindir}
cp -LR {fonts,patterns,qm} $RPM_BUILD_ROOT%{_datadir}/qcad

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc qcad-manual-en-%{_enver}.html
%lang(cs) %doc qcad-manual-cs-%{_csver}.html
%lang(de) %doc qcad-manual-de-%{_dever}.html
%lang(hu) %doc qcad-manual-hu-%{_huver}.html
%attr(755,root,root) %{_bindir}/qcad
%dir %{_datadir}/qcad
%{_datadir}/qcad/fonts
%{_datadir}/qcad/patterns
%{_datadir}/qcad/scripts
%dir %{_datadir}/qcad/qm
%lang(cs) %{_datadir}/qcad/qm/*_cs.qm
%lang(da) %{_datadir}/qcad/qm/*_da.qm
%lang(de) %{_datadir}/qcad/qm/*_de.qm
%lang(el) %{_datadir}/qcad/qm/*_el.qm
%{_datadir}/qcad/qm/*_en.qm
%lang(es) %{_datadir}/qcad/qm/*_es.qm
%lang(et) %{_datadir}/qcad/qm/*_et.qm
%lang(fr) %{_datadir}/qcad/qm/*_fr.qm
%lang(hu) %{_datadir}/qcad/qm/*_hu.qm
%lang(it) %{_datadir}/qcad/qm/*_it.qm
%lang(nl) %{_datadir}/qcad/qm/*_nl.qm
%lang(nb) %{_datadir}/qcad/qm/*_no.qm
%lang(pa) %{_datadir}/qcad/qm/*_pa.qm
%lang(pl) %{_datadir}/qcad/qm/*_pl.qm
%lang(ru) %{_datadir}/qcad/qm/*_ru.qm
%lang(sk) %{_datadir}/qcad/qm/*_sk.qm
%lang(tr) %{_datadir}/qcad/qm/*_tr.qm
%{_desktopdir}/qcad.desktop
%{_pixmapsdir}/qcad.png
