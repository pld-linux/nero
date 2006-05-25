#
# Conditional build:
%bcond_with	reqs		# force optional Requires
#
Summary:	NeroLINUX CD/DVD burning
Summary(pl):	NeroLINUX - program do wypalania p³yt CD/DVD
Name:		nero
Version:	2.0.0.5
Release:	1
License:	Commercial (see EULA)
Group:		X11/Applications
Source0:	ftp://ftp2.usw.nero.com/nerolinux-%{version}-x86.rpm
# NoSource0-md5:	b68ecfe412ab11ee588e54ce0b5930da
NoSource:	0
URL:		http://www.nero.com/
BuildRequires:	cpio
BuildRequires:	sed >= 4.0
%if %{with reqs}
Requires:	mp3info
Requires:	mpg123
Requires:	sox
Requires:	vorbis-tools
%endif
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD/DVD burning software for Linux.

%description -l pl
Oprogramowanie do wypalania p³yt CD/DVD pod Linuksem.

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -i -d

%{__sed} -i 's,Categories=.*,Categories=GTK;AudioVideo;DiscBurning;,' \
	usr/share/nero/desktop/NeroLINUX.template
cat >> usr/share/nero/desktop/NeroLINUX.template <<EOF
Icon=nero.png
Exec=nero
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_libdir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{docs,sounds}

install usr/bin/nero $RPM_BUILD_ROOT%{_bindir}
install usr/lib/* $RPM_BUILD_ROOT%{_libdir}
install usr/share/nero/*.{CFG,ima,so,txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install usr/share/nero/sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install usr/share/nero/desktop/* $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install usr/share/nero/pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}
# displayed at first startup
install usr/share/nero/docs/EULA $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

# FHS compliance (*.so moved to %{_libdir})
cd $RPM_BUILD_ROOT%{_datadir}/%{name}
for i in *.so ; do
	mv -f $i $RPM_BUILD_ROOT%{_libdir}
	ln -s %{_libdir}/$i $i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc usr/share/nero/docs/{Manual.pdf,NEWS}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_datadir}/nero
%{_desktopdir}/*
%{_pixmapsdir}/*
