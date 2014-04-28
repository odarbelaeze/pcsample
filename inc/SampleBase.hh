#ifndef SAMPLE_BASE_HH_
#define SAMPLE_BASE_HH_

#include <iostream>
#include <voro++.hh>

namespace vo = voro;

class SampleBase : public vo::container_periodic {
    public:
        SampleBase(double, double, double, double, double, double);
        virtual ~SampleBase();

        void setOptions(const std::string&);
        const std::string& getOptions() const;

    protected:
        std::string _options;

};

#endif

