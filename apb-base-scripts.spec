%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: apb-base-scripts
Version:	1.4.2
Release:	1%{build_timestamp}%{?dist}
Summary:	Scripts for the apb-base container image

License:	ASL 2.0
URL:		https://github.com/fusor/apb-examples
Source0:	https://github.com/fusor/apb-examples/archive/%{name}-%{version}.tar.gz
BuildArch:  noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/ansible
mkdir -p %{buildroot}%{_sysconfdir}/apb-secrets
mkdir -p %{buildroot}/opt/apb/.kube
mkdir -p %{buildroot}/opt/apb/inventory
mkdir -p %{buildroot}/opt/apb/env
install -m 644 files/opt/apb/.ansible.cfg %{buildroot}/opt/apb/.ansible.cfg
install -m 644 files/opt/apb/inventory/hosts %{buildroot}/opt/apb/inventory/hosts
install -m 644 files/opt/apb/env/settings %{buildroot}/opt/apb/env/settings
install -m 775 files/opt/apb/.kube/config %{buildroot}/opt/apb/.kube/config
install -m 755 files/usr/bin/test-retrieval-init %{buildroot}%{_bindir}
install -m 755 files/usr/bin/test-retrieval %{buildroot}%{_bindir}
install -m 755 files/usr/bin/entrypoint.sh %{buildroot}%{_bindir}

%files
%doc
%{_bindir}/test-retrieval-init
%{_bindir}/test-retrieval
%{_bindir}/entrypoint.sh
%dir %{_sysconfdir}/apb-secrets
%dir %{_sysconfdir}/ansible
%attr(0775, apb, root) %dir /opt/apb/env
%attr(0664, apb, root) /opt/apb/.ansible.cfg
%attr(0664, apb, root) /opt/apb/inventory/hosts
%attr(0664, apb, root) /opt/apb/env/settings
%attr(0775, apb, root) /opt/apb/.kube/config

%pre
getent passwd apb >/dev/null || \
  /usr/sbin/useradd -u 1001 -r -g 0 -M -d /opt/apb -b /opt/apb -s /sbin/nologin -c "apb user" apb

%changelog
* Fri Feb 01 2019 Jason Montleon <jmontleo@redhat.com> 1.4.2-1
- Add jmespath to apb-base (#54) (dzager@redhat.com)
- Validate and print usage in case of wrong entrypoint usage (#49)
  (rgolan@redhat.com)
- Disable buffered output (#52) (jmontleo@redhat.com)
- Fix apb-base canary (jmontleo@redhat.com)
- add v3.10 and v3.11 Dockerfiles (jmontleo@redhat.com)

* Fri Sep 14 2018 jesus m. rodriguez <jmrodri@gmail.com> 1.4.1-1
- Prepare branch for 4.0 release (#48) (jmrodri@gmail.com)
- Add git to fix ansible-galaxy - issue 1073 (jmontleo@redhat.com)

* Mon Aug 06 2018 David Zager <david.j.zager@gmail.com> 1.3.6-1
- Bug 1612004: Remove dependency on jq (david.j.zager@gmail.com)

* Wed Aug 01 2018 David Zager <david.j.zager@gmail.com> 1.3.5-1
- Create user and Set file permissions in the rpm (#32) (jmontleo@redhat.com)

* Fri Jul 27 2018 David Zager <david.j.zager@gmail.com> 1.3.4-1
- Accept galaxy_url parameter from broker (#43) (dzager@redhat.com)

* Fri Jul 27 2018 David Zager <david.j.zager@gmail.com> 1.3.3-1
- Copy actions instead of moving (#42) (dzager@redhat.com)

* Thu Jul 26 2018 David Zager <david.j.zager@gmail.com> 1.3.2-1
- Add settings for ansible-runner (#41) (dzager@redhat.com)

* Mon Jul 23 2018 David Zager <david.j.zager@gmail.com> 1.3.1-1
- Use ansible-runner in APB Base (#36) (dzager@redhat.com)
- Revert "Use epel-testing for apb-base:latest" (dzager@redhat.com)
- Use epel-testing for apb-base:latest (david.j.zager@gmail.com)
- Bump version (#35) (dzager@redhat.com)
- manually install proper version of urllib3 (fabian@fabianism.us)
- Hardcode the inventory to /etc/ansible/hosts
  (rhallisey@localhost.localdomain)

* Wed Apr 25 2018 David Zager <david.j.zager@gmail.com> 1.2.6-1
- remove file glob and replace with proper Dockerfile syntax
  (jmontleo@redhat.com)
- Copy .kube directory to canary image (jmontleo@redhat.com)

* Fri Apr 20 2018 Jason Montleon <jmontleo@redhat.com> 1.2.5-1
- revert ownership settings on files (jmontleo@redhat.com)

* Fri Apr 20 2018 Jason Montleon <jmontleo@redhat.com> 1.2.4-1
- fix typos (jmontleo@redhat.com)

* Fri Apr 20 2018 Jason Montleon <jmontleo@redhat.com> 1.2.3-1
- fix RPM conflict by placing these files elsewhere (jmontleo@redhat.com)

* Thu Apr 19 2018 David Zager <david.j.zager@gmail.com> 1.2.2-1
- Bug 1565241 - stops using bash "-x" unless in debug mode (#25)
  (mhrivnak@hrivnak.org)
- Use 644 (david.j.zager@gmail.com)
- Include ansible config in rpm spec (david.j.zager@gmail.com)
- Prevents ansible from trying to create retry files, which can't be used
  anyway. (mhrivnak@redhat.com)

* Mon Apr 09 2018 David Zager <david.j.zager@gmail.com> 1.2.1-1
- Bump version for 3.10 (david.j.zager@gmail.com)
- Add jmespath to canary image (david.j.zager@gmail.com)

* Fri Feb 02 2018 David Zager <david.j.zager@gmail.com> 1.1.5-1
- Bug 1533425 - return error when no action found (jmrodri@gmail.com)

* Mon Jan 08 2018 David Zager <david.j.zager@gmail.com> 1.1.4-1
- Fixing tito releasers (david.j.zager@gmail.com)

* Mon Jan 08 2018 David Zager <david.j.zager@gmail.com> 1.1.3-1
- Update tito releasers (david.j.zager@gmail.com)

* Thu Dec 21 2017 Jason Montleon <jmontleo@redhat.com> 1.1.2-1
- Remove erroneous copy in nightly, install it (david.j.zager@gmail.com)
- Fix location where kube config is copied (david.j.zager@gmail.com)
- Fixing dockerfiles after moving kube config (david.j.zager@gmail.com)
- Move kubeconfig based on convention (david.j.zager@gmail.com)
- Replace oc login with kube config (david.j.zager@gmail.com)

* Mon Dec 04 2017 Jason Montleon <jmontleo@redhat.com> 1.1.1-1
- Remove bind files from files section of rpm spec (david.j.zager@gmail.com)
- Update the RPM spec for now deleted files (david.j.zager@gmail.com)
- Add runtime label to apb-base (david.j.zager@gmail.com)
- Canary apb-base should use latest asb modules (david.j.zager@gmail.com)
- Remove bind credential scripts (david.j.zager@gmail.com)
- bump release (#6) (jmrodri@gmail.com)

* Tue Nov 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.5-1
- Bug 1510299 add missing /etc/apb-secrets (jmontleo@redhat.com)
- Fixed link to ansible-asb-modules for canary (cchase@redhat.com)
- Adding Apache License Version 2.0 file (matzew@apache.org)
- update tito releasers (jmontleo@redhat.com)

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- 1498185 - Removed version label from apb-base (dymurray@redhat.com)

* Tue Sep 19 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- new package built with tito

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- apply role path on the command line (#115) (jmontleo@redhat.com)
- Fix canary build and stop overwriting files rpm RPM's in latest (#114)
  (jmontleo@redhat.com)

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

