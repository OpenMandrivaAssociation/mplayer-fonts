%define base_name	mplayer
%define name		%{base_name}-fonts
%define summary		Fonts for %{base_name}
%define version 1.0
%define release %mkrel 15
%define fonts_dir	%{_datadir}/%{base_name}/fonts
%define font_dir	%{_datadir}/%{base_name}/font

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
Source0:	koi8r-font.tar.bz2
Source1:	mp-arial-iso-8859-1.tar.bz2
Source2:	mp-arial-iso-8859-2.tar.bz2
URL:		http://www.mplayerhq.hu
License:	GPL
Group:		Video
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This packages includes following fonts:
- Fonts & symbols package for OSD (ISO 8859-1), by Arpi
- Fonts & symbols package for OSD (ISO 8859-2), by Arpi
- Russian fonts, by Nick Kurshev

%prep
%setup -q -c
%setup -q -c -T -D -a1
%setup -q -c -T -D -a2

%build

%install
install -d -m 755 ${RPM_BUILD_ROOT}%{fonts_dir}
cp -r * ${RPM_BUILD_ROOT}%{fonts_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-alternatives --install %font_dir mplayer-fonts %{fonts_dir}/iso-8859-1/arial-24 30
update-alternatives --install %font_dir mplayer-fonts %{fonts_dir}/iso-8859-2/arial-24 20
update-alternatives --install %font_dir mplayer-fonts %{fonts_dir}/koi8r-font 10

%postun
update-alternatives --remove mplayer-fonts %{fonts_dir}/iso-8859-1/arial-24
update-alternatives --remove mplayer-fonts %{fonts_dir}/iso-8859-2/arial-24
update-alternatives --remove mplayer-fonts %{fonts_dir}/koi8r-font

%files
%defattr(-,root,root)
%{fonts_dir}



%changelog
* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 1.0-15mdv2012.0
+ Revision: 692729
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0-14mdv2011.0
+ Revision: 252963
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.0-12mdv2008.1
+ Revision: 140963
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jul 31 2006 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2007.0
- Rebuild

* Tue Mar 14 2006 Götz Waschk <waschk@mandriva.org> 1.0-11mdk
- Rebuild
- use mkrel

* Sun Mar 13 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0-10mdk
- rebuild

* Fri Feb 06 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.0-9mdk
- anniversary rebuild

