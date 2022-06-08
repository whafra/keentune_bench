%define anolis_release 1

Name:           keentune-bench
Version:        1.1.0
Release:        %{?anolis_release}%{?dist}
Url:            https://gitee.com/anolis/keentune_bench
Summary:        Benchmark script running models for KeenTune
Vendor:         Alibaba
License:        MulanPSLv2
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BUildRequires:	systemd

BuildArch:      noarch

Requires:	python3-tornado
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Benchmark script running models for KeenTune

%prep
%autosetup -n %{name}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --single-version-externally-managed -O1 \
			      --prefix=%{_prefix} \
			      --root=%{buildroot} \
 			      --record=INSTALLED_FILES

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/systemd/system/
cp -f ./keentune-bench.service ${RPM_BUILD_ROOT}/usr/lib/systemd/system/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post keentune-bench.service
if [ -f "%{_prefix}/lib/systemd/system/keentune-bench.service" ]; then
    systemctl enable keentune-bench.service || :
    systemctl start keentune-bench.service || :
fi

%preun
%systemd_preun keentune-bench.service

%postun
%systemd_postun_with_restart keentune-bench.service

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md README_cn.md
%license LICENSE
%{_prefix}/lib/systemd/system/keentune-bench.service

%changelog
* Wed Mar 03 2022 Runzhe Wang <runzhe.wrz@alibaba-inc.com> - 1.1.0-1
- fix bug: update version to 1.1.0 in setup.py script.
- refactor tornado module: replace await by threadpool
- fix other bugs

* Wed Jan 01 2022 Runzhe Wang <runzhe.wrz@alibaba-inc.com> - 1.0.1
- Supporting of multiple target tuning
- Remove version limitation of tornado
- Fix some user experience issues

* Wed Jan 26 2022 Runzhe Wang <runzhe.wrz@alibaba-inc.com> - 1.0.0
- remove empty conf dir when uninstall keentune-bench
- fix bug: can not running in alinux2 and centos7
- change modify codeup address to gitee
- add keentune to systemd
- use '%license' macro
- update license to MulanPSLv2
- Initial KeenTune-bench