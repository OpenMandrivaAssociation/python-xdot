%define	module	xdot
#%define rel	git81b8d7d

Summary:	Interactive viewer for Graphviz dot files
Name:		python-%{module}
Version:	0.8
Release:	1
Source0:	https://github.com/jrfonseca/xdot.py/archive/%{version}.tar.gz
License:	LGPLv3+
Group:		Graphics
Url:		https://code.google.com/p/jrfonseca/wiki/XDot/
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
%setup -q -n xdot.py-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc sample.py

