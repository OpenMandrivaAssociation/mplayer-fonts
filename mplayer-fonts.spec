Summary:	Fonts for MPlayer
Name:		mplayer-fonts
Version:	20030714
Release:	1
License:	GPL
Group:		Video
Url:		https://www.mplayerhq.hu
Source0:	koi8r-font.tar.bz2
Source1:	mp-arial-iso-8859-1.tar.bz2
Source2:	mp-arial-iso-8859-2.tar.bz2
Buildarch:	noarch

%description
This packages includes following fonts:
- Fonts & symbols package for OSD (ISO 8859-1), by Arpi
- Fonts & symbols package for OSD (ISO 8859-2), by Arpi
- Russian fonts, by Nick Kurshev

%files
%{_datadir}/mplayer/fonts/

%post
update-alternatives --install %{_datadir}/mplayer/font mplayer-fonts %{_datadir}/mplayer/fonts/iso-8859-1/arial-24 30
update-alternatives --install %{_datadir}/mplayer/font mplayer-fonts %{_datadir}/mplayer/fonts/iso-8859-2/arial-24 20
update-alternatives --install %{_datadir}/mplayer/font mplayer-fonts %{_datadir}/mplayer/fonts/koi8r-font 10

%postun
update-alternatives --remove mplayer-fonts %{_datadir}/mplayer/fonts/iso-8859-1/arial-24
update-alternatives --remove mplayer-fonts %{_datadir}/mplayer/fonts/iso-8859-2/arial-24
update-alternatives --remove mplayer-fonts %{_datadir}/mplayer/fonts/koi8r-font

#----------------------------------------------------------------------------

%prep
%setup -q -c
%setup -q -c -T -D -a1
%setup -q -c -T -D -a2

%build

%install
install -d -m 755 %{buildroot}%{_datadir}/mplayer/fonts
cp -r * %{buildroot}%{_datadir}/mplayer/fonts

