%define name qcad
%define version 1.2.0
%define release 1mdk

Summary: a professional CAD system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_source.tar.bz2
Patch0: %{name}-make.patch.bz2
URL: http://www.qcad.org
Copyright: GPL 
Group: Applications/Graphics
BuildRoot: /var/tmp/%{name}-%{version}-root
Prefix: /usr
Requires: qt2
BuildPreReq: XFree86-devel, qt2-devel

%description
QCad is a professional CAD System. With QCad you can easily construct and
change drawings with ISO-text and many other features and save them as
DXF-files. These DXF-files are the interface to many CAD-systems such
as AutoCAD® and many others.

%prep
%setup -n %{name}_source
%patch -p1 -b .make

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{prefix}/{bin,lib/qcad}
install -s -m 755 qcad $RPM_BUILD_ROOT/%{prefix}/lib/qcad
install -m 644 qcad.ini qcad.xpm language.cxl \
	$RPM_BUILD_ROOT/%{prefix}/lib/qcad
cp -pR {examples,fonts,hatches} $RPM_BUILD_ROOT/%{prefix}/lib/qcad

cat > $RPM_BUILD_ROOT/%{prefix}/bin/qcad <<EOF
#!/bin/sh
cd %{prefix}/lib/qcad
./qcad "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/* AUTHORS COPYING README INSTALL LICENSE
%attr(755,root,root) %{prefix}/bin/qcad
%{prefix}/lib/qcad

%changelog
* Mon Nov  8 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
