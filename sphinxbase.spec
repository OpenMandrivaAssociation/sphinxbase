Name: sphinxbase
Version: 0.7
Release: 2
BuildRoot: %{_tmppath}/%{name}-%{version}
Summary: Base files of CMU Sphinx Recognition System
Group: System/Libraries
License: BSD and LGPLv2+
Url: https://cmusphinx.sourceforge.net/
Source: http://downloads.sourceforge.net/cmusphinx/%name-%version.tar.gz
BuildRequires: bison python-devel
Patch0: sphinxbase.patch

%description
The CMU Sphinx Recognition System is a library and a set
of examples and utilities for speech recognition.

This package will install the cmu-sphinx library and some examples.

%package devel
Summary: Header files for developing with sphinxbase
Group: Development/C
Requires: %{name} = %{version}-%{release}, pkgconfig
Provides: %{name}-devel = %{version}-%{release}

%description devel
Header files for developing with sphinxbase

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .lda

%build
./autogen.sh
%configure
%make

%install
rm -fr %{buildroot}
%makeinstall

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/sphinx*
%{_libdir}/libsphinx*
%{_libdir}/pkgconfig/%{name}.pc
%{py_platsitedir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}


%changelog
* Thu Apr 28 2011 zamir <zamir@mandriva.org> 0.7-1mdv2011.0
+ Revision: 659853
- fix LDA train bug

* Wed Apr 20 2011 zamir <zamir@mandriva.org> 0.7-0
+ Revision: 656171
- add build req
- new release
- new release

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-3
+ Revision: 645885
- relink against libmysqlclient.so.18

* Fri Feb 11 2011 zamir <zamir@mandriva.org> 0.6.1-2
+ Revision: 637303
- changed provide information

* Sat Nov 27 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.6.1-1mdv2011.0
+ Revision: 601629
- Added python-devel as BR.
- Use proper group
- Use proper python sitedir.

  + zamir <zamir@mandriva.org>
    - firts build
    - Created package structure for sphinxbase.

