#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	Simple
Summary:	Email::Simple - email handling, simply
Summary(pl.UTF-8):	Email::Simple - obsługa poczty elektronicznej, po prostu
Name:		perl-Email-Simple
Version:	2.218
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af643390d7bec05428c3d809f538072a
URL:		https://search.cpan.org/dist/Email-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%{?with_tests:BuildRequires:	perl-Email-Date-Format}
Obsoletes:	perl-Email-Simple-Creator
Requires:	perl-Email-Date-Format
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Simple is the first deliverable of the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
Mail::* modules. In contrast, Email::* modules are meant to be simple
to use and to maintain, pared to the bone, fast, minimal in their
external dependencies, and correct.

Methods are deliberately kept to a minimum. This is meant to be
simple. No, I will not add method X. This is meant to be simple. Why
doesn't it have feature Y? Because it's meant to be simple.

%description -l pl.UTF-8
Email::Simple to pierwszy produkt projektu "Perl Email Project",
będącego reakcją na złożoność i rosnący współczynnik zapluskwienia
modułów Mail::*. W przeciwieństwie do Mail::*, moduły Email::* mają
być proste w użyciu i w utrzymaniu, jednocześnie być szybkie i mieć
minimalne zależności, a także być poprawne.

Metody są rozmyślnie utrzymywane w minimalnej liczbie. To ma być
proste. Nie, nie dodamy metody X. To ma być proste. Dlaczego nie ma to
możliwości Y? Ponieważ to ma być proste.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's/(use 5.005)(03;)/$1_$2/' lib/Email/Simple.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/Simple.pm
%{perl_vendorlib}/Email/Simple/*.pm
%{_mandir}/man3/Email::Simple*.3pm*
