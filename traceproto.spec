Summary:	Traceproto - a traceroute replacement
Summary(pl):	Traceproto - zamiennik traceroute
Name:		traceproto
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/traceproto/%{name}-%{version}.tar.gz
# Source0-md5:	7996fdc9855bf03b90e9d898d303f1df
URL:		http://traceproto.sourceforge.net/index.php
BuildRequires:	libnet-devel >= 1.1.2.1-2
BuildRequires:	libpcap-devel >= 0.8.3-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Traceproto is a traceroute replacement that allows the user to specify
the protocol and port to trace to. It currently supports TCP, UDP, and
ICMP traces.

%description -l pl
Traceproto jest narzêdziem do wy¶wietlania trasy pakietów do
docelowego hosta. Obs³uguje trasowanie TCP, UDP oraz ICMP.

%prep
%setup -q

%build
%configure
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
