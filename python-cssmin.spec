%define		module	cssmin
Summary:	A Python port of the YUI CSS compression algorithm
Name:		python-%{module}
Version:	0.2.0
Release:	1
# same as yui?
License:	BSD
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/c/cssmin/cssmin-%{version}.tar.gz
# Source0-md5:	c2798658a4f69663365a3e70c3b8250b
URL:		https://pypi.python.org/pypi/cssmin/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python port of the YUI CSS compression algorithm.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cssmin
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
