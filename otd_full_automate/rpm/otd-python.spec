# File Path
%global	install_path	/ORACLE_HOME/

%define	name		traffic-director
%define	version		12.2.1
%define	release		12c
%define debug_package	%{nil}
%define	_sbindir	/sbin
%define	_libdir		/%{_lib}
%define __jar_repack	%{nil}
%define __arch_install_post	%{nil}
%define __os_install_post	%{nil}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Installation for OTD 12.2.1 Collocated Server
Group:		Development/Tools
License:	GPL
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_builddir}/%{name}-root
AutoReqProv:	no
Requires:	python

%description
The package otd traffic-director

%prep
%setup -q
python otd_installationSetUp.py %{install_path}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{install_path}
cp -rf %{install_path}* $RPM_BUILD_ROOT%{install_path}
chmod 757 -R $RPM_BUILD_ROOT%{install_path}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%{install_path}OPatch
%{install_path}bin
%{install_path}cfgtoollogs
%{install_path}crs
%{install_path}css
%{install_path}has
%{install_path}install
%{install_path}inventory
%{install_path}jlib
%{install_path}ldap
%{install_path}lib
%{install_path}network
%{install_path}nls
%{install_path}oracle_common
%{install_path}otd
%{install_path}oui
%{install_path}plsql
%{install_path}plugins
%{install_path}precomp
%{install_path}rdbms
%{install_path}slax
%{install_path}sqlplus
%{install_path}srvm
%{install_path}webgate
%{install_path}wlserver
%{install_path}xdk
%{install_path}root.sh
%{install_path}oraInst.loc
%{install_path}/oracore/*

%changelog
* Wed Jul 13 2016 I Made Sanadhi Sutandi <i.made.sanadhi.sutandi@cern.ch> - 12.2.1-12c
- create RPM
