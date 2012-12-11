%define	module	xdot
%define rel	git81b8d7d
%define release 0.%rel

Summary:	Interactive viewer for Graphviz dot files
Name:		python-%{module}
Version:	0.4
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	LGPLv3+
Group:		Graphics
Url:		http://code.google.com/p/jrfonseca/wiki/XDot/
BuildArch:	noarch
Requires:	graphviz
Requires:	pygtk2.0
BuildRequires:	python-setuptools
BuildRequires:	python-devel

%description 
xdot is an interactive viewer for graphs written in
Graphviz's dot language.

It internally uses Graphviz's xdot output format as an
intermediate format, and PyGTK and Cairo for rendering.

xdot can be used either as a standalone application from 
the command line, or as a library embedded in your Python 
application.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc sample.py




%changelog
* Tue Jan 03 2012 Lev Givon <lev@mandriva.org> 0.4-0.git81b8d7dmdv2011.0
+ Revision: 749031
- imported package python-xdot

