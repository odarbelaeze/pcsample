#include <SampleBase.hh>

SampleBase::SampleBase(
        double bx,
        double bxy,
        double by,
        double bxz,
        double byz,
        double bz)
    :
        vo::container_periodic(bx, bxy, by, bxz, byz, bz, 6, 6, 6, 4)
{
    this -> _options = "%i %q %l";
}


SampleBase::~SampleBase()
{
}


void SampleBase::setOptions(const std::string& opt)
{
    this -> _options = opt;
}


const std::string& SampleBase::getOptions() const
{
    return this -> _options;
}

