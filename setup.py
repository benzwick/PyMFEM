"""
  MFEM + PyMFEM (finite element method library)
"""
import sys
import os
import urllib
import gzip
import re
import shutil
import subprocess
from subprocess import DEVNULL 

import multiprocessing

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.install import install as _install
try:
    from setuptools._distutils.command.clean import clean as _clean
except ImportError:
    from distutils.command.clean import clean as _clean

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    haveWheel = True
except ImportError:
    haveWheel = False    

# To use a consistent encoding
# from codecs import open

### constants
repos = {"mfem": "https://github.com/mfem/mfem/archive/v4.2.tar.gz",
         "metis": "http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz",
         "hypre": "https://github.com/hypre-space/hypre/archive/v2.20.0.tar.gz",}

rootdir = os.path.abspath(os.path.dirname(__file__))
extdir = os.path.join(rootdir, 'external')

from sys import platform
if platform == "linux" or platform == "linux2":
    dylibext = '.so'
elif platform == "darwin":
    # OS X
    dylibext = '.dylib'
elif platform == "win32":
    # Windows...
    assert False, "Windows is not supported yet. Contribution is welcome"


### global variables
is_configured = False
prefix = ''

verbose = -1
swig_only = False
run_swig = False
clean_swig = False
build_mfem = True
build_mfemp = False
build_metis = False
build_hypre = False
build_parallel = False
build_serial = False
mfems_prefix = ''
mfemp_prefix = ''
metis_prefix = ''
hypre_prefix = ''

enable_cuda = False
cuda_prefix = ''
enable_pumi = False
pumi_prefix = ''
enable_strumpack = False
strumpack_prefix = ''

dry_run = -1

cc_command = 'cc' if os.getenv("CC") is None else os.getenv("CC")
cxx_command = 'c++' if os.getenv("CC") is None else os.getenv("CXX")
mpicc_command = 'mpicc' if os.getenv("MPICC") is None else os.getenv("MPICC")
mpicxx_command = 'mpic++' if os.getenv("MPICXX") is None else os.getenv("MPICXX")
cxx11_flag = '-std=c++11'

### meta data
def version():
    VERSIONFILE = os.path.join('mfem', '__init__.py')
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))

def long_description():
    with open(os.path.join(rootdir, 'README.md'), encoding='utf-8') as f:
        return f.read()

keywords = """
scientific computing
finite element method
"""

platforms = """
Mac OS X
Linux
"""
metadata = {'name'             : 'mfem', 
            'version'          : version(),
            'description'      : __doc__.strip(),
            'long_description' : long_description(),
            'long_description_content_type':"text/markdown",
            'url'              : 'http://mfem.org',
            'download_url'     : 'https://github.com/mfem',
            'classifiers'      :['Development Status :: 4 - Beta',
                                 'Intended Audience :: Developers',
                                 'Topic :: Scientific/Engineering :: Physics',
                                 'License :: OSI Approved :: BSD License',
                                 'Programming Language :: Python :: 3.6',  ],
            'keywords'         : [k for k in keywords.split('\n')    if k],
            'platforms'        : [p for p in platforms.split('\n')   if p],
            'license'          : 'BSD-3',
            'author'           : 'MFEM developement team',
            'author_email'     : '',
            'maintainer'       : 'S. Shiraiwa',
            'maintainer_email' : 'shiraiwa@princeton.edu',}

##  utilities
def abspath(path):
    return os.path.abspath(os.path.expanduser(path))

def find_command(name):
    from shutil import which
    return which(name)

def make_call(command, target=''):
    '''
    call command
    '''
    if dry_run or verbose:
        print("calling ... " + " ".join(command))
    if dry_run:        
        return
    kwargs = {}
    if not verbose:
        kwargs['stdout'] = DEVNULL
        kwargs['stderr'] = DEVNULL
    try:
        subprocess.check_call(command, **kwargs)
    except subprocess.CalledProcessError:
        if target == '':
            target = " ".join(command)
        print("Failed when calling command: " + target)
        raise

def chdir(path):
    '''
    change directory
    '''
    pwd = os.getcwd()
    os.chdir(path)
    if verbose:
        print("Moving to a directory : " + path)
    return pwd

def remove_files(files):
    for f in files:
        if verbose:
            print("Removing : " + f)
        if dry_run:
            continue
        os.remove(f)
    
def make(target):
    '''
    make : add -j option automatically
    '''
    command = ['make', '-j', str(max((multiprocessing.cpu_count()-1, 1)))]
    make_call(command, target=target) 

def make_install(target):
    '''
    make install
    '''
    command = ['make', 'install']
    make_call(command, target=target)

def download(xxx):
    '''
    download tar.gz from somewhere. xxx is name.
    url is given by repos above
    '''
    from urllib import request
    import tarfile

    if os.path.exists(os.path.join(extdir, xxx)):
        print("Download " + xxx + " skipped. Use clean --all-exts if needed")
        return
    url = repos[xxx]
    print("Downloading :", url)
    
    ftpstream = request.urlopen(url)
    targz = tarfile.open(fileobj=ftpstream, mode="r|gz")
    targz.extractall(path=extdir)
    os.rename(os.path.join(extdir, targz.getnames()[0].split('/')[0]),
              os.path.join(extdir, xxx))

def cmake(path, **kwargs):
    '''
    run cmake. must be called in the target directory
    '''
    command = ['cmake', path]
    for key, value in kwargs.items():
        command.append('-'+key+'='+value)
    make_call(command)

def cmake_make_hypre():
    '''
    build hypre
    '''
    cmbuild = 'cmbuild'
    path = os.path.join(extdir, 'hypre', 'src', cmbuild)
    if os.path.exists(path):
        print("working directory already exists!")
    else:
        os.makedirs(path)

    pwd = chdir(path)

    cmake_opts = {'DCMAKE_VERBOSE_MAKEFILE':'1',
                  'DBUILD_SHARED_LIBS': '1',
                  'DHYPRE_INSTALL_PREFIX': os.path.join(prefix, 'mfem'),
                  'DHYPRE_ENABLE_SHARED': '1',
                  'DCMAKE_INSTALL_PREFIX':os.path.join(prefix, 'mfem'),
                  'DCMAKE_INSTALL_NAME_DIR':os.path.join(prefix, 'mfem', 'lib'),
                  'DCMAKE_C_COMPILER': mpicc_command} 

    cmake('..', **cmake_opts)

    make('hypre')
    make_install('hypre')

    os.chdir(pwd)

def make_metis(use_int64=False, use_real64=False):
    '''
    build metis 
    '''
    path = os.path.join(extdir, 'metis')
    if not os.path.exists(path):
        assert False, "metis is not downloaded"

    pwd = chdir(path)
    
    sed_command = find_command('sed')
    if sed_command is None:
        assert False, "sed is not foudn"

    if use_int64:
        command = [sed_command, '-i',
                   's/#define IDXTYPEWIDTH 32/#define IDXTYPEWIDTH 64/g',
                   'include/metis.h']
    else:
        command = [sed_command, '-i',
                   's/#define IDXTYPEWIDTH 64/#define IDXTYPEWIDTH 32/g',
                   'include/metis.h']

    if use_real64:
        command = [sed_command, '-i',
                   's/#define REALTYPEWIDTH 32/#define REALTYPEWIDTH 64/g',
                   'include/metis.h']
    else:
        command = [sed_command, '-i',
                   's/#define REALTYPEWIDTH 64/#define REALTYPEWIDTH 32/g',
                   'include/metis.h']
    make_call(command)

    command = ['make', 'config', 'shared=1',
               'prefix='+os.path.join(prefix, 'mfem'),
               'cc='+cc_command]
    make_call(command)
    make('metis')
    make_install('metis')

    if platform == "darwin":
        command = ['install_name_tool',
                   '-id',
                   os.path.join(prefix, 'lib', 'libmetis.dylib'),
                   os.path.join(prefix, 'lib', 'libmetis.dylib'),]
        make_call(command)
    os.chdir(pwd)

def cmake_make_mfem(serial=True):
    '''
    build MFEM 
    '''
    cmbuild = 'cmbuild_ser' if serial else 'cmbuild_par'
    path = os.path.join(extdir, 'mfem', cmbuild)
    if os.path.exists(path):
        print("working directory already exists!")
    else:
        os.makedirs(path)

    cmake_opts = {'DCMAKE_VERBOSE_MAKEFILE':'1',
                  'DBUILD_SHARED_LIBS': '1',
                  'DMFEM_ENABLE_EXAMPLES': '1',
                  'DMFEM_ENABLE_MINIAPPS': '1',
                  'DCMAKE_SHARED_LINKER_FLAGS':'',
                  'DCMAKE_CXX_FLAGS': cxx11_flag}

    if serial:
        cmake_opts['DCMAKE_CXX_COMPILER'] = cxx_command
        cmake_opts['DMFEM_USE_EXCEPTIONS'] = '1'
        cmake_opts['DCMAKE_INSTALL_PREFIX'] = os.path.join(prefix, 'mfem', 'ser')
    else:
        cmake_opts['DCMAKE_CXX_COMPILER'] = mpicxx_command
        cmake_opts['DMFEM_USE_EXCEPTIONS'] = '0'
        cmake_opts['DCMAKE_INSTALL_PREFIX'] = os.path.join(prefix, 'mfem', 'par')
        cmake_opts['DMFEM_USE_MPI'] = '1'
        cmake_opts['DMFEM_USE_METIS_5'] = '1'
        cmake_opts['DHYPRE_DIR'] = os.path.join(hypre_prefix)
        #cmake_opts['DHYPRE_INCLUDE'] = os.path.join(hypre_prefix, 'include')
        cmake_opts['DMETIS_DIR'] = os.path.join(metis_prefix)
        #cmake_opts['DMETIS_INCLUDE'] = os.path.join(metis_prefix, 'include')
        #cmake_opts['DCMAKE_CXX_STANDARD_LIBRARIES'] = "-lHYPRE -lmetis"

        lflags = "-L" + os.path.join(metis_prefix, 'lib')
        lflags = lflags + " -L" + os.path.join(hypre_prefix, 'lib')
        cmake_opts['DCMAKE_SHARED_LINKER_FLAGS'] = lflags
        #cmake_opts['DCMAKE_EXT_LINKER_FLAGS'] = lflags

        if enable_strumpack:
            cmake_opts['DMFEM_USE_STRUMPACK'] = '1'
            cmake_opts['STRUMPACK_DIR'] = strumpack_prefix            
        if enable_pumi:
            cmake_opts['DMFEM_USE_PUMI'] = '1'
            cmake_opts['DPUMI_DIR'] = pumi_prefix
            
    if enable_cuda:
        cmake_opts['DMFEM_USE_CUDA'] = '1'
        
    pwd = chdir(path)
    cmake('..', **cmake_opts)

    txt = 'serial' if serial else 'parallel'
    make('mfem_'+txt)
    make_install('mfem_'+txt)
    
    os.chdir(pwd)

def write_setup_local():
    '''
    create setup_local.py. parameters written here will be read
    by setup.py in mfem._ser and mfem._par
    '''
    import numpy

    if build_mfem:
        mfemser = os.path.join(prefix, 'mfem', 'ser')
        mfempar = os.path.join(prefix, 'mfem', 'par')
    else:
        mfemser = mfems_prefix
        mfempar = mfemp_prefix
    
    params = {'cxx_ser': cxx_command,
              'cc_ser': cc_command,
              'cxx_par': mpicxx_command,
              'cc_par': mpicc_command,
              'whole_archive': '--whole-archive',
              'no_whole_archive': '--no-whole-archive',
              'nocompactunwind': '',
              'swigflag': '-Wall -c++ -python -fastproxy -olddefs -keyword',

              'hypreinc': os.path.join(hypre_prefix, 'include'),
              'hyprelib': os.path.join(hypre_prefix, 'lib'),
              'metisinc': os.path.join(metis_prefix, 'include'),
              'metis5lib': os.path.join(metis_prefix, 'lib'),
              'numpync': numpy.get_include(),
              'mfembuilddir': os.path.join(mfempar, 'include'),
              'mfemincdir': os.path.join(mfempar, 'include', 'mfem'),
              'mfemlnkdir': os.path.join(mfempar, 'lib'),
              'mfemserbuilddir': os.path.join(mfemser, 'include'),
              'mfemserincdir': os.path.join(mfemser, 'include', 'mfem'),
              'mfemserlnkdir': os.path.join(mfemser, 'lib'),
              'add_pumi': '',
              'add_strumpack': '',
              'add_cuda': '',              
              'cxx11flag': cxx11_flag,
              }


    try:
        import mpi4py ## avaialbility of this is checked before
        params['mpi4pyinc'] = mpi4py.get_include()
    except ImportError:
        params['mpi4pyinc'] = ''

    def add_extra(xxx):
        params['add_' + xxx] = '1'
        params[xxx + 'inc'] = os.path.join(globals()[xxx + '_prefix'], 'include')
        params[xxx + 'lib'] = os.path.join(globals()[xxx + '_prefix'], 'lib')

    if enable_pumi:
        add_extra('pumi')
    if enable_strumpack:
        add_extra('strumpack')
    if enable_cuda:
        add_extra('cuda')


    pwd = chdir(rootdir)
    
    fid = open('setup_local.py', 'w')
    fid.write("#  setup_local.py \n")
    fid.write("#  generated from setup.py\n")
    fid.write("#  do not edit this directly\n")

    for key, value in params.items():
        text = key.lower() + ' = "' + value + '"'
        fid.write(text+"\n")
    fid.close()
    
    os.chdir(pwd)

def generate_wrapper():
    '''
    run swig.
    '''
    if dry_run or verbose:
        print("generating SWIG wrapper")
    def ifiles():
        ifiles = os.listdir()
        ifiles = [x for x in ifiles if x.endswith('.i')]
        ifiles = [x for x in ifiles if not x.startswith('#')]
        ifiles = [x for x in ifiles if not x.startswith('.')]                
        return ifiles

    def check_new(ifile):
        wfile = ifile[:-2]+'_wrap.cxx'
        if not os.path.exists(wfile):
            return True
        return os.path.getmtime(ifile) > os.path.getmtime(wfile)

    if build_mfem:
        mfemser = os.path.join(prefix, 'mfem', 'ser')
        mfempar = os.path.join(prefix, 'mfem', 'par')
    else:
        mfemser = mfems_prefix
        mfempar = mfemp_prefix

    swig_command = find_command('swig')
    if swig_command is None:
        assert False, "SWIG is not installed"

    swigflag = '-Wall -c++ -python -fastproxy -olddefs -keyword'.split(' ')

    pwd = chdir(os.path.join(rootdir, 'mfem', '_ser'))

    serflag = ['-I'+ os.path.join(mfemser, 'include'),
               '-I'+ os.path.join(mfemser, 'include', 'mfem')]
    for file in ifiles():
        if not check_new(file):
            continue
        command = [swig_command] + swigflag + serflag + [file]
        make_call(command)

    if not build_parallel:
        os.chdir(pwd)
        return

    chdir(os.path.join(rootdir, 'mfem', '_par'))

    import mpi4py
    parflag = ['-I'+ os.path.join(mfempar, 'include'),
               '-I'+ os.path.join(mfempar, 'include', 'mfem'),
               '-I'+ mpi4py.get_include()]

    if enable_pumi:
        parflag.append('-I'+os.path.join(pumi_prefix, 'include'))
    if enable_strumpack:
        parflag.append('-I'+os.path.join(strumpack_prefix, 'include'))

    for file in ifiles():
        if file == 'pumi.i' and not enable_pumi:
            continue
        if file == 'strumpack.i' and not enable_strumpack:
            continue
        if not check_new(file):
            continue
        command = [swig_command] + swigflag + parflag + [file]
        make_call(command)

    os.chdir(pwd)

def clean_wrapper():

    pwd = chdir(os.path.join(rootdir, 'mfem', '_ser'))
    
    wfiles = [x for x in os.listdir() if x.endswith('_wrap.cxx')]
    remove_files(wfiles)

    chdir(os.path.join(rootdir, 'mfem', '_par'))
    wfiles = [x for x in os.listdir() if x.endswith('_wrap.cxx')]
    remove_files(wfiles)

    chdir(pwd)
    
def clean_so():
    pwd =chdir(os.path.join(rootdir, 'mfem', '_ser'))
    for f in os.listdir():
        if f.endswith('.so'):
            os.remove(f)
        if f.endswith('.dylib'):
            os.remove(f)
            
    chdir(os.path.join(rootdir, 'mfem', '_par'))
    for f in os.listdir():
        if f.endswith('.so'):
            os.remove(f)
        if f.endswith('.dylib'):
            os.remove(f)
    chdir(pwd)
    
def make_mfem_wrapper(serial=True):
    '''
    compile PyMFEM wrapper code
    '''
    if dry_run or verbose:
        print("compiling wrapper code, serial="+str(serial))
    
    write_setup_local()

    if serial:
        pwd = chdir(os.path.join(rootdir, 'mfem', '_ser'))
    else:
        pwd = chdir(os.path.join(rootdir, 'mfem', '_par'))

    python = sys.executable
    command = [python, 'setup.py', 'build_ext', '--inplace']
    make_call(command)
    os.chdir(pwd)

def print_config():
    print("----configuration----")
    print(" prefix", prefix)
    print(" when needed, the dependency (mfem/hypre/metis) will be installed under " +
          prefix + "/mfem")
    print(" build mfem : " + ("Yes" if build_mfem else "No"))        
    print(" build metis : " + ("Yes" if build_metis else "No"))
    print(" build hypre : " + ("Yes" if build_hypre else "No"))
    print(" call swig wrapper : " + ("Yes" if run_swig else "No"))
    print(" build serial wrapper: " + ("Yes" if build_serial else "No"))
    print(" build parallel wrapper : " + ("Yes" if build_parallel else "No"))
    print(" c compiler : " + cc_command)
    print(" c++ compiler : " + cxx_command)
    print(" mpi-c compiler : " + mpicc_command)
    print(" mpi-c++ compiler : " + mpicxx_command)
    print("")
    
def configure_install(self):
    '''
    called when install workflow is used
    '''
    global prefix, dry_run, verbose
    global clean_swig, run_swig, swig_only
    global build_mfem, build_mfemp, build_parallel, build_serial
    global build_metis, build_hypre
    global mfems_prefix, mfemp_prefix, metis_prefix, hypre_prefix
    global cc_command, cxx_command, mpicc_command, mpicxx_command
    global metis_64
    global enable_cuda, cuda_prefix
    global enable_pumi, pumi_prefix
    global enable_strumpack, strumpack_prefix

    dry_run = bool(self.dry_run) if dry_run == -1 else dry_run
    verbose = bool(self.verbose) if verbose == -1 else verbose

    prefix = abspath(self.prefix)
    skip_ext = bool(self.skip_ext)

    swig_only = bool(self.swig)
    ext_only = bool(self.ext_only)
    build_serial = (not swig_only and not ext_only)
    run_swig = swig_only

    build_parallel = bool(self.with_parallel)     # controlls PyMFEM parallel
    metis_64 = bool(self.with_metis64)
    enable_pumi = bool(self.with_pumi)
    enable_strumpack = bool(self.with_strumpack)
    enable_cuda = bool(self.with_cuda)    

    if build_parallel:
        try:
            import mpi4py
        except ImportError:
            assert False, "Can not import mpi4py"

    if self.mfem_prefix_no_swig != '':
        self.mfem_prefix = self.mfem_prefix_no_swig

    if self.mfem_prefix != '':
        mfem_prefix = abspath(self.mfem_prefix)
        mfems_prefix = abspath(self.mfem_prefix)
        mfemp_prefix = abspath(self.mfem_prefix)

        path = os.path.join(mfem_prefix, 'lib', 'libmfem'+dylibext)
        assert os.path.exists(path), "libmfem.so is not found in the specified <path>/lib"
        build_mfem = False
        hypre_prefix = mfem_prefix
        metis_prefix = mfem_prefix

        if self.mfem_prefix_no_swig != '':
            clean_swig = False
            run_swig = False
        else:
            clean_swig = True
            run_swig = True

    else:
        build_mfem = True
        build_mfemp = build_parallel
        build_hypre = build_parallel
        build_metis = build_parallel
        hypre_prefix = os.path.join(prefix, 'mfem')
        metis_prefix = os.path.join(prefix, 'mfem')
        mfem_prefix  = os.path.join(prefix, 'mfem')
        mfems_prefix = os.path.join(prefix, 'mfem', 'ser')
        mfemp_prefix = os.path.join(prefix, 'mfem', 'par')

    if self.hypre_prefix != '':
        hypre_prefix = abspath(self.hypre_prefix)            
        path = os.path.join(hypre_prefix, 'lib', 'libHYPRE'+dylibext)
        assert os.path.exists(path), "libHYPRE.so is not found in the specified <path>/lib"
        build_hypre = False

    if self.metis_prefix != '':
        metis_prefix = abspath(self.metis_prefix)
        path = os.path.join(metis_prefix, 'lib', 'libmetis'+dylibext)
        assert os.path.exists(path), "libmetis.so is not found in the specified <path>/lib"
        build_metis = False

    if enable_pumi: run_swig = True
    if enable_strumpack : run_swig = True    
    if self.pumi_prefix != '':
        pumi_prefix = abspath(self.pumi_prefix)
    else:
        pumi_prefix = mfem_prefix

    if self.strumpack_prefix != '':
        strumpack_prefix = abspath(self.strumpack_prefix)
    else:
        strumpack_prefix = mfem_prefix

    if enable_cuda:
        nvcc = find_command('nvcc')
        cuda_prefix = os.path.dirname(os.path.dirname(nvcc))

    if self.CC != '':
        cc_command = self.CC
    if self.CXX != '':
        cxx_command = self.CXX
    if self.MPICC != '':
        mpicc_command = self.MPICC
    if self.MPICXX != '':
        mpicxx_command = self.MPICXX

    if skip_ext:
        build_metis = False
        build_hypre = False
        build_mfem = False
        build_mfemp = False        
    if ext_only:
        clean_swig = False
        run_swig = False
        build_serial = False
        build_parallel = False
    
    global is_configured
    is_configured = True

def configure_bdist(self):
    '''
    called when bdist workflow is used
    '''
    global prefix, dry_run, verbose, run_swig
    global build_mfem, build_parallel, build_serial

    global cc_command, cxx_command, mpicc_command, mpicxx_command
    global enable_pumi, pumi_prefix
    global enable_strumpack, strumpack_prefix

    dry_run = bool(self.dry_run) if dry_run == -1 else dry_run
    verbose = bool(self.verbose) if verbose == -1 else verbose


    prefix = abspath(self.bdist_dir)
    
    run_swig = False
    build_parallel = False
    build_serial = True

    global is_configured
    is_configured = True

class Install(_install):
    '''
    called when pyton setup.py install
    '''
    user_options = _install.user_options + [
        ('with-parallel', None, 'Installed both serial and parallel version'),
        ('mfem-prefix=', None, 'Specify locaiton of mfem' +
         'libmfem.so must exits under <mfem-prefix>/lib'),
        ('mfem-prefix-no-swig=', None, 'Specify locaiton of mfem' +
         'libmfem.so must exits under <mfem-prefix>/lib witout regenerating SWIG wrapper'),
        ('hypre-prefix=', None, 'Specify locaiton of hypre' +
         'libHYPRE.so must exits under <hypre-prefix>/lib'),
        ('metis-prefix=', None, 'Specify locaiton of metis'+
         'libmetis.so must exits under <metis-prefix>/lib'),
        ('swig', None, 'Run Swig'),
        ('ext-only', None, 'Build metis, hypre, mfem(C++) only'),
        ('skip-ext', None, 'Skip building metis, hypre, mfem(C++) only'),        

        ('CC=', None, 'c compiler'),
        ('CXX=', None, 'c++ compiler'),
        ('MPICC=', None, 'mpic compiler'),
        ('MPICXX=', None, 'mpic++ compiler'),
        ('with-cuda', None, 'enable cuda'),
        ('with-metis64', None, 'use 64bit int in metis'),
        ('with-pumi', None, 'enable pumi (parallel only)'),
        ('pumi-prefix=', None, 'Specify locaiton of pumi'),
        ('with-strumpack', None, 'enable strumpack (parallel only)'),
        ('strumpack-prefix=', None, 'Specify locaiton of strumpack'),
    ]

    def initialize_options(self):
        _install.initialize_options(self)

        self.swig = False
        self.ext_only = False
        self.skip_ext = False
        self.with_parallel = False
        self.mfem_prefix = ''
        self.mfem_prefix_no_swig = ''                        
        self.metis_prefix = ''
        self.hypre_prefix = ''

        self.with_cuda = False
        self.with_metis64 = False
        self.with_pumi = False
        self.pumi_prefix = ''

        self.with_strumpack = False
        self.strumpack_prefix = ''

        self.CC = ''
        self.CXX = ''
        self.MPICC = ''
        self.MPICXX = ''

    def finalize_options(self):
        if (bool(self.ext_only) and bool(self.skip_ext)):
            assert False, "skip-ext and ext-only can not use together"
        _install.finalize_options(self)
        
    def run(self):
        if not is_configured:
            configure_install(self)
            print_config()

        if swig_only:
            self.run_command("build")
        else:
            _install.run(self)

class BuildPy(_build_py):
    '''
    Called when python setup.py build_py
    '''
    user_options = _build_py.user_options
    def initialize_options(self):
        _build_py.initialize_options(self)

    def finalize_options(self):
        _build_py.finalize_options(self)

    def run(self):
        if not swig_only:            
            if build_metis:
                download('metis')
                make_metis(use_int64=metis_64)
            if build_hypre:
                download('hypre')
                cmake_make_hypre()
            mfem_downloaded = False
            if build_mfem:
                download('mfem')
                mfem_downloaded = True                
                cmake_make_mfem(serial=True)

            if build_mfemp:
                if not mfem_downloaded:
                    download('mfem')                    
                cmake_make_mfem(serial=False)
                    
        if clean_swig:
            clean_wrapper()
        if run_swig:
            generate_wrapper()
            if swig_only:
                return

        if build_serial:
            make_mfem_wrapper(serial=True)
        if build_parallel:
            make_mfem_wrapper(serial=False)
        
        _build_py.run(self)

class BdistWheel(_bdist_wheel):
    '''
    Wheel build performs serial+paralell
    '''
    def finalize_options(self):
        def _has_ext_modules(self):
            return True
        from setuptools.dist import Distribution
        #Distribution.is_pure = _is_pure
        Distribution.has_ext_modules = _has_ext_modules
        _bdist_wheel.finalize_options(self)

    def run(self):
        _bdist_wheel.run(self)        
        assert False, "bdist install is not supported, use source install"
        '''
        if not is_configured:
            print('running config')
            configure_bdist(self)
            print_config()
            
        # Ensure that there is a basic library build for bdist_egg to pull from.
        self.run_command("build")
        #_cleanup_symlinks(self)

        # Run the default bdist_wheel command
        '''
        
class Clean(_clean):
    '''
    Called when python setup.py clean
    '''
    user_options = _clean.user_options + [
        ('ext', None, 'clean exteranal dependencies)'),
        ('mfem', None, 'clean mfem'),
        ('metis', None, 'clean metis'),
        ('hypre', None, 'clean hypre'),
        ('swig', None,  'clean swig'),        
        ('all-exts', None, 'delete all externals'),
        ]

    def initialize_options(self):
        _clean.initialize_options(self)
        self.ext = False
        self.mfem = False
        self.hypre = False
        self.metis = False
        self.swig = False
        self.all_exts = False

    def run(self):
        global dry_run, verbose
        dry_run = self.dry_run
        verbose = bool(self.verbose)
        
        os.chdir(extdir)

        make_command = find_command('make')
        
        if self.ext or self.mfem:
            path = os.path.join(extdir, 'mfem', 'cmbuild_par')
            if os.path.exists(path):
                shutil.rmtree(path)
            path = os.path.join(extdir, 'mfem', 'cmbuild_ser')
            if os.path.exists(path):
                shutil.rmtree(path)
        if self.ext or self.hypre:    
            path = os.path.join(extdir, 'hypre', 'cmbuild')
            if os.path.exists(path):
                shutil.rmtree(path)
        if self.ext or self.metis:
            path = os.path.join(extdir, 'metis')
            if os.path.exists(path):
                os,chdir(path)
                command = ['make', 'clean']
                subprocess.check_call(command)                
        if self.all_exts or self.hypre:
            for xxx in ('metis', 'hypre', 'mfem'):
                path = os.path.join(extdir, xxx)
                if os.path.exists(path):
                    shutil.rmtree(path)
        if self.swig:
            clean_wrapper()

        clean_so()
        
        os.chdir(rootdir)
        _clean.run(self)

datafiles = [os.path.join('data', f) for f in os.listdir('data')]
def run_setup():
    setup_args = metadata.copy()

    setup(
        cmdclass = {'build_py': BuildPy,
                    'install': Install,
                    'bdist_wheel': BdistWheel,
                    'clean': Clean},
        install_requires=["numpy"],
        packages=find_packages(),
        extras_require={},
        package_data={'mfem._par':['*.so'], 'mfem._ser':['*.so']},
        #data_files=[('data', datafiles)],
        entry_points={},
        **setup_args)

def main():
    run_setup()

if __name__ == '__main__':
    main()

