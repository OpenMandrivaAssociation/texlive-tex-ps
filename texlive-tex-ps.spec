%global tl_name tex-ps
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX to PostScript generic macros and add-ons
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/TeX-PS
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX to PostScript generic macros and add-ons: transformations of EPS
files, prepress preparation, color separation, mirror, etc.

