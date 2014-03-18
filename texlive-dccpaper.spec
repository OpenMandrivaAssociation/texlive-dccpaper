# revision 33142
# category Package
# catalog-ctan /macros/latex/contrib/dccpaper
# catalog-date 2014-03-09 14:23:10 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-dccpaper
Version:	1.1
Release:	1
Summary:	Typeset papers for the International Journal of Digital Curation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dccpaper
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dccpaper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dccpaper.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dccpaper.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX class ijdc-v9 produces camera-ready papers and
articles suitable for inclusion in the International Journal of
Digital Curation, with applicability from volume 9 onwards. The
similar idcc class can be used for submissions to the
International Digital Curation Conference, beginning with the
2015 conference.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dccpaper/dccpaper-base.tex
%{_texmfdistdir}/tex/latex/dccpaper/dccpaper-by.eps
%{_texmfdistdir}/tex/latex/dccpaper/dccpaper-by.pdf
%{_texmfdistdir}/tex/latex/dccpaper/idcc.cls
%{_texmfdistdir}/tex/latex/dccpaper/ijdc-v9.cls
%doc %{_texmfdistdir}/doc/latex/dccpaper/README
%doc %{_texmfdistdir}/doc/latex/dccpaper/README.txt
%doc %{_texmfdistdir}/doc/latex/dccpaper/dccpaper-apacite.bib
%doc %{_texmfdistdir}/doc/latex/dccpaper/dccpaper-biblatex.bib
%doc %{_texmfdistdir}/doc/latex/dccpaper/dccpaper.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dccpaper/Makefile
%doc %{_texmfdistdir}/source/latex/dccpaper/dccpaper.dtx
%doc %{_texmfdistdir}/source/latex/dccpaper/dccpaper.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
