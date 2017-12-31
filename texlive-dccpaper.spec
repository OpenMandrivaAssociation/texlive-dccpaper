Name:		texlive-dccpaper
Version:	1.6
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
%{_texmfdistdir}/tex/latex/dccpaper
%doc %{_texmfdistdir}/doc/latex/dccpaper
#- source
%doc %{_texmfdistdir}/source/latex/dccpaper

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
