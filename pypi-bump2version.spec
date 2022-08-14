#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-bump2version
Version  : 1.0.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/29/2a/688aca6eeebfe8941235be53f4da780c6edee05dbbea5d7abaa3aab6fad2/bump2version-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/29/2a/688aca6eeebfe8941235be53f4da780c6edee05dbbea5d7abaa3aab6fad2/bump2version-1.0.1.tar.gz
Summary  : Version-bump your software with a single command!
Group    : Development/Tools
License  : MIT
Requires: pypi-bump2version-bin = %{version}-%{release}
Requires: pypi-bump2version-license = %{version}-%{release}
Requires: pypi-bump2version-python = %{version}-%{release}
Requires: pypi-bump2version-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# bump2version

%package bin
Summary: bin components for the pypi-bump2version package.
Group: Binaries
Requires: pypi-bump2version-license = %{version}-%{release}

%description bin
bin components for the pypi-bump2version package.


%package license
Summary: license components for the pypi-bump2version package.
Group: Default

%description license
license components for the pypi-bump2version package.


%package python
Summary: python components for the pypi-bump2version package.
Group: Default
Requires: pypi-bump2version-python3 = %{version}-%{release}

%description python
python components for the pypi-bump2version package.


%package python3
Summary: python3 components for the pypi-bump2version package.
Group: Default
Requires: python3-core
Provides: pypi(bump2version)

%description python3
python3 components for the pypi-bump2version package.


%prep
%setup -q -n bump2version-1.0.1
cd %{_builddir}/bump2version-1.0.1
pushd ..
cp -a bump2version-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362822
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bump2version
cp %{_builddir}/bump2version-1.0.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-bump2version/e12aef25fc32114a2b056953d9d0cba9a306369c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bump2version
/usr/bin/bumpversion

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bump2version/e12aef25fc32114a2b056953d9d0cba9a306369c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
