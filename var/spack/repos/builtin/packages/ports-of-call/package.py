# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PortsOfCall(CMakePackage, CudaPackage):
    """Ports of Call: Performance Portability Utilities"""

    homepage    = "https://github.com/lanl/ports-of-call"
    url         = "https://github.com/lanl/ports-of-call/archive/refs/tags/v1.0.0.tar.gz"
    git         = "https://github.com/lanl/ports-of-call.git"

    maintainers = ['rbberger']

    version("main", branch="main")
    version('1.0.0', sha256='4f451a41baeb2f95d30760cf39279785dcd6e550b3ce5eac05ef0a258af67e03')

    variant("doc", default=False, description="Sphinx Documentation Support")
    variant("portability_strategy", description="Portability strategy backend",
            values=("Kokkos", "Cuda", "None"), multi=False, default="None")

    depends_on("cmake@3.12:")

    depends_on("py-sphinx", when="+doc")
    depends_on("py-sphinx-rtd-theme@0.4.3", when="+doc")
    depends_on("py-sphinx-multiversion", when="+doc")

    def cmake_args(self):
        args = [
            self.define_from_variant("PORTABILITY_STRATEGY", "portability_strategy")
        ]
        return args