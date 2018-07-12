%define modname	Net-Telnet
%define modver	3.04

Summary:	Net::Telnet perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/Net::Telnet
Source0:	https://cpan.metacpan.org/authors/id/J/JR/JROGERS/Net-Telnet-%{modver}.tar.gz
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

