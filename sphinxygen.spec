#
# Conditional build:
%bcond_with	tests	# testing (missing test data in sdist)

Summary:	A script to generate Sphinx ReST from Doxygen XML
Summary(pl.UTF-8):	Skrypt do generowania sphinxowego ReSTa z XML-a Doxygena
Name:		sphinxygen
Version:	1.0.10
Release:	1
License:	ISC
Group:		Development/Tools
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.gz
# Source0-md5:	29d15a4a2684abac843918d110f09b77
URL:		https://gitlab.com/drobilla/sphinxygen
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:61.2
%if %{with tests}
BuildRequires:	python3-html5lib
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinxygen is a Python module/script that generates Sphinx markup to
describe a C API, from an XML description extracted by Doxygen.

%description -l pl.UTF-8
Sphinxygen to moduł/skrypt Pythona, generujący znaczniki Sphinksa do
opisu API w języku C z opisu XML wydobytego przez Doxygena.

%prep
%setup -q

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%attr(755,root,root) %{_bindir}/sphinxygen
%{py3_sitescriptdir}/sphinxygen
%{py3_sitescriptdir}/sphinxygen-%{version}.dist-info
