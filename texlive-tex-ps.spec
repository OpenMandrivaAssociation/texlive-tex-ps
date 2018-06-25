Name:		texlive-tex-ps
Version:	20180303
Release:	1
Summary:	TeX to PostScript generic macros and add-ons
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/TeX-PS
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeX to PostScript generic macros and add-ons: transformations
of EPS files, prepress preparation, color separation, mirror,
etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/tex-ps
%{_texmfdistdir}/tex/generic/tex-ps
%doc %{_texmfdistdir}/doc/generic/tex-ps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
