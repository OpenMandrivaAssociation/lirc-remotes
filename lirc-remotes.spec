%define	name	lirc-remotes
%define	version 0.8.3
%define	rel	0.20080704.4
%define	release	%mkrel %{rel}

Summary:	Lirc remotes database
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.lirc.org/remotes.tar.bz2
Source1:	lirc-remotes-qsonic.tar.bz2
Source2:	lirc-fixup-keys.c
Source3:	http://d.gardon.free.fr/vase/lirc/full/nns_full.txt
# (fc) 0.8.3-0.20080704.3mdv fix remote names for files not parsed by gnome-lirc-properties
Patch0:		lirc-fixname.patch
URL:		http://www.lirc.org/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
Requires:	lirc >= %{version}

%description
LIRC is a package that allows you to decode and send infra-red signals
of many (but not all) commonly used remote controls.

This package contains configuration files for many remotes 
supported by lirc.

%prep
%setup -q -T -c -b 0 -n remotes -a 1 
cp %{SOURCE2} %{SOURCE3} .
# no backup extension, since we copy the entire dir
%patch0 -p1 

%build

gcc -o lirc-fixup-keys lirc-fixup-keys.c `pkg-config --libs --cflags glib-2.0`

./lirc-fixup-keys nns_full.txt remotes

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r remotes/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/lirc-remotes

