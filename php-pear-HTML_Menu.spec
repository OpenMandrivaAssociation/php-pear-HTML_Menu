%define		_class		HTML
%define		_subclass	Menu
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	2.1.4
Release:	10
Summary:	Generates HTML Menu from multidimensional hashes
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/HTML_Menu/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
With the %{upstream_name} class one can easily create and maintain a
navigation structure for website, configuring it via a multidimensional
hash structure. Different modes for the HTML output are supported.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-8mdv2012.0
+ Revision: 741994
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-7
+ Revision: 679345
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-6mdv2011.0
+ Revision: 613671
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.4-5mdv2010.1
+ Revision: 477866
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.1.4-4mdv2010.0
+ Revision: 441118
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-3mdv2009.1
+ Revision: 322113
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-2mdv2009.0
+ Revision: 236872
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.1.4-1mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-1mdv2008.0
+ Revision: 28876
- 2.1.4

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.1.3-1mdv2008.0
+ Revision: 15676
- 2.1.3


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-7mdv2007.0
+ Revision: 81622
- Import php-pear-HTML_Menu

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-1mdk
- initial Mandriva package (PLD import)

