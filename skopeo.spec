%global with_devel 0
%global with_bundled 1
%global with_unit_test 0
%global with_check 0

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo skopeo
# https://github.com/containers/skopeo
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
%global git0 https://%{import_path}

%global build_version v1.5.2

%define epoch 1

ExcludeArch: ppc64

Name: %{repo}
Epoch: 1
Version: 1.5.2
Release: 1
Summary: Work with remote images registries - retrieving information, images, signing content
License: ASL 2.0
URL: %{git0}
Source0: %{git0}/archive/%{build_version}.tar.gz
Source1: https://github.com/cpuguy83/go-md2man/archive/v1.0.10.tar.gz

BuildRequires: go-srpm-macros git-core pkgconfig(devmapper) make
BuildRequires: golang >= 1.16.6
BuildRequires: gpgme-devel libassuan-devel btrfs-progs-devel ostree-devel glib2-devel
Requires: containers-common

Provides: bundled(golang(github.com/beorn7/perks)) = 4c0e84591b9aa9e6dcfdf3e020114cd81f89d5f9
Provides: bundled(golang(github.com/BurntSushi/toml)) = master
Provides: bundled(golang(github.com/containerd/continuity)) = d8fb8589b0e8e85b8c8bbaa8840226d0dfeb7371
Provides: bundled(golang(github.com/containers/image)) = master
Provides: bundled(golang(github.com/containers/storage)) = master
Provides: bundled(golang(github.com/davecgh/go-spew)) = master
Provides: bundled(golang(github.com/docker/distribution)) = master
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = d68f9aeca33f5fd3f08eeae5e9d175edf4e731d1
Provides: bundled(golang(github.com/docker/docker)) = da99009bbb1165d1ac5688b5c81d2f589d418341
Provides: bundled(golang(github.com/docker/go-connections)) = 7beb39f0b969b075d1325fecb092faf27fd357b6
Provides: bundled(golang(github.com/docker/go-metrics)) = 399ea8c73916000c64c2c76e8da00ca82f8387ab
Provides: bundled(golang(github.com/docker/go-units)) = 8a7beacffa3009a9ac66bad506b18ffdd110cf97
Provides: bundled(golang(github.com/docker/libtrust)) = master
Provides: bundled(golang(github.com/ghodss/yaml)) = 73d445a93680fa1a78ae23a5839bad48f32ba1ee
Provides: bundled(golang(github.com/go-check/check)) = v1
Provides: bundled(golang(github.com/gogo/protobuf)) = fcdc5011193ff531a548e9b0301828d5a5b97fd8
Provides: bundled(golang(github.com/golang/glog)) = 44145f04b68cf362d9c4df2182967c2275eaefed
Provides: bundled(golang(github.com/golang/protobuf)) = 8d92cf5fc15a4382f8964b08e1f42a75c0591aa3
Provides: bundled(golang(github.com/gorilla/context)) = 14f550f51a
Provides: bundled(golang(github.com/gorilla/mux)) = e444e69cbd
Provides: bundled(golang(github.com/imdario/mergo)) = 6633656539c1639d9d78127b7d47c622b5d7b6dc
Provides: bundled(golang(github.com/kr/pretty)) = v0.1.0
Provides: bundled(golang(github.com/kr/text)) = v0.1.0
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = c12348ce28de40eed0136aa2b644d0ee0650e56c
Provides: bundled(golang(github.com/mistifyio/go-zfs)) = 22c9b32c84eb0d0c6f4043b6e90fc94073de92fa
Provides: bundled(golang(github.com/mtrmac/gpgme)) = master
Provides: bundled(golang(github.com/opencontainers/go-digest)) = master
Provides: bundled(golang(github.com/opencontainers/image-spec)) = 149252121d044fddff670adcdc67f33148e16226
Provides: bundled(golang(github.com/opencontainers/image-tools)) = 6d941547fa1df31900990b3fb47ec2468c9c6469
Provides: bundled(golang(github.com/opencontainers/runc)) = master
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/selinux)) = master
Provides: bundled(golang(github.com/ostreedev/ostree-go)) = aeb02c6b6aa2889db3ef62f7855650755befd460
Provides: bundled(golang(github.com/pborman/uuid)) = v1.0
Provides: bundled(golang(github.com/pkg/errors)) = master
Provides: bundled(golang(github.com/pmezard/go-difflib)) = master
Provides: bundled(golang(github.com/pquerna/ffjson)) = d49c2bc1aa135aad0c6f4fc2056623ec78f5d5ac
Provides: bundled(golang(github.com/prometheus/client_golang)) = c332b6f63c0658a65eca15c0e5247ded801cf564
Provides: bundled(golang(github.com/prometheus/client_model)) = 99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c
Provides: bundled(golang(github.com/prometheus/common)) = 89604d197083d4781071d3c65855d24ecfb0a563
Provides: bundled(golang(github.com/prometheus/procfs)) = cb4147076ac75738c9a7d279075a253c0cc5acbd
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.0.0
Provides: bundled(golang(github.com/stretchr/testify)) = v1.1.3
Provides: bundled(golang(github.com/syndtr/gocapability)) = master
Provides: bundled(golang(github.com/tchap/go-patricia)) = v2.2.6
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.4
Provides: bundled(golang(github.com/urfave/cli)) = v1.17.0
Provides: bundled(golang(github.com/vbatts/tar-split)) = v0.10.2
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = master
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = master
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = master
Provides: bundled(golang(go4.org)) = master
Provides: bundled(golang(golang.org/x/crypto)) = master
Provides: bundled(golang(golang.org/x/net)) = master
Provides: bundled(golang(golang.org/x/sys)) = master
Provides: bundled(golang(golang.org/x/text)) = master
Provides: bundled(golang(gopkg.in/cheggaaa/pb.v1)) = ad4efe000aa550bb54918c06ebbadc0ff17687b9
Provides: bundled(golang(gopkg.in/yaml.v2)) = d466437aa4adc35830964cffc5b5f262c63ddcb4
Provides: bundled(golang(k8s.io/client-go)) = master

%description
A command line utility that performs various operations on container images and image repositories

%if 0%{?with_devel}
%package devel
Summary: %{summary}
BuildArch: noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/Azure/go-ansiterm/winterm)
BuildRequires: golang(github.com/Sirupsen/logrus)
BuildRequires: golang(github.com/docker/distribution)
BuildRequires: golang(github.com/docker/distribution/context)
BuildRequires: golang(github.com/docker/distribution/digest)
BuildRequires: golang(github.com/docker/distribution/manifest)
BuildRequires: golang(github.com/docker/distribution/manifest/manifestlist)
BuildRequires: golang(github.com/docker/distribution/manifest/schema1)
BuildRequires: golang(github.com/docker/distribution/manifest/schema2)
BuildRequires: golang(github.com/docker/distribution/reference)
BuildRequires: golang(github.com/docker/distribution/registry/api/errcode)
BuildRequires: golang(github.com/docker/distribution/registry/api/v2)
BuildRequires: golang(github.com/docker/distribution/registry/client)
BuildRequires: golang(github.com/docker/distribution/registry/client/auth)
BuildRequires: golang(github.com/docker/distribution/registry/client/transport)
BuildRequires: golang(github.com/docker/distribution/registry/storage/cache)
BuildRequires: golang(github.com/docker/distribution/registry/storage/cache/memory)
BuildRequires: golang(github.com/docker/distribution/uuid)
BuildRequires: golang(github.com/docker/docker/api)
BuildRequires: golang(github.com/docker/docker/daemon/graphdriver)
BuildRequires: golang(github.com/docker/docker/distribution/metadata)
BuildRequires: golang(github.com/docker/docker/distribution/xfer)
BuildRequires: golang(github.com/docker/docker/dockerversion)
BuildRequires: golang(github.com/docker/docker/image)
BuildRequires: golang(github.com/docker/docker/image/v1)
BuildRequires: golang(github.com/docker/docker/layer)
BuildRequires: golang(github.com/docker/docker/opts)
BuildRequires: golang(github.com/docker/docker/pkg/archive)
BuildRequires: golang(github.com/docker/docker/pkg/chrootarchive)
BuildRequires: golang(github.com/docker/docker/pkg/fileutils)
BuildRequires: golang(github.com/docker/docker/pkg/homedir)
BuildRequires: golang(github.com/docker/docker/pkg/httputils)
BuildRequires: golang(github.com/docker/docker/pkg/idtools)
BuildRequires: golang(github.com/docker/docker/pkg/ioutils)
BuildRequires: golang(github.com/docker/docker/pkg/jsonlog)
BuildRequires: golang(github.com/docker/docker/pkg/jsonmessage)
BuildRequires: golang(github.com/docker/docker/pkg/longpath)
BuildRequires: golang(github.com/docker/docker/pkg/mflag)
BuildRequires: golang(github.com/docker/docker/pkg/parsers/kernel)
BuildRequires: golang(github.com/docker/docker/pkg/plugins)
BuildRequires: golang(github.com/docker/docker/pkg/pools)
BuildRequires: golang(github.com/docker/docker/pkg/progress)
BuildRequires: golang(github.com/docker/docker/pkg/promise)
BuildRequires: golang(github.com/docker/docker/pkg/random)
BuildRequires: golang(github.com/docker/docker/pkg/reexec)
BuildRequires: golang(github.com/docker/docker/pkg/stringid)
BuildRequires: golang(github.com/docker/docker/pkg/system)
BuildRequires: golang(github.com/docker/docker/pkg/tarsum)
BuildRequires: golang(github.com/docker/docker/pkg/term)
BuildRequires: golang(github.com/docker/docker/pkg/term/windows)
BuildRequires: golang(github.com/docker/docker/pkg/useragent)
BuildRequires: golang(github.com/docker/docker/pkg/version)
BuildRequires: golang(github.com/docker/docker/reference)
BuildRequires: golang(github.com/docker/docker/registry)
BuildRequires: golang(github.com/docker/engine-api/types)
BuildRequires: golang(github.com/docker/engine-api/types/blkiodev)
BuildRequires: golang(github.com/docker/engine-api/types/container)
BuildRequires: golang(github.com/docker/engine-api/types/filters)
BuildRequires: golang(github.com/docker/engine-api/types/image)
BuildRequires: golang(github.com/docker/engine-api/types/network)
BuildRequires: golang(github.com/docker/engine-api/types/registry)
BuildRequires: golang(github.com/docker/engine-api/types/strslice)
BuildRequires: golang(github.com/docker/go-connections/nat)
BuildRequires: golang(github.com/docker/go-connections/tlsconfig)
BuildRequires: golang(github.com/docker/go-units)
BuildRequires: golang(github.com/docker/libtrust)
BuildRequires: golang(github.com/gorilla/context)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires: golang(github.com/vbatts/tar-split/archive/tar)
BuildRequires: golang(github.com/vbatts/tar-split/tar/asm)
BuildRequires: golang(github.com/vbatts/tar-split/tar/storage)
BuildRequires: golang(golang.org/x/net/context)
%endif

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary: Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires: %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%autosetup -Sgit -n %{name}-%{version}
tar -xf %SOURCE1

%build
pushd go-md2man-*
go build -mod=vendor -o go-md2man .
export GOMD2MAN=$(realpath go-md2man)
popd
mkdir -p src/github.com/containers
ln -s ../../../ src/%{import_path}

mkdir -p vendor/src
for v in vendor/*; do
    if test ${v} = vendor/src; then continue; fi
    if test -d ${v}; then
        mv ${v} vendor/src/
    fi
done

%if ! 0%{?with_bundled}
rm -rf vendor/
export GOPATH=$(pwd)
%else
export GOPATH=$(pwd):$(pwd)/vendor
%endif

mkdir -p bin
export GO111MODULE=off

go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d '  \n') -extldflags '-Wl,-z,relro -Wl,-z,now '" -a -v -x -o bin/%{name} ./cmd/%{name}
%{__make} docs
 
%install
make \
    PREFIX=%{buildroot}%{_prefix} \
    install-docs install-completions

install -m0755 -d -p %{buildroot}%{_bindir}
install -m0755 bin/skopeo %{buildroot}%{_bindir}/%{name}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go" | grep -v "./vendor") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go" | grep -v "./vendor"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%gotest %{import_path}/integration
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_prefix}/share/man/man1/%{name}*
%dir %{_prefix}/share/bash-completion
%dir %{_prefix}/share/bash-completion/completions
%{_prefix}/share/bash-completion/completions/%{name}

%changelog
* Thu Mar 24 2022 fushanqing <fushanqing@kylinos.cn> - 1:1.5.2-1
- update to 1.5.2 and remove subpackage containers-common

* Fri Dec 10 2021 wangqing <wangqing@uniontech.com> - 1.1.0-8.dev.git63085f5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:install seccomp.json for skopeo

* Thu Nov 25 2021 haozi007<liuhao27@huawei.com> - 1.1.0-7.dev.git63085f5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:install registries.conf for skopeo

* Thu Mar  18 2021 haozi007 <liuhao27@huawei.com> - 1.1.0-6.dev.git63085f5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:enable debug rpm

* Fri Feb  19 2021 haozi007 <liuhao27@huawei.com> - 1.1.0-5.dev.git63085f5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Change BuildRequires to source go-md2man

* Mon Feb  8 2021 haozi007 <liuhao27@huawei.com> - 1.1.0-4.dev.git63085f5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Change BuildRequires to golang
