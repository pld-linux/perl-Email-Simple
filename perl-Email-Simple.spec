#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Simple
Summary:	Email::Simple - email handling, simply
Summary(pl):	Email::Simple - obs�uga poczty elektronicznej, po prostu
Name:		perl-Email-Simple
Version:	1.61
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5359133be32d214115ba859dd8bfae55
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Simple is the first deliverable of the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
Mail::* modules. In contrast, Email::* modules are meant to be simple
to use and to maintain, pared to the bone, fast, minimal in their
external dependencies, and correct.

Methods are deliberately kept to a minimum. This is meant to be simple.
No, I will not add method X. This is meant to be simple. Why doesn't it
have feature Y? Because it's meant to be simple.

%description -l pl
Email::Simple to pierwszy produkt projektu "Perl Email Project",
b�d�cego reakcj� na z�o�ono�� i rosn�cy wsp�czynnik zapluskwienia
modu��w Mail::*. W przeciwie�stwie do Mail::*, modu�y Email::* maj�
by� proste w u�yciu i w utrzymaniu, jednocze�nie by� szybkie i mie�
minimalne zale�no�ci, a tak�e by� poprawne.

Metody s� rozmy�lnie utrzymywane w minimalnej liczbie. To ma by�
proste. Nie, nie dodamy metody X. To ma by� proste. Dlaczego nie ma
to mo�liwo�ci Y? Poniewa� to ma by� proste.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*