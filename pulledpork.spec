%define name pulledpork
%define version 0.6.0

Name: %{name}
Summary: Pulledpork designed to make your snort rules fly
Version: %{version}
Release: 2
License: GPLv2
Group: Monitoring
Source: http://pulledpork.googlecode.com/files/%{name}-%{version}.tar.gz
URL:	http://code.google.com/p/pulledpork/
Requires: perl-Archive-Tar, perl-Crypt-SSLeay

%description
PulledPork designed to make your Snort rules fly with the intent of handling
all rules.

%prep
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


%changelog
* Wed Jun 15 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.6.0-1mdv2011.0
+ Revision: 685417
- first mandriva version
- Created package structure for pulledpork.

