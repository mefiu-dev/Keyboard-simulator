Name:           test
Version:        1.0
Release:        alt1
Summary:        Test projeckt

License:        GPLv3+
Group:          Education
URL:            https://oskometa.ru
BuildArch:      noarch


%if_disabled snapshot
Source:         https://oskometa.ru/releases/%{name}-%{version}.tar.gz
%else
Source:         %{name}-%{version}.tar.gz 
%endif

Requires: /usr/bin/python3, python3(PIL) < 0, python3(random) < 0, python3(threading) < 0, python3(tkinter) < 0, python3(tkinter.ttk) < 0, python3(webbrowser) < 0

%description
The long-tail description for our Example projeckt

%prep
%setup -q
 
%install
install -Dm0755 test.py %buildroot%_bindir/test.py
install -Dm0644 logo.png %buildroot%_pixmapsdir/logo.png
install -Dm0644 menu.png %buildroot%_pixmapsdir/menu.png
install -Dm0644 circleb30px.png %buildroot%_pixmapsdir/circleb30px.png
install -Dm0644 circle30px.png %buildroot%_pixmapsdir/circle30px.png
install -Dm0644 Test.desktop %buildroot%_desktopdir/Test.desktop

%files
%_bindir/test.py
%_pixmapsdir/logo.png
%_pixmapsdir/menu.png
%_pixmapsdir/circleb30px.png
%_pixmapsdir/circle30px.png
%_desktopdir/Test.desktop

%changelog
* Tue Jan 13 2020 User Name <mgroshkov@mail.ru> - 1.0-1
- First example package
