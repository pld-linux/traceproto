%define		pre	beta0
Summary:	Traceproto - a traceroute replacement
Summary(pl.UTF-8):	Traceproto - zamiennik traceroute
Name:		traceproto
Version:	1.1.2
Release:	0.%{pre}.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/traceproto/%{name}-%{version}%{pre}.tar.gz
# Source0-md5:	621d69c14ff69243353d743f7beb6c8f
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

%description -l pl.UTF-8
Traceproto jest narzędziem do wyświetlania trasy pakietów do
docelowego hosta. Obsługuje trasowanie TCP, UDP oraz ICMP.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%configure \
	--bindir=%{_sbindir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(4754,root,adm) %{_sbindir}/%{name}
%{_mandir}/man8/*
