%define name    cvc3
%define version 2.4.1 

%define lib_name_orig libcvc3
%define major 5
%define devprovname %mklibname %{name}
# Note the underscore: name ends with a number, we don't want "libcvc35" here (approach taken from libdc1394 package)
%define libname %mklibname %{name}_ %major
%define develname %mklibname -d %{name}_ %major

Name:           %{name} 
Summary:        Automatic theorem prover for Satisfiability Modulo Theories
Version:        %{version} 
Release:        %mkrel 0
Source0:        http://cs.nyu.edu/acsys/cvc3/releases/%{version}/cvc3-%{version}.tar.gz
URL:            http://cs.nyu.edu/acsys/cvc3/index.html
Patch0:		cvc3-no-as-needed.patch

Group:          Sciences/Computer science 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        BSD
# This library package is described in this very spec
Requires:       %{libname} = %{version}
BuildRequires:	glibc-static-devel libstdc++-static-devel
# CVC3, by default, statically compiles with GMP library.  This should be changed to dynamic linkage, though there's no matching configure opiton that works for sure.
BuildRequires:	libgmp-devel

%description
CVC3 is an automatic theorem prover for Satisfiability Modulo Theories (SMT)
problems. It can be used to prove the validity (or, dually, the satisfiability)
of first-order formulas in a large number of built-in logical theories and
their combination.

CVC3 contains built-in support for theories for rational and integer linear
arithmetic, arrays, tuples, records, inductive data types, bit vectors, and
equality over uninterpreted function symbols.  CVC3 also supports quantifiers.

%package -n %{libname}
Summary:        Shared libraries for automatic SMT theorem proving
Group:          Sciences/Computer science 
License:        BSD

%description -n %{libname}
CVC3 is an automatic theorem prover for Satisfiability Modulo Theories (SMT)
problems. It can be used to prove the validity (or, dually, the satisfiability)
of first-order formulas in a large number of built-in logical theories and
their combination.

CVC3 contains built-in support for theories for rational and integer linear
arithmetic, arrays, tuples, records, inductive data types, bit vectors, and
equality over uninterpreted function symbols.  CVC3 also supports quantifiers.

This is a shared library with CVC3 for use in external applications.

%package -n %{develname}
Summary:        Library and includes to use automatic SMT theorem proving
Group:          Sciences/Computer science 
License:        BSD
Requires:	%{libname} = %{version}
Provides:	%{devprovname}-devel = %{version}-%{release}

%description -n %{develname}
CVC3 is an automatic theorem prover for Satisfiability Modulo Theories (SMT)
problems. It can be used to prove the validity (or, dually, the satisfiability)
of first-order formulas in a large number of built-in logical theories and
their combination.

CVC3 contains built-in support for theories for rational and integer linear
arithmetic, arrays, tuples, records, inductive data types, bit vectors, and
equality over uninterpreted function symbols.  CVC3 also supports quantifiers.

This is a development package for CVC3 shared library.

%prep 
%setup -q
%patch0 -p2 -b .makefile

%build 
%configure --prefix=/usr --includedir=/usr/include/cvc3 --enable-dynamic
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}%{_libdir}/pkgconfig

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean 
rm -rf %{buildroot}

%files -n %{libname}
%{_libdir}/%{lib_name_orig}*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_prefix}/include/cvc3/*.h

%files 
%doc LICENSE PEOPLE README
%attr(0755,root,root) %{_bindir}/cvc3 

