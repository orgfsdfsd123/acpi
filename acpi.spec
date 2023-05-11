Summary:	Command-line ACPI client
Name:		acpi
Version:	1.7
Release:	1
License:	GPLv2+
Source0:	http://downloads.sourceforge.net/project/acpiclient/acpiclient/%{version}/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/acpiclient/

BuildRequires:  gcc
BuildRequires: make
%description
Linux ACPI client is a small command-line program that attempts to
replicate the functionality of the 'old' apm command on ACPI systems.
It includes battery and thermal information.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/acpi
%{_mandir}/man1/acpi.1*

%changelog
* Thu Feb 16 2023 lichaoran <pkwarcraft@hotmail.com> - 1.7-1
- Init package
