# TODO:
# - build x8664 package
#
# Conditional build:
%bcond_with	reqs		# force optional Requires
#
Summary:	NeroLINUX CD/DVD burning
Summary(pl.UTF-8):	NeroLINUX - program do wypalania płyt CD/DVD
Name:		nero
Version:	3.0.0.0
Release:	1.1
License:	Commercial (see EULA)
Group:		X11/Applications
Source0:	ftp://ftp10.de.nero.com/PUB/c76cad1378e8a9e4bc4c62700e4ad856/nerolinux-%{version}-x86.rpm
# NoSource0-md5:	43d35405cbc8dd0078949e8cc763a999
Source1:	ftp://ftp5.de.nero.com/PUB/ee97bc40ba51279ad5ee49c5f88c9c09/nerolinux-%{version}-x86_64.rpm
# NoSource1-md5:	d0ae720344f1743a43c3e5bb2904cef0
NoSource:	0 1
URL:		http://www.nero.com/
BuildRequires:	cpio
BuildRequires:	sed >= 4.0
%if %{with reqs}
Requires:	mp3info
Requires:	mpg123
Requires:	sox
Requires:	vorbis-tools
%endif
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD/DVD burning software for Linux.

%description -l pl.UTF-8
Oprogramowanie do wypalania płyt CD/DVD pod Linuksem.

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -i -d

%{__sed} -i 's,Categories=.*,Categories=GTK;AudioVideo;DiscBurning;,' \
	usr/share/applications/nerolinux.desktop

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_libdir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{docs,sounds}

install usr/bin/nero $RPM_BUILD_ROOT%{_bindir}
cp -ar usr/lib/* $RPM_BUILD_ROOT%{_libdir}
install usr/share/nero/*.{CFG,ima,txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install usr/share/applications/*.desktop $RPM_BUILD_ROOT%{_desktopdir}
install usr/share/nero/sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp -ar usr/share/nero/images $RPM_BUILD_ROOT%{_datadir}/%{name}
# displayed at first startup
cp -ar usr/share/nero/eula $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc usr/share/doc/nero/{Manual.pdf,NEWS}
%lang(de) %doc usr/share/doc/nero/Manual-Deu.pdf
%lang(fr) %doc usr/share/doc/nero/Manual-Fra.pdf
%lang(ko) %doc usr/share/doc/nero/Manual-Kor.pdf
%lang(zh_CN) %doc usr/share/doc/nero/Manual-Chs.pdf
%lang(zh_TW) %doc usr/share/doc/nero/Manual-Cht.pdf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/nero
%{_desktopdir}/*.desktop
