%define	name	lirc-remotes
%define	version 0.8.3
%define	rel	0.20080704.1
%define	release	%mkrel %{rel}

Summary:	Lirc remotes database
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.lirc.org/remotes.tar.bz2
Source1:	lirc-remotes-qsonic.tar.bz2
URL:		http://www.lirc.org/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	lirc >= %{version}

%description
LIRC is a package that allows you to decode and send infra-red signals
of many (but not all) commonly used remote controls.

This package contains configuration files for many remotes 
supported by lirc.

%prep
%setup -q -c -b 0 -n remotes -a 1

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r remotes/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/lirc-remotes

