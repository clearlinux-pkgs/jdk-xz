Name     : jdk-xz
Version  : 1.5
Release  : 1
URL      : http://tukaani.org/xz/xz-java-1.5.zip
Source0  : http://tukaani.org/xz/xz-java-1.5.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
BuildRequires : apache-ant
BuildRequires : openjdk-dev
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : lxml
BuildRequires : javapackages-tools

%description
No detailed description available

%prep
%setup -q -c xz-java-1.5

# Dummy package-list to avoid ths file download. 
mkdir -p extdoc
touch extdoc/package-list

%build
ant maven

%install

mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

cp build/maven/xz-1.5.pom %{buildroot}/usr/share/maven-poms/xz-java.pom
cp build/jar/xz.jar %{buildroot}/usr/share/java/xz-java.jar
ln -sf xz-java.jar %{buildroot}/usr/share/java/xz.jar

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/xz-java.xml \
%{buildroot}/usr/share/maven-poms/xz-java.pom \
%{buildroot}/usr/share/java/xz-java.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/xz-java.jar
/usr/share/java/xz.jar
/usr/share/maven-metadata/xz-java.xml
/usr/share/maven-poms/xz-java.pom
