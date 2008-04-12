# TODO
# - webserver integration
# - it doesn't find any perl deps due compiled code
%include	/usr/lib/rpm/macros.perl
Summary:	The Perl Script Pages Engine
Name:		psp
Version:	0.7
Release:	0.2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://home.ircnet.de/cru/psp/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	0fb7b78cdb8a5100074788a9b69e8d64
URL:		http://home.ircnet.de/cru/psp/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	%{_prefix}/lib/cgi-bin

# No ELF objects packaged. Were not noarch only because of compiled perl code
%define		_enable_debug_packages			0

%description
The Perl Script Pages Engine.

%prep
%setup -q

%build
./build

mkdir -p man
cd src
for a in $(find -name '*.pm'); do
	p=$(echo ${a#./} | sed -e 's,/,::,g')
	pod2man ${a#./} > ../man/${p%.pm}.3pm
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man3,%{perl_vendorarch}}
install bin/psp.cgi $RPM_BUILD_ROOT%{_bindir}
# the compiled perl code is arch dependant
cp -a bin/PSP $RPM_BUILD_ROOT%{perl_vendorarch}
cp -a man/*.3pm $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL LICENSE TODO
%doc support/* html
%attr(755,root,root) %{_bindir}/psp.cgi
%{_mandir}/man3/PSP::CGI.3pm*
%{_mandir}/man3/PSP::CGI::Generate.3pm*
%{_mandir}/man3/PSP::CGI::HTTP.3pm*
%{_mandir}/man3/PSP::CGI::Info.3pm*
%{_mandir}/man3/PSP::CGI::Transform.3pm*
%{_mandir}/man3/PSP::Config.3pm*
%{_mandir}/man3/PSP::Engine.3pm*
%{perl_vendorarch}/PSP
