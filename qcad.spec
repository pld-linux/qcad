Summary:	A professional CAD system
Summary(pl):	Profesjonalny program CAD
Summary(pt_BR):	Um sistema de CAD 2D livre (Open Source)
Name:		qcad
Version:	2.0.0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://www.ribbonsoft.com/archives/qcad/%{name}-%{version}-1.src.tar.gz
# Source0-md5:	a2f62fb7865aa35445d9cbfc3414096f
Source1:	%{name}.desktop
Source2:	%{name}.png
Source4:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-2.0.0.5-1.xml.zip
# Source4-md5:	25717640f5d7d5c231695bf39a8c02ee
Icon:		qcad.xpm
URL:		http://www.qcad.org/
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QCad is a professional CAD System. With QCad you can easily construct
and change drawings with ISO-text and many other features and save
them as DXF-files. These DXF-files are the interface to many
CAD-systems such as AutoCAD(c) and many others.

%description -l pl
QCad jest profesjonalnym programem CAD. QCad-em mo�esz prosto
konstruowa� i zmienia� rysunki i zapisywa� je w formacie DXF, kt�ry
jest akceptowany przez wiele program�w CAD w tym program AutoCAD(c).

%description -l pt_BR
O QCad � um sistema profissional de CAD. Com ele voc� pode facilmente
construir e mudar desenhos com textos ISO e muitas outras
caracter�sticas e salv�-los como arquivos DXF. Estes arquivos DXF s�o
a interface para muitos outros sistemas de CAD, como o AutoCAD(c).

%prep
%setup -q -n %{name}-%{version}-1.src -a4

%build
QTDIR=%{_prefix}; export QTDIR
QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++; export QMAKESPEC
for i in fparser dxflib; do
	cd $i
	%{__autoconf}
	%configure
	%{__make} \
		CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions %{!?debug:-DQT_NO_DEBUG}" \
		LDFLAGS="%{rpmldflags}"
	cd ..
done
cd qcadcmd
%{__make} prepare
cd ..
for i in qcadlib qcadcmd qcadactions qcadguiqt qcad; do
	cd $i
	%{__make} \
		CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions %{!?debug:-DQT_NO_DEBUG}" \
		LDFLAGS="%{rpmldflags}"
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

cd qcad		
install qcad $RPM_BUILD_ROOT%{_bindir}
cp -LR {examples,fonts,patterns,qm,scripts} $RPM_BUILD_ROOT%{_datadir}/qcad

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc qcad-manual-2.0.0.5-1.xml/*
%attr(755,root,root) %{_bindir}/qcad
%{_datadir}/qcad
%{_desktopdir}/qcad.desktop
%{_pixmapsdir}/qcad.png
