Summary:	Traceproto - a traceroute replacement
Summary(pl):	Traceproto - zamiennik traceroute
Name:		traceproto
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/traceproto/%{name}-%{version}.tar.gz
# Source0-md5:	265d558d8689790cdb158b7d46c88b31
URL:		http://traceproto.sourceforge.net/
BuildRequires:	libcap-devel >= 1.10
BuildRequires:	libnet-devel >= 1.1.2.1-2
BuildRequires:	libpcap-devel >= 0.8.3-1
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Traceproto is a traceroute replacement that allows the user to specify
the protocol and port to trace to. It currently supports TCP, UDP, and
ICMP traces.

%description -l pl
Traceproto jest narz�dziem do wy�wietlania trasy pakiet�w do
docelowego hosta. Obs�uguje trasowanie TCP, UDP oraz ICMP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install traceproto $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(4754,root,adm) %{_sbindir}/%{name}
%{_mandir}/man8/*