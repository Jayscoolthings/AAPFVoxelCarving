// This script is to test if you have the Vcpkg libraries properly configured. It will simply print the versions of each package as long as they are properly installed.

#include <iostream>
#include <zlib.h>
#include <boost/version.hpp>

int main() {
	std::cout << "Zlib Version: " << zlibVersion() << std::endl;
	std::cout << "Boost Version: " << BOOST_VERSION / 1000 << "." << BOOST_VERSION % 1000 << std::endl;

	return 0;
}