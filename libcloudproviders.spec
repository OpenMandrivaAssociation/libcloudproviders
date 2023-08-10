%define major 0
%define api 0.3
%define libname   %mklibname cloudproviders %{major}
%define girname   %mklibname cloudproviders-gir %{version}
%define develname %mklibname cloudproviders -d

Name:           libcloudproviders
Version:        0.3.2
Release:        1
Summary:        Library for integration of cloud storage providers
Group:          System/Libraries
License:        LGPLv3+
URL:            https://gitlab.gnome.org/World/libcloudproviders
Source0:        https://gitlab.gnome.org/World/libcloudproviders/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  vala-tools
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Cross desktop library for desktop integration of cloud storage providers and sync tools.

%package -n %{libname}
Summary:    Library for integration of cloud storage providers
Group:      System/Libraries

%description -n %{libname}
This package contains the library files required for running services built
using %{name}.

%package -n %{girname}
Summary:    GObject Introspection interface description for CloudProviders
Group:      System/Libraries
Requires:   %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for CloudProviders.

%package -n %{develname}
Summary:    Development files for %{name}
Group:      Development/C
Requires:   %{libname} = %{version}-%{release}
Requires:   %{girname} = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for developing applications
that use %{name}.

%prep
%autosetup -p1

%build
%meson -Denable-gtk-doc=true
%meson_build

%install
%meson_install

%files -n %{libname}
%doc LICENSE
%doc CHANGELOG README.md
%{_libdir}/libcloudproviders.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/CloudProviders-%{api}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/libcloudproviders/
%{_includedir}/cloudproviders/
%{_libdir}/pkgconfig/cloudproviders.pc
%{_libdir}/libcloudproviders.so
%{_datadir}/gir-1.0/CloudProviders-%{api}.gir
%{_datadir}/vala/vapi/cloudproviders.deps
%{_datadir}/vala/vapi/cloudproviders.vapi
