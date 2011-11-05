# revision 15878
# category Package
# catalog-ctan /macros/generic/TeX-PS
# catalog-date 2009-10-10 00:51:28 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-tex-ps
Version:	20091010
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeX to PostScript generic macros and add-ons: transformations
of EPS files, prepress preparation, color separation, mirror,
etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/tex-ps/crops.pro
%{_texmfdistdir}/dvips/tex-ps/mirr.hd
%{_texmfdistdir}/dvips/tex-ps/separate.pro
%{_texmfdistdir}/tex/generic/tex-ps/cmyk-hax.tex
%{_texmfdistdir}/tex/generic/tex-ps/epsfx.tex
%{_texmfdistdir}/tex/generic/tex-ps/poligraf.sty
%{_texmfdistdir}/tex/generic/tex-ps/trans.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/README
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/cmyk-doc.pdf
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/fountain.eps
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/gdansk.eps
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/rules.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/sam1-sep.bat
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/sample1.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/sample2.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/sample3.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/sample4.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/cmyk-hax/screen.eps
%doc %{_texmfdistdir}/doc/generic/tex-ps/poligraf/README
%doc %{_texmfdistdir}/doc/generic/tex-ps/poligraf/kol-cmyk.eps
%doc %{_texmfdistdir}/doc/generic/tex-ps/poligraf/sample.tex
%doc %{_texmfdistdir}/doc/generic/tex-ps/poligraf/samplelx.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
