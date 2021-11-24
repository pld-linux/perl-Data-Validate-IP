#
# Conditional build:
%bcond_without	tests		# build without tests

%define		pdir	Data
%define		pnam	Validate-IP
Summary:	Perl IP address validation routines
Name:		perl-Data-Validate-IP
Version:	0.30
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Data-Validate-IP-%{version}.tar.gz
# Source0-md5:	1302d60a6a0670b4105c9b7478a37992
URL:		http://search.cpan.org/dist/Data-Validate-IP
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(NetAddr::IP)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(constant)
BuildRequires:	perl(lib)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module collects IP address validation routines to make input
validation, and untainting easier and more readable.

%prep
%setup -q -n Data-Validate-IP-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Data/Validate/IP.pm
%{_mandir}/man3/Data::Validate::IP.3pm*
