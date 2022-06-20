%define anolis_release 1

#
# spec file for package KeenTune-bench
#

Name:           keentune-bench
Version:        1.2.1
Release:        %{?anolis_release}%{?dist}
Url:            https://gitee.com/anolis/keentune_bench
Summary:        Benchmark script running models for KeenTune
License:        MulanPSLv2
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch

Vendor:         Alibaba

%description
Benchmark script running models for KeenTune

%prep
%setup -q -n %{name}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --single-version-externally-managed -O1 --prefix=%{_prefix} --root=%{buildroot} --record=INSTALLED_FILES
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/systemd/system/
cp -f ./keentune-bench.service ${RPM_BUILD_ROOT}/usr/lib/systemd/system/
install -D -m644 man/keentune-bench.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/keentune-bench.8
install -D -m644 man/keentune-bench.conf.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/keentune-bench.conf.5

%clean
rm -rf $RPM_BUILD_ROOT

%postun
CONF_DIR=%{_sysconfdir}/keentune/conf
if [ "$(ls -A $CONF_DIR)" = "" ]; then
        rm -rf $CONF_DIR
fi

%files -f INSTALLED_FILES
%license LICENSE
%{_prefix}/lib/systemd/system/keentune-bench.service
%{_mandir}/man8/keentune-bench.8*
%{_mandir}/man5/keentune-bench.conf.5*

%changelog
* Mon Jun 20 2022 Runzhe Wang <runzhe.wrz@alibaba-inc.com> - 1.2.1-1
- update docs

* Wed Jan 26 2022 lilinjie <lilinjie@uniontech.com> - 1.0.0-6
- remove empty conf dir when uninstall keentune-bench

* Wed Dec 15 2021 Runzhe Wang <15501019889@126.com> - 1.0.0-5
- fix bug: can not running in alinux2 and centos7
- change modify codeup address to gitee

* Wed Dec 01 2021 Runzhe Wang <15501019889@126.com> - 1.0.0-4
- add keentune to systemd

* Mon Nov 15 2021 Runzhe Wang <15501019889@126.com> - 1.0.0-3
- fix: wrong license in setup.py

* Wed Nov 10 2021 Runzhe Wang <15501019889@126.com> - 1.0.0-2
- use '%license' macro
- update license to MulanPSLv2

* Wed Aug 18 2021 Runzhe Wang <15501019889@126.com> - 1.0.0-1
- Initial KeenTune-bench
