Summary:	OpenPTC for X11
Summary(pl.UTF-8):	OpenPTC dla X11
Name:		OpenPTC-x11
Version:	1.0.0
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://www.gaffer.org/ptc/download/distributions/Unix/%{name}-%{version}.tar.gz
# Source0-md5:	7fb728f05ea8bea6b797fd6109f933d4
# from dead http://www.cs.ucl.ac.uk/students/c.nentwich/ptc/%{name}-1.0.0-1.0.0-2.patch
Patch0:		%{name}-1.0.0-1.0.0-2.patch
URL:		http://www.gaffer.org/ptc/ptc.html
Requires:	Hermes >= 1.2.4
BuildRequires:	Hermes-devel >= 1.2.4
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Prometheus Truecolour (OpenPTC) is a third-generation standard for
cross platform low-level graphics access. A lot of design experience
has gone into it to provide one of the cleanest APIs available for
this kind of purpose.

OpenPTC will provide you with a frame-buffer to draw into. You can
choose that buffer to use a pixel format convenient for you, OpenPTC
will convert it to the video modes on the target platform, using
highly optimised x86 and MMX routines where available. This is
achieved using the HERMES ((c)1998/99 Christian Nentwich et al) pixel
conversion library.

OpenPTC 1.0 is available for X11, GGI (Linux), Win32, DOS and JAVA.
Work for other platforms is in progress. All implementations of PTC
come with full source code and may be used free of charge even in
commercial projects.

%description -l pl.UTF-8
Prometheus Truecolour (OpenPTC) jest trzecią generacją standardu dla
wieloplatformowej niskopoziomowej grafiki. Umożliwia operacje na
frame-bufferze oraz konwersją (przy pomocy biblioteki Hermes) na różne
tryby graficzne.

OpenPTC jest dostępne dla X11, GGI, Win32, DOS i JAVA.

%package devel
Summary:	OpenPTC development package
Summary(pl.UTF-8):	Pakiet programistyczny dla OpenPTC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
OpenPTC development package.

%description devel -l pl.UTF-8
Pakiet programistyczny dla OpenPTC.

%package static
Summary:	OpenPTC static libraries
Summary(pl.UTF-8):	Biblioteki statyczne dla OpenPTC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
OpenPTC static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dla OpenPTC.

%prep
%setup -q

%build
# Hack to avoid question in configure
LDFLAGS="%{rpmldflags}" \
echo y | \
./configure %{_target_platform} \
	--prefix=%{_prefix}

%{__make} ptclib \
	CC="c++ %{rpmcflags} -fno-rtti -fno-implicit-templates"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README BUGS CHANGES TODO docs demos examples
%attr(755,root,root) %{_bindir}/ptc-config
%{_libdir}/lib*.so
%{_includedir}/ptc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
