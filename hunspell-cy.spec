Name: hunspell-cy
Summary: Welsh hunspell dictionaries
%define upstreamid 20040425
Version: 0.%{upstreamid}
Release: 5.1%{?dist}
Source: http://www.e-gymraeg.co.uk/myspell/myspell.zip
Group: Applications/Text
URL: http://www.e-gymraeg.co.uk/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Welsh hunspell dictionaries.

%prep
%setup -q -c -n hunspell-cy

%build
unzip PackWelsh.zip
unzip cy_GB.zip
chmod -x *
for i in README_cy_GB.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_cy_GB.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20040425-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040425-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20040425-4
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040425-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 20 2007 Caolan McNamara <caolanm@redhat.com> - 0.20040425-2
- clarify license version
- track down canonical upstream source

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040425-1
- initial version
