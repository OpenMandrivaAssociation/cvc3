%define lib_name_orig libcvc3
%define major 5
%define devprovname %mklibname %{name}
# Note the underscore: name ends with a number, we don't want "libcvc35" here (approach taken from libdc1394 package)
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname -d %{name}_ %{major}

Name:		cvc3
Summary:	Automatic theorem prover for Satisfiability Modulo Theories
Version:	2.4.1 
Release:	2
Group:		Sciences/Computer science 
License:	BSD
URL:		http://cs.nyu.edu/acsys/cvc3/index.html
Source0:	http://cs.nyu.edu/acsys/cvc3/releases/%{version}/cvc3-%{version}.tar.gz
Patch0:		cvc3-no-as-needed.patch
BuildRequires:	glibc-static-devel
BuildRequires:	libstdc++-static-devel
BuildRequires:	gmp-devel
BuildRequires:  bison
BuildRequires:  flex
# This library package is described in this very spec
Requires:       %{libname} = %{version}

%description
CVC3 is an automatic theorem prover for Satisfiability Modulo Theories (SMT)
problems. It can be used to prove the validity (or, dually, the satisfiability)
of first-order formulas in a large number of built-in logical theories and
their combination.

CVC3 contains built-in support for theories for rational and integer linear
arithmetic, arrays, tuples, records, inductive data types, bit vectors, and
equality over uninterpreted function symbols.  CVC3 also supports quantifiers.

%package -n %{libname}
Summary:	Shared libraries for automatic SMT theorem proving
Group:		Sciences/Computer science 

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
Summary:	Library and includes to use automatic SMT theorem proving
Group:		Sciences/Computer science 
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
%makeinstall
rm -rf %{buildroot}%{_libdir}/pkgconfig

# Fix unstripped-binary-or-object rpmlint error
chmod 0755 %{buildroot}%{_libdir}/%{lib_name_orig}*.so.%{major}*

%files -n %{libname}
%{_libdir}/%{lib_name_orig}*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_prefix}/include/cvc3/*.h

%files 
%doc LICENSE PEOPLE README
%attr(0755,root,root) %{_bindir}/cvc3 

