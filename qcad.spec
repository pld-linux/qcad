Summary:	a professional CAD system
Summary(pl):	Profesjonalny program CAD
Summary(pt_BR):	Um sistema de CAD 2D livre (Open Source)
Name:		qcad
Version:	1.5.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/qcad/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:		%{name}-Makefile.patch
Patch2: 	%{name}-lib.patch
Icon:		qcad.xpm
URL:		http://www.qcad.org/
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%setup -q -n %{name}-%{version}-src
%patch1 -p1
%patch2 -p1

%build
QTDIR="/usr/X11R6"
export QTDIR
%{__make} \
	INCPATH="-I/usr/X11R6/include -I/usr/X11R6/include/qt" \
	QMAKE_CONF="%{_datadir}/qt/mkspecs/linux-g++/qmake.conf" \
	LDFLAGS="%{rpmldflags}" qcad

#	CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions %{!?debug:-DQT_NO_DEBUG}" \
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/qcad,%{_datadir}/qcad} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir}}

install qcad $RPM_BUILD_ROOT%{_bindir}
cp -pR {examples,fonts,hatches,libraries,messages,xpm} $RPM_BUILD_ROOT%{_datadir}/qcad
ln -sf %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/qcad/doc

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS README MANIFEST changes-* TODO
%attr(755,root,root) %{_bindir}/qcad
%{_datadir}/qcad
%{_applnkdir}/Graphics/*
%{_pixmapsdir}/*
