Summary:	a professional CAD system
Summary(pl):	Profesjonalny program CAD
Name:		qcad
Version:	1.4.4
Release:	1
Source0:	http://www.qcad.org/archives/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-datadir.patch
URL:		http://www.qcad.org
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Requires:	qt >= 2.2
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix /usr/X11R6

%description
QCad is a professional CAD System. With QCad you can easily construct
and change drawings with ISO-text and many other features and save
them as DXF-files. These DXF-files are the interface to many
CAD-systems such as AutoCAD® and many others.

%description -l pl

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
%{__make} \
	CFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -DDATADIR=\\\"%{_datadir}/\\\"" \
	QTDIR="%{_prefix}" \
	LFLAGS=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/qcad,%{_datadir}/qcad}
install qcad $RPM_BUILD_ROOT%{_bindir}
cp -pR {examples,fonts,hatches,libraries,messages,xpm} $RPM_BUILD_ROOT%{_datadir}/qcad
ln -s %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/qcad/doc

gzip -9nf AUTHORS README MANIFEST changes-* TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS.gz README.gz MANIFEST.gz changes-*.gz TODO.gz 
%attr(755,root,root) %{_bindir}/qcad
%{_datadir}/qcad
