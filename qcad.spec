Summary:	a professional CAD system
Summary(pl):	Profesjonalny program CAD
Name:		qcad
Version:	1.4.0
Release:	1
Source0:	%{name}_source.tar.bz2
Patch0:		%{name}-make.patch.bz2
URL:		http://www.qcad.org
License:	GPL
Group:		X11/Applications/Graphics
######		Unknown group!
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	qt2
BuildPreReq:	XFree86-devel, qt2-devel

%description
QCad is a professional CAD System. With QCad you can easily construct and
change drawings with ISO-text and many other features and save them as
DXF-files. These DXF-files are the interface to many CAD-systems such as
AutoCAD® and many others.

%description -l pl

%prep
%setup -q -n %{name}_source
%patch -p1 -b .make

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix}/{bin,lib/qcad}
install -s -m 755 qcad $RPM_BUILD_ROOT/%{_libdir}/qcad
install qcad.ini qcad.xpm language.cxl \
	$RPM_BUILD_ROOT/%{_libdir}/qcad
cp -pR {examples,fonts,hatches} $RPM_BUILD_ROOT/%{_libdir}/qcad

cat > $RPM_BUILD_ROOT/%{_bindir}/qcad <<EOF
#!/bin/sh
cd %{_libdir}/qcad
./qcad "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS COPYING README INSTALL LICENSE
%attr(755,root,root) %{_bindir}/qcad
%{_libdir}/qcad
