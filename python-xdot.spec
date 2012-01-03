%define	module	xdot
%define name	python-%{module}
%define version 0.4
%define rel	git81b8d7d
%define release %mkrel 0.%rel

Summary:	Interactive viewer for Graphviz dot files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	LGPLv3+
Group:		Graphics
Url:		http://code.google.com/p/jrfonseca/wiki/XDot/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	graphviz, pygtk2.0
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc sample.py


