Summary:	A professional CAD system
Summary(pl):	Profesjonalny program CAD
Summary(pt_BR):	Um sistema de CAD 2D livre (Open Source)
Name:		qcad
Version:	2.0.3.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://www.ribbonsoft.com/archives/qcad/%{name}-%{version}-1.src.tar.gz
# Source0-md5:	d5c87f9a416657e20da94e21dc6d4245
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-de-2.0.1.3-1.html.zip
# Source3-md5:	78bfef9f9295899e1534b24469a8a40e
Source4:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-en-2.0.1.3-1.html.zip
# Source4-md5:	4c9e3c08e4b0b9e41eef2fdcc0e8af41
Source5:	http://www.ribbonsoft.com/archives/qcad/%{name}-manual-hu-2.0.1.4-2.html.zip
# Source5-md5:	978358eff7246dad3b5e94fc4d346552
Icon:		qcad.xpm
URL:		http://www.ribbonsoft.com/qcad.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
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
%setup -q -n %{name}-%{version}-1.src -a3 -a4 -a5

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
%doc qcad-manual-en-2.0.1.3-1.html
%lang(de) %doc qcad-manual-de-2.0.1.3-1.html
%lang(hu) %doc qcad-manual-hu-2.0.1.4-2.html
%attr(755,root,root) %{_bindir}/qcad
%dir %{_datadir}/qcad
%{_datadir}/qcad/examples
%{_datadir}/qcad/fonts
%{_datadir}/qcad/patterns
%{_datadir}/qcad/scripts
%dir %{_datadir}/qcad/qm
%lang(cs) %{_datadir}/qcad/qm/*_cs.qm
%lang(da) %{_datadir}/qcad/qm/*_da.qm
%lang(de) %{_datadir}/qcad/qm/*_de.qm
%lang(el) %{_datadir}/qcad/qm/*_el.qm
%{_datadir}/qcad/qm/*_en.qm
%lang(fr) %{_datadir}/qcad/qm/*_fr.qm
%lang(hu) %{_datadir}/qcad/qm/*_hu.qm
%lang(it) %{_datadir}/qcad/qm/*_it.qm
%lang(nl) %{_datadir}/qcad/qm/*_nl.qm
%lang(nb) %{_datadir}/qcad/qm/*_no.qm
%lang(ru) %{_datadir}/qcad/qm/*_ru.qm
%lang(sk) %{_datadir}/qcad/qm/*_sk.qm
%lang(tr) %{_datadir}/qcad/qm/*_tr.qm
%{_desktopdir}/qcad.desktop
%{_pixmapsdir}/qcad.png
