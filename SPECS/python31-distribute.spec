
%define pyver 31 
%define pybasever 3.1

%define __python /usr/bin/python%{pybasever}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}


%define real_name python-distribute

Name:           python%{pyver}-distribute
Version:        0.6.35
Release:        1.ius%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages
Vendor:         IUS Community Project 
Group:          Development/Languages
License:        PSFL/ZPL
URL:            http://bitbucket.org/tarek/distribute/wiki/Home 
Source0:        http://pypi.python.org/packages/source/d/distribute/distribute-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pyver}, python%{pyver}-devel, python%{pyver}-tools
Requires:       python%{pyver}, python%{pyver}-devel
Provides:       python%{pyver}-setuptools


%description
Distribute is a fork of the Setuptools project. It is intended to replace 
Setuptools as the standard method for working with Python module distributions.

Setuptools was a collection of enhancements to the Python distutils that 
allowed you to more easily build and distribute Python packages.  It has since
been abandoned and there are no plans for supporting Python 3.


%prep
%setup -q -n distribute-%{version}

find -name '*.py' -print0 | xargs -0 sed -i '1s|^#!python|#!%{__python}|'


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} %{buildroot}%{_bindir}

%{__python} setup.py install -O1 --skip-build \
    --root $RPM_BUILD_ROOT \
    --single-version-externally-managed
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.exe' | xargs rm -f
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.txt' | xargs chmod -x

mv %{buildroot}%{_bindir}/easy_install %{buildroot}%{_bindir}/easy_install-%{pybasever}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc *.txt 
%{_bindir}/easy_install-%{pybasever}
%{python_sitelib}/distribute-%{version}-py%{pybasever}.egg-info
%{python_sitelib}/easy_install.py*
%{python_sitelib}/site.py*
%{python_sitelib}/pkg_resources.py*
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-0.6c11-py%{pybasever}.egg-info
%{python_sitelib}/setuptools.pth
%{python_sitelib}/_markerlib

%changelog
* Mon Feb 18 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.35-1.ius
- Latest sources from upstream

* Wed Jan 02 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.34-1.ius
- Latest sources from upstream

* Mon Dec 31 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.33-1.ius
- Latest sources from upstream

* Tue Nov 27 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.32-1.ius
- Latest sources from upstream

* Mon Nov 26 2012 Ben Harper <ben.harper@rackspace.com> - 0.6.31-1.ius
- Latest sources from upstream

* Mon Oct 22 2012 Ben Harper <ben.harper@rackspace.com> - 0.6.30-1.ius
- Latest sources from upstream

* Mon Jul 23 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.28-1.ius
- Latest sources from upstream

* Wed May 23 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 0.6.27-3.ius
- Fix release version

* Mon May 21 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 0.6.27-1.ius
- Latest upstream source

* Mon Apr 16 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.26-2.ius
- Rebuiding against latest python31

* Mon Apr 09 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.26-1.ius
- Latest sources from upstream

* Tue Mar 13 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.25-1.ius
- Latest sources from upstream
- spaces in names caused find to fail, using -print0 now

* Tue Oct 18 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.24-1.ius
- Latest sources from upstream

* Mon Aug 22 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.21-1.ius
- Latest sources from upstream
  http://pypi.python.org/pypi/distribute#id2

* Mon Jun 13 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.19-2.ius
- Rebuilding against latest python 3.1.4

* Thu Jun 02 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.19-1.ius
- Latest sources from upstream

* Tue May 31 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.17-1.ius
- Latest sources from upstream

* Wed May 04 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.16-1.ius
- Latest sources from upstream

* Fri Apr 01 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.15-1.ius
- Latest sources from upstream

* Tue Oct 20 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.6.6-1.ius
- Porting spec from setuptools to distribute
- Rebuilding for python31

* Thu Jul 23 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.6c9-1.1.ius
- Rebuilding for IUS

* Wed May 20 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.6c9-1.1.rs
- Drop /opt install, do side-by-side instead.

* Wed May 13 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.6c9-1.rs
- Building for python26 (/opt/rackspace)
- Source update.

* Tue Apr 14 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.6c5-2.1.rs
- Rebuild 

* Thu Jan 17 2008 James Antill <james.antill@redhat.com> - 0.6c5-2
- Import into RHEL-5
- Related: rhbz#384691

* Sun Jan 28 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c5-1
- Upstream 0.6c5 (known bugs, but the promised 0.6c6 is taking too long)

* Tue Dec 05 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c3-1
- Upstream 0.6c3 (#218540, thanks to Michel Alexandre Salim for the patch)

* Tue Sep 12 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c2-1
- Upstream 0.6c2
- Ghostbusting

* Mon Jul 31 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c1-2
- Set perms on license files (#200768)

* Sat Jul 22 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c1-1
- Version 0.6c1

* Wed Jun 28 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6b3-1
- Taking over from Ignacio
- Version 0.6b3
- Ghost .pyo files in sitelib
- Add license files
- Remove manual python-abi, since we're building FC4 and up
- Kill .exe files

* Wed Feb 15 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6a10-1
- Upstream update

* Mon Jan 16 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6a9-1
- Upstream update

* Sat Dec 24 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6a8-1
- Initial RPM release
