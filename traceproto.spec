Summary:	Traceproto is a traceroute replacement
Summary(pl):	Traceproto jest zastêpnikiem traceroute
Name:		traceproto
Version:	0.9.2
%define         _beta           beta0
%define         mversion        %{version}%{_beta}
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/sourceforge/traceproto/%{name}-%{mversion}.tar.gz
# Source0-md5:	2047f6802706a5c2b3ac5c93d6cb277e
URL:		http://traceproto.sourceforge.net/index.php
BuildRequires:	libpcap-devel >= 0.8.3-1
BuildRequires:	libnet-devel >= 1.1.2.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Traceproto is a traceroute replacement that allows the user to specify
the protocol and port to trace to. It currently supports TCP, UDP, and
ICMP traces.

%description -l pl
Traceproto jest narzêdziam do wy¶wietlania trasy pakietów do
docelowego hosta. Obs³uguje trasowanie TCP, UDP oraz ICMP.

%prep
%setup -q -n %{name}-%{mversion} -a 0

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
