Summary:	a professional CAD system
Summary(pl):	Profesjonalny program CAD
Name:		qcad
Version:	1.4.7
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.qcad.org/archives/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-pl.po.patch
Patch2:		%{name}-Makefile.patch
Icon:		qcad.xpm
URL:		http://www.qcad.org/
Requires:	qt >= 2.2
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel >= 2.2
#BuildRequires:	tmake >= 1.7-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
QCad is a professional CAD System. With QCad you can easily construct
and change drawings with ISO-text and many other features and save
them as DXF-files. These DXF-files are the interface to many
CAD-systems such as AutoCAD(c) and many others.

%description -l pl
QCad jest profesjonalnym programem CAD. QCad-em mo¿esz prosto
konstruowaæ i zmieniaæ rysunki i zapisywaæ je w formacie DXF,
który jest akceptowany przez wiele programów CAD w tym program
AutoCAD(c).

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__make} \
	CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g} \
	-fno-rtti -fno-exceptions -DDATADIR=\\\"%{_datadir}/\\\"" \
	INCPATH="-I/usr/X11R6/include -I/usr/X11R6/include/qt" \
	LDFLAGS="" qcad

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/qcad,%{_datadir}/qcad} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir}}

install qcad $RPM_BUILD_ROOT%{_bindir}
cp -pR {examples,fonts,hatches,libraries,messages,xpm} $RPM_BUILD_ROOT%{_datadir}/qcad
ln -s %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/qcad/doc

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS README MANIFEST changes-* TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* *.gz 
%attr(755,root,root) %{_bindir}/qcad
%{_datadir}/qcad
%{_applnkdir}/Graphics/*
%{_pixmapsdir}/*
