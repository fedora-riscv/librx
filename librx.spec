Summary: POSIX regexp functions
Name: librx
Version: 1.5
Release: 24%{?dist}
License: GPLv2+
URL: http://www.gnu.org/software/rx/rx.html
Group: Applications/Text
# Originally downloaded from ftp://ftp.gnu.org/gnu/rx/rx-1.5.tar.bz2
# The FSF no longer offers this code.
Source0: rx-%{version}.tar.bz2
Patch0: rx-1.5-shared.patch
Patch1: rx-1.5-texinfo.patch
Patch2: librx-1.5-libdir64.patch
Patch3: rx-1.5-libtoolmode.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: texinfo, libtool

%description
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

%package devel
Summary: POSIX regexp functions, developers library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

This package contains files needed for development with librx.

%prep
%setup -q -n rx-%{version}
%patch0 -p1
%patch1 -p1 -b .texipatch
%ifarch x86_64 s390x ia64 %{power64} alpha sparc64 aarch64 
%patch2 -p1 -b .64bit
%endif
%patch3 -p1 -b .libtoolmode

%build
%configure
make %{?_smp_mflags}
make doc/rx.info

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
make install DESTDIR=${RPM_BUILD_ROOT}
install -m 644 doc/rx.info ${RPM_BUILD_ROOT}%{_infodir}
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/librx.la
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/librx.a
chmod -x ${RPM_BUILD_ROOT}%{_includedir}/rxposix.h

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/rx.info \
    %{_infodir}/dir 2>/dev/null || :

%postun devel
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/rx.info \
    %{_infodir}/dir 2>/dev/null || :
fi

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc ANNOUNCE BUILDING COOKOFF rx/ChangeLog
%{_includedir}/*
%{_infodir}/*
%{_libdir}/*.so

%changelog
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 1.5-22
- Update 64bit arch list

* Wed Jan 15 2014 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.5-21
- Remove single trailing space in -devel post scriptlet which caused a file
  named " " in / to appear on install.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-19
- Update 64bit arch list

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-15
- don't package static lib (resolves bz 556072)

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-14
- take URL out of Source0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Karsten Hopp <karsten@redhat.com> 1.5-12.1
- add s390x to 64bit archs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-11
- pass modes to libtool

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5-10
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-9
- fix license, rebuild for BuildID

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-8
- fix bz 200090

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7
- fix bz 197717
- bump for FC-6

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-6
- bump for FC-5

* Mon May  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-5
- remove hardcoded dist tags

* Sun May  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-4
- Fix 64 bit arches to install to the right libdir

* Thu May  5 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-3
- add BuildRequires: texinfo

* Sun Apr 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-2
- use dist tag

* Sat Apr 23 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-1
- new package, based on Alexey Voinov's package from AltLinux
