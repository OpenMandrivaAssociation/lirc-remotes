%define	name	lirc-remotes
%define	version 0.8.3
%define release	0.20130327.2

Summary:	Lirc remotes database
Name:		lirc-remotes
Version:	0.8.3
Release:	0.20130327.2
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.lirc.org/remotes.tar.bz2
#Source1:	lirc-remotes-qsonic.tar.bz2
Source2:	lirc-fixup-keys.c
Source3:	http://d.gardon.free.fr/vase/lirc/full/nns_full.txt
# (fc) 0.8.3-0.20080704.3mdv fix remote names for files not parsed by gnome-lirc-properties
Patch0:		lirc-fixname.patch
URL:		https://www.lirc.org/
BuildArch:	noarch
BuildRequires:	glib2-devel
Requires:	lirc >= %{version}

%description
LIRC is a package that allows you to decode and send infra-red signals
of many (but not all) commonly used remote controls.

This package contains configuration files for many remotes 
supported by lirc.

%prep
%setup -q -T -c -b 0 -n remotes
cp %{SOURCE2} %{SOURCE3} .
# no backup extension, since we copy the entire dir
%patch0 -p1 

%build

#gcc -o lirc-fixup-keys lirc-fixup-keys.c `pkg-config --libs --cflags glib-2.0`

#./lirc-fixup-keys nns_full.txt remotes

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r remotes/* %{buildroot}%{_datadir}/%{name}

%files
%{_datadir}/lirc-remotes

