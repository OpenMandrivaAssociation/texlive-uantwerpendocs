Name:		texlive-uantwerpendocs
Version:	72118
Release:	1
Summary:	Course texts, master theses, and exams in University of Antwerp style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uantwerpendocs
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uantwerpendocs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uantwerpendocs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uantwerpendocs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These class files implement the house style of the University
of Antwerp. This package originated from the Faculty of Applied
Engineering. Using these class files will make it easy for you
to make and keep your documents compliant to this version and
future versions of the house style of the University of
Antwerp.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uantwerpendocs
%{_texmfdistdir}/tex/latex/uantwerpendocs
%doc %{_texmfdistdir}/doc/latex/uantwerpendocs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
