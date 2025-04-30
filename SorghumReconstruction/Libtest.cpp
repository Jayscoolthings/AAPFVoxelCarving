#include <iostream>
#include <zlib.h>
#include <boost/version.hpp>

int main() {
	std::cout << "Zlib Version: " << zlibVersion() << std::endl;
	std::cout << "Boost Version: " << BOOST_VERSION / 1000 << "." << BOOST_VERSION % 1000 << std::endl;

	return 0;
}