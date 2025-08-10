#include <wx/wx.h>
#include "MyProjectBase.h"
#include "MyProjectBase.cpp"
 
class MyApp : public wxApp
{
public:
    bool OnInit() override;
};
 
wxIMPLEMENT_APP(MyApp);

bool MyApp::OnInit()
{
    MyFrame *frame = new MyFrame(nullptr, wxID_ANY, "Hello World!");
    frame->Show(true);
    return true;
}
