Summary:	a professional CAD system
Summary(pl):	Profesjonalny program CAD
Summary(pt_BR):	Um sistema de CAD 2D livre (Open Source)
Name:		qcad
Version:	1.5.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/qcad/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-lib.patch
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
QCad jest profesjonalnym programem CAD. QCad-em mo¿esz prosto
konstruowaæ i zmieniaæ rysunki i zapisywaæ je w formacie DXF, który
jest akceptowany przez wiele programów CAD w tym program AutoCAD(c).

%description -l pt_BR
O QCad é um sistema profissional de CAD. Com ele você pode facilmente
construir e mudar desenhos com textos ISO e muitas outras
características e salvá-los como arquivos DXF. Estes arquivos DXF são
a interface para muitos outros sistemas de CAD, como o AutoCAD(c).

%prep
%setup -q
%patch0 -p1

%build
QTDIR=%{_prefix}; export QTDIR
%{_bindir}/qmake qcad.pro -o Makefile
%{__make} \
	CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions %{!?debug:-DQT_NO_DEBUG}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/qcad} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir}}

install qcad $RPM_BUILD_ROOT%{_bindir}
cp -pR {examples,fonts,hatches,libraries,messages,xpm} $RPM_BUILD_ROOT%{_datadir}/qcad
ln -sf %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/qcad/doc

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cd $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog MANIFEST README TODO
%attr(755,root,root) %{_bindir}/qcad
%{_datadir}/qcad
%{_applnkdir}/Graphics/*
%{_pixmapsdir}/*
