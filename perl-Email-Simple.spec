#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Simple
Summary:	Email::Simple - email handling, simply
Summary(pl):	Email::Simple - obs³uga poczty elektronicznej, po prostu
Name:		perl-Email-Simple
Epoch:		1
Version:	1.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c6d3889a956b089e17aad95b1b94b71b
BuildRequires:	perl-devel >= 1:5.8.0
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
bêd±cego reakcj± na z³o¿ono¶æ i rosn±cy wspó³czynnik zapluskwienia
modu³ów Mail::*. W przeciwieñstwie do Mail::*, modu³y Email::* maj±
byæ proste w u¿yciu i w utrzymaniu, jednocze¶nie byæ szybkie i mieæ
minimalne zale¿no¶ci, a tak¿e byæ poprawne.

Metody s± rozmy¶lnie utrzymywane w minimalnej liczbie. To ma byæ
proste. Nie, nie dodamy metody X. To ma byæ proste. Dlaczego nie ma
to mo¿liwo¶ci Y? Poniewa¿ to ma byæ proste.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
