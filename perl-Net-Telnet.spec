%define upstream_name	 Net-Telnet
%define upstream_version 3.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Net::Telnet perl module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Telnet allows you to make client connections to a TCP port and do network
I/O, especially to a port using the TELNET protocol.  Simple I/O methods such
as print, get, and getline are provided.  More sophisticated interactive
features are provided because connecting to a TELNET port ultimately means
communicating with a program designed for human interaction.  These interactive
features include the ability to specify a timeout and to wait for patterns to
appear in the input stream, such as the prompt from a shell.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_mandir}/*/*
%{perl_vendorlib}/Net


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.30.0-5mdv2012.0
+ Revision: 765538
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.30.0-4
+ Revision: 764061
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3.30.0-3
+ Revision: 763097
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.30.0-2
+ Revision: 667281
- mass rebuild

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.30.0-1mdv2011.0
+ Revision: 407882
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.03-8mdv2009.1
+ Revision: 351800
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.03-7mdv2009.0
+ Revision: 223907
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 3.03-6mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 3.03-6mdv2008.0
+ Revision: 19236
- rebuild


* Fri Feb 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.03-5mdk
- Rebuild
- Fix URL, description and summary, remove MANIFEST
- Add tests

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.03-4mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Fri Jul 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.03-3mdk
- don't require perl, rpm will figure it out by itself
- drop Prefix tag, use %%{_prefix}
- buildrequires

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.03-2mdk
- rebuild for new auto{prov,req}

