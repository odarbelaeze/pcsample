#include <iostream>
#include <string>

#include <boost/program_options.hpp>
#include <voro++.hh>

namespace po = boost::program_options;
namespace vo = voro;

int main(int argc, char const *argv[])
{
	po::options_description desc("Allowed options");

	desc.add_options()
		("help", "produce help message")
		("input", po::value<std::string>(), "input file")
	;

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    if (vm.count("help"))
    {
        std::cout << desc << std::endl;
        return 0;
    }

    if (vm.count("input"))
    {
        std::cout << "input file name: "
                  << vm["input"].as<std::string>()
                  << std::endl
        ;
    }

	return 0;
}
