%define version	3.03
%define release	%mkrel 6
%define realname	Net-Telnet
%define name	perl-%realname

Summary:	Net::Telnet perl module
Name:		%{name}
version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source:		%{realname}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%realname
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
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/*/*
%{perl_vendorlib}/Net

