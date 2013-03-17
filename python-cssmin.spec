%define		module	cssmin
Summary:	A Python port of the YUI CSS compression algorithm
Name:		python-%{module}
Version:	0.1.4
Release:	1
# same as yui?
License:	BSD
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/c/cssmin/cssmin-%{version}.tar.gz
# Source0-md5:	b9149b8a58e70cac5f7972b0dcce776f
URL:		https://pypi.python.org/pypi/cssmin/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python port of the YUI CSS compression algorithm.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cssmin
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
