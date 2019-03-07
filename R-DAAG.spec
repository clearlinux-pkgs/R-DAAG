#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DAAG
Version  : 1.22.1
Release  : 13
URL      : https://cran.r-project.org/src/contrib/DAAG_1.22.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DAAG_1.22.1.tar.gz
Summary  : Data Analysis and Graphics Data and Functions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-latticeExtra
BuildRequires : R-latticeExtra
BuildRequires : buildreq-R

%description
book Maindonald, J.H. and Braun, W.J. (2003, 2007, 2010) "Data
        Analysis and Graphics Using R".

%prep
%setup -q -c -n DAAG

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551584046

%install
export SOURCE_DATE_EPOCH=1551584046
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DAAG
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DAAG
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DAAG
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library DAAG|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DAAG/DESCRIPTION
/usr/lib64/R/library/DAAG/INDEX
/usr/lib64/R/library/DAAG/Meta/Rd.rds
/usr/lib64/R/library/DAAG/Meta/data.rds
/usr/lib64/R/library/DAAG/Meta/features.rds
/usr/lib64/R/library/DAAG/Meta/hsearch.rds
/usr/lib64/R/library/DAAG/Meta/links.rds
/usr/lib64/R/library/DAAG/Meta/nsInfo.rds
/usr/lib64/R/library/DAAG/Meta/package.rds
/usr/lib64/R/library/DAAG/Meta/vignette.rds
/usr/lib64/R/library/DAAG/NAMESPACE
/usr/lib64/R/library/DAAG/NEWS
/usr/lib64/R/library/DAAG/R/DAAG
/usr/lib64/R/library/DAAG/R/DAAG.rdb
/usr/lib64/R/library/DAAG/R/DAAG.rdx
/usr/lib64/R/library/DAAG/data/Rdata.rdb
/usr/lib64/R/library/DAAG/data/Rdata.rds
/usr/lib64/R/library/DAAG/data/Rdata.rdx
/usr/lib64/R/library/DAAG/data/datalist
/usr/lib64/R/library/DAAG/doc/index.html
/usr/lib64/R/library/DAAG/doc/motifs.txt
/usr/lib64/R/library/DAAG/doc/rockArt.pdf
/usr/lib64/R/library/DAAG/doc/simulate-regdiags.R
/usr/lib64/R/library/DAAG/doc/simulate-regdiags.Rnw
/usr/lib64/R/library/DAAG/doc/simulate-regdiags.pdf
/usr/lib64/R/library/DAAG/doc/simulate-varselect.R
/usr/lib64/R/library/DAAG/doc/simulate-varselect.Rnw
/usr/lib64/R/library/DAAG/doc/simulate-varselect.pdf
/usr/lib64/R/library/DAAG/help/AnIndex
/usr/lib64/R/library/DAAG/help/DAAG.rdb
/usr/lib64/R/library/DAAG/help/DAAG.rdx
/usr/lib64/R/library/DAAG/help/aliases.rds
/usr/lib64/R/library/DAAG/help/paths.rds
/usr/lib64/R/library/DAAG/html/00Index.html
/usr/lib64/R/library/DAAG/html/R.css
/usr/lib64/R/library/DAAG/misc/seedrates.txt
/usr/lib64/R/library/DAAG/misc/viewtemps.RData
/usr/lib64/R/library/DAAG/seedrates.txt
