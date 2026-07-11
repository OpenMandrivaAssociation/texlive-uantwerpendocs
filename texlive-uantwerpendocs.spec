%global tl_name uantwerpendocs
%global tl_revision 78619

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.12
Release:	%{tl_revision}.1
Summary:	Course texts, master theses, and exams in University of Antwerp style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uantwerpendocs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uantwerpendocs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uantwerpendocs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uantwerpendocs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These class files implement the house style of the University of
Antwerp. This package originated from the Faculty of Applied
Engineering. Using these class files will make it easy for you to make
and keep your documents compliant to this version and future versions of
the house style of the University of Antwerp. This includes classes for
course texts, master theses, phd theses, exams, reports and a beamer
theme for slides.

