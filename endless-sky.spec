%define hidpi   %{name}-high-dpi
%define oversion 0.10.14

Name:           endless-sky
Version:        0.10.14
Release:        1
Summary:        A space exploration and combat game similar to Escape Velocity
Group:          Games/Simulation
License:        GPLv3+ and CC-BY-SA 3.0 and CC-BY-SA 4.0 and CC-BY 4.0 and Public Domain
URL:            https://endless-sky.github.io

Source0:        https://github.com/endless-sky/endless-sky/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/endless-sky/endless-sky-high-dpi/archive/v%{version}/%{hidpi}-%{oversion}.tar.gz

BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  scons

Requires:       %{name}-data >= %{version}-%{release}

%description
Endless Sky is a sandbox-style space exploration game similar to Elite,
Escape Velocity, or Star Control. You start out as the captain of a tiny
space ship and can choose what to do from there. The game includes a major
plot line and many minor missions, but you can choose whether you want to
play through the plot or strike out on your own as a merchant or bounty
hunter or explorer.

Note: For users of high-DPI monitors, there is an optional %{hidpi}
package that contains high-resolution graphics for this game.

%files
%doc copyright credits.txt README.md
%{_gamesbindir}/%{name}
%{_datadir}/metainfo/io.github.endless_sky.endless_sky.appdata.xml
%{_datadir}/applications/io.github.endless_sky.endless_sky.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%package data
Summary:        Data files for the Endless Sky game
License:        GPLv3+ and CC-BY 3.0 and CC-BY-SA 3.0 and CC-BY-SA 4.0 and Public domain
BuildArch:      noarch

%description data
This package contains arch-independent data files for the Endless Sky
game (sounds, graphics, game scripts and texts).

%files data
%{_gamesdatadir}/%{name}/
%exclude %{_gamesdatadir}/%{name}/plugins/%{hidpi}

#----------------------------------------------------------------------

%package high-dpi
Summary:        High-DPI graphics for Endless Sky
License:        CC-BY 3.0 and CC-BY-SA 3.0 and CC-BY-SA 4.0 and Public domain
BuildArch:      noarch

%description high-dpi
This is a collection of double-resolution sprites for Endless Sky. Installing
this package is fully optional. These sprites will only be used if:

- you have set the "zoom factor" to higher than 100%% in the preferences, or
- you have a high-DPI monitor.

%files high-dpi
%{_gamesdatadir}/%{name}/plugins/%{hidpi}

#----------------------------------------------------------------------

%prep
%setup -q -a1
%autopatch -p1

%build
%set_build_flags
%scons

%install
%set_build_flags
%scons_install PREFIX=%{_prefix}

install -d %{buildroot}%{_gamesdatadir}/%{name}/plugins
mv %{hidpi}-%{oversion} %{buildroot}%{_gamesdatadir}/%{name}/plugins/%{hidpi}
