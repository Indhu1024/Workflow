import json

# JSON data (replace this with your data)
json_data = '''
{
	"results": [
		{
			"id": "sha256:bd08b0c17e93272cda54d566f0597f5d4196c52f95ad5e3b49d2be31c7d11dd2",
			"name": "gws-oci-dev.artifactory.gws.genesys.com/gws-api-v2:8.6.000.00-0007",
			"distro": "Red Hat Enterprise Linux release 8.8 (Ootpa)",
			"distroRelease": "RHEL8",
			"digest": "sha256:35a9110d259c99a16430aa28f86f5435a5e01fa0db44a401434a17e038b2fc7f",
			"collections": [
				"All"
			],
			"packages": [
				{
					"type": "os",
					"name": "langpacks-ja",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "tzdata",
					"version": "2023c-1.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "nss-tools",
					"version": "3.79.0-11.el8_7",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "python3-pip-wheel",
					"version": "9.0.3-22.el8",
					"licenses": [
						"MIT and Python and ASL 2.0 and BSD and ISC and LGPLv2 and MPLv2.0 and (ASL 2.0 or BSD)"
					]
				},
				{
					"type": "os",
					"name": "make",
					"version": "4.2.1-11.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "redhat-release",
					"version": "8.8-0.8.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "alsa-lib",
					"version": "1.2.8-2.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "filesystem",
					"version": "3.8-6.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "lua",
					"version": "5.3.4-12.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "publicsuffix-list-dafsa",
					"version": "20180723-1.el8",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "libfontenc",
					"version": "1.1.3-8.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "pcre2",
					"version": "10.32-3.el8_6",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "xorg-x11-fonts-Type1",
					"version": "7.5-19.el8",
					"licenses": [
						"MIT and Lucida and Public Domain"
					]
				},
				{
					"type": "os",
					"name": "ncurses-libs",
					"version": "6.1-9.20180224.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libxcb",
					"version": "1.13.1-1.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "glibc-common",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "libX11",
					"version": "1.6.8-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "bash",
					"version": "4.4.20-4.el8_6",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libXi",
					"version": "1.7.10-1.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "zlib",
					"version": "1.2.11-21.el8_7",
					"licenses": [
						"zlib and Boost"
					]
				},
				{
					"type": "os",
					"name": "libXcomposite",
					"version": "0.4.4-14.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "bzip2-libs",
					"version": "1.0.6-26.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "javapackages-filesystem",
					"version": "5.3.0-1.module+el8+2447+6f56d9a6",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "sqlite-libs",
					"version": "3.26.0-18.el8_8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "avahi-libs",
					"version": "0.7-20.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "info",
					"version": "6.5-7.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "java-17-openjdk-headless",
					"version": "17.0.8.0.7-2.el8",
					"licenses": [
						"ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib and ISC and FTL and RSA"
					]
				},
				{
					"type": "os",
					"name": "libxcrypt",
					"version": "4.1.1-6.el8",
					"licenses": [
						"LGPLv2+ and BSD and Public Domain"
					]
				},
				{
					"type": "os",
					"name": "java-17-openjdk-devel",
					"version": "17.0.8.0.7-2.el8",
					"licenses": [
						"ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib and ISC and FTL and RSA"
					]
				},
				{
					"type": "os",
					"name": "popt",
					"version": "1.18-1.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "expat",
					"version": "2.2.5-11.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libcom_err",
					"version": "1.45.6-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libuuid",
					"version": "2.32.1-42.el8_8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "gmp",
					"version": "6.1.2-10.el8",
					"licenses": [
						"LGPLv3+ or GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libacl",
					"version": "2.2.53-1.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libblkid",
					"version": "2.32.1-42.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "sed",
					"version": "4.5-5.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libstdc++",
					"version": "8.5.0-18.el8",
					"licenses": [
						"GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD"
					]
				},
				{
					"type": "os",
					"name": "p11-kit",
					"version": "0.23.22-1.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "libunistring",
					"version": "0.9.9-3.el8",
					"licenses": [
						"GPLv2+ or LGPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libgcrypt",
					"version": "1.8.5-7.el8_6",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libcap-ng",
					"version": "0.7.11-1.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "lz4-libs",
					"version": "1.8.3-3.el8_4",
					"licenses": [
						"GPLv2+ and BSD"
					]
				},
				{
					"type": "os",
					"name": "gdbm-libs",
					"version": "1.18-2.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libtasn1",
					"version": "4.13-4.el8_7",
					"licenses": [
						"GPLv3+ and LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "pcre",
					"version": "8.42-6.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "systemd-libs",
					"version": "239-74.el8_8.3",
					"licenses": [
						"LGPLv2+ and MIT"
					]
				},
				{
					"type": "os",
					"name": "ca-certificates",
					"version": "2022.2.54-80.2.el8_6",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "libusbx",
					"version": "1.0.23-4.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libutempter",
					"version": "1.1.6-14.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libfdisk",
					"version": "2.32.1-42.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "cracklib",
					"version": "2.9.6-15.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "which",
					"version": "2.21-18.el8",
					"licenses": [
						"GPLv3"
					]
				},
				{
					"type": "os",
					"name": "mpfr",
					"version": "3.1.6-1.el8",
					"licenses": [
						"LGPLv3+ and GPLv3+ and GFDL"
					]
				},
				{
					"type": "os",
					"name": "libcomps",
					"version": "0.1.18-1.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "brotli",
					"version": "1.0.6-3.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libnghttp2",
					"version": "1.33.0-3.el8_2.1",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libseccomp",
					"version": "2.5.2-1.el8",
					"licenses": [
						"LGPLv2"
					]
				},
				{
					"type": "os",
					"name": "gawk",
					"version": "4.2.1-4.el8",
					"licenses": [
						"GPLv3+ and GPLv2+ and LGPLv2+ and BSD"
					]
				},
				{
					"type": "os",
					"name": "libnsl2",
					"version": "1.2.0-2.20180605git4a062cf.el8",
					"licenses": [
						"BSD and LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "krb5-libs",
					"version": "1.18.2-25.el8_8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "crypto-policies",
					"version": "20221215-1.gitece0092.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "platform-python-setuptools",
					"version": "39.2.0-7.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-libs",
					"version": "3.6.8-51.el8_8.1",
					"licenses": [
						"Python"
					]
				},
				{
					"type": "os",
					"name": "libpwquality",
					"version": "1.4.4-6.el8",
					"licenses": [
						"BSD or GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-six",
					"version": "1.11.0-8.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-dateutil",
					"version": "2.6.1-6.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "glib2",
					"version": "2.56.4-161.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "librhsm",
					"version": "0.0.3-5.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "dbus-glib",
					"version": "0.110-2.el8",
					"licenses": [
						"AFL and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "gobject-introspection",
					"version": "1.56.1-1.el8",
					"licenses": [
						"GPLv2+, LGPLv2+, MIT"
					]
				},
				{
					"type": "os",
					"name": "virt-what",
					"version": "1.25-3.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "openldap",
					"version": "2.4.46-18.el8",
					"licenses": [
						"OpenLDAP"
					]
				},
				{
					"type": "os",
					"name": "passwd",
					"version": "0.80-4.el8",
					"licenses": [
						"BSD or GPL+"
					]
				},
				{
					"type": "os",
					"name": "libdb-utils",
					"version": "5.3.28-42.el8_4",
					"licenses": [
						"BSD and LGPLv2 and Sleepycat"
					]
				},
				{
					"type": "os",
					"name": "python3-libcomps",
					"version": "0.1.18-1.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-dmidecode",
					"version": "3.12.3-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "python3-chardet",
					"version": "3.0.4-7.el8",
					"licenses": [
						"LGPLv2"
					]
				},
				{
					"type": "os",
					"name": "python3-idna",
					"version": "2.5-5.el8",
					"licenses": [
						"BSD and Python and Unicode"
					]
				},
				{
					"type": "os",
					"name": "python3-pysocks",
					"version": "1.6.8-3.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "python3-requests",
					"version": "2.20.0-3.el8_8",
					"licenses": [
						"ASL 2.0"
					]
				},
				{
					"type": "os",
					"name": "python3-syspurpose",
					"version": "1.28.36-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "device-mapper",
					"version": "1.02.181-9.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "cryptsetup-libs",
					"version": "2.3.7-5.el8",
					"licenses": [
						"GPLv2+ and LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "elfutils-libs",
					"version": "0.188-3.el8",
					"licenses": [
						"GPLv2+ or LGPLv3+"
					]
				},
				{
					"type": "os",
					"name": "systemd",
					"version": "239-74.el8_8.3",
					"licenses": [
						"LGPLv2+ and MIT and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libarchive",
					"version": "3.3.3-5.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "ima-evm-utils",
					"version": "1.3.2-12.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "npth",
					"version": "1.5-4.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "gpgme",
					"version": "1.13.1-11.el8",
					"licenses": [
						"LGPLv2+ and GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libssh-config",
					"version": "0.9.6-10.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libcurl",
					"version": "7.61.1-30.el8_8.3",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-librepo",
					"version": "1.14.2-4.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "rpm",
					"version": "4.14.3-26.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libmodulemd",
					"version": "2.13.0-1.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libdnf",
					"version": "0.63.0-14.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-hawkey",
					"version": "0.63.0-14.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-rpm",
					"version": "4.14.3-26.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libreport-filesystem",
					"version": "2.9.5-15.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-dnf",
					"version": "4.7.0-16.el8_8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-dnf-plugins-core",
					"version": "4.0.21-19.el8_8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "subscription-manager",
					"version": "1.28.36-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "gdb-gdbserver",
					"version": "8.2-19.el8",
					"licenses": [
						"GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "vim-minimal",
					"version": "8.0.1763-19.el8_6.4",
					"licenses": [
						"Vim and MIT"
					]
				},
				{
					"type": "os",
					"name": "gpg-pubkey",
					"version": "fd431d51-4ae0493b",
					"licenses": [
						"pubkey"
					]
				},
				{
					"type": "os",
					"name": "dbus-libs",
					"version": "1.12.8-24.el8_8.1",
					"licenses": [
						"(GPLv2+ or AFL) and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "dbus-common",
					"version": "1.12.8-24.el8_8.1",
					"licenses": [
						"(GPLv2+ or AFL) and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "dbus",
					"version": "1.12.8-24.el8_8.1",
					"licenses": [
						"(GPLv2+ or AFL) and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libsemanage",
					"version": "2.9-9.el8_6",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-en",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "nss-util",
					"version": "3.79.0-11.el8_7",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "fontpackages-filesystem",
					"version": "1.44-22.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "dejavu-sans-fonts",
					"version": "2.35-7.el8",
					"licenses": [
						"Bitstream Vera and Public Domain"
					]
				},
				{
					"type": "os",
					"name": "nss-softokn",
					"version": "3.79.0-11.el8_7",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "nss",
					"version": "3.79.0-11.el8_7",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "fipscheck",
					"version": "1.5.0-4.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-ja",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-ar",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-tr",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-it",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-ru",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-nl",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-pl",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "openssl",
					"version": "1.1.1k-9.el8_7",
					"licenses": [
						"OpenSSL and ASL 2.0"
					]
				},
				{
					"type": "os",
					"name": "pcre2-utf32",
					"version": "10.32-3.el8_6",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "pkgconf-m4",
					"version": "1.4.2-1.el8",
					"licenses": [
						"GPLv2+ with exceptions"
					]
				},
				{
					"type": "os",
					"name": "pkgconf",
					"version": "1.4.2-1.el8",
					"licenses": [
						"ISC"
					]
				},
				{
					"type": "os",
					"name": "libsepol-devel",
					"version": "2.9-3.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libselinux-devel",
					"version": "2.9-8.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "libcom_err-devel",
					"version": "1.45.6-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "zlib-devel",
					"version": "1.2.11-21.el8_7",
					"licenses": [
						"zlib and Boost"
					]
				},
				{
					"type": "os",
					"name": "freetype",
					"version": "2.9.1-9.el8",
					"licenses": [
						"(FTL or GPLv2+) and BSD and MIT and Public Domain and zlib with acknowledgement"
					]
				},
				{
					"type": "os",
					"name": "openssl-devel",
					"version": "1.1.1k-9.el8_7",
					"licenses": [
						"OpenSSL and ASL 2.0"
					]
				},
				{
					"type": "os",
					"name": "krb5-workstation",
					"version": "1.18.2-25.el8_8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "langpacks-cs",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-fr",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-ko",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-pt_BR",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-zh_CN",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-de",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libgcc",
					"version": "8.5.0-18.el8",
					"licenses": [
						"GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD"
					]
				},
				{
					"type": "os",
					"name": "langpacks-es",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-setuptools-wheel",
					"version": "39.2.0-7.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "glibc-all-langpacks",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "subscription-manager-rhsm-certificates",
					"version": "1.28.36-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "tzdata-java",
					"version": "2023c-1.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "setup",
					"version": "2.12.2-9.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "ttmkfdir",
					"version": "3.0.9-54.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "basesystem",
					"version": "11-5.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "copy-jdk-configs",
					"version": "4.0-2.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "ncurses-base",
					"version": "6.1-9.20180224.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "xorg-x11-font-utils",
					"version": "7.5-41.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libselinux",
					"version": "2.9-8.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "libXau",
					"version": "1.0.9-3.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "glibc-minimal-langpack",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "libX11-common",
					"version": "1.6.8-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "glibc",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "libXext",
					"version": "1.3.4-1.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libsepol",
					"version": "2.9-3.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libXtst",
					"version": "1.2.3-7.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "xz-libs",
					"version": "5.2.4-4.el8_6",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "libXrender",
					"version": "0.9.10-7.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libgpg-error",
					"version": "1.31-1.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "lksctp-tools",
					"version": "1.0.18-3.el8",
					"licenses": [
						"GPLv2 and GPLv2+ and LGPLv2 and MIT"
					]
				},
				{
					"type": "os",
					"name": "libxml2",
					"version": "2.9.7-16.el8_8.1",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "cups-libs",
					"version": "2.2.6-51.el8",
					"licenses": [
						"LGPLv2 and zlib"
					]
				},
				{
					"type": "os",
					"name": "libcap",
					"version": "2.48-5.el8_8",
					"licenses": [
						"BSD or GPLv2"
					]
				},
				{
					"type": "os",
					"name": "java-17-openjdk",
					"version": "17.0.8.0.7-2.el8",
					"licenses": [
						"ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib and ISC and FTL and RSA"
					]
				},
				{
					"type": "os",
					"name": "libzstd",
					"version": "1.4.4-1.el8",
					"licenses": [
						"BSD and GPLv2"
					]
				},
				{
					"type": "os",
					"name": "elfutils-libelf",
					"version": "0.188-3.el8",
					"licenses": [
						"GPLv2+ or LGPLv3+"
					]
				},
				{
					"type": "os",
					"name": "json-c",
					"version": "0.13.1-3.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libffi",
					"version": "3.1-24.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "readline",
					"version": "7.0-10.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libattr",
					"version": "2.4.48-3.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "coreutils-single",
					"version": "8.30-15.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libmount",
					"version": "2.32.1-42.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libsmartcols",
					"version": "2.32.1-42.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "lua-libs",
					"version": "5.3.4-12.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "chkconfig",
					"version": "1.19.1-1.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "libidn2",
					"version": "2.2.0-1.el8",
					"licenses": [
						"(GPLv2+ or LGPLv3+) and GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "file-libs",
					"version": "5.33-24.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "audit-libs",
					"version": "3.0.7-4.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libassuan",
					"version": "2.5.1-3.el8",
					"licenses": [
						"LGPLv2+ and GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "keyutils-libs",
					"version": "1.5.10-9.el8",
					"licenses": [
						"GPLv2+ and LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "p11-kit-trust",
					"version": "0.23.22-1.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "grep",
					"version": "3.1-6.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "gdbm",
					"version": "1.18-2.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "shadow-utils",
					"version": "4.6-17.el8",
					"licenses": [
						"BSD and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libpsl",
					"version": "0.20.2-6.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "gzip",
					"version": "1.9-13.el8_5",
					"licenses": [
						"GPLv3+ and GFDL"
					]
				},
				{
					"type": "os",
					"name": "cracklib-dicts",
					"version": "2.9.6-15.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "acl",
					"version": "2.2.53-1.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "nettle",
					"version": "3.4.1-7.el8",
					"licenses": [
						"LGPLv3+ or GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libksba",
					"version": "1.3.5-9.el8_7",
					"licenses": [
						"(LGPLv3+ or GPLv2+) and GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "dmidecode",
					"version": "3.3-4.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libnl3",
					"version": "3.7.0-1.el8",
					"licenses": [
						"LGPLv2"
					]
				},
				{
					"type": "os",
					"name": "libsigsegv",
					"version": "2.11-5.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libverto",
					"version": "0.3.2-2.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libtirpc",
					"version": "1.1.4-8.el8",
					"licenses": [
						"SISSL and BSD"
					]
				},
				{
					"type": "os",
					"name": "openssl-libs",
					"version": "1.1.1k-9.el8_7",
					"licenses": [
						"OpenSSL and ASL 2.0"
					]
				},
				{
					"type": "os",
					"name": "crypto-policies-scripts",
					"version": "20221215-1.gitece0092.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "platform-python",
					"version": "3.6.8-51.el8_8.1",
					"licenses": [
						"Python"
					]
				},
				{
					"type": "os",
					"name": "libdb",
					"version": "5.3.28-42.el8_4",
					"licenses": [
						"BSD and LGPLv2 and Sleepycat"
					]
				},
				{
					"type": "os",
					"name": "pam",
					"version": "1.3.1-25.el8",
					"licenses": [
						"BSD and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "util-linux",
					"version": "2.32.1-42.el8_8",
					"licenses": [
						"GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain"
					]
				},
				{
					"type": "os",
					"name": "gnutls",
					"version": "3.6.16-6.el8_7",
					"licenses": [
						"GPLv3+ and LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "json-glib",
					"version": "1.4.4-1.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-iniparse",
					"version": "0.4-31.el8",
					"licenses": [
						"MIT and Python"
					]
				},
				{
					"type": "os",
					"name": "python3-dbus",
					"version": "1.2.4-15.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-gobject-base",
					"version": "3.28.3-2.el8",
					"licenses": [
						"LGPLv2+ and MIT"
					]
				},
				{
					"type": "os",
					"name": "cyrus-sasl-lib",
					"version": "2.1.27-6.el8_5",
					"licenses": [
						"BSD with advertising"
					]
				},
				{
					"type": "os",
					"name": "libuser",
					"version": "0.62-25.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "usermode",
					"version": "1.113-2.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-ethtool",
					"version": "0.14-5.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "python3-libxml2",
					"version": "2.9.7-16.el8_8.1",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-systemd",
					"version": "234-8.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "python3-decorator",
					"version": "4.2.1-2.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "python3-inotify",
					"version": "0.9.6-13.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-urllib3",
					"version": "1.24.2-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "python3-cloud-what",
					"version": "1.28.36-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "kmod-libs",
					"version": "25-19.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "device-mapper-libs",
					"version": "1.02.181-9.el8",
					"licenses": [
						"LGPLv2"
					]
				},
				{
					"type": "os",
					"name": "elfutils-default-yama-scope",
					"version": "0.188-3.el8",
					"licenses": [
						"GPLv2+ or LGPLv3+"
					]
				},
				{
					"type": "os",
					"name": "systemd-pam",
					"version": "239-74.el8_8.3",
					"licenses": [
						"LGPLv2+ and MIT and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "tpm2-tss",
					"version": "2.3.2-4.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "libyaml",
					"version": "0.1.7-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "gnupg2",
					"version": "2.2.20-3.el8_6",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "python3-gpg",
					"version": "1.13.1-11.el8",
					"licenses": [
						"LGPLv2+ and GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "libssh",
					"version": "0.9.6-10.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "librepo",
					"version": "1.14.2-4.el8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "curl",
					"version": "7.61.1-30.el8_8.3",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "rpm-libs",
					"version": "4.14.3-26.el8",
					"licenses": [
						"GPLv2+ and LGPLv2+ with exceptions"
					]
				},
				{
					"type": "os",
					"name": "python3-libdnf",
					"version": "0.63.0-14.el8_8",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "rpm-build-libs",
					"version": "4.14.3-26.el8",
					"licenses": [
						"GPLv2+ and LGPLv2+ with exceptions"
					]
				},
				{
					"type": "os",
					"name": "python3-subscription-manager-rhsm",
					"version": "1.28.36-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "dnf-data",
					"version": "4.7.0-16.el8_8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "dnf",
					"version": "4.7.0-16.el8_8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "dnf-plugin-subscription-manager",
					"version": "1.28.36-2.el8",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "os",
					"name": "yum",
					"version": "4.7.0-16.el8_8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "tar",
					"version": "1.30-9.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "findutils",
					"version": "4.6.0-20.el8",
					"licenses": [
						"GPLv3+"
					]
				},
				{
					"type": "os",
					"name": "rootfiles",
					"version": "8.1-22.el8",
					"licenses": [
						"Public Domain"
					]
				},
				{
					"type": "os",
					"name": "gpg-pubkey",
					"version": "d4082792-5b32db75",
					"licenses": [
						"pubkey"
					]
				},
				{
					"type": "os",
					"name": "dbus-tools",
					"version": "1.12.8-24.el8_8.1",
					"licenses": [
						"(GPLv2+ or AFL) and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "dbus-daemon",
					"version": "1.12.8-24.el8_8.1",
					"licenses": [
						"(GPLv2+ or AFL) and GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libsolv",
					"version": "0.7.20-4.el8_7",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-en",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "nspr",
					"version": "4.34.0-3.el8_6",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "libkadm5",
					"version": "1.18.2-25.el8_8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "dejavu-fonts-common",
					"version": "2.35-7.el8",
					"licenses": [
						"Bitstream Vera and Public Domain"
					]
				},
				{
					"type": "os",
					"name": "nss-softokn-freebl",
					"version": "3.79.0-11.el8_7",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "nss-sysinit",
					"version": "3.79.0-11.el8_7",
					"licenses": [
						"MPLv2.0"
					]
				},
				{
					"type": "os",
					"name": "fipscheck-lib",
					"version": "1.5.0-4.el8",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-es",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-de",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-zh",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-pt",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-ko",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-fr",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "glibc-langpack-cs",
					"version": "2.28-225.el8",
					"licenses": [
						"LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL"
					]
				},
				{
					"type": "os",
					"name": "libss",
					"version": "1.45.6-5.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "pcre2-utf16",
					"version": "10.32-3.el8_6",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "keyutils-libs-devel",
					"version": "1.5.10-9.el8",
					"licenses": [
						"GPLv2+ and LGPLv2+"
					]
				},
				{
					"type": "os",
					"name": "libpkgconf",
					"version": "1.4.2-1.el8",
					"licenses": [
						"ISC"
					]
				},
				{
					"type": "os",
					"name": "pkgconf-pkg-config",
					"version": "1.4.2-1.el8",
					"licenses": [
						"ISC"
					]
				},
				{
					"type": "os",
					"name": "pcre2-devel",
					"version": "10.32-3.el8_6",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "os",
					"name": "libverto-devel",
					"version": "0.3.2-2.el8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "krb5-devel",
					"version": "1.18.2-25.el8_8",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "os",
					"name": "libpng",
					"version": "1.6.34-5.el8",
					"licenses": [
						"zlib"
					]
				},
				{
					"type": "os",
					"name": "fontconfig",
					"version": "2.13.1-4.el8",
					"licenses": [
						"MIT and Public Domain and UCD"
					]
				},
				{
					"type": "os",
					"name": "openssl-pkcs11",
					"version": "0.4.10-3.el8",
					"licenses": [
						"LGPLv2+ and BSD"
					]
				},
				{
					"type": "os",
					"name": "langpacks-pl",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-nl",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-ru",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-it",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-tr",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "os",
					"name": "langpacks-ar",
					"version": "1.0-12.el8",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-servlets",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-servlets-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.springframework.data_spring-data-keyvalue",
					"version": "2.7.7",
					"path": "/opt/genesys/application/gws.jar/spring-data-keyvalue-2.7.7.jar"
				},
				{
					"type": "jar",
					"name": "org.yaml_snakeyaml",
					"version": "1.30",
					"path": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"licenses": [
						"Apache License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.cometd.java_cometd-java-websocket-javax-server",
					"version": "3.1.12",
					"path": "/opt/genesys/application/gws.jar/cometd-java-websocket-javax-server-3.1.12.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.httpcomponents_httpclient",
					"version": "4.5.13",
					"path": "/opt/genesys/application/gws.jar/httpclient-4.5.13.jar"
				},
				{
					"type": "jar",
					"name": "commons-lang_commons-lang",
					"version": "2.6",
					"path": "/opt/genesys/application/gws.jar/commons-lang-2.6.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-client",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-client-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-xml",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-xml-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-queryparser",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-queryparser-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.opensaml_openws",
					"version": "1.5.6",
					"path": "/opt/genesys/application/gws.jar/openws-1.5.6.jar"
				},
				{
					"type": "jar",
					"name": "spring-webmvc",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-webmvc-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-continuation",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-continuation-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "joda-time_joda-time",
					"version": "2.2",
					"path": "/opt/genesys/application/gws.jar/joda-time-2.2.jar",
					"licenses": [
						"Apache 2"
					]
				},
				{
					"type": "jar",
					"name": "spring-boot-jarmode-layertools",
					"version": "2.7.8",
					"path": "/opt/genesys/application/gws.jar/spring-boot-jarmode-layertools-2.7.8.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.httpcomponents_httpcore",
					"version": "4.4.13",
					"path": "/opt/genesys/application/gws.jar/httpcore-4.4.13.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-redis",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-redis-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_openmediaprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/openmediaprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-jvm",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-jvm-3.1.0.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-handler-ssl-ocsp",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-handler-ssl-ocsp-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "spring-boot",
					"version": "2.7.8",
					"path": "/opt/genesys/application/gws.jar/spring-boot-2.7.8.jar"
				},
				{
					"type": "jar",
					"name": "commons-io_commons-io",
					"version": "2.5",
					"path": "/opt/genesys/application/gws.jar/velocity-engine-core-2.0.jar"
				},
				{
					"type": "jar",
					"name": "com.codahale.metrics_metrics-core",
					"version": "3.0.2",
					"path": "/opt/genesys/application/gws.jar/metrics-core-3.0.2.jar"
				},
				{
					"type": "jar",
					"name": "com.google.errorprone_error_prone_annotations",
					"version": "2.3.4",
					"path": "/opt/genesys/application/gws.jar/error_prone_annotations-2.3.4.jar",
					"licenses": [
						"Apache 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.jvnet.staxex_stax-ex",
					"version": "1.8",
					"path": "/opt/genesys/application/gws.jar/stax-ex-1.8.jar",
					"licenses": [
						"\n                Dual license consisting of the CDDL v1.1 and GPL v2\n            "
					]
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_comappblock",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/comappblock-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-handler",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-handler-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-xml",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-xml-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "spring-oxm",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-oxm-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "commons-fileupload_commons-fileupload",
					"version": "1.3.3",
					"path": "/opt/genesys/application/gws.jar/commons-fileupload-1.3.3.jar"
				},
				{
					"type": "jar",
					"name": "org.cometd.java_bayeux-api",
					"version": "3.1.12",
					"path": "/opt/genesys/application/gws.jar/bayeux-api-3.1.12.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_outboundprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/outboundprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-memcache",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-memcache-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "io.github.x-stream_mxparser",
					"version": "1.2.2",
					"path": "/opt/genesys/application/gws.jar/mxparser-1.2.2.jar",
					"licenses": [
						"Indiana University Extreme! Lab Software License"
					]
				},
				{
					"type": "jar",
					"name": "com.thoughtworks.xstream_xstream",
					"version": "1.4.18",
					"path": "/opt/genesys/application/gws.jar/xstream-1.4.18.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.core_jackson-databind",
					"version": "2.13.4.2",
					"path": "/opt/genesys/application/gws.jar/jackson-databind-2.13.4.2.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_websocket-common",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/websocket-common-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-util-ajax",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-util-ajax-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "tomcat-embed-el",
					"version": "9.0.71",
					"path": "/opt/genesys/application/gws.jar/tomcat-embed-el-9.0.71.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.module_jackson-module-parameter-names",
					"version": "2.13.4",
					"path": "/opt/genesys/application/gws.jar/jackson-module-parameter-names-2.13.4.jar"
				},
				{
					"type": "jar",
					"name": "javax.activation_javax.activation-api",
					"version": "1.2.0",
					"path": "/opt/genesys/application/gws.jar/javax.activation-api-1.2.0.jar"
				},
				{
					"type": "jar",
					"name": "spring-security-web",
					"version": "5.7.6",
					"path": "/opt/genesys/application/gws.jar/spring-security-web-5.7.6.jar"
				},
				{
					"type": "jar",
					"name": "reactor-core",
					"version": "3.4.18",
					"path": "/opt/genesys/application/gws.jar/reactor-core-3.4.18.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-codecs",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-codecs-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_websocket-servlet",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/websocket-servlet-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-stomp",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-stomp-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "javax.annotation_javax.annotation-api",
					"version": "1.3.2",
					"path": "/opt/genesys/application/gws.jar/javax.annotation-api-1.3.2.jar",
					"licenses": [
						"CDDL + GPLv2 with classpath exception"
					]
				},
				{
					"type": "jar",
					"name": "org.glassfish.jaxb_txw2",
					"version": "2.3.1",
					"path": "/opt/genesys/application/gws.jar/txw2-2.3.1.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.logging.log4j_log4j-api",
					"version": "2.17.2",
					"path": "/opt/genesys/application/gws.jar/log4j-api-2.17.2.jar"
				},
				{
					"type": "jar",
					"name": "jsr250-api",
					"version": "1.0",
					"path": "/opt/genesys/application/gws.jar/jsr250-api-1.0.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.logging.log4j_log4j-to-slf4j",
					"version": "2.17.2",
					"path": "/opt/genesys/application/gws.jar/log4j-to-slf4j-2.17.2.jar"
				},
				{
					"type": "jar",
					"name": "spring-security-config",
					"version": "5.7.6",
					"path": "/opt/genesys/application/gws.jar/spring-security-config-5.7.6.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-jmx",
					"version": "9.2.29.v20191105",
					"path": "/opt/genesys/application/gws.jar/jetty-jmx-9.2.29.v20191105.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-analyzers-common",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-analyzers-common-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-smtp",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-smtp-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "spring-security-crypto",
					"version": "5.7.6",
					"path": "/opt/genesys/application/gws.jar/spring-security-crypto-5.7.6.jar"
				},
				{
					"type": "jar",
					"name": "com.spatial4j_spatial4j",
					"version": "0.3",
					"path": "/opt/genesys/application/gws.jar/spatial4j-0.3.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "spring-aop",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-aop-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-resolver-dns-native-macos",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-resolver-dns-native-macos-4.1.87.Final-osx-aarch_64.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-server",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-server-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.slf4j_slf4j-api",
					"version": "1.7.36",
					"path": "/opt/genesys/application/gws.jar/slf4j-api-1.7.36.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-json",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-json-3.1.0.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_routingprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/routingprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "jakarta.servlet_jakarta.servlet-api",
					"version": "4.0.4",
					"path": "/opt/genesys/application/gws.jar/jakarta.servlet-api-4.0.4.jar",
					"licenses": [
						"EPL 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.hdrhistogram_HdrHistogram",
					"version": "2.1.12",
					"path": "/opt/genesys/application/gws.jar/HdrHistogram-2.1.12.jar",
					"licenses": [
						"Public Domain, per Creative Commons CC0"
					]
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_reportingprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/reportingprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "elasticsearch-java",
					"version": "8.8.2",
					"path": "/opt/genesys/application/gws.jar/elasticsearch-java-8.8.2.jar"
				},
				{
					"type": "jar",
					"name": "spring-tx",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-tx-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-rxtx",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-rxtx-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.httpcomponents_httpcore-nio",
					"version": "4.4.13",
					"path": "/opt/genesys/application/gws.jar/httpcore-nio-4.4.13.jar"
				},
				{
					"type": "jar",
					"name": "spring-web",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-web-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-native-epoll",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-native-epoll-4.1.87.Final-linux-aarch_64.jar"
				},
				{
					"type": "jar",
					"name": "asm-tree",
					"version": "9.4",
					"path": "/opt/genesys/application/gws.jar/asm-tree-9.4.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-dns",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-dns-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "jakarta.annotation_jakarta.annotation-api",
					"version": "1.3.5",
					"path": "/opt/genesys/application/gws.jar/jakarta.annotation-api-1.3.5.jar",
					"licenses": [
						"EPL 2.0"
					]
				},
				{
					"type": "jar",
					"name": "checker-qual",
					"version": "3.3.0",
					"path": "/opt/genesys/application/gws.jar/checker-qual-3.3.0.jar"
				},
				{
					"type": "jar",
					"name": "org.bouncycastle_bcprov-ext-jdk15on",
					"version": "1.60",
					"path": "/opt/genesys/application/gws.jar/bcprov-ext-jdk15on-1.60.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.cometd.java_cometd-java-common",
					"version": "3.1.12",
					"path": "/opt/genesys/application/gws.jar/cometd-java-common-3.1.12.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-http2",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-http2-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.bouncycastle_bcprov-jdk15on",
					"version": "1.60",
					"path": "/opt/genesys/application/gws.jar/bcprov-jdk15on-1.60.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-queries",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-queries-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "net.sf.ehcache_sizeof-agent",
					"version": "1.0.1",
					"path": "/opt/genesys/application/gws.jar/ehcache-core-2.6.2.jar/sizeof-agent.jar"
				},
				{
					"type": "jar",
					"name": "javax.mail_mail",
					"version": "1.4.7",
					"path": "/opt/genesys/application/gws.jar/mail-1.4.7.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-mqtt",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-mqtt-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "com.sun.xml.fastinfoset_FastInfoset",
					"version": "1.2.15",
					"path": "/opt/genesys/application/gws.jar/FastInfoset-1.2.15.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.xalan_xalan",
					"version": "2.7.2",
					"path": "/opt/genesys/application/gws.jar/xalan-2.7.2.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_messagebrokerappblock",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/messagebrokerappblock-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.core_jackson-core",
					"version": "2.13.4",
					"path": "/opt/genesys/application/gws.jar/jackson-core-2.13.4.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "ch.qos.logback_logback-core",
					"version": "1.2.11",
					"path": "/opt/genesys/application/gws.jar/logback-core-1.2.11.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-native-kqueue",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-native-kqueue-4.1.87.Final-osx-aarch_64.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-resolver",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-resolver-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "jakarta.json_jakarta.json-api",
					"version": "2.0.1",
					"path": "/opt/genesys/application/gws.jar/jakarta.json-api-2.0.1.jar",
					"licenses": [
						"Eclipse Public License 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_javax-websocket-client-impl",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/javax-websocket-client-impl-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.bouncycastle_bcpkix-jdk15on",
					"version": "1.60",
					"path": "/opt/genesys/application/gws.jar/bcpkix-jdk15on-1.60.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.datatype_jackson-datatype-json-org",
					"version": "2.13.4",
					"path": "/opt/genesys/application/gws.jar/jackson-datatype-json-org-2.13.4.jar"
				},
				{
					"type": "jar",
					"name": "spring-boot-actuator",
					"version": "2.7.8",
					"path": "/opt/genesys/application/gws.jar/spring-boot-actuator-2.7.8.jar"
				},
				{
					"type": "jar",
					"name": "asm-commons",
					"version": "9.4",
					"path": "/opt/genesys/application/gws.jar/asm-commons-9.4.jar"
				},
				{
					"type": "jar",
					"name": "elasticsearch",
					"version": "1.0.1",
					"path": "/opt/genesys/application/gws.jar/elasticsearch-1.0.1.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-suggest",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-suggest-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.cometd.java_cometd-java-websocket-common-server",
					"version": "3.1.12",
					"path": "/opt/genesys/application/gws.jar/cometd-java-websocket-common-server-3.1.12.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.parsson_parsson",
					"version": "1.0.0",
					"path": "/opt/genesys/application/gws.jar/parsson-1.0.0.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.httpcomponents_httpasyncclient",
					"version": "4.1.5",
					"path": "/opt/genesys/application/gws.jar/httpasyncclient-4.1.5.jar"
				},
				{
					"type": "jar",
					"name": "commons-io_commons-io",
					"version": "2.2",
					"path": "/opt/genesys/application/gws.jar/commons-io-2.2.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-servlet",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-servlet-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-resolver-dns",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-resolver-dns-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-common",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-common-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "commons-logging_commons-logging",
					"version": "1.2",
					"path": "/opt/genesys/application/gws.jar/commons-logging-1.2.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-grouping",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-grouping-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.springframework.data_spring-data-redis",
					"version": "2.7.7",
					"path": "/opt/genesys/application/gws.jar/spring-data-redis-2.7.7.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-resolver-dns-classes-macos",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-resolver-dns-classes-macos-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-haproxy",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-haproxy-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-core",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-core-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.commons_commons-lang3",
					"version": "3.9",
					"path": "/opt/genesys/application/gws.jar/commons-lang3-3.9.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-jetty9",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-jetty9-3.1.0.jar"
				},
				{
					"type": "jar",
					"name": "io.lettuce_lettuce-core",
					"version": "6.1.10.RELEASE",
					"path": "/opt/genesys/application/gws.jar/lettuce-core-6.1.10.RELEASE.jar",
					"licenses": [
						"Apache License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.json_json",
					"version": "20190722",
					"path": "/opt/genesys/application/gws.jar/json-20190722.jar",
					"licenses": [
						"The JSON License"
					]
				},
				{
					"type": "jar",
					"name": "org.aspectj.weaver_aspectjweaver",
					"version": "1.9.7",
					"path": "/opt/genesys/application/gws.jar/aspectjweaver-1.9.7.jar"
				},
				{
					"type": "jar",
					"name": "xmlpull",
					"version": "1.1.3.1",
					"path": "/opt/genesys/application/gws.jar/xmlpull-1.1.3.1.jar"
				},
				{
					"type": "jar",
					"name": "com.google.guava_guava",
					"version": "13.0.1",
					"path": "/opt/genesys/application/gws.jar/guava-13.0.1.jar"
				},
				{
					"type": "jar",
					"name": "elasticsearch-rest-client",
					"version": "8.8.2",
					"path": "/opt/genesys/application/gws.jar/elasticsearch-rest-client-8.8.2.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.santuario_xmlsec",
					"version": "1.5.8",
					"path": "/opt/genesys/application/gws.jar/xmlsec-1.5.8.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_commonsappblock",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/commonsappblock-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_protocolmanagerappblock",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/protocolmanagerappblock-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-io",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-io-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.latencyutils_LatencyUtils",
					"version": "2.0.3",
					"path": "/opt/genesys/application/gws.jar/LatencyUtils-2.0.3.jar",
					"licenses": [
						"Public Domain, per Creative Commons CC0"
					]
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-misc",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-misc-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-classes-epoll",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-classes-epoll-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.datatype_jackson-datatype-jdk8",
					"version": "2.13.4",
					"path": "/opt/genesys/application/gws.jar/jackson-datatype-jdk8-2.13.4.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-memory",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-memory-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_webmediaprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/webmediaprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "spring-boot-actuator-autoconfigure",
					"version": "2.7.8",
					"path": "/opt/genesys/application/gws.jar/spring-boot-actuator-autoconfigure-2.7.8.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-sandbox",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-sandbox-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_websocket-api",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/websocket-api-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "commons-collections_commons-collections",
					"version": "3.2.2",
					"path": "/opt/genesys/application/gws.jar/commons-collections-3.2.2.jar"
				},
				{
					"type": "jar",
					"name": "org.springframework.data_spring-data-commons",
					"version": "2.7.7",
					"path": "/opt/genesys/application/gws.jar/spring-data-commons-2.7.7.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-sctp",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-sctp-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "jakarta.websocket_jakarta.websocket-api",
					"version": "1.1.2",
					"path": "/opt/genesys/application/gws.jar/jakarta.websocket-api-1.1.2.jar"
				},
				{
					"type": "jar",
					"name": "com.sun.istack_istack-commons-runtime",
					"version": "3.0.7",
					"path": "/opt/genesys/application/gws.jar/istack-commons-runtime-3.0.7.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-spatial",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-spatial-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-plus",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-plus-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_commons",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/commons-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "caffeine",
					"version": "2.8.2",
					"path": "/opt/genesys/application/gws.jar/caffeine-2.8.2.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_websocket-server",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/websocket-server-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-security",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-security-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.slf4j_jcl-over-slf4j",
					"version": "1.7.5",
					"path": "/opt/genesys/application/gws.jar/jcl-over-slf4j-1.7.5.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_warmstandbyappblock",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/warmstandbyappblock-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_kvlistbinding",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/kvlistbinding-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "spring-context-support",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-context-support-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "asm",
					"version": "9.4",
					"path": "/opt/genesys/application/gws.jar/asm-9.4.jar"
				},
				{
					"type": "jar",
					"name": "net.sf.ehcache_ehcache-core",
					"version": "2.6.2",
					"path": "/opt/genesys/application/gws.jar/ehcache-core-2.6.2.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_clusterprotocolappblock",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/clusterprotocolappblock-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_managementprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/managementprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "org.bouncycastle_bcmail-jdk15on",
					"version": "1.51",
					"path": "/opt/genesys/application/gws.jar/bcmail-jdk15on-1.51.jar"
				},
				{
					"type": "jar",
					"name": "spring-expression",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-expression-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "jackson-core-asl",
					"version": "1.9.13",
					"path": "/opt/genesys/application/gws.jar/jackson-core-asl-1.9.13.jar"
				},
				{
					"type": "jar",
					"name": "tomcat-embed-websocket",
					"version": "9.0.71",
					"path": "/opt/genesys/application/gws.jar/tomcat-embed-websocket-9.0.71.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-all",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-all-4.1.87.Final.jar",
					"licenses": [
						"Apache License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.owasp.esapi_esapi",
					"version": "2.1.0.1",
					"path": "/opt/genesys/application/gws.jar/esapi-2.1.0.1.jar",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "jar",
					"name": "org.slf4j_jul-to-slf4j",
					"version": "1.7.36",
					"path": "/opt/genesys/application/gws.jar/jul-to-slf4j-1.7.36.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-handler-proxy",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-handler-proxy-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-socks",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-socks-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "javax.servlet_javax.servlet-api",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/javax.servlet-api-3.1.0.jar",
					"licenses": [
						"CDDL + GPLv2 with classpath exception"
					]
				},
				{
					"type": "jar",
					"name": "org.glassfish.jaxb_jaxb-runtime",
					"version": "2.3.1",
					"path": "/opt/genesys/application/gws.jar/jaxb-runtime-2.3.1.jar"
				},
				{
					"type": "jar",
					"name": "org.springframework.security.oauth_spring-security-oauth2",
					"version": "2.0.8.RELEASE",
					"path": "/opt/genesys/application/gws.jar/spring-security-oauth2-2.0.8.RELEASE.jar"
				},
				{
					"type": "jar",
					"name": "org.opensaml_opensaml",
					"version": "2.6.6",
					"path": "/opt/genesys/application/gws.jar/opensaml-2.6.6.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.velocity_velocity-engine-core",
					"version": "2.0",
					"path": "/opt/genesys/application/gws.jar/velocity-engine-core-2.0.jar"
				},
				{
					"type": "jar",
					"name": "spring-core",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-core-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-servlets",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-servlets-3.1.0.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_voiceprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/voiceprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_websocket-client",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/websocket-client-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-join",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-join-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "tomcat-embed-core",
					"version": "9.0.71",
					"path": "/opt/genesys/application/gws.jar/tomcat-embed-core-9.0.71.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty.websocket_javax-websocket-server-impl",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/javax-websocket-server-impl-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_connection",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/connection-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_switchpolicy",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/switchpolicy-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-http",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-http-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "spring-security-saml2-core",
					"version": "1.0.9.RELEASE",
					"path": "/opt/genesys/application/gws.jar/spring-security-saml2-core-1.0.9.RELEASE.jar"
				},
				{
					"type": "jar",
					"name": "javax.activation_activation",
					"version": "1.1",
					"path": "/opt/genesys/application/gws.jar/activation-1.1.jar"
				},
				{
					"type": "jar",
					"name": "org.cometd.java_cometd-java-annotations",
					"version": "3.1.12",
					"path": "/opt/genesys/application/gws.jar/cometd-java-annotations-3.1.12.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-buffer",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-buffer-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.cometd.java_cometd-java-server",
					"version": "3.1.12",
					"path": "/opt/genesys/application/gws.jar/cometd-java-server-3.1.12.jar"
				},
				{
					"type": "jar",
					"name": "org.opensaml_xmltooling",
					"version": "1.4.6",
					"path": "/opt/genesys/application/gws.jar/xmltooling-1.4.6.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-classes-kqueue",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-classes-kqueue-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_kvlists",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/kvlists-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.core_jackson-annotations",
					"version": "2.13.4",
					"path": "/opt/genesys/application/gws.jar/jackson-annotations-2.13.4.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "restfb",
					"version": "1.6.12",
					"path": "/opt/genesys/application/gws.jar/restfb-1.6.12.jar"
				},
				{
					"type": "jar",
					"name": "jrt-fs",
					"version": "17.0.8",
					"path": "/usr/lib/jvm/java-17-openjdk-17.0.8.0.7-2.el8.x86_64/lib/jrt-fs.jar"
				},
				{
					"type": "jar",
					"name": "com.googlecode.libphonenumber_libphonenumber",
					"version": "4.3",
					"path": "/opt/genesys/application/gws.jar/libphonenumber-4.3.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-annotations",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-annotations-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "com.codahale.metrics_metrics-healthchecks",
					"version": "3.0.2",
					"path": "/opt/genesys/application/gws.jar/metrics-healthchecks-3.0.2.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-codec-http",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-codec-http-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "org.jctools_jctools-core",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/netty-common-4.1.87.Final.jar",
					"licenses": [
						"Apache License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "spring-boot-autoconfigure",
					"version": "2.7.8",
					"path": "/opt/genesys/application/gws.jar/spring-boot-autoconfigure-2.7.8.jar"
				},
				{
					"type": "jar",
					"name": "com.ryantenney.metrics_metrics-spring",
					"version": "3.0.3",
					"path": "/opt/genesys/application/gws.jar/metrics-spring-3.0.3.jar",
					"licenses": [
						"Apache License 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-webapp",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-webapp-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "javax.xml.bind_jaxb-api",
					"version": "2.3.1",
					"path": "/opt/genesys/application/gws.jar/jaxb-api-2.3.1.jar"
				},
				{
					"type": "jar",
					"name": "com.narupley_not-going-to-be-commons-ssl",
					"version": "0.3.20",
					"path": "/opt/genesys/application/gws.jar/not-going-to-be-commons-ssl-0.3.20.jar",
					"licenses": [
						"The Apache License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_protocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/protocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "spring-webflux",
					"version": "5.3.20",
					"path": "/opt/genesys/application/gws.jar/spring-webflux-5.3.20.jar"
				},
				{
					"type": "jar",
					"name": "ch.qos.logback_logback-classic",
					"version": "1.2.11",
					"path": "/opt/genesys/application/gws.jar/logback-classic-1.2.11.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-native-unix-common",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-native-unix-common-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "commons-httpclient_commons-httpclient",
					"version": "3.1",
					"path": "/opt/genesys/application/gws.jar/commons-httpclient-3.1.jar"
				},
				{
					"type": "jar",
					"name": "com.googlecode.libphonenumber_geocoder",
					"version": "1.7",
					"path": "/opt/genesys/application/gws.jar/geocoder-1.7.jar"
				},
				{
					"type": "jar",
					"name": "com.codahale.metrics_metrics-annotation",
					"version": "3.0.2",
					"path": "/opt/genesys/application/gws.jar/metrics-annotation-3.0.2.jar"
				},
				{
					"type": "jar",
					"name": "gws-library-redis",
					"version": "9.0.100.00.24",
					"path": "/opt/genesys/application/gws.jar/gws-library-redis-9.0.100.00.24.jar"
				},
				{
					"type": "jar",
					"name": "micrometer-core",
					"version": "1.9.7",
					"path": "/opt/genesys/application/gws.jar/micrometer-core-1.9.7.jar"
				},
				{
					"type": "jar",
					"name": "jakarta-regexp",
					"version": "1.4",
					"path": "/opt/genesys/application/gws.jar/jakarta-regexp-1.4.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_jackson2-module",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/jackson2-module-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "spring-jcl",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-jcl-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "spring-context",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-context-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "spring-security-core",
					"version": "5.7.6",
					"path": "/opt/genesys/application/gws.jar/spring-security-core-5.7.6.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-core",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-core-3.1.0.jar"
				},
				{
					"type": "jar",
					"name": "commons-codec_commons-codec",
					"version": "1.15",
					"path": "/opt/genesys/application/gws.jar/commons-codec-1.15.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.lucene_lucene-highlighter",
					"version": "4.6.1",
					"path": "/opt/genesys/application/gws.jar/lucene-highlighter-4.6.1.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.xmlcommons.Version_xml-apis",
					"version": "1.4.01",
					"path": "/opt/genesys/application/gws.jar/xml-apis-1.4.01.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_configurationprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/configurationprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "org.apache.xml.serializer_serializer",
					"version": "2.7.2",
					"path": "/opt/genesys/application/gws.jar/serializer-2.7.2.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_contactsprotocol",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/contactsprotocol-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "com.fasterxml.jackson.datatype_jackson-datatype-jsr310",
					"version": "2.13.4",
					"path": "/opt/genesys/application/gws.jar/jackson-datatype-jsr310-2.13.4.jar"
				},
				{
					"type": "jar",
					"name": "jackson-mapper-asl",
					"version": "1.9.13",
					"path": "/opt/genesys/application/gws.jar/jackson-mapper-asl-1.9.13.jar"
				},
				{
					"type": "jar",
					"name": "com.genesyslab.platform_logging",
					"version": "900.10.0",
					"path": "/opt/genesys/application/gws.jar/logging-900.10.0.jar"
				},
				{
					"type": "jar",
					"name": "org.eclipse.jetty_jetty-util",
					"version": "9.4.50.v20221201",
					"path": "/opt/genesys/application/gws.jar/jetty-util-9.4.50.v20221201.jar"
				},
				{
					"type": "jar",
					"name": "spring-beans",
					"version": "5.3.25",
					"path": "/opt/genesys/application/gws.jar/spring-beans-5.3.25.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-servlet",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-servlet-3.1.0.jar"
				},
				{
					"type": "jar",
					"name": "io.netty_netty-transport-udt",
					"version": "4.1.87.Final",
					"path": "/opt/genesys/application/gws.jar/netty-transport-udt-4.1.87.Final.jar"
				},
				{
					"type": "jar",
					"name": "com.google.code.findbugs_jsr305",
					"version": "3.0.2",
					"path": "/opt/genesys/application/gws.jar/jsr305-3.0.2.jar",
					"licenses": [
						"The Apache Software License, Version 2.0"
					]
				},
				{
					"type": "jar",
					"name": "org.json",
					"version": "2.0",
					"path": "/opt/genesys/application/gws.jar/org.json-2.0.jar"
				},
				{
					"type": "jar",
					"name": "reactive-streams",
					"version": "1.0.3",
					"path": "/opt/genesys/application/gws.jar/reactive-streams-1.0.3.jar"
				},
				{
					"type": "jar",
					"name": "io.dropwizard.metrics_metrics-healthchecks",
					"version": "3.1.0",
					"path": "/opt/genesys/application/gws.jar/metrics-healthchecks-3.1.0.jar"
				},
				{
					"type": "python",
					"name": "decorator",
					"version": "4.2.1",
					"path": "/usr/lib/python3.6/site-packages/decorator-4.2.1-py3.6.egg-info",
					"licenses": [
						"new BSD License"
					]
				},
				{
					"type": "python",
					"name": "idna",
					"version": "2.5",
					"path": "/usr/lib/python3.6/site-packages/idna-2.5-py3.6.egg-info",
					"licenses": [
						"BSD-like"
					]
				},
				{
					"type": "python",
					"name": "requests",
					"version": "2.20.0",
					"path": "/usr/lib/python3.6/site-packages/requests-2.20.0-py3.6.egg-info",
					"licenses": [
						"Apache 2.0"
					]
				},
				{
					"type": "python",
					"name": "six",
					"version": "1.11.0",
					"path": "/usr/lib/python3.6/site-packages/six-1.11.0.dist-info",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "python",
					"name": "rpm",
					"version": "4.14.3",
					"path": "/usr/lib64/python3.6/site-packages",
					"licenses": [
						"UNKNOWN"
					]
				},
				{
					"type": "python",
					"name": "systemd-python",
					"version": "234",
					"path": "/usr/lib64/python3.6/site-packages",
					"licenses": [
						"LGPLv2+"
					]
				},
				{
					"type": "python",
					"name": "chardet",
					"version": "3.0.4",
					"path": "/usr/lib/python3.6/site-packages/chardet-3.0.4-py3.6.egg-info",
					"licenses": [
						"LGPL"
					]
				},
				{
					"type": "python",
					"name": "python-dateutil",
					"version": "2.6.1",
					"path": "/usr/lib/python3.6/site-packages/python_dateutil-2.6.1-py3.6.egg-info",
					"licenses": [
						"Simplified BSD"
					]
				},
				{
					"type": "python",
					"name": "ethtool",
					"version": "0.14",
					"path": "/usr/lib64/python3.6/site-packages/ethtool-0.14-py3.6.egg-info",
					"licenses": [
						"GPL-2.0"
					]
				},
				{
					"type": "python",
					"name": "gpg",
					"version": "1.13.1",
					"path": "/usr/lib64/python3.6/site-packages",
					"licenses": [
						"LGPL2.1+ (the library), GPL2+ (tests and examples)"
					]
				},
				{
					"type": "python",
					"name": "libcomps",
					"version": "0.1.18",
					"path": "/usr/lib64/python3.6/site-packages/libcomps-0.1.18-py3.6.egg-info",
					"licenses": [
						"GPLv2+"
					]
				},
				{
					"type": "python",
					"name": "python-dmidecode",
					"version": "3.12.2",
					"path": "/usr/lib64/python3.6/site-packages",
					"licenses": [
						"GPL-2"
					]
				},
				{
					"type": "python",
					"name": "iniparse",
					"version": "0.4",
					"path": "/usr/lib/python3.6/site-packages/iniparse-0.4-py3.6.egg-info",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "python",
					"name": "pyinotify",
					"version": "0.9.6",
					"path": "/usr/lib/python3.6/site-packages/pyinotify-0.9.6-py3.6.egg-info",
					"licenses": [
						"MIT License"
					]
				},
				{
					"type": "python",
					"name": "syspurpose",
					"version": "1.28.36",
					"path": "/usr/lib/python3.6/site-packages/syspurpose-1.28.36-py3.6.egg-info",
					"licenses": [
						"GPLv2"
					]
				},
				{
					"type": "python",
					"name": "dbus-python",
					"version": "1.2.4",
					"path": "/usr/lib64/python3.6/site-packages/dbus_python-1.2.4-py3.6.egg-info",
					"licenses": [
						"Expat (MIT/X11)"
					]
				},
				{
					"type": "python",
					"name": "pygobject",
					"version": "3.28.3",
					"path": "/usr/lib64/python3.6/site-packages",
					"licenses": [
						"GNU LGPL"
					]
				},
				{
					"type": "python",
					"name": "pysocks",
					"version": "1.6.8",
					"path": "/usr/lib/python3.6/site-packages/PySocks-1.6.8-py3.6.egg-info",
					"licenses": [
						"BSD"
					]
				},
				{
					"type": "python",
					"name": "setuptools",
					"version": "39.2.0",
					"path": "/usr/lib/python3.6/site-packages/setuptools-39.2.0.dist-info",
					"licenses": [
						"UNKNOWN"
					]
				},
				{
					"type": "python",
					"name": "urllib3",
					"version": "1.24.2",
					"path": "/usr/lib/python3.6/site-packages/urllib3-1.24.2-py3.6.egg-info",
					"licenses": [
						"MIT"
					]
				},
				{
					"type": "python",
					"name": "subscription-manager",
					"version": "1.28.36",
					"path": "/usr/lib64/python3.6/site-packages/subscription_manager-1.28.36-py3.6.egg-info",
					"licenses": [
						"GPLv2"
					]
				}
			],
			"applications": [
				{
					"name": "java",
					"version": "17.0.8",
					"path": "/usr/lib/jvm/java-17-openjdk-17.0.8.0.7-2.el8.x86_64/bin/java"
				}
			],
			"complianceDistribution": {
				"critical": 0,
				"high": 0,
				"medium": 0,
				"low": 0,
				"total": 0
			},
			"complianceScanPassed": true,
			"vulnerabilities": [
				{
					"id": "CVE-2023-34034",
					"status": "fixed in 6.1.2, 6.0.5, 5.8.5,...",
					"cvss": 9.8,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "Using \\\"**\\\" as a pattern in Spring Security configuration  for WebFlux creates a mismatch in pattern matching between Spring  Security and Spring WebFlux, and the potential for a security bypass.  ",
					"severity": "critical",
					"packageName": "spring-security-core",
					"packageVersion": "5.7.6",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-34034",
					"riskFactors": [
						"Has fix",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network",
						"Critical severity",
						"DoS - High"
					],
					"impactedVersions": [
						"\u003c5.7.10,5.7",
						"\u003e=5.7.0,5.7"
					],
					"publishedDate": "2023-07-19T08:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -17,
					"fixDate": "2023-07-28T11:46:54-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-core-5.7.6.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20862",
					"status": "fixed in 6.0.3, 5.8.3, 5.7.8",
					"cvss": 9.8,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "In Spring Security, versions 5.7.x prior to 5.7.8, versions 5.8.x prior to 5.8.3, and versions 6.0.x prior to 6.0.3, the logout support does not properly clean the security context if using serialized versions. Additionally, it is not possible to explicitly save an empty security context to the HttpSessionSecurityContextRepository. This vulnerability can keep users authenticated even after they performed logout. Users of affected versions should apply the following mitigation. 5.7.x users should upgrade to 5.7.8. 5.8.x users should upgrade to 5.8.3. 6.0.x users should upgrade to 6.0.3.",
					"severity": "critical",
					"packageName": "spring-security-core",
					"packageVersion": "5.7.6",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20862",
					"riskFactors": [
						"Recent vulnerability",
						"Attack vector: network",
						"Critical severity",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c5.7.8,5.7",
						"\u003e=5.7.0,5.7"
					],
					"publishedDate": "2023-04-19T13:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -105,
					"fixDate": "2023-05-01T16:32:12-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-core-5.7.6.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-1471",
					"status": "fixed in 2.0",
					"cvss": 9.8,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "SnakeYaml\\'s Constructor() class does not restrict types which can be instantiated during deserialization.u00a0Deserializing yaml content provided by an attacker can lead to remote code execution. We recommend using SnakeYaml\\'s SafeConsturctor when parsing untrusted content to restrict deserialization. We recommend upgrading to version 2.0 and beyond. ",
					"severity": "critical",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-1471",
					"riskFactors": [
						"Has fix",
						"Remote execution",
						"Attack complexity: low",
						"Attack vector: network",
						"Critical severity",
						"DoS - High",
						"Exploit exists - POC"
					],
					"impactedVersions": [
						"\u003c2.0"
					],
					"publishedDate": "2022-12-01T03:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -251,
					"fixDate": "2022-12-06T11:59:50-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2016-1000027",
					"status": "fixed in 6.0.0",
					"cvss": 9.8,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "Pivotal Spring Framework through 5.3.16 suffers from a potential remote code execution (RCE) issue if used for Java deserialization of untrusted data. Depending on how the library is implemented within a product, this issue may or not occur, and authentication may be required. NOTE: the vendor\\'s position is that untrusted data is not an intended use case. The product\\'s behavior will not be changed because some users rely on deserialization of trusted data.",
					"severity": "critical",
					"packageName": "spring-web",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2016-1000027",
					"riskFactors": [
						"Remote execution",
						"Attack complexity: low",
						"Attack vector: network",
						"Critical severity",
						"DoS - High",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c6.0.0"
					],
					"publishedDate": "2020-01-02T15:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -447,
					"fixDate": "2022-05-24T10:05:30-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-web-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-34034",
					"status": "fixed in 6.1.2, 6.0.5, 5.8.5, 5.7.10, 5.6.12",
					"cvss": 9,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "Using \\\"**\\\" as a pattern in Spring Security configuration  for WebFlux creates a mismatch in pattern matching between Spring  Security and Spring WebFlux, and the potential for a security bypass.  ",
					"severity": "critical",
					"packageName": "spring-security-config",
					"packageVersion": "5.7.6",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-34034",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"Critical severity",
						"DoS - High",
						"Has fix",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003e=5.7.0",
						"\u003c5.7.10"
					],
					"publishedDate": "2023-07-19T08:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -14,
					"fixDate": "2023-07-31T16:20:39-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-config-5.7.6.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20873",
					"status": "fixed in 2.7.11, 3.0.6",
					"cvss": 9,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "In Spring Boot versions 3.0.0 - 3.0.5, 2.7.0 - 2.7.10, and older unsupported versions, an application that is deployed to Cloud Foundry could be susceptible to a security bypass. Users of affected versions should apply the following mitigation: 3.0.x users should upgrade to 3.0.6+. 2.7.x users should upgrade to 2.7.11+. Users of older, unsupported versions should upgrade to 3.0.6+ or 2.7.11+.",
					"severity": "critical",
					"packageName": "spring-boot-actuator-autoconfigure",
					"packageVersion": "2.7.8",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20873",
					"riskFactors": [
						"Has fix",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network",
						"Critical severity",
						"DoS - High"
					],
					"impactedVersions": [
						"\u003c2.7.11"
					],
					"publishedDate": "2023-04-20T14:33:27-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -112,
					"fixDate": "2023-04-24T13:52:08-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-boot-actuator-autoconfigure-2.7.8.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2018-1260",
					"status": "fixed in 2.1.2, 2.0.15, 2.2.2, 2.3.3",
					"cvss": 9,
					"vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "Spring Security OAuth, versions 2.3 prior to 2.3.3, 2.2 prior to 2.2.2, 2.1 prior to 2.1.2, 2.0 prior to 2.0.15 and older unsupported versions contains a remote code execution vulnerability. A malicious user or attacker can craft an authorization request to the authorization endpoint that can lead to remote code execution when the resource owner is forwarded to the approval endpoint.",
					"severity": "critical",
					"packageName": "org.springframework.security.oauth_spring-security-oauth2",
					"packageVersion": "2.0.8.RELEASE",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2018-1260",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"Critical severity",
						"DoS - High",
						"Has fix",
						"Remote execution"
					],
					"impactedVersions": [
						"\u003e=2.0.0",
						"\u003c2.0.15"
					],
					"publishedDate": "2018-10-18T11:05:34-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -1761,
					"fixDate": "2018-10-18T11:05:34-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-oauth2-2.0.8.RELEASE.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2020-13936",
					"status": "fixed in 2.3",
					"cvss": 8.8,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
					"description": "An attacker that is able to modify Velocity templates may execute arbitrary Java code or run arbitrary system commands with the same privileges as the account running the Servlet container. This applies to applications that allow untrusted users to upload/modify velocity templates running Apache Velocity Engine versions up to 2.2.",
					"severity": "high",
					"packageName": "org.apache.velocity_velocity-engine-core",
					"packageVersion": "2.0",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2020-13936",
					"riskFactors": [
						"Remote execution",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c2.3"
					],
					"publishedDate": "2021-03-10T00:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -864,
					"fixDate": "2021-03-10T00:15:00-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/velocity-engine-core-2.0.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "PRISMA-2023-0067",
					"status": "fixed in 2.15.0",
					"cvss": 7.5,
					"description": "com.fasterxml.jackson.core_jackson-core package versions before 2.15.0 are vulnerable to Denial of Service (DoS). The package does not properly restrict the size or amount of resources that are requested or influenced by an actor, which can be used to consume more resources than intended and leads to Uncontrolled Resource Consumption (\\'Resource Exhaustion\\').",
					"severity": "high",
					"packageName": "com.fasterxml.jackson.core_jackson-core",
					"packageVersion": "2.13.4",
					"link": "https://github.com/FasterXML/jackson-core/pull/827",
					"riskFactors": [
						"DoS - High",
						"Has fix",
						"High severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c2.15.0"
					],
					"publishedDate": "2023-04-24T04:01:32-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -89,
					"fixDate": "2023-04-23T17:00:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/jackson-core-2.13.4.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "PRISMA-2021-0081",
					"status": "fixed in 8.10.0",
					"cvss": 7.5,
					"description": "Apache Lucene is vulnerable to ReDos, the regex engine in Lucene can take long time and high CPU usage before determining the total count for the states of a regex.",
					"severity": "high",
					"packageName": "org.apache.lucene_lucene-core",
					"packageVersion": "4.6.1",
					"link": "https://issues.apache.org/jira/browse/LUCENE-9981",
					"riskFactors": [
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c8.10.0"
					],
					"publishedDate": "2021-10-03T01:30:11-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -657,
					"fixDate": "2021-10-03T01:30:11-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/lucene-core-4.6.1.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-28709",
					"status": "fixed in 10.1.8, 9.0.74, 8.5.88",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "The fix for CVE-2023-24998 was incomplete for Apache Tomcat 11.0.0-M2 to 11.0.0-M4, 10.1.5 to 10.1.7, 9.0.71 to 9.0.73 and 8.5.85 to 8.5.87. If non-default HTTP       connector settings were used such that the maxParameterCountu00a0could be reached using query string parameters and a request was       submitted that supplied exactly maxParameterCount parametersu00a0in the query string, the limit for uploaded request parts could beu00a0bypassed with the potential for a denial of service to occur.     ",
					"severity": "high",
					"packageName": "tomcat-embed-core",
					"packageVersion": "9.0.71",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-28709",
					"riskFactors": [
						"High severity",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c=9.0.73,9",
						"\u003e=9.0.71,9"
					],
					"publishedDate": "2023-05-22T04:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -56,
					"fixDate": "2023-05-26T23:21:35-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/tomcat-embed-core-9.0.71.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-24998",
					"status": "fixed in 1.5",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "Apache Commons FileUpload before 1.5 does not limit the number of request parts to be processed resulting in the possibility of an attacker triggering a DoS with a malicious upload or series of uploads.     Note that, like all of the file upload limits, the           new configuration option (FileUploadBase#setFileCountMax) is not           enabled by default and must be explicitly configured.   ",
					"severity": "high",
					"packageName": "commons-fileupload_commons-fileupload",
					"packageVersion": "1.3.3",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-24998",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c1.5",
						"\u003e=1.0"
					],
					"publishedDate": "2023-02-20T08:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -150,
					"fixDate": "2023-02-21T19:56:47-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/commons-fileupload-1.3.3.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20860",
					"status": "fixed in 6.0.7, 5.3.26",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N",
					"description": "Spring Framework running version 6.0.0 - 6.0.6 or 5.3.0 - 5.3.25 using \\\"**\\\" as a pattern in Spring Security configuration with the mvcRequestMatcher creates a mismatch in pattern matching between Spring Security and Spring MVC, and the potential for a security bypass.",
					"severity": "high",
					"packageName": "spring-core",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20860",
					"riskFactors": [
						"Attack vector: network",
						"Has fix",
						"High severity",
						"Recent vulnerability",
						"Attack complexity: low"
					],
					"impactedVersions": [
						"\u003c5.3.26,5",
						"\u003e=5.3.0,5"
					],
					"publishedDate": "2023-03-27T15:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -110,
					"fixDate": "2023-04-03T13:50:35-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-core-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20860",
					"status": "fixed in 6.0.7, 5.3.26",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N",
					"description": "Spring Framework running version 6.0.0 - 6.0.6 or 5.3.0 - 5.3.25 using \\\"**\\\" as a pattern in Spring Security configuration with the mvcRequestMatcher creates a mismatch in pattern matching between Spring Security and Spring MVC, and the potential for a security bypass.",
					"severity": "high",
					"packageName": "spring-web",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20860",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"Has fix",
						"High severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c5.3.26,5",
						"\u003e=5.3.0,5"
					],
					"publishedDate": "2023-03-27T15:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -110,
					"fixDate": "2023-04-03T13:50:35-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-web-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-41966",
					"status": "fixed in 1.4.20",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "XStream serializes Java objects to XML and back again. Versions prior to 1.4.20 may allow a remote attacker to terminate the application with a stack overflow error, resulting in a denial of service only via manipulation the processed input stream. The attack uses the hash code implementation for collections and maps to force recursive hash calculation causing a stack overflow. This issue is patched in version 1.4.20 which handles the stack overflow and raises an InputManipulationException instead. A potential workaround for users who only use HashMap or HashSet and whose XML refers these only as default map or set, is to change the default implementation of java.util.Map and java.util per the code example in the referenced advisory. However, this implies that your application does not care about the implementation of the map and all elements are comparable.",
					"severity": "high",
					"packageName": "com.thoughtworks.xstream_xstream",
					"packageVersion": "1.4.18",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-41966",
					"riskFactors": [
						"DoS - High",
						"Has fix",
						"High severity",
						"Attack complexity: low",
						"Attack vector: network"
					],
					"impactedVersions": [
						"\u003c1.4.20"
					],
					"publishedDate": "2022-12-27T16:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -205,
					"fixDate": "2022-12-28T20:48:57-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/xstream-1.4.18.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-40152",
					"status": "fixed in 1.4.20",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "Those using Woodstox to parse XML data may be vulnerable to Denial of Service attacks (DOS) if DTD support is enabled. If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow. This effect may support a denial of service attack.",
					"severity": "high",
					"packageName": "com.thoughtworks.xstream_xstream",
					"packageVersion": "1.4.18",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-40152",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c=1.4.19"
					],
					"publishedDate": "2022-09-16T03:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -209,
					"fixDate": "2022-12-25T12:52:20-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/xstream-1.4.18.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-40151",
					"status": "fixed in 1.4.20",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "Those using Xstream to seralize XML data may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow. This effect may support a denial of service attack.",
					"severity": "high",
					"packageName": "com.thoughtworks.xstream_xstream",
					"packageVersion": "1.4.18",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-40151",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c=1.4.19"
					],
					"publishedDate": "2022-09-16T03:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -209,
					"fixDate": "2022-12-25T12:52:20-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/xstream-1.4.18.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-34169",
					"status": "fixed in 2.7.3",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N",
					"description": "The Apache Xalan Java XSLT library is vulnerable to an integer truncation issue when processing malicious XSLT stylesheets. This can be used to corrupt Java class files generated by the internal XSLTC compiler and execute arbitrary Java bytecode. Users are recommended to update to version 2.7.3 or later. Note: Java runtimes (such as OpenJDK) include repackaged copies of Xalan.",
					"severity": "high",
					"packageName": "org.apache.xalan_xalan",
					"packageVersion": "2.7.2",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-34169",
					"riskFactors": [
						"High severity",
						"Remote execution",
						"Attack complexity: low",
						"Attack vector: network",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c2.7.3"
					],
					"publishedDate": "2022-07-19T11:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -112,
					"fixDate": "2023-03-31T17:00:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/xalan-2.7.2.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-25857",
					"status": "fixed in 1.31",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "The package org.yaml:snakeyaml from 0 and before 1.31 are vulnerable to Denial of Service (DoS) due missing to nested depth limitation for collections.",
					"severity": "high",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-25857",
					"riskFactors": [
						"Has fix",
						"High severity",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High"
					],
					"impactedVersions": [
						"\u003c1.31"
					],
					"publishedDate": "2022-08-29T22:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -326,
					"fixDate": "2022-08-29T22:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2021-43859",
					"status": "fixed in 1.4.19",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "XStream is an open source java library to serialize objects to XML and back again. Versions prior to 1.4.19 may allow a remote attacker to allocate 100% CPU time on the target system depending on CPU type or parallel execution of such a payload resulting in a denial of service only by manipulating the processed input stream. XStream 1.4.19 monitors and accumulates the time it takes to add elements to collections and throws an exception if a set threshold is exceeded. Users are advised to upgrade as soon as possible. Users unable to upgrade may set the NO_REFERENCE mode to prevent recursion. See GHSA-rmr5-cpv2-vgjf for further details on a workaround if an upgrade is not possible.",
					"severity": "high",
					"packageName": "com.thoughtworks.xstream_xstream",
					"packageVersion": "1.4.18",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2021-43859",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c1.4.19"
					],
					"publishedDate": "2022-02-01T04:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -536,
					"fixDate": "2022-02-01T04:15:00-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/xstream-1.4.18.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2021-40690",
					"status": "fixed in 2.2.3, 2.1.7",
					"cvss": 7.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
					"description": "All versions of Apache Santuario - XML Security for Java prior to 2.2.3 and 2.1.7 are vulnerable to an issue where the \\\"secureValidation\\\" property is not passed correctly when creating a KeyInfo from a KeyInfoReference element. This allows an attacker to abuse an XPath Transform to extract any local .xml files in a RetrievalMethod element.",
					"severity": "high",
					"packageName": "org.apache.santuario_xmlsec",
					"packageVersion": "1.5.8",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2021-40690",
					"riskFactors": [
						"Attack vector: network",
						"Has fix",
						"High severity",
						"Attack complexity: low"
					],
					"impactedVersions": [
						"\u003c2.1.7"
					],
					"publishedDate": "2021-09-19T11:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -670,
					"fixDate": "2021-09-20T16:18:41-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/xmlsec-1.5.8.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-2976",
					"status": "fixed in 32.0.0",
					"cvss": 7.1,
					"vector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N",
					"description": "Use of Java\\'s default temporary directory for file creation in `FileBackedOutputStream` in Google Guava versions 1.0 to 31.1 on Unix systems and Android Ice Cream Sandwich allows other users and apps on the machine with access to the default Java temporary directory to be able to access the files created by the class.  Even though the security vulnerability is fixed in version 32.0.0, we recommend using version 32.0.1 as version 32.0.0 breaks some functionality under Windows.  ",
					"severity": "high",
					"packageName": "com.google.guava_guava",
					"packageVersion": "13.0.1",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-2976",
					"riskFactors": [
						"Attack complexity: low",
						"Has fix",
						"High severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c32.0.0"
					],
					"publishedDate": "2023-06-14T11:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -38,
					"fixDate": "2023-06-14T16:12:39-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/guava-13.0.1.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20883",
					"status": "fixed in 2.5.15, 2.6.15, 2.7.12, 3.0.7",
					"cvss": 7,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "In Spring Boot versions 3.0.0 - 3.0.6, 2.7.0 - 2.7.11, 2.6.0 - 2.6.14, 2.5.0 - 2.5.14 and older unsupported versions, there is potential for a denial-of-service (DoS) attack if Spring MVC is used together with a reverse proxy cache.",
					"severity": "high",
					"packageName": "spring-boot-autoconfigure",
					"packageVersion": "2.7.8",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20883",
					"riskFactors": [
						"High severity",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix"
					],
					"impactedVersions": [
						"\u003e=2.7.0",
						"\u003c2.7.12"
					],
					"publishedDate": "2023-05-26T11:30:21-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -56,
					"fixDate": "2023-05-26T19:47:01-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-boot-autoconfigure-2.7.8.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-45688",
					"status": "fixed in 20230227",
					"cvss": 7,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "A stack overflow in the XML.toJSONObject component of hutool-json v5.8.10 allows attackers to cause a Denial of Service (DoS) via crafted JSON or XML data.",
					"severity": "high",
					"packageName": "org.json_json",
					"packageVersion": "20190722",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-45688",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c20230227"
					],
					"publishedDate": "2022-12-13T07:30:26-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -99,
					"fixDate": "2023-04-14T13:39:24-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/json-20190722.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-23457",
					"status": "fixed in 2.3.0.0",
					"cvss": 7,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "ESAPI (The OWASP Enterprise Security API) is a free, open source, web application security control library. Prior to version 2.3.0.0, the default implementation of `Validator.getValidDirectoryPath(String, String, File, boolean)` may incorrectly treat the tested input string as a child of the specified parent directory. This potentially could allow control-flow bypass checks to be defeated if an attack can specify the entire string representing the \\'input\\' path. This vulnerability is patched in release 2.3.0.0 of ESAPI. As a workaround, it is possible to write one\\'s own implementation of the Validator interface. However, maintainers do not recommend this.",
					"severity": "high",
					"packageName": "org.owasp.esapi_esapi",
					"packageVersion": "2.1.0.1",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-23457",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003c=2.2.3.1"
					],
					"publishedDate": "2022-04-27T14:09:43-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -451,
					"fixDate": "2022-04-27T14:09:43-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/esapi-2.1.0.1.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2018-15758",
					"status": "fixed in 2.3.4, 2.2.3, 2.1.3, 2.0.16",
					"cvss": 7,
					"vector": "CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H",
					"description": "Spring Security OAuth, versions 2.3 prior to 2.3.4, and 2.2 prior to 2.2.3, and 2.1 prior to 2.1.3, and 2.0 prior to 2.0.16, and older unsupported versions could be susceptible to a privilege escalation under certain conditions. A malicious user or attacker can craft a request to the approval endpoint that can modify the previously saved authorization request and lead to a privilege escalation on the subsequent approval. This scenario can happen if the application is configured to use a custom approval endpoint that declares AuthorizationRequest as a controller method argument. This vulnerability exposes applications that meet all of the following requirements: Act in the role of an Authorization Server (e.g. @EnableAuthorizationServer) and use a custom Approval Endpoint that declares AuthorizationRequest as a controller method argument. This vulnerability does not expose applications that: Act in the role of an Authorization Server and use the default Approval Endpoint, act in the role of a Resource Server only (e.g. @EnableResourceServer), act in the role of a Client only (e.g. @EnableOAuthClient).",
					"severity": "high",
					"packageName": "org.springframework.security.oauth_spring-security-oauth2",
					"packageVersion": "2.0.8.RELEASE",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2018-15758",
					"riskFactors": [
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"High severity"
					],
					"impactedVersions": [
						"\u003e=2.0.0",
						"\u003c2.0.16"
					],
					"publishedDate": "2018-10-19T15:00:28-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -1737,
					"fixDate": "2018-10-19T15:00:28-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-oauth2-2.0.8.RELEASE.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2016-4977",
					"status": "fixed in 2.0.10",
					"cvss": 7,
					"vector": "CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
					"description": "When processing authorization requests using the whitelabel views in Spring Security OAuth 2.0.0 to 2.0.9 and 1.0.0 to 1.0.5, the response_type parameter value was executed as Spring SpEL which enabled a malicious user to trigger remote code execution via the crafting of the value for response_type.",
					"severity": "high",
					"packageName": "org.springframework.security.oauth_spring-security-oauth2",
					"packageVersion": "2.0.8.RELEASE",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2016-4977",
					"riskFactors": [
						"High severity",
						"Remote execution",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c2.0.10"
					],
					"publishedDate": "2018-10-18T11:06:22-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"graceDays": -1738,
					"fixDate": "2018-10-18T11:06:22-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-oauth2-2.0.8.RELEASE.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-34462",
					"status": "fixed in 4.1.94",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers \u0026 clients. The `SniHandler` can allocate up to 16MB of heap for each channel during the TLS handshake. When the handler or the channel does not have an idle timeout, it can be used to make a TCP server using the `SniHandler` to allocate 16MB of heap. The `SniHandler` class is a handler that waits for the TLS handshake to configure a `SslHandler` according to the indicated server name by the `ClientHello` record. For this matter it allocates a `ByteBuf` using the value defined in the `ClientHello` record. Normally the value of the packet should be smaller than the handshake packet but there are not checks done here and the way the code is written, it is possible to craft a packet that makes the `SslClientHelloHandler`. This vulnerability has been fixed in version 4.1.94.Final.",
					"severity": "medium",
					"packageName": "io.netty_netty-all",
					"packageVersion": "4.1.87.Final",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-34462",
					"riskFactors": [
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network"
					],
					"impactedVersions": [
						"\u003c4.1.94"
					],
					"publishedDate": "2023-06-22T16:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-06-30T13:19:06-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/netty-all-4.1.87.Final.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-34462",
					"status": "fixed in 4.1.94",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers \u0026 clients. The `SniHandler` can allocate up to 16MB of heap for each channel during the TLS handshake. When the handler or the channel does not have an idle timeout, it can be used to make a TCP server using the `SniHandler` to allocate 16MB of heap. The `SniHandler` class is a handler that waits for the TLS handshake to configure a `SslHandler` according to the indicated server name by the `ClientHello` record. For this matter it allocates a `ByteBuf` using the value defined in the `ClientHello` record. Normally the value of the packet should be smaller than the handshake packet but there are not checks done here and the way the code is written, it is possible to craft a packet that makes the `SslClientHelloHandler`. This vulnerability has been fixed in version 4.1.94.Final.",
					"severity": "medium",
					"packageName": "io.netty_netty-codec",
					"packageVersion": "4.1.87.Final",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-34462",
					"riskFactors": [
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Recent vulnerability",
						"Attack complexity: low"
					],
					"impactedVersions": [
						"\u003c4.1.94"
					],
					"publishedDate": "2023-06-22T16:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-06-30T13:19:06-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/netty-codec-4.1.87.Final.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20863",
					"status": "fixed in 6.0.8, 5.3.27, 5.2.24",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "In spring framework versions prior to 5.2.24 release+ ,5.3.27+ and 6.0.8+ , it is possible for a user to provide a specially crafted SpEL expression that may cause a denial-of-service (DoS) condition.",
					"severity": "medium",
					"packageName": "spring-web",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20863",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c5.3.27,5.3",
						"\u003e=5.3.0,5.3"
					],
					"publishedDate": "2023-04-13T13:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-04-21T12:44:37-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-web-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20863",
					"status": "fixed in 6.0.8, 5.3.27, 5.2.24",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "In spring framework versions prior to 5.2.24 release+ ,5.3.27+ and 6.0.8+ , it is possible for a user to provide a specially crafted SpEL expression that may cause a denial-of-service (DoS) condition.",
					"severity": "medium",
					"packageName": "spring-core",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20863",
					"riskFactors": [
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Recent vulnerability",
						"Attack complexity: low"
					],
					"impactedVersions": [
						"\u003c5.3.27,5.3",
						"\u003e=5.3.0,5.3"
					],
					"publishedDate": "2023-04-13T13:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-04-17T13:33:03-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-core-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20861",
					"status": "fixed in 6.0.7, 5.3.26, 5.2.23",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "In Spring Framework versions 6.0.0 - 6.0.6, 5.3.0 - 5.3.25, 5.2.0.RELEASE - 5.2.22.RELEASE, and older unsupported versions, it is possible for a user to provide a specially crafted SpEL expression that may cause a denial-of-service (DoS) condition.",
					"severity": "medium",
					"packageName": "spring-core",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20861",
					"riskFactors": [
						"Medium severity",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - Low",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c=5.3.25,5.3",
						"\u003e=5.3.0,5.3"
					],
					"publishedDate": "2023-03-23T14:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-03-23T18:18:51-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-core-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-20861",
					"status": "fixed in 6.0.7, 5.3.26, 5.2.23",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "In Spring Framework versions 6.0.0 - 6.0.6, 5.3.0 - 5.3.25, 5.2.0.RELEASE - 5.2.22.RELEASE, and older unsupported versions, it is possible for a user to provide a specially crafted SpEL expression that may cause a denial-of-service (DoS) condition.",
					"severity": "medium",
					"packageName": "spring-web",
					"packageVersion": "5.3.25",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-20861",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - Low",
						"Has fix",
						"Medium severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c=5.3.25,5.3",
						"\u003e=5.3.0,5.3"
					],
					"publishedDate": "2023-03-23T14:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-03-28T13:53:33-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-web-5.3.25.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-41854",
					"status": "fixed in 1.32",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H",
					"description": "Those using Snakeyaml to parse untrusted YAML files may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stack overflow. This effect may support a denial of service attack.",
					"severity": "medium",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-41854",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"\u003c1.32"
					],
					"publishedDate": "2022-11-11T05:15:00-08:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2022-11-11T05:15:00-08:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-38752",
					"status": "fixed in 1.32",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "Using snakeYAML to parse untrusted YAML files may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stack-overflow.",
					"severity": "medium",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-38752",
					"riskFactors": [
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Attack complexity: low"
					],
					"impactedVersions": [
						"\u003c1.32"
					],
					"publishedDate": "2022-09-05T03:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2022-09-05T03:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-38751",
					"status": "fixed in 1.31",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "Using snakeYAML to parse untrusted YAML files may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow.",
					"severity": "medium",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-38751",
					"riskFactors": [
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Attack complexity: low"
					],
					"impactedVersions": [
						"\u003c1.31"
					],
					"publishedDate": "2022-09-05T03:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2022-09-05T03:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-38749",
					"status": "fixed in 1.31",
					"cvss": 6.5,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "Using snakeYAML to parse untrusted YAML files may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow.",
					"severity": "medium",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-38749",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"\u003c1.31"
					],
					"publishedDate": "2022-09-05T03:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2022-09-05T03:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2018-10237",
					"status": "fixed in 24.1.1",
					"cvss": 5.9,
					"vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H",
					"description": "Unbounded memory allocation in Google Guava 11.0 through 24.x before 24.1.1 allows remote attackers to conduct denial of service attacks against servers that depend on this library and deserialize attacker-provided data, because the AtomicDoubleArray class (when serialized with Java serialization) and the CompoundOrdering class (when serialized with GWT serialization) perform eager allocation without appropriate checks on what a client has sent and whether the data size is reasonable.",
					"severity": "medium",
					"packageName": "com.google.guava_guava",
					"packageVersion": "13.0.1",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2018-10237",
					"riskFactors": [
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"\u003c24.1.1",
						"\u003e=11.0"
					],
					"publishedDate": "2018-04-26T14:29:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2018-04-26T14:29:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/guava-13.0.1.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-38750",
					"status": "fixed in 1.31",
					"cvss": 5.5,
					"vector": "CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H",
					"description": "Using snakeYAML to parse untrusted YAML files may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow.",
					"severity": "medium",
					"packageName": "org.yaml_snakeyaml",
					"packageVersion": "1.30",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-38750",
					"riskFactors": [
						"Has fix",
						"Medium severity",
						"Attack complexity: low",
						"DoS - High"
					],
					"impactedVersions": [
						"\u003c1.31"
					],
					"publishedDate": "2022-09-05T03:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2022-09-05T03:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/snakeyaml-1.30.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-26049",
					"status": "fixed in 11.0.14, 10.0.14, 9.4.51",
					"cvss": 5.3,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N",
					"description": "Jetty is a java based web server and servlet engine. Nonstandard cookie parsing in Jetty may allow an attacker to smuggle cookies within other cookies, or otherwise perform unintended behavior by tampering with the cookie parsing mechanism. If Jetty sees a cookie VALUE that starts with `\\\"` (double quote), it will continue to read the cookie string until it sees a closing quote -- even if a semicolon is encountered. So, a cookie header such as: `DISPLAY_LANGUAGE=\\\"b; JSESSIONID=1337; c=d\\\"` will be parsed as one cookie, with the name DISPLAY_LANGUAGE and a value of b; JSESSIONID=1337; c=d instead of 3 separate cookies. This has security implications because if, say, JSESSIONID is an HttpOnly cookie, and the DISPLAY_LANGUAGE cookie value is rendered on the page, an attacker can smuggle the JSESSIONID cookie into the DISPLAY_LANGUAGE cookie and thereby exfiltrate it. This is significant when an intermediary is enacting some policy based on cookies, so a smuggled cookie can bypass that policy yet still be seen by the Jetty server or its logging system. This issue has been addressed in versions 9.4.51, 10.0.14, 11.0.14, and 12.0.0.beta0 and users are advised to upgrade. There are no known workarounds for this issue.",
					"severity": "medium",
					"packageName": "org.eclipse.jetty_jetty-io",
					"packageVersion": "9.4.50.v20221201",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-26049",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"Has fix",
						"Medium severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c9.4.51"
					],
					"publishedDate": "2023-04-18T14:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-04-28T16:34:41-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/jetty-io-9.4.50.v20221201.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-26048",
					"status": "fixed in 11.0.14, 10.0.14, 9.4.51",
					"cvss": 5.3,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L",
					"description": "Jetty is a java based web server and servlet engine. In affected versions servlets with multipart support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a part that has a name but no filename and very large content. This happens even with the default settings of `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the whole multipart content is limited (although still read into memory).",
					"severity": "medium",
					"packageName": "org.eclipse.jetty_jetty-io",
					"packageVersion": "9.4.50.v20221201",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-26048",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - Low",
						"Has fix",
						"Medium severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c9.4.51"
					],
					"publishedDate": "2023-04-18T14:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-04-28T16:34:41-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/jetty-io-9.4.50.v20221201.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2021-29425",
					"status": "fixed in 2.7",
					"cvss": 4.8,
					"vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N",
					"description": "In Apache Commons IO before 2.7, When invoking the method FileNameUtils.normalize with an improper input string, like \\\"//../foo\\\", or \\\"\\\\..\\\\foo\\\", the result would be the same value, thus possibly providing access to files in the parent directory, but not further above (thus \\\"limited\\\" path traversal), if the calling code would use the result to construct a path value.",
					"severity": "medium",
					"packageName": "commons-io_commons-io",
					"packageVersion": "2.5",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2021-29425",
					"riskFactors": [
						"Attack vector: network",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"==2.5"
					],
					"publishedDate": "2021-04-13T00:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2021-04-13T00:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/velocity-engine-core-2.0.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2021-29425",
					"status": "fixed in 2.7",
					"cvss": 4.8,
					"vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N",
					"description": "In Apache Commons IO before 2.7, When invoking the method FileNameUtils.normalize with an improper input string, like \\\"//../foo\\\", or \\\"\\\\..\\\\foo\\\", the result would be the same value, thus possibly providing access to files in the parent directory, but not further above (thus \\\"limited\\\" path traversal), if the calling code would use the result to construct a path value.",
					"severity": "medium",
					"packageName": "commons-io_commons-io",
					"packageVersion": "2.2",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2021-29425",
					"riskFactors": [
						"Attack vector: network",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"==2.2"
					],
					"publishedDate": "2021-04-13T00:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2021-04-13T00:15:00-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/commons-io-2.2.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-28708",
					"status": "fixed in 10.1.6, 9.0.72, 8.5.86",
					"cvss": 4.3,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N",
					"description": "When using the RemoteIpFilter with requests received from a reverse proxy via HTTP that include the X-Forwarded-Proto header set to https, session cookies created by Apache Tomcat 11.0.0-M1 to 11.0.0.-M2, 10.1.0-M1 to 10.1.5, 9.0.0-M1 to 9.0.71 and 8.5.0 to 8.5.85 did not include the secure attribute. This could result in the user agent transmitting the session cookie over an insecure channel.",
					"severity": "medium",
					"packageName": "tomcat-embed-core",
					"packageVersion": "9.0.71",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-28708",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"Has fix",
						"Medium severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c9.0.72,9",
						"\u003e9.0.0,9"
					],
					"publishedDate": "2023-03-22T04:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-03-27T09:59:23-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/tomcat-embed-core-9.0.71.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-34462",
					"status": "fixed in 4.1.94.Final",
					"cvss": 4,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H",
					"description": "Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers \u0026 clients. The `SniHandler` can allocate up to 16MB of heap for each channel during the TLS handshake. When the handler or the channel does not have an idle timeout, it can be used to make a TCP server using the `SniHandler` to allocate 16MB of heap. The `SniHandler` class is a handler that waits for the TLS handshake to configure a `SslHandler` according to the indicated server name by the `ClientHello` record. For this matter it allocates a `ByteBuf` using the value defined in the `ClientHello` record. Normally the value of the packet should be smaller than the handshake packet but there are not checks done here and the way the code is written, it is possible to craft a packet that makes the `SslClientHelloHandler`. This vulnerability has been fixed in version 4.1.94.Final.",
					"severity": "moderate",
					"packageName": "io.netty_netty-handler",
					"packageVersion": "4.1.87.Final",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-34462",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - High",
						"Has fix",
						"Medium severity",
						"Recent vulnerability"
					],
					"impactedVersions": [
						"\u003c4.1.94.Final"
					],
					"publishedDate": "2023-06-22T16:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-06-20T12:00:33-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/netty-handler-4.1.87.Final.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2023-26048",
					"status": "fixed in 9.4.51.v20230217, 11.0.14, 10.0.14",
					"cvss": 4,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L",
					"description": "Jetty is a java based web server and servlet engine. In affected versions servlets with multipart support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a part that has a name but no filename and very large content. This happens even with the default settings of `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the whole multipart content is limited (although still read into memory).",
					"severity": "moderate",
					"packageName": "org.eclipse.jetty_jetty-server",
					"packageVersion": "9.4.50.v20221201",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2023-26048",
					"riskFactors": [
						"Has fix",
						"Medium severity",
						"Recent vulnerability",
						"Attack complexity: low",
						"Attack vector: network",
						"DoS - Low"
					],
					"impactedVersions": [
						"\u003c9.4.51.v20230217"
					],
					"publishedDate": "2023-04-18T14:15:00-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2023-04-19T12:55:05-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/jetty-server-9.4.50.v20221201.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2022-24891",
					"status": "fixed in 2.3.0.0",
					"cvss": 4,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N",
					"description": "ESAPI (The OWASP Enterprise Security API) is a free, open source, web application security control library. Prior to version 2.3.0.0, there is a potential for a cross-site scripting vulnerability in ESAPI caused by a incorrect regular expression for \\\"onsiteURL\\\" in the **antisamy-esapi.xml** configuration file that can cause \\\"javascript:\\\" URLs to fail to be correctly sanitized. This issue is patched in ESAPI 2.3.0.0. As a workaround, manually edit the **antisamy-esapi.xml** configuration files to change the \\\"onsiteURL\\\" regular expression. More information about remediation of the vulnerability, including the workaround, is available in the maintainers\\' release notes and security bulletin.",
					"severity": "moderate",
					"packageName": "org.owasp.esapi_esapi",
					"packageVersion": "2.1.0.1",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2022-24891",
					"riskFactors": [
						"Attack complexity: low",
						"Attack vector: network",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"\u003c=2.2.3.1"
					],
					"publishedDate": "2022-04-27T14:09:46-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2022-04-27T14:09:46-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/esapi-2.1.0.1.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2020-15522",
					"status": "fixed in 1.66",
					"cvss": 4,
					"vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
					"description": "Bouncy Castle BC Java before 1.66, BC C# .NET before 1.8.7, BC-FJA before 1.0.1.2, 1.0.2.1, and BC-FNA before 1.0.1.1 have a timing issue within the EC math library that can expose information about the private key when an attacker is able to observe timing information for the generation of multiple deterministic ECDSA signatures.",
					"severity": "moderate",
					"packageName": "org.bouncycastle_bcprov-ext-jdk15on",
					"packageVersion": "1.60",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2020-15522",
					"riskFactors": [
						"Attack vector: network",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"\u003c1.66"
					],
					"publishedDate": "2021-08-13T08:22:31-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2021-08-13T08:22:31-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/bcprov-ext-jdk15on-1.60.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2020-15522",
					"status": "fixed in 1.66",
					"cvss": 4,
					"vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
					"description": "Bouncy Castle BC Java before 1.66, BC C# .NET before 1.8.7, BC-FJA before 1.0.1.2, 1.0.2.1, and BC-FNA before 1.0.1.1 have a timing issue within the EC math library that can expose information about the private key when an attacker is able to observe timing information for the generation of multiple deterministic ECDSA signatures.",
					"severity": "moderate",
					"packageName": "org.bouncycastle_bcprov-jdk15on",
					"packageVersion": "1.60",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2020-15522",
					"riskFactors": [
						"Attack vector: network",
						"Has fix",
						"Medium severity"
					],
					"impactedVersions": [
						"\u003c1.66"
					],
					"publishedDate": "2021-08-13T08:22:31-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2021-08-13T08:22:31-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/bcprov-jdk15on-1.60.jar",
					"layerInstruction": "USER 500"
				},
				{
					"id": "CVE-2019-3778",
					"status": "fixed in 2.3.5.RELEASE, 2.2.4.RELEASE, 2.1.4.RELEASE, 2.0.17.RELEASE",
					"cvss": 4,
					"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N",
					"description": "Spring Security OAuth, versions 2.3 prior to 2.3.5, and 2.2 prior to 2.2.4, and 2.1 prior to 2.1.4, and 2.0 prior to 2.0.17, and older unsupported versions could be susceptible to an open redirector attack that can leak an authorization code. A malicious user or attacker can craft a request to the authorization endpoint using the authorization code grant type, and specify a manipulated redirection URI via the \\\"redirect_uri\\\" parameter. This can cause the authorization server to redirect the resource owner user-agent to a URI under the control of the attacker with the leaked authorization code. This vulnerability exposes applications that meet all of the following requirements: Act in the role of an Authorization Server (e.g. @EnableAuthorizationServer) and uses the DefaultRedirectResolver in the AuthorizationEndpoint. This vulnerability does not expose applications that: Act in the role of an Authorization Server and uses a different RedirectResolver implementation other than DefaultRedirectResolver, act in the role of a Resource Server only (e.g. @EnableResourceServer), act in the role of a Client only (e.g. @EnableOAuthClient).",
					"severity": "moderate",
					"packageName": "org.springframework.security.oauth_spring-security-oauth2",
					"packageVersion": "2.0.8.RELEASE",
					"link": "https://nvd.nist.gov/vuln/detail/CVE-2019-3778",
					"riskFactors": [
						"Medium severity",
						"Attack complexity: low",
						"Attack vector: network",
						"Has fix"
					],
					"impactedVersions": [
						"\u003c2.0.17.RELEASE"
					],
					"publishedDate": "2019-03-14T08:39:30-07:00",
					"discoveredDate": "2023-08-21T08:08:35-07:00",
					"fixDate": "2019-03-14T08:39:30-07:00",
					"layerTime": "2023-08-16T02:33:55-07:00",
					"packagePath": "/opt/genesys/application/gws.jar/spring-security-oauth2-2.0.8.RELEASE.jar",
					"layerInstruction": "USER 500"
				}
			],
			"vulnerabilityDistribution": {
				"critical": 7,
				"high": 20,
				"medium": 23,
				"low": 0,
				"total": 50
			},
			"vulnerabilityScanPassed": false,
			"history": [
				{
					"created": "2023-08-02T09:13:43-07:00",
					"instruction": "ADD file:66850d5e06c92b8217827133037551e15038c13d34d93849bbbae9b267ebfcab in / "
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "RUN mv -f /etc/yum.repos.d/ubi.repo /tmp || :"
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "ADD file:214c1de395c24e4a86ef9a706069ef30a9e804c63f851c37c35655e16fea3ced in /tmp/tls-ca-bundle.pem "
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "ADD multi:dad1054d72a3e8b4c584c001e3dcf03e2e308d6704afa67bdb7e61f11a6faa13 in /etc/yum.repos.d/ "
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL maintainer=\"Red Hat, Inc.\""
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL com.redhat.component=\"ubi8-container\"    ..."
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL com.redhat.license_terms=\"https://www.red..."
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL summary=\"Provides the latest release of R..."
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL description=\"The Universal Base Image is ..."
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL io.k8s.display-name=\"Red Hat Universal Ba..."
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL io.openshift.expose-services=\"\""
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "LABEL io.openshift.tags=\"base rhel8\""
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "ENV container oci"
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
				},
				{
					"created": "2023-08-02T09:13:44-07:00",
					"instruction": "CMD [\"/bin/bash\"]"
				},
				{
					"created": "2023-08-02T09:13:45-07:00",
					"instruction": "RUN rm -rf /var/log/*"
				},
				{
					"created": "2023-08-02T09:13:46-07:00",
					"instruction": "RUN mkdir -p /var/log/rhsm"
				},
				{
					"created": "2023-08-02T09:13:46-07:00",
					"instruction": "LABEL release=1032"
				},
				{
					"created": "2023-08-02T09:13:46-07:00",
					"instruction": "ADD file:4eb2d82a9268a2eceef36401799108b9d67f1aaef5a81e0ea744b7f736a98596 in /root/buildinfo/content_manifests/ubi8-container-8.8-1032.json "
				},
				{
					"created": "2023-08-02T09:13:46-07:00",
					"instruction": "ADD file:f9f7ba78e28f98ff3613c1dd6e098c454103de4a37a63fc4d55862f10312d4fa in /root/buildinfo/Dockerfile-ubi8-8.8-1032 "
				},
				{
					"created": "2023-08-02T09:13:46-07:00",
					"instruction": "LABEL \"distribution-scope\"=\"public\" \"vendor\"=\"R..."
				},
				{
					"created": "2023-08-02T09:13:47-07:00",
					"instruction": "RUN rm -f '/etc/yum.repos.d/repo-cdf2d.repo' '/etc/yum.repos.d/repo-a0366.repo'"
				},
				{
					"created": "2023-08-02T09:13:48-07:00",
					"instruction": "RUN rm -f /tmp/tls-ca-bundle.pem"
				},
				{
					"created": "2023-08-02T09:13:50-07:00",
					"instruction": "RUN mv -fZ /tmp/ubi.repo /etc/yum.repos.d/ubi.repo || :"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "ARG EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "ARG BUILD_TAG=595 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "LABEL com.genesysengage.external.image-from=\"${..."
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "USER root"
				},
				{
					"created": "2023-08-14T00:05:08-07:00",
					"instruction": "WORKDIR /"
				},
				{
					"created": "2023-08-14T00:05:52-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c set -ex \u0026\u0026     dnf -y --setopt=tsflags=nodocs --nodocs update \u0026\u0026     dnf reinstall -y --setopt=tsflags=nodocs --nodocs langpacks-en"
				},
				{
					"created": "2023-08-14T00:05:53-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c set -ex \u0026\u0026     cp /etc/locale.conf /etc/locale.conf.c-utf8 \u0026\u0026     sed -i 's/^LANG=.*/LANG=\"en_US.UTF-8\"/' /etc/locale.conf"
				},
				{
					"created": "2023-08-14T00:06:22-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c set -ex \u0026\u0026     INSTALL_PKGS=\"fipscheck fontconfig langpacks-en langpacks-ar langpacks-zh_CN langpacks-cs langpacks-nl langpacks-fr langpacks-de langpacks-it langpacks-ja langpacks-ko langpacks-pl langpacks-pt_BR langpacks-ru langpacks-es langpacks-tr glibc-all-langpacks libgcc libgcrypt nss nss-softokn nss-tools openssl openssl-pkcs11 openssl-devel shadow-utils make curl which tar gzip krb5-libs krb5-workstation\" \u0026\u0026     dnf --setopt=tsflags=nodocs --nodocs install -y $INSTALL_PKGS \u0026\u0026     rpm -V $INSTALL_PKGS \u0026\u0026     dnf clean all 2\u003e/dev/null || true \u0026\u0026     rm -rf /var/cache/yum 2\u003e/dev/null || true \u0026\u0026     sed -i 's/enabled=1/enabled=0/g' /etc/yum/pluginconf.d/subscription-manager.conf \u0026\u0026     subscription-manager unregister 2\u003e/dev/null || true \u0026\u0026     subscription-manager repo-override --remove-all 2\u003e/dev/null || true \u0026\u0026     rm -f /etc/yum.repos.d/redhat.repo 2\u003e/dev/null || true"
				},
				{
					"created": "2023-08-14T00:06:23-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c set -ex \u0026\u0026     locale -a"
				},
				{
					"created": "2023-08-14T00:06:23-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c set -ex     \u0026\u0026 openssl version | grep \"FIPS\"     \u0026\u0026 ln -f -s /etc/pki/tls/openssl.cnf /etc/ssl/openssl.cnf"
				},
				{
					"created": "2023-08-14T00:06:24-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c set -ex     \u0026\u0026 groupadd --system --gid 500 genesys     \u0026\u0026 useradd --system --uid 500 --gid genesys --shell /bin/bash --create-home genesys     \u0026\u0026 chown -R 500:0 /home/genesys     \u0026\u0026 chmod -R ug+rwx /home/genesys"
				},
				{
					"created": "2023-08-14T00:06:25-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 EXT_FROM=registry.access.redhat.com/ubi8/ubi@sha256:64cee7b543ac539d0a45a59f607b5248f2a332038c1214ac920b9d7bf6708f61 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 /bin/sh -c find / -user root -perm -6000 -type f -exec chmod a-s {} \\; 2\u003e/dev/null || true"
				},
				{
					"created": "2023-08-14T00:06:25-07:00",
					"instruction": "USER 500"
				},
				{
					"created": "2023-08-14T00:06:25-07:00",
					"instruction": "WORKDIR /home/genesys"
				},
				{
					"created": "2023-08-14T00:06:25-07:00",
					"instruction": "USER root"
				},
				{
					"created": "2023-08-14T00:06:30-07:00",
					"instruction": "CMD [\"/bin/bash\"]"
				},
				{
					"created": "2023-08-14T00:50:56-07:00",
					"instruction": "ARG BUILD_TAG=595"
				},
				{
					"created": "2023-08-14T00:50:56-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00"
				},
				{
					"created": "2023-08-14T00:50:56-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871"
				},
				{
					"created": "2023-08-14T00:50:56-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595"
				},
				{
					"created": "2023-08-14T00:50:57-07:00",
					"instruction": "ARG BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 JAVA_VERSION=17"
				},
				{
					"created": "2023-08-14T00:50:57-07:00",
					"instruction": "LABEL com.genesysengage.openjdk.image-name=\"bas..."
				},
				{
					"created": "2023-08-14T00:50:57-07:00",
					"instruction": "USER root"
				},
				{
					"created": "2023-08-14T00:51:15-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 JAVA_VERSION=17 /bin/sh -c set -ex \u0026\u0026     INSTALL_PKGS=\"java-17-openjdk-headless java-17-openjdk-devel\" \u0026\u0026     yum install -y --setopt=install_weak_deps=0 --setopt=tsflags=nodocs --nodocs $INSTALL_PKGS \u0026\u0026     rpm -V $INSTALL_PKGS \u0026\u0026     yum -y clean all --enablerepo='*' \u0026\u0026     subscription-manager unregister 2\u003e/dev/null || true \u0026\u0026     subscription-manager repo-override --remove-all 2\u003e/dev/null || true \u0026\u0026     rm -f /etc/yum.repos.d/redhat.repo 2\u003e/dev/null || true \u0026\u0026     mkdir -p -m 755 /etc/.java/deployment 2\u003e/dev/null || true \u0026\u0026     java -version"
				},
				{
					"created": "2023-08-14T00:51:15-07:00",
					"instruction": "ENV JAVA_HOME /etc/alternatives/jre"
				},
				{
					"created": "2023-08-14T00:51:16-07:00",
					"instruction": "COPY file:f3296a8ec55312f7b97586cd579087772e62f8dbc25855750659f0cbcb0f1c4f in /etc/.java/deployment/ "
				},
				{
					"created": "2023-08-14T00:51:16-07:00",
					"instruction": "COPY file:fb5240f3a15d8ba1494a08bbf689fb410dfaa10eaffc3aab361b897a7b7b0257 in /etc/.java/deployment/ "
				},
				{
					"created": "2023-08-14T00:51:16-07:00",
					"instruction": "COPY file:82f2bb3aae9fb523d3e9bf6d23af3eb392aa3c3d4f024327b5c7c334fa29a739 in /etc/.java/deployment/ "
				},
				{
					"created": "2023-08-14T00:51:17-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 JAVA_VERSION=17 /bin/sh -c set -ex     \u0026\u0026 chmod 644 /etc/.java/deployment/*     \u0026\u0026 cd /usr/lib/jvm/jre/conf/security/     \u0026\u0026 cp java.security java.security.orig     \u0026\u0026 cp java.security java.security.stig"
				},
				{
					"created": "2023-08-14T00:51:17-07:00",
					"instruction": "COPY file:42159f251f960021683fc0df79a04516b999ae0b9d19ac96576275c8dfaca02f in /etc/genesys/ "
				},
				{
					"created": "2023-08-14T00:51:17-07:00",
					"instruction": "COPY file:aad185d052e96e5ad59243401b4a0cd6d04254e44ba29e8945a0e0ec7a1cc366 in /home/genesys "
				},
				{
					"created": "2023-08-14T00:51:18-07:00",
					"instruction": "COPY file:ab9864eba2a5292982812b7faf1c16d5fd7d6838680872ef68b40efea75d9267 in /home/genesys "
				},
				{
					"created": "2023-08-14T00:51:18-07:00",
					"instruction": "COPY file:e6d1fe8f7a997a16498da67289ceeff9f5664ab0498fc76dcb5195eb3529ea04 in /etc/genesys/ "
				},
				{
					"created": "2023-08-14T00:51:18-07:00",
					"instruction": "COPY file:08d512d901d9a4b765f414aeb10c2f81b4374fd7d96012e2926e07db8fd67f61 in /home/genesys "
				},
				{
					"created": "2023-08-14T00:51:18-07:00",
					"instruction": "USER 500"
				},
				{
					"created": "2023-08-14T00:51:19-07:00",
					"instruction": "WORKDIR /home/genesys"
				},
				{
					"created": "2023-08-14T00:51:19-07:00",
					"instruction": "ENV JAVA_HOME /etc/alternatives/jre"
				},
				{
					"created": "2023-08-14T00:51:19-07:00",
					"instruction": "USER root"
				},
				{
					"created": "2023-08-14T00:51:26-07:00",
					"instruction": "RUN |5 BUILD_TAG=595 BUILD_TIME=2023-08-14T00:02-07:00 GIT_COMMIT=891746e21a90849cd7b8c2cd2dcff24747a27871 IMAGE_VERSION=100.0.088.0595 JAVA_VERSION=17 /bin/sh -c chown -R 500:0 /home/genesys     \u0026\u0026 chmod -R ug+rwx /home/genesys"
				},
				{
					"created": "2023-08-16T02:33:49-07:00",
					"instruction": "ARG _project_name"
				},
				{
					"created": "2023-08-16T02:33:49-07:00",
					"instruction": "ARG _project_name _project_version"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "ARG _project_name _project_version _user"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "ENTRYPOINT [     \"java\",     \"-Dfile.encoding=UTF-8\",     \"-Djavax.net.ssl.keyStore=NONE\",     \"-XX:+ExitOnOutOfMemoryError\" ]"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "USER genesys"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "WORKDIR /opt/genesys/application"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "EXPOSE 8080"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "CMD [\"-jar\", \"gws.jar\"]"
				},
				{
					"created": "2023-08-16T02:33:50-07:00",
					"instruction": "ENV GWS_SERVICE_NAME=${_project_name}     GWS_SERVICE_VERSION=${_project_version}     GWS_JAVA_OPTIONS_HEAPSIZE=\"-Xms6g -Xmx6g\"     GWS_JAVA_OPTIONS_COMMON=\"-Dfile.encoding=UTF-8 -XX:+ExitOnOutOfMemoryError -XX:+UseG1GC -XX:+PrintFlagsFinal\""
				},
				{
					"created": "2023-08-16T02:33:51-07:00",
					"instruction": "COPY file:983d177c13f079563d17bb5c8c71f4f50a77d9cb95fb52d45eef6c37eb197e4e in ./ "
				},
				{
					"created": "2023-08-16T02:33:51-07:00",
					"instruction": "USER root"
				},
				{
					"created": "2023-08-16T02:33:51-07:00",
					"instruction": "RUN |3 _project_name=gws-api-v2 _project_version=8.6.000.00-0007 _user=500 /bin/sh -c chown -R 500:0 /opt/genesys/application \u0026\u0026     chmod -R ug+rw /opt/genesys/application"
				},
				{
					"created": "2023-08-16T02:33:55-07:00",
					"instruction": "USER 500"
				}
			],
			"scanTime": "2023-08-21T15:08:38.655559555Z",
			"scanID": "64e37df67f60bf7d4825c5d6"
		}
	],
	"consoleURL": "https://app3.prismacloud.io/compute?computeState=/monitor/vulnerabilities/images/ci?search=sha256%3Abd08b0c17e93272cda54d566f0597f5d4196c52f95ad5e3b49d2be31c7d11dd2"
}
'''


# Parse JSON data
data = json.loads(json_data)

# Extract the packages list
packages = data["results"][0]["packages"]

# Generate HTML table
table_html = '<table>'
table_html += '<tr><th>Type</th><th>Name</th><th>Version</th><th>Licenses</th></tr>'
for package in packages:
    table_html += f'''
    <tr>
        <td>{package["type"]}</td>
        <td>{package["name"]}</td>
        <td>{package["version"]}</td>
        <td>{", ".join(package["licenses"])}</td>
    </tr>
'''
table_html += '</table>'

# Save HTML to a file
with open('table.html', 'w', encoding='utf-8') as html_file:
    html_file.write(table_html)

print("HTML table generated and saved to table.html")
