# TODO: noarch or ExclusiveArch? It's GPL, so either noarch, or it should be compiled from source
%define		_pver	pre1-linux-jar-gtk
Summary:	Graphical user interface for p2p cores
Summary(pl):	Interfejs graficzny dla p2p
Name:		g2gui
Version:	0.3.0
Release:	0.1
License:	CPL/GPL
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/mldonkey/%{name}-%{version}-%{_pver}.tar.bz2
# Source0-md5:	7f4770e42530215f51fb320029aa2732
URL:		http://developer.berlios.de/projects/mldonkey/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDonkey G2gui is a next-generation crossplatform Graphical User
Interface to the MLDonkey core. Its goal is to be userfriendly and
powerful, using state of the art Java-techniques like SWT and other
parts of the eclipse framework.

%description -l pl
MLDonkey G2gui jest zaawansowan± graficzn± konsol± umo¿liwiaj±c±
zarz±dzanie rdzeniem MLDonkey. G³ówna zalet± G2gui jest ³atwy i
intuicyjny w obs³udze interfejs napisany w technologii Java.

%prep
%setup -q -n %{name}-%{version}-%{_pver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_libdir}/%{name}}

install g2gui $RPM_BUILD_ROOT%{_bindir}
install lib/* $RPM_BUILD_ROOT%{_libdir}/%{name}
install g2submit/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc distrib/ChangeLog.txt distrib/license-cpl.txt distrib/license-gpl.txt distrib/README.txt distrib/TODO.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}
