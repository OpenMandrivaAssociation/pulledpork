%define name pulledpork
%define version 0.6.0

Name: %{name}
Summary: Pulledpork designed to make your snort rules fly
Version: %{version}
Release: %mkrel 1
License: GPLv2
Group: Monitoring
Source: http://pulledpork.googlecode.com/files/%{name}-%{version}.tar.gz
URL:	http://code.google.com/p/pulledpork/
Requires: perl-Archive-Tar, perl-Crypt-SSLeay
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
PulledPork designed to make your Snort rules fly with the intent of handling all rules.

%prep
rm -rf %{buildroot}
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
mkdir -p %{buildroot}%{_bindir}
mv etc/* %{buildroot}%{_sysconfdir}/%{name}/
install -m 755 pulledpork.pl %{buildroot}%{_bindir}/

%files
%defattr(0755,root,root)
%{_bindir}/pulledpork.pl
%{_sysconfdir}/%{name}/
%doc README LICENSE doc/*

%clean
rm -rf $RPM_BUILD_ROOT
