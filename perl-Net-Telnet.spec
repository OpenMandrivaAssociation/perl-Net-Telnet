%define modname	Net-Telnet
%define modver	3.03

Summary:	Net::Telnet perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%modname
Source0:	%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Net::Telnet allows you to make client connections to a TCP port and do network
I/O, especially to a port using the TELNET protocol.  Simple I/O methods such
as print, get, and getline are provided.  More sophisticated interactive
features are provided because connecting to a TELNET port ultimately means
communicating with a program designed for human interaction.  These interactive
features include the ability to specify a timeout and to wait for patterns to
appear in the input stream, such as the prompt from a shell.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{perl_vendorlib}/Net
%{_mandir}/man3/*

